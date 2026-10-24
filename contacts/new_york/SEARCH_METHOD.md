# New York: city notes

This file holds what is specific to New York. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [New York dbt Meetup](https://www.meetup.com/nyc-dbt-meetup/), data in `new_york_dbt_companies.json`
- **Region:** the NYC metro area.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-01)

| | Count |
|---|---|
| Companies | 118 |
| People | 166 |
| Tier 1 leads | 45 |
| First-time speakers (publish, no talk yet) | 24 |
| Proven speakers | 121 |
| Spoke at this chapter before | 65 |
| Based in the region | 84 |
| Based elsewhere | 24 |
| Location unknown | 58 |
| With a LinkedIn profile | 98 |
| Job ads mentioning dbt | 59 |
| Past chapter meetups | 30 |
<!-- at-a-glance:end -->

## 1. Where to look in New York

One research run covered New York. It used about 22 web searches before the session limit stopped it. Everything after that came from direct page fetches. Leads are scored by the [central scoring rules](../research/README.md#3-scoring-rules).

### dbt conference pages

- **[dbt Summit 2026 speaker pages](https://www.getdbt.com/sitemap-0.xml):** the getdbt.com sitemap lists all 178 speaker pages, which beats searching agendas. Each page gives name, title, employer, bio and session. About 30 speakers work for New York employers.
- **[dbt case studies](https://www.getdbt.com/case-studies/bilt-rewards):** the same sitemap lists them. Bilt, Ramp, J.Crew, Wellthy, Nasdaq and JetBlue are New York area companies.
- **[Coalesce on the Road NYC 2026](https://www.getdbt.com/events/roadshow/coalesce-in-nyc):** a Bilt customer session, with no talk titles.

### Meetups

- **Chapter history:** every named speaker in [`../enriched/nyc-dbt-meetup.json`](../enriched/nyc-dbt-meetup.json) was added as a person. That file holds 30 meetups, from 2019-07-31 to 2026-09-30. 65 people in the file have spoken at the chapter.
- **Meetup `gql2`:** `groupSearch` near Manhattan, with a latitude, longitude and radius, listed about 45 New York data groups. Each group's 2024 to 2026 events took one more call, with no browser. Event queries also return host profiles with a city.
- **[NYC Apache Airflow Meetup](https://www.meetup.com/nyc-apache-airflow-meetup/):** 30 events from 2024 to 2026, including one dbt talk on the Cosmos package.
- **[ClickHouse New York User Group](https://www.meetup.com/clickhouse-new-york-user-group/):** speakers from Ramp, Clay, Hex, Evidence, Braze and Datavations.
- **[Apache Spark NYC](https://www.meetup.com/spark-nyc/):** Datadog, EXL and Nielsen speakers.
- **[Databricks Community Meetup NYC](https://www.meetup.com/databricks-community-meetup-nyc/):** one FanDuel speaker.
- **[Data Engineer Things NYC #2](https://motherduck.com/events/det-nyc-2-meetup-2026/):** one named speaker.
- **[Snowflake New York User Group](https://usergroups.snowflake.com/new-york):** organisers only.

### Company and consultancy blogs

- **[Brooklyn Data](https://www.brooklyndata.co/ideas):** bylines on 20 dbt posts. Brooklyn Data organises the chapter.
- **[Datadog](https://www.datadoghq.com/blog/understanding-dbt/):** a dbt best-practice post.
- **[NYC Data newsletter](https://nycdata.substack.com/archive):** a weekly list of New York data events and local writers.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[Data + Women NYC](https://usergroups.tableau.com/data-women-nyc):** gave its organisers. Its events focus on Tableau.
- **[NYC WiMLDS](https://www.meetup.com/nyc-wimlds/):** one panel with named data leaders, on generative AI. Its events since then are AI demo nights and LLM bootcamps.
- **[GDG NYC and Women Techmakers NYC](https://www.meetup.com/gdgnyc/):** the Women Techmakers Ambassadors run International Women's Day and women-in-AI events, mostly at Google's New York office. The Meetup copies carry full speaker bios. [Build with AI 2024](https://www.meetup.com/gdgnyc/events/300509530/) gave Paige Epstein and Dean Manko of Kantar on LLMs in digital analytics. [Power Women in AI/ML 2023](https://www.meetup.com/gdgnyc/events/294478731/) gave Jayeeta Putatunda (Fitch Ratings). [Women in AI/ML 2023](https://www.meetup.com/gdgnyc/events/292262065/) gave Supreet Kaur (Morgan Stanley) and Phanom Noelani Parker (Amazon). The organisers are connectors: Anna Nerezova, Shivika Arora (JPMorgan Chase) and Carolina Castro (Google). Events since 2025 are mostly AI hackathons.
- **[R-Ladies New York](https://www.meetup.com/rladiesnyc/):** the Meetup slug is `rladiesnyc`. It runs talks, tutorials and lightning talks. Talks since 2024 gave Jennifer Hill on causal inference, Rika Gorn on Quarto and Mitzi Morris on Stan. The gql2 `eventHosts` field gave 5 regular hosts as connectors: Dorota Rizik, Jacki Buros, Clara Wang, Mei Guan and Nicole Burke.
- **Also ask:** the GDG NYC and R-Ladies hosts to suggest analytics engineers from their members.

### Job ads

- **[Built In NYC](https://www.builtinnyc.com/jobs/data-analytics/search/analytics-engineer):** ads from Clay, Datavations, Brainforge and Zocdoc quote dbt.
- **Venture capital job boards:** gave ads at Zocdoc, GlossGenius and Peloton.
- **Result:** 7 ads at 6 companies. All 7 show dbt in the ad text.
- **[HN Who is hiring](https://hn.algolia.com/api/v1/search?query=dbt&tags=comment):** the Algolia API searched each monthly thread since January 2023 for dbt, one call per thread. Posts were kept when the header names New York and the text uses the whole word dbt. Gave 9 companies, among them Atria Health, Garner Health, iCapital, EnergyHub (Brooklyn office) and Absinthe Labs.
- **Company job boards (open JSON):** the Greenhouse, Lever and Ashby APIs return every open ad with its full text. About 60 employers were checked, and ads located in New York that use the word dbt were kept. Gave CLEAR and Ro as new strong leads. It also found NYC data roles at Anthropic, Plaid, Gusto, Headway, Figma, Maven Clinic and Sigma Computing. It confirmed New York presence for Oscar Health, Peloton, Justworks and Rent the Runway.
- **[dbt Labs case studies, full text](https://www.getdbt.com/llms-full-case-studies.txt):** one file, linked from the sitemap, holds every case study with its headquarters line. Its headquarters lines confirm J.Crew, Wellthy, Bilt, Ramp, Nasdaq and JetBlue in New York.

### Locations

- **Location pass (page fetches):** 26 people placed, 20 in the region and 6 elsewhere, under the [central location rules](../research/README.md#6-location-rules). Meetup host profiles of the person's own event gave 5. GitHub profiles with a matching employer gave 11, because the company field ties a profile to the person and the location field places it. In-person chapter talks since late 2024, at an employer with a New York office, gave 10.
- **LinkedIn pass (search results only):** 12 people searched and 6 placed. Alfe Hossain and Gisela Chen are in New York. Darcy Norman, Fernando Bolaños, Emily Ng and Dane Slutzky are elsewhere.

## 2. What didn't work here

- **Medium:** every [Medium feed](https://medium.com/feed/justworks-tech) returned HTTP 429 (too many requests), so New York company blogs on Medium are unread.
- **[NYT Open blog](https://open.nytimes.com/feed):** blocked the fetch.
- **[Squarespace engineering blog](https://engineering.squarespace.com/blog):** no data posts on its first page.
- **[PyData NYC](https://www.meetup.com/pydatanyc/):** no dbt talks from 2024 to 2026.
- **[Data Council NYC group](https://www.meetup.com/data-council-nyc-data-engineering-science/):** only promotes other conferences.
- **[NYC PyLadies](https://www.meetup.com/nyc-pyladies/):** one event since 2024, on vector search.
- **[NYC PyLadies](https://www.meetup.com/nyc-pyladies/):** no event since October 2024.
- **Women-focused Meetup groups with no data talks:** [Girl Develop It NYC](https://www.meetup.com/girldevelopit/) runs paid classes and doesn't name instructors. [Women in Software Engineering NYC](https://www.meetup.com/women-in-software-engineering-nyc/) runs bootcamp sessions and AI hackathons. [NYC Women in STEM](https://www.meetup.com/nyc-stem/) is a book club. [NYC Fintech Women](https://www.meetup.com/nyc-fintech-women/) posts vendor events. [Real Women in Tech](https://www.meetup.com/real-women-in-tech/) has no events. [New York AI 2030](https://www.meetup.com/new-york-ai-2030-women-in-ai-leadership-award-group/) runs responsible AI summits.
- **[Lesbians Who Tech Summit](https://lesbianswhotech.org/):** held in New York each October. Its speakers are executives, with no data talk titles.
- **No New York chapter or event:** [Women in Big Data](https://www.womeninbigdata.org/), [WiDS](https://www.widsworldwide.org/events/), [She Loves Data](https://www.shelovesdata.com/) and [Women on Snowflake](https://usergroups.snowflake.com/women-on-snowflake/). Women Who Code closed in 2024.
- **[GDG NYC Bevy API](https://gdg.community.dev/api/event_slim/for_chapter/937/?status=Completed&page_size=100):** the list is unsorted and has no speakers. The Meetup copies are easier.
- **Web search:** the session limit stopped the run after about 22 searches.
- **dbt Summit bios:** none of the 18 bios checked names a city.
- **Brooklyn Data posts:** the author line has no profile link, so most of its consultants stay unplaced.
- **GitHub code search for `dbt_project.yml`:** found nothing in about 35 New York orgs, among them spotify, squarespace, etsy, seatgeek, zocdoc, justworks, nytimes and ramp.
- **Meetup venue scan:** the venues of New York Data and AI, NYC Apache Airflow, Databricks Community NYC, NYC MLOps and Real Time Analytics events since 2024 named Ramp, Zocdoc and Astronomer. All three were already in the file.
- **Job boards with no open JSON:** chainalysis, noom, bilt, etsy, doubleverify, dataminr, warbyparker, glossgenius, cityblockhealth, nytimes and hebbia answered none of the three APIs.
- **HN posts skipped:** posts that name dbt only as an investor or as a product integration, and posts with no company name, were not counted as dbt users.

## 3. Companies looked at

- **Brooklyn Data dominates.** 21 of the 24 first-time speakers work at Brooklyn Data, which organises the chapter. Its consultants work remotely: 9 Brooklyn Data people are placed outside New York, and only 4 inside. Cap it at one speaker per event.
- **Location by headquarters:** most dbt Summit speakers are tied to New York only by the employer's head office. Those locations stay unknown.
- **Bilt** has the strongest company story, with two dbt Summit 2026 talks and a dbt case study.

<!-- companies:start -->
117 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (86)</summary>

A&E Networks (local presence not confirmed), Absinthe Labs, AlphaSense, Anthropic, Astronomer, Atria Health, Avenue One (local presence not confirmed), BARK (local presence not confirmed), Better.com (local presence not confirmed), Billie (local presence not confirmed), Bilt, BMG (local presence not confirmed), Bombas (local presence not confirmed), Bowery Farming (local presence not confirmed), Brainforge, Brooklyn Data, Casper (local presence not confirmed), Cityblock Health (local presence not confirmed), Clay, CLEAR, Dandy (local presence not confirmed), Data Culture (local presence not confirmed), Data for Progress (local presence not confirmed), DatabaseTycoon (local presence not confirmed), Datadog, Datavations, dbt Labs (local presence not confirmed), DonorsChoose (local presence not confirmed), DoubleVerify (local presence not confirmed), Elevate Labs (local presence not confirmed), EnergyHub, Espresso AI, Fanatics Betting & Gaming (local presence not confirmed), Figma, Flywire (local presence not confirmed), Folio, GameChanger (local presence not confirmed), Garner Health, GlossGenius, Greenhouse (local presence not confirmed), Gusto, Headway, Hex, iCapital, J.Crew, JetBlue, Justworks, Kaplan North America (local presence not confirmed), Lyft Bikes & Scooters (local presence not confirmed), Materialize, Maven Clinic, Mode Analytics (local presence not confirmed), Nasdaq, OM1 (local presence not confirmed), Oscar Health, P.volve (local presence not confirmed), Peloton, PICO Portal (local presence not confirmed), Plaid, Planned Parenthood Federation of America (local presence not confirmed), Pomelo Care, pymetrics (local presence not confirmed), Qventus (local presence not confirmed), Ramp, Rec Room (local presence not confirmed), Rent the Runway, Ro, Share Local Media (SLM), Sigma Computing, Snowflake, Sorare (local presence not confirmed), Spotify, Squarespace (local presence not confirmed), Steady (local presence not confirmed), TeePublic (local presence not confirmed), Textql (local presence not confirmed), The Atlantic (local presence not confirmed), The Trevor Project (local presence not confirmed), Thinx Inc. (local presence not confirmed), Velir x Brooklyn Data (local presence not confirmed), Verisk (local presence not confirmed), Warby Parker (local presence not confirmed), Wellthy, Westchester Medical Center, WeWork (local presence not confirmed), Zocdoc

</details>

<details><summary><b>Some dbt signal</b> (12)</summary>

Bluecore (local presence not confirmed), Braze, Delfina, Evidence (local presence not confirmed), Faire, Gen Digital (MoneyLion) (local presence not confirmed), Mercury, MotherDuck (local presence not confirmed), NY Times, Robinhood, SeatGeek (local presence not confirmed), The Information Lab

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

Scale AI

</details>

<details><summary><b>Not verified</b> (10)</summary>

Artemis (local presence not confirmed), Circle (local presence not confirmed), EXL (local presence not confirmed), FanDuel (local presence not confirmed), Ippon Technologies USA (local presence not confirmed), JPMorgan Chase, Nielsen (local presence not confirmed), SoFi (local presence not confirmed), Third Point (local presence not confirmed), United Nations Federal Credit Union

</details>

<details><summary><b>Uses a different stack</b> (8)</summary>

Amazon (local presence not confirmed), Fitch Ratings (local presence not confirmed), GDG NYC, Google, Kantar (local presence not confirmed), Morgan Stanley (local presence not confirmed), NYC Women in Machine Learning & Data Science, R-Ladies New York

</details>

<details><summary><b>Blogs and sites scanned</b> (1)</summary>

- https://www.brooklyndata.co/ideas

</details>

<details><summary><b>Other sources checked</b> (42)</summary>

- [dbt Summit 2026 speaker pages (via getdbt.com sitemap)](https://www.getdbt.com/sitemap-0.xml)
- [Coalesce on the Road NYC 2026](https://www.getdbt.com/events/roadshow/coalesce-in-nyc)
- [dbt case studies (sitemap)](https://www.getdbt.com/case-studies/bilt-rewards)
- [NYC Apache Airflow Meetup](https://www.meetup.com/nyc-apache-airflow-meetup/)
- [ClickHouse New York User Group](https://www.meetup.com/clickhouse-new-york-user-group/)
- [Apache Spark NYC](https://www.meetup.com/spark-nyc/)
- [PyData NYC](https://www.meetup.com/pydatanyc/) (nothing useful)
- [Databricks Community Meetup NYC](https://www.meetup.com/databricks-community-meetup-nyc/)
- [Data Council NYC meetup](https://www.meetup.com/data-council-nyc-data-engineering-science/) (nothing useful)
- [Snowflake New York User Group](https://usergroups.snowflake.com/new-york)
- [Data Engineer Things NYC #2](https://motherduck.com/events/det-nyc-2-meetup-2026/)
- [Brooklyn Data blog](https://www.brooklyndata.co/ideas)
- [Datadog blog](https://www.datadoghq.com/blog/understanding-dbt/)
- [NYC Data newsletter](https://nycdata.substack.com/archive)
- [Data + Women NYC](https://usergroups.tableau.com/data-women-nyc)
- [NYC WiMLDS](https://www.meetup.com/nyc-wimlds/)
- [NYC PyLadies](https://www.meetup.com/nyc-pyladies/) (nothing useful)
- [R-Ladies NYC](https://www.meetup.com/rladies-newyork/) (nothing useful)
- [Medium RSS feeds of nyc company blogs](https://medium.com/feed/justworks-tech) (nothing useful)
- [NYT Open blog](https://open.nytimes.com/feed) (nothing useful)
- [Squarespace engineering blog](https://engineering.squarespace.com/blog) (nothing useful)
- [Built In NYC job ads](https://www.builtinnyc.com/jobs/data-analytics/search/analytics-engineer)
- [Meetup gql2 groupSearch near Manhattan (women-in-data queries)](https://www.meetup.com/gql2#nyc-wid)
- [GDG NYC (Women Techmakers events)](https://www.meetup.com/gdgnyc/)
- [GDG NYC Bevy events API](https://gdg.community.dev/api/event_slim/for_chapter/937/?status=Completed&page_size=100) (nothing useful)
- [R-Ladies New York (Meetup rladiesnyc)](https://www.meetup.com/rladiesnyc/)
- [NYC WiMLDS (re-check)](https://www.meetup.com/nyc-wimlds/events/) (nothing useful)
- [NYC PyLadies (re-check)](https://www.meetup.com/nyc-pyladies/events/) (nothing useful)
- [Girl Develop It NYC](https://www.meetup.com/girldevelopit/) (nothing useful)
- [Women in Software Engineering NYC](https://www.meetup.com/women-in-software-engineering-nyc/) (nothing useful)
- [NYC Women in STEM](https://www.meetup.com/nyc-stem/) (nothing useful)
- [NYC Fintech Women](https://www.meetup.com/nyc-fintech-women/) (nothing useful)
- [Real Women in Tech](https://www.meetup.com/real-women-in-tech/) (nothing useful)
- [Empowering Women of Color in Technology](https://www.meetup.com/source-coder-hub/) (nothing useful)
- [New York AI 2030 (women in AI leadership group)](https://www.meetup.com/new-york-ai-2030-women-in-ai-leadership-award-group/) (nothing useful)
- [Lesbians Who Tech Summit New York](https://lesbianswhotech.org/) (nothing useful)
- [Women in Big Data (New York)](https://www.womeninbigdata.org/?s=new+york) (nothing useful)
- [WiDS Worldwide events](https://www.widsworldwide.org/events/) (nothing useful)
- [Women on Snowflake](https://usergroups.snowflake.com/women-on-snowflake/) (nothing useful)
- [She Loves Data](https://www.shelovesdata.com/) (nothing useful)
- [Girls in Tech New York](https://girlsintech.org/new-york/) (nothing useful)
- [Women Who Code](https://womenwhocode.com/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Ilan Man (Brooklyn Data, New York):** wrote ["Plan, Build, & Ship: How to Execute a Data Migration"](https://www.brooklyndata.co/ideas/2024/05/29/plan-build-ship-how-to-execute-a-data-migration) (2024-05).
  - **Alfe Hossain (New York):** wrote ["My Experience Migrating to dbt Fusion"](https://www.brooklyndata.co/ideas/2025/12/11/my-experience-migrating-to-dbt-fusion) at Brooklyn Data (2025-12). The LinkedIn result suggests a move to Lithic.
  - **Gisela Chen (New York):** wrote about [dbt's auto-exposures feature](https://www.brooklyndata.co/ideas/2024/12/05/boost-data-visibility-and-trust-with-dbts-new-auto-exposures-feature) at Brooklyn Data (2024-12). The LinkedIn result shows a newer employer.
  - **David Booke (Brooklyn Data):** wrote ["The Overlooked Cost of Snowflake Query Compilation Time"](https://www.brooklyndata.co/ideas/2026/06/24/the-overlooked-cost-of-snowflake-query-compilation-time) (2026-06). Location unknown.
  - **Randy Au (independent):** writes the [Counting Stuff](https://www.counting-stuff.com/how-many-ways-can-we-database-a-store/) newsletter on data work. Location unknown.
- **Anchor speakers:** none of these has spoken at the chapter.
  - **Bilt:** Ben Kramer, James Dorado and Nick Heron, all in New York. The three gave two dbt Summit 2026 talks: [the agentic data stack](https://www.getdbt.com/dbt-summit/agenda/inside-the-agentic-data-stack-at-bilt) and [real-time analytics](https://www.getdbt.com/dbt-summit/agenda/real-time-analytics-at-bilt-architecture-and-approach).
  - **Christine Kwon and Brett Pendleton (Fanatics Betting & Gaming):** [dbt metrics for natural-language analytics](https://www.getdbt.com/dbt-summit/agenda/how-fanatics-manages-dbt-metrics-with-snowflake-coco-for-natural-language-analytics), dbt Summit 2026.
  - **Divyakumar Savla (Datadog):** [catching silent data failures beyond dbt tests](https://www.getdbt.com/dbt-summit/speakers/divyakumar-savla), dbt Summit 2026.
  - **Kensly Alexander and Ariel Kaplan (Planned Parenthood Federation of America):** [a nonprofit's journey with dbt](https://www.getdbt.com/dbt-summit/speakers/kensly-alexander), dbt Summit 2026.
- **Connectors:**
  - **Josh Laurito (NY Times):** writes the [NYC Data newsletter](https://nycdata.substack.com/), a weekly list of local events.
  - **Juliet Craig, Tabitha Diaz, Lisa Hitch and Bianca Ng:** organisers of [Data + Women NYC](https://usergroups.tableau.com/data-women-nyc). Ask the four for speaker introductions.
  - **Ajay Phatak (Braze) and Kevin Jong (Snowflake):** organisers of the [Snowflake New York User Group](https://usergroups.snowflake.com/new-york).
  - **David Gelman (Brooklyn Data):** [hosts the chapter](https://www.meetup.com/nyc-dbt-meetup/events/314288570/). The Meetup host profile gives Boston.

## 5. Before outreach

- [ ] **Check unknown locations.** 84 people have no known location. Most are dbt Summit speakers tied to New York by the employer's head office.
- [ ] **Check name-only matches.** Kenny Ning, Andi Muskaj and Randy Au matched a profile by name, with nothing tying it to the employer. These locations stay unknown.
- [ ] **Check Sean McIntyre.** The Vienna location comes from a GitHub profile that lists dbt Labs. Nothing ties it to the 2019 Warby Parker talk.
- [ ] **Check tier-1 people raised by the rule.** Nicholas Thomson (Datadog) is a content writer. Brooklyn Data's marketing author Jill Roberson is also tier 1.
- [ ] **Check the line-up has practitioners first.** Elias DeFaria, Ben Butler and Stephen Robb are tier 1, work at dbt Labs and are labelled.
- [ ] **Check two records.** Millie Symns is listed under Thinx Inc., but dbt Summit 2026 lists Justworks. "Velir x Brooklyn Data" holds Eric Thomas and Jake Hannan under a three-person title from a 2026 panel.
- [ ] **Check current employers** for anyone sourced from 2022 or 2023 pages. Ian Macomber, Ryan Delgado and Kevin Chao (Ramp) and Ben Singleton (JetBlue) come from those pages.
- [ ] **Check spelling.** Phoenix Millicy Jay appears as "Millacy" on the Meetup host profile.
- [ ] **Check who is already booked.** Compare leads with the chapter's upcoming events.

## 6. Next run

- **Sources to try first:**
  - **First-time speakers outside Brooklyn Data:** the Ramp, Datadog, Squarespace and NYT Open engineering blogs.
  - **Medium:** retry the New York company blogs (Justworks and others). Space the requests out.
  - **dbt Summit:** new speaker pages from the getdbt.com sitemap, filtered to New York employers.
  - **Meetup `gql2`:** new events of New York data groups through `groupSearch` and events, with `curl`.
  - **Data + Women NYC:** ask the organisers for analytics engineering speakers.
  - **Women-in-data communities not reachable:** the [Girls in Tech New York](https://girlsintech.org/new-york/) site timed out. The [R-Ladies NYC board page](https://www.rladiesnyc.org/#board) did not render. Retry both.
  - **Lesbians Who Tech Summit:** check the 2026 agenda after the 5-7 October summit for data talks.
  - **Job ads:** `site:` searches on Lever, Greenhouse and Ashby with "dbt New York".
- **People to locate:** 108 people are still `not_searched` on LinkedIn. Start with the dbt Summit speakers whose location is unknown. Re-check old profiles at Ramp and JetBlue.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `new_york/new_york_dbt_companies.json`, the chapter `nyc-dbt-meetup`, `../enriched/nyc-dbt-meetup.json` and the region "the NYC metro area". Cap Brooklyn Data at one speaker per event. Budget about 25 web searches.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build from one research run: 89 companies, 151 people, 7 job ads at 6 companies, 30 past meetups. 66 people had spoken at the chapter. Tiers: 52 tier 1, 65 tier 2, 26 tier 3, 8 connectors. Lead types: 113 proven speakers, 24 emerging voices, 8 featured, 6 with no public content. |
| 2026-10-01 | 1 | Location pass from public pages: 26 people placed, 20 in the region and 6 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 12 people searched, 6 placed, 2 in the region and 4 elsewhere. 86 people are still unknown. |
| 2026-10-01 | 2 | Women-in-data pass with fetches only: 16 people added from GDG NYC and Women Techmakers NYC and R-Ladies New York, 8 speakers and 8 connectors. 7 companies added. 20 women-focused communities checked. |
| 2026-10-01 | 3 | Company pass with fetches only: HN Who is hiring, company job boards, dbt Labs case studies, GitHub code search and Meetup venues. 96 to 118 companies. 22 added, 17 with a strong dbt signal. Oscar Health raised to strong. New York presence confirmed for Peloton, Oscar Health, J.Crew, Wellthy, Rent the Runway, Materialize and Justworks. Job ads 7 to 59. |
