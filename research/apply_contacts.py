"""Applies search results to a city file: a LinkedIn or other public profile link and, when the result states it, the location.

usage, from the repo root: python3 research/apply_contacts.py <city file> <patch.json>
patch: {"<person id>": {"linkedin_url": "...", "evidence": "result title and location", "confidence": "high|medium",
         "based_in_region": true|false|null, "city": "..."}}
a non-linkedin profile replaces linkedin_url with "profile": {"type": "<validate.PROFILE_TYPES>", "url": "...", "source": "<page or result that ties it to the person>"}.
a person searched without a match is {"confidence": "low"}, which marks them searched.
a known location is never overwritten; a person who already has the link is skipped.
"""

import json, sys
from collections import Counter
from validate import PROFILE_TYPES

path, patch_path = sys.argv[1], sys.argv[2]
raw = open(path).read()
d = json.loads(raw)
patch = json.load(open(patch_path))
people = {p["id"]: (p, c) for c in d["companies"] for p in c["people"]}
applied, profiled, located, missed, problems = 0, 0, 0, 0, []
for pid, f in patch.items():
    if pid not in people:
        problems.append(f"unknown person id {pid}")
        continue
    p, c = people[pid]
    if f.get("confidence") == "low" and not f.get("linkedin_url") and not f.get("profile"):
        if p["linkedin_confidence"] == "not_searched":
            p["linkedin_confidence"] = "low"
            missed += 1
        continue
    if f.get("confidence") not in ("high", "medium"):
        problems.append(f"{pid}: needs confidence high|medium")
        continue
    prof = f.get("profile")
    if prof:
        if set(prof) != {"type", "url", "source"} or prof["type"] not in PROFILE_TYPES or not prof["url"].startswith("http"):
            problems.append(f"{pid}: profile needs type, url and source, with a type from validate.PROFILE_TYPES")
            continue
        url = prof["url"]
        if url not in [u["url"] for u in p["profile_urls"]]:
            p["profile_urls"].append(prof)
            p["evidence"].append({"url": url, "note": f"profile found by search: {f.get('evidence') or ''}".strip()})
            profiled += 1
    else:
        url = f.get("linkedin_url") or ""
        if "linkedin.com/in/" not in url:
            problems.append(f"{pid}: needs a linkedin.com/in url or a profile")
            continue
    if not prof and url not in p["linkedin_urls"]:
        p["linkedin_urls"].append(url)
        p["has_linkedin"] = True
        p["linkedin_confidence"] = f["confidence"]
        p["evidence"].append({"url": url, "note": f"linkedin search result: {f.get('evidence') or ''}".strip()})
        applied += 1
    if p["based_in_region"] is None and f.get("based_in_region") in (True, False):
        p["based_in_region"] = f["based_in_region"]
        if f.get("city"):
            p["city"] = f["city"]
        note = f"location ({f['confidence']}): {'search result' if prof else 'linkedin search result'}: {f.get('evidence') or ''} {url}"
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
print(f"{path}: {applied} linkedin profiles, {profiled} other profiles, {located} locations, {missed} searched without a match")
