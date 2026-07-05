## context
You are an event organiser and analytics engineer taking over the dbt Berlin meetup. Your goal is to understand what has been done in the past before shaping future strategy.

## task

**Step 1: Locate all past event links**
- Start at https://www.meetup.com/berlin-dbt-meetup/events/?type=past
- Extract all event URLs from the past events list
- Filter out Coalesce events and any events co-hosted with other chapters (keep Berlin-only events, online or in-person)
- Expected: ~17 events

**Step 2: Extract data from each event page (run in parallel via sub-agents)**
For each event URL, fetch the page and extract:

**Required fields:**
- `event_url`: Full meetup event URL
- `event_id`: Numeric ID from URL
- `event_name`: Event title
- `date`: Event date (YYYY-MM-DD format)
- `time`: Start time and duration (e.g., "19:00-21:00")
- `location`: Venue name and city (or "Online" if virtual)
- `attendees`: Number of RSVPs/attendees
- `agenda`: Event description/theme (1-2 sentences)
- `event_description`: How the event was described on Meetup (the event's own description text)
- `talks`: Array of talk objects, each with:
  - `title`: Talk title
  - `speaker_name`: Speaker name
  - `speaker_title`: Speaker role/company (if available)
  - `duration_minutes`: Talk length in minutes (if available)
  - `description`: Summary description of what the talk covers
  - `raw_text_excerpt`: Verbatim text from the raw_text describing the talk
  - `topics`: Zero-shot classification of talk topics (e.g., "data modeling", "data quality", "data testing", "analytics engineering", "dbt best practices", etc.)
- `additional_metadata`: Any other useful info (host name, recording link, slides link, event description URL, etc.)
- `raw_text`: Original fetched page content as plain text for recomputation

**Step 3: Handle fetch failures gracefully**
- If a page fails to load or returns empty, ask the user to manually copy-paste the full page content
- Mark failed events in status tracking with reason for failure

## output format
- Single JSON file: `dbt-meetups/events.json`
- Structure: `{ "events": [...], "metadata": { "total_events": X, "extraction_date": "YYYY-MM-DD", "status": {...} } }`
- Status tracking in metadata: `{ "status": { "successfully_extracted": [...], "manual_copy_paste_needed": [...], "excluded_events": [...] } }`

## validation & quality checks
- Each event should have 2-3 talks (flag anomalies: <2 or >3 talks)
- All required fields must be present for each event
- No duplicate events in final output
- If a field is unavailable, use `null` instead of omitting it

## post-processing: enrichment of talk descriptions and topics

After initial data extraction, enrich each talk with:

**Step 4: Extract talk descriptions from raw_text**
- For each talk in the event's `raw_text`, find the verbatim text describing the talk
- Add `raw_text_excerpt`: The exact phrase(s) from the raw_text that mention the talk (preserve original wording)

**Step 5: Generate talk summaries**
- For each talk, write a concise `description` (1-2 sentences) summarizing what the talk covers
- Base the summary on:
  - The talk title
  - The speaker's title/company
  - Any context from the raw_text agenda or featured speakers section
- Keep summaries neutral and descriptive of content, not promotional

**Step 6: Zero-shot topic classification**
- For each talk, classify topics covered using data-related terminology
- Assign 1-3 relevant topics per talk from this standardized vocabulary only (do not invent new topic strings):
  - `dbt best practices`
  - `dbt fundamentals`
  - `dbt product features` (dbt Core, Cloud, Fusion, Python models — which part of the product)
  - `dbt product updates`
  - `dbt migration & adoption`
  - `data modeling`
  - `data quality & testing`
  - `data governance`
  - `data mesh`
  - `data engineering`
  - `analytics engineering`
  - `business intelligence`
  - `semantic layer`
  - `orchestration & ci/cd`
  - `performance & scale`
  - `modern data stack`
  - `tools & ecosystem`
  - `developer workflow`
  - `project structure`
  - `genai & llm`
  - `team & org design`
  - `career development`
  - `community`
  - `industry trends`
  - `domain-specific use cases`
  - `data warehouse & platforms` (Snowflake, BigQuery, Databricks, DuckDB, other cloud platforms — which vendor)

Notes:
- This list was derived 2026-07-05 by clustering ~195 raw topic strings found across `analysis/dbt-meetups/enriched/*.json`, first down to 35 standardized topics, then condensed further to 26 by merging umbrella pairs that didn't lose discriminating power: `data quality`+`data testing`; `dbt core`/`dbt cloud`/`dbt fusion`/`dbt python models` (all "which part of dbt"); `snowflake`/`bigquery`/`databricks`/`duckdb`/`cloud platforms` (all "which vendor"); `ci/cd`+`orchestration` (both "how work gets run/deployed"). See `git log` for the consolidation commits.
- `case studies` / `case study` / `real-world implementation` / `real-world application` were deliberately dropped as topic tags — almost every talk is some form of case study, so the tag wasn't discriminating. Talks that only had a case-study tag were re-tagged with their actual subject matter instead.
- When a new talk's true topic isn't covered by this vocabulary, propose a new standardized topic to the user for approval before adding it, rather than free-texting a one-off tag.

## topic categories (roll-up for high-level reporting, e.g. donut charts)

The 26 topics above are the source of truth stored in each talk's `topics` array in `enriched/*.json` — do not replace them. For high-level reporting (e.g. a donut chart with readable slice counts), roll each topic up into one of these 8 categories via lookup; do not persist the category onto the talk records themselves.

| Category | Topics included |
|---|---|
| `dbt engineering practices` | dbt best practices, dbt fundamentals, data modeling, developer workflow, project structure |
| `data quality & governance` | data quality & testing, data governance |
| `platform & architecture` | modern data stack, data warehouse & platforms, data engineering, performance & scale, data mesh |
| `orchestration & delivery` | orchestration & ci/cd, semantic layer, tools & ecosystem |
| `dbt product` | dbt product features, dbt product updates, dbt migration & adoption |
| `analytics & bi` | analytics engineering, business intelligence, domain-specific use cases |
| `people & organization` | team & org design, career development, community |
| `emerging & trends` | genai & llm, industry trends |

Notes:
- A talk can have multiple topics spanning multiple categories. For a single-category-per-talk view (e.g. donut chart slice counts), use the talk's **first-listed topic** in its `topics` array as the primary category — topics are ordered by relevance from the enrichment step (Step 6).
- Derived 2026-07-05. Verified against all 73 enriched files: primary-category distribution across 978 talks ranges 6%-21% per category (no single category dominates or is negligible), suitable for an 8-slice donut chart.

## speaker identity resolution

`speaker_name` in the enriched files is raw/as-scraped and not deduplicated across chapters — the same person can appear with slightly different spellings (typos, missing diacritics, capitalization). `analysis/dbt-meetups/speaker-identities.json` (generated 2026-07-05, via fuzzy matching with rapidfuzz on single-speaker name strings, cross-checked against `speaker_title`/company/event context) contains:
- `canonical_merges`: confirmed name variants of the same person, with a canonical name to use for identity/attendance analysis
- `confirmed_different_people`: near-matches (fuzzy-matched but different surname/given name) that were reviewed and confirmed to be different people, not merged
- `repeat_speakers_across_chapters`: speakers (post-canonicalization) who have spoken at more than one chapter, useful for identifying a recurring/traveling speaker circuit

This file does not modify `enriched/*.json` — apply the canonical mapping at analysis time if you need deduplicated speaker counts.

## processing notes for replication

**For another dbt chapter (e.g., dbt NYC, dbt SF):**

1. Replace the chapter name in Step 1's URL (e.g., `https://www.meetup.com/nyc-dbt-meetup/events/?type=past`)
2. Adjust filtering rules if the chapter has different characteristics (e.g., online-only or different co-hosting patterns)
3. Follow the same enrichment steps 4-6 for all talks
4. Update the output file path: `dbt-meetups/{chapter_name}/events.json`
5. Keep the same metadata tracking structure for consistency

**File structure for multi-chapter analysis:**
```
analysis/dbt-meetups/
├── berlin/
│   └── events.json
├── nyc/
│   └── events.json
├── sf/
│   └── events.json
└── past-meetups.md (this file)
```