"""Finds LinkedIn profile links for people from pages already tied to them, without searching.

usage, from the repo root:
  python3 research/harvest_linkedin.py fetch <cache dir>   # reads each person's evidence pages and GitHub social accounts
  python3 research/harvest_linkedin.py apply <cache dir>   # writes matched links into the city files

a link counts only when it is linkedin.com/in/<slug>, appears on a page in the person's own evidence, and matches the person:
the slug or the link text contains the person's first and last name, and no other person's name on that page matches it.
links from the person's own GitHub profile are high confidence; links from event, speaker or author pages are medium.
"""

import concurrent.futures, glob, hashlib, json, os, re, subprocess, sys, unicodedata, urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
LINK = re.compile(r"""(?:https?:)?//(?:[a-z]{2,3}\.)?linkedin\.com/in/([A-Za-z0-9\-_%.]+)/?(?:["'\s<)?#]|$)""", re.I)
ANCHOR = re.compile(r"""<a[^>]+href=["']([^"']*linkedin\.com/in/[^"']+)["'][^>]*>(.*?)</a>""", re.I | re.S)
SKIP = ("linkedin.com", "medium.com")  # medium answers 429 to scripted fetches


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", " ", s)


def tokens(name):
    t = [x for x in norm(re.sub(r"\(.*?\)", "", name)).split() if len(x) > 1]
    return (t[0], t[-1]) if len(t) >= 2 else None


def people():
    for f in sorted(glob.glob("*/*_dbt_companies.json")):
        for c in json.load(open(f))["companies"]:
            for p in c["people"]:
                yield f, p


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
            req = urllib.request.Request(url, headers={"user-agent": UA})
            text = urllib.request.urlopen(req, timeout=20).read(3_000_000).decode("utf-8", "ignore")
    except Exception:
        text = ""
    open(path, "w", encoding="utf-8").write(text)
    return text


def github_links(login):
    try:
        out = subprocess.run(["gh", "api", f"users/{login}/social_accounts"], capture_output=True, text=True, timeout=30).stdout
        return [a["url"] for a in json.loads(out or "[]") if "linkedin.com/in/" in a.get("url", "")]
    except Exception:
        return []


def matches(slug_or_text, tok):
    s = norm(slug_or_text).replace(" ", "")
    return tok[0] in s and tok[1] in s


def fetch(cache):
    os.makedirs(cache, exist_ok=True)
    jobs, gh = set(), {}
    for f, p in people():
        if p["linkedin_urls"]:
            continue
        for e in p["speaker_evidence"] + p["evidence"]:
            u = e.get("url") or ""
            m = re.match(r"https?://(?:www\.)?github\.com/([A-Za-z0-9-]+)/?$", u) or re.match(r"https?://api\.github\.com/users/([A-Za-z0-9-]+)", u)
            if m:
                gh.setdefault(m.group(1), None)
            elif u.startswith("http") and not any(d in u for d in SKIP):
                jobs.add(u)
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        list(pool.map(lambda u: page_text(u, cache), sorted(jobs)))
    for login in gh:
        gh[login] = github_links(login)
    json.dump(gh, open(os.path.join(cache, "github.json"), "w"))
    print(f"fetched {len(jobs)} pages and {len(gh)} github accounts into {cache}")


def candidates(cache):
    gh = json.load(open(os.path.join(cache, "github.json")))
    by_page = {}  # page url -> names of everyone whose evidence uses it, so a link can be checked against all of them
    for f, p in people():
        for e in p["speaker_evidence"] + p["evidence"]:
            by_page.setdefault(e.get("url"), set()).add(p["name"])
    found = {}
    for f, p in people():
        tok = tokens(p["name"])
        if p["linkedin_urls"] or not tok:
            continue
        for e in p["speaker_evidence"] + p["evidence"]:
            u = e.get("url") or ""
            m = re.match(r"https?://(?:www\.)?github\.com/([A-Za-z0-9-]+)/?$", u) or re.match(r"https?://api\.github\.com/users/([A-Za-z0-9-]+)", u)
            if m and gh.get(m.group(1)):
                found[(f, p["id"])] = (gh[m.group(1)][0], f"github.com/{m.group(1)} social accounts", "high")
                break
            if not u.startswith("http") or any(d in u for d in SKIP):
                continue
            text = page_text(u, cache)
            if "linkedin.com/in/" not in text:
                continue
            links = {}
            for href, label in ANCHOR.findall(text):
                sm = LINK.search(href + '"')
                if sm:
                    links[sm.group(1)] = links.get(sm.group(1), "") + " " + re.sub(r"<[^>]+>", " ", label)
            for sm in LINK.finditer(text):
                links.setdefault(sm.group(1), "")
            hits = [s for s, label in links.items() if matches(s, tok) or matches(label, tok)]
            others = [n for n in by_page.get(u, ()) if n != p["name"] and tokens(n)]
            hits = [s for s in hits if not any(matches(s, tokens(n)) for n in others if tokens(n) != tok)]
            if len(set(hits)) == 1:
                found[(f, p["id"])] = (f"https://www.linkedin.com/in/{hits[0].rstrip('/')}/", u, "medium")
                break
    return found


def apply(cache):
    found = candidates(cache)
    by_file = {}
    for (f, pid), v in found.items():
        by_file.setdefault(f, {})[pid] = v
    total = 0
    for f, hits in sorted(by_file.items()):
        raw = open(f).read()
        d = json.loads(raw)
        for c in d["companies"]:
            for p in c["people"]:
                if p["id"] in hits and not p["linkedin_urls"]:
                    url, source, conf = hits[p["id"]]
                    p["linkedin_urls"] = [url]
                    p["has_linkedin"] = True
                    p["linkedin_confidence"] = conf
                    p["evidence"].append({"url": url, "note": f"linkedin profile linked from {source}"})
        allp = [p for c in d["companies"] for p in c["people"]]
        d["metadata"]["counts"]["people_with_linkedin"] = sum(p["has_linkedin"] for p in allp)
        open(f, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
        total += len(hits)
        print(f"{f}: {len(hits)} linkedin profiles added")
    print(f"total {total}")


if __name__ == "__main__":
    {"fetch": fetch, "apply": apply}[sys.argv[1]](sys.argv[2])
