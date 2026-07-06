# dbt-meetups

Cross-chapter analysis of the ~75 [dbt](https://www.getdbt.com/) Meetup groups
worldwide: events, talks, speakers, and topics, scraped from Meetup.com,
structured by an LLM, and published as a static dashboard.

**Live dashboard:** deployed via GitHub Pages on every push to `main` (see
`.github/workflows/deploy-dashboard.yml`).

## How it fits together

```
1. scrape.py            Meetup.com        --> raw_events/*.json
2. enrich.py             raw_events/*.json --> enriched/*.json
3. update_speakers.py    enriched/*.json   --> speaker-identities.json
4. build_dashboard_data.py   enriched/*.json + speaker-identities.json
                                            --> dashboard/dashboard_data.json
                                            --> dashboard/index.html
```

- **`raw_events/*.json`** — one file per chapter, the scraped page text and
  structured metadata (dates, RSVPs, location) straight from Meetup.
- **`enriched/*.json`** — the same events, with an LLM structuring each
  event's talks (title, speaker, topics) against a fixed schema and 26-topic
  vocabulary. This is the closest thing this project has to a "modeled"
  layer.
- **`pipeline/speaker-identities.json`** — cross-chapter speaker
  de-duplication (the same person's name spelled two different ways across
  two chapters' events).
- **`dashboard/dashboard_data.json`** — the aggregated output the dashboard
  actually reads: per-chapter stats, topic/category rollups, growth-over-time
  series, computed fresh from `enriched/*.json` on every build.

Full step-by-step docs (what each script does, flags, state files, how to add
a new chapter) live in [`pipeline/README.md`](pipeline/README.md). The
enrichment schema and topic vocabulary are documented in
[`pipeline/past-meetups.md`](pipeline/past-meetups.md) — that file is the
source of truth `enrich.py`'s prompt is built from.

## Quick start

```sh
pip install -r requirements.txt
python -m playwright install chromium

pipeline/run_pipeline.sh --slugs oslo-dbt-group   # scrape + enrich + rebuild, one chapter
pipeline/run_pipeline.sh                          # all ~75 chapters (slow, calls an LLM per new event)
```

`pipeline/run_pipeline.sh` bootstraps `.venv/` automatically if you skip the
manual install above. See `pipeline/README.md` for the full flag list
(`SKIP_SCRAPE=1`, `DBT_MEETUPS_DATA_DIR=...` for testing against a data copy).

## Running the tests

```sh
python3 -m unittest discover -s tests -v
```

Tests run against small fixture data in `tests/fixtures/`, not the real
`enriched/` directory, so they're fast and don't drift as new meetups get
scraped. One test (`CategoryMapVocabularyTests`) parses
`pipeline/past-meetups.md` directly and asserts the category-rollup table
documented there matches the `CATEGORY_MAP` dict hardcoded in
`dashboard/build_dashboard_data.py` — those two are independent files by
design (see below) and this is what keeps them from silently drifting apart.

CI (`.github/workflows/deploy-dashboard.yml`) runs this suite before every
dashboard rebuild/deploy, and `.github/workflows/test.yml` runs it on every
push and pull request.

## Design decisions

**No dbt, no database, no dimensional modeling.** This project analyzes dbt
Meetups but doesn't itself use dbt, which is worth explaining since it's the
obvious question.

- **The whole "warehouse" fits in memory.** ~75 chapters, ~500 events, ~1,000
  talks. That's a few megabytes of JSON. A star schema, a warehouse, and a
  dbt project modeling `fct_talks`/`dim_speakers` would add real
  infrastructure (a database to run, credentials to manage, a second
  toolchain to learn) to solve a problem this data doesn't have. dbt earns
  its keep when you're transforming data in a warehouse, at scale, with a
  team; there's no warehouse here, no scale problem, and no team of
  analysts writing competing SQL against the same tables.
- **The transform is LLM extraction, not SQL.** The one genuinely hard data
  problem in this project — turning "a scraped Meetup page's raw text" into
  "a list of structured talks with speakers and topics" — isn't expressible
  as a SQL transformation over structured source tables, because the source
  isn't structured. `enrich.py`'s prompt (built from
  `pipeline/past-meetups.md`) *is* the transformation logic; a dbt model
  would have nothing to do once that step is done, because the remaining
  aggregation (group by chapter, roll up categories, compute trailing
  windows) is a couple hundred lines of Python over data that already fits
  in a `dict`.
- **Static output, not a queryable warehouse.** The end product is a
  dashboard, not a place for analysts to write ad-hoc SQL. Precomputing
  `dashboard_data.json` once per pipeline run and shipping it as a static
  JSON blob the frontend reads client-side is simpler to deploy (GitHub
  Pages, no backend, no query engine) and simpler to reason about (the
  entire "data model" is one Python dict, defined in one place,
  `build_dashboard_data.build_output()`) than standing up a database to
  serve the same handful of aggregate queries.
- **What *is* modeled, just not with dbt:** `enriched/*.json` is the
  structured/typed layer (the "staging models," if you like the analogy) —
  every event has a fixed schema, every talk has a controlled topic
  vocabulary rather than free text. `build_dashboard_data.py` is the "mart" —
  it reads the staging layer and produces the aggregates the dashboard
  needs. The transformation logic just lives in Python functions and an LLM
  prompt instead of `.sql` files, because the inputs and the scale don't
  call for anything heavier.

If this ever needed to scale past a few thousand events, or needed multiple
people writing independent transformations against the same underlying data,
that's exactly the point where introducing a real warehouse + dbt would earn
its complexity. This project hasn't reached that point yet.

## Known limitations

- **Advisory-only validation.** `enrich.py` checks each enriched record
  against the schema/topic vocabulary but only prints a warning on failure —
  it does not reject bad records. If a chapter's enriched data looks wrong,
  check `pipeline/enrich.py`'s output for `WARNING:` lines from the last run.
- **No dependency pinning below the direct level.** `requirements.txt` pins
  `playwright`/`numpy`/`shapely` (this project's direct dependencies); their
  own transitive dependencies aren't locked. Fine for a project this size;
  revisit with a lockfile (`pip-compile`, `uv`) if that ever becomes a
  problem.
- **`raw_events/*.json` contains scraped page text verbatim**, which can
  include incidental personal contact info that was public on the source
  Meetup page (e.g. an organizer's email in an event description). This is a
  known, accepted tradeoff of scraping public event pages as-is rather than
  scrubbing them — worth being aware of before treating `raw_events/` as
  safe to share more widely than the repo already is.

## License

No license file is currently included, which by default means all rights
reserved — add one (e.g. MIT) before inviting outside use or contributions.
