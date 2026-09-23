# dbt-meetups

A cross-chapter analysis of the ~75 [dbt](https://www.getdbt.com/) Meetup groups worldwide. It scrapes events, talks, speakers and topics from Meetup.com. An LLM structures them, and the results are published as a static dashboard.

**Live dashboard:** deployed to GitHub Pages on every push to `main` (see `.github/workflows/deploy-dashboard.yml`).

## How it fits together

```
1. scrape.py                 Meetup.com                 --> raw_events/*.json
2. enrich.py                 raw_events/*.json          --> enriched/*.json
3. update_speakers.py        enriched/*.json            --> speaker-identities.json
4. build_dashboard_data.py   enriched/*.json
                             + speaker-identities.json  --> dashboard/dashboard_data.json
                                                        --> dashboard/index.html
```

### Data files

- **`raw_events/*.json`** — the scraped page text and basic metadata (dates, RSVPs, location), straight from Meetup. One file per chapter.
- **`enriched/*.json`** — the same events after an LLM has pulled out each talk's title, speaker and topics. Every record follows a fixed schema and a 26-topic vocabulary. This is the closest thing the project has to a modeled layer.
- **`pipeline/speaker-identities.json`** — matches speakers across chapters. For example, one person whose name is spelled two ways in two chapters.
- **`dashboard/dashboard_data.json`** — what the dashboard reads. It holds per-chapter stats, topic and category rollups, and growth over time. It is rebuilt from `enriched/*.json` on every build.

### Further docs

- **Pipeline:** [`pipeline/README.md`](pipeline/README.md) covers each script, its flags, its state files, and how to add a chapter.
- **Schema and topics:** [`pipeline/past-meetups.md`](pipeline/past-meetups.md) defines the enrichment schema and topic vocabulary. The `enrich.py` prompt is built from it.

## Quick start

### Install

```sh
pip install -r requirements.txt
python -m playwright install chromium
```

### Run the pipeline

```sh
# scrape, enrich and rebuild one chapter
pipeline/run_pipeline.sh --slugs oslo-dbt-group

# all ~75 chapters (slow: calls an LLM for each new event)
pipeline/run_pipeline.sh
```

> **Tip:** `pipeline/run_pipeline.sh` sets up `.venv/` itself if you skip the install step. See `pipeline/README.md` for the full flag list, such as `SKIP_SCRAPE=1` or `DBT_MEETUPS_DATA_DIR=...` to test against a copy of the data.

## Running the tests

```sh
python3 -m unittest discover -s tests -v
```

- **Fixture data.** Tests run against small files in `tests/fixtures/`, not the real `enriched/` directory. So they stay fast and don't change as new meetups are scraped.
- **Docs and code stay in sync.** `CategoryMapVocabularyTests` reads the category-rollup table in `pipeline/past-meetups.md`. It checks that table matches `CATEGORY_MAP` in `dashboard/build_dashboard_data.py`. Without it, the two files could drift apart silently.
- **CI.** The suite runs before every dashboard deploy (`.github/workflows/deploy-dashboard.yml`). It also runs on every push and pull request (`.github/workflows/test.yml`).

## Design decisions

This project analyzes dbt Meetups, but **it does not use dbt, SQL or a database.** Here is why.

### 1. The data fits in memory

~75 chapters, ~500 events, ~1,000 talks. That is a few megabytes of JSON. A warehouse and a dbt project would mean a database to run, credentials to manage and a second toolchain. None of that solves a problem this data has.

### 2. The hard step is LLM extraction, not SQL

The real work is turning a Meetup page's raw text into a list of talks, speakers and topics. The source isn't structured, so SQL can't do it. The `enrich.py` prompt (built from `pipeline/past-meetups.md`) is the transformation. What's left afterwards is a few hundred lines of Python aggregation.

### 3. Static output, not a query engine

The end product is a dashboard, not a place for ad-hoc SQL. `dashboard_data.json` is computed once per pipeline run and served as a static file. That keeps hosting to GitHub Pages, with no backend. The whole data model lives in one function, `build_dashboard_data.build_output()`.

### 4. It is still modeled, just not with dbt

- **`enriched/*.json` is the staging layer.** Every event has a fixed schema. Every talk uses a controlled topic vocabulary, not free text.
- **`build_dashboard_data.py` is the mart.** It reads the staging layer and produces the aggregates the dashboard needs.

A warehouse and dbt would earn their complexity past a few thousand events. The same goes for several people writing separate transformations on the same data. The project hasn't reached that point.

## Known limitations

- **Validation only warns.** `enrich.py` checks each record against the schema and topic vocabulary. On failure it prints a warning but keeps the record. If a chapter's data looks wrong, look for `WARNING:` lines in the last run's output.
- **Only direct dependencies are pinned.** `requirements.txt` pins `playwright`, `numpy` and `shapely`. Their own dependencies aren't locked. If that causes trouble, move to a lockfile (`uv` or `pip-compile`).
- **Raw files can hold personal details.** `raw_events/*.json` keeps the scraped page text as-is. That can include contact details that were public on Meetup, such as an organizer's email in an event description. Check before sharing `raw_events/` beyond this repo.
