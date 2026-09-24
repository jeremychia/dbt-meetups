"""Builds organiser/organiser_data.json from every <region>_dbt_companies.json in the repo.

The files follow the shared schema in berlin_planning/SEARCH_METHOD.md §3.
"""

import glob
import json
import os
from collections import Counter, defaultdict

DASHBOARD_DIR = os.path.dirname(os.path.abspath(__file__))
ANALYSIS_DIR = os.path.dirname(DASHBOARD_DIR)
SOURCE_GLOB = os.environ.get(
    "ORGANISER_SOURCE_GLOB", os.path.join(ANALYSIS_DIR, "*", "*_dbt_companies.json")
)
OUTPUT_FILE = os.environ.get(
    "ORGANISER_OUTPUT_FILE",
    os.path.join(DASHBOARD_DIR, "organiser", "organiser_data.json"),
)

# keyed by the file name before "_dbt_companies.json"; a file with no entry still loads, with goal "both".
# goal decides which view the cockpit opens on: speakers, attendees or both.
CHAPTERS = {
    "berlin": {"label": "Berlin", "goal": "speakers"},
    "lithuania": {"label": "Vilnius", "goal": "attendees"},
    "kuala_lumpur": {"label": "Kuala Lumpur", "goal": "speakers"},
    "paris": {"label": "Paris", "goal": "speakers"},
}

TIER_ORDER = {"1": 0, "2": 1, "backup": 2, "3": 3, "connector": 4, "organiser": 5}
# within a tier, emerging voices (publish, but no talk yet) come before proven speakers:
# the meetup wants to give first-time speakers a chance. See SEARCH_METHOD.md "Outreach order".
LEAD_ORDER = {"emerging_voice": 0, "proven_speaker": 1, "featured": 2, "no_public_content": 3}
LEAD_REASONS = {
    "emerging_voice": "first-time speaker: publishes, no talk yet",
    "proven_speaker": "proven speaker",
}
POTENTIAL_ORDER = {"high": 0, "medium": 1, "low": 2}
SIGNAL_ORDER = {"strong": 0, "medium": 1, "nice-to-have": 2, "weak": 3, "none": 4}
PRESENCE_ORDER = {"confirmed": 0, "not_confirmed": 1, "none": 2}
REGION_ORDER = {True: 0, None: 1, False: 2}


def chapter_key(path):
    return os.path.basename(path).removesuffix("_dbt_companies.json")


def latest_date(dates):
    dates = [d for d in dates if d]
    return max(dates) if dates else None


def shape_person(person, company, label):
    evidence = [
        {
            "type": e["type"],
            "event": e["event"],
            "title": e["title"],
            "date": e["date"],
            "url": e["url"],
            "topics": e["topics"] or [],
            "mentions_dbt": e["mentions_dbt"],
        }
        for e in person["speaker_evidence"]
    ]
    past_talks = person["past_chapter_talks"]
    topics = []
    for item in past_talks + evidence:
        for t in item.get("topics") or []:
            if t != "community" and t not in topics:
                topics.append(t)
    talk_angle = person["suggested_talk_angle"] or next(
        (e["suggested_talk_angle"] for e in person["speaker_evidence"] if e["suggested_talk_angle"]),
        None,
    )
    dbt_items = sum(1 for e in evidence if e["mentions_dbt"])
    tier = str(person["priority_tier"])
    fit = person["meetup_fit"]
    last_talk = latest_date([t["date"] for t in past_talks])

    lead_type = person["lead_type"]
    speaker_reasons = []
    if lead_type in LEAD_REASONS:
        speaker_reasons.append(LEAD_REASONS[lead_type])
    if last_talk:
        speaker_reasons.append(f"spoke here {last_talk[:7]}")
    if tier in ("1", "2"):
        speaker_reasons.append(f"tier {tier} lead")
    elif tier in ("backup", "connector", "organiser"):
        speaker_reasons.append(tier)
    if dbt_items:
        speaker_reasons.append(f"{dbt_items} public dbt item{'s' if dbt_items > 1 else ''}")
    elif evidence:
        speaker_reasons.append(f"{len(evidence)} public item{'s' if len(evidence) > 1 else ''}, none on dbt")

    attendee_reasons = []
    if person["based_in_region"] is True:
        attendee_reasons.append(f"based in {label}")
    elif person["based_in_region"] is False:
        attendee_reasons.append("based elsewhere")
    else:
        attendee_reasons.append("location unverified")
    if company["dbt_signal"] in ("strong", "medium"):
        attendee_reasons.append(f"{company['dbt_signal']} dbt signal at company")
    if person["mentions_dbt"]:
        attendee_reasons.append("mentions dbt publicly")

    return {
        "id": person["id"],
        "name": person["name"],
        "title": person["title"],
        "city": person["city"],
        "based_in_region": person["based_in_region"],
        "level": person["level"],
        "linkedin": person["linkedin_urls"][0] if person["linkedin_urls"] else None,
        "linkedin_confidence": person["linkedin_confidence"],
        "confidence": person["confidence"],
        "speaker_potential": fit["speaker_potential"],
        "attendee_potential": fit["attendee_potential"],
        "mentions_dbt": person["mentions_dbt"],
        "lead_type": lead_type,
        "priority_tier": tier,
        "talk_angle": talk_angle,
        "past_talks": past_talks,
        "evidence": evidence,
        "topics": topics,
        "last_active": latest_date([last_talk] + [e["date"] for e in evidence]),
        "notes": person["notes"] or None,
        "internal_vinted": person["internal_vinted"],
        "company_id": company["id"],
        "company_name": company["name"],
        "company_dbt_signal": company["dbt_signal"],
        "company_excluded": company["excluded_from_outreach"],
        "speaker_reasons": speaker_reasons,
        "attendee_reasons": attendee_reasons,
        "_dbt_items": dbt_items,
    }


def speaker_sort_key(p):
    return (
        TIER_ORDER.get(p["priority_tier"], 9),
        LEAD_ORDER.get(p["lead_type"], 9),
        POTENTIAL_ORDER.get(p["speaker_potential"], 9),
        0 if p["past_talks"] else 1,
        -p["_dbt_items"],
    )


def attendee_sort_key(p):
    return (
        REGION_ORDER.get(p["based_in_region"], 9),
        POTENTIAL_ORDER.get(p["attendee_potential"], 9),
        SIGNAL_ORDER.get(p["company_dbt_signal"], 9),
        0 if p["mentions_dbt"] else 1,
        p["name"],
    )


def company_sort_key(c):
    return (
        1 if c["excluded_from_outreach"] else 0,
        PRESENCE_ORDER.get(c["local_presence"], 9),
        1 if c["watchlist"] else 0,
        SIGNAL_ORDER.get(c["dbt_signal"], 9),
        -c["dbt_job_count"],
        -c["people_count"],
        c["name"],
    )


def shape_company(company, people_count):
    dbt_jobs = [j for j in company["job_postings"] if j["dbt_mentioned_in_text"]]
    return {
        "id": company["id"],
        "name": company["name"],
        "type": company["type"],
        "cities": company["cities"],
        "local_presence": company["local_presence"],
        "dbt_signal": company["dbt_signal"],
        "watchlist": company["watchlist"],
        "excluded_from_outreach": company["excluded_from_outreach"],
        "stack": company["stack_signals"],
        "jobs": [
            {"title": j["title"], "url": j["url"], "posted_date": j["posted_date"], "last_seen": j["last_seen"]}
            for j in company["job_postings"]
        ],
        "dbt_job_count": len(dbt_jobs),
        "people_count": people_count,
        "notes": company["notes"] or None,
    }


def topic_coverage(vocabulary, past_meetups, people):
    past = Counter()
    last_covered = {}
    for meetup in past_meetups:
        for talk in meetup["talks"]:
            for t in talk["topics"]:
                past[t] += 1
                last_covered[t] = latest_date([last_covered.get(t), meetup["date"]])
    leads = Counter(t for p in people for t in p["topics"])
    return [
        {"topic": t, "past_talks": past[t], "last_covered": last_covered.get(t), "leads": leads[t]}
        for t in vocabulary
        if t != "community"
    ]


def build_chapter(path):
    with open(path) as f:
        data = json.load(f)
    key = chapter_key(path)
    config = CHAPTERS.get(key, {})
    label = config.get("label", data["metadata"]["region"])

    people, companies = [], []
    for company in data["companies"]:
        people.extend(shape_person(p, company, label) for p in company["people"])
        companies.append(shape_company(company, len(company["people"])))

    # stable sort: people tied on the speaker key keep newest-activity-first order
    by_recency = sorted(people, key=lambda p: p["last_active"] or "", reverse=True)
    for rank, p in enumerate(sorted(by_recency, key=speaker_sort_key), 1):
        p["speaker_rank"] = rank
    for rank, p in enumerate(sorted(people, key=attendee_sort_key), 1):
        p["attendee_rank"] = rank
    companies.sort(key=company_sort_key)
    for p in people:
        del p["_dbt_items"]

    past_meetups = sorted(data["past_meetups"], key=lambda m: m["date"], reverse=True)
    return {
        "key": key,
        "label": label,
        "goal": config.get("goal", "both"),
        "region": data["metadata"]["region"],
        "generated_at": data["metadata"]["generated_at"],
        "version": data["metadata"]["version"],
        "caveats": data["metadata"]["caveats"],
        "channels": data["community_channels"],
        "past_meetups": [
            {"name": m["name"], "date": m["date"], "url": m["url"], "attendees": m["attendees"], "talks": m["talks"]}
            for m in past_meetups
        ],
        "topics": topic_coverage(data["metadata"]["topic_vocabulary"], data["past_meetups"], people),
        "people": sorted(people, key=lambda p: p["speaker_rank"]),
        "companies": companies,
    }


def mark_cross_chapter(chapters):
    """Tags people and companies that appear in more than one chapter's file."""
    person_chapters, company_chapters = defaultdict(set), defaultdict(set)
    for ch in chapters:
        for p in ch["people"]:
            person_chapters[p["id"]].add(ch["label"])
        for c in ch["companies"]:
            company_chapters[c["id"]].add(ch["label"])
    for ch in chapters:
        for p in ch["people"]:
            p["also_in"] = sorted(person_chapters[p["id"]] - {ch["label"]})
        for c in ch["companies"]:
            c["also_in"] = sorted(company_chapters[c["id"]] - {ch["label"]})


def build_output(source_glob=SOURCE_GLOB):
    paths = sorted(p for p in glob.glob(source_glob) if "/.venv/" not in p)
    chapters = [build_chapter(p) for p in paths]
    mark_cross_chapter(chapters)
    return {"chapters": chapters}


def main():
    output = build_output()
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, ensure_ascii=False)
    labels = ", ".join(c["label"] for c in output["chapters"])
    print(f"organiser_data.json written ({labels})")


if __name__ == "__main__":
    main()
