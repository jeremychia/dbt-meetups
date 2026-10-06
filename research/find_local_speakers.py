"""Lists local speaker and practitioner candidates for a city from sources web search misses, without searching.

usage, from the repo root:
  python3 research/find_local_speakers.py <city folder> <out.json> --lat 40.76 --lon -111.89 --places "Salt Lake City,Lehi,Provo" [--since 2024-01-01]

- meetup: every data group within 50 km (groupSearch), and the named speaker of each past event since --since. meetup's
  speakerDetails field names the speaker even when the event text does not. hosts are listed as possible connectors.
- bevy: every Snowflake, Tableau, Databricks and Google Developer Group chapter in one of --places, and the speaker and host
  records on each past event page, with title and employer.
- github: users whose location is one of --places and whose profile names a data role, with the accounts they list. one graphql
  search call returns 100 users with their profiles, so the hourly api allowance is not the limit.
each candidate is marked known when the city file already has the name. it writes no city file: look the new people up,
then merge them with assemble.py.
"""

import argparse, concurrent.futures, glob, json, re, subprocess, sys, unicodedata, urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
DATA_GROUP = re.compile(r"\b(data|analytics|dbt|sql|bi|snowflake|databricks|tableau|power ?bi|fabric|python|pydata|pyladies|r-?ladies|r user|"
                        r"machine learning|ai|ml|engineering|postgres|kafka|spark|cloud|women in tech|women techmakers|wids)\b", re.I)
GROUP_QUERIES = ["data", "analytics", "dbt", "sql", "python", "snowflake", "databricks", "machine learning", "ai", "women in tech"]
DATA_ROLE = re.compile(r"\b(dbt|analytics engineer|analytics|data engineer|data engineering|data architect|data platform|business intelligence|"
                       r"\bbi\b|looker|snowflake|tableau|power bi|data warehouse|data scientist)\b", re.I)
GENERATED_BIO = "data engineer by day, homelab tinkerer by night"  # a batch of generated github accounts shares this bio
BEVY = ["usergroups.snowflake.com", "usergroups.tableau.com", "usergroups.databricks.com", "gdg.community.dev"]
GITHUB_ROLES = ["dbt", '"analytics engineer"', '"data engineer"', "analytics", '"business intelligence"', "snowflake"]


def norm(s):
    return " ".join(re.sub(r"[^a-z ]", " ", unicodedata.normalize("NFKD", re.sub(r"\(.*?\)", "", s or "")).encode("ascii", "ignore").decode().lower()).split())


def post(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request("https://www.meetup.com/gql2", body, {"content-type": "application/json", "user-agent": UA})
    try:
        return json.load(urllib.request.urlopen(req, timeout=30)).get("data") or {}
    except Exception:
        return {}


def get_json(url):
    try:
        return json.loads(subprocess.run(["curl", "-s", "-m", "30", "-A", UA, url], capture_output=True, text=True).stdout or "{}")
    except ValueError:
        return {}


def meetup(lat, lon, since):
    groups = {}
    for q in GROUP_QUERIES:
        d = post("query($q:String!,$lat:Float!,$lon:Float!){groupSearch(filter:{query:$q,lat:$lat,lon:$lon,radius:50},first:50){edges{node{urlname name}}}}",
                 {"q": q, "lat": lat, "lon": lon})
        for e in ((d.get("groupSearch") or {}).get("edges") or []):
            if DATA_GROUP.search(e["node"]["name"]):
                groups[e["node"]["urlname"]] = e["node"]["name"]
    def past(urlname):
        found, after = [], None
        for _ in range(10):
            d = post("query($u:String!,$a:String){groupByUrlname(urlname:$u){events(status:PAST,first:100,after:$a){pageInfo{hasNextPage endCursor} "
                     "edges{node{id title dateTime eventUrl eventType venue{city} eventHosts{member{name}}}}}}}", {"u": urlname, "a": after})
            ev = ((d.get("groupByUrlname") or {}).get("events") or {})
            found += [(urlname, e["node"]) for e in ev.get("edges") or [] if e["node"]["dateTime"][:10] >= since]
            if not (ev.get("pageInfo") or {}).get("hasNextPage"):
                break
            after = ev["pageInfo"]["endCursor"]
        return found

    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        events = [e for found in pool.map(past, groups) for e in found]

    def speaker(item):
        urlname, e = item
        d = post("query($id:ID!){event(id:$id){speakerDetails{name socialNetworks{url}}}}", {"id": e["id"]})
        return urlname, e, ((d.get("event") or {}).get("speakerDetails") or {})

    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        rows = list(pool.map(speaker, events))
    out = []
    for urlname, e, s in rows:
        where = {"source": "meetup", "group": groups[urlname], "event": e["title"].strip(), "date": e["dateTime"][:10], "url": e["eventUrl"],
                 "in_person": e.get("eventType") == "PHYSICAL", "venue_city": (e.get("venue") or {}).get("city")}
        if s.get("name"):
            out.append({**where, "name": s["name"].strip(), "role": "speaker", "links": [n["url"] for n in s.get("socialNetworks") or []]})
        for h in e.get("eventHosts") or []:
            out.append({**where, "name": h["member"]["name"].strip(), "role": "host", "links": []})
    return out, groups


def bevy_people(page):
    """speaker and host records that a bevy event page keeps in its page data."""
    out = []
    for m in re.finditer(r'"first_name":"([^"]*)","last_name":"([^"]*)","company":"([^"]*)"', page):
        rec = page[m.end():m.end() + 3000].split('"first_name":')[0]
        field = lambda k: (lambda x: json.loads(f'"{x.group(1)}"') if x else None)(re.search(rf'"{k}":"([^"]*)"', rec))
        li = field("personal_linkedin_page")
        out.append({"name": json.loads(f'"{m.group(1)} {m.group(2)}"').strip(), "company": json.loads(f'"{m.group(3)}"') or None, "title": field("title") or None,
                    "role": field("role") or "speaker", "links": [li if "linkedin.com" in li else f"https://www.linkedin.com/in/{li.strip('/').removeprefix('in/')}/"] if li else []})
    return list({p["name"]: p for p in out}.values())


def bevy(places, since):
    wanted = {norm(p) for p in places}
    out, chapters = [], []
    for host in BEVY:
        page = 1
        while page < 20:
            d = get_json(f"https://{host}/api/chapter_slim/?page_size=500&page={page}")
            for c in d.get("results") or []:
                if norm(c.get("city")) in wanted:
                    chapters.append((host, c["id"], c.get("title")))
            if not d.get("next"):
                break
            page += 1
    events = [(title, e) for host, cid, title in chapters
              for e in get_json(f"https://{host}/api/event_slim/for_chapter/{cid}/?status=Completed&page_size=200").get("results") or []
              if (e.get("start_date") or "")[:10] >= since]

    def people_on(item):
        title, e = item
        return title, e, bevy_people(subprocess.run(["curl", "-sL", "-m", "30", "-A", UA, e["static_url"]], capture_output=True, text=True).stdout)

    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        for title, e, found in pool.map(people_on, events):
            out += [{"source": "bevy", "group": title, "event": e["title"], "date": e["start_date"][:10], "url": e["static_url"],
                     "in_person": not e.get("is_virtual_event"), **p} for p in found]
    return out, chapters


def github_queries(places):
    """github ORs repeated location qualifiers and OR-joined keywords, so a whole region fits in a few queries of at most 256 characters."""
    roles = " OR ".join(GITHUB_ROLES)
    queries, chunk = [], []
    for place in places:
        q = f'{roles} ' + " ".join(f'location:"{p}"' for p in chunk + [place])
        if len(q) > 250 and chunk:
            queries.append(f'{roles} ' + " ".join(f'location:"{p}"' for p in chunk)); chunk = [place]
        else:
            chunk.append(place)
    if chunk:
        queries.append(f'{roles} ' + " ".join(f'location:"{p}"' for p in chunk))
    return queries


USER_SEARCH = """query($q:String!,$after:String){search(type:USER,query:$q,first:100,after:$after){pageInfo{hasNextPage endCursor}
nodes{... on User{login name bio company location url twitterUsername socialAccounts(first:10){nodes{url}}}}}}"""


def github(places):
    """one graphql call returns 100 users with their profile and listed accounts, so a region costs a handful of calls, not two per user."""
    users = {}
    for q in github_queries(places):
        after = None
        for _ in range(10):  # search returns at most 1000 results
            args = ["gh", "api", "graphql", "-f", f"query={USER_SEARCH}", "-f", f"q={q}"] + (["-f", f"after={after}"] if after else [])
            for attempt in range(4):
                r = subprocess.run(args, capture_output=True, text=True)
                if r.returncode == 0:
                    break
                print(f"github search limited, retrying: {(r.stderr or r.stdout).strip()[:80]}", file=sys.stderr)
                subprocess.run(["sleep", "60"])
            try:
                found = (json.loads(r.stdout or "{}").get("data") or {}).get("search") or {}
            except ValueError:
                found = {}
            for u in found.get("nodes") or []:
                if u.get("login"):
                    users[u["login"]] = u
            if not (found.get("pageInfo") or {}).get("hasNextPage"):
                break
            after = found["pageInfo"]["endCursor"]
    out = []
    for login, u in sorted(users.items()):
        bio = (u.get("bio") or "").replace("\r", " ").replace("\n", " ")
        if not u.get("name") or len(norm(u["name"]).split()) < 2 or GENERATED_BIO in bio.lower():
            continue
        if not DATA_ROLE.search(bio + " " + (u.get("company") or "")):
            continue
        social = [a["url"] for a in ((u.get("socialAccounts") or {}).get("nodes") or [])] + ([f"https://x.com/{u['twitterUsername']}"] if u.get("twitterUsername") else [])
        out.append({"source": "github", "name": u["name"].strip(), "company": (u.get("company") or "").lstrip("@").strip() or None, "title": bio[:160] or None,
                    "location": u.get("location"), "url": u["url"], "links": social, "role": "practitioner"})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("city"); ap.add_argument("out")
    ap.add_argument("--lat", type=float, required=True); ap.add_argument("--lon", type=float, required=True)
    ap.add_argument("--places", required=True, help="comma-separated towns in the region, as github and bevy spell them")
    ap.add_argument("--since", default="2024-01-01")
    a = ap.parse_args()
    places = [p.strip() for p in a.places.split(",") if p.strip()]
    f = glob.glob(f"{a.city}/*_dbt_companies.json")[0]
    known = {norm(p["name"]) for c in json.load(open(f))["companies"] for p in c["people"]}
    m, groups = meetup(a.lat, a.lon, a.since)
    print(f"meetup: {len(groups)} data groups, {len(m)} speakers and hosts", file=sys.stderr)
    b, chapters = bevy(places, a.since)
    print(f"bevy: {len(chapters)} chapters ({', '.join(t for _, _, t in chapters)}), {len(b)} speakers and hosts", file=sys.stderr)
    g = github(places)
    print(f"github: {len(g)} data people", file=sys.stderr)
    rows = m + b + g
    for r in rows:
        r["known"] = norm(r["name"]) in known
    json.dump({"city": a.city, "meetup_groups": groups, "bevy_chapters": [t for _, _, t in chapters], "candidates": rows}, open(a.out, "w"), ensure_ascii=False, indent=1)
    new = {norm(r["name"]) for r in rows if not r["known"]}
    print(f"{len(rows)} candidate rows, {len(new)} names not yet in {f}", file=sys.stderr)


if __name__ == "__main__":
    main()
