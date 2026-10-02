# Montreal: city notes

This file holds what is specific to Montreal. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Montreal dbt Meetup](https://www.meetup.com/montreal-dbt-meetup/), data in `montreal_dbt_companies.json`
- **Region:** Greater Montreal.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 4, 2026-10-01)

| | Count |
|---|---|
| Companies | 61 |
| People | 73 |
| Tier 1 leads | 12 |
| First-time speakers (publish, no talk yet) | 11 |
| Proven speakers | 53 |
| Spoke at this chapter before | 15 |
| Based in the region | 56 |
| Based elsewhere | 1 |
| Location unknown | 16 |
| With a LinkedIn profile | 39 |
| Job ads mentioning dbt | 43 |
| Past chapter meetups | 6 |
<!-- at-a-glance:end -->

## 1. Where to look in Montreal

Two research runs built the file. The first build (2026-09-24) used about 18 web searches and a job ad scan. The extension (2026-10-01) looked for more speakers, especially first-time speakers. It used about 17 web searches before the session limit, then direct page fetches. Leads are scored by the [central scoring rules](../research/README.md#3-scoring-rules).

Much of the local content is in French. French posts and talks are recorded as they are, with an English description.

### Meetups and user groups

- **[Snowflake Montreal User Group](https://usergroups.snowflake.com/montreal/):** the richest local source, and the best source of local proven speakers. It is a better speaker source than the dbt chapter, which was dormant for long periods. Its agendas are bilingual.
  - **First build:** the June 2025, January 2026, April 2026 and June 2026 agendas.
  - **Extension:** older event pages from July 2023 to April 2025 gave 17 new speakers. Pages follow the slug pattern `snowflake-montreal-presents-<season>-<year>`, for example [winter 2024](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-hiver-winter-2024).
  - **[Fall 2026](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-automne-fall-2026/):** talks by Oliver Benning, Lamia Goeffon and João Vitor de Camargo.
- **Chapter history:** every named speaker in [`../enriched/montreal-dbt-meetup.json`](../enriched/montreal-dbt-meetup.json) was added as a person. That file holds 6 meetups, from 2021-10-29 to 2026-08-06. 15 people in the file have spoken at the chapter. Montreal Analytics ran the 2021 to 2023 events. Solution BI hosted October 2024. Maxa and Solution BI ran the August 2026 relaunch, a networking evening with no talks.
- **Meetup `gql2` with `curl`:** works with no browser. Query by group name so results do not depend on a shared browser tab. It read [MTL Data](https://www.meetup.com/mtldata/), [Data Driven Montréal](https://www.meetup.com/datadrivenmontreal/), [Montréal-Python](https://www.meetup.com/montreal-python/), [GDG Montreal](https://www.meetup.com/gdg-montreal/) and [GDG Cloud Montreal](https://www.meetup.com/gdg-cloud-montreal/). GDG Montreal gave Jihoo Park (Warner Bros. Games Montréal) and its organisers. GDG Cloud Montreal gave its organiser.

### Company and consultancy blogs

- **[Maxa blog](https://maxa.ai/blog):** named authors writing on dbt, semantic layers and AI agents. The listing hides bylines, but each post's JSON-LD author field names the writer. Maxa hosted the chapter's 2026 relaunch.
- **[agileDSS blog](https://agiledss.com/blogue):** a Quebec BI consultancy that publishes in French. Six authors, each post with the author's title, and one post that mentions dbt.
- **[dbt developer blog authors](https://docs.getdbt.com/blog/authors):** Callie White and Jade Milaney of Montreal Analytics, from 2023.
- **[Potloc on dev.to](https://dev.to/potloc):** a 2023 post on dbt and Elementary.
- **[Infostrux events](https://www.infostrux.com/events):** Montreal labs and a dbt talk by Nasko Grozdanov.

### Women-in-data communities

Speakers come from women-focused groups' own events. Nobody's gender is recorded or guessed. 16 people are tagged `women_in_data_community`.

- **Women on Snowflake (June 2024):** a [Snowflake Montreal User Group edition](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-montreal-user-group-meeting) with an all-women speaker line-up. It gave four speakers.
- **[PyLadies Montréal](https://www.meetup.com/pyladiesmtl/):** two named speakers in March 2026. The talk topics are not listed.
- **Women Techmakers Montreal:** runs through [GDG Montreal](https://www.meetup.com/gdg-montreal/). It gave organisers and ambassadors. The GDG events API (`event_slim/for_chapter/954`) lists IWD events for 2023 to 2025. The [IWD 2025 page](https://gdg.community.dev/e/mctsvr/) names 12 organisers but no speakers. Raphaëlle Giraud (Vooban, data engineering lead) and Mimoh Solanki are recorded as connectors.
- **[R-Ladies Montreal](https://www.meetup.com/rladies-montreal/):** relaunched in June 2025. Its 3 organisers are recorded as connectors. The 2024 sessions were introductions to R and Python at McGill, with no named speakers.
- **[Women In The Loop](https://www.meetup.com/meetup-women-in-the-loop/):** a new study group (2026) that runs system design sessions. One session covered retrieval pipelines for AI. The organiser is recorded as a connector.
- **[WiDS Montreal](https://www.widsworldwide.org/events/event/wids-montreal/):** the 2024 edition names an ambassador only.

### Job ads and locations

- **LinkedIn Jobs (first build):** a logged-out scan for "dbt" in the Montreal area. Up to 150 ads were checked for the whole word "dbt". 40 ads at 18 companies mention it. Many ads are in French.
- **Company job boards (open JSON):** the Greenhouse, Lever and Ashby APIs return every open ad with its full text. About 35 Montreal employers were tried. An AlayaCare Staff Data Developer ad in Montreal requires strong dbt skills, which raised it to strong. Cohere lists dbt as a plus for a role open in Montreal. Super.com ads say the data team are long-time dbt users, but they name Canada, not Montreal.
- **Meetup venues:** Sid Lee hosts every [Snowflake Montreal User Group](https://www.meetup.com/snowflake-montreal-user-group/) meetup. Zinnia hosted [MTL Data](https://www.meetup.com/mtldata/) in April 2024.
- **Location pass (page fetches):** no one qualified under the [central location rules](../research/README.md#6-location-rules). Most chapter talks were from 2021 to 2023, too old for in-person evidence. The bios on event pages state no city. Audrey Leduc spoke in person in October 2024, but KOHO's Montreal office could not be confirmed.
- **LinkedIn pass (search results only):** 12 people searched and 3 placed. [Hassan Al-Rabea](https://www.linkedin.com/in/hassan-al-rabea/) and [Audrey Leduc](https://www.linkedin.com/in/audreyleduc/) are in Montreal. [Kristi Gourlay](https://www.linkedin.com/in/kristi-gourlay/) is in Toronto. Results that gave only "Canada" or "United States", or did not tie the profile to the recorded employer, were skipped.

## 2. What didn't work here

- **Medium feeds:** [SSENSE](https://medium.com/feed/ssense-tech), Hopper, Lightspeed, Dialogue, Transit and Workleap returned HTTP 429 (too many requests), to both `curl` and direct fetches.
- **[Infostrux blog](https://www.infostrux.com/blog) and [Datatonic insights](https://www.datatonic.com/insights/):** no bylines. The Montreal Analytics blog now redirects to Datatonic.
- **[dev.to's dbt tag](https://dev.to/t/dbt):** 112 authors, none in Montreal or Quebec.
- **GitHub user search:** rate-limited.
- **General Montreal data meetups:** MTL Data, Data Driven Montréal and Montréal-Python had no dbt talks since 2023.
- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** no Montreal employers. KOHO speakers are the nearest match.
- **[Montreal Databricks User Group](https://usergroups.databricks.com/montreal-databricks-user-group/):** ran AI vendor demos in March 2026.
- **[HEC Forecast](https://www.csdhec.ca/hec-forecast):** lists no speakers.
- **[ConFoo](https://confoo.ca/en/yul2026/sessions):** returned HTTP 500.
- **[Data Developer Meetup MTL](https://luma.com/7yr2a677):** the page lists no panellists.
- **[Montreal AI & Data Engineering meetup](https://www.meetup.com/montreal-data-engineering/):** off topic.
- **[Montreal Women in ML & DS meetup](https://www.meetup.com/montreal-women-in-machine-learning-and-data-science/):** no events since June 2024.
- **[R-Ladies Montreal](https://www.meetup.com/rladies-montreal/):** rebooting with intro sessions. No talk has a named speaker.
- **More women-in-tech groups with no data talks:** [Montréal Women in Agile](https://www.meetup.com/WiA-Montreal/) runs agile and leadership talks. [QueerTech Montreal](https://www.meetup.com/queertech-montreal/) runs career events. PyLadies Montréal has held no new talks since March 2026.
- **French searches:** Meetup's group search for "femmes", "femmes en tech" and "elles" returns social groups only.
- **Data + Women:** no Montreal Tableau user group or Data + Women page was found. Both guessed pages return 404.
- **Web search:** the session limit stopped the extension after about 17 searches, and most results were job ads.
- **[HN Who is hiring](https://hn.algolia.com/api/v1/search?query=dbt%20montreal&tags=comment):** no post since 2023 places a dbt role in Montreal or Quebec.
- **Company job boards with no Montreal dbt ads:** Workleap, Hopper, Lightspeed, AppDirect, Poka, Behavox, Zinnia, Osedea, Mirego, Sonder, Gopuff and Wealthsimple. SSENSE, Coveo, Dialogue, Potloc, Flinks, Nesto, Unito, Breathe Life, Plusgrade, Busbud and Nuvei have no open Greenhouse, Lever or Ashby board.
- **GitHub code and repository search:** no public dbt project at Hopper, Lightspeed, Workleap, SSENSE, Coveo, Potloc, Dialogue, AlayaCare, Mila, Unito or Infostrux.
- **[dbt Labs case studies](https://www.getdbt.com/sitemap-0.xml):** none for a Montreal company.

## 3. Companies looked at

- **Maxa dominates.** Maxa co-organises the chapter, and 10 people sit under its record. Plan one speaker per company per event.
- **Marketing posts:** some Maxa and agileDSS posts read as product marketing. Check for a hands-on angle before inviting.
- **Montreal Analytics is now part of Datatonic.** Its 2021 to 2023 speakers may have moved.
- **KOHO is based in Toronto.** Célia Bru, Gabriel Gambacorta and Ian Whitestone also appear in the Toronto file.

<!-- companies:start -->
60 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (8)</summary>

AlayaCare, Breathe Life (local presence not confirmed), KOHO Financial (local presence not confirmed), Maxa, Montreal Analytics (a Datatonic company), Potloc, Super.com (local presence not confirmed), Unito (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (20)</summary>

Aduna Global, Agoda, AppDirect, Astek, Autodesk, Behaviour Interactive, Data Sciences, Dialogue, Flinks, Infostrux (local presence not confirmed), Kake, KPMG Canada, Lightspeed Commerce, MaintainX, SELECT (local presence not confirmed), Slalom, Solution BI Canada, Toboggan Labs, TS Imagine, ValPay

</details>

<details><summary><b>dbt as a nice-to-have</b> (2)</summary>

Cohere, Snowflake Montreal User Group

</details>

<details><summary><b>Not verified</b> (26)</summary>

agileDSS, Air Canada, Air Transat, Altitude Sports, Browns Shoes, CDPQ, Datafold (local presence not confirmed), Gopuff (local presence not confirmed), GRICS, Harnois Énergies (local presence not confirmed), Maxa or Lightspeed Commerce (unclear) (local presence not confirmed), Montreal Artificial Intelligence and Data Engineering (meetup), Montreal Women in Machine Learning and Data Science, Poka, Privacy Safe (local presence not confirmed), PyLadies Montréal, R-Ladies Montréal, Sid Lee, Snowflake (local presence not confirmed), SSENSE, Veronica Beard (local presence not confirmed), Vidéotron, Warner Bros. Games Montréal, WiDS Montreal, Workleap, Zinnia

</details>

<details><summary><b>Uses a different stack</b> (4)</summary>

GDG Cloud Montreal, GDG Montreal / Women Techmakers Montreal, Vooban (local presence not confirmed), Women In The Loop

</details>

<details><summary><b>Blogs and sites scanned</b> (11)</summary>

- https://agiledss.com/blogue
- https://dev.to/potloc
- https://docs.getdbt.com/blog/authors
- https://maxa.ai/blog
- https://medium.com/ssense-tech
- https://usergroups.snowflake.com/montreal/
- https://www.meetup.com/montreal-data-engineering/
- https://www.meetup.com/montreal-women-in-machine-learning-and-data-science/
- https://www.meetup.com/pyladiesmtl/
- https://www.potloc.com/en/resources/blog
- https://www.widsworldwide.org/events/event/wids-montreal/

</details>

<details><summary><b>Other sources checked</b> (41)</summary>

- [Montréal dbt Meetup past events (meetup gql2)](https://www.meetup.com/montreal-dbt-meetup/)
- [dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers)
- [Coalesce 2025 speakers](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/speakers) (nothing useful)
- [Snowflake Montreal User Group events](https://usergroups.snowflake.com/montreal/)
- [Maxa blog](https://maxa.ai/blog)
- [Luma - Data Developer Meetup MTL (Maxa)](https://luma.com/7yr2a677) (nothing useful)
- [Infostrux events](https://www.infostrux.com/events)
- [Potloc DEV blog](https://dev.to/potloc)
- [SSENSE-TECH Medium](https://medium.com/ssense-tech) (nothing useful)
- [PyLadies Montréal meetup](https://www.meetup.com/pyladiesmtl/)
- [Montreal Women in ML & DS meetup](https://www.meetup.com/montreal-women-in-machine-learning-and-data-science/) (nothing useful)
- [WiDS Montreal](https://www.widsworldwide.org/events/event/wids-montreal/)
- [Montreal AI & Data Engineering meetup](https://www.meetup.com/montreal-data-engineering/) (nothing useful)
- [LinkedIn Jobs guest API (keywords=dbt, Montreal-area)](https://www.linkedin.com/jobs/search?keywords=dbt)
- [Snowflake Montreal User Group, older events (2023-2025)](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-hiver-winter-2024)
- [Snowflake Montreal User Group, Fall 2026](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-automne-fall-2026/)
- [agileDSS blog (French)](https://agiledss.com/blogue)
- [dbt developer blog author index](https://docs.getdbt.com/blog/authors)
- [MTL Data meetup (gql2)](https://www.meetup.com/mtldata/) (nothing useful)
- [Data Driven Montréal meetup (gql2)](https://www.meetup.com/datadrivenmontreal/) (nothing useful)
- [Montréal-Python meetup (gql2)](https://www.meetup.com/montreal-python/) (nothing useful)
- [R-Ladies Montreal (gql2)](https://www.meetup.com/rladies-montreal/) (nothing useful)
- [GDG Montreal and Women Techmakers (gql2)](https://www.meetup.com/gdg-montreal/)
- [GDG Cloud Montreal (gql2)](https://www.meetup.com/gdg-cloud-montreal/)
- [Montreal Databricks User Group](https://usergroups.databricks.com/montreal-databricks-user-group/) (nothing useful)
- [HEC Forecast](https://www.csdhec.ca/hec-forecast) (nothing useful)
- [ConFoo Montreal sessions](https://confoo.ca/en/yul2026/sessions) (nothing useful)
- [Medium publication feeds (SSENSE, Hopper, Lightspeed, Dialogue, Transit, Workleap and others)](https://medium.com/feed/ssense-tech) (nothing useful)
- [dev.to dbt tag authors](https://dev.to/t/dbt) (nothing useful)
- [Infostrux blog](https://www.infostrux.com/blog) (nothing useful)
- [Datatonic insights](https://www.datatonic.com/insights/) (nothing useful)
- [Meetup gql2 groupSearch near Montreal (women-in-data queries)](https://www.meetup.com/gql2)
- [GDG Montreal events API (Women Techmakers Montreal)](https://gdg.community.dev/api/event_slim/for_chapter/954/?status=Completed&page_size=300)
- [Women Techmakers Montreal IWD 2025](https://gdg.community.dev/e/mctsvr/)
- [Women Techmakers Montreal IWD 2024](https://gdg.community.dev/e/mj8dh2/) (nothing useful)
- [R-Ladies Montreal reboot (Meetup gql2)](https://www.meetup.com/rladies-montreal/events/308391618/)
- [Women In The Loop (Meetup gql2)](https://www.meetup.com/meetup-women-in-the-loop/)
- [Montréal Women in Agile (Meetup gql2)](https://www.meetup.com/WiA-Montreal/) (nothing useful)
- [QueerTech Montreal (Meetup gql2)](https://www.meetup.com/queertech-montreal/) (nothing useful)
- [PyLadies Montréal events since March 2026](https://www.meetup.com/PyLadiesMTL/) (nothing useful)
- [Data + Women and the Montreal Tableau user group](https://usergroups.tableau.com/montreal-tableau-user-group/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Otmane El Idrissi (agileDSS):** wrote about [migrating to Microsoft Fabric](https://agiledss.com/blogue/migration-microsoft-fabric), including dbt there (2025-02, in French).
  - **Raphael Steinman (Maxa):** wrote about [an agent that builds and maintains dbt pipelines](https://maxa.ai/blog/introducing-maxa-autopilot-agentic-way-build-maintain-data-pipelines) (2026-05).
  - **Samuel Bouchard (Maxa):** wrote about [reverse-engineering an inherited chart of accounts](https://maxa.ai/blog/reverse-engineering-a-chart-of-accounts-you-inherited) (2026-08).
  - **Priyaanka Arora (Maxa):** wrote ["Why business context should come before building semantic layers"](https://maxa.ai/blog/why-business-context-before-building-semantic-layers) (2026-09). Also announced Maxa's July 2026 Montreal meetup, so a possible connector.
  - **Callie White (Montreal Analytics):** co-wrote [a dbt certification guide](https://docs.getdbt.com/blog/tips-for-the-dbt-certification-exam) on the dbt developer blog (2023-02). Current employer not verified.
- **Anchor speakers:**
  - **Maxime Castello (Poka):** [from daily batch to near real-time transformations at controlled Snowflake cost](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-hiver-winter-2024), December 2024.
  - **João Vitor de Camargo (Maxa):** writes on [spec-driven development with dbt Wizard](https://maxa.ai/blog/how-spec-driven-development-maximizes-dbt-wizard). Spoke at the [Snowflake Montreal User Group in September 2026](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-automne-fall-2026/).
  - **Eliott Pourrat (Maxa) and Nicolas Lelièvre:** presented [dbt on Snowflake](https://www.getdbt.com/events) at Snowflake's data engineering masterclass in Montreal, September 2025.
  - **Elisabeth Mercier (AlayaCare):** [practical strategies for multi-tenant data on Snowflake](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-hiver-winter-2026/), January 2026.
- **Connectors:**
  - **Daniel Paes (Solution BI Canada):** co-organises the [Montreal dbt Meetup](https://www.meetup.com/montreal-dbt-meetup/).
  - **Quentin Tabourin (Maxa) and Lamia Goeffon:** [chapter leaders](https://usergroups.snowflake.com/montreal/) of the Snowflake Montreal User Group.
  - **Cyril Marques (Montreal Analytics):** founded the chapter and ran it from 2021 to 2023.
  - **Sophie Courtemanche-Martel (Altitude Sports):** [hosts Snowflake Montreal User Group events](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-hiver-winter-2026/).
  - **Laurence de Villers:** organiser of [GDG Montreal and Women Techmakers Montreal](https://www.meetup.com/gdg-montreal/events/300159943/).
  - **Stacy Véronneau (TELUS Digital):** organiser of [GDG Cloud Montreal](https://www.meetup.com/gdg-cloud-montreal/).
  - **JL Marechaux:** [WiDS Montreal](https://www.widsworldwide.org/events/event/wids-montreal/) ambassador.

## 5. Before outreach

- [ ] **Check "in region" calls.** 49 people are marked in the region, but only 2 of those calls come from the LinkedIn pass. Most came from a local event or the employer's head office during research.
- [ ] **Check unknown locations.** 17 people, including Jacob Frackson, Jeremie Pineau, Callie White, Jade Milaney and Kelsey Pericak.
- [ ] **Check current employers.** Nicolas Lelièvre may be at Maxa or Lightspeed Commerce. Lamia Goeffon has a 2026 Maxa byline but is listed at Browns Shoes. Stéphane Burwash sits under Infostrux with a Potloc title. The former Montreal Analytics staff may have moved.
- [ ] **Check tier-1 people raised by the rule.** Tomas Rezek, Adrien Chaudé, Adrien Lecellier and Ricardo Briones are tier 1, but the posts are about BI tools and data design, not dbt. Fabien Rivenet's post reads as marketing.
- [ ] **Coordinate with the Toronto chapter** on Célia Bru, Gabriel Gambacorta and Ian Whitestone.
- [ ] **Check who is already booked.** Compare leads with the chapter's upcoming events after the 2026 relaunch.

## 6. Next run

- **Sources to try first:**
  - **Snowflake Montreal User Group:** new events, through the slug pattern `snowflake-montreal-presents-<season>-<year>`.
  - **Maxa and agileDSS blogs:** new posts.
  - **Medium feeds:** SSENSE, Hopper, Lightspeed, Dialogue, Transit and Workleap. Try `api.rss2json.com` and space the calls out.
  - **Job ads:** refresh with `site:` searches on Lever, Greenhouse and Ashby, in English and French. The 40 ads date from 2026-09-24.
  - **Pages not read yet:** ConFoo sessions, Coalesce 2025 speakers and the Data Developer Meetup MTL panellists.
  - **PyLadies Montréal:** ask the organisers about the topics of the March 2026 talks.
  - **Women Techmakers Montreal IWD speakers:** the 2024 and 2025 pages name no speakers. Ask Stefania Pecore or Mimoh Solanki for the line-ups.
  - **First-time speakers outside Maxa and agileDSS:** for example at Lightspeed, Workleap, AlayaCare and Poka.
- **People to locate:** 53 people are still `not_searched` on LinkedIn. Start with the 17 unknown locations.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `montreal/montreal_dbt_companies.json`, the chapter `montreal-dbt-meetup`, `../enriched/montreal-dbt-meetup.json` and the region "Greater Montreal". Search in English and French, and record French content with an English description. Plan one Maxa speaker per event. Budget about 25 web searches.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build from one research run and a LinkedIn Jobs scan: 44 companies, 35 people, 40 job ads at 18 companies, 6 past meetups. Tiers: 2 tier 1, 21 tier 2, 5 tier 3, 7 connectors. Lead types: 30 proven speakers, 2 emerging voices, 3 featured. |
| 2026-10-01 | 2 | Extension run, mostly from older Snowflake Montreal User Group pages and the Maxa and agileDSS blogs: 67 people and 58 companies. Emerging voices rose from 2 to 11, and tier 1 from 2 to 12. |
| 2026-10-01 | 2 | Location pass from public pages: no one qualified. |
| 2026-10-01 | 2 | LinkedIn pass from search results: 12 people searched, 3 placed, 2 in the region and 1 elsewhere. 17 people are still unknown. |
| 2026-10-01 | 3 | Women-in-data pass: Women Techmakers Montreal IWD pages, R-Ladies Montreal and Women In The Loop. 6 new people, all organisers recorded as connectors. |
| 2026-10-01 | 4 | Company pass with fetches only: HN Who is hiring, company job boards, dbt Labs case studies, GitHub code and repository search, and Meetup venues. 58 to 61 companies. Cohere, Sid Lee and Zinnia added. AlayaCare raised from medium to strong, and Super.com from weak to strong. |
