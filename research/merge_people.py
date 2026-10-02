"""Merges duplicate person records in one city file.

usage: python3 research/merge_people.py <city_file.json> <keep id> <drop id> [<drop id> ...]
the kept record gains the dropped records' evidence, talks, links and notes; a known location wins over unknown.
"""

import json, sys
from collections import Counter
from assemble import merge_lists, standard_counts

path, keep_id, drop_ids = sys.argv[1], sys.argv[2], set(sys.argv[3:])
raw = open(path).read()
d = json.loads(raw)
people = {p["id"]: p for c in d["companies"] for p in c["people"]}
missing = ({keep_id} | drop_ids) - set(people)
if missing:
    sys.exit(f"unknown ids: {sorted(missing)}")

keep = people[keep_id]
for drop in (people[i] for i in drop_ids):
    keep["speaker_evidence"] = merge_lists(keep["speaker_evidence"], drop["speaker_evidence"], lambda e: e["content_id"])
    keep["evidence"] = merge_lists(keep["evidence"], drop["evidence"], lambda e: e["url"])
    keep["past_chapter_talks"] = merge_lists(keep["past_chapter_talks"], drop["past_chapter_talks"], lambda t: (t["date"], t["talk_title"]))
    keep["linkedin_urls"] = list(dict.fromkeys(keep["linkedin_urls"] + drop["linkedin_urls"]))
    keep["profile_urls"] = merge_lists(keep["profile_urls"], drop["profile_urls"], lambda u: u["url"])
    keep["has_linkedin"] = bool(keep["linkedin_urls"])
    keep["sourced_via"] = list(dict.fromkeys(keep["sourced_via"] + drop["sourced_via"]))
    if keep["based_in_region"] is None and drop["based_in_region"] is not None:
        keep["based_in_region"], keep["city"], keep["meetup_fit"]["attendee_potential"] = drop["based_in_region"], drop["city"], drop["meetup_fit"]["attendee_potential"]
    if drop["lead_type"] == "proven_speaker":
        keep["lead_type"] = "proven_speaker"
    parts = [x for n in (keep["notes"], drop["notes"]) for x in (n or "").split(" | ") if x]
    keep["notes"] = " | ".join(dict.fromkeys(parts + [f"merged duplicate record '{drop['name']}' ({drop['id']})"]))

for c in d["companies"]:
    c["people"] = [p for p in c["people"] if p["id"] not in drop_ids]
d["metadata"]["counts"] = standard_counts(d)
open(path, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
print(f"{path}: merged {sorted(drop_ids)} into {keep_id}")
