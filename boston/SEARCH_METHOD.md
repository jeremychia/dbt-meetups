# Boston dbt search: method, lessons and replication prompt

This file goes with `boston_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in Greater Boston who could **speak at** (or attend) the [Boston dbt Meetup](https://www.meetup.com/boston-dbt-meetup/), and the local companies that use dbt.
- **Region:** Greater Boston. Boston, Cambridge and Burlington count. Commuter towns are local for this chapter, so Providence counts too.

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 77 |
| People | 43 |
| Tier 1 leads | 6 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 37 |
| Spoke at this chapter before | 21 |
| Based in the region | 32 |
| Based elsewhere | 4 |
| Location unknown | 7 |
| With a LinkedIn profile | 6 |
| Job ads mentioning dbt | 62 |
| Past chapter meetups | 12 |
<!-- at-a-glance:end -->

## 1. How the search was done

The first build used about 18 web searches, plus a logged-out LinkedIn Jobs scan. Scoring follows [`../berlin_planning/SEARCH_METHOD.md`](../berlin_planning/SEARCH_METHOD.md) §1 Step 6.

### Step 1: Chapter history

- **What was added:** every named speaker in `../enriched/boston-dbt-meetup.json`, with their talk.
- **Range:** 12 meetups, from 2020-05-08 to 2025-06-18. The last three were at Klaviyo, 125 Summer Street.
- **Yield:** 21 people who have spoken at the chapter, and the 3 organisers of the 2024–25 events.
- **Status:** the chapter has had no event since 2025-06-18.

### Step 2: dbt conference agendas

- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** the best source. Filtered to Boston employers, it gave 3 WHOOP speakers, plus CarGurus, HubSpot and Datadog. Each speaker page gives the session title.
- **[Coalesce 2025 on-demand](https://www.getdbt.com/resources/coalesce-on-demand):** a WHOOP session.
- **[Coalesce 2025 sessions preview](https://www.getdbt.com/blog/what-to-expect-from-sessions-at-coalesce-2025):** a Datadog session.
- **Empty:** the [Coalesce 2025 agenda](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/agenda-at-a-glance) renders with JavaScript, so a fetch returns nothing. The [dbt World Tour](https://www.getdbt.com/events/roadshow/dbt-world-tour) has no Boston stop in 2026.

### Step 3: Other local meetups and conferences

- **[Snowflake User Group Boston](https://usergroups.snowflake.com/boston/):** its April and July 2026 events gave 2 speakers and the 3 organisers. It meets at Microsoft NERD in Cambridge.
- **[Boston Data and AI Saturday 2026](https://sessionize.com/sql-saturday-boston-2026/):** 137 talk submissions for 3 October 2026, in Burlington. These are submissions, not accepted sessions.
- **Low yield:** [PyData Boston - Cambridge](https://www.meetup.com/pydata-boston-cambridge/) has AI and agent topics only. [Data Engineering Boston](https://www.meetup.com/data-engineering-boston/) has had 2 events since 2024. [Data, Cloud and AI in Boston](https://www.meetup.com/Big-Data-Developers-in-Boston/) has IBM agent talks.
- **Not found:** Meetup groups for Boston Airflow, Databricks, Tableau and WiMLDS were not found under the guessed group names.

### Step 4: Women-in-data communities

People were taken only from each community's own events. Nobody's gender is recorded.

- **[PyLadies Boston](https://www.meetup.com/pyladies-boston/):** the only useful source. It gave a Women in Data Boston representative, a regular presenter and a careers panel. Its venues include CarGurus and Kensho.
- **Weak or empty:** [R-Ladies Boston](https://www.meetup.com/rladies-boston/) runs socials only. [WiDS Cambridge 2026](https://www.widscambridge.org/featured-speakers-2026) has academic and policy speakers. WiDS means Women in Data Science.

### Step 5: Company blogs

- **[Klaviyo Engineering](https://klaviyo.tech/):** the only dbt posts are a CI series by Corey Angers, a past chapter speaker.
- **[Wayfair tech blog](https://www.aboutwayfair.com/careers/tech-blog):** BigQuery and ML content, with no dbt.

### Step 6: Job ads

- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt), logged out:** up to 150 Boston-area ads checked for the whole word "dbt". 62 ads at 48 companies mention it.
- **Employers with several ads:** WHOOP, MFS Investment Management and Dynatrace (3 each), and Xometry, IDEXX, Prenuvo, Northeastern University, Counsel Health, SmithRx, Grant Thornton and Tata Consultancy Services (2 each).

### Step 7: Location and LinkedIn passes (2026-10-01)

- **Page fetches:** 8 people placed, 7 in the region and 1 outside.
  - The Meetup `gql2` endpoint gave the profile city of each chapter event's hosts and RSVPs.
  - GitHub profiles and recent in-person talks at an employer with a Boston office gave the rest.
- **LinkedIn search results:** 5 people placed, 4 in the region and 1 outside. No LinkedIn page was opened.
- **Still unknown:** 9 people.

## 2. What we learnt

- **Sources that worked:**
  - **The dbt Summit speaker index and its speaker pages** (`getdbt.com/dbt-summit/speakers/<slug>`) are the highest-yield source for US chapters. Filtering by local employer gives 5–8 leads for about one fetch each.
  - **Snowflake user groups on Bevy** list speakers, bios and organisers in static HTML. They find local dbt-on-Snowflake practitioners and possible co-hosts.
  - **Meetup `gql2` RSVPs** placed most past chapter speakers. Add `sort: DESC` to the past-events query, because it returns the oldest events first.
- **Sources that didn't:**
  - **Guessed Meetup group names** found nothing for Airflow, Databricks, Tableau or WiMLDS.
  - **Local company blogs** had no new dbt authors.
  - **Old chapter talks** give no location evidence. Most talks from 2020–23 could not be placed.
- **Watch out for:**
  - **No first-time speakers yet.** An emerging voice is someone who publishes about dbt but has no talk on record. Boston has none, so the list leans on people who already speak.
  - **Head-office locations.** The WHOOP and CarGurus speakers are placed by their employer's Boston head office, not by their own profile.
  - **A chapter talk missing from the history.** Kasey Mazza's record cites a March 2023 chapter talk, but the chapter history has no event that month.

## 3. Key leads

- **First-time speakers at this chapter:**
  - **Samyuktha Kapoor**, analytics engineer. Spoke in person at the Snowflake User Group on reliable Snowflake and dbt pipelines: [April 2026 event](https://usergroups.snowflake.com/events/details/snowflake-boston-presents-april-meetup-community-case-studies/). Early career, with a dbt talk ready to give.
  - **William Tsu**, **Madhura Pharande** and **Sophia Scaglioni Melegari**, WHOOP. dbt Summit 2026 talk on bridging dbt models and Snowflake semantic views: [session](https://www.getdbt.com/dbt-summit/agenda/how-whoop-bridges-dbt-models-and-snowflake-semantic-views).
  - **Jordan Morgan**, Principal Data Analytics Engineer, CarGurus. dbt Summit 2026 talk on moving 80 developers from dbt Core to Fusion: [speaker page](https://www.getdbt.com/dbt-summit/speakers/jordan-morgan).
  - **John Miner** submitted a dbt introduction to Boston Data and AI Saturday: [submissions](https://sessionize.com/sql-saturday-boston-2026/).
- **Anchor speakers:**
  - **Kasey Mazza**, HubSpot. Manages analytics engineering teams and led a dbt Summit 2026 session on positioning them: [session](https://www.getdbt.com/dbt-summit/agenda/beyond-the-bottleneck-position-your-analytics-engineering-team-as-a-strategic-force). Also a route to HubSpot as a host.
  - **Matt Luizzi**, Senior Director Business Analytics, WHOOP. Coalesce 2025 talk on decisions with dbt and Snowflake: [recording](https://www.getdbt.com/resources/coalesce-on-demand/coalesce-2025-how-whoop-unlocks-smarter-decisions-with-dbt-and-snowflake).
  - **Corey Angers**, Klaviyo. Two chapter talks in 2024, on observability and CI with GitHub Actions: [July 2024 event](https://www.meetup.com/boston-dbt-meetup/events/301705215/).
  - **Kevin Hu**, Datadog (formerly Metaplane). A borderline vendor talk, co-presented with Ramp: [Coalesce 2025 preview](https://www.getdbt.com/blog/what-to-expect-from-sessions-at-coalesce-2025).
- **Connectors:**
  - **Chitra Sundaram**, **Riddhima Shukla** and **Stefan Mitrano** (Cleartelligence) organised the 2024–25 chapter events. Contact them first about a restart: [chapter page](https://www.meetup.com/boston-dbt-meetup/).
  - **Evan Cover**, Director of BI Engineering, Klaviyo. The likely sponsor for hosting at Klaviyo again: [dbt Labs post](https://www.getdbt.com/blog/new-dbt-cloud-enhancements-empower-organizations-with-trustworthy-data-at-scale).
  - **Keith Belanger**, **David Garrison** and **Elizabeth Rosso** organise the Snowflake User Group, which has about 2,575 members: [group page](https://usergroups.snowflake.com/boston/).
  - **Kaveesha Shah** represents Women in Data Boston: [PyLadies event](https://www.meetup.com/pyladies-boston/events/313918889/).

## 4. Before outreach

- [ ] **Confirm the tier-1 locations.** All 6 tier-1 people are placed by employer or event, not by their own profile. Jordan Morgan may work remotely from Maine.
- [ ] **Confirm the 9 unknown locations.** William Kuan's LinkedIn results point to Rapid7 and to Greater Boston separately. Athena Casarotto's Greater Boston profile is a different one from the Drizly profile, and mentions Providence. Jason Ganz's only match is a Meetup name match to Washington, which is not enough to place.
- [ ] **Check the weak location call.** Sabin Thomas was placed by a name match to a chapter member only.
- [ ] **Skip or re-rank people outside the region.** Divyakumar Savla is in the San Francisco Bay Area, and Adrien Ledoux is in Zurich.
- [ ] **Check Kasey Mazza's chapter talk** against the Meetup page before treating it as a repeat invite.
- [ ] **Treat Boston Data and AI Saturday entries as unconfirmed** until the schedule for 3 October 2026 is out.
- [ ] **dbt Labs staff are labelled.** Stephen Thibeault, Jason Ganz, Grace Goheen and Jeremy Cohen work there. They can speak, but check the line-up has practitioners first.

## 5. Next run

- **Run the LinkedIn pass first.** 20 tier-1 and tier-2 people are still `not_searched`.
- **Find first-time speakers** through GitHub user search (`dbt location:Boston`). It was the best source of emerging voices in Atlanta.
- **List local data groups** with the Meetup `gql2` `groupSearch` query and Boston's latitude and longitude, instead of guessing group names.
- **Read the accepted Boston Data and AI Saturday schedule** after 3 October 2026.
- **Scan Women in Data Boston's own events**, and the PyLadies Boston events since the last run.

## 6. Replication prompt

````
You are extending my dataset of Greater Boston companies that use dbt, and people who could speak
at or attend the Boston dbt Meetup. The file is boston/boston_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read boston/SEARCH_METHOD.md, then
research/README.md and the briefs it links (raw-format.md, location-task.md, linkedin-task.md).
The region is Greater Boston (Boston, Cambridge, Burlington and nearby). Commuter towns such as
Providence count as local.

Budget about 25 web searches. Try these first:
1. LinkedIn search results for tier 1-2 people with linkedin_confidence "not_searched".
2. GitHub user search (dbt location:Boston) for first-time speakers with public dbt work.
3. Meetup gql2 groupSearch near Boston, then past events (sort: DESC) of the data groups it finds.
4. The accepted Boston Data and AI Saturday 2026 schedule, and new Snowflake User Group events.
5. A LinkedIn Jobs guest scan re-run (keywords=dbt, Boston); keep ads with the whole word dbt.

Rules: never fetch LinkedIn pages; use only search results. Public professional information only;
never guess gender, and record pronouns only when self-stated. Assemble with research/assemble.py
--base, run research/validate.py (must print ok), and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build: dbt Summit 2026 and Coalesce 2025 agendas filtered to local employers, local meetups and user groups, PyLadies Boston and other women-in-data communities, company blogs, and a LinkedIn Jobs scan. Past chapter speakers added from `../enriched/boston-dbt-meetup.json`. 78 companies (18 on the watchlist), 43 people, 62 job ads at 48 companies, 12 past meetups. Split: 37 proven speakers, 6 featured. Tiers: 6 tier 1, 25 tier 2, 4 tier 3, 8 connectors. 21 people had already spoken at the chapter. |
| 2026-10-01 | 2 | Location pass: 8 people placed from Meetup host and RSVP profiles, GitHub and recent in-person talks, 7 in the region and 1 outside. |
| 2026-10-01 | 2 | LinkedIn pass: 5 people placed from LinkedIn search results, 4 in the region and 1 outside. 9 people are still unknown. |
