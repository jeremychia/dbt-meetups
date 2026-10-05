"""Adds a person's Meetup member profile when they host or RSVP to the event where they spoke.

usage, from the repo root: python3 research/match_meetup_members.py [--city-pool]

the events come from the person's evidence (meetup.com/<group>/events/<id>) and from the chapter meetups in
past_chapter_talks. a member counts only when exactly one host or RSVP of that event has the person's first and
last name, so the profile is tied to the talk, not to a namesake.

--city-pool: for people still without a contact, also look among everyone who hosted or RSVP'd to any meetup event in
the city file. a member counts only when exactly one person in that pool has the first and last name, and the name is
rare: 15 or fewer GitHub users share it. the source says so, since the tie is to the city's data meetups, not the talk.
"""

import concurrent.futures, glob, json, re, sys, time, unicodedata, urllib.request
from validate import reachable

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
EVENT = re.compile(r"meetup\.com/[^/]+/events/(\d+)")
QUERY = "query($id:ID!,$after:String){event(id:$id){eventHosts{member{id name}} rsvps(first:500,after:$after){pageInfo{hasNextPage endCursor} edges{node{member{id name}}}}}}"


def norm(s):
    return re.sub(r"[^a-z0-9 ]", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).split()


def members(event_id):
    found, after = {}, None
    for _ in range(10):
        body = json.dumps({"query": QUERY, "variables": {"id": event_id, "after": after}}).encode()
        req = urllib.request.Request("https://www.meetup.com/gql2", body, {"content-type": "application/json", "user-agent": UA})
        try:
            ev = (json.load(urllib.request.urlopen(req, timeout=30)).get("data") or {}).get("event") or {}
        except Exception:
            break
        for h in ev.get("eventHosts") or []:
            found[h["member"]["id"]] = h["member"]["name"]
        r = ev.get("rsvps") or {}
        for e in r.get("edges") or []:
            found[e["node"]["member"]["id"]] = e["node"]["member"]["name"]
        if not (r.get("pageInfo") or {}).get("hasNextPage"):
            break
        after = r["pageInfo"]["endCursor"]
    return found


def match(person_name, roster):
    tok = [t for t in norm(re.sub(r"\(.*?\)", "", person_name)) if len(t) > 1]
    if len(tok) < 2:
        return None
    hits = [mid for mid, name in roster.items() if tok[0] in norm(name) and tok[-1] in norm(name)]
    return hits[0] if len(hits) == 1 else None


def main():
    files = sorted(glob.glob("*/*_dbt_companies.json"))
    data = {f: json.loads(open(f).read()) for f in files}
    wanted = {}  # (file, person id) -> event ids
    for f, d in data.items():
        by_date = {m["date"]: m["url"] for m in d["past_meetups"] if m.get("url")}
        for c in d["companies"]:
            for p in c["people"]:
                if p["has_linkedin"] or any(u["type"] == "meetup" for u in p["profile_urls"]):
                    continue
                ids = {m.group(1) for e in p["speaker_evidence"] + p["evidence"] for m in [EVENT.search(e.get("url") or "")] if m}
                ids |= {m.group(1) for t in p["past_chapter_talks"] for m in [EVENT.search(by_date.get(t["date"], ""))] if m}
                if ids:
                    wanted[(f, p["id"])] = ids
    events = sorted({i for ids in wanted.values() for i in ids})
    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        rosters = dict(zip(events, pool.map(members, events)))
    for f, d in data.items():
        n = 0
        for c in d["companies"]:
            for p in c["people"]:
                for eid in sorted(wanted.get((f, p["id"]), ())):
                    mid = match(p["name"], rosters.get(eid, {}))
                    if mid:
                        p["profile_urls"].append({"type": "meetup", "url": f"https://www.meetup.com/members/{mid}/", "source": f"https://www.meetup.com/events/{eid}/ (host or RSVP)"})
                        n += 1
                        break
        allp = [p for c in d["companies"] for p in c["people"]]
        d["metadata"]["counts"]["people_with_contact"] = sum(map(reachable, allp))
        raw = open(f).read()
        open(f, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
        print(f"{f.split('/')[0]:16} +{n:3} meetup profiles  reachable {d['metadata']['counts']['people_with_contact']}/{len(allp)}")
    print(f"{len(events)} events read")


def rare(tok):
    from find_github_profiles import gh
    res = gh("search/users", f'q=fullname:"{" ".join(tok)}"', "per_page=1") or {}
    time.sleep(2.2)  # search allows 30 calls a minute
    return res.get("total_count", 99) <= 15


def city_pool():
    files = sorted(glob.glob("*/*_dbt_companies.json"))
    data = {f: json.loads(open(f).read()) for f in files}
    pools = {}
    for f, d in data.items():
        urls = [m.get("url") or "" for m in d["past_meetups"]] + [e.get("url") or "" for c in d["companies"] for p in c["people"] for e in p["speaker_evidence"] + p["evidence"]]
        pools[f] = {m.group(1) for u in urls for m in [EVENT.search(u)] if m}
    events = sorted(set().union(*pools.values()))
    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        rosters = dict(zip(events, pool.map(members, events)))
    for f, d in data.items():
        roster = {mid: name for eid in pools[f] for mid, name in rosters.get(eid, {}).items()}
        n = 0
        for c in d["companies"]:
            for p in c["people"]:
                if reachable(p):
                    continue
                tok = [t for t in norm(re.sub(r"\(.*?\)", "", p["name"])) if len(t) > 1]
                mid = match(p["name"], roster)
                if mid and len(tok) >= 2 and rare(tok):
                    p["profile_urls"].append({"type": "meetup", "url": f"https://www.meetup.com/members/{mid}/",
                                              "source": f"only member named {roster[mid]} among hosts and RSVPs of this city's meetup events"})
                    n += 1
        allp = [p for c in d["companies"] for p in c["people"]]
        d["metadata"]["counts"]["people_with_contact"] = sum(map(reachable, allp))
        raw = open(f).read()
        open(f, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
        print(f"{f.split('/')[0]:16} +{n:3} meetup profiles from the city pool  reachable {d['metadata']['counts']['people_with_contact']}/{len(allp)}")


if __name__ == "__main__":
    city_pool() if "--city-pool" in sys.argv else main()
