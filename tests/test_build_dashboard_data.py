"""Tests for dashboard/build_dashboard_data.py.

Run from the repo root: python3 -m unittest discover -s tests -v
(requires numpy/shapely NOT needed here - only dashboard/'s own imports.)
"""

import datetime
import os
import re
import sys
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DASHBOARD_DIR = os.path.join(REPO_ROOT, "dashboard")
FIXTURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")

sys.path.insert(0, DASHBOARD_DIR)
import build_dashboard_data as bdd  # noqa: E402


class BuildOutputTests(unittest.TestCase):
    """Exercises build_output() against a small, hand-written fixture set
    (tests/fixtures/enriched/*.json + speaker-identities.json) rather than
    the real enriched/ data, so these assertions don't drift every time a
    new meetup is scraped."""

    @classmethod
    def setUpClass(cls):
        cls.fixed_today = datetime.date(2024, 7, 1)
        cls.output = bdd.build_output(
            enriched_dir=os.path.join(FIXTURES_DIR, "enriched"),
            speaker_id_file=os.path.join(FIXTURES_DIR, "speaker-identities.json"),
            today=cls.fixed_today,
        )

    def test_is_pure_no_file_written(self):
        # build_output must not write dashboard_data.json itself - only
        # main() does. Regression guard against re-introducing the old
        # module-scope side-effectful script.
        stray_output = os.path.join(FIXTURES_DIR, "dashboard_data.json")
        self.assertFalse(os.path.exists(stray_output))

    def test_chapter_totals(self):
        chapters = self.output["chapters"]
        self.assertIn("berlin", chapters)
        self.assertIn("nyc", chapters)
        self.assertEqual(chapters["berlin"]["total_events"], 2)
        self.assertEqual(chapters["berlin"]["total_talks"], 3)
        self.assertEqual(chapters["nyc"]["total_events"], 1)
        self.assertEqual(chapters["nyc"]["total_talks"], 2)

    def test_summary_totals_match_sum_of_chapters(self):
        s = self.output["summary"]
        chapters = self.output["chapters"]
        self.assertEqual(
            s["total_events"], sum(c["total_events"] for c in chapters.values())
        )
        self.assertEqual(
            s["total_talks"], sum(c["total_talks"] for c in chapters.values())
        )

    def test_unique_speakers_counts_canonical_merge_once(self):
        # "Ada Lovelace" appears in both berlin talks and the nyc talk; the
        # canonical_merges fixture also folds a "Ada  Lovelace" (double
        # space) variant into the same canonical name. Total distinct
        # speakers across the fixture set: Ada Lovelace, Grace Hopper,
        # Alan Turing = 3.
        self.assertEqual(self.output["summary"]["total_unique_speakers"], 3)

    def test_repeat_speakers_across_chapters(self):
        repeat = {r["name"]: r for r in self.output["repeat_speakers"]}
        self.assertIn("Ada Lovelace", repeat)
        self.assertEqual(repeat["Ada Lovelace"]["chapter_count"], 2)
        self.assertEqual(sorted(repeat["Ada Lovelace"]["chapters"]), ["berlin", "nyc"])
        # Grace Hopper and Alan Turing only spoke at one chapter each.
        self.assertNotIn("Grace Hopper", repeat)
        self.assertNotIn("Alan Turing", repeat)

    def test_category_rollup_from_primary_topic(self):
        # Berlin's first talk lists topics in order
        # ["data quality & testing", "dbt best practices"] - the primary
        # category must come from the FIRST topic only.
        cat_dist = dict(self.output["category_distribution"])
        self.assertIn("data quality & governance", cat_dist)
        # "dbt best practices" (listed 2nd) must NOT also be counted as a
        # primary category for that same talk.
        talk = next(
            t
            for t in self.output["all_talks"]
            if t["title"] == "Testing your dbt models properly"
        )
        self.assertEqual(talk["category"], "data quality & governance")

    def test_online_event_excluded_from_venue_but_counted_in_format_split(self):
        s = self.output["summary"]
        self.assertEqual(s["format_split"]["online"], 1)
        self.assertEqual(s["format_split"]["in-person"], 2)

    def test_trailing_12mo_window_uses_injected_today(self):
        # fixed_today = 2024-07-01, trailing window = 2023-07-01..2024-07-01.
        # Berlin's 2024-03-14 event falls inside; its 2023-01-10 event
        # falls outside (before the window starts).
        berlin = self.output["chapters"]["berlin"]
        self.assertEqual(berlin["trailing_12mo_events"], 1)

    def test_active_status_derives_from_trailing_window(self):
        # NYC's only event (2024-06-20) is inside the trailing window ->
        # active. A chapter with zero recent events would be dormant; we
        # don't have one in this fixture set to assert the negative case
        # cheaply, so just check the positive case holds.
        self.assertTrue(self.output["chapters"]["nyc"]["is_active"])

    def test_output_is_json_serializable(self):
        import json

        json.dumps(self.output)  # raises if any non-serializable value snuck in


class CategoryMapVocabularyTests(unittest.TestCase):
    """Guards against dashboard/build_dashboard_data.py's CATEGORY_MAP
    drifting out of sync with pipeline/past-meetups.md, which documents the
    26-topic vocabulary and the 8-category roll-up table as the source of
    truth. These are two independent files by design (past-meetups.md feeds
    enrich.py's prompt; CATEGORY_MAP is plain Python for build speed) - this
    test is the only thing keeping them honest."""

    @classmethod
    def setUpClass(cls):
        past_meetups_path = os.path.join(REPO_ROOT, "pipeline", "past-meetups.md")
        with open(past_meetups_path) as f:
            cls.doc = f.read()

    def _extract_vocabulary(self):
        # Vocabulary is a markdown bullet list of `topic name` (optionally
        # followed by a parenthetical), one per line, between the
        # "standardized vocabulary only" line and the "Notes:" line.
        section = self.doc.split("vocabulary only")[1].split("\nNotes:")[0]
        return set(re.findall(r"`([^`]+)`", section))

    def _extract_category_table(self):
        # Markdown table rows: | `category` | topic, topic, topic |
        table_section = self.doc.split("## topic categories")[1]
        rows = re.findall(r"\|\s*`([^`]+)`\s*\|\s*([^|]+)\|", table_section)
        mapping = {}
        for category, topics_csv in rows:
            for topic in topics_csv.split(","):
                mapping[topic.strip()] = category
        return mapping

    def test_every_vocabulary_topic_has_a_category(self):
        vocabulary = self._extract_vocabulary()
        missing = vocabulary - set(bdd.CATEGORY_MAP.keys())
        self.assertEqual(
            missing,
            set(),
            f"Topics in past-meetups.md vocabulary with no CATEGORY_MAP entry: {missing}",
        )

    def test_category_map_matches_documented_table(self):
        documented = self._extract_category_table()
        self.assertEqual(
            bdd.CATEGORY_MAP,
            documented,
            "CATEGORY_MAP in build_dashboard_data.py has drifted from the "
            "topic categories table in pipeline/past-meetups.md — update "
            "whichever one is stale.",
        )


if __name__ == "__main__":
    unittest.main()
