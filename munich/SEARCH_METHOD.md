# Munich dbt search: method, lessons and replication prompt

This file goes with `munich_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in the Munich area who could **speak at** (or attend) the [Munich dbt Meetup](https://www.meetup.com/munich-dbt-meetup/), and the local companies that use dbt.
- **Region:** the Munich metro area. Ingolstadt and Haar are counted in. Karlsruhe, Ulm, Würzburg and Zürich are outside.

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 65 |
| People | 73 |
| Tier 1 leads | 20 |
| First-time speakers (publish, no talk yet) | 23 |
| Proven speakers | 44 |
| Spoke at this chapter before | 16 |
| Based in the region | 44 |
| Based elsewhere | 12 |
| Location unknown | 17 |
| With a LinkedIn profile | 16 |
| Job ads mentioning dbt | 24 |
| Past chapter meetups | 7 |
<!-- at-a-glance:end -->

## 1. How the search was done

### Step 1: Chapter history

- **What was checked:** 7 chapter events from April 2023 to February 2026. Most were held at [Synabi](https://synabi.com/en/events/) in Munich. One was at Daiichi Sankyo in July 2025.
- **What it yielded:** 16 past speakers, added from `../enriched/munich-dbt-meetup.json`. The November 2025 event has no talks on record.
- **What failed:** the [past events page](https://www.meetup.com/munich-dbt-meetup/events/?type=past) renders in the browser only, so a plain fetch returned nothing.

### Step 2: Other local meetups and conferences

- **[Munich Snowflake User Group](https://www.meetup.com/munich-snowflake-data-cloud-meetup-group/):** the richest dbt-adjacent source. It ran a joint [Snowflake & dbt evening](https://usergroups.snowflake.com/events/details/snowflake-munich-presents-snowflake-amp-dbt-user-group-meeting-in-munich/) at Synabi in February 2025. The user group's own [event API](https://usergroups.snowflake.com/api/event/?chapter=143) lists all 10 of its events.
- **[Munich Datageeks](https://www.munich-datageeks.de/tag/talks/):** its recorded talk write-ups gave the strongest dbt practitioner lead. Its [meetup.com events](https://www.meetup.com/munich-datageeks/events/?type=past) added data-engineering speakers from E.ON, Finanz Informatik, Lakekeeper, Firebolt and Aiven.
- **Group search:** a meetup.com search around Munich listed about 60 data groups. The past events of 20 were read and searched for dbt.
- **Smaller groups with a dbt talk:** [Kaggle Munich](https://www.meetup.com/kaggle-munich/events/?type=past) hosted a dbt talk in June 2024. [Analytics Pioneers Munich](https://www.meetup.com/analytics-pioneers-munich/events/?type=past) ran dbt trainings in 2022 and 2024.
- **Low yield:** [Data Modeling Meetup Munich](https://www.meetup.com/data-modeling-dm3/) (speakers are international and online), [PyData Munich](https://www.meetup.com/pydata-munchen/events/?type=past) (GenAI only), the [TDWI conference programme](https://www.tdwi-konferenz.de/de/programm/konferenzprogramm), [PyCon DE](https://pretalx.com/pyconde-pydata-2026/schedule/) and the [Munich Database Meetup](https://munichdatabases.xyz/).

### Step 3: Company and consultancy blogs

- **b.telligent:** the [blog](https://www.btelligent.com/en/blog) names an author on every post. Its 211 posts gave 6 emerging voices. An emerging voice is someone who publishes about data topics but has no talk on record. Its [dbt partner page](https://www.btelligent.com/en/partner/dbt) names two contacts.
- **synvert:** the [blog](https://synvert.com/de-de/synvert-blog/) names the author above each title. Its 221 posts gave 5 emerging voices, including three dbt posts from May 2026.
- **inovex and Woodmark:** the [inovex blog search](https://www.inovex.de/wp-json/wp/v2/posts?search=dbt) and the [Woodmark sitemap](https://www.woodmark.de/sitemap.xml) gave 4 more authors.
- **GitHub:** a search of [dbt repositories](https://github.com/search?q=topic%3Adbt&type=repositories) with Munich or Bavaria owners found 7 people with public dbt projects.
- **No dbt content:** the Medium feeds of Personio, Celonis, FlixBus, Sixt, BMW, Allianz and others were empty or inactive. [dev.to](https://dev.to/t/dbt) had 231 dbt authors, none in Munich.

### Step 4: Women-in-data communities

- **[WiDS Munich](https://widsmunich.de/):** its team and 2025 speakers are mostly academic or machine learning. They are useful as organiser contacts at Sixt, LMU and BR.
- **[AWS Women's User Group Munich](https://www.meetup.com/aws-womens-user-group-munich/):** its founder at BMW gave a query-performance talk.
- **[PyLadies Munich](https://www.meetup.com/pyladiesmunich/events/?type=past):** quarterly talk nights, mostly Python and machine learning.
- **Dormant:** [Munich WiMLDS](https://www.meetup.com/munich-women-in-machine-learning-and-data-science/), with no events since 2021.
- **Rule:** speakers were taken only from the communities' own events. No one's gender is recorded or guessed.

### Step 5: Job ads

- **LinkedIn Jobs, logged out:** a search for dbt around Munich. Up to 150 ads were checked for the whole word "dbt". 24 ads at 18 companies mention it.
- **Who is hiring:** adesso posted 6 ads and JobRad 2. Personio, AutoScout24, Octopus Energy and E.ON posted one each.

### Step 6: Location pass

- **Method:** each person's base was looked up on public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
- **Best sources:** meetup.com RSVP lists for the 10 Munich events, and company legal-notice and office pages.
- **Result:** 18 people were placed, 10 in the region and 8 elsewhere. Unknown locations fell from 40 to 22.

### Step 7: LinkedIn pass

- **Method:** one or two LinkedIn searches per person, using search results only. No LinkedIn page was opened.
- **Who:** the 14 tier-1 emerging voices without a location, plus Jorrit Posor.
- **Result:** 5 people were placed. Jorrit Posor is in Munich. Marvin Klossek, Simon Bachstein, Milan Wenske and Saskia Kutz are outside. 17 locations are still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **The Snowflake user group** is where Munich's dbt activity sits. Its event API and Bevy pages list speakers and hosts without a browser.
  - **Munich Datageeks write-ups** name speakers and topics, and the talks are recorded.
  - **b.telligent and synvert blogs** name an author on every post. They were the best source of first-time speakers, though neither states an office.
  - **GitHub search on dbt repositories** found practitioners at Databricks, ZEISS and OMMAX that no blog or agenda lists.
  - **meetup.com's `gql2` endpoint** answers plain requests, so every data group's past line-ups could be pulled in one pass.
- **Sources that didn't:**
  - **Company blogs** name almost no dbt authors. Check community recordings first.
  - **Medium feeds and dev.to** gave nothing local.
  - **Web search** ran out after 9 searches in the extension run.
- **Watch out for:**
  - **One venue cluster dominates.** Synabi and b.telligent share a site and hosted most chapter events. b.telligent people make up a large share of the leads.
  - **Tier 1 is generous here.** 9 of the 20 tier-1 people have no item that mentions dbt. Most are consultancy authors.
  - **Name spellings:** Matthias Nohl is "Mathias Nohl" on the event listing.
  - **Guessed details:** the mohrstade founders' titles come from the company name. Qing Ye's and Cassio Bolba's employers come from short GitHub fields ("IFX" and "HSE").
  - **Shared with the Rhein-Ruhr file:** Mathias Heinze and Benedikt Buchert appear in both. This file places Mathias Heinze in Munich, on a name match only.

## 3. Key leads

- **First-time speakers:**
  - **Mathias Heinze**, b.telligent: [Adding the E to dbt: extracting source systems with dbt Core and Snowflake](https://www.btelligent.com/en/blog/extracting-source-systems-dbt-core-snowflake) (August 2026).
  - **Marcin Wojtyczka**, Databricks, Munich: maintains [databricks-dbt-factory](https://github.com/mwojtyczka/databricks-dbt-factory), which turns dbt projects into Databricks workflows.
  - **Moritz Koerber**, ZEISS, Munich: [a local data stack project](https://github.com/moritzkoerber/local-data-stack) (2026).
  - **Almuth Hattwich**, Woodmark: [is dbt the right ELT tool for you? 10 considerations](https://www.woodmark.de/de/data-ai/datenengineering-datentransformation/blog-detail/eignet-sich-dbt-fuer-ihr-unternehmen) (October 2024).
  - **Cassio Bolba**, Munich: [an Airflow, dbt and Snowflake proof of concept](https://github.com/cassiobolba/airflow-dbt-snowflake-poc) (2024).
- **Anchor speakers:**
  - **Patricia Goldberg**, Wemolo: [automating BI tools with Pydantic and Python](https://www.munich-datageeks.de/talk-from-chaos-to-control-automating-bi-tools-with-pydantic-and-python/) at Munich Datageeks (February 2026). This is the strongest local dbt practitioner lead.
  - **Labib Mansour**, CELUS: [using dbt to fuel data-driven decisions](https://www.meetup.com/kaggle-munich/events/301271537/) at Kaggle Munich (June 2024).
  - **Christopher Gutknecht**, Bergzeit: [how Bergzeit manages 2,000+ dbt tests](https://www.meetup.com/munich-dbt-meetup/events/308060144/) at the chapter (July 2025).
  - **Christian Eberhardt**, b.telligent: [how dbt saved the day on a toxic join issue](https://www.meetup.com/munich-dbt-meetup/events/312785951/) at the chapter (February 2026).
- **Connectors:**
  - **Mathias Höreth**, b.telligent: organises and hosts the [Munich Snowflake User Group](https://usergroups.snowflake.com/events/details/snowflake-munich-presents-snowflake-amp-dbt-user-group-meeting-in-munich/). One contact can unlock venue, co-host and speakers.
  - **Manuel Ifland**, synvert: co-organises the [Snowflake user group](https://www.meetup.com/munich-snowflake-data-cloud-meetup-group/events/313614650/), and synvert hosted its April 2026 event.
  - **Stephanie Thiemichen** and **Torsten Schön**: board of [Munich Datageeks](https://www.munich-datageeks.de/), the largest local data meetup.
  - **Christian Kaul**, virtual7: runs the [Data Modeling Meetup Munich](https://www.meetup.com/data-modeling-dm3/).
  - **Marcus Stade** and **Patrick Mohr**, mohrstade: co-host [Analytics Pioneers Munich](https://www.meetup.com/analytics-pioneers-munich/).
  - **Meyyar Palaniappan**, BMW Group: founder of [AWS Women's User Group Munich](https://www.meetup.com/aws-womens-user-group-munich/).

## 4. Before outreach

- [ ] **Check tier-1 consultancy authors for dbt.** 9 of the 20 have never written about dbt.
- [ ] **Confirm each b.telligent, synvert, inovex and Woodmark author's office.** None of the author boxes states a city.
- [ ] **Check the name-only matches.** Thomas Lindner and Mathias Heinze are placed in Munich from a Meetup profile with a matching name only.
- [ ] **Decide on borderline locations.** Bergzeit's office is in Otterfing, about 25 km south of Munich. Athar Nawaz is in Ingolstadt, about 70 km away.
- [ ] **Check stale roles.** Helena Steurer's and Stephanie Hubert's Bergzeit roles date from 2022. Jorrit Posor has left FINN.
- [ ] **Exclude dbt Labs staff** from speaker outreach: Stephan Durry.

## 5. Next run

- **People still without a location:** 17.
  - Searched once on LinkedIn, no match: Benita Zeug, John Held, Lennart Werner, Viola Oduola, Giuliano Gaub, Hiroshi Hamano, Almuth Hattwich, Niels Warnecke, Tobias Walter and Kimia Karamzadeh.
  - Never searched on LinkedIn: Christopher Gutknecht, Michal Lapinski, Pradeep Srikakolapu, Tim Hiebenthal, Allan Mitchell, Geethu Uday and Polina Galkin.
- **Speakers left out** because their event pages name no employer: Martin Worzalla, Jan Behnke and Aychin Gasimov (Snowflake user group, May 2025), Daniel Schmidt and Beatrix Stade (Analytics Pioneers), and Annalena Wiesheu and Miriam Deml (AWS Women's User Group).
- **What to try first:** LinkedIn searches for the 7 people never searched there, starting with Christopher Gutknecht. Then read the November 2025 chapter event through `gql2`, since it has no talks on record.

## 6. Replication prompt

````
You are extending the Munich dbt dataset: munich/munich_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. The region is the Munich metro area.
Read munich/SEARCH_METHOD.md first, then research/README.md and the briefs it links
(raw-format.md, location-task.md, linkedin-task.md).

Budget about 25 web searches. Prefer direct fetches and APIs.

1. New talks: the Munich dbt Meetup, Munich Snowflake User Group (its event API), Munich
   Datageeks, Kaggle Munich and Analytics Pioneers, through the meetup.com gql2 endpoint.
2. New posts: the b.telligent and synvert blogs (sitemaps plus author lines), inovex and
   Woodmark. Then GitHub dbt repositories with Munich or Bavaria owners.
3. Women-in-data: new WiDS Munich, AWS Women's User Group and PyLadies Munich events. Take
   speakers only from the community's own events.
4. Locations: the 7 never-searched people listed in SEARCH_METHOD.md §5.
Rules: never open LinkedIn pages, use only search results. Record professional information
only, never gender, and pronouns only when self-stated. Assemble with research/assemble.py
--base, apply locations with research/apply_locations.py, and run research/validate.py.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build, from one research pass and a LinkedIn Jobs scan. 52 companies, 32 people and 24 dbt job ads at 18 companies. 25 proven speakers, 6 featured and 1 emerging voice. 16 people had spoken at the chapter. 11 people had LinkedIn profiles. |
| 2026-10-01 | 2 | Extension run through meetup.com, the Snowflake user group API, consultancy blogs and GitHub. 41 people and 13 companies added, for 73 people and 65 companies. Emerging voices rose from 1 to 23. Tier 1 rose from 1 to 20. |
| 2026-10-01 | 2 | Location pass from public pages. 18 people placed: 10 in the region and 8 elsewhere. Unknown locations fell from 40 to 22. |
| 2026-10-01 | 2 | LinkedIn pass on 15 people. 5 placed: 1 in the region and 4 elsewhere. 17 locations are still unknown, and 16 people now have LinkedIn profiles. |
