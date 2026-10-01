"""Builds or extends a <city>_dbt_companies.json (shared schema v3) from a loose research file.

usage: python3 research/assemble.py <raw.json> <out.json> [--base <existing.json>]
run from the dbt-meetups repo root. exits non-zero with a list of problems to fix in raw.json.
"""

import json, re, sys, unicodedata, datetime
from collections import Counter

sys.path.insert(0, "pipeline")
from enrich import TOPIC_VOCABULARY as V

TODAY = datetime.date.today().isoformat()
LEAD_TYPES = {"proven_speaker", "emerging_voice", "featured", "no_public_content"}
TIERS = {"1", "2", "3", "connector", "organiser", "backup"}
LEADERSHIP = re.compile(r"\b(head|director|vp|vice president|chief|founder|co-founder|cto|ceo|cdo|cfo|coo|manager|lead)\b", re.I)
errors = []
touched = set()  # ids of companies and people that new research added or changed; only these are re-scored


def norm(s):
    ascii_form = re.sub(r"[^a-z0-9 ]", "", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()
    # a name in a non-latin script has no ascii form, so match it on its own characters instead
    return ascii_form or re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s or "")).strip().lower()


def slug(s):
    return re.sub(r"\s+", "-", norm(s))[:60].strip("-") or "unknown"


def has_dbt(*texts):
    return any(re.search(r"\bdbt\b", t or "", re.I) for t in texts)


def evidence_item(e, who):
    topics = [t for t in (e.get("topics") or []) if t in V][:3]
    bad = [t for t in (e.get("topics") or []) if t not in V]
    if bad or not topics:
        errors.append(f"{who}: '{e.get('title')}' needs 1-3 topics from the vocabulary (bad: {bad})")
    if not e.get("url"):
        errors.append(f"{who}: '{e.get('title')}' has no url")
    return {
        "type": e.get("type", "talk"), "event": e.get("event"), "title": e.get("title"), "date": e.get("date"),
        "url": e.get("url"), "content_id": e.get("content_id") or slug(f"{e.get('event') or ''}-{e.get('title') or ''}"),
        "co_authors": e.get("co_authors") or [],
        "mentions_dbt": e["mentions_dbt"] if e.get("mentions_dbt") is not None else has_dbt(e.get("title"), e.get("description")),
        "description": e.get("description"), "topics": topics, "suggested_talk_angle": e.get("suggested_talk_angle"),
        "url_precision": e.get("url_precision", "direct"), "confidence": e.get("confidence", "medium"),
    }


def person(p, company_name):
    who = p.get("name")
    links = p.get("linkedin_urls") or []
    out = {
        "id": p.get("id") or slug(who), "name": who, "pronouns": p.get("pronouns"), "title": p.get("title"),
        "city": p.get("city"), "based_in_region": p.get("based_in_region"), "level": None,
        "linkedin_urls": links, "has_linkedin": bool(links),
        "linkedin_confidence": p.get("linkedin_confidence") or ("medium" if links else "not_searched"),
        "meetup_fit": {}, "lead_type": p.get("lead_type"), "sourced_via": p.get("sourced_via") or ["other"],
        "mentions_dbt": p.get("mentions_dbt"),
        "speaker_evidence": [evidence_item(e, who) for e in p.get("speaker_evidence") or []],
        "attendee_signal": p.get("attendee_signal"),
        "evidence": p.get("evidence") or [{"url": e.get("url"), "note": f"{e.get('type', 'talk')}: {e.get('title')}"} for e in p.get("speaker_evidence") or []],
        "confidence": p.get("confidence", "Medium"), "internal_vinted": bool(p.get("internal_vinted")) or norm(company_name) == "vinted",
        "priority_tier": str(p.get("priority_tier", "2")), "suggested_talk_angle": p.get("suggested_talk_angle"),
        "past_chapter_talks": [], "notes": p.get("notes"),
    }
    if out["lead_type"] not in LEAD_TYPES:
        errors.append(f"{who}: lead_type must be one of {sorted(LEAD_TYPES)}")
    if out["priority_tier"] not in TIERS:
        errors.append(f"{who}: priority_tier must be one of {sorted(TIERS)}")
    for u in links:
        if "linkedin.com/in/" not in u:
            errors.append(f"{who}: {u} is not a linkedin.com/in url")
    return out


def job(j, company_name):
    return {
        "title": j.get("title"), "url": j.get("url"), "source": j.get("source"),
        "linkedin_company_name": j.get("linkedin_company_name"), "dbt_mentioned_in_text": j.get("dbt_mentioned_in_text"),
        "dbt_snippet": j.get("dbt_snippet"), "job_poster": j.get("job_poster"), "posted_date": j.get("posted_date"),
        "last_seen": j.get("last_seen") or TODAY, "job_family": j.get("job_family"), "work_mode": j.get("work_mode"),
    }


def company(c):
    out = {
        "id": c.get("id") or slug(c["name"]), "name": c["name"], "type": c.get("type", "employer"), "watchlist": None,
        "excluded_from_outreach": bool(c.get("excluded_from_outreach")) or slug(c["name"]).startswith("dbt-labs"),
        "cities": c.get("cities") or [], "local_presence": c.get("local_presence", "not_confirmed"),
        "dbt_signal": c.get("dbt_signal", "weak"), "stack_signals": c.get("stack_signals") or [],
        "job_postings": [job(j, c["name"]) for j in c.get("job_postings") or []],
        "other_evidence": c.get("other_evidence") or [], "people": [], "notes": c.get("notes"),
    }
    out["people"] = [person(p, c["name"]) for p in c.get("people") or []]
    return out


def merge_lists(old, new, key):
    seen = {key(x) for x in old}
    return old + [x for x in new if key(x) not in seen]


def merge(base, raw_companies):
    by_id = {c["id"]: c for c in base}
    by_name = {norm(c["name"]): c for c in base}
    people_index = {}
    for c in base:
        for p in c["people"]:
            people_index[p["id"]] = p
            people_index[norm(p["name"])] = p
    for rc in raw_companies:
        c = company(rc)
        target = by_id.get(c["id"]) or by_name.get(norm(c["name"]))
        if target is None:
            base.append(c); target = c; touched.add(id(c))
            by_id[c["id"]] = c; by_name[norm(c["name"])] = c
            new_people, c["people"] = c["people"], []
        else:
            new_people = c["people"]
            touched.add(id(target))
            target["job_postings"] = merge_lists(target["job_postings"], c["job_postings"], lambda j: j["url"])
            target["other_evidence"] = merge_lists(target["other_evidence"], c["other_evidence"], lambda e: e["url"])
            target["stack_signals"] = list(dict.fromkeys(target["stack_signals"] + c["stack_signals"]))
            target["cities"] = list(dict.fromkeys(target["cities"] + c["cities"]))
            if c["notes"] and c["notes"] not in (target["notes"] or ""):
                target["notes"] = " | ".join(x for x in [target["notes"], c["notes"]] if x)
        for p in new_people:
            existing = people_index.get(p["id"]) or people_index.get(norm(p["name"]))
            if existing:
                touched.add(id(existing))
                existing["speaker_evidence"] = merge_lists(existing["speaker_evidence"], p["speaker_evidence"], lambda e: e["content_id"])
                if existing["lead_type"] != "proven_speaker" and any(
                        e["type"] in ("talk", "panel", "podcast", "workshop", "webinar") for e in p["speaker_evidence"]):
                    existing["lead_type"] = "proven_speaker"  # a talk on record makes anyone a proven speaker
                existing["evidence"] = merge_lists(existing["evidence"], p["evidence"], lambda e: e["url"])
                existing["linkedin_urls"] = list(dict.fromkeys(existing["linkedin_urls"] + p["linkedin_urls"]))
                existing["sourced_via"] = list(dict.fromkeys(existing["sourced_via"] + p["sourced_via"]))
                if p["notes"] and p["notes"] not in (existing["notes"] or ""):
                    existing["notes"] = " | ".join(x for x in [existing["notes"], p["notes"]] if x)
            else:
                target["people"].append(p); touched.add(id(p))
                people_index[p["id"]] = p; people_index[norm(p["name"])] = p
    return base


def past_meetups_from(enriched_file):
    events = json.load(open(enriched_file))["events"]
    out = []
    for e in sorted(events, key=lambda e: e["date"]):
        meta = e.get("additional_metadata") or {}
        out.append({
            "name": e["event_name"], "date": e["date"], "venue": e.get("location"), "url": e["event_url"],
            "organisers": [h for h in (meta.get("hosts") or []) if h], "attendees": e.get("attendees"),
            "talks": [{"speaker": t.get("speaker_name"), "company": t.get("speaker_title"), "title": t.get("title"),
                       "topics": [x for x in (t.get("topics") or []) if x in V]} for t in e.get("talks") or []],
        })
    return out


def add_chapter_speakers(companies, past, chapter_name, city):
    """Every past chapter speaker becomes a person, so the cockpit can show who has spoken before."""
    index = {norm(p["name"]): p for c in companies for p in c["people"]}
    by_name = {norm(c["name"]): c for c in companies}
    for m in past:
        for t in m["talks"]:
            for name in re.split(r"\s*(?:&|,| and )\s*", t["speaker"] or ""):
                if len(norm(name).split()) < 2 or norm(name) in index:
                    continue
                parts = [x.strip() for x in re.split(r",|@|\bat\b", t["company"] or "")]
                parts = [x for x in parts if x and not re.fullmatch(r"(inc|ltd|llc|gmbh|se|ag|plc|corp)\.?", x, re.I)]
                employer = parts[-1] if parts else "Independent / no company"
                c = by_name.get(norm(employer))
                if c is None:
                    c = company({"name": employer, "type": "employer", "cities": [city], "local_presence": "not_confirmed",
                                 "dbt_signal": "strong", "notes": f"employer of a past {chapter_name} speaker"})
                    if norm(employer) == "independent  no company":
                        c["id"], c["type"] = "independent", "independent"
                    companies.append(c); by_name[norm(employer)] = c; touched.add(id(c))
                p = person({"name": name, "title": t["company"], "city": city, "based_in_region": None,
                            "lead_type": "proven_speaker", "sourced_via": ["chapter_meetup_history"], "confidence": "High",
                            "priority_tier": "1" if m["date"] >= "2025-01-01" else "2"}, employer)
                c["people"].append(p); index[norm(name)] = p; touched.add(id(p))


def past_chapter_talks(name, past):
    toks = norm(name).split()
    if len(toks) < 2:
        return []
    return [{"date": m["date"], "talk_title": t["title"], "topics": t["topics"]}
            for m in past for t in m["talks"] if toks[0] in norm(t["speaker"]).split() and toks[-1] in norm(t["speaker"]).split()]


def rescore(companies, past):
    for c in companies:
        if id(c) in touched:
            c["watchlist"] = c["type"] not in ("community", "independent") and (
                c["local_presence"] != "confirmed" or c["dbt_signal"] in ("weak", "none"))
        for p in c["people"]:
            p["past_chapter_talks"] = past_chapter_talks(p["name"], past)
            if id(p) not in touched:
                continue
            ev = p["speaker_evidence"]
            if p["mentions_dbt"] is None and ev:
                p["mentions_dbt"] = any(e["mentions_dbt"] for e in ev)
            p["level"] = "leadership" if LEADERSHIP.search(p["title"] or "") else "working"
            authored = [e for e in ev if e["type"] in ("blog", "article", "newsletter", "oss", "linkedin_post", "post")]
            if p["lead_type"] == "emerging_voice" and p["based_in_region"] is not False \
                    and any((e["date"] or "") >= "2024" for e in authored) and str(p["priority_tier"]) in ("2", "3"):
                p["priority_tier"] = "1"  # the rule only raises an emerging voice, never lowers anyone
            talks = [e for e in ev if e["type"] in ("talk", "panel", "podcast", "workshop", "webinar")]
            high = any(e["mentions_dbt"] for e in talks) or len(talks) >= 2 or p["past_chapter_talks"] or str(p["priority_tier"]) == "1"
            p["meetup_fit"] = {
                "speaker_potential": "high" if high else ("medium" if ev else "low"),
                "attendee_potential": "low" if p["based_in_region"] is False else
                ("high" if p["based_in_region"] and (p["mentions_dbt"] or c["dbt_signal"] == "strong") else "medium"),
            }


def standard_counts(ds):
    allp = [p for c in ds["companies"] for p in c["people"]]
    return {"companies": len(ds["companies"]), "people": len(allp),
            "job_postings": sum(len(c["job_postings"]) for c in ds["companies"]),
            "companies_with_job_postings": sum(1 for c in ds["companies"] if c["job_postings"]),
            "speaker_evidence_items": sum(len(p["speaker_evidence"]) for p in allp),
            "unique_content_items": len({e["content_id"] for p in allp for e in p["speaker_evidence"]}),
            "people_with_linkedin": sum(p["has_linkedin"] for p in allp),
            "people_who_spoke_at_this_chapter": sum(1 for p in allp if p["past_chapter_talks"]),
            "internal_vinted": sum(p["internal_vinted"] for p in allp),
            "level": dict(Counter(p["level"] for p in allp)),
            "speaker_potential": dict(Counter(p["meetup_fit"]["speaker_potential"] for p in allp)),
            "attendee_potential": dict(Counter(p["meetup_fit"]["attendee_potential"] for p in allp)),
            "priority_tier": dict(Counter(str(p["priority_tier"]) for p in allp)),
            "watchlist_companies": sum(1 for c in ds["companies"] if c["watchlist"]),
            "past_meetups": len(ds["past_meetups"]),
            "lead_type": dict(Counter(p["lead_type"] for p in allp)),
            "people_with_self_stated_pronouns": sum(1 for p in allp if p["pronouns"]),
            "sourced_via": dict(Counter(s for p in allp for s in p["sourced_via"]))}


def main():
    raw_path, out_path = sys.argv[1], sys.argv[2]
    base_path = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == "--base" else None
    raw = json.load(open(raw_path))
    base = json.load(open(base_path)) if base_path else None

    companies = merge(base["companies"] if base else [], raw.get("companies") or [])
    past = past_meetups_from(raw["enriched_file"])
    add_chapter_speakers(companies, past, raw["chapter_name"], raw["city"])
    rescore(companies, past)

    errors.extend(f"{p['name']}: id '{p['id']}' must be ascii kebab-case, set \"id\" in the raw file (romanised name or handle)"
                  for c in companies for p in c["people"] if not re.fullmatch(r"[a-z0-9-]+", p["id"]))
    seen = Counter(p["id"] for c in companies for p in c["people"])
    errors.extend(f"duplicate person id {i}" for i, n in seen.items() if n > 1)
    if errors:
        print("fix these in the raw file:\n- " + "\n- ".join(errors)); sys.exit(1)

    m = base["metadata"] if base else {}
    method_line = raw.get("method") or "research sub-agent run"
    ds = {
        "metadata": {
            "title": m.get("title") or f"{raw['city']} dbt companies and people for the {raw['chapter_name']}",
            "generated_at": TODAY, "prepared_for": "Jeremy Chia (dbt meetups)",
            "purpose": m.get("purpose") or f"Find {raw['city']} companies using dbt, and people who could speak at or attend the {raw['chapter_name']}.",
            "version": (m.get("version") or 0) + 1, "schema_version": 3,
            "region": m.get("region") or f"{raw['city']} ({raw['chapter_name']})",
            "method": (m.get("method") or []) + [f"v{(m.get('version') or 0) + 1} ({TODAY}): {method_line}"] + (raw.get("lessons") or []),
            "field_definitions": json.load(open("berlin_planning/berlin_dbt_companies.json"))["metadata"]["field_definitions"],
            "caveats": list(dict.fromkeys((m.get("caveats") or []) + (raw.get("caveats") or []))),
            "counts": {}, "topic_vocabulary_source": "pipeline/enrich.py::TOPIC_VOCABULARY", "topic_vocabulary": V,
            "topic_counts": {},
        },
        "companies": companies,
        "sources": base["sources"] if base else {
            "chapter_past_events": raw.get("chapter_url"), "past_meetups_derived_from": raw["enriched_file"],
            "checked": raw.get("sources_checked") or []},
        "past_meetups": past,
        "community_channels": merge_lists((base or {}).get("community_channels") or [], raw.get("community_channels") or [], lambda x: x["url"]),
    }
    if base:
        ds["sources"]["checked"] = merge_lists(ds["sources"].get("checked") or [], raw.get("sources_checked") or [], lambda x: x.get("url"))
    for c in companies:  # numbered tiers are integers in every file; named roles stay strings
        for p in c["people"]:
            if str(p["priority_tier"]).isdigit():
                p["priority_tier"] = int(p["priority_tier"])
    ds["metadata"]["counts"] = standard_counts(ds)
    ds["metadata"]["topic_counts"] = dict(Counter(t for c in companies for p in c["people"] for e in p["speaker_evidence"] for t in e["topics"]).most_common())
    json.dump(ds, open(out_path, "w"), ensure_ascii=False, indent=2)
    print(f"wrote {out_path}: {ds['metadata']['counts']['companies']} companies, {ds['metadata']['counts']['people']} people")


if __name__ == "__main__":
    main()
