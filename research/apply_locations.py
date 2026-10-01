"""Applies location findings to a <city>_dbt_companies.json.

usage: python3 research/apply_locations.py <city_file.json> <patch.json>
patch: {"<person id>": {"based_in_region": true|false, "city": "Lyon", "evidence_url": "...", "evidence": "github profile location: Lyon, France", "confidence": "high|medium", "linkedin_url": "optional"}}
only people whose based_in_region is null are changed; a known location is never overwritten.
"""

import json, sys
from collections import Counter

path, patch_path = sys.argv[1], sys.argv[2]
raw = open(path).read()
d = json.loads(raw)
patch = json.load(open(patch_path))
people = {p["id"]: (p, c) for c in d["companies"] for p in c["people"]}

problems, applied = [], 0
for pid, f in patch.items():
    if pid not in people:
        problems.append(f"unknown person id {pid}")
        continue
    p, c = people[pid]
    if p["based_in_region"] is not None:
        continue
    if f.get("based_in_region") not in (True, False) or not f.get("evidence_url") or f.get("confidence") not in ("high", "medium"):
        problems.append(f"{pid}: needs based_in_region true/false, evidence_url and confidence high|medium")
        continue
    p["based_in_region"] = f["based_in_region"]
    if f.get("linkedin_url"):
        if "linkedin.com/in/" not in f["linkedin_url"]:
            problems.append(f"{pid}: {f['linkedin_url']} is not a linkedin.com/in url")
        elif f["linkedin_url"] not in p["linkedin_urls"]:
            p["linkedin_urls"].append(f["linkedin_url"])
            p["has_linkedin"] = True
            p["linkedin_confidence"] = "high" if f["confidence"] == "high" else "medium"
    if f.get("city"):
        p["city"] = f["city"]
    note = f"location ({f['confidence']}): {f.get('evidence') or 'see link'} {f['evidence_url']}"
    p["notes"] = " | ".join(x for x in [p["notes"], note] if x)
    p["evidence"].append({"url": f["evidence_url"], "note": note})
    # attendee_potential follows SEARCH_METHOD.md §1 Step 6
    p["meetup_fit"]["attendee_potential"] = "low" if not f["based_in_region"] else (
        "high" if p["mentions_dbt"] or c["dbt_signal"] == "strong" else "medium")
    applied += 1

if problems:
    print("not applied:\n- " + "\n- ".join(problems))
allp = [p for c in d["companies"] for p in c["people"]]
d["metadata"]["counts"]["people_with_linkedin"] = sum(p["has_linkedin"] for p in allp)
d["metadata"]["counts"]["attendee_potential"] = dict(Counter(p["meetup_fit"]["attendee_potential"] for p in allp))
open(path, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
print(f"{path}: {applied} locations applied, {sum(p['based_in_region'] is None for p in allp)} still unknown")
