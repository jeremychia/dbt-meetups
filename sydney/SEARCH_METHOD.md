# Sydney: city notes

This file holds what is specific to Sydney. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Sydney dbt Meetup](https://www.meetup.com/sydney-dbt-meetup/), data in `sydney_dbt_companies.json`
- **Region:** Greater Sydney. Newcastle, Adelaide and Melbourne do not count. Docklands, Victoria is part of Melbourne.
- **First built:** 2026-09-24

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
| Based in the region | 109 |
| Based elsewhere | 10 |
| Location unknown | 22 |
| With a LinkedIn profile | 54 |
| Job ads mentioning dbt | 87 |
| Past chapter meetups | 13 |
<!-- at-a-glance:end -->

## 1. Where to look in Sydney

The first build had three parts: local meetups and communities, conferences and blogs, and job ads. A build script merged them with a file of manual corrections.

### dbt Labs events and conferences

- **[Coalesce on the Road Sydney 2025](https://www.getdbt.com/events/roadshow/coalesce-in-sydney)** (2025-11-06): the richest source. Speakers and talk abstracts sit in the page's embedded JSON, not the visible HTML, with every speaker, company and title. It gave humm group, nib, Rezdy, Macquarie, Envato and OneStop speakers.
- **[dbt World Tour Sydney 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-sydney)** (2026-10-08): speaker names appear only in the page's embedded JSON. It gave Mitti, Brighte, Bankwest and Suncorp speakers.
- **[dbt Summit 2026 agenda](https://www.getdbt.com/dbt-summit/agenda):** Mitti is the only Australian company on it.
- **[DataEngBytes Sydney 2026](https://dataengbytes.com/2026/sydney):** rendered with JavaScript. The `/api/2026/sessions` and `/api/2026/users` endpoints worked in the browser. They include self-stated pronouns, which almost no other source does, and LinkedIn URLs.
- **[PyCon AU 2026](https://2026.pycon.org.au/schedule/VHXDSA/):** one AEMO talk on dbt. The full Data & AI track was not scanned.

### Local meetups

- **[Snowflake User Group Sydney](https://usergroups.snowflake.com/sydney/):** the best community source, with the most dbt talks of any local group: nib, Cochlear with Vivanti, and Scape. Its pages fetch cleanly.
- **[Sydney Databricks User Group](https://www.meetup.com/sydney-databricks-user-group/):** practitioner talks from Ausgrid, Mantel, Lendi, Zip and Synechron, with LinkedIn URLs inline.
- **[Data & Analytics Wednesday Sydney](https://www.meetup.com/data-and-analytics-wednesday-sydney/):** monthly, with many BI and analytics speakers and LinkedIn URLs inline.
- **[DataEngBytes Luma calendar](https://luma.com/dataengbytes):** the Sydney Data Eng meetups moved here. Luma's API endpoints work when called from a luma.com page. The past list only reaches back to 2026-06.
- **Smaller sources:** the [Power BI & Fabric User Group](https://www.meetup.com/microsoft-power-bi-fabric-user-group-sydney/), [Sydney AI + Data](https://www.meetup.com/data-science-sydney/) and [Sydney Python (SyPy)](https://luma.com/sydneypython).
- **Women-in-data groups:** [R-Ladies Sydney](https://www.meetup.com/rladies-sydney/), [GEEQ](https://www.meetup.com/geeq-australia/) (formerly Girl Geek Sydney), [Women in Tech Australia](https://www.meetup.com/womenintechaustralia/) and [She Loves Data](https://shelovesdata.com/events/) gave speakers or organisers. 12 people are tagged from them. The talks are mostly R, general tech or GenAI, not dbt.
- **Chapter history:** every named speaker from `../enriched/sydney-dbt-meetup.json` was added. That covers 13 events, from the inaugural meetup (2019-10-09) to the Mantel Group edition (2024-05-30). Meetup `gql2` shows 774 members, and the organiser field says "dbt Labs".

### Blogs and job ads

- **[Canva Engineering Blog](https://www.canva.dev/blog/engineering/):** the data platform tag and three articles. They gave 4 first-time speakers, but no article mentions dbt.
- **[EdgeRed](https://edgered.com.au/our-data-engineers-favourite-tools-of-2025-so-far/):** a Sydney dbt partner.
- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt&location=Sydney%2C%20New%20South%20Wales%2C%20Australia), logged out:** 250 ads listed (the cap) and 250 checked. 82 contain the whole word dbt. 16 ads named the person who posted them.
- **ATS search:** `site:jobs.lever.co`, `site:job-boards.greenhouse.io` and `site:jobs.ashbyhq.com` with dbt Sydney. They added Blinq, Tracksuit, Mixpanel and Xero.
- **Yield:** 87 job ads at 56 companies. Recruiters are recorded with type `other` and a "RECRUITER" note.

### Locations

- **In-person conference talks:** placed 4 people at medium confidence. 3 spoke at the in-person Coalesce on the Road Sydney, at employers with a confirmed Sydney office: Mantel (580 George St) and Rezdy (320 Pitt St). 1 spoke at DataEngBytes Sydney 2026, for IAG, which is headquartered in Sydney.
- **LinkedIn search results:** 12 people were searched. It placed 6 in Greater Sydney and 1 in Adelaide. One more result put Kevin Dang (EdgeRed) in Docklands, which is Melbourne.
- **Yield:** 12 people placed across both passes, and 37 still unknown. The evidence rules are in [location rules](../research/README.md#6-location-rules).

## 2. What didn't work here

- **The chapter itself:** it is dormant. The last in-person event was on 2024-05-30 at Mantel Group. After that it only cross-posted two online dbt Labs sessions in 2024, and it has had no events in 2025 or 2026. Its history is mostly 2019 to 2022.
- **[Seek](https://www.seek.com.au/dbt-jobs/in-All-Sydney-NSW):** stuck on a Cloudflare bot check.
- **DataEngBytes 2025 archive:** does not load.
- **[WiDS Sydney](https://widssydney.com.au/):** returned nothing, because the page is rendered with JavaScript.
- **Closed groups:** [Women in Big Data Sydney](https://www.meetup.com/women-in-big-data-wibd-sydney/) and PyLadies Sydney have closed or could not be found. The old [Sydney Data Engineering Meetup](https://www.meetup.com/sydney-data-engineering-meetup/) group no longer exists.
- **[Snowflake Sydney Meetup group](https://www.meetup.com/Snowflake-Sydney/):** no events since 2023.
- **[Australia Apache Airflow Meetup](https://www.meetup.com/australia-apache-airflow-meetup/):** runs only online vendor sessions.
- **EdgeRed blog index:** timed out.
- **[Mantel dbt page](https://mantelgroup.com.au/uplift-your-business-with-dbt):** redirects to the homepage.
- **Company feeds:** the [SafetyCulture](https://medium.com/feed/safetyculture), [Airwallex](https://medium.com/feed/airwallex-engineering), [Domain](https://tech.domain.com.au/feed) and [Atlassian](https://www.atlassian.com/blog/atlassian-engineering/feed) feeds had no dbt posts or came back empty.

## 3. Companies looked at

- **Mantel Group dominates:** it hosted the last two chapter events, the Databricks user group and a Snowflake user group. Plan for one speaker per company per event.
- **Melbourne and Newcastle employers:** Envato and Easygo are based in Melbourne. nib's head office is in Newcastle. Their speakers are not placed in Sydney. The exception is Brad Williams (nib), who is marked in the region with no location evidence.
- **Recruiters and talent staff:** 16 people were found through job ads. None has public content, so none is a speaker lead.

<!-- companies:start -->
163 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (40)</summary>

Advance Delivery Consulting, AEMO (local presence not confirmed), Bankwest (CBA) (local presence not confirmed), BaptistCare, Bendigo Bank, BizCover, Blinq, Brighte, Canva, CMC Markets ANZ, Cochlear, Commonwealth Bank, CoStar Group, dbt Labs (APAC), Eftsure, Envato (local presence not confirmed), Heidi, Helia, hipages Group, humm group, Immutable, Launch Group, Lyka, Macquarie Group, Mantel Group, Mitti (formerly SafetyCulture), NexVenture, nib Group, Omio, Optiver, Rezdy, Scape Australia, Snowflake User Groups Sydney, Suncorp (local presence not confirmed), Synechron, Talent Insights Group, Tracksuit, UpGuard, Viable Solutions Pty Ltd, Xero

</details>

<details><summary><b>Some dbt signal</b> (36)</summary>

Agoda, Airwallex (local presence not confirmed), BINGO INDUSTRIES, CareCone Group, Cevo Australia, Databricks, Datacom, Deloitte, Domain, EdgeRed, FR Consultancy, Hawksworth, Ingrity, Lendi Group, Mixpanel, NCS Group Australia, Nine, NOVON, OneStop (local presence not confirmed), PwC Australia, Qantas, Simple Machines, Slalom, Snowflake, Supermetrics, Sydney Local Health District, synogize, Tata Consultancy Services, tekFinder, The Iconic, Trideca, Versent, Vivanti, Vivanti Consulting, World Wide Technology, Zone IT Solutions

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

DataEngBytes

</details>

<details><summary><b>Not verified</b> (86)</summary>

Actian (local presence not confirmed), Afterpay / Block, Aginic (local presence not confirmed), Airtasker, Altis Consulting, AMP, Assembly Payments (local presence not confirmed), Atlassian, Ausgrid (local presence not confirmed), Australian Energy Market Operator (AEMO) (local presence not confirmed), Azility (local presence not confirmed), Brooklyn Data Co. (local presence not confirmed), Cevo, Contino (local presence not confirmed), Culture Amp (local presence not confirmed), DashByte Co. (local presence not confirmed), Data & Analytics Wednesday Sydney, DataEngBytes / Cloud Shuttle (local presence not confirmed), Dataro (local presence not confirmed), DAZN Foxtel Group (local presence not confirmed), dbt (Fishtown Analytics) (local presence not confirmed), Deputy, Did Someone Say Data (local presence not confirmed), Easygo (local presence not confirmed), Eliiza (local presence not confirmed), Employment Hero, Endeavour Drinks (local presence not confirmed), Excelerator BI (local presence not confirmed), ExeQution Analytics (local presence not confirmed), Finder, Fivetran (local presence not confirmed), GEEQ (formerly Girl Geek Sydney), Harrison.ai, Hypothesis (local presence not confirmed), IAG (local presence not confirmed), Innova (local presence not confirmed), InterWorks (local presence not confirmed), Judo Bank (local presence not confirmed), Kinso AI (local presence not confirmed), Linktree (local presence not confirmed), Luxury Escapes (local presence not confirmed), Mable (local presence not confirmed), Macquarie University (local presence not confirmed), Manuka (local presence not confirmed), Mathspace (local presence not confirmed), Microsoft (local presence not confirmed), Microsoft Power BI & Fabric User Group - Sydney, NAB, Nearmap (local presence not confirmed), Nine / Stan, Octopus Deploy (local presence not confirmed), Omnata (local presence not confirmed), Open Colleges (local presence not confirmed), Optiver Australia (local presence not confirmed), Organon (local presence not confirmed), Poplin Data (local presence not confirmed), Presciient (local presence not confirmed), Prospa (local presence not confirmed), QMetrix (local presence not confirmed), R-Ladies Sydney, REA Group (local presence not confirmed), Rheem Australia (local presence not confirmed), Rokt, RoundRect (local presence not confirmed), SafetyCulture (local presence not confirmed), Seek (local presence not confirmed), Servian (Cognizant), She Loves Data (local presence not confirmed), Shippit (local presence not confirmed), Snowplow (local presence not confirmed), Sonder (local presence not confirmed), Sydney Databricks User Group, Syenchron Australia (local presence not confirmed), Telstra, Temple & Webster, The New Zealand Institute for Plant and Food Research (local presence not confirmed), Trustpower (local presence not confirmed), Tyro, Vendo (local presence not confirmed), Versix (local presence not confirmed), Westpac, Women in Tech Australia, Woolworths / Quantium, XPON Technologies Group (local presence not confirmed), Zip Co, Zip Money (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (14)</summary>

- https://dataengbytes.com/
- https://dataengbytes.com/2026
- https://dataengbytes.com/2026/sydney
- https://edgered.com.au/our-data-engineers-favourite-tools-of-2025-so-far/
- https://mantelgroup.com.au/
- https://mantelgroup.com.au/case-studies/humm-group/
- https://mantelgroup.com.au/uplift-your-business-with-dbt
- https://medium.com/feed/airwallex-engineering
- https://medium.com/feed/safetyculture
- https://tech.domain.com.au/feed
- https://usergroups.snowflake.com/sydney/
- https://www.atlassian.com/blog/atlassian-engineering/feed
- https://www.canva.dev/blog/engineering/
- https://www.canva.dev/blog/engineering/tag/data-platform/

</details>

<details><summary><b>Other sources checked</b> (45)</summary>

- [Sydney dbt Meetup (meetup.com gql2)](https://www.meetup.com/sydney-dbt-meetup/)
- [Snowflake User Groups Sydney (Bevy)](https://usergroups.snowflake.com/sydney/)
- [Sydney Databricks User Group](https://www.meetup.com/sydney-databricks-user-group/)
- [Data & Analytics Wednesday Sydney](https://www.meetup.com/data-and-analytics-wednesday-sydney/)
- [Microsoft Power BI & Fabric User Group - Sydney](https://www.meetup.com/microsoft-power-bi-fabric-user-group-sydney/)
- [Sydney AI + Data (formerly Data Science Sydney)](https://www.meetup.com/data-science-sydney/)
- [DataEngBytes Luma calendar](https://luma.com/dataengbytes)
- [DataEngBytes website](https://dataengbytes.com/sydney) (nothing useful)
- [Sydney Data Engineering Meetup (meetup.com)](https://www.meetup.com/sydney-data-engineering-meetup/) (nothing useful)
- [Sydney Python (SyPy) Luma](https://luma.com/sydneypython)
- [R-Ladies Sydney](https://www.meetup.com/rladies-sydney/)
- [GEEQ (formerly Girl Geek Sydney)](https://www.meetup.com/geeq-australia/)
- [Women in Tech Australia](https://www.meetup.com/womenintechaustralia/)
- [She Loves Data (site + Eventbrite)](https://shelovesdata.com/events/)
- [WiDS Sydney](https://widssydney.com.au/) (nothing useful)
- [Women in Big Data Sydney (meetup)](https://www.meetup.com/women-in-big-data-wibd-sydney/) (nothing useful)
- [PyData Sydney / PyLadies Sydney](https://www.meetup.com/pydata-sydney/) (nothing useful)
- [Sydney Snowflake Meetup Group (meetup.com)](https://www.meetup.com/Snowflake-Sydney/) (nothing useful)
- [Australia Apache Airflow Meetup](https://www.meetup.com/australia-apache-airflow-meetup/) (nothing useful)
- [Sydney Tableau User Group](https://usergroups.tableau.com/) (nothing useful)
- [Coalesce on the Road Sydney agenda](https://www.getdbt.com/events/roadshow/coalesce-in-sydney-agenda) (nothing useful)
- [Analytics.Club Sydney, The Data People, Data Driven Sydney, Data Council Sydney](https://www.meetup.com/ac-syd/) (nothing useful)
- [dbt World Tour Sydney 2026 agenda](https://www.getdbt.com/events/roadshow/dbt-world-tour-sydney)
- [Coalesce on the Road Sydney 2025](https://www.getdbt.com/events/roadshow/coalesce-in-sydney)
- [dbt World Tour Melbourne 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-melbourne) (nothing useful)
- [dbt Summit 2026 agenda](https://www.getdbt.com/dbt-summit/agenda)
- [DataEngBytes 2026 Sydney](https://dataengbytes.com/2026/sydney)
- [DataEngBytes 2025 Sydney archive](https://dataengbytes.com/2025/sydney) (nothing useful)
- [Canva Engineering Blog](https://www.canva.dev/blog/engineering/)
- [Snowflake User Group Sydney](https://usergroups.snowflake.com/sydney/)
- [Snowflake World Tour Sydney 2025 recap (Alex Hruska)](https://alexhruska.medium.com/snowflake-world-tour-sydney-2025-retro-2859dac35e53)
- [PyCon AU 2026 session](https://2026.pycon.org.au/schedule/VHXDSA/)
- [EdgeRed blog](https://edgered.com.au/our-data-engineers-favourite-tools-of-2025-so-far/)
- [Mantel dbt page](https://mantelgroup.com.au/uplift-your-business-with-dbt) (nothing useful)
- [SafetyCulture Medium feed](https://medium.com/feed/safetyculture) (nothing useful)
- [Airwallex Engineering Medium feed](https://medium.com/feed/airwallex-engineering) (nothing useful)
- [Domain tech blog feed](https://tech.domain.com.au/feed) (nothing useful)
- [Atlassian engineering blog feed](https://www.atlassian.com/blog/atlassian-engineering/feed) (nothing useful)
- [Sydney Data Engineering Meetup](https://www.meetup.com/sydney-data-engineering-meetup/events/?type=past) (nothing useful)
- [LinkedIn Jobs guest API (keywords=dbt, Sydney NSW)](https://www.linkedin.com/jobs/search?keywords=dbt&location=Sydney%2C%20New%20South%20Wales%2C%20Australia)
- [Seek (dbt jobs in All Sydney NSW)](https://www.seek.com.au/dbt-jobs/in-All-Sydney-NSW) (nothing useful)
- [WebSearch site:jobs.lever.co dbt Sydney](https://jobs.lever.co)
- [WebSearch site:job-boards.greenhouse.io dbt Sydney](https://job-boards.greenhouse.io)
- [WebSearch site:jobs.ashbyhq.com dbt Sydney](https://jobs.ashbyhq.com)
- [WebSearch smartrecruiters/workday dbt Sydney](https://jobs.smartrecruiters.com) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:** the pool is thin, and none of these posts mentions dbt.
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
- **Connectors:**
  - **Margie Iliescu (Mantel Group):** organised the [last two chapter events](https://www.meetup.com/sydney-dbt-meetup/events/300649055/). The first contact for a restart and a venue.
  - **Peter Hanssens:** founded DataEngBytes and hosts the [monthly Sydney Data Eng meetup](https://luma.com/dataen-fjyv). Spoke at the inaugural chapter event in 2019.
  - **Phillip Lim and Shirley Gao (Snowflake):** organise the [Snowflake User Group Sydney](https://usergroups.snowflake.com/sydney/), a natural co-host.
  - **Renee Noble:** co-organises [SyPy](https://luma.com/sydneypython), which runs [talk-writing workshops](https://luma.com/5plwd5oh) that could help new speakers.
  - **Susan Luo:** co-organises [R-Ladies Sydney](https://www.meetup.com/rladies-sydney/).

## 5. Before outreach

- [ ] **Check most "in region" calls:** only 10 of the people marked in Greater Sydney have a location note with evidence. The rest were placed from the employer or event during the first build.
- [ ] **Check people already booked:** Mitti (Zarmina Muhammad and Filip Milanovic), Brighte, Bankwest and Suncorp speak at dbt World Tour Sydney on 2026-10-08.
- [ ] **Check Canva leads:** Jun Ye and Jack Caperon have both left Canva.
- [ ] **Merge duplicate companies:** examples are Mitti and SafetyCulture, CBA, Commonwealth Bank and Commonwealth Bank of Australia, Vivanti and Vivanti Consulting, and Zip Co and Zip Money.
- [ ] **Balance dbt Labs and Fivetran staff:** Shabbir Khanbhai works at dbt Labs. Kelly Hotta's record sits under "dbt (Fishtown Analytics)", which counts as dbt Labs. Dominic Colyer works at Fivetran, so is labelled too. All three can speak, but check the line-up has practitioners first.
- [ ] **Use pronouns only where recorded:** 5 people stated pronouns on DataEngBytes. Everyone else has none.

## 6. Next run

- **Sources to try first:**
  - **After 2026-10-08:** add the dbt World Tour Sydney recordings and any new speakers, from the embedded speaker JSON on getdbt.com roadshow pages.
  - **Local groups:** new Snowflake User Group Sydney, Sydney Databricks User Group and Data & Analytics Wednesday events, and the DataEngBytes Luma calendar.
  - **Job ads:** the Lever, Greenhouse and Ashby `site:` searches for dbt Sydney.
  - **Sources not yet read:** the PyCon AU 2026 Data & AI track, the DataEngBytes 2025 archive, the EdgeRed blog index and Seek through the browser.
  - **Women-in-data:** find the GEEQ 2023 "Diversity in data engineering" panel names, and read She Loves Data's Eventbrite events in the browser.
  - **Restarting the chapter:** ask Margie Iliescu, Peter Hanssens and the Snowflake organisers about co-hosting.
- **People to locate:**
  - **Past speakers:** 37 people are still unknown, mostly chapter speakers from 2019 to 2022.
  - **No usable LinkedIn result:** Sangzhuoyang Yu, Pip Sidaway, Lavanya Kommuri and Mike Robins. Arunkumar Kamalakarapandian's result says only "Australia".
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `sydney/sydney_dbt_companies.json`, the Sydney dbt Meetup, `../enriched/sydney-dbt-meetup.json` and Greater Sydney. Add: "Count Docklands as Melbourne and Newcastle as outside the region."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build, in three parts: local meetups and communities, conferences and blogs, and job ads, plus chapter history. 141 people at 166 companies, 28 of them past chapter speakers. 87 dbt job ads at 56 companies. |
| 2026-10-01 | 2 | Location pass from public pages: in-person talks at Coalesce on the Road Sydney and DataEngBytes, at employers with a Sydney office. 4 people placed. |
| 2026-10-01 | 2 | LinkedIn pass from search results: 8 people placed, 6 in Greater Sydney and 2 elsewhere. With the location pass, 12 people placed and 37 still unknown. |
