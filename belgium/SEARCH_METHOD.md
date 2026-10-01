# Belgium dbt search: method, lessons and replication prompt

This file goes with `belgium_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-10-01
- **Goal:** find people in Belgium who could **speak at** (or attend) the [Belgium dbt Meetup](https://www.meetup.com/analytics-engineering-belgium/), and the local companies that use dbt.
- **Region:** Belgium. Brussels, Antwerp, Ghent, Leuven, Mechelen, Hasselt and Ottignies-Louvain-la-Neuve all count.

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 56 |
| People | 106 |
| Tier 1 leads | 34 |
| First-time speakers (publish, no talk yet) | 13 |
| Proven speakers | 87 |
| Spoke at this chapter before | 34 |
| Based in the region | 77 |
| Based elsewhere | 6 |
| Location unknown | 23 |
| With a LinkedIn profile | 23 |
| Job ads mentioning dbt | 3 |
| Past chapter meetups | 14 |
<!-- at-a-glance:end -->

## 1. How the search was done

Web search ran out after about 25 calls. Most of the search used page fetches and the Meetup data endpoint instead.

### Step 1: Other Belgian meetups

- **Meetup's `gql2` endpoint:** it answers a plain `curl` POST. One `groupSearch` call with a latitude and longitude listed every Belgian data group. Past events for 15 groups were pulled and filtered for dbt.
- **[Databricks User Group Belgium](https://www.meetup.com/databricks-user-group-belgium/events/?type=past):** 14 events. It had the dbt talks from IBA and Volvo Trucks.
- **[dataMinds.be](https://www.meetup.com/dataminds-ai/events/?type=past):** 116 events, with 3 dbt sessions in 2025 and 2026. It is a Microsoft data user group.
- **[PyData Belgium](https://www.meetup.com/pydata-belgium/events/?type=past)** had 2 dbt talks in 2026. **[Data Science Leuven](https://www.meetup.com/data-science-leuven/events/?type=past)** had 2 in 78 events.
- **[Belgium Snowflake User Group](https://usergroups.snowflake.com/belgium/):** 4 events and 5 organisers. Its December 2025 evening at Telenet was held jointly with the chapter.

### Step 2: Consultancy and company blogs

- **[dataroots blog](https://dataroots.io/blog):** 8 dbt or data quality posts with named authors. Each post names its authors, so fetch the posts rather than the listing.
- **[Data Minded on Medium](https://medium.com/feed/datamindedbe):** 10 posts from 2026.
- **[Biztory blog](https://www.biztory.com/blog):** 2 dbt posts.
- **No usable content:** the [Datashift](https://www.datashift.eu/insights), element61, Lytix, Plainsight and Aivix blogs returned 404 errors or images only.

### Step 3: Conferences and dbt Labs pages

- **[dataMinds Connect 2025](https://element61.be/en/node/44093):** element61's sessions at the Mechelen conference.
- **No Belgian employers:** the [dbt Summit 2026 sessions](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role) and the [dbt developer blog authors](https://docs.getdbt.com/blog/authors).

### Step 4: Women-in-data communities

This step looks for speakers through women-focused groups' own events. It never labels or guesses anyone's gender.

- **[WiDS Belgium](https://www.widsworldwide.org/?p=17492):** it lists 4 event ambassadors but no speakers. The ambassadors are recorded as connectors, meaning people who can introduce others.
- **[PyLadies Brussels](https://www.meetup.com/pyladies-brussels/):** beginner Python workshops with no named speakers.
- **[R-Ladies Brussels](https://www.meetup.com/R-Ladies-Brussels/):** no events since 2023.
- **Result:** the women-in-data pool is only the 4 WiDS ambassadors.

### Step 5: Job ads

- **[TheirStack](https://theirstack.com/en/technology/dbt/be):** it shows 10 of the 167 Belgian companies it lists as using dbt.
- **Ads found:** 3, at [Datashift](https://careers.datashift.eu/o/analytics-engineer), [Lighthouse](https://startup.jobs/senior-analytics-engineer-lighthouse-8769874) and [Deliverect](https://careers.redpoint.com/companies/deliverect/jobs/59856833-analytics-engineer).
- **Empty:** a [Stepstone search](https://www.stepstone.be/emplois/dbt/a-gand) returned 0 results, and the aijobs pages redirected.

### Step 6: Chapter history

- **Past speakers:** every named speaker in `../enriched/analytics-engineering-belgium.json` was added, with their talk as evidence. That covers 14 events, from meetup #1 (2023-03-23) to meetup #14 (2026-05-12).
- **Result:** 34 people in the file have spoken at the chapter.

### Step 7: Location pass and LinkedIn pass

- **Location pass:** people were placed from public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
  - Sessionize speaker pages gave 11 high-confidence calls.
  - An in-person talk or host role at a chapter event since 2024-10, at an employer with a Belgian office, gave 14 medium-confidence calls.
  - Together they placed 25 people: 21 in Belgium and 4 elsewhere (Zagreb, Aarhus, Naaldwijk and Ilioúpoli).
- **LinkedIn pass:** search results only, never a LinkedIn page. 14 people were searched and 11 placed: 10 in Belgium and 1 in Paris.
- **Yield:** 36 people placed across both passes, and 24 still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **Meetup's `gql2` endpoint** needs no browser. It returns past events with full descriptions for any group.
  - **Databricks User Group Belgium and dataMinds.be** are the richest Belgian sources of dbt talks outside the chapter.
  - **The dataroots blog** names the authors of each post. Most of the first-time speakers came from it.
  - **Sessionize speaker pages** state a city for most Belgian speakers.
  - **LinkedIn search results** placed most dataroots authors, whose posts link only to LinkedIn.
- **Sources that didn't:**
  - **Medium feeds** returned HTTP 429 (too many requests) after a few calls. Fetch the known publications first.
  - **Plain web searches for Lytix and element61** returned pages about dialectical behaviour therapy. Search the company site instead.
  - **Belgian job boards** gave almost nothing, so job-ad coverage is thin.
- **Watch out for:**
  - **Speakers who gave online sessions.** dataMinds.be runs online talks with speakers from other countries, for example Inspari in Denmark and Solvership in Croatia.
  - **Duplicate company records.** "Xebia Data" and the GoDataDriven/Xebia record are one company.
  - **One placeholder employer.** 8 speakers whose employer the event page did not name sit under "Unstated employer (Belgium)".

## 3. Key leads

- **First-time speakers** (people who publish about dbt but have no talk on record):
  - **Stijn Dolphen (dataroots, Brussels):** [SQLMesh vs dbt Core](https://dataroots.io/blog/sqlmesh-vs-dbt-core-is-a-new-challenger-emerging-in-analytics-engineering), plus a post on dbt Copilot.
  - **Amaury Fouville and Corentin De Ro (dataroots):** [lessons from a one-year migration to Fabric and dbt](https://dataroots.io/blog/lessons-learned-from-a-one-year-migration-towards-fabric-dbt). It would suit a joint talk.
  - **Kristy Broekmans (Biztory, Antwerp):** [the dbt and Snowflake CI/CD workflow](https://www.biztory.com/blog/the-dbt-and-snowflake-ci-cd-workflow).
  - **Mustafa Kurtoglu (dataroots, Leuven):** [open-source Unity Catalog with dbt and DuckDB](https://dataroots.io/blog/open-source-unity-catalog-with-dbt-duckdb). The post was written during an internship.
  - **Paolo Léonard and Nemish Mehta (formerly dataroots, Brussels):** [the state of data quality tools in 2024](https://dataroots.io/blog/state-of-data-quality-tools-2024-q1), including the dbt-native ones.
- **Anchor speakers** (proven dbt speakers who have not spoken at the chapter):
  - **Samuël Delefortrie (Volvo Trucks, Ghent):** [scaling dbt and Databricks across 20+ teams](https://www.meetup.com/databricks-user-group-belgium/events/313956684/).
  - **Flavien Hancart (IBA):** [dbt, Dagster and Databricks](https://www.meetup.com/databricks-user-group-belgium/events/306531852/).
  - **Senne Vanstraelen and Tom Van de Velde (Datashift):** [dbt on Fabric](https://www.meetup.com/dataminds-ai/events/305988682/).
  - **Geert Vinck and David Mat (Telenet):** [dbt and Snowflake at Telenet](https://usergroups.snowflake.com/events/details/snowflake-belgium-presents-belgium-snowflake-user-group-telenet-data-amp-ai-journey/).
  - **Jonas Crevecoeur (Data Minded, Leuven):** [pipelines where Polars and dbt work together](https://www.meetup.com/pydata-belgium/events/315298608/).
- **Connectors:**
  - **Lise Kerckhove (OTA Insight):** [co-hosted the chapter meetup at Lighthouse](https://www.meetup.com/analytics-engineering-belgium/events/303680207/) in Ghent.
  - **Jeroen Wijnants, Kris Van der Biest, Willem Dullaart and Joy Muttai:** the [Belgium Snowflake User Group](https://usergroups.snowflake.com/belgium/) organisers.
  - **Murilo Cunha (dataroots):** [runs PyData Belgium community sessions](https://www.meetup.com/pydata-belgium/events/308607098/).
  - **Setareh Tasdighian, Yanou Ramon, Edith Heiter and Sofie Goethals:** [WiDS Belgium](https://www.widsworldwide.org/?p=17492) event ambassadors.
  - **Bart Smeets (dataroots co-founder):** a likely sponsor contact.

## 4. Before outreach

- **Check most "in region" calls.** Only 31 of the 77 people marked in Belgium have a location note with evidence. The rest were placed from an event city or an employer's office during research.
- **Check tier 1.** It holds 34 people, and 17 of them have no item recorded as mentioning dbt. Examples are David Backx, Raghid Bsat and Tim Dries.
- **Check 12 LinkedIn URLs.** They were copied from the organiser's Meetup event pages, not taken from search results. Each person has a note saying so, and the confidence is medium. Remove them if only search results should count.
- **Check people who have moved:**
  - Florian Thoen now works in Paris.
  - Paolo Léonard is now at NEO, Nemish Mehta at IBA and Katarina Milosevic at Datanesis.
- **Fill missing employers and titles.** Titles marked "(title not stated)" are placeholders. Murilo Cunha's employer is inferred from co-hosting the dataroots podcast.
- **Skip dbt Labs staff.** Bart van Delft is tier 1, but dbt Labs is excluded from outreach.
- **Check people listed in other chapters.** Mikkel Dengsøe, Bart van Delft, Pádraic Slattery, Juan Manuel Perafán and Niko Korvenlaita also appear in other city files.
- **Read the 2025-12-04 chapter entry** as the joint Snowflake user group evening at Telenet.

## 5. Next run

- **People still without a location:** 24. They include tier-1 leads Arthur Chionh and Johannes Lootens, and most chapter speakers from 2023 and 2024.
- **Consultancy blogs:** retry Datashift, element61, Lytix, Plainsight and Aivix through a site search.
- **Medium:** fetch other Belgian company publications before the rate limit starts.
- **Job ads:** run the ATS searches (`site:jobs.lever.co`, `site:job-boards.greenhouse.io`, `site:jobs.ashbyhq.com` with dbt Belgium).
- **Women-in-data:** ask the WiDS Belgium ambassadors for introductions, and look for named speakers at WiDS Belgium itself.
- **Data Professionals - Belgium:** its [quarterly data drinks](https://www.meetup.com/data-professionals-belgium/) in Brussels were not scanned for speakers.

## 6. Replication prompt

````
You are extending my dataset of Belgian companies that use dbt, and people who could
speak at or attend the Belgium dbt Meetup. The file is belgium/belgium_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read belgium/SEARCH_METHOD.md first, then
research/README.md, research/raw-format.md, research/location-task.md and
research/linkedin-task.md. Keep the shared schema (berlin_planning/SEARCH_METHOD.md §3).

Try first: new events since metadata.generated_at from Databricks User Group Belgium,
dataMinds.be, PyData Belgium and Data Science Leuven (Meetup gql2 by curl), new dataroots
and Data Minded posts, and the consultancy blogs that failed last time through a site search.
Then the ATS job-ad searches, and LinkedIn searches for the people still without a location.

Rules: never fetch LinkedIn pages, and take LinkedIn URLs only from search results;
public professional information only; never guess gender, and record pronouns only when
self-stated. Assemble with research/assemble.py --base, place people with
research/apply_locations.py, then run research/validate.py and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Meetup data for 15 Belgian data groups, the dataroots, Data Minded and Biztory blogs, the Snowflake user group, WiDS Belgium and job boards, plus chapter history. 106 people at 56 companies, 34 of them past chapter speakers. 3 job ads. Web search ran out after about 25 calls. |
| 2026-10-01 | 1 | Location pass from public pages: Sessionize speaker pages and in-person chapter talks. 25 people placed, 21 in Belgium and 4 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 14 people searched, 10 placed in Belgium and 1 in Paris. With the location pass, 36 people placed and 24 still unknown. |
