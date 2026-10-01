"""Sets people's location back to unknown, undoing apply_locations.py.

usage: python3 research/revert_locations.py <city_file.json> <person id> [<person id> ...]
"""

import json, sys
from collections import Counter

path, ids = sys.argv[1], set(sys.argv[2:])
raw = open(path).read()
d = json.loads(raw)
done = set()
for c in d["companies"]:
    for p in c["people"]:
        if p["id"] not in ids:
            continue
        p["based_in_region"] = None
        p["city"] = None  # the city came with the reverted location
        p["notes"] = " | ".join(x for x in (p["notes"] or "").split(" | ") if not x.startswith("location (")) or None
        p["evidence"] = [e for e in p["evidence"] if not (e.get("note") or "").startswith("location (")]
        p["meetup_fit"]["attendee_potential"] = "medium"  # in-region or unknown, per SEARCH_METHOD.md §1 Step 6
        done.add(p["id"])
allp = [p for c in d["companies"] for p in c["people"]]
d["metadata"]["counts"]["attendee_potential"] = dict(Counter(p["meetup_fit"]["attendee_potential"] for p in allp))
open(path, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
print(f"{path}: reverted {sorted(done)}; not found {sorted(ids - done)}")
