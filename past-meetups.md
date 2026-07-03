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
- Include 2-4 relevant topics per talk from this vocabulary:
  - **Data modeling**: data modeling, model design, incremental models, dbt fundamentals
  - **Data quality & testing**: data testing, data quality, testing best practices, dbt tests
  - **Analytics engineering**: analytics engineering, team management, junior engineer training, project structure
  - **Modern data stack**: modern data stack, data stack architecture, dbt ecosystem, computational notebooks
  - **Organizational**: dbt migration, organizational adoption, change management, team operations
  - **Technical**: CI/CD pipeline, data orchestration, scalability, performance optimization
  - **Tools & ecosystem**: tool comparison, dbt API, dbt cloud, dbt core, visualization tools
  - **Domain-specific**: marketing analytics, e-commerce, real-world implementation, case studies

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