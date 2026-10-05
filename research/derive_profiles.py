"""Adds public profiles that a person's own evidence already proves, without searching.
a page that the evidence of two or more different people points to is skipped: it is a company publication or an event.
so is a page whose username names the employer, and a medium author whose username does not fit the person.

usage, from the repo root: python3 research/derive_profiles.py

a profile counts when the evidence url itself names its author or owner:
- zenn.dev/<user>/articles/..., qiita.com/<user>/items/..., note.com/<user>/n/..., velog.io/@<user>/...,
  medium.com/@<user>/..., dev.to/<user>/<post>: the author's profile page.
- meetup.com/members/<id> and sessionize.com/<speaker> pages already in the evidence.
- github.com/<owner>/... or api.github.com/users/<owner>: only when GitHub says the owner is a user (not an
  organisation) whose name matches the person; its linked LinkedIn account is added too.
"""

import glob, json, re, subprocess, unicodedata
from validate import reachable

AUTHOR = [
    (re.compile(r"https?://zenn\.dev/([A-Za-z0-9_]+)/(?:articles|books|scraps)/"), "zenn", "https://zenn.dev/{}"),
    (re.compile(r"https?://qiita\.com/([A-Za-z0-9_-]+)/items/"), "qiita", "https://qiita.com/{}"),
    (re.compile(r"https?://note\.com/([A-Za-z0-9_]+)/n/"), "note", "https://note.com/{}"),
    (re.compile(r"https?://velog\.io/@([^/]+)/"), "velog", "https://velog.io/@{}"),
    (re.compile(r"https?://medium\.com/@([^/?#]+)"), "medium", "https://medium.com/@{}"),
    (re.compile(r"https?://dev\.to/([A-Za-z0-9_]+)/[^/]+"), "devto", "https://dev.to/{}"),
    (re.compile(r"https?://(?:www\.)?meetup\.com/members/(\d+)"), "meetup", "https://www.meetup.com/members/{}/"),
    (re.compile(r"https?://sessionize\.com/([a-z0-9-]+)/?$"), "sessionize", "https://sessionize.com/{}"),
]
GITHUB = re.compile(r"https?://(?:www\.)?github\.com/([A-Za-z0-9-]+)(?:/|$)|https?://api\.github\.com/users/([A-Za-z0-9-]+)")
NOT_USERS = {"orgs", "topics", "sponsors", "features", "about", "marketplace", "apps"}


def norm(s):
    return re.sub(r"[^a-z0-9 ]", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower())


def name_matches(person_name, github_name, login):
    tok = [t for t in norm(re.sub(r"\(.*?\)", "", person_name)).split() if len(t) > 1]
    if len(tok) < 2:  # a handle-only record matches its own login
        return norm(person_name).replace(" ", "") == login.lower()
    have = norm(github_name).replace(" ", "") + " " + login.lower()
    return tok[0] in have and tok[-1] in have


_gh = {}


def github_user(login):
    if login not in _gh:
        out = subprocess.run(["gh", "api", f"users/{login}"], capture_output=True, text=True).stdout
        user = json.loads(out) if out.strip().startswith("{") else {}
        social = []
        if user.get("type") == "User":
            s = subprocess.run(["gh", "api", f"users/{login}/social_accounts"], capture_output=True, text=True).stdout
            social = json.loads(s) if s.strip().startswith("[") else []
        _gh[login] = (user, social)
    return _gh[login]


COMPANY_WORDS = {"tech", "data", "blog", "dev", "jp", "inc", "engineering", "team", "official", "digital", "media"}


def company_page(slug, company):
    """the username is the employer's name, as in zenn.dev/pixiv for pixiv or zenn.dev/cybozu_data for Cybozu: a company publication.
    a personal account with a company prefix, such as qiita.com/nttd-maruyamat, is not."""
    stem = "".join(w for w in re.split(r"[_\-.]", slug.lower()) if w not in COMPANY_WORDS)
    emp = [t for t in norm(company).split() if len(t) >= 3 and t not in {"the", "inc", "group", "holdings", "formerly"}]
    return bool(stem) and (stem in "".join(norm(company).split()) or any((stem.startswith(t) or stem.endswith(t)) and len(stem) - len(t) <= 4 for t in emp))


def own_author(kind, slug, p):
    """a medium post is often someone else writing about the talk, so its author counts only when the username fits the person."""
    if kind != "medium":
        return True
    from harvest_profiles import handles, matches_name, same_handle, slug_fits_name, tokens
    return slug_fits_name(slug, p) or matches_name(slug, tokens(p["name"])) or any(same_handle(slug, h) for h in handles(p))


def author_pages(p):
    return {template.format(m.group(1)) for u in (e.get("url") or "" for e in p["speaker_evidence"] + p["evidence"])
            for pattern, kind, template in AUTHOR for m in [pattern.search(u)] if m}


def main():
    added = {}
    files = sorted(glob.glob("*/*_dbt_companies.json"))
    # a page that several people's evidence points to is a company publication or an event, not one person's profile
    owners = {}
    for f in files:
        for c in json.load(open(f))["companies"]:
            for p in c["people"]:
                for url in author_pages(p):
                    owners.setdefault(url, set()).add(norm(p["name"]).strip())
    shared = {url for url, names in owners.items() if len(names) > 1}
    for f in files:
        raw = open(f).read()
        d = json.loads(raw)
        n = 0
        for c in d["companies"]:
            for p in c["people"]:
                have = {u["url"] for u in p["profile_urls"]}
                urls = [e.get("url") or "" for e in p["speaker_evidence"] + p["evidence"]]
                for u in urls:
                    for pattern, kind, template in AUTHOR:
                        m = pattern.search(u)
                        if m:
                            url = template.format(m.group(1))
                            if url not in have and url not in shared and not company_page(m.group(1), c["name"]) and own_author(kind, m.group(1), p):
                                p["profile_urls"].append({"type": kind, "url": url, "source": u})
                                have.add(url)
                                n += 1
                    m = GITHUB.search(u)
                    login = m and (m.group(1) or m.group(2))
                    if login and login.lower() not in NOT_USERS:
                        user, social = github_user(login)
                        if user.get("type") == "User" and name_matches(p["name"], user.get("name"), login):
                            url = user["html_url"]
                            if url not in have:
                                p["profile_urls"].append({"type": "github", "url": url, "source": u})
                                have.add(url)
                                n += 1
                            for a in social:
                                li = a.get("url", "")
                                if "linkedin.com/in/" in li and li not in p["linkedin_urls"]:
                                    p["linkedin_urls"].append(li)
                                    p["has_linkedin"] = True
                                    p["linkedin_confidence"] = "high"
                                    p["evidence"].append({"url": li, "note": f"linkedin profile linked from github.com/{login} social accounts"})
        allp = [p for c in d["companies"] for p in c["people"]]
        d["metadata"]["counts"]["people_with_linkedin"] = sum(p["has_linkedin"] for p in allp)
        d["metadata"]["counts"]["people_with_contact"] = sum(map(reachable, allp))
        open(f, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
        added[f] = (n, d["metadata"]["counts"]["people_with_contact"], len(allp))
    for f, (n, contact, total) in added.items():
        print(f"{f.split('/')[0]:16} +{n:3} profiles  reachable {contact}/{total}")


if __name__ == "__main__":
    main()
