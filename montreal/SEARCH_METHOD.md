# Montreal dbt search: method, lessons and replication prompt

This file goes with `montreal_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in Greater Montreal who could **speak at** (or attend) the [Montreal dbt Meetup](https://www.meetup.com/montreal-dbt-meetup/), and the local companies that use dbt.
- **Region:** Greater Montreal.

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 56 |
| People | 67 |
| Tier 1 leads | 12 |
| First-time speakers (publish, no talk yet) | 11 |
| Proven speakers | 53 |
| Spoke at this chapter before | 15 |
| Based in the region | 49 |
| Based elsewhere | 1 |
| Location unknown | 17 |
| With a LinkedIn profile | 6 |
| Job ads mentioning dbt | 40 |
| Past chapter meetups | 6 |
<!-- at-a-glance:end -->

Much of the local content is in French. French posts and talks are recorded as they are, with an English description.

## 1. How the search was done

Two research runs built the file. The first build (2026-09-24) used about 18 web searches and a job ad scan. The extension (2026-10-01) looked for more speakers, especially first-time speakers. It used about 17 web searches before the session limit, then direct page fetches.

### Step 1: Snowflake Montreal User Group

- **[Snowflake Montreal User Group](https://usergroups.snowflake.com/montreal/):** the richest local source. It is a better speaker source than the dbt chapter, which was dormant for long periods. Its agendas are bilingual.
- **First build:** the June 2025, January 2026, April 2026 and June 2026 agendas.
- **Extension:** older event pages from July 2023 to April 2025 gave 17 new speakers. Pages follow the slug pattern `snowflake-montreal-presents-<season>-<year>`, for example [winter 2024](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-hiver-winter-2024).
- **[Fall 2026](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-automne-fall-2026/):** talks by Oliver Benning, Lamia Goeffon and João Vitor de Camargo.

### Step 2: Company and consultancy blogs

- **[Maxa blog](https://maxa.ai/blog):** named authors writing on dbt, semantic layers and AI agents. The listing hides bylines, but each post's JSON-LD author field names the writer. Maxa hosted the chapter's 2026 relaunch.
- **[agileDSS blog](https://agiledss.com/blogue):** a Quebec BI consultancy that publishes in French. Six authors with titles, and one post that mentions dbt.
- **[dbt developer blog authors](https://docs.getdbt.com/blog/authors):** Callie White and Jade Milaney of Montreal Analytics, from 2023.
- **[Potloc on dev.to](https://dev.to/potloc):** a 2023 post on dbt and Elementary.
- **[Infostrux events](https://www.infostrux.com/events):** Montreal labs and a dbt talk by Nasko Grozdanov.
- **No yield:** Medium feeds ([SSENSE](https://medium.com/feed/ssense-tech), Hopper, Lightspeed, Dialogue, Transit, Workleap) returned HTTP 429 (too many requests). The [Infostrux blog](https://www.infostrux.com/blog) and [Datatonic insights](https://www.datatonic.com/insights/) have no bylines. The Montreal Analytics blog now redirects to Datatonic. [dev.to's dbt tag](https://dev.to/t/dbt) had 112 authors, none in Montreal or Quebec.

### Step 3: Other Montreal meetups and conferences

- **Read through Meetup `gql2` with `curl`:** [MTL Data](https://www.meetup.com/mtldata/), [Data Driven Montréal](https://www.meetup.com/datadrivenmontreal/), [Montréal-Python](https://www.meetup.com/montreal-python/), [GDG Montreal](https://www.meetup.com/gdg-montreal/) and [GDG Cloud Montreal](https://www.meetup.com/gdg-cloud-montreal/).
- **Yield:** the general data groups had no dbt talks since 2023. GDG Montreal gave Jihoo Park (Warner Bros. Games Montréal) and its organisers. GDG Cloud Montreal gave its organiser.
- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** no Montreal employers. KOHO speakers are the nearest match.
- **No yield:** the [Montreal Databricks User Group](https://usergroups.databricks.com/montreal-databricks-user-group/) ran AI vendor demos in March 2026. [HEC Forecast](https://www.csdhec.ca/hec-forecast) lists no speakers. [ConFoo](https://confoo.ca/en/yul2026/sessions) returned HTTP 500. The [Data Developer Meetup MTL](https://luma.com/7yr2a677) page lists no panellists. The [Montreal AI & Data Engineering meetup](https://www.meetup.com/montreal-data-engineering/) is off topic.

### Step 4: Women-in-data communities

This step finds speakers through women-focused groups' own events. It never records or guesses anyone's gender.

- **Women on Snowflake (June 2024):** a [Snowflake Montreal User Group edition](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-montreal-user-group-meeting) with an all-women speaker line-up. It gave four speakers.
- **[PyLadies Montréal](https://www.meetup.com/pyladiesmtl/):** two named speakers in March 2026. Their topics are not listed.
- **Women Techmakers Montreal:** runs through [GDG Montreal](https://www.meetup.com/gdg-montreal/). It gave organisers and ambassadors.
- **[WiDS Montreal](https://www.widsworldwide.org/events/event/wids-montreal/):** the 2024 edition names an ambassador only.
- **No yield:** the [Montreal Women in ML & DS meetup](https://www.meetup.com/montreal-women-in-machine-learning-and-data-science/) has had no events since June 2024. [R-Ladies Montreal](https://www.meetup.com/rladies-montreal/) is rebooting with intro sessions.
- **Result:** 10 people are tagged `women_in_data_community`.

### Step 5: Job ads

- **First build:** a logged-out scan of LinkedIn Jobs for "dbt" in the Montreal area. Up to 150 ads were checked for the whole word "dbt". 40 ads at 18 companies mention it. Many ads are in French.
- **Current rule:** the shared method no longer allows fetching the LinkedIn Jobs API. Refresh the ads through job board `site:` searches instead.

### Step 6: Chapter history

- **Source:** every named speaker in [`../enriched/montreal-dbt-meetup.json`](../enriched/montreal-dbt-meetup.json) was added as a person. That file holds 6 meetups, from 2021-10-29 to 2026-08-06.
- **Organisers over time:** Montreal Analytics ran the 2021 to 2023 events. Solution BI hosted October 2024. Maxa and Solution BI ran the August 2026 relaunch, a networking evening with no talks.
- **Result:** 15 people in the file have spoken at the chapter.

### Step 7: Location pass and LinkedIn pass

The location rules are in [`../research/README.md`](../research/README.md). In short, a location needs the person's own profile, or a recent in-person local talk plus a local office.

- **Location pass (page fetches):** no one qualified. Most chapter talks were from 2021 to 2023, too old for in-person evidence. The bios on event pages state no city. Audrey Leduc spoke in person in October 2024, but KOHO's Montreal office could not be confirmed.
- **LinkedIn pass (search results only):** 12 people searched and 3 placed. [Hassan Al-Rabea](https://www.linkedin.com/in/hassan-al-rabea/) and [Audrey Leduc](https://www.linkedin.com/in/audreyleduc/) are in Montreal. [Kristi Gourlay](https://www.linkedin.com/in/kristi-gourlay/) is in Toronto.
- **Skipped:** results that gave only "Canada" or "United States", or did not tie the profile to the recorded employer.
- **Still unknown:** 17 people.

## 2. What we learnt

- **Sources that worked:**
  - **Snowflake Montreal User Group pages:** the best source of local proven speakers. Try the slug pattern to reach older events.
  - **Maxa post metadata:** the JSON-LD author field names writers the listing hides.
  - **French consultancy blogs:** agileDSS posts carry each author's title.
  - **Meetup `gql2`:** it works from `curl` with no browser. Query by group name so results do not depend on a shared browser tab.
- **Sources that didn't:**
  - **Medium:** HTTP 429 to both `curl` and direct fetches.
  - **GitHub user search:** rate-limited.
  - **General Montreal data meetups:** no dbt talks since 2023.
  - **Web search:** the session limit stopped the extension after about 17 searches, and most results were job ads.
- **Watch out for:**
  - **Maxa dominates.** Maxa co-organises the chapter, and 10 people sit under its record. Plan one speaker per company per event.
  - **Marketing posts:** a first-time speaker (an "emerging voice") is someone who publishes about dbt but has no talk on record. Some Maxa and agileDSS posts read as product marketing. Check for a hands-on angle before inviting.
  - **Unclear employers:** Nicolas Lelièvre may be at Maxa or Lightspeed Commerce. Lamia Goeffon has a 2026 Maxa byline but is listed at Browns Shoes. Stéphane Burwash sits under Infostrux with a Potloc title.
  - **Montreal Analytics is now part of Datatonic.** Its 2021 to 2023 speakers may have moved.
  - **People in two cities:** Célia Bru, Gabriel Gambacorta and Ian Whitestone also appear in the Toronto file. KOHO is based in Toronto.

## 3. Key leads

A tier is a priority level. Tier 1 means a person in the region (or not known to be elsewhere) with a dbt item from 2024 onwards, or a first-time speaker with a post from 2024 onwards.

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
- **Connectors:** community organisers who can introduce people.
  - **Daniel Paes (Solution BI Canada):** co-organises the [Montreal dbt Meetup](https://www.meetup.com/montreal-dbt-meetup/).
  - **Quentin Tabourin (Maxa) and Lamia Goeffon:** [chapter leaders](https://usergroups.snowflake.com/montreal/) of the Snowflake Montreal User Group.
  - **Cyril Marques (Montreal Analytics):** founded the chapter and ran it from 2021 to 2023.
  - **Sophie Courtemanche-Martel (Altitude Sports):** [hosts Snowflake Montreal User Group events](https://usergroups.snowflake.com/events/details/snowflake-montreal-presents-snowflake-montreal-user-group-meetup-hiver-winter-2026/).
  - **Laurence de Villers:** organiser of [GDG Montreal and Women Techmakers Montreal](https://www.meetup.com/gdg-montreal/events/300159943/).
  - **Stacy Véronneau (TELUS Digital):** organiser of [GDG Cloud Montreal](https://www.meetup.com/gdg-cloud-montreal/).
  - **JL Marechaux:** [WiDS Montreal](https://www.widsworldwide.org/events/event/wids-montreal/) ambassador.

## 4. Before outreach

- [ ] **Check "in region" calls.** 49 people are marked in the region, but only 2 of those calls come from the LinkedIn pass. Most came from a local event or the employer's head office during research.
- [ ] **Check unknown locations.** 17 people, including Jacob Frackson, Jeremie Pineau, Callie White, Jade Milaney and Kelsey Pericak.
- [ ] **Check current employers.** Nicolas Lelièvre, Lamia Goeffon, Stéphane Burwash and the former Montreal Analytics staff.
- [ ] **Check tier-1 people raised by the rule.** Tomas Rezek, Adrien Chaudé, Adrien Lecellier and Ricardo Briones are tier 1, but their posts are about BI tools and data design, not dbt. Fabien Rivenet's post reads as marketing.
- [ ] **Coordinate with the Toronto chapter** on Célia Bru, Gabriel Gambacorta and Ian Whitestone.
- [ ] **Check who is already booked.** Compare leads with the chapter's upcoming events after the 2026 relaunch.

## 5. Next run

- **Read the unread Medium feeds:** SSENSE, Hopper, Lightspeed, Dialogue, Transit and Workleap. Try `api.rss2json.com` and space the calls out.
- **Finish LinkedIn.** 53 people are still `not_searched`. Start with the 17 unknown locations.
- **Refresh job ads** with `site:` searches on Lever, Greenhouse and Ashby, in English and French. The 40 ads date from 2026-09-24.
- **Try the pages not read yet:** ConFoo sessions, Coalesce 2025 speakers and the Data Developer Meetup MTL panellists.
- **Ask the PyLadies Montréal organisers** about the topics of the March 2026 talks.
- **Look for first-time speakers outside Maxa and agileDSS**, for example at Lightspeed, Workleap, AlayaCare and Poka.

## 6. Replication prompt

````
You are extending my dataset of Montreal companies that use dbt, and people who could speak at or
attend the Montreal dbt Meetup. The file is montreal/montreal_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Region: Greater Montreal.
Read montreal/SEARCH_METHOD.md first, then research/README.md, research/raw-format.md,
research/location-task.md and research/linkedin-task.md.

Budget about 25 web searches. Try these first:
1. New Snowflake Montreal User Group events (slug pattern snowflake-montreal-presents-<season>-<year>).
2. New posts on the Maxa and agileDSS blogs (French content is fine; record it with an English description).
3. Medium feeds through api.rss2json.com: SSENSE, Hopper, Lightspeed, Dialogue, Transit, Workleap.
4. Job ads: site: searches on Lever, Greenhouse and Ashby for dbt Montréal, in English and French.

Rules: never fetch LinkedIn pages or the LinkedIn Jobs API, use only search results. Public
professional information only; never record or guess gender; pronouns only when self-stated.
Skip past chapter speakers; the assembler adds them. Plan one Maxa speaker per event. Assemble
with research/assemble.py --base, run research/validate.py (must print ok), then add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build from one research run and a LinkedIn Jobs scan: 44 companies, 35 people, 40 job ads at 18 companies, 6 past meetups. Tiers: 2 tier 1, 21 tier 2, 5 tier 3, 7 connectors. Lead types: 30 proven speakers, 2 emerging voices, 3 featured. |
| 2026-10-01 | 2 | Extension run, mostly from older Snowflake Montreal User Group pages and the Maxa and agileDSS blogs: 67 people and 58 companies. Emerging voices rose from 2 to 11, and tier 1 from 2 to 12. |
| 2026-10-01 | 2 | Location pass from public pages: no one qualified. |
| 2026-10-01 | 2 | LinkedIn pass from search results: 12 people searched, 3 placed, 2 in the region and 1 elsewhere. 17 people are still unknown. |
