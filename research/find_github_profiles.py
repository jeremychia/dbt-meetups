"""Finds GitHub profiles for people with no contact yet, by the handle the record gives or full-name search, keeping only verified matches.

usage, from the repo root: python3 research/find_github_profiles.py [<city folder> ...]

a candidate counts only when it is the single result that GitHub's own profile ties to what we know:
its company, bio or blog names the person's employer, or its location names the chapter's city and its bio is
about data. its linked LinkedIn account is added too. needs a logged-in gh; searches are paced to the API limit.
"""

import glob, json, re, subprocess, sys, time, unicodedata
from harvest_profiles import handles
from validate import reachable

NATIVE = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af]")  # chinese, japanese or korean script
DATA = re.compile(r"\b(data|analytics|dbt|sql|bi|warehouse|etl|engineer|scientist)\b", re.I)
GENERIC = {"independent", "no", "company", "employer", "not", "identified", "stated", "the", "and", "group", "inc", "gmbh", "ltd", "labs", "data", "ab", "as", "sa", "bv", "co"}


def norm(s):
    return re.sub(r"[^a-z0-9 ]", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower())


def gh(path, *params):
    # query text goes in -f params so gh encodes it; a raw space or quote in the path makes the call hang
    args = ["gh", "api", "-X", "GET", path] + [x for p in params for x in ("-f", p)]
    for attempt in range(4):
        try:
            r = subprocess.run(args, capture_output=True, text=True, timeout=30)
        except subprocess.TimeoutExpired:
            continue
        if r.returncode == 0:
            return json.loads(r.stdout)
        if "rate limit" in (r.stderr + r.stdout).lower():
            time.sleep(60)
            continue
        return None
    return None


def employer_tokens(company):
    return {t for t in norm(company).split() if len(t) > 3 and t not in GENERIC}


# --country: also accept a profile whose location names the chapter's country, but only when its name is unique on GitHub
COUNTRY = {"amsterdam": "netherlands nederland", "atlanta": "usa united states", "baltics": "lithuania lietuva", "belgium": "belgium belgique belgie",
           "berlin_planning": "germany deutschland", "boston": "usa united states", "copenhagen": "denmark danmark", "dusseldorf": "germany deutschland",
           "kuala_lumpur": "malaysia", "london": "uk united kingdom england", "melbourne": "australia", "montreal": "canada quebec",
           "munich": "germany deutschland bavaria bayern", "new_york": "usa united states", "paris": "france", "san_francisco": "usa united states california",
           "seattle": "usa united states washington", "seoul": "korea", "singapore": "singapore", "sofia": "bulgaria", "stockholm": "sweden sverige",
           "sydney": "australia", "taipei": "taiwan", "tokyo": "japan", "toronto": "canada ontario"}


def verified(user, employer, city_words):
    text = norm(" ".join(str(user.get(k) or "") for k in ("company", "bio", "blog")))
    if employer and employer & set(text.split()):
        return True
    loc = norm(user.get("location"))
    return bool(city_words & set(loc.split())) and bool(DATA.search(user.get("bio") or ""))


def main(folders):
    by_country = "--country" in folders
    folders = [x for x in folders if x != "--country"]
    files = [f for f in sorted(glob.glob("*/*_dbt_companies.json")) if not folders or f.split("/")[0] in folders]
    for f in files:
        raw = open(f).read()
        d = json.loads(raw)
        city_words = set(norm(d["metadata"]["region"]).split()) - {"dbt", "meetup", "the", "and"}
        country_words = set(COUNTRY.get(f.split("/")[0], "").split())
        n = 0
        for c in d["companies"]:
            employer = employer_tokens(c["name"])
            for p in c["people"]:
                if reachable(p) or any(u["type"] == "github" for u in p["profile_urls"]):
                    continue
                tok = [t for t in norm(re.sub(r"\(.*?\)", "", p["name"])).split() if len(t) > 1]
                native = re.sub(r"\s*\(.*?\)", "", p["name"]).strip()
                good = []
                for h in handles(p):  # a handle the record gives may be the github login; it still has to name the employer or city
                    user = gh(f"users/{h}") or {}
                    if user.get("type") == "User" and verified(user, employer, city_words):
                        good.append(user)
                if not good and (len(tok) >= 2 or NATIVE.search(native)):
                    query = native if NATIVE.search(native) else " ".join(tok)
                    res = gh("search/users", f'q=fullname:"{query}"', "per_page=5") or {}
                    time.sleep(2.2)  # search allows 30 calls a minute
                    if not res.get("items") or res.get("total_count", 0) > 15:  # too common a name to verify
                        continue
                    for item in res["items"][:5]:
                        user = gh(f"users/{item['login']}") or {}
                        full = norm(user.get("name"))
                        named = query in (user.get("name") or "") if NATIVE.search(native) else (tok[0] in full and tok[-1] in full)
                        if user.get("type") != "User" or not named:
                            continue
                        in_country = res.get("total_count") == 1 and country_words & set(norm(user.get("location")).split()) and DATA.search(user.get("bio") or "")
                        if verified(user, employer, city_words) or (by_country and in_country):
                            good.append(user)
                if len(good) != 1:
                    continue
                user = good[0]
                p["profile_urls"].append({"type": "github", "url": user["html_url"], "source": f"github user search, profile names {user.get('company') or user.get('location')}"})
                for a in gh(f"users/{user['login']}/social_accounts") or []:
                    li = a.get("url", "")
                    if "linkedin.com/in/" in li and li not in p["linkedin_urls"]:
                        p["linkedin_urls"].append(li)
                        p["has_linkedin"] = True
                        p["linkedin_confidence"] = "high"
                        p["evidence"].append({"url": li, "note": f"linkedin profile linked from github.com/{user['login']} social accounts"})
                n += 1
        allp = [p for c in d["companies"] for p in c["people"]]
        d["metadata"]["counts"]["people_with_linkedin"] = sum(p["has_linkedin"] for p in allp)
        d["metadata"]["counts"]["people_with_contact"] = sum(map(reachable, allp))
        open(f, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
        print(f"{f.split('/')[0]:16} +{n:3} github profiles  reachable {d['metadata']['counts']['people_with_contact']}/{len(allp)}", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
