"""Fills the generated blocks in every SEARCH_METHOD.md from its city file: the at-a-glance table and the companies looked at.

usage, from the repo root: python3 research/write_at_a_glance.py
"""

import glob, json, os, re

START, END = "<!-- at-a-glance:start -->", "<!-- at-a-glance:end -->"
CO_START, CO_END = "<!-- companies:start -->", "<!-- companies:end -->"
SIGNALS = [("strong", "Strong dbt use"), ("medium", "Some dbt signal"), ("nice-to-have", "dbt as a nice-to-have"), ("weak", "Not verified"), ("none", "Uses a different stack")]


def source_line(x):
    """A web source becomes a link; a local file (file: url) is shown as its path in the repo."""
    tail = " (nothing useful)" if x.get("yielded") is False else ""
    url = x["url"]
    if url.startswith("http"):
        return f"- [{x.get('name') or url}]({url}){tail}"
    path = re.sub(r"^file:(//)?(/.*?/dbt-meetups/)?", "", url)
    return f"- {x.get('name') or path}: `{path}`{tail}"


def companies_block(d):
    companies = [c for c in d["companies"] if c["type"] not in ("independent",)]
    lines = [f"{len(companies)} companies and communities were looked at. A company is local when it has people or roles in the region.", ""]
    for signal, label in SIGNALS:
        group = sorted((c for c in companies if c["dbt_signal"] == signal), key=lambda c: c["name"].lower())
        if not group:
            continue
        names = ", ".join(c["name"] + ("" if c["local_presence"] == "confirmed" else " (local presence not confirmed)") for c in group)
        lines += [f"<details><summary><b>{label}</b> ({len(group)})</summary>", "", names, "", "</details>", ""]
    scanned = sorted({e["url"] for c in d["companies"] for e in c["other_evidence"] if e["type"] == "blog_scanned"})
    if scanned:
        lines += [f"<details><summary><b>Blogs and sites scanned</b> ({len(scanned)})</summary>", ""] + [f"- {u}" for u in scanned] + ["", "</details>", ""]
    checked = [x for x in (d["sources"].get("checked") or []) if isinstance(x, dict) and x.get("url")] if isinstance(d["sources"], dict) else []
    if checked:
        lines += [f"<details><summary><b>Other sources checked</b> ({len(checked)})</summary>", ""]
        lines += [source_line(x) for x in checked] + ["", "</details>", ""]
    return "\n".join(lines).rstrip()

for doc in sorted(glob.glob("*/SEARCH_METHOD.md")):
    text = open(doc).read()
    if START not in text and CO_START not in text:
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
    text = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda m: f"{START}\n{table}\n{END}", text, flags=re.S)
    if CO_START in text:
        block = companies_block(d)
        text = re.sub(re.escape(CO_START) + ".*?" + re.escape(CO_END), lambda m: f"{CO_START}\n{block}\n{CO_END}", text, flags=re.S)
    open(doc, "w").write(text)
    print(f"{doc}: table written")
