# Düsseldorf dbt search: method, lessons and replication prompt

This file goes with `dusseldorf_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in the Rhein-Ruhr area who could **speak at** (or attend) the [Rhein-Ruhr dbt Meetup](https://www.meetup.com/rhein-ruhr-dbt-meetup/), and the local companies that use dbt.
- **Region:** Düsseldorf, Cologne, Essen, Dortmund, Bonn and nearby towns. Commuter towns are local for this chapter, so Münster counts. Leipzig counts as outside.

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 64 |
| People | 69 |
| Tier 1 leads | 22 |
| First-time speakers (publish, no talk yet) | 20 |
| Proven speakers | 43 |
| Spoke at this chapter before | 5 |
| Based in the region | 32 |
| Based elsewhere | 5 |
| Location unknown | 32 |
| With a LinkedIn profile | 9 |
| Job ads mentioning dbt | 49 |
| Past chapter meetups | 2 |
<!-- at-a-glance:end -->

## 1. How the search was done

### Step 1: Chapter history

- **What was checked:** the two in-person chapter events, both in Cologne. The first was on 2024-12-05 at [adesso](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/304543797/). The second was on 2025-05-15 at [taod](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/307198615/).
- **What it yielded:** 5 past speakers, added from `../enriched/rhein-ruhr-dbt-meetup.json`. The meetup.com event pages also gave full agendas and organiser names.
- **Activity:** the chapter has had no events since May 2025.

### Step 2: Other local meetups and conferences

- **Databricks User Group Rhein-Ruhr:** the [group](https://www.meetup.com/databricks-user-group-rhein-ruhr/) gave the most local data-platform speakers. They work at Deichmann, Handelsblatt, BarmeniaGothaer and FIEGE.
- **Microsoft data community:** [Data Saturday Rheinland](https://datasaturdays.com/Event/20260711-datasaturday0084) (2025 and 2026) lists about 60 sessions. The [Data Platform Usergroup Rheinland](https://www.meetup.com/pass-microsoft-data-platform-usergroup-rheinland/) and [Datamonsters Ruhrgebiet](https://www.meetup.com/pass-germany-regional-group-ruhrgebiet/) added more. Most talks are on the Microsoft stack, and many speakers come from outside the region.
- **Smaller meetups:** the [trivago Tech, Data & Product meetup](https://www.meetup.com/trivago-tech-data-product/) ran a data-platform evening in August 2025. [Engineering Kiosk Rhine-Ruhr](https://www.meetup.com/engineering-kiosk-rhine-ruhr/), [Data Analytics & AI Köln](https://www.meetup.com/data-analytics-ai-koeln/) and the [Power Platform & Fabric User Group Cologne](https://www.meetup.com/power-platform-ug-cologne/) each added a few speakers.
- **Online trainings:** [Analytics Pioneers](https://www.meetup.com/analytics-pioneers-dusseldorf/) ran a dbt modelling course in May 2024. Its organisers are in Munich.
- **Group search:** a meetup.com search around the Rhein-Ruhr centre listed about 120 local groups. The past events of 20 data groups were read.

### Step 3: Company and consultancy blogs

- **adesso:** the [blog feed](https://www.adesso.de/de/news/blog/blog-rss.xml) and each post's author box gave 9 emerging voices. An emerging voice is someone who publishes about data topics but has no talk on record. Only two adesso posts mention dbt.
- **ORAYLIS:** the [blog feed](https://www.oraylis.de/feed) gave 6 emerging voices. The posts cover Microsoft Fabric and Databricks, not dbt.
- **b.telligent:** the [blog](https://www.btelligent.com/en/blog) has one dbt post, from August 2026.
- **GitHub:** a user search by NRW city found 3 people with their own dbt projects.
- **No dbt content:** [trivago tech blog](https://tech.trivago.com/), [codecentric](https://www.codecentric.de/feed), [inovex](https://www.inovex.de/de/blog/?s=dbt), [areto](https://areto.de/blog/) and [datadice](https://www.datadice.io/en/blog/). The large NRW corporates (REWE, METRO, Henkel, Vodafone) publish nothing on dbt.

### Step 4: Women-in-data communities

- **[Women in Big Data NRW](https://www.meetup.com/women-in-big-data-dusseldorf/):** recent events are discussions without named speakers. The [recap of its Thoughtworks evening](https://www.womeninbigdata.org/women-in-big-data-nrw-x-thoughtworks-event/) named two speakers and two hosts.
- **[Women in AI Cologne #3](https://www.ki.nrw/women-in-ai-cologne-meetup-3/):** one speaker, on AI transformation.
- **No data speakers:** PyCologne, PyData Dortmund, inovex Cologne, Female Dev Club and Women in Tech Köln.
- **Rule:** speakers were taken only from the communities' own events. No one's gender is recorded or guessed.

### Step 5: Job ads

- **LinkedIn Jobs, logged out:** a search for dbt around Düsseldorf and the Rhein-Ruhr area. Up to 150 ads were checked for the whole word "dbt". 49 ads at 24 companies mention it.
- **Who is hiring:** adesso posted 18 of the 49 ads. viadee and Redcare Pharmacy posted 4 each.

### Step 6: Location pass

- **Method:** each person's base was looked up on public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
- **Best source:** meetup.com RSVP and host lists. They give the profile city of the person who spoke at that event.
- **Result:** 16 people were placed, 12 in the region and 4 elsewhere. Unknown locations fell from 51 to 35.

### Step 7: LinkedIn pass

- **Method:** one or two LinkedIn searches per person, using search results only. No LinkedIn page was opened.
- **Who:** the 15 tier-1 blog authors without a location.
- **Result:** 2 people were placed. Michael Peichl is in Leipzig, outside the region. Jonas Thiele is in Münster, which counts as local. 33 locations are still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **meetup.com's `gql2` endpoint** answers plain `curl` requests. It gives past events with full speaker text, and RSVP lists with profile cities.
  - **Sessionize embeds** on Data Saturday pages give speaker names and taglines.
  - **adesso and ORAYLIS blog feeds** with author boxes were the best source of first-time speakers. They give name and role, but rarely the office.
  - **meetup.com event pages** fetched directly return full agendas, even without a browser.
- **Sources that didn't:**
  - **Web search** mostly returned job ads for NRW dbt queries. The session's search limit was reached early.
  - **Medium, dev.to and GitHub search** were rate-limited, so no Medium or dev.to authors were scanned.
  - **Snowflake user groups** have no NRW chapter. The Köln Snowflake and PyData Cologne-Bonn groups no longer exist.
  - **Big corporates** publish nothing on dbt.
- **Watch out for:**
  - **adesso dominates.** It has 9 of the 20 emerging voices and 18 of the 49 job ads. Plan one speaker per company per event.
  - **Tier 1 is generous here.** 16 of the 22 tier-1 people have no item that mentions dbt. Most are adesso and ORAYLIS authors writing about Fabric, Databricks or Snowflake.
  - **Consultancy authors rarely state an office.** That is why most tier-1 people have no known location.
  - **Hicham Babahmed** is also spelled "Hisham". This organiser of the first event (then at adesso) now works at dbt Labs, with a Frankfurt profile.
  - **Shared with the Munich file:** Mathias Heinze (b.telligent) and Benedikt Buchert (Analytics Pioneers) appear in both. The Munich file places Mathias Heinze in Munich, on a name match only.

## 3. Key leads

- **First-time speakers:**
  - **Mathias Heinze**, b.telligent: [Adding the E to dbt: extracting source systems with dbt Core and Snowflake](https://www.btelligent.com/en/blog/extracting-source-systems-dbt-core-snowflake) (August 2026). This is the only new lead writing directly about dbt. Location unknown.
  - **Jan Krings**, Cologne, employer not stated: [a retail analytics pipeline built with dbt](https://github.com/jan-krings-dev/retail_bi_pipeline_rewe) (2026).
  - **Marc-Philipp Esser**, Cologne: [a Data Vault project for e-commerce data](https://github.com/m-p-esser/ecom_data_vault) (2024).
  - **Tim Pursche**, adesso: [data quality monitoring with Snowflake data metric functions](https://www.adesso.de/de/news/blog/implementierung-eines-data-quality-monitorings-mit-data-metric-functions-in-snowflake.jsp) (July 2026). This fits a talk on dbt tests.
  - **Kevin Letellier**, ORAYLIS: [Data Mesh in Azure](https://oraylis.de/blog/2024/data-mesh-in-azure) (2024).
- **Anchor speakers:**
  - **Sönke Maibach**, taod, Cologne: [lessons on migrating a legacy stack to dbt](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/307198615/) at the chapter in May 2025.
  - **Alex Rupp**, Schüttflix: [pairing dbt and Slack bots](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/307198615/) at the chapter in May 2025.
  - **Andrés Sopeña Pérez**, trivago, Düsseldorf: [Plenty of Mistakes](https://www.meetup.com/trivago-tech-data-product/events/309266552/), on moving trivago's data platform to the cloud (August 2025).
  - **Mareike Heller**, DeepL, Cologne: [value lineage for marketing measurement](https://www.womeninbigdata.org/women-in-big-data-nrw-x-thoughtworks-event/) at Women in Big Data NRW (May 2025).
- **Connectors:**
  - **Sarah Hennig** and **Benedikt Stienen**, taod: organiser of the [May 2025 chapter event](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/307198615/), and the CEO who runs taod's [Cologne event programme](https://www.taod.de/pressemitteilungen/data-ai-after-hours).
  - **Aasma Jabin**, trivago: wrote up [trivago's QA meetup](https://tech.trivago.com/post/2026-08-12-agents-randomness-and-receipts-notes-from-trivagos-qa-meetup), which shows trivago still hosts outside meetups in Düsseldorf.
  - **Liisel Jessop**: lead organiser of [Women in Big Data NRW](https://www.meetup.com/women-in-big-data-dusseldorf/).
  - **Margarita Neumüller** (ALDI SÜD) and **Gabi Münster** (Microsoft): organisers of [Datamonsters Ruhrgebiet](https://www.meetup.com/pass-germany-regional-group-ruhrgebiet/).
  - **Oliver Engels**, oh22data: co-organiser of [Data Saturday Rheinland](https://datasaturdays.com/Event/20260711-datasaturday0084).
  - **Daniela Jäkel**, Thoughtworks Cologne: co-host of the [Women in Big Data NRW evening](https://www.womeninbigdata.org/women-in-big-data-nrw-x-thoughtworks-event/), and a venue route.

## 4. Before outreach

- [ ] **Check tier-1 blog authors for dbt.** 16 of the 22 have never written about dbt.
- [ ] **Confirm each consultancy author's office.** None of the adesso, ORAYLIS or b.telligent author boxes states a city.
- [ ] **Check the LinkedIn hints that had no profile link.** Search summaries put Lasse Jenzen, Insa Menzel, Nils Kux and Tobias Jasinski in Düsseldorf, but no profile carried the evidence.
- [ ] **Check Inna Zykova.** A LinkedIn result from the Berlin search places this person in Düsseldorf. This file still records the location as unknown.
- [ ] **Treat visiting speakers as visitors.** Pádraic Slattery is in Amsterdam, Stephan Durry in Berlin, and Sascha Dittmann and Hicham Babahmed in Frankfurt.
- [ ] **dbt Labs staff are labelled.** Stephan Durry and Hicham Babahmed work there. They can speak, but check the line-up has practitioners first.

## 5. Next run

- **People still without a location:** 33. All 15 LinkedIn targets have now been searched once or twice. Only Jonas Thiele, in Münster, was placed in the region. The 17 people below were never searched on LinkedIn:
  - Tier 1: Siver Rajab (adesso).
  - Tier 2: Alex Rupp, Anastasia Senitz, Hanna Schwab, Benedikt Buchert, Daniel Schmidt, Diana Ackermann, Jake Mongaya, Marco Nielinger, Mario Müller and Simon Schröder.
  - Tier 3: Andreas Schiffer, Benjamin Kirsche, Christopher König, Frank Geisler, Moritz Bauer, Sebastian Grünwald and Stephan Dahlmann.
  - Connector: Oliver Engels.
- **Sources not yet searched:** Medium and dev.to authors, which were rate-limited. Try them from a fresh session.
- **What to try first:** search Alex Rupp on LinkedIn, as a past chapter speaker. Then ask taod and adesso which of their authors work in the region.

## 6. Replication prompt

````
You are extending the Rhein-Ruhr dbt dataset: dusseldorf/dusseldorf_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. The region is Düsseldorf, Cologne, Essen,
Dortmund, Bonn and nearby towns; commuter towns such as Münster count as local.
Read dusseldorf/SEARCH_METHOD.md first, then
research/README.md and the briefs it links (raw-format.md, location-task.md, linkedin-task.md).

Budget about 25 web searches. Most NRW dbt searches return job ads, so prefer direct fetches.

1. New talks: past events of the Rhein-Ruhr dbt Meetup, Databricks User Group Rhein-Ruhr,
   trivago Tech, Data & Product, Datamonsters Ruhrgebiet and Data Saturday Rheinland,
   through the meetup.com gql2 endpoint and Sessionize embeds.
2. New posts: the adesso, ORAYLIS and b.telligent blog feeds, with each author box.
   Then Medium and dev.to, which were rate-limited last time.
3. Women-in-data: new Women in Big Data NRW and Women in AI Cologne events. Take speakers
   only from the community's own events.
4. Locations: the 18 never-searched people listed in SEARCH_METHOD.md §5.
Rules: never open LinkedIn pages, use only search results. Record professional information
only, never gender, and pronouns only when self-stated. Assemble with research/assemble.py
--base, apply locations with research/apply_locations.py, and run research/validate.py.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build, from one research pass and a LinkedIn Jobs scan. 49 companies, 23 people and 49 dbt job ads at 24 companies. 16 proven speakers, 6 featured and 1 emerging voice. 5 people had spoken at the chapter. 7 people had LinkedIn profiles. |
| 2026-10-01 | 2 | Extension run through meetup.com, Sessionize, consultancy blog feeds and GitHub. 46 people and 15 companies added, for 69 people and 64 companies. Emerging voices rose from 1 to 20. Tier 1 rose from 1 to 21. |
| 2026-10-01 | 2 | Location pass from public pages. 16 people placed: 12 in the region and 4 elsewhere. Unknown locations fell from 51 to 35. |
| 2026-10-01 | 2 | LinkedIn pass on the 15 tier-1 blog authors without a location. 2 people placed: 1 in the region and 1 elsewhere. 33 locations are still unknown. |
