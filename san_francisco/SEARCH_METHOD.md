# San Francisco: city notes

This file holds what is specific to San Francisco. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [San Francisco dbt Meetup](https://www.meetup.com/san-francisco-dbt-meetup/), data in `san_francisco_dbt_companies.json`
- **Region:** the nine SF Bay Area counties. San Francisco, the Peninsula (San Mateo, Menlo Park, Portola Valley) and the South Bay (Sunnyvale) count. Commuter towns are local for this chapter, so Santa Cruz counts too. San Diego and Irvine do not.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-01)

| | Count |
|---|---|
| Companies | 96 |
| People | 97 |
| Tier 1 leads | 24 |
| First-time speakers (publish, no talk yet) | 10 |
| Proven speakers | 67 |
| Spoke at this chapter before | 36 |
| Based in the region | 56 |
| Based elsewhere | 13 |
| Location unknown | 28 |
| With a LinkedIn profile | 28 |
| Job ads mentioning dbt | 48 |
| Past chapter meetups | 13 |
<!-- at-a-glance:end -->

## 1. Where to look in San Francisco

The first build had about 20 web searches before the shared session limit ran out. The rest came from about 50 page fetches and the GitHub API. Leads are scored by the [central scoring rules](../research/README.md#3-scoring-rules).

### Chapter history and conferences

- **Past chapter speakers:** every named speaker in `../enriched/san-francisco-dbt-meetup.json`, with the talk. 13 meetups, from 2019-06-12 to 2026-08-26, gave 36 people who have spoken at the chapter. One of them, Dori Wilson, was merged with a newer record at Chime.
- **[dbt Summit 2026 sessions by role](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role):** the best page, and the cheapest way to find Bay Area talks. It names speakers and companies at Zipline, Sigma, LangChain, DoorDash and Okta on one page.
- **[Coalesce 2025 sessions overview](https://www.getdbt.com/blog/what-to-expect-from-sessions-at-coalesce-2025):** Okta and Cribl sessions, but most speakers are not named.

### Vendor customer stories and blogs

- **[Hex customer stories](https://hex.tech/customers/):** Chime, LangChain, Figma, Notion and Modern Treasury. Each names Bay Area analytics staff and states the stack. Hex and Omni stories are the cheapest route to practitioners.
- **[Omni blog and case studies](https://omni.co/blog):** Cribl and Handshake, plus posts by Omni staff.
- **[dbt Developer Blog authors](https://docs.getdbt.com/blog/authors):** authors at Mainspring Energy, Merit, Census, Mode and Fivetran. Most posts are from 2022–23.

### Women-in-data communities

People were taken only from each community's own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.

- **[Snowflake Women in Data Bay Area](https://www.snowflake.com/event/women-in-data-bay-area-20260128) (January 2026):** 5 speakers, from DoorDash, Ross Stores, CrowdStrike, Engage3 and Snowflake.
- **[Hightouch Women in Data SF](https://hightouch.com/events/women-in-data-meetup) (February 2023):** 1 keynote speaker.
- **[WiDS Berkeley](https://wids.berkeley.edu/speakers):** WiDS means Women in Data Science. The page shows the 2023 line-up, including an analytics engineering leader at Meta.
- **[PyLadies San Francisco](https://www.meetup.com/pyladiessf/):** monthly talk nights at sponsor offices, with full line-ups on Meetup. The [September 2026 meetup at Snowflake](https://www.meetup.com/pyladiessf/events/315897145/) gave Rose Tan (Snowflake), Kasia Rachuta (Intuit) and Lilinoe Harbottle on data integrity in regulated pipelines. The [October 2025 meetup](https://www.meetup.com/pyladiessf/events/311140845/) gave Dori Wilson, now listed as Head of Data at Recce, and Jennifer Slotnick. Divya Dhar spoke on data cleaning with AI. The organisers are connectors: Alla Barbalat, Semona Igama (Okta), Kasia Rachuta and Shruti Taware.
- **[Bay Area WiMLDS](https://www.meetup.com/bay-area-women-in-machine-learning-and-data-science/):** Women in Machine Learning & Data Science. Monthly talks, often at Snowflake. It gave Amanda Kelly (Snowflake, Streamlit) and Lisa Dusseault (Data Transfer Initiative) in May 2024, Barkha Herman (StarTree) on Apache Pinot and anomaly detection, and Shubhi Asthana (IBM Research) on PII guardrails. A [2023 lightning talk night with Lyft](https://www.meetup.com/bay-area-women-in-machine-learning-and-data-science/events/292687386/) gave Gina Longo (SiriusXM), Grishma Jena (IBM) and 3 Lyft data scientists. Joanne Rodrigues spoke at the joint event with PyLadies in July 2025. The hosts Carolina Arriaga and Erin Pangilinan are connectors.
- **[R-Ladies San Francisco](https://www.meetup.com/rladies-san-francisco/):** no data talks since 2023. Its host Gabriela de Queiroz is a connector.
- **Also ask:** the PyLadies SF and WiMLDS organisers to suggest analytics engineers from their members.

### Meetups, GitHub and job ads

- **[Snowflake Bay Area User Group](https://usergroups.snowflake.com/san-francisco/):** lists its 2 leaders, but not its event speakers.
- **[GitHub user search](https://github.com/search?q=dbt+location%3A%22San+Francisco%22&type=users):** "dbt" in the bio and a San Francisco location. Mostly job-seeker portfolios. Two people were kept.
- **Job ads:** only 3, found through web search, at World, Perplexity and Slash. No LinkedIn Jobs scan was run.
- **[HN Who is hiring](https://hn.algolia.com/api/v1/search?query=dbt&tags=comment):** the Algolia API searched each monthly thread since January 2023 for dbt, one call per thread. Posts were kept when the header names the Bay Area and the text uses the whole word dbt. Gave 7 companies, among them COVU, Folio, Pomelo Care and the DataSF team of the City & County of San Francisco.
- **Company job boards (open JSON):** the Greenhouse, Lever and Ashby APIs return every open ad with its full text. About 60 employers were checked, and ads located in the Bay Area that use the word dbt were kept. Gave Discord, Brex, Plaid, Gusto, Robinhood, Anthropic, Benchling and Vanta as new strong leads. It raised Snowflake and Mercor to strong and PagerDuty to medium.
- **[dbt Labs case studies, full text](https://www.getdbt.com/llms-full-case-studies.txt):** one file, linked from the sitemap, holds every case study with its headquarters line. It added Retool, Vivian Health, Vida Health, SpotOn, Blend, Reforge, Sunrun and Aktify, all with Bay Area headquarters, and confirmed Tempo.

### Locations

- **Location pass (2026-10-01):** page fetches placed 18 people, 12 in the region and 6 outside. The Meetup `gql2` endpoint gave the profile city of each event's hosts and RSVPs, and placed most past chapter speakers. The member must be the RSVP or host of the event where the talk was given. GitHub profiles gave the rest.
- **LinkedIn pass (2026-10-01):** LinkedIn search results placed 7 people, 4 in the region and 3 outside. No LinkedIn page was opened.
- **Other city files:** Karen Hsieh is placed from the same person's record in the Taipei file.

## 2. What didn't work here

- **[dbt Summit 2026 keynotes](https://www.getdbt.com/blog/dbt-summit-2026-keynotes-product-sessions):** dbt Labs staff only.
- **Session and customer pages:** the individual dbt Summit and Coalesce session pages returned 404. So did the getdbt.com case studies and the Datafold and Lightdash customer pages.
- **[Monte Carlo case studies](https://montecarlo.ai/case-studies/):** PagerDuty and Credit Karma. Neither mentions dbt.
- **[Women in Big Data Bay Area](https://www.meetup.com/women-in-big-data-bay-area/):** the Meetup group no longer exists. The [May 2026 summit recap](https://www.womeninbigdata.org/building-the-future-together-reflections-from-the-wibd-bay-area-10-year-innovation-summit/) names only AI and leadership speakers, without employers.
- **Women-focused groups with no data talks:** [GDG San Francisco](https://www.meetup.com/gdgsanfrancisco/) Women Techmakers events (career and AI talks; IWD 2024 cancelled), [Mature Women in Tech](https://www.meetup.com/sfmaturewomenintech/) (career meetings), [Girl Develop It SF](https://www.meetup.com/girl-develop-it-san-francisco/) (paid classes, no named instructors) and [OutGeek Women in Tech](https://www.meetup.com/outgeek-women-in-tech/) (no events).
- **Pages that no longer exist:** the [Data + Women San Francisco](https://usergroups.tableau.com/data-women-san-francisco/) Tableau group page and the [WiDS conference page](https://www.widsworldwide.org/conference/) return 404. Women Who Code closed in 2024.
- **[MotherDuck SF meetups](https://motherduck.com/events/motherduck-duckdb-july-meetup-2026.md):** DuckDB and agent talks, with no dbt speakers.
- **[AI Council Bay Area](https://www.aicouncil.com/bay-2025):** Data Council was renamed, and the page lists no speakers.
- **Company Medium feeds:** [Gusto](https://medium.com/feed/gusto-engineering) and Faire had no dbt posts. [Airbnb](https://medium.com/feed/airbnb-engineering), Lyft and Instacart returned HTTP 429 (too many requests), so Bay Area company tech blogs are still unscanned.
- **GitHub user search:** finds mostly job-seeker portfolios. Only a few are usable speaker leads.
- **GitHub code search for `dbt_project.yml`:** found nothing in about 25 Bay Area orgs, among them stripe, airbnb, lyft, dropbox, instacart, plaid, figma and discord. Vendor orgs return only their own dbt packages.
- **Meetup venue scan:** Snowflake Bay Area, Bay Area Apache Airflow and Data Council SF events since 2024 were held at Snowflake, Lyft, Amazon, Samba TV and Astronomer. None of the events mentions dbt.
- **Job boards with no open JSON:** doordash, rippling, retool, modern-treasury, whatnot and grove answered none of the three APIs. Stripe, Airbnb, Notion, OpenAI, Pinterest, Reddit and Carta had no ad that uses the word dbt.
- **HN posts skipped:** posts that name dbt only as an investor or as a product integration, and posts with no company name, were not counted as dbt users.

## 3. Companies looked at

- **Vendors dominate the Bay Area.** Hex, Omni, Sigma, Fivetran and dbt Labs staff publish the most. Rank vendor staff below practitioners at non-vendor companies.
- **Fivetran and dbt Labs have merged.** Toby Mao and Donny Flynn are labelled as Fivetran staff. Census staff are not labelled, so Boris Jabes is not. Dave Fowler already sits under dbt Labs.
- **Many leads are featured** in someone else's content, with no talk or post of their own. Ask these people for a first talk rather than a repeat.

<!-- companies:start -->
95 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (58)</summary>

Absolunet.com (local presence not confirmed), Aktify, Altimate AI (local presence not confirmed), Anthropic, Benchling, Blend, Brex, Census, Chime, City & County of San Francisco, COVU, Cribl, Datafold (local presence not confirmed), dbt Labs, Decodable (local presence not confirmed), Discord, DocuSign, DoorDash, Envoy (local presence not confirmed), Fastly (local presence not confirmed), Figma, Fishtown Analytics (local presence not confirmed), Fivetran, Folio, Grove Collaborative (local presence not confirmed), Gusto, Hex, Instacart, Kaelio (local presence not confirmed), Landed (local presence not confirmed), LangChain, Mainspring Energy, Mercor, Merit (local presence not confirmed), Metabase (local presence not confirmed), Nimbus Intelligence (local presence not confirmed), Okta, Omni, Plaid, Pomelo Care, Reforge, Retool, Robinhood, Sigma Computing, Snowflake, SpotOn, Stealth (local presence not confirmed), Sunrun, Tempo, Vanta, Vida Health, Vivian Health, Whatnot (local presence not confirmed), World, Yerdle Recommerce (local presence not confirmed), Zing (local presence not confirmed), Zipline, Zoox (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (14)</summary>

Databricks, Delfina, Faire, Hightouch, InScope, Mercury, Mode, Monte Carlo, MotherDuck, PagerDuty, Perplexity, Poshmark, Slash, Spinwheel (local presence not confirmed)

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

Scale AI

</details>

<details><summary><b>Not verified</b> (12)</summary>

Big Time Data (local presence not confirmed), Credit Karma, CrowdStrike (local presence not confirmed), DatologyAI (local presence not confirmed), Engage3 (local presence not confirmed), Handshake, Meta, Modern Treasury, Notion, Reddit, Ross Stores, Spaulding Ridge (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (10)</summary>

Bay Area WiMLDS, Data Transfer Initiative (local presence not confirmed), IBM (local presence not confirmed), Intuit (local presence not confirmed), Lyft, PyLadies San Francisco, R-Ladies San Francisco, SiriusXM (local presence not confirmed), StarTree (local presence not confirmed), WiDS Berkeley

</details>

<details><summary><b>Blogs and sites scanned</b> (4)</summary>

- https://hex.tech/blog/
- https://hex.tech/customers/
- https://montecarlo.ai/case-studies/
- https://omni.co/blog

</details>

<details><summary><b>Other sources checked</b> (30)</summary>

- [dbt Summit 2026 sessions by role](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role)
- [dbt Summit 2026 keynotes and product sessions](https://www.getdbt.com/blog/dbt-summit-2026-keynotes-product-sessions) (nothing useful)
- [Coalesce 2025 sessions overview](https://www.getdbt.com/blog/what-to-expect-from-sessions-at-coalesce-2025)
- [Hex customer stories](https://hex.tech/customers/)
- [Omni blog and case studies](https://omni.co/blog)
- [Monte Carlo case studies](https://montecarlo.ai/case-studies/)
- [dbt Developer Blog authors](https://docs.getdbt.com/blog/authors)
- [Snowflake Women in Data Bay Area (Jan 2026)](https://www.snowflake.com/event/women-in-data-bay-area-20260128)
- [Hightouch Women in Data SF (Feb 2023)](https://hightouch.com/events/women-in-data-meetup)
- [WiDS Berkeley speakers](https://wids.berkeley.edu/speakers)
- [Snowflake Bay Area User Group](https://usergroups.snowflake.com/san-francisco/)
- [MotherDuck SF meetups](https://motherduck.com/events/motherduck-duckdb-july-meetup-2026.md) (nothing useful)
- [Gusto and Faire Medium feeds](https://medium.com/feed/gusto-engineering) (nothing useful)
- [Airbnb, Lyft, Instacart Medium feeds](https://medium.com/feed/airbnb-engineering) (nothing useful)
- [Data Council / AI Council Bay Area 2025](https://www.aicouncil.com/bay-2025) (nothing useful)
- [Women in Big Data Bay Area meetup](https://www.meetup.com/women-in-big-data-bay-area/) (nothing useful)
- [GitHub user search (dbt in bio, SF)](https://github.com/search?q=dbt+location%3A%22San+Francisco%22&type=users)
- [Meetup gql2 groupSearch near San Francisco (women-in-data queries)](https://www.meetup.com/gql2#sf-wid)
- [PyLadies San Francisco](https://www.meetup.com/pyladiessf/)
- [Bay Area WiMLDS](https://www.meetup.com/bay-area-women-in-machine-learning-and-data-science/)
- [R-Ladies San Francisco](https://www.meetup.com/rladies-san-francisco/) (nothing useful)
- [GDG San Francisco (Women Techmakers events)](https://www.meetup.com/gdgsanfrancisco/) (nothing useful)
- [Mature Women in Tech (SF)](https://www.meetup.com/sfmaturewomenintech/) (nothing useful)
- [Girl Develop It San Francisco](https://www.meetup.com/girl-develop-it-san-francisco/) (nothing useful)
- [Women in Tech Events by OutGeek Collective](https://www.meetup.com/outgeek-women-in-tech/) (nothing useful)
- [Women in Big Data Bay Area 10-Year Innovation Summit](https://www.womeninbigdata.org/building-the-future-together-reflections-from-the-wibd-bay-area-10-year-innovation-summit/) (nothing useful)
- [Data + Women San Francisco](https://usergroups.tableau.com/data-women-san-francisco/) (nothing useful)
- [WiDS Worldwide conference page](https://www.widsworldwide.org/conference/) (nothing useful)
- [Girls in Tech](https://girlsintech.org/) (nothing useful)
- [Women Who Code](https://womenwhocode.com/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers** (practitioners with dbt material and no talk on record):
  - **Priya Gupta**, Head of Data, Cribl. Quoted at length on dbt docs as the single source of truth for AI analytics: [Omni case study](https://omni.co/blog/case-study-cribl).
  - **Jordan Farrer**, Director of Data Science & Analytics, Chime. Featured on Chime's AI context and evaluation set-up on Snowflake and dbt: [Hex story](https://hex.tech/customers/chime/).
  - **Tyler Ritter**, Senior Analytics Engineer, Handshake. Featured on migrating a ten-year-old analytics estate in eight weeks: [Omni case study](https://omni.co/blog/case-study-handshake).
  - **Chang Sun**, Analytics Engineering Lead, Modern Treasury: [Hex story](https://hex.tech/customers/modern-treasury/).
  - **Charlie Summers**, Staff Software Engineer, Merit. Wrote about turning event streams into tables with dbt (2022): [dbt Developer Blog](https://docs.getdbt.com/blog/demystifying-event-streams).
- **Anchor speakers:**
  - **Harsha Reddy**, DoorDash. dbt Summit 2026 talk on DoorDash's analytics development process with dbt and ThoughtSpot: [agenda](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role).
  - **Logan Cochran**, Analytics Engineer, LangChain. dbt Summit 2026 talk on keeping AI agents to agreed definitions: [agenda](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role).
  - **Matt Senick**, Senior Analytics Engineer, Sigma. dbt Summit 2026 talk and a post on the semantic layer with dbt and Dagster: [Sigma blog](https://www.sigmacomputing.com/blog/semantic-layer-dbt-dagster). Sigma is a vendor.
  - **Josh Wills**, DatologyAI. Creator of dbt-duckdb, based in San Francisco: [GitHub](https://github.com/jwills).
- **Connectors:**
  - **Vince Faller** organised the 2026-08-26 chapter meetup and has spoken there twice: [Meetup profile](https://www.meetup.com/members/481607209/).
  - **Divya Koppolu** and **John Miller** run the [Snowflake Bay Area User Group](https://usergroups.snowflake.com/san-francisco/), which has about 8,700 members.
  - **Karen Hsieh** organised the 2025-04, 2025-10 and 2026-06 chapter meetups: [chapter page](https://www.meetup.com/san-francisco-dbt-meetup/).

## 5. Before outreach

- [ ] **Check the tier-1 people raised by the rule.** The rule raises 5 vendor bloggers to tier 1: Katie Bauer, Rachel Herrera and Izzy Miller (Hex), and Jamie Davidson and Colin Zima (Omni). Deepanshu Girsa is tier 1 on one personal repo.
- [ ] **Skip or re-rank tier-1 people outside the region.** Lexi Galantino is in San Diego, Pooja Crahen in New York and Emily Hawkins in Boston. Hamzah Chaudhary is in London and Juan Manuel Perafan in Norwalk.
- [ ] **Confirm the 26 unknown locations.** They include Matt Senick, Logan Cochran and Harsha Reddy. Harsha Reddy has two possible LinkedIn matches, in Fremont and Santa Clara.
- [ ] **Check the weak location calls.** Jason Lally, Boris Jabes, Raul Maldonado and Pradnesh Patil were placed by a name match to a chapter member only.
- [ ] **Resolve conflicting profiles.** Karen Hsieh's Meetup accounts say Taipei. Gleb Mezhanskiy's Meetup profile says San Francisco but GitHub says New York.
- [ ] **Confirm current employers.** The Chime story lists Dori Wilson at Chime, not Recce. Several dbt Developer Blog authors' roles date from 2022–23.
- [ ] **Check the line-up has practitioners first.** Dave Fowler, Ani Venkateshwaran, Paige Berry, Lauren Benezra and Julia Schottenstein work at dbt Labs, and Toby Mao and Donny Flynn at Fivetran. All are labelled.

## 6. Next run

- **Sources to try first:**
  - **LinkedIn pass:** 53 tier-1 and tier-2 people are still `not_searched`.
  - **LinkedIn Jobs guest scan** (keywords=dbt, San Francisco Bay Area), keeping ads with the whole word dbt. The file has only 3 job ads, all from web search.
  - **dbt Summit speaker pages** (`getdbt.com/dbt-summit/speakers/<slug>`) for Bay Area employers. These give session titles, and worked for Boston and Seattle.
  - **Customer stories:** Hex, Omni and Sigma stories published since `metadata.generated_at`.
  - **Medium feeds:** retry Airbnb, Lyft and Instacart (`medium.com/feed/<publication>`). Find the author of Instacart's "Adopting dbt" post.
  - **Named speakers:** search for the speakers at DocuSign, Figma and Instacart, which have a dbt talk but no named speaker.
  - **Women-in-data communities not reachable:** the [Girls in Tech](https://girlsintech.org/) site timed out. Data + Women San Francisco has no working page; find its new address on the Tableau user group directory.
  - **Dori Wilson:** confirm the move from Chime to Recce before outreach.
- **People to locate:** the 26 unknown locations. Find GitHub logins for the unknown-location people at Hex, Omni, LangChain, DoorDash, Zipline, Sigma and Okta.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `san_francisco/san_francisco_dbt_companies.json`, the chapter `san-francisco-dbt-meetup`, `../enriched/san-francisco-dbt-meetup.json` and the region "the nine SF Bay Area counties, with commuter towns such as Santa Cruz". Budget about 25 web searches.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build: dbt Summit 2026 and Coalesce 2025 agendas, vendor customer stories (Hex, Omni, Monte Carlo), the dbt Developer Blog, the Snowflake Bay Area User Group, 3 women-in-data events, GitHub user search and job ads from web search. Past chapter speakers added from `../enriched/san-francisco-dbt-meetup.json`. 61 companies (36 on the watchlist), 76 people, 3 job ads, 13 past meetups. Split: 51 proven speakers, 10 emerging voices, 13 featured, 2 with no public content. Tiers: 24 tier 1, 41 tier 2, 9 tier 3, 2 connectors. 36 people had already spoken at the chapter. |
| 2026-10-01 | 1 | Location pass: 18 people placed from Meetup host and RSVP profiles and GitHub, 12 in the region and 6 outside. |
| 2026-10-01 | 1 | LinkedIn pass: 7 people placed from LinkedIn search results, 4 in the region and 3 outside. 27 people are still unknown. |
| 2026-10-01 | 2 | Women-in-data pass with fetches only: 21 people added from PyLadies SF, Bay Area WiMLDS and R-Ladies SF, 15 speakers and 6 connectors, and a new talk added for Dori Wilson. 9 companies added. 13 women-focused communities checked. |
| 2026-10-01 | 3 | Company pass with fetches only: HN Who is hiring, company job boards, dbt Labs case studies, GitHub code search and Meetup venues. 70 to 96 companies. 26 added, 19 with a strong dbt signal. Snowflake and Mercor raised to strong, PagerDuty to medium. Bay Area presence confirmed for the City & County of San Francisco, Tempo and Census. Job ads 3 to 48. |
