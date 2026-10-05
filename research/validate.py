"""Checks that <region>_dbt_companies.json files follow the shared schema (research/README.md §4).

usage, from the repo root: python3 research/validate.py [<file> ...]
"""

import json, re, sys
sys.path.insert(0, "pipeline")
from enrich import TOPIC_VOCABULARY as V

TOP = ["metadata","companies","sources","past_meetups","community_channels"]
META = ["title","generated_at","prepared_for","purpose","version","schema_version","region","method",
        "field_definitions","caveats","counts","topic_vocabulary_source","topic_vocabulary","topic_counts"]
COMPANY = ["id","name","type","watchlist","excluded_from_outreach","cities","local_presence","dbt_signal",
           "stack_signals","job_postings","other_evidence","people","notes"]
JOB = ["title","url","source","linkedin_company_name","dbt_mentioned_in_text","dbt_snippet","job_poster",
       "posted_date","last_seen","job_family","work_mode"]
PERSON = ["id","name","pronouns","title","city","based_in_region","level","linkedin_urls","has_linkedin",
          "linkedin_confidence","profile_urls","meetup_fit","lead_type","sourced_via","mentions_dbt","speaker_evidence","attendee_signal","evidence",
          "confidence","internal_vinted","priority_tier","suggested_talk_angle","past_chapter_talks","notes"]
EVID = ["type","event","title","date","url","content_id","co_authors","mentions_dbt","description","topics",
        "suggested_talk_angle","url_precision","confidence"]
PROFILE_TYPES = {"github","meetup","zenn","qiita","velog","medium","devto","substack","ithome","sessionize","x","bluesky","website","note"}
PAST = ["name","date","venue","url","organisers","attendees","talks"]
PAST_TALK = ["speaker","company","title","topics"]

def keys(obj, expected, where):
    assert list(obj) == expected, (where, set(expected) ^ set(obj))

def check(path):
    d = json.load(open(path))
    keys(d, TOP, "top"); keys(d["metadata"], META, "metadata")
    assert d["metadata"]["topic_vocabulary"] == V, "vocabulary out of date"
    people_ids, owner = set(), {}
    for c in d["companies"]:
        keys(c, COMPANY, c["id"])
        for j in c["job_postings"]: keys(j, JOB, j["url"])
        for p in c["people"]:
            keys(p, PERSON, p["id"])
            assert p["id"] not in people_ids, ("duplicate person", p["id"]); people_ids.add(p["id"])
            for u in p["profile_urls"]:
                assert set(u) == {"type", "url", "source"} and u["type"] in PROFILE_TYPES and u["url"].startswith("http"), (p["id"], u)
                assert owner.setdefault(u["url"], p["id"]) == p["id"], ("profile shared by two people; merge them or drop the link", u["url"], owner[u["url"]], p["id"])
            for u in p["linkedin_urls"]:
                slug = "linkedin:" + re.sub(r"^.*linkedin\.com/in/", "", u).split("?")[0].strip("/").lower()
                assert owner.setdefault(slug, p["id"]) == p["id"], ("linkedin profile shared by two people; merge them or drop the link", u, owner[slug], p["id"])
            for e in p["speaker_evidence"]:
                keys(e, EVID, (p["id"], e["title"]))
                assert 1 <= len(e["topics"]) <= 3 and all(t in V for t in e["topics"]), (p["id"], e["title"])
    for m in d["past_meetups"]:
        keys(m, PAST, m["name"])
        for t in m["talks"]:
            keys(t, PAST_TALK, t["title"])
            assert all(x in V for x in (t["topics"] or [])), t["title"]
    return d

if __name__ == "__main__":
    import glob
    # with no arguments, check every chapter file; berlin's field_definitions are the reference
    files = (sys.argv[1:] or sorted(p for p in glob.glob("*/*_dbt_companies.json") if "berlin" not in p)) + ["berlin_planning/berlin_dbt_companies.json"]
    ds = [check(f) for f in files]
    ref = ds[-1]
    for d in ds:
        assert d["metadata"]["field_definitions"] == ref["metadata"]["field_definitions"], "field_definitions differ"
        assert list(d["metadata"]["counts"]) == list(ref["metadata"]["counts"]), "counts keys differ"
        assert d["metadata"]["schema_version"] == ref["metadata"]["schema_version"]
    print("ok")
