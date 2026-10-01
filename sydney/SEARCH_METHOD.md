# Sydney dbt search: method, lessons and replication prompt

This file goes with `sydney_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in Greater Sydney who could **speak at** (or attend) the [Sydney dbt Meetup](https://www.meetup.com/sydney-dbt-meetup/), and the local companies that use dbt.
- **Region:** Greater Sydney. Newcastle, Adelaide and Melbourne do not count. Docklands, Victoria is part of Melbourne.

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 164 |
| People | 141 |
| Tier 1 leads | 16 |
| First-time speakers (publish, no talk yet) | 6 |
| Proven speakers | 105 |
| Spoke at this chapter before | 28 |
| Based in the region | 102 |
| Based elsewhere | 2 |
| Location unknown | 37 |
| With a LinkedIn profile | 39 |
| Job ads mentioning dbt | 87 |
| Past chapter meetups | 13 |
<!-- at-a-glance:end -->

## 1. How the search was done

The first build had three parts: local meetups and communities, conferences and blogs, and job ads. A build script merged them with a file of manual corrections.

The chapter is dormant. Its last in-person event was on 2024-05-30 at Mantel Group. After that it only cross-posted two online dbt Labs sessions in 2024, and it has had no events in 2025 or 2026.

### Step 1: dbt Labs events and other conferences

- **[Coalesce on the Road Sydney 2025](https://www.getdbt.com/events/roadshow/coalesce-in-sydney)** (2025-11-06): the richest source. Speakers and talk abstracts sit in the page's embedded data, not the visible HTML. It gave humm group, nib, Rezdy, Macquarie, Envato and OneStop speakers.
- **[dbt World Tour Sydney 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-sydney)** (2026-10-08): speaker names appear only in the page's embedded JSON. It gave Mitti, Brighte, Bankwest and Suncorp speakers.
- **[dbt Summit 2026 agenda](https://www.getdbt.com/dbt-summit/agenda):** Mitti is the only Australian company on it.
- **[DataEngBytes Sydney 2026](https://dataengbytes.com/2026/sydney):** rendered with JavaScript. The `/api/2026/sessions` and `/api/2026/users` endpoints worked in the browser. They include self-stated pronouns and LinkedIn URLs. The 2025 archive does not load.
- **[PyCon AU 2026](https://2026.pycon.org.au/schedule/VHXDSA/):** one AEMO talk on dbt. The full Data & AI track was not scanned.

### Step 2: Other local meetups

- **[Snowflake User Group Sydney](https://usergroups.snowflake.com/sydney/):** the best community source, with 3 explicit dbt talks (nib, Cochlear with Vivanti, and Scape). Its pages fetch cleanly.
- **[Sydney Databricks User Group](https://www.meetup.com/sydney-databricks-user-group/):** practitioner talks from Ausgrid, Mantel, Lendi, Zip and Synechron, with LinkedIn URLs inline.
- **[Data & Analytics Wednesday Sydney](https://www.meetup.com/data-and-analytics-wednesday-sydney/):** monthly, with many BI and analytics speakers and LinkedIn URLs inline.
- **[DataEngBytes Luma calendar](https://luma.com/dataengbytes):** the Sydney Data Eng meetups moved here. Luma's API endpoints work when called from a luma.com page. The past list only reaches back to 2026-06.
- **Smaller sources:** the [Power BI & Fabric User Group](https://www.meetup.com/microsoft-power-bi-fabric-user-group-sydney/), [Sydney AI + Data](https://www.meetup.com/data-science-sydney/) and [Sydney Python (SyPy)](https://luma.com/sydneypython).
- **Empty or gone:** the old [Sydney Data Engineering Meetup](https://www.meetup.com/sydney-data-engineering-meetup/) group no longer exists. The [Snowflake Sydney Meetup group](https://www.meetup.com/Snowflake-Sydney/) has had no events since 2023. The [Australia Apache Airflow Meetup](https://www.meetup.com/australia-apache-airflow-meetup/) runs only online vendor sessions.

### Step 3: Company and consultancy blogs

- **[Canva Engineering Blog](https://www.canva.dev/blog/engineering/):** the data platform tag and three articles. They gave 4 first-time speakers, but no article mentions dbt.
- **[EdgeRed](https://edgered.com.au/our-data-engineers-favourite-tools-of-2025-so-far/):** a Sydney dbt partner. The blog index timed out.
- **Empty:** the [Mantel dbt page](https://mantelgroup.com.au/uplift-your-business-with-dbt) redirects to the homepage. The [SafetyCulture](https://medium.com/feed/safetyculture), [Airwallex](https://medium.com/feed/airwallex-engineering), [Domain](https://tech.domain.com.au/feed) and [Atlassian](https://www.atlassian.com/blog/atlassian-engineering/feed) feeds had no dbt posts or came back empty.

### Step 4: Job ads

- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt&location=Sydney%2C%20New%20South%20Wales%2C%20Australia), logged out:** 250 ads listed (the cap) and 250 checked. 82 contain the whole word dbt. 16 ads named the person who posted them.
- **ATS search:** `site:jobs.lever.co`, `site:job-boards.greenhouse.io` and `site:jobs.ashbyhq.com` with dbt Sydney. They added Blinq, Tracksuit, Mixpanel and Xero.
- **[Seek](https://www.seek.com.au/dbt-jobs/in-All-Sydney-NSW):** stuck on a Cloudflare bot check.
- **Yield:** 87 job ads at 56 companies. Recruiters are recorded with type `other` and a "RECRUITER" note.

### Step 5: Women-in-data communities

This step looks for speakers through women-focused groups' own events. It never labels or guesses anyone's gender.

- **Sources with speakers or organisers:** [R-Ladies Sydney](https://www.meetup.com/rladies-sydney/), [GEEQ](https://www.meetup.com/geeq-australia/) (formerly Girl Geek Sydney), [Women in Tech Australia](https://www.meetup.com/womenintechaustralia/) and [She Loves Data](https://shelovesdata.com/events/). 12 people are tagged from them.
- **Weak fit:** their talks are mostly R, general tech or GenAI, not dbt.
- **Empty:** [WiDS Sydney](https://widssydney.com.au/) returned nothing. [Women in Big Data Sydney](https://www.meetup.com/women-in-big-data-wibd-sydney/) and PyLadies Sydney have closed or could not be found.

### Step 6: Chapter history

- **Past speakers:** every named speaker from `../enriched/sydney-dbt-meetup.json` was added. That covers 13 events, from the inaugural meetup (2019-10-09) to the Mantel Group edition (2024-05-30).
- **Read through Meetup `gql2`:** the group has 774 members, and its organiser field says "dbt Labs".

### Step 7: Location pass and LinkedIn pass

- **Location pass:** people were placed from public pages, by the evidence rules in [`../research/README.md`](../research/README.md). It placed 4 people at medium confidence.
  - 3 spoke at the in-person Coalesce on the Road Sydney, at employers with a confirmed Sydney office: Mantel (580 George St) and Rezdy (320 Pitt St).
  - 1 spoke at DataEngBytes Sydney 2026, for IAG, which is headquartered in Sydney.
- **LinkedIn pass:** search results only, never a LinkedIn page. 12 people were searched. It placed 6 in Greater Sydney and 1 in Adelaide. One more result put Kevin Dang (EdgeRed) in Docklands, which is Melbourne.
- **Yield:** 12 people placed across both passes, and 37 still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **getdbt.com roadshow pages.** Their embedded JSON names every speaker, company and title.
  - **The Snowflake User Group Sydney.** It has the most dbt talks of any local group.
  - **Meetup pages with inline LinkedIn URLs.** The Databricks User Group and Data & Analytics Wednesday gave many profiles without a search.
  - **The DataEngBytes API.** It gave self-stated pronouns, which almost no other source does.
- **Sources that didn't:**
  - **Seek** blocks fetches with a bot check.
  - **JavaScript-rendered pages:** the DataEngBytes archive and WiDS Sydney.
  - **The chapter itself.** It has had no events since 2024-05-30, so its history is mostly 2019 to 2022.
- **Watch out for:**
  - **Mantel Group dominates.** It hosted the last two chapter events, the Databricks user group and a Snowflake user group. Plan for one speaker per company per event.
  - **Melbourne and Newcastle employers.** Envato and Easygo are based in Melbourne. nib's head office is in Newcastle. Their speakers are not placed in Sydney. The exception is Brad Williams (nib), who is marked in the region with no location evidence.
  - **Canva staff move on.** Jun Ye and Jack Caperon have both left Canva.
  - **Job-ad posters.** 16 people are recruiters or talent staff found through job ads. They have no public content and are not speaker leads.

## 3. Key leads

- **First-time speakers** (people who publish but have no talk on record): the pool is thin, and none of these posts mentions dbt.
  - **Jack Caperon:** wrote [the foundations of Canva's continuous data platform](https://www.canva.dev/blog/engineering/snowpipe-streaming/), on Snowpipe Streaming.
  - **Jun Ye:** wrote [measuring commercial impact at scale at Canva](https://www.canva.dev/blog/engineering/measuring-commerical-impact-at-scale/).
  - **Sangzhuoyang Yu (Canva):** wrote [scaling to count billions](https://www.canva.dev/blog/engineering/scaling-to-count-billions/). The location is unknown.
- **New to the chapter, with dbt talks elsewhere:**
  - **Suvarna Yenugudhati (Scape):** [a metadata-driven ingestion framework with dbt incremental models](https://usergroups.snowflake.com/events/details/snowflake-sydney-presents-sydney-technical-user-group-2/), covering 400+ API objects.
  - **Brad Williams (nib):** [semantic models as code](https://usergroups.snowflake.com/events/details/snowflake-sydney-presents-build-meetup/), with tooling built into dbt.
  - **Yuan Li (Vivanti):** co-presented [Cochlear's dbt data products](https://usergroups.snowflake.com/events/details/snowflake-sydney-presents-build-meetup/). Ask for a practitioner talk, not a pitch.
- **Anchor speakers:**
  - **Thiago Baldim (Mitti):** co-presented [Mitti's dbt rebuild](https://www.getdbt.com/dbt-summit/agenda/from-14-hour-batches-and-poor-documentation-to-ai-ready-data-mittis-dbt-rebuild) at dbt Summit 2026.
  - **Michael Fridolfsson (Brighte):** spoke at the [last chapter event](https://www.meetup.com/sydney-dbt-meetup/events/300649055/), and speaks at dbt World Tour Sydney 2026 on five years of Brighte's dbt platform.
  - **Sabarish Palanisamy (Rezdy):** presented [Rezdy's analytics with Fivetran and dbt](https://www.getdbt.com/events/roadshow/coalesce-in-sydney) at Coalesce Sydney 2025.
  - **Tom Leggett (Macquarie):** the featured customer at [Coalesce Sydney 2025](https://www.getdbt.com/events/roadshow/coalesce-in-sydney). A keynote or panel slot fits better than a deep dive.
- **Connectors** (people who can introduce others):
  - **Margie Iliescu (Mantel Group):** organised the [last two chapter events](https://www.meetup.com/sydney-dbt-meetup/events/300649055/). The first contact for a restart and a venue.
  - **Peter Hanssens:** founded DataEngBytes and hosts the [monthly Sydney Data Eng meetup](https://luma.com/dataen-fjyv). Spoke at the inaugural chapter event in 2019.
  - **Phillip Lim and Shirley Gao (Snowflake):** organise the [Snowflake User Group Sydney](https://usergroups.snowflake.com/sydney/), a natural co-host.
  - **Renee Noble:** co-organises [SyPy](https://luma.com/sydneypython), which runs [talk-writing workshops](https://luma.com/5plwd5oh) that could help new speakers.
  - **Susan Luo:** co-organises [R-Ladies Sydney](https://www.meetup.com/rladies-sydney/).

## 4. Before outreach

- **Check most "in region" calls.** Only 10 of the people marked in Greater Sydney have a location note with evidence. The rest were placed from their employer or event during the first build.
- **Check people already booked.** Mitti (Zarmina Muhammad and Filip Milanovic), Brighte, Bankwest and Suncorp speak at dbt World Tour Sydney on 2026-10-08.
- **Merge duplicate companies.** Examples are Mitti and SafetyCulture, CBA, Commonwealth Bank and Commonwealth Bank of Australia, Vivanti and Vivanti Consulting, and Zip Co and Zip Money.
- **Skip dbt Labs staff.** Shabbir Khanbhai is excluded from outreach. Kelly Hotta's record sits under "dbt (Fishtown Analytics)" and is not excluded yet.
- **Use pronouns only where recorded.** 5 people stated their pronouns on DataEngBytes. Everyone else has none.

## 5. Next run

- **After 2026-10-08:** add the dbt World Tour Sydney recordings and any new speakers.
- **People still without a location:** 37, mostly chapter speakers from 2019 to 2022. LinkedIn found nothing usable for Sangzhuoyang Yu, Pip Sidaway, Lavanya Kommuri and Mike Robins. Arunkumar Kamalakarapandian's result says only "Australia".
- **Sources not yet read:** the PyCon AU 2026 Data & AI track, the DataEngBytes 2025 archive, the EdgeRed blog index and Seek through the browser.
- **Women-in-data:** find the GEEQ 2023 "Diversity in data engineering" panel names, and read She Loves Data's Eventbrite events in the browser.
- **Restarting the chapter:** ask Margie Iliescu, Peter Hanssens and the Snowflake organisers about co-hosting.

## 6. Replication prompt

````
You are extending my dataset of Greater Sydney companies that use dbt, and people who could
speak at or attend the Sydney dbt Meetup. The file is sydney/sydney_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read sydney/SEARCH_METHOD.md first, then
research/README.md, research/raw-format.md, research/location-task.md and
research/linkedin-task.md. Keep the shared schema (berlin_planning/SEARCH_METHOD.md §3).

Try first: the dbt World Tour Sydney 2026 recordings and the embedded speaker JSON on
getdbt.com roadshow pages; new Snowflake User Group Sydney, Sydney Databricks User Group and
Data & Analytics Wednesday events; the DataEngBytes Luma calendar; and job ads through Lever,
Greenhouse and Ashby site: searches for dbt Sydney. Count Docklands as Melbourne and Newcastle
as outside the region.

Rules: never fetch LinkedIn pages, only use search results; public professional information
only; never guess gender, and record pronouns only when self-stated. Assemble with
research/assemble.py --base, place people with research/apply_locations.py, then run
research/validate.py and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build, in three parts: local meetups and communities, conferences and blogs, and job ads, plus chapter history. 141 people at 166 companies, 28 of them past chapter speakers. 87 dbt job ads at 56 companies. |
| 2026-10-01 | 2 | Location pass from public pages: in-person talks at Coalesce on the Road Sydney and DataEngBytes, at employers with a Sydney office. 4 people placed. |
| 2026-10-01 | 2 | LinkedIn pass from search results: 8 people placed, 6 in Greater Sydney and 2 elsewhere. With the location pass, 12 people placed and 37 still unknown. |
