"""Shared paths for the dbt-meetups pipeline.

All data locations resolve relative to DBT_MEETUPS_DATA_DIR when set, which
lets tests run the whole pipeline against a copy of the data without touching
the real raw_events/ and enriched/ directories.
"""
import os
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
REPO_DIR = PIPELINE_DIR.parent

DATA_DIR = Path(os.environ.get("DBT_MEETUPS_DATA_DIR", REPO_DIR))

RAW_EVENTS_DIR = DATA_DIR / "raw_events"
ENRICHED_DIR = DATA_DIR / "enriched"
# speaker-identities.json lives in pipeline/ normally, but inside the data
# copy when DBT_MEETUPS_DATA_DIR is set (tests copy it alongside the data).
if "DBT_MEETUPS_DATA_DIR" in os.environ:
    SPEAKER_ID_FILE = DATA_DIR / "speaker-identities.json"
else:
    SPEAKER_ID_FILE = PIPELINE_DIR / "speaker-identities.json"
# Tracks event_ids that were deliberately not enriched (cancelled events,
# Coalesce watch parties, empty pages) so reruns stay idempotent.
ENRICHMENT_STATE_FILE = ENRICHED_DIR / "_enrichment_state.json"

GROUPS_FILE = PIPELINE_DIR / "dbt-meetup-groups.json"
# Browser profile always lives at the repo root (login session is shared,
# never part of the test data copy).
PROFILE_DIR = REPO_DIR / ".browser-profile"


def chapter_slug(filename: str) -> str:
    """Short chapter key used in speaker-identities.json, e.g. 'berlin'."""
    return (
        filename.replace("-dbt-meetup-group.json", "")
        .replace("-dbt-meetup.json", "")
        .replace(".json", "")
    )
