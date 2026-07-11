# dbt-meetups pipeline

Incremental, idempotent pipeline that keeps `raw_events/`, `enriched/`,
`pipeline/speaker-identities.json`, and the dashboard up to date. Running it
twice in a row with no new Meetup events changes nothing.

This folder also holds the pipeline's inputs and docs: `dbt-meetup-groups.json`
(the chapter list the scraper iterates), `speaker-identities.json` (step 3's
state), and `past-meetups.md` (the schema, topic vocabulary, and enrichment
rules that `enrich.py`'s prompt is built from).

## One command

```sh
pipeline/run_pipeline.sh                                   # all groups
pipeline/run_pipeline.sh --slugs oslo-dbt-group,berlin-dbt-meetup
SKIP_SCRAPE=1 pipeline/run_pipeline.sh                     # re-enrich/rebuild only
```

The script bootstraps `.venv/` with Playwright + Chromium on first run. It's shell-agnostic (works with `bash`, `sh`, `zsh`, etc.).

## Steps

| # | Script | What it does | Incremental via |
|---|---|---|---|
| 1 | `scrape.py` | Lists each group's past events (Meetup GraphQL), scrapes only pages whose `event_id` isn't in `raw_events/<slug>.json`, prepends them | id diff against the raw file |
| 2 | `enrich.py` | For each raw event not yet enriched, calls Claude headlessly (`claude -p`, default model `claude-opus-4-8`) with the schema + 26-topic vocabulary from `past-meetups.md`, appends the structured event to `enriched/<slug>.json`. Cancelled/empty/Coalesce events are excluded and recorded so they're never retried | enriched ids + `enriched/_enrichment_state.json` |
| 3 | `update_speakers.py` | Refreshes `speaker-identities.json`: auto-merges exact-normalized name variants, flags fuzzy near-matches into `pending_review` (human decides), recomputes `repeat_speakers_across_chapters` | pure recompute, stable output |
| 4 | `dashboard/build_dashboard_data.py` (+ `build_dashboard.sh`) | Regenerates `dashboard_data.json` and embeds it into `dashboard/index.html` | full rebuild (cheap) |

## Requirements

- `claude` CLI (found on PATH, via `CLAUDE_BIN`, or auto-detected from the
  VSCode Claude Code extension) with an active login — the enrich step uses it.
- Scraping currently works anonymously. If Meetup starts requiring login, run
  `python pipeline/login.py` once to save a session into `.browser-profile/`.

## Testing against a data copy

Set `DBT_MEETUPS_DATA_DIR` to a directory containing copies of `raw_events/`,
`enriched/`, and `speaker-identities.json`. All steps read/write there instead
of the repo, and the dashboard step writes `dashboard_data.json` into the copy
without touching `dashboard/index.html`:

```sh
DBT_MEETUPS_DATA_DIR=/tmp/testdata pipeline/run_pipeline.sh --slugs oslo-dbt-group
```

## State files

- `enriched/_enrichment_state.json` — per-chapter map of event_ids that were
  deliberately not enriched, with reasons. The initial baseline (2026-07-06)
  marks every pre-pipeline raw/enriched gap as reviewed. Regenerate a baseline
  with `python pipeline/enrich.py --baseline`.
- `raw_events/_enrichment_progress.json` — legacy progress log from the
  original one-off enrichment; not used by the pipeline.

## Adding a new chapter

1. Add the group to `pipeline/dbt-meetup-groups.json`.
2. Add its slug to `dashboard/chapter_geo.py` and `dashboard/chapter_names.py`
   (the dashboard build warns if missing).
3. Run `pipeline/run_pipeline.sh --slugs <new-slug>`.
