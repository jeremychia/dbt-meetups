"""Fills the at-a-glance table in every SEARCH_METHOD.md that has the marker comments, from its city file.

usage, from the repo root: python3 research/write_at_a_glance.py
"""

import glob, json, os, re

START, END = "<!-- at-a-glance:start -->", "<!-- at-a-glance:end -->"

for doc in sorted(glob.glob("*/SEARCH_METHOD.md")):
    text = open(doc).read()
    if START not in text:
        continue
    data_files = glob.glob(os.path.join(os.path.dirname(doc), "*_dbt_companies.json"))
    if len(data_files) != 1:
        print(f"{doc}: skipped, expected one data file next to it")
        continue
    d = json.load(open(data_files[0]))
    people = [p for c in d["companies"] for p in c["people"]]
    tier1 = [p for p in people if str(p["priority_tier"]) == "1"]
    rows = [
        ("Companies", len(d["companies"])),
        ("People", len(people)),
        ("Tier 1 leads", len(tier1)),
        ("First-time speakers (publish, no talk yet)", sum(p["lead_type"] == "emerging_voice" for p in people)),
        ("Proven speakers", sum(p["lead_type"] == "proven_speaker" for p in people)),
        ("Spoke at this chapter before", sum(bool(p["past_chapter_talks"]) for p in people)),
        ("Based in the region", sum(p["based_in_region"] is True for p in people)),
        ("Based elsewhere", sum(p["based_in_region"] is False for p in people)),
        ("Location unknown", sum(p["based_in_region"] is None for p in people)),
        ("With a LinkedIn profile", sum(p["has_linkedin"] for p in people)),
        ("Job ads mentioning dbt", sum(len(c["job_postings"]) for c in d["companies"])),
        ("Past chapter meetups", len(d["past_meetups"])),
    ]
    table = "\n".join(
        [f"**At a glance** (version {d['metadata']['version']}, {d['metadata']['generated_at']})", "", "| | Count |", "|---|---|"]
        + [f"| {label} | {n} |" for label, n in rows]
    )
    text = re.sub(re.escape(START) + ".*?" + re.escape(END), f"{START}\n{table}\n{END}", text, flags=re.S)
    open(doc, "w").write(text)
    print(f"{doc}: table written")
