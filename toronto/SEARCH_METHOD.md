# Toronto dbt search: method, lessons and replication prompt

This file goes with `toronto_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in the Greater Toronto Area who could **speak at** (or attend) the [Toronto dbt Meetup](https://www.meetup.com/toronto-dbt-meetup/), and the local companies that use dbt.
- **Region:** the Greater Toronto Area, including the Waterloo region.

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 103 |
| People | 69 |
| Tier 1 leads | 4 |
| First-time speakers (publish, no talk yet) | 8 |
| Proven speakers | 51 |
| Spoke at this chapter before | 4 |
| Based in the region | 62 |
| Based elsewhere | 2 |
| Location unknown | 5 |
| With a LinkedIn profile | 3 |
| Job ads mentioning dbt | 70 |
| Past chapter meetups | 4 |
<!-- at-a-glance:end -->

## 1. How the search was done

Two research runs built the file. The first build (2026-09-24) used about 18 web searches and a job ad scan. The extension (2026-10-01) used about 20 web searches, then direct page fetches once the session limit was reached.

### Step 1: Local user groups and meetups

- **[Snowflake Toronto User Group](https://usergroups.snowflake.com/toronto/):** the best source of 2025 and 2026 local speakers and organisers. Its Bevy pages fetch cleanly. The [Meetup copy of the group](https://www.meetup.com/snowflake-usergroup-toronto/) added 11 events, including 2026 expert tables.
- **[Toronto Databricks User Group](https://usergroups.databricks.com/toronto-databricks-user-group/):** July 2026 speakers. dbt Labs is a local sponsor.
- **[Toronto Modern Data Stack](https://www.meetup.com/toronto-modern-data/):** the city's 2022 to 2024 dbt speaker pool. The group is now dormant and has rebranded as Toronto Enterprise AI. Its speakers' roles need re-checking.
- **Found through Meetup `gql2`:** 25 Toronto and Waterloo groups, listed in one `groupSearch` call by latitude and longitude. The ones that yielded were:
  - [Toronto Apache Airflow Meetup](https://www.meetup.com/toronto-apache-airflow-meetup/): three speakers at an in-person event in May 2025.
  - [Toronto Apache Kafka Ecosystem Meetup](https://www.meetup.com/toronto-kafka/): Geotab data platform talks in September 2026.
  - [Toronto Data Engineering Meetup with ClickHouse](https://luma.com/8p8unbnw): 2026 speakers from FiveOneFour and Evidence.
- **Organiser only:** [Data Engineers in Toronto](https://www.meetup.com/data-engineers-in-toronto/) runs online talks centred on Microsoft Fabric.
- **No yield:** the [Toronto Data Professionals Community](https://www.meetup.com/toronto-data-professionals-meetup-group/) had one intro-to-dbt talk, by a speaker from outside the region. The [Waterloo Data Science and Data Engineering](https://www.meetup.com/waterloo-data-science/) group, ODSC, Analytics.Club and Toronto AI groups had no dbt or analytics engineering talks since 2024.

### Step 2: Conferences

- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** matching Toronto employer names against the page text found only KOHO, with Célia Bru and Gabriel Gambacorta.
- **[Databricks Data + AI World Tour Toronto 2025](https://dataaisummit.databricks.com/flow/db/wt25yyz/scheduler/page/catalog):** customer speakers from CIBC, Manulife, Intact, Apotex and Canadian Tire, mostly senior leaders.
- **[Generative AI Summit Toronto](https://world.aiacceleratorinstitute.com/location/toronto/speakers):** data leaders from Wealthsimple, RBC, TD and Interac, on AI topics.
- **Not readable:** the [Coalesce 2025 speaker pages](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/speakers) and the [Snowflake World Tour Toronto 2026 speakers](https://www.snowflake.com/en/world-tour/toronto/speakers/) are rendered by JavaScript. The [Big Data & Analytics Summit Canada](https://bigdatasummitcanada.com/all-speakers/) was not fetched.

### Step 3: Company blogs

- **[Loblaw Digital on Medium](https://medium.com/loblaw-digital):** the best Toronto company blog for dbt authors. A post on generating dbt documentation with LLMs, and a Data as a Service series, name 7 authors. Medium blocks direct fetches, so the feeds were read through `api.rss2json.com`.
- **[Shopify Data](https://medium.com/data-shopify):** dbt posts from 2020 only.
- **No dbt posts:** the [Shopify Engineering](https://shopify.engineering/), [Wealthsimple Engineering](https://engineering.wealthsimple.com/) and [Faire](https://craft.faire.com/all?topic=engineering) blogs, and the latest 10 posts of the [Wealthsimple Medium feed](https://medium.com/wealthsimple).
- **No yield:** [dev.to](https://dev.to/t/dbt) and GitHub user search by location gave job-seeker portfolios, not speakers. GitHub gave one person, Hubert Chan (Granum).

### Step 4: Women-in-data communities

This step finds speakers through women-focused groups' own events. It never records or guesses anyone's gender.

- **[PyLadies Toronto](https://www.meetup.com/PyLadies-Toronto/):** its organiser is recorded as a connector. The group is back in person from April 2026, with a call for lightning talks.
- **[AWS User Group Women in Tech Ontario](https://www.meetup.com/aws-women-in-tech-user-group-ontario/):** its organiser is recorded as a connector.
- **[R-Ladies Toronto](https://www.meetup.com/R-Ladies-Toronto/):** one lightning-talk speaker.
- **[WiDS Toronto @ Dataiku](https://www.widsworldwide.org/events/event/wids-toronto-dataiku/):** names event ambassadors only, not panellists.
- **No yield:** [PyData Toronto](https://www.meetup.com/pydata-toronto/), Toronto Women's Data Group and Women in Big Data Toronto had no local speaker events since mid-2024.
- **Result:** 5 people are tagged `women_in_data_community`.

### Step 5: Job ads

- **First build:** a logged-out scan of LinkedIn Jobs for "dbt" in the Toronto area. Up to 150 ads were checked for the whole word "dbt". 70 ads at 52 companies mention it.
- **Current rule:** the shared method no longer allows fetching the LinkedIn Jobs API. Refresh the ads through job board `site:` searches instead.

### Step 6: Chapter history

- **Source:** every named speaker in [`../enriched/toronto-dbt-meetup.json`](../enriched/toronto-dbt-meetup.json) was added as a person. That file holds 4 meetups, from 2025-09-17 to 2026-08-19. The first was a social with no talks.
- **Result:** 4 people in the file have spoken at the chapter. A speaker listed by first name only, "Michelle" (November 2025), was skipped.

### Step 7: Location pass and LinkedIn pass

The location rules are in [`../research/README.md`](../research/README.md). In short, a location needs the person's own profile, or a recent in-person local talk plus a local office.

- **Location pass (page fetches):** 6 people placed, 4 in the region and 2 elsewhere.
  - Daria Sukhareva: a Tableau Public profile linked from kwwhat.com.
  - Archie Sarre Wood: a GitHub profile.
  - Nicole Kim and Jessie Lamontagne: in-person chapter talks in August 2026, at a Toronto-based employer.
  - Nicolas Joseph (Portland) and John Miner (Providence): their own GitHub and Sessionize profiles.
- **LinkedIn pass (search results only):** 1 person searched. The result for Josh Harris gave Toronto, but it may describe the company rather than the person. The profile link is recorded and the location stays unknown.
- **Still unknown:** 5 people.

## 2. What we learnt

- **Sources that worked:**
  - **Snowflake and Databricks user group pages:** for a mid-sized chapter, they give the best 2025 and 2026 speaker lists and organisers.
  - **Dormant meetups:** Toronto Modern Data Stack holds the city's older dbt speakers. Read it with Meetup `gql2` and re-check current roles.
  - **Meetup `gql2`:** it works from plain `curl`, and `groupSearch` lists a city's data groups in one call.
  - **`api.rss2json.com`:** it returns a Medium publication's last 10 posts with full text.
- **Sources that didn't:**
  - **Medium:** it blocks `curl` and direct fetches. rss2json rate-limits after about 10 new feeds.
  - **dev.to and GitHub location search:** job-seeker portfolios, not worth the calls.
  - **JavaScript pages:** Coalesce 2025 and Snowflake World Tour speaker lists.
  - **Web search:** the session limit stopped the extension after about 20 searches.
- **Watch out for:**
  - **Leaders, not practitioners:** the Databricks World Tour and AI summit agendas give senior bank and insurer leaders. They suit panels better than technical talks, and most sit in tier 3.
  - **Old posts:** the Loblaw Digital posts are from 2023, and the authors' titles were not stated. Check current roles.
  - **Off-topic posts:** a first-time speaker (an "emerging voice") is someone who publishes about dbt but has no talk on record. Samara Xiang reached tier 1 by the rule, but the post is about machine learning experiments, not dbt.
  - **People in two cities:** Célia Bru, Gabriel Gambacorta and Ian Whitestone also appear in the Montreal file.
  - **Vendor speakers:** Snowflake, Astronomer, FiveOneFour, Evidence and Artemis staff fill several slots. dbt Labs staff are labelled in the cockpit. Muneeb Master works there and can speak, but check the line-up has practitioners first.

## 3. Key leads

A tier is a priority level. Tier 1 means a person in the region (or not known to be elsewhere) with a dbt item from 2024 onwards, or a first-time speaker with a post from 2024 onwards. Toronto has only 4 tier-1 people.

- **First-time speakers:**
  - **Joseph Jing (Loblaw Digital):** lead author of ["Leveraging LLMs to generate AI driven dbt documentation"](https://medium.com/loblaw-digital/leveraging-llms-to-generate-ai-driven-dbt-documentation-c4735faa6ca5) (2023-11).
  - **Indrani Gorti (Loblaw Digital):** co-wrote the dbt documentation post and the [Data as a Service series](https://medium.com/loblaw-digital/part-2-data-as-a-service-simplifying-real-time-data-ingestion-and-delivery-ef7cb22e144d).
  - **Colin Barber (Loblaw Digital):** lead author of the [Data as a Service series](https://medium.com/loblaw-digital/part-2-data-as-a-service-simplifying-real-time-data-ingestion-and-delivery-ef7cb22e144d), on real-time BigQuery pipelines (2023-09).
  - **Lindsay Murphy (Secoda):** wrote ["Implementing Data Contracts with dbt and across the MDS"](https://www.secoda.co/blog/implementing-data-contracts-with-dbt). Also a connector: co-ran Toronto Modern Data Stack in 2022 and 2023.
- **Anchor speakers:**
  - **Célia Bru and Gabriel Gambacorta (KOHO Financial):** ["Before the agents: what self-serve analytics actually needs"](https://www.getdbt.com/dbt-summit/speakers/celia-bru), dbt Summit 2026.
  - **Ian Whitestone (SELECT):** ["Proven methods for optimizing your dbt project"](https://c.select.dev/blog/proven-methods-for-optimizing-your-dbt-project-dbt-coalesce-2023), Coalesce 2023. Attended the Snowflake Toronto User Group in person in July 2026.
  - **Xiao Ma and Wenyang Liu (Geotab):** [data platform talks](https://www.meetup.com/toronto-kafka/events/316272838/) at the Toronto Kafka meetup, September 2026.
  - **Alvira Narshidani (Scotia Global Asset Management):** led a [BI and AI storytelling table](https://www.meetup.com/snowflake-usergroup-toronto/events/315505233/) at the Snowflake Toronto User Group, July 2026. One of few non-vendor practitioners on recent agendas.
- **Connectors:** community organisers who can introduce people.
  - **Eddy Zulkifly:** [Toronto dbt Meetup](https://www.meetup.com/toronto-dbt-meetup/) organiser.
  - **Augusto Rosa (Archetype Consulting) and Ryan Ovas (Polar Labs):** organisers of the [Snowflake Toronto User Group](https://usergroups.snowflake.com/toronto/).
  - **Kevin Poulton (Databricks):** leads the [Toronto Databricks User Group](https://usergroups.databricks.com/toronto-databricks-user-group/) organiser team.
  - **Jill Cates:** organiser of [PyLadies Toronto](https://www.meetup.com/PyLadies-Toronto/).
  - **Vijayanirmala Gopal:** organiser of [AWS User Group Women in Tech Ontario](https://www.meetup.com/aws-women-in-tech-user-group-ontario/).
  - **Michael Olafusi (MHS Analytics):** organiser of [Data Engineers in Toronto](https://www.meetup.com/data-engineers-in-toronto/).

## 4. Before outreach

- [ ] **Check "in region" calls.** 62 people are marked in the region, but only 4 of those calls come from the location pass. Most came from a local event or the employer's head office during research.
- [ ] **Check unknown locations.** 5 people: Josh Harris, Josh Gray, Constance Martineau, Amanda Milberg and Jacqueline Kuo.
- [ ] **Check Gabriel Gambacorta.** No title was captured, and Toronto is assumed from KOHO's head office.
- [ ] **Check tier-1 people raised by the rule.** Samara Xiang writes about machine learning, not dbt.
- [ ] **Check current roles** for Loblaw Digital authors and Toronto Modern Data Stack speakers from 2022 and 2023.
- [ ] **Coordinate with the Montreal chapter** on Célia Bru, Gabriel Gambacorta and Ian Whitestone.
- [ ] **Check who is already booked.** Nicole Kim, Jessie Lamontagne, Josh Harris and Daria Sukhareva spoke in 2026.

## 5. Next run

- **Read the unread Medium feeds:** Ritual, Wattpad, KOHO, League, Super.com, Clio, Infostrux and the dbt tag feed. Use rss2json and space the calls out.
- **Finish LinkedIn.** 66 people are still `not_searched`. Start with tier 1 and tier 2.
- **Refresh job ads** with `site:` searches on Lever, Greenhouse and Ashby. The 70 ads date from 2026-09-24.
- **Try the pages not read yet:** Coalesce 2025 speakers (needs a browser), Snowflake World Tour Toronto 2026, Day of Data Toronto 2026 and Big Data & Analytics Summit Canada.
- **Ask the PyLadies Toronto organiser** about its April 2026 lightning-talk speakers.
- **Look harder at Waterloo.** No Waterloo group had dbt talks, so try Waterloo company blogs.

## 6. Replication prompt

````
You are extending my dataset of Toronto companies that use dbt, and people who could speak at or
attend the Toronto dbt Meetup. The file is toronto/toronto_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Region: the Greater Toronto Area, including the
Waterloo region. Read toronto/SEARCH_METHOD.md first, then research/README.md,
research/raw-format.md, research/location-task.md and research/linkedin-task.md.

Budget about 25 web searches. Try these first:
1. Medium feeds through api.rss2json.com: Ritual, Wattpad, KOHO, League, Super.com, Clio, Infostrux.
2. New events of the Snowflake Toronto and Databricks Toronto user groups, and Toronto data
   groups through Meetup gql2 groupSearch, with curl.
3. Day of Data Toronto, Big Data & Analytics Summit Canada, and dbt Summit speaker pages.
4. Job ads: site: searches on Lever, Greenhouse and Ashby for dbt Toronto.

Rules: never fetch LinkedIn pages or the LinkedIn Jobs API, use only search results. Public
professional information only; never record or guess gender; pronouns only when self-stated.
Skip past chapter speakers; the assembler adds them. Assemble with research/assemble.py --base,
run research/validate.py (must print ok), then add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build from one research run and a LinkedIn Jobs scan: 84 companies, 31 people, 70 job ads at 52 companies, 4 past meetups. Tiers: 2 tier 1, 11 tier 2, 10 tier 3, 8 connectors. Lead types: 24 proven speakers, 1 emerging voice, 6 featured. |
| 2026-10-01 | 2 | Extension run: 38 people and 19 companies added, giving 69 people and 103 companies. 7 new emerging voices, all Loblaw Digital authors. Tiers: 4 tier 1, 22 tier 2, 33 tier 3, 10 connectors. |
| 2026-10-01 | 2 | Location pass from public pages: 6 people placed, 4 in the region and 2 elsewhere. |
| 2026-10-01 | 2 | LinkedIn pass from search results: 1 person searched; the profile link was recorded but the location stays unknown. 5 people are still unknown. |
