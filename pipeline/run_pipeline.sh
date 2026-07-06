#!/bin/bash
# End-to-end incremental pipeline:
#   1. scrape   — fetch new past events into raw_events/
#   2. enrich   — structure new raw events into enriched/ via `claude -p`
#   3. speakers — refresh speaker-identities.json
#   4. dashboard — regenerate dashboard data (and index.html for the real data)
#
# Idempotent: a second run with no new Meetup events changes nothing.
#
# Usage:
#   pipeline/run_pipeline.sh                          # all groups
#   pipeline/run_pipeline.sh --slugs oslo-dbt-group,taipei-dbt-meetup
#   DBT_MEETUPS_DATA_DIR=/path/to/copy pipeline/run_pipeline.sh ...   # run against a data copy
#   SKIP_SCRAPE=1 pipeline/run_pipeline.sh            # skip the scrape step
set -euo pipefail
cd "$(dirname "$0")/.."

PY=".venv/bin/python"
if [ ! -x "$PY" ]; then
  echo "No .venv found — creating one with playwright..."
  python3 -m venv .venv
  .venv/bin/pip install -q playwright
  .venv/bin/python -m playwright install chromium
fi

SLUGS_ARGS=()
if [ "${1:-}" = "--slugs" ] && [ -n "${2:-}" ]; then
  SLUGS_ARGS=(--slugs "$2")
fi

if [ "${SKIP_SCRAPE:-0}" != "1" ]; then
  echo "== 1/4 scrape =="
  "$PY" pipeline/scrape.py "${SLUGS_ARGS[@]}"
else
  echo "== 1/4 scrape (skipped) =="
fi

echo "== 2/4 enrich =="
"$PY" pipeline/enrich.py "${SLUGS_ARGS[@]}"

echo "== 3/4 speakers =="
"$PY" pipeline/update_speakers.py

echo "== 4/4 dashboard =="
if [ -n "${DBT_MEETUPS_DATA_DIR:-}" ]; then
  # Test/copy mode: build dashboard data next to the data copy, leave the
  # committed dashboard/index.html untouched.
  DASHBOARD_ENRICHED_DIR="$DBT_MEETUPS_DATA_DIR/enriched" \
  DASHBOARD_SPEAKER_FILE="$DBT_MEETUPS_DATA_DIR/speaker-identities.json" \
  DASHBOARD_OUTPUT_FILE="$DBT_MEETUPS_DATA_DIR/dashboard_data.json" \
    "$PY" dashboard/build_dashboard_data.py
else
  ./dashboard/build_dashboard.sh
fi

echo "pipeline done."
