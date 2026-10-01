# City research: method and tools

This folder holds the shared method and scripts for the `<city>/<city>_dbt_companies.json` research files that feed the [organiser cockpit](../README.md#organiser-cockpit). Each city also has its own `SEARCH_METHOD.md` with what was searched there, what worked and the key leads.

- **Schema:** every file follows shared schema version 3 in [`berlin_planning/SEARCH_METHOD.md`](../berlin_planning/SEARCH_METHOD.md) §3.
- **Scoring rules:** tiers, lead types and meetup fit follow the same file, §1 Step 6.
- **Older cities:** Berlin, Vilnius, Kuala Lumpur and Paris were built by hand before these scripts existed. Their own `SEARCH_METHOD.md` files describe how.

## The four steps

| Step | What it does | Brief | Script |
|---|---|---|---|
| 1. Research | One agent per city finds companies using dbt and people who could speak | [raw-format.md](raw-format.md) | — |
| 2. Assemble | Turns the agent's loose records into a valid file | — | [assemble.py](assemble.py) |
| 3. Location | Finds where each person is based, from public pages | [location-task.md](location-task.md) | [apply_locations.py](apply_locations.py) |
| 4. LinkedIn | Fills the remaining locations from LinkedIn search results | [linkedin-task.md](linkedin-task.md) | [apply_locations.py](apply_locations.py) |

Then validate and rebuild the cockpit:

```sh
python3 research/validate.py          # every city file; prints ok
dashboard/build_organiser.sh
```

## Step 1: research

- **Give each agent one city** and about 25 web searches. Point it at [raw-format.md](raw-format.md) and at `berlin_planning/SEARCH_METHOD.md` §1.
- **Look for, in order:** first-time speakers (people who publish about dbt but have no talk on record), proven speakers, women-in-data communities sourced through their own events, and job ads that mention dbt.
- **Skip past chapter speakers.** The assembler adds everyone who has spoken at the chapter, from `enriched/<chapter>.json`.
- **Never fetch LinkedIn pages** or the LinkedIn jobs API. LinkedIn is used only through search results, in step 4.

## Step 2: assemble

```sh
python3 research/assemble.py <raw.json> <city>/<city>_dbt_companies.json                       # new city
python3 research/assemble.py <raw.json> <city>/<city>_dbt_companies.json --base <city>/<city>_dbt_companies.json   # add to a city
```

- **What it derives:** ids, `level`, `meetup_fit`, `watchlist`, counts, `past_meetups` and `past_chapter_talks`.
- **Extending a city:** it merges by id or name, and only re-scores the records the new research touched. Run it against the committed file, so a failed run can be undone with `git checkout`.
- **Non-Latin names** need an explicit ASCII `id` (a romanised name or a handle). The script stops and asks for one.
- **Lead type:** an existing first-time speaker who gains a talk becomes a proven speaker.

## Steps 3 and 4: location

Location decides the cockpit's "in region only" filter and the attendee ranking, so it needs evidence.

- **High:** the person's own profile states a city. That means a GitHub location, a speaker bio, an author box, a Meetup profile tied to the person, or a LinkedIn search result that shows their name, employer and location.
- **Medium:** an in-person talk or organiser role at a local event in the last 2 years, and the employer has a local office.
- **Outside the region:** needs the same standard, a stated city elsewhere.
- **Otherwise unknown.** Never infer a location from a name, a hometown, a university or a company's head office alone.
- **Meetup member profiles** count only when the member is tied to the person: the RSVP or host of the event they spoke at. A name match alone is medium at best, and never supports "outside the region".

```sh
python3 research/apply_locations.py <city file> <patch.json>        # fills unknown locations only
python3 research/revert_locations.py <city file> <person id> ...    # sets people back to unknown
```

Each applied location adds a note and an evidence link to the person, so every call can be checked.

## What we learnt

### Sources that worked

- **Meetup's `gql2` endpoint** answers a plain `curl` POST. It returns past events with full descriptions, whether each event was in person, the venue, and the hosts and RSVPs with their profile city. `groupSearch` with a latitude and longitude lists a city's data groups in one call.
- **LinkedIn search results** show a person's location next to their name and employer, which no other source does as reliably.
- **GitHub profiles** have a location field. The unauthenticated API allows about 60 calls an hour, shared by every agent, but the HTML profile page still shows the location after that.
- **Sessionize speaker pages** often state a city.
- **Company blogs with author boxes** were the best source of first-time speakers. Examples are adesso and ORAYLIS (Rhein-Ruhr), Xebia (Amsterdam), dataroots (Belgium), b.telligent and synvert (Munich), Brooklyn Data (New York) and The Information Lab (London).
- **Zenn and Qiita APIs** (Tokyo) and **velog** (Seoul) list dbt authors with their employers.
- **The getdbt.com sitemap** lists every dbt Summit speaker page.

### Sources that didn't

- **Medium feeds** return HTTP 429 after a few calls, from both curl and WebFetch.
- **JavaScript-rendered pages** return nothing to a fetch. These include the Coalesce on-demand listing, the DataEngBytes speakers page, connpass and most Japanese company sites.
- **Old talks:** most chapter talks before late 2024 give no location evidence.

### Limits and traps

- **Web search is capped at about 200 calls per session**, shared by every agent, and it also rate-limits bursts. Fifteen agents in parallel used it up within the first 20–25 searches each. Run the LinkedIn pass in its own session, or give each agent a smaller budget.
- **The tier-1 rule is generous.** Any first-time speaker with a post from 2024 onwards is raised to tier 1. That includes vendor bloggers and authors whose post doesn't mention dbt. Check them before outreach.
- **One consultancy can dominate a city.** Examples are Xebia in Amsterdam, Brooklyn Data in New York, The Information Lab in London and adesso in Rhein-Ruhr. Plan for one speaker per company per event.
- **Past speakers' employers** come from the Meetup talk text. A talk with several speakers can produce a company record named after a job title. Check `companies` for those after assembling.
- **Duplicate people:** the same person can appear under two spellings or two employers. Search each city for near-duplicate names before outreach.
