# dbt-meetups pipeline

An incremental pipeline that keeps `raw_events/`, `enriched/`, `pipeline/speaker-identities.json` and the dashboard up to date. It is idempotent: running it twice with no new Meetup events changes nothing.

This folder also holds the pipeline's inputs and docs:

- **`dbt-meetup-groups.json`** — the list of chapters the scraper works through.
- **`speaker-identities.json`** — the state written by step 3.
- **`past-meetups.md`** — the schema, topic vocabulary and enrichment rules. The `enrich.py` prompt is built from it.

## One command

```sh
# all groups
pipeline/run_pipeline.sh

# only some groups
pipeline/run_pipeline.sh --slugs oslo-dbt-group,berlin-dbt-meetup

# re-enrich and rebuild without scraping
SKIP_SCRAPE=1 pipeline/run_pipeline.sh
```

> **Note:** on its first run, the script sets up `.venv/` with Playwright and Chromium. It runs under bash whatever shell you call it from.

## Steps

### 1. Scrape — `scrape.py`

Lists each group's past events through Meetup's GraphQL API. It scrapes only events whose `event_id` isn't already in `raw_events/<slug>.json`, and adds them to the top of that file.

**Incremental via:** comparing ids against the raw file.

### 2. Enrich — `enrich.py`

Sends each raw event that isn't enriched yet to Claude, run headlessly (`claude -p`, default model `claude-opus-4-8`). The prompt carries the schema and 26-topic vocabulary from `past-meetups.md`. The structured event is appended to `enriched/<slug>.json`. Cancelled, empty and Coalesce events are skipped and recorded, so they are never retried.

**Incremental via:** the ids already in `enriched/`, plus `enriched/_enrichment_state.json`.

### 3. Speakers — `update_speakers.py`

Refreshes `speaker-identities.json`. Name variants that match once normalized are merged automatically. Near-matches go into `pending_review` for a person to decide. It then recomputes `repeat_speakers_across_chapters`.

**Incremental via:** nothing needed. It recomputes everything, and the output is the same each time.

### 4. Dashboard — `dashboard/build_dashboard_data.py` (run by `build_dashboard.sh`)

Regenerates `dashboard_data.json` and embeds it into `dashboard/index.html`.

**Incremental via:** nothing needed. A full rebuild is cheap.

## Requirements

- **The `claude` CLI, logged in.** Step 2 needs it. The pipeline looks for it in `CLAUDE_BIN` first, then on your `PATH`, then inside the VS Code Claude Code extension.
- **No Meetup login, for now.** Scraping works anonymously. If Meetup starts requiring a login, run `python pipeline/login.py` once. It saves a session into `.browser-profile/`.

## Testing against a copy of the data

Point `DBT_MEETUPS_DATA_DIR` at a folder holding copies of `raw_events/`, `enriched/` and `speaker-identities.json`. Every step then reads and writes there instead of the repo. The dashboard step writes `dashboard_data.json` into the copy and leaves `dashboard/index.html` alone.

```sh
DBT_MEETUPS_DATA_DIR=/tmp/testdata pipeline/run_pipeline.sh --slugs oslo-dbt-group
```

## State files

- **`enriched/_enrichment_state.json`** — for each chapter, the event ids deliberately left unenriched, with the reason. The first baseline (2026-07-06) marks every gap that existed before the pipeline as reviewed. To regenerate a baseline, run `python pipeline/enrich.py --baseline`.
- **`raw_events/_enrichment_progress.json`** — an old progress log from the original one-off enrichment. The pipeline doesn't use it.

## Adding a new chapter

1. Add the group to `pipeline/dbt-meetup-groups.json`.
2. Add its slug to `dashboard/chapter_geo.py` and `dashboard/chapter_names.py`. The dashboard build warns if either is missing.
3. Run the pipeline for it:

   ```sh
   pipeline/run_pipeline.sh --slugs <new-slug>
   ```
