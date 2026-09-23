"""Tests for dashboard/build_organiser_data.py.

Run from the repo root: python3 -m unittest discover -s tests -v
"""

import os
import sys
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DASHBOARD_DIR = os.path.join(REPO_ROOT, "dashboard")
FIXTURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "organiser")

sys.path.insert(0, DASHBOARD_DIR)
import build_organiser_data as bod  # noqa: E402


class BuildOrganiserOutputTests(unittest.TestCase):
    """Runs build_output() against two hand-written chapter files in tests/fixtures/organiser/."""

    @classmethod
    def setUpClass(cls):
        output = bod.build_output(source_glob=os.path.join(FIXTURES_DIR, "*_dbt_companies.json"))
        cls.chapters = {c["key"]: c for c in output["chapters"]}
        cls.testtown = cls.chapters["testtown"]
        cls.people = {p["id"]: p for p in cls.testtown["people"]}

    def test_every_chapter_file_is_loaded(self):
        self.assertEqual(set(self.chapters), {"testtown", "othertown"})

    def test_unconfigured_chapter_uses_region_label_and_both_goal(self):
        self.assertEqual(self.testtown["label"], "Testtown")
        self.assertEqual(self.testtown["goal"], "both")

    def test_configured_chapters_have_a_known_goal(self):
        for key, config in bod.CHAPTERS.items():
            self.assertIn(config["goal"], {"speakers", "attendees", "both"}, key)

    def test_vinted_colleagues_are_kept_and_tagged(self):
        self.assertTrue(self.people["vic-colleague"]["internal_vinted"])
        self.assertFalse(self.people["ada-returning"]["internal_vinted"])
        acme = next(c for c in self.testtown["companies"] if c["id"] == "acme")
        self.assertEqual(acme["people_count"], 3)

    def test_tier_outranks_past_talk_for_speakers(self):
        self.assertLess(self.people["tia-tierone"]["speaker_rank"], self.people["ada-returning"]["speaker_rank"])
        self.assertEqual(self.people["ada-returning"]["speaker_rank"], 3)

    def test_emerging_voice_ranks_before_proven_speaker_in_same_tier(self):
        self.assertEqual(self.people["eve-emerging"]["speaker_rank"], 1)
        self.assertEqual(self.people["tia-tierone"]["speaker_rank"], 2)

    def test_lead_type_is_passed_through_with_a_reason(self):
        self.assertEqual(self.people["eve-emerging"]["lead_type"], "emerging_voice")
        self.assertIn("first-time speaker: publishes, no talk yet", self.people["eve-emerging"]["speaker_reasons"])
        self.assertIn("proven speaker", self.people["tia-tierone"]["speaker_reasons"])
        self.assertEqual(self.people["gus-local"]["lead_type"], "no_public_content")

    def test_in_region_people_rank_first_for_attendees(self):
        ranked = sorted(self.testtown["people"], key=lambda p: p["attendee_rank"])
        self.assertEqual(ranked[0]["id"], "gus-local")
        self.assertEqual(ranked[-1]["id"], "tia-tierone")

    def test_only_dbt_evidence_counts_toward_reasons(self):
        self.assertIn("1 public dbt item", self.people["tia-tierone"]["speaker_reasons"])
        self.assertIn("spoke here 2025-05", self.people["ada-returning"]["speaker_reasons"])

    def test_talk_angle_falls_back_to_evidence(self):
        self.assertEqual(self.people["ada-returning"]["talk_angle"], "modeling follow-up")

    def test_community_topic_is_not_a_lead_topic(self):
        self.assertEqual(self.people["tia-tierone"]["topics"], ["semantic layer"])
        topics = {t["topic"] for t in self.testtown["topics"]}
        self.assertNotIn("community", topics)

    def test_topic_coverage_counts_past_talks_and_leads(self):
        coverage = {t["topic"]: t for t in self.testtown["topics"]}
        self.assertEqual(coverage["data modeling"]["past_talks"], 1)
        self.assertEqual(coverage["data modeling"]["last_covered"], "2025-05-01")
        self.assertEqual(coverage["semantic layer"]["past_talks"], 0)
        self.assertEqual(coverage["semantic layer"]["leads"], 1)

    def test_only_job_ads_with_dbt_in_the_text_count(self):
        acme = next(c for c in self.testtown["companies"] if c["id"] == "acme")
        self.assertEqual(acme["dbt_job_count"], 1)
        self.assertEqual(len(acme["jobs"]), 2)

    def test_companies_with_confirmed_presence_rank_first(self):
        self.assertEqual([c["id"] for c in self.testtown["companies"]], ["acme", "shared-co", "globex"])

    def test_people_and_companies_in_two_chapters_are_tagged(self):
        self.assertEqual(self.people["sam-both"]["also_in"], ["Othertown"])
        shared = next(c for c in self.testtown["companies"] if c["id"] == "shared-co")
        self.assertEqual(shared["also_in"], ["Othertown"])
        self.assertEqual(self.people["gus-local"]["also_in"], [])


if __name__ == "__main__":
    unittest.main()
