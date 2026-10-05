"""Finds public profile links for people from pages already tied to them, without searching.

usage, from the repo root:
  python3 research/harvest_profiles.py fetch <cache dir>   # reads each person's evidence pages and GitHub social accounts
  python3 research/harvest_profiles.py check <cache dir>   # lists the matches, and how often they agree with links already on file
  python3 research/harvest_profiles.py apply <cache dir>   # writes matched links into the city files

a link counts only when it appears on a page in the person's own evidence and one of these ties it to the person:
- name: the slug or link text contains the person's first and last name, and no other person on that page matches it.
- handle: the username equals the handle the record gives, e.g. "kayo (tshizuku03)" and x.com/tshizuku03.
- nearby: it is the profile link closest to the person's name on the page, no other known person's name is closer,
  and the slug fits the name (see slug_fits_name).
- the page's own data: bevy (snowflake, tableau and google developer group events) and luma store each speaker's or
  host's name next to their linkedin and x usernames. those count under the name rule, with the stored name as the link text.
- own profile: the person's own github, qiita or zenn account lists the link, or their sessionize, personal site or
  other profile page carries it under the own page rule.
- own page: the evidence page links the person's full name to their own page on the same site (a speaker, author or
  cv page), and that page has exactly one link of the type. outside linkedin the slug must also fit the name,
  since x and github links on those pages are often the organiser's own account.
a person gets a link of a type only when exactly one link of that type matches.
links from the person's own GitHub social accounts are high confidence; links from event, speaker or author pages are medium.
"""

import concurrent.futures, glob, hashlib, html, json, os, re, subprocess, sys, unicodedata, urllib.parse, urllib.request
from collections import Counter
from validate import reachable

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
SKIP = ("linkedin.com", "medium.com")  # medium answers 429 to scripted fetches
NEAR = 300  # characters between a name and its profile link on event and speaker pages
PROFILE = [  # type, pattern, canonical url
    ("linkedin", re.compile(r"(?:[a-z]{2,3}\.)?linkedin\.com/in/([A-Za-z0-9\-_%.]+)", re.I), "https://www.linkedin.com/in/{}/"),
    ("x", re.compile(r"(?:www\.)?(?:x|twitter)\.com/(?!intent|share|home|search|hashtag|i/)@?([A-Za-z0-9_]{2,15})(?![A-Za-z0-9_/])", re.I), "https://x.com/{}"),
    ("bluesky", re.compile(r"bsky\.app/profile/([A-Za-z0-9.\-]+)", re.I), "https://bsky.app/profile/{}"),
    ("sessionize", re.compile(r"sessionize\.com/(?!api|app|s/)([A-Za-z0-9\-_.]+)/?(?![A-Za-z0-9\-_./])", re.I), "https://sessionize.com/{}"),
    ("github", re.compile(r"github\.com/(?!orgs|sponsors|topics|features|about)([A-Za-z0-9\-]+)/?(?![A-Za-z0-9\-_./])", re.I), "https://github.com/{}"),
]
URL = re.compile(r"""https?://[^\s"'<>)\]]+""")
OWN = re.compile(r"""<a\b[^>]*?href=["']([^"']+)["'][^>]*>(.*?)</a>""", re.I | re.S)
TAG = re.compile(r"""<a\b[^>]*?href=["']([^"']+)["'][^>]*>(.*?)</a>|<script.*?</script>|<style.*?</style>|<[^>]+>""", re.I | re.S)


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", " ", s)


def fold(text):
    """lowercases and strips accents one character at a time, so positions still line up with the original text."""
    out = []
    for ch in text:
        a = unicodedata.normalize("NFKD", ch).encode("ascii", "ignore").decode()
        out.append(a[0].lower() if a and a[0].isalnum() else (ch if ch.isalpha() else " "))
    return "".join(out)


def tokens(name):
    t = [x for x in norm(re.sub(r"\(.*?\)", "", name)).split() if len(x) > 1]
    return (t[0], t[-1]) if len(t) >= 2 else None


def handles(p):
    """usernames the record itself gives: a handle in parentheses, a one-word name, or an id with no spaces in the name."""
    out = set(re.findall(r"\(([A-Za-z0-9_.\-]{3,})\)", p["name"]))
    if re.fullmatch(r"[A-Za-z0-9_.\-]{3,}", p["name"].strip()):
        out.add(p["name"].strip())
    return out


def same_handle(a, b):
    return a.lower().replace("-", "_") == b.lower().replace("-", "_")


def people():
    for f in sorted(glob.glob("*/*_dbt_companies.json")):
        for c in json.load(open(f))["companies"]:
            for p in c["people"]:
                yield f, p


def evidence_urls(p):
    return [e.get("url") or "" for e in p["speaker_evidence"] + p["evidence"]]


def own_pages(p, cache):
    """same-site pages that an evidence page links from the person's full name, such as a speaker or author page."""
    tok, out = tokens(p["name"]), []
    if not tok:
        return out
    for u in evidence_urls(p):
        if not u.startswith("http") or any(d in u for d in SKIP):
            continue
        site = urllib.parse.urlparse(u).netloc.split(".")[-2:]
        for href, label in OWN.findall(page_text(u, cache)):
            words = norm(re.sub(r"<[^>]+>", " ", label)).split()
            full = urllib.parse.urljoin(u, html.unescape(href)).split("#")[0]
            if (len(words) <= 5 and tok[0] in words and tok[1] in words and full.startswith("http")
                    and urllib.parse.urlparse(full).netloc.split(".")[-2:] == site and full.rstrip("/") != u.rstrip("/") and full not in out):
                out.append(full)
    return out


def github_login(u):
    m = re.match(r"https?://(?:www\.)?github\.com/([A-Za-z0-9-]+)/?$", u) or re.match(r"https?://api\.github\.com/users/([A-Za-z0-9-]+)", u)
    return m.group(1) if m else None


def page_text(url, cache):
    path = os.path.join(cache, hashlib.sha1(url.encode()).hexdigest() + ".txt")
    if os.path.exists(path):
        return open(path, encoding="utf-8", errors="ignore").read()
    text = ""
    try:
        m = re.search(r"meetup\.com/[^/]+/events/(\d+)", url)
        if m:  # meetup pages render client-side; the gql2 api returns the event description
            body = json.dumps({"query": "query($id:ID!){event(id:$id){description}}", "variables": {"id": m.group(1)}}).encode()
            req = urllib.request.Request("https://www.meetup.com/gql2", body, {"content-type": "application/json", "user-agent": UA})
            text = (json.load(urllib.request.urlopen(req, timeout=20)).get("data") or {}).get("event", {}).get("description") or ""
        else:
            req = urllib.request.Request(url, headers={"user-agent": UA, "accept-language": "en"})
            text = urllib.request.urlopen(req, timeout=20).read(3_000_000).decode("utf-8", "ignore")
    except Exception:
        text = ""
    open(path, "w", encoding="utf-8").write(text)
    return text


def github_social(login):
    """the accounts a github user lists on their profile, including the x username field."""
    try:
        out = subprocess.run(["gh", "api", f"users/{login}/social_accounts"], capture_output=True, text=True, timeout=30).stdout
        user = subprocess.run(["gh", "api", f"users/{login}"], capture_output=True, text=True, timeout=30).stdout
        x = (json.loads(user or "{}") or {}).get("twitter_username")
        return [a["url"] for a in json.loads(out or "[]")] + ([f"https://x.com/{x}"] if x else [])
    except Exception:
        return []


def profile_api(url):
    """the api url for a qiita or zenn profile, whose json holds the user's own x and linkedin usernames."""
    m = re.match(r"https?://qiita\.com/([A-Za-z0-9_-]+)/?$", url)
    if m:
        return f"https://qiita.com/api/v2/users/{m.group(1)}"
    m = re.match(r"https?://zenn\.dev/([A-Za-z0-9_]+)/?$", url)
    return f"https://zenn.dev/api/users/{m.group(1)}" if m else None


def api_links(text):
    try:
        d = json.loads(text or "{}")
    except ValueError:
        return []
    d = d.get("user", d) if isinstance(d, dict) else {}
    out = []
    if d.get("twitter_screen_name") or d.get("twitter_username"):
        out.append("https://x.com/" + (d.get("twitter_screen_name") or d.get("twitter_username")))
    if d.get("linkedin_id"):
        out.append("https://www.linkedin.com/in/" + d["linkedin_id"])
    if d.get("github_login_name") or d.get("github_username"):
        out.append("https://github.com/" + (d.get("github_login_name") or d.get("github_username")))
    return out


OWN_TYPES = {"sessionize", "website", "velog", "devto", "note", "substack"}  # profile pages to read like the person's own page


def own_profiles(p):
    return [u["url"] for u in p["profile_urls"] if u["type"] in OWN_TYPES and not any(d in u["url"] for d in SKIP)]


def classify(url):
    for kind, pat, canon in PROFILE:
        m = pat.search(url)
        if m:
            return kind, m.group(1).rstrip("/"), canon.format(m.group(1).rstrip("/"))
    return None


def embedded(text):
    """(name, profile url) pairs from speaker and host records that bevy and luma pages carry in their page data."""
    out = []
    for m in re.finditer(r'"first_name":"([^"]*)","last_name":"([^"]*)"', text):  # bevy speakers
        rec = text[m.end():m.end() + 3000].split('"first_name":')[0]
        name = json.loads(f'"{m.group(1)} {m.group(2)}"')
        li = re.search(r'"personal_linkedin_page":"([^"]+)"', rec)
        tw = re.search(r'"personal_twitter":"([^"]+)"', rec)
        if li:
            out.append((name, li.group(1) if "linkedin.com" in li.group(1) else "https://www.linkedin.com/in/" + li.group(1).strip("/")))
        if tw:
            out.append((name, tw.group(1) if "/" in tw.group(1) else "https://x.com/" + tw.group(1).lstrip("@")))
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', text, re.S)
    if m and "luma" in text[:5000].lower():
        def walk(o):
            if isinstance(o, dict):
                if isinstance(o.get("name"), str):
                    if (o.get("linkedin_handle") or "").startswith("/in/"):
                        out.append((o["name"], "https://www.linkedin.com" + o["linkedin_handle"]))
                    if o.get("twitter_handle"):
                        out.append((o["name"], "https://x.com/" + o["twitter_handle"].lstrip("@")))
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        try:
            walk(json.loads(m.group(1)))
        except ValueError:
            pass
    return out


def links_on(text):
    """the page as plain text, plus every profile link with its position in that text and its link text."""
    plain, links, last = [], [], 0
    for m in TAG.finditer(text):
        plain.append(html.unescape(text[last:m.start()]))
        pos = sum(map(len, plain))
        if m.group(1):
            label = html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))
            c = classify(m.group(1))
            if c:
                links.append((pos, c, label))
            plain.append(" " + label + " ")
        else:
            plain.append(" ")
        last = m.end()
    plain.append(html.unescape(text[last:]))
    plain = "".join(plain)
    for name, url in embedded(text):
        c = classify(url)
        if c:
            links.append((len(plain), c, name))
            plain += f" {name} "
    for m in URL.finditer(plain):  # bare links, as in meetup descriptions
        c = classify(m.group(0))
        if c and not any(abs(p - m.start()) < 5 and c[2] == x[2] for p, x, _ in links):
            links.append((m.start(), c, ""))
    return plain, sorted(links, key=lambda x: x[0])


def name_spans(folded, p):
    tok = tokens(p["name"])
    pats = []
    if tok:
        f, l = map(re.escape, tok)
        pats += [rf"(?<![a-z0-9]){f}[a-z]*\W{{1,3}}(?:[a-z.]+\W{{1,3}}){{0,2}}{l}(?![a-z0-9])", rf"(?<![a-z0-9]){l}\W{{1,3}}{f}(?![a-z0-9])"]
    native = re.sub(r"\s*\(.*?\)", "", p["name"]).strip()
    if re.search(r"[぀-ヿ一-鿿가-힯]", native):
        pats.append(re.escape(native))
    pats += [rf"(?<![a-z0-9_]){re.escape(h)}(?![a-z0-9_])" for h in handles(p)]
    return [(m.start(), m.end()) for pat in pats for m in re.finditer(pat, folded)]


def slug_fits_name(slug, p):
    """the slug is the first name plus initials or the start of a later name (konradmal, taislaurindo),
    a short first name with the last name (jennlisborg), or the last name with at most three letters around it
    (dnedev, letourmy). nafisemirzaei does not fit zahra mirzaei."""
    s = re.sub(r"[^a-z]", "", norm(urllib.parse.unquote(slug)))
    t = [x for x in norm(re.sub(r"\(.*?\)", "", p["name"])).split() if len(x) > 1]
    if len(t) < 2:
        return False
    if s.startswith(t[0]):
        rest = s[len(t[0]):]
        return len(rest) <= 4 or any(rest.startswith(x[:2]) for x in t[1:])
    if s.startswith(t[0][:3]) and t[-1] in s:  # a short first name: jennlisborg
        return True
    return bool(re.fullmatch(rf"[a-z]{{0,3}}{re.escape(t[-1])}[a-z]{{0,3}}", s))


def matches_name(text, tok):
    s = norm(urllib.parse.unquote(text)).replace(" ", "")
    return bool(tok) and tok[0] in s and tok[1] in s


def fetch(cache):
    os.makedirs(cache, exist_ok=True)
    jobs, gh = set(), {}
    for f, p in people():  # everyone, so check can compare the rules with links already on file
        for u in evidence_urls(p) + [x["url"] for x in p["profile_urls"] if x["type"] == "github"]:
            login = github_login(u)
            if login:
                gh.setdefault(login, None)
            elif u.startswith("http") and not any(d in u for d in SKIP):
                jobs.add(u)
        jobs |= set(own_profiles(p)) | {a for a in map(profile_api, (x["url"] for x in p["profile_urls"])) if a}
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        list(pool.map(lambda u: page_text(u, cache), sorted(jobs)))
        own = sorted({u for f, p in people() for u in own_pages(p, cache)})
        list(pool.map(lambda u: page_text(u, cache), own))
    for login in gh:
        gh[login] = github_social(login)
    json.dump(gh, open(os.path.join(cache, "github.json"), "w"))
    print(f"fetched {len(jobs)} pages, {len(own)} own pages and {len(gh)} github accounts into {cache}")


def candidates(cache, everyone=False):
    """{(file, person id): {type: (url, source, confidence, rule)}} for people still missing that type, or everyone when checking."""
    gh = json.load(open(os.path.join(cache, "github.json")))
    on_page = {}  # page url -> everyone whose evidence uses it, so a link can be checked against all of them
    for f, p in people():
        for u in evidence_urls(p):
            on_page.setdefault(u, {})[p["id"]] = p
    parsed, found = {}, {}
    for f, p in people():
        tok, hs = tokens(p["name"]), handles(p)
        hits = {}  # type -> {url: (source, confidence, rule)}
        mine_pages = set(own_pages(p, cache)) | set(own_profiles(p))
        for prof in p["profile_urls"]:  # the person's own github, qiita or zenn account lists their other accounts
            login = github_login(prof["url"]) if prof["type"] == "github" else None
            listed = gh.get(login) or [] if login else api_links(page_text(profile_api(prof["url"]), cache)) if profile_api(prof["url"]) else []
            for s in listed:
                c = classify(s)
                if c and c[0] != prof["type"]:
                    hits.setdefault(c[0], {})[c[2]] = (f"{prof['url']} profile", "high", "own profile")
        for u in evidence_urls(p) + sorted(mine_pages):
            login = github_login(u)
            if login and gh.get(login):
                for s in gh[login]:
                    c = classify(s)
                    if c and c[0] != "github":
                        hits.setdefault(c[0], {})[c[2]] = (f"github.com/{login} social accounts", "high", "github")
                continue
            if not u.startswith("http") or any(d in u for d in SKIP):
                continue
            if u not in parsed:
                text = page_text(u, cache)
                parsed[u] = links_on(text) if re.search(r"linkedin\.com/in/|x\.com/|twitter\.com/|bsky\.app|sessionize\.com/|github\.com/|personal_linkedin_page|linkedin_handle", text) else ("", [])
            plain, links = parsed[u]
            if not links:
                continue
            folded = fold(plain)
            others = [o for oid, o in on_page.get(u, {}).items() if oid != p["id"]]
            mine = name_spans(folded, p)
            theirs = [s for o in others for s in name_spans(folded, o)]
            for pos, (kind, slug, canon), label in links:
                if any(matches_name(slug, tokens(o["name"])) or matches_name(label, tokens(o["name"])) for o in others if tokens(o["name"]) != tok):
                    continue
                rule = None
                if matches_name(slug, tok) or matches_name(label, tok):
                    rule = "name"
                elif u in mine_pages and sum(x[0] == kind for _, x, _ in links) == 1 and (kind == "linkedin" or slug_fits_name(slug, p)):
                    rule = "own page"
                elif any(same_handle(slug, h) for h in hs):
                    rule = "handle"
                elif mine and slug_fits_name(slug, p):
                    d = min(min(abs(pos - a), abs(pos - b)) for a, b in mine)
                    d_other = min([min(abs(pos - a), abs(pos - b)) for a, b in theirs] or [10**9])
                    same = [q for q, x, _ in links if x[0] == kind and min(min(abs(q - a), abs(q - b)) for a, b in mine) < d]
                    if d <= NEAR and d < d_other and not same:
                        rule = "nearby"
                if rule:
                    hits.setdefault(kind, {}).setdefault(canon, (u, "medium", rule))
        out = {k: (url, *v) for k, urls in hits.items() if len(urls) == 1 for url, v in urls.items()}
        if not everyone:  # a link already on file is not new
            have = {classify(u)[2] for u in p["linkedin_urls"] + [x["url"] for x in p["profile_urls"]] if classify(u)}
            out = {k: v for k, v in out.items() if v[0] not in have}
        if not everyone:
            if p["has_linkedin"]:
                out.pop("linkedin", None)
            if reachable(p):
                out = {k: v for k, v in out.items() if k == "linkedin"}
        if out:
            found[(f, p["id"])] = out
    return found


def check(cache):
    """lists new matches, and measures the rules against linkedin links already on file."""
    found = candidates(cache, everyone=True)
    agree, disagree = Counter(), []
    known = {(f, p["id"]): p for f, p in people()}
    for key, hits in sorted(found.items()):
        p = known[key]
        url, source, conf, rule = hits.get("linkedin", (None,) * 4)
        if url and p["has_linkedin"]:
            slugs = {classify(u)[1].lower() for u in p["linkedin_urls"] if classify(u)}
            if classify(url)[1].lower() in slugs:
                agree[rule] += 1
            else:
                disagree.append((key, rule, url, p["linkedin_urls"]))
    print(f"agree with links on file, by rule: {dict(agree)}; disagree: {len(disagree)}")
    for key, rule, url, have in disagree:
        print(f"  disagree {key[1]} ({rule}): {url} vs {have}")
    new = candidates(cache)
    for (f, pid), hits in sorted(new.items()):
        for kind, (url, source, conf, rule) in hits.items():
            print(f"new {f.split('/')[0]}/{pid} {kind} ({rule}): {url}  from {source}")
    print(f"{sum(len(h) for h in new.values())} new links for {len(new)} people")


def apply(cache):
    by_file = {}
    for (f, pid), hits in candidates(cache).items():
        by_file.setdefault(f, {})[pid] = hits
    total = 0
    for f, found in sorted(by_file.items()):
        raw = open(f).read()
        d = json.loads(raw)
        for c in d["companies"]:
            for p in c["people"]:
                for kind, (url, source, conf, rule) in found.get(p["id"], {}).items():
                    note = f"{kind} profile linked from {source} ({rule} match)"
                    if kind == "linkedin":
                        p["linkedin_urls"] = [url]
                        p["has_linkedin"] = True
                        p["linkedin_confidence"] = conf
                    else:
                        p["profile_urls"].append({"type": kind, "url": url, "source": source})
                    p["evidence"].append({"url": url, "note": note})
        allp = [p for c in d["companies"] for p in c["people"]]
        m = d["metadata"]["counts"]
        m["people_with_linkedin"] = sum(p["has_linkedin"] for p in allp)
        m["people_with_contact"] = sum(map(reachable, allp))
        open(f, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
        n = sum(len(h) for h in found.values())
        total += n
        print(f"{f}: {n} profile links added")
    print(f"total {total}")


if __name__ == "__main__":
    {"fetch": fetch, "check": check, "apply": apply}[sys.argv[1]](sys.argv[2])
