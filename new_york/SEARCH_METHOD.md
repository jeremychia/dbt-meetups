# New York dbt search: method, lessons and replication prompt

This file goes with `new_york_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-10-01
- **Goal:** find people in the New York metro area who could **speak at** (or attend) the [New York dbt Meetup](https://www.meetup.com/nyc-dbt-meetup/), and the local companies that use dbt.
- **Region:** the NYC metro area.

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 89 |
| People | 150 |
| Tier 1 leads | 46 |
| First-time speakers (publish, no talk yet) | 24 |
| Proven speakers | 113 |
| Spoke at this chapter before | 65 |
| Based in the region | 55 |
| Based elsewhere | 11 |
| Location unknown | 84 |
| With a LinkedIn profile | 7 |
| Job ads mentioning dbt | 7 |
| Past chapter meetups | 30 |
<!-- at-a-glance:end -->

## 1. How the search was done

One research run covered New York. It used about 22 web searches before the session limit stopped it. Everything after that came from direct page fetches.

### Step 1: dbt conference pages

- **[dbt Summit 2026 speaker pages](https://www.getdbt.com/sitemap-0.xml):** the getdbt.com sitemap lists all 178 speaker pages. Each page gives name, title, employer, bio and session. About 30 speakers work for New York employers.
- **[dbt case studies](https://www.getdbt.com/case-studies/bilt-rewards):** the same sitemap lists them. Bilt, Ramp, J.Crew, Wellthy, Nasdaq and JetBlue are New York area companies.
- **[Coalesce on the Road NYC 2026](https://www.getdbt.com/events/roadshow/coalesce-in-nyc):** a Bilt customer session, with no talk titles.

### Step 2: Other New York meetups

- **What was checked:** 2024 to 2026 past events of about 45 New York data groups. Meetup's `gql2` endpoint found the groups with `groupSearch` near Manhattan, then listed each group's events. No browser was needed.
- **[NYC Apache Airflow Meetup](https://www.meetup.com/nyc-apache-airflow-meetup/):** 30 events from 2024 to 2026, including one dbt talk on the Cosmos package.
- **[ClickHouse New York User Group](https://www.meetup.com/clickhouse-new-york-user-group/):** speakers from Ramp, Clay, Hex, Evidence, Braze and Datavations.
- **[Apache Spark NYC](https://www.meetup.com/spark-nyc/):** Datadog, EXL and Nielsen speakers.
- **Smaller yields:** [Databricks Community Meetup NYC](https://www.meetup.com/databricks-community-meetup-nyc/) gave one FanDuel speaker. [Data Engineer Things NYC #2](https://motherduck.com/events/det-nyc-2-meetup-2026/) gave one named speaker. The [Snowflake New York User Group](https://usergroups.snowflake.com/new-york) gave organisers only.
- **No yield:** [PyData NYC](https://www.meetup.com/pydatanyc/) had no dbt talks from 2024 to 2026. The [Data Council NYC group](https://www.meetup.com/data-council-nyc-data-engineering-science/) only promotes other conferences.

### Step 3: Company and consultancy blogs

- **[Brooklyn Data](https://www.brooklyndata.co/ideas):** bylines on 20 dbt posts. Brooklyn Data organises the chapter.
- **[Datadog](https://www.datadoghq.com/blog/understanding-dbt/):** a dbt best-practice post.
- **[NYC Data newsletter](https://nycdata.substack.com/archive):** a weekly list of New York data events and local writers.
- **Blocked or empty:** every [Medium feed](https://medium.com/feed/justworks-tech) returned HTTP 429 (too many requests). The [NYT Open blog](https://open.nytimes.com/feed) blocked the fetch. The [Squarespace engineering blog](https://engineering.squarespace.com/blog) had no data posts on its first page.

### Step 4: Women-in-data communities

This step finds speakers through women-focused groups' own events. It never records or guesses anyone's gender.

- **[Data + Women NYC](https://usergroups.tableau.com/data-women-nyc):** gave its organisers. Its events focus on Tableau.
- **[NYC WiMLDS](https://www.meetup.com/nyc-wimlds/):** one panel with named data leaders, on generative AI.
- **No yield:** [NYC PyLadies](https://www.meetup.com/nyc-pyladies/) had one event since 2024, on vector search. [R-Ladies NYC](https://www.meetup.com/rladies-newyork/) posts partner promotions only.
- **Result:** these groups run Tableau, AI and LLM events rather than analytics engineering talks. Their organisers are the useful contacts.

### Step 5: Job ads

- **[Built In NYC](https://www.builtinnyc.com/jobs/data-analytics/search/analytics-engineer):** ads from Clay, Datavations, Brainforge and Zocdoc quote dbt.
- **Venture capital job boards:** gave ads at Zocdoc, GlossGenius and Peloton.
- **Result:** 7 ads at 6 companies. All 7 show dbt in the ad text.

### Step 6: Chapter history

- **Source:** every named speaker in [`../enriched/nyc-dbt-meetup.json`](../enriched/nyc-dbt-meetup.json) was added as a person. That file holds 30 meetups, from 2019-07-31 to 2026-09-30.
- **Result:** 65 people in the file have spoken at the chapter.

### Step 7: Location pass and LinkedIn pass

The location rules are in [`../research/README.md`](../research/README.md). In short, a location needs the person's own profile, or a recent in-person local talk plus a local office.

- **Location pass (page fetches):** 26 people placed, 20 in the region and 6 elsewhere.
  - Meetup host profiles of the person's own event gave 5.
  - GitHub profiles with a matching employer gave 11.
  - In-person chapter talks since late 2024, at an employer with a New York office, gave 10.
- **LinkedIn pass (search results only):** 12 people searched and 6 placed. Alfe Hossain and Gisela Chen are in New York. Darcy Norman, Fernando Bolaños, Emily Ng and Dane Slutzky are elsewhere.
- **Still unknown:** 85 people.

## 2. What we learnt

- **Sources that worked:**
  - **The getdbt.com sitemap:** it lists every dbt Summit speaker page, which beats searching agendas.
  - **Meetup `gql2`:** `groupSearch` with a latitude, longitude and radius lists a city's data groups. Each group's events take one more call. Event queries also return host profiles with a city.
  - **GitHub:** the company field ties a profile to the person, and the location field places them.
- **Sources that didn't:**
  - **Medium:** HTTP 429 on every feed, so New York company blogs on Medium are unread.
  - **Web search:** the session limit stopped the run after about 22 searches.
  - **dbt Summit bios:** none of the 18 bios checked names a city.
  - **Brooklyn Data posts:** the author line has no profile link, so most of its consultants stay unplaced.
- **Watch out for:**
  - **Brooklyn Data dominates.** A first-time speaker (an "emerging voice") is someone who publishes about dbt but has no talk on record. 21 of the 24 emerging voices work at Brooklyn Data. Its consultants work remotely: 8 Brooklyn Data people are placed outside New York, and only 3 inside. Cap it at one speaker per event.
  - **Location by headquarters:** most dbt Summit speakers are tied to New York only by their employer's head office. Their location stays unknown.
  - **Bad company record:** "Velir x Brooklyn Data" holds Eric Thomas and Jake Hannan under a three-person title from a 2026 panel.
  - **Old employers:** Millie Symns is listed under Thinx Inc., but dbt Summit 2026 lists Justworks. Ian Macomber, Ryan Delgado and Kevin Chao (Ramp) and Ben Singleton (JetBlue) come from 2022 and 2023 pages.
  - **Spelling:** Phoenix Millicy Jay appears as "Millacy" on the Meetup host profile.

## 3. Key leads

A tier is a priority level. Tier 1 means a person in the region (or not known to be elsewhere) with a dbt item from 2024 onwards, or a first-time speaker with a post from 2024 onwards.

- **First-time speakers:**
  - **Ilan Man (Brooklyn Data, New York):** wrote ["Plan, Build, & Ship: How to Execute a Data Migration"](https://www.brooklyndata.co/ideas/2024/05/29/plan-build-ship-how-to-execute-a-data-migration) (2024-05).
  - **Alfe Hossain (New York):** wrote ["My Experience Migrating to dbt Fusion"](https://www.brooklyndata.co/ideas/2025/12/11/my-experience-migrating-to-dbt-fusion) at Brooklyn Data (2025-12). The LinkedIn result suggests a move to Lithic.
  - **Gisela Chen (New York):** wrote about [dbt's auto-exposures feature](https://www.brooklyndata.co/ideas/2024/12/05/boost-data-visibility-and-trust-with-dbts-new-auto-exposures-feature) at Brooklyn Data (2024-12). The LinkedIn result shows a newer employer.
  - **David Booke (Brooklyn Data):** wrote ["The Overlooked Cost of Snowflake Query Compilation Time"](https://www.brooklyndata.co/ideas/2026/06/24/the-overlooked-cost-of-snowflake-query-compilation-time) (2026-06). Location unknown.
  - **Randy Au (independent):** writes the [Counting Stuff](https://www.counting-stuff.com/how-many-ways-can-we-database-a-store/) newsletter on data work. Location unknown.
- **Anchor speakers:** none of these has spoken at the chapter.
  - **Bilt:** Ben Kramer, James Dorado and Nick Heron, all in New York. They gave two dbt Summit 2026 talks: [the agentic data stack](https://www.getdbt.com/dbt-summit/agenda/inside-the-agentic-data-stack-at-bilt) and [real-time analytics](https://www.getdbt.com/dbt-summit/agenda/real-time-analytics-at-bilt-architecture-and-approach). Bilt also has a dbt case study.
  - **Christine Kwon and Brett Pendleton (Fanatics Betting & Gaming):** [dbt metrics for natural-language analytics](https://www.getdbt.com/dbt-summit/agenda/how-fanatics-manages-dbt-metrics-with-snowflake-coco-for-natural-language-analytics), dbt Summit 2026.
  - **Divyakumar Savla (Datadog):** [catching silent data failures beyond dbt tests](https://www.getdbt.com/dbt-summit/speakers/divyakumar-savla), dbt Summit 2026.
  - **Kensly Alexander and Ariel Kaplan (Planned Parenthood Federation of America):** [a nonprofit's journey with dbt](https://www.getdbt.com/dbt-summit/speakers/kensly-alexander), dbt Summit 2026.
- **Connectors:** community organisers who can introduce people.
  - **Josh Laurito (NY Times):** writes the [NYC Data newsletter](https://nycdata.substack.com/), a weekly list of local events.
  - **Juliet Craig, Tabitha Diaz, Lisa Hitch and Bianca Ng:** organisers of [Data + Women NYC](https://usergroups.tableau.com/data-women-nyc). Ask them for speaker introductions.
  - **Ajay Phatak (Braze) and Kevin Jong (Snowflake):** organisers of the [Snowflake New York User Group](https://usergroups.snowflake.com/new-york).
  - **David Gelman (Brooklyn Data):** [hosts the chapter](https://www.meetup.com/nyc-dbt-meetup/events/314288570/). The Meetup host profile gives Boston.

## 4. Before outreach

- [ ] **Check unknown locations.** 85 people have no known location. Most are dbt Summit speakers tied to New York by their employer's head office.
- [ ] **Check name-only matches.** Kenny Ning, Andi Muskaj and Randy Au matched a profile by name, with nothing tying it to their employer. Their locations stay unknown.
- [ ] **Check Sean McIntyre.** The Vienna location comes from a GitHub profile that lists dbt Labs. Nothing ties it to the 2019 Warby Parker talk.
- [ ] **Check tier-1 people raised by the rule.** Nicholas Thomson (Datadog) is a content writer. Brooklyn Data's marketing author Jill Roberson is also tier 1.
- [ ] **dbt Labs staff are labelled.** Elias DeFaria, Ben Butler and Stephen Robb are tier 1 and work there. They can speak, but check the line-up has practitioners first.
- [ ] **Check two records.** Millie Symns's employer may be out of date, and "Velir x Brooklyn Data" is a joint company record.
- [ ] **Check current employers** for anyone sourced from 2022 or 2023 pages.
- [ ] **Check who is already booked.** Compare leads with the chapter's upcoming events.

## 5. Next run

- **Finish LinkedIn first.** 138 people are still `not_searched`. Start with the dbt Summit speakers whose location is unknown.
- **Retry Medium.** New York company blogs (Justworks and others) are unread. Space the requests out.
- **Find emerging voices outside Brooklyn Data.** Try the Ramp, Datadog, Squarespace and NYT Open engineering blogs.
- **Ask the Data + Women NYC organisers** for analytics engineering speakers.
- **Add job ads.** Try `site:` searches on Lever, Greenhouse and Ashby with "dbt New York".
- **Re-check old profiles** at Ramp and JetBlue.

## 6. Replication prompt

````
You are extending my dataset of New York companies that use dbt, and people who could speak at or
attend the New York dbt Meetup. The file is new_york/new_york_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Region: the NYC metro area.
Read new_york/SEARCH_METHOD.md first, then research/README.md, research/raw-format.md,
research/location-task.md and research/linkedin-task.md.

Budget about 25 web searches. Try these first:
1. Emerging voices outside Brooklyn Data: Ramp, Datadog, Squarespace and NYT Open blogs, and
   Medium feeds of New York companies (space requests out).
2. New dbt Summit speaker pages from the getdbt.com sitemap, filtered to New York employers.
3. New events of New York data groups through Meetup gql2 groupSearch and events, with curl.
4. Job ads: site: searches on Lever, Greenhouse and Ashby for dbt New York.

Rules: never fetch LinkedIn pages, use only search results. Public professional information only;
never record or guess gender; pronouns only when self-stated. Skip past chapter speakers; the
assembler adds them. Cap Brooklyn Data at one speaker per event. Assemble with
research/assemble.py --base, run research/validate.py (must print ok), then add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build from one research run: 89 companies, 151 people, 7 job ads at 6 companies, 30 past meetups. 66 people had spoken at the chapter. Tiers: 52 tier 1, 65 tier 2, 26 tier 3, 8 connectors. Lead types: 113 proven speakers, 24 emerging voices, 8 featured, 6 with no public content. |
| 2026-10-01 | 1 | Location pass from public pages: 26 people placed, 20 in the region and 6 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 12 people searched, 6 placed, 2 in the region and 4 elsewhere. 86 people are still unknown. |
