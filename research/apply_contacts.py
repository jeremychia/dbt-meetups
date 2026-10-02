"""Applies LinkedIn search results to a city file: the profile link and, when the result states it, the location.

usage, from the repo root: python3 research/apply_contacts.py <city file> <patch.json>
patch: {"<person id>": {"linkedin_url": "...", "evidence": "result title and location", "confidence": "high|medium",
         "based_in_region": true|false|null, "city": "..."}}
a known location is never overwritten; a person who already has the link is skipped.
"""

import json, sys
from collections import Counter

path, patch_path = sys.argv[1], sys.argv[2]
raw = open(path).read()
d = json.loads(raw)
patch = json.load(open(patch_path))
people = {p["id"]: (p, c) for c in d["companies"] for p in c["people"]}
applied, located, problems = 0, 0, []
for pid, f in patch.items():
    if pid not in people:
        problems.append(f"unknown person id {pid}")
        continue
    p, c = people[pid]
    url = f.get("linkedin_url") or ""
    if "linkedin.com/in/" not in url or f.get("confidence") not in ("high", "medium"):
        problems.append(f"{pid}: needs a linkedin.com/in url and confidence high|medium")
        continue
    if url not in p["linkedin_urls"]:
        p["linkedin_urls"].append(url)
        p["has_linkedin"] = True
        p["linkedin_confidence"] = f["confidence"]
        p["evidence"].append({"url": url, "note": f"linkedin search result: {f.get('evidence') or ''}".strip()})
        applied += 1
    if p["based_in_region"] is None and f.get("based_in_region") in (True, False):
        p["based_in_region"] = f["based_in_region"]
        if f.get("city"):
            p["city"] = f["city"]
        note = f"location ({f['confidence']}): linkedin search result: {f.get('evidence') or ''} {url}"
        p["notes"] = " | ".join(x for x in [p["notes"], note] if x)
        p["evidence"].append({"url": url, "note": note})
        p["meetup_fit"]["attendee_potential"] = "low" if not f["based_in_region"] else ("high" if p["mentions_dbt"] or c["dbt_signal"] == "strong" else "medium")
        located += 1
if problems:
    print("not applied:\n- " + "\n- ".join(problems))
allp = [p for c in d["companies"] for p in c["people"]]
m = d["metadata"]["counts"]
m["people_with_linkedin"] = sum(p["has_linkedin"] for p in allp)
m["people_with_contact"] = sum(bool(p["has_linkedin"] or p["profile_urls"]) for p in allp)
m["attendee_potential"] = dict(Counter(p["meetup_fit"]["attendee_potential"] for p in allp))
open(path, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
print(f"{path}: {applied} linkedin profiles, {located} locations")
