# Munich: city notes

This file holds what is specific to Munich. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Munich dbt Meetup](https://www.meetup.com/munich-dbt-meetup/), data in `munich_dbt_companies.json`
- **Region:** the Munich metro area. Ingolstadt and Haar count as local. Karlsruhe, Ulm, Würzburg and Zürich are outside.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 4, 2026-10-01)

| | Count |
|---|---|
| Companies | 78 |
| People | 89 |
| Tier 1 leads | 20 |
| First-time speakers (publish, no talk yet) | 23 |
| Proven speakers | 51 |
| Spoke at this chapter before | 16 |
| Based in the region | 59 |
| Based elsewhere | 16 |
| Location unknown | 14 |
| With a LinkedIn profile | 60 |
| Job ads mentioning dbt | 34 |
| Past chapter meetups | 7 |
<!-- at-a-glance:end -->

## 1. Where to look in Munich

### Chapter history

- **Chapter events:** 7 events from April 2023 to February 2026. Most were held at [Synabi](https://synabi.com/en/events/) in Munich. One was at Daiichi Sankyo in July 2025. They gave 16 past speakers, added from `../enriched/munich-dbt-meetup.json`. The November 2025 event has no talks on record.

### Meetups and conferences

- **[Munich Snowflake User Group](https://www.meetup.com/munich-snowflake-data-cloud-meetup-group/):** the richest dbt-adjacent source, and where Munich's dbt activity sits. It ran a joint [Snowflake & dbt evening](https://usergroups.snowflake.com/events/details/snowflake-munich-presents-snowflake-amp-dbt-user-group-meeting-in-munich/) at Synabi in February 2025. The user group's own [event API](https://usergroups.snowflake.com/api/event/?chapter=143) lists all 10 of its events. The API and the Bevy event pages list speakers and hosts without a browser.
- **[Munich Datageeks](https://www.munich-datageeks.de/tag/talks/):** its write-ups name speakers and topics, and the talks are recorded. They gave the strongest dbt practitioner lead. Its [meetup.com events](https://www.meetup.com/munich-datageeks/events/?type=past) added data-engineering speakers from E.ON, Finanz Informatik, Lakekeeper, Firebolt and Aiven.
- **Group search:** a meetup.com search around Munich listed about 60 data groups. The past events of 20 were read and searched for dbt.
- **Smaller groups with a dbt talk:** [Kaggle Munich](https://www.meetup.com/kaggle-munich/events/?type=past) hosted a dbt talk in June 2024. [Analytics Pioneers Munich](https://www.meetup.com/analytics-pioneers-munich/events/?type=past) ran dbt trainings in 2022 and 2024.

### Company blogs

- **b.telligent:** the [blog](https://www.btelligent.com/en/blog) names an author on every post. Its 211 posts gave 6 emerging voices. Its [dbt partner page](https://www.btelligent.com/en/partner/dbt) names two contacts.
- **synvert:** the [blog](https://synvert.com/de-de/synvert-blog/) names the author above each title. Its 221 posts gave 5 emerging voices, including three dbt posts from May 2026.
- **inovex and Woodmark:** the [inovex blog search](https://www.inovex.de/wp-json/wp/v2/posts?search=dbt) and the [Woodmark sitemap](https://www.woodmark.de/sitemap.xml) gave 4 more authors.
- **GitHub:** a search of [dbt repositories](https://github.com/search?q=topic%3Adbt&type=repositories) with Munich or Bavaria owners found 7 people with public dbt projects. It found practitioners at Databricks, ZEISS and OMMAX that no blog or agenda lists.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[WiDS Munich](https://widsmunich.de/):** its team and 2025 speakers are mostly academic or machine learning. They are useful as organiser contacts at Sixt, LMU and BR.
  - **[2024 agenda](https://sites.google.com/view/widsmunich/past-events/wids-2024/agenda):** it names speakers with employer and talk title. The event was held at Bayerischer Rundfunk. It gave 5 people: Katharina Brunner (BR Data) on data in investigative journalism, Marie-Louise Timcke (head of the Süddeutsche Zeitung data department), Uli Köppen (BR), Ann-Kristin Vester (CorrelAid) and the moderator Leah von der Heyde (LMU).
  - **[2026 team](https://widsmunich.de/team/):** 12 people, mostly at LMU and TUM. Johanna Sommer (Pruna AI), Isabella Almstätter and Shan Huang (Munich Data Science Institute) and Helena Džakula (SOS Children's Villages) are recorded as connectors. The 2026 conference is on 11 December 2026 at LMU, and its speakers are not yet announced.
- **[AWS Women's User Group Munich](https://www.meetup.com/aws-womens-user-group-munich/):** its founder at BMW gave a query-performance talk. Its only other data talk was ["One Data Agent"](https://www.meetup.com/aws-womens-user-group-munich/events/311291873/) by Annalena Wiesheu and Miriam Deml (October 2025, at the BMW Future Lab). The page names no employer for them. The other talks since 2024 are about cloud, security, GenAI and careers.
- **[PyLadies Munich](https://www.meetup.com/pyladiesmunich/events/?type=past):** quarterly talk nights, mostly Python and machine learning. Two data talks: Patricia Goldberg (Wemolo) on [Python in data engineering](https://www.meetup.com/pyladiesmunich/events/304177482/) (November 2024), and Denise Hartmann (inovex) on [agents at inovexGPT](https://www.meetup.com/pyladiesmunich/events/311379318/) (November 2025). Meetup's event-host data names the organisers Laysa Uchoa (Nordcloud), Yulia Barabash and Daryna Dementieva. They are connectors.
- **[Women Techmakers Munich](https://gdg.community.dev/e/m95dgx/):** its only recent event was a brunch at DevFest Munich 2023. Its host, Aiman Saeed, is a connector.
- **Also ask:** data leads at dbt companies to suggest people on their teams.

### Job ads

- **LinkedIn Jobs:** a search for dbt around Munich. 24 ads at 18 companies mention dbt. adesso posted 6 ads and JobRad 2. Personio, AutoScout24, Octopus Energy and E.ON posted one each.
- **Company job boards:** the open Greenhouse, Lever and Ashby job APIs (`boards-api.greenhouse.io/v1/boards/<slug>/jobs?content=true`, `api.lever.co/v0/postings/<slug>?mode=json`, `api.ashbyhq.com/posting-api/job-board/<slug>`) return the full ad text, so one call per company checks for the whole word dbt and the location. Flix, Yazio, Helsing, Holidu, AutoScout24 and FINN have Munich or Germany ads that mention dbt.
- **[arbeitnow.com API](https://www.arbeitnow.com/api/job-board-api):** `?page=N` returns German job ads with full text. 14 pages (1,851 ads) were read before it returned HTTP 429. It added Reev and confirmed Flix and Holidu ads in Munich.
- **HN Who is hiring:** the Algolia search for "dbt munich" gave Return, which has a Munich office.
- **[dbt Labs case studies](https://www.getdbt.com/sitemap-0.xml):** the sitemap lists 61 `/case-studies/` pages. Each page states the company headquarters. The [Siemens case study](https://www.getdbt.com/case-studies/siemens) raised Siemens to strong.
- **[Munich Snowflake User Group](https://www.meetup.com/munich-snowflake-data-cloud-meetup-group/events/?type=past) and [Analytics Pioneers Munich](https://www.meetup.com/analytics-pioneers-munich/events/?type=past) on Meetup gql2:** a February 2025 dbt talk by Project A Ventures and a May 2024 dbt training by the mohrstade founders raised both to strong.

### Locations

- **meetup.com RSVP lists:** the RSVP lists for the 10 Munich events were the best location source.
- **Company legal-notice and office pages:** the second-best location source.
- **LinkedIn search results:** the 14 tier-1 emerging voices without a location were searched, plus Jorrit Posor. Jorrit Posor was placed in Munich. Marvin Klossek, Simon Bachstein, Milan Wenske and Saskia Kutz were placed outside.

## 2. What didn't work here

- **Chapter past events page:** the [past events page](https://www.meetup.com/munich-dbt-meetup/events/?type=past) renders in the browser only, so a plain fetch returned nothing.
- **Company blogs:** they name almost no dbt authors. Check community recordings first.
- **Medium feeds:** the feeds of Personio, Celonis, FlixBus, Sixt, BMW, Allianz and others were empty or inactive.
- **dev.to:** the [dbt tag](https://dev.to/t/dbt) had 231 dbt authors, none in Munich.
- **Low-yield meetups and conferences:** [Data Modeling Meetup Munich](https://www.meetup.com/data-modeling-dm3/) (speakers are international and online), [PyData Munich](https://www.meetup.com/pydata-munchen/events/?type=past) (GenAI only), the [TDWI conference programme](https://www.tdwi-konferenz.de/de/programm/konferenzprogramm), [PyCon DE](https://pretalx.com/pyconde-pydata-2026/schedule/) and the [Munich Database Meetup](https://munichdatabases.xyz/).
- **Dormant women-in-data groups:** [Munich WiMLDS](https://www.meetup.com/munich-women-in-machine-learning-and-data-science/) has had no events since 2021. [Google Women Techmakers Munich](https://www.meetup.com/Google-Women-in-Technology-Munchen/) on Meetup has had none since 2023.
- **Other women-in-data networks:** Meetup's group search found no R-Ladies, Women in Big Data or She Loves Data group near Munich. Two new groups, the [Data & Digital Skills Study Club](https://www.meetup.com/data-digital-skills-study-club/) and Women thinktank, had no talks. [Women on Snowflake](https://usergroups.snowflake.com/women-on-snowflake/) has held no Munich event.
- **GitHub code search:** `filename:dbt_project.yml org:<org>` found no public dbt project in the orgs tried. The search rate limit cut several calls short. Orgs tried: Celonis, Personio, Holidu, Flix and Scalable Capital.
- **Job boards with no Munich dbt ad:** Celonis, Sixt, IDnow, EGYM, Parloa, NavVis, Wemolo and Personio have no Munich ad that mentions dbt. Scalable Capital, Trade Republic, tado and Freeletics have no open Greenhouse, Lever or Ashby board.
- **Munich Datageeks venues:** the 2024–26 hosts (PAYBACK, KPMG, Allianz, E.ON, Celonis, BSH, QAware, Netlight, JetBrains) show local presence only. No event text mentions dbt.

## 3. Companies looked at

- **One venue cluster dominates.** Synabi and b.telligent share a site and hosted most chapter events. b.telligent people make up a large share of the leads.
- **Consultancy blogs give most first-time speakers.** b.telligent and synvert name an author on every post, but neither states an office.

<!-- companies:start -->
77 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (11)</summary>

b.telligent, CELUS, Databricks (local presence not confirmed), FINN (local presence not confirmed), FlixMobility, inovex (local presence not confirmed), mohrstade, Project A Ventures (local presence not confirmed), Siemens AG, Wemolo (VMO), Yazio

</details>

<details><summary><b>Some dbt signal</b> (27)</summary>

4flow, adesso SE, Agoda, AutoScout24, Celonis, codecentric AG, Daiichi Sankyo, E.ON Deutschland, Eraneos, EY, Helsing, Holidu, INFOMOTION GmbH, JobRad Deutschland, Kartenliebe GmbH, Munich Snowflake User Group (MSUG), myposter GmbH, Octopus Energy, Personio, Return, Skalar – Digitale Steuerberatung, Synabi Business Solutions GmbH, Trade Republic (local presence not confirmed), Verlag C.H.Beck, Woodmark Consulting, x1F, ZEISS (local presence not confirmed)

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

Reev

</details>

<details><summary><b>Not verified</b> (37)</summary>

Bayerischer Rundfunk (BR Data / BR Recherche) (local presence not confirmed), Bergzeit (local presence not confirmed), BMW Group, CorrelAid (local presence not confirmed), Data Modeling Meetup Munich (DM3), dbt Labs (local presence not confirmed), Finanz Informatik (local presence not confirmed), Firebolt (local presence not confirmed), Frontify (local presence not confirmed), Hochschule München (Munich University of Applied Sciences) (local presence not confirmed), HSE (local presence not confirmed), IDEX.Q (local presence not confirmed), In516ht (local presence not confirmed), Infineon Technologies (local presence not confirmed), Lakekeeper (Vakamo) (local presence not confirmed), LMU Munich (Social Data Science and AI Lab) (local presence not confirmed), Microsoft Fabric (local presence not confirmed), Munich Data Science Institute (TUM) (local presence not confirmed), Munich Database Meetup, Munich Datageeks e.V., Nordcloud (local presence not confirmed), OMMAX (local presence not confirmed), Pruna AI (local presence not confirmed), PyLadies Munich (local presence not confirmed), SAP (local presence not confirmed), Scalable Capital, SIXT SE (local presence not confirmed), Snowflake (local presence not confirmed), SOS Children's Villages (local presence not confirmed), Sundeck (local presence not confirmed), SVA System Vertrieb Alexander (local presence not confirmed), synvert (synvert Data Insights), Süddeutsche Zeitung (local presence not confirmed), Technische Hochschule Ingolstadt (local presence not confirmed), Unstated employer (Munich) (local presence not confirmed), virtual7 GmbH (local presence not confirmed), Women in Data Science (WiDS) Munich

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

Aiven (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (12)</summary>

- https://medium.com/@holidu
- https://medium.com/inside-personio/all?topic=engineering
- https://munichdatabases.xyz/
- https://sites.google.com/view/widsmunich/past-events/wids-2025/speakers-2025
- https://synabi.com/en/events/
- https://widsmunich.de/
- https://widsmunich.de/team/
- https://www.meetup.com/data-modeling-dm3/
- https://www.meetup.com/munich-snowflake-data-cloud-meetup-group/
- https://www.munich-datageeks.de/tag/talks/
- https://www.munich-datageeks.de/tag/talks/page/2/
- https://www.munich-datageeks.de/tag/talks/page/3/

</details>

<details><summary><b>Other sources checked</b> (44)</summary>

- [Munich Datageeks talks (pages 1-3)](https://www.munich-datageeks.de/tag/talks/)
- [Snowflake UG Munich - Snowflake & dbt meeting Feb 2025](https://usergroups.snowflake.com/events/details/snowflake-munich-presents-snowflake-amp-dbt-user-group-meeting-in-munich/)
- [Munich Snowflake Data Cloud Meetup Group](https://www.meetup.com/munich-snowflake-data-cloud-meetup-group/)
- [Munich dbt Meetup past events](https://www.meetup.com/munich-dbt-meetup/events/?type=past) (nothing useful)
- [Data Modeling Meetup Munich (DM3)](https://www.meetup.com/data-modeling-dm3/)
- [Data Engineering Munich meetup](https://www.meetup.com/data-engineering/) (nothing useful)
- [Munich WiMLDS meetup](https://www.meetup.com/munich-women-in-machine-learning-and-data-science/) (nothing useful)
- [PyLadies Munich meetup](https://www.meetup.com/pyladies-munich/) (nothing useful)
- [WiDS Munich site, team and 2025 speakers](https://widsmunich.de/)
- [MCML WiDS 2025 event page](https://mcml.ai/events/2025-10-21-women-in-data-science-conference/)
- [TDWI München conference programme](https://www.tdwi-konferenz.de/de/programm/konferenzprogramm) (nothing useful)
- [b.telligent dbt partner page](https://www.btelligent.com/en/partner/dbt)
- [Holidu Tech Blog (Medium)](https://medium.com/@holidu) (nothing useful)
- [Inside Personio (Medium) engineering](https://medium.com/inside-personio/all?topic=engineering) (nothing useful)
- [Synabi events page](https://synabi.com/en/events/) (nothing useful)
- [Munich Database Meetup](https://munichdatabases.xyz/) (nothing useful)
- [Coalesce 2025 / dbt Summit 2026 speaker searches](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/speakers) (nothing useful)
- [LinkedIn Jobs guest API (keywords=dbt, Munich-area)](https://www.linkedin.com/jobs/search?keywords=dbt)
- [Meetup gql2 groupSearch near Munich](https://www.meetup.com/gql2)
- [Kaggle Munich past events](https://www.meetup.com/kaggle-munich/events/?type=past)
- [Analytics Pioneers Munich past events](https://www.meetup.com/analytics-pioneers-munich/events/?type=past)
- [Munich Datageeks meetup.com events 2024-2026 (full text)](https://www.meetup.com/munich-datageeks/events/?type=past)
- [PyLadies Munich past events](https://www.meetup.com/pyladiesmunich/events/?type=past)
- [AWS Women's User Group Munich](https://www.meetup.com/aws-womens-user-group-munich/)
- [PyData Munich past events](https://www.meetup.com/pydata-munchen/events/?type=past) (nothing useful)
- [Snowflake UG Munich, Bevy API (all 10 events)](https://usergroups.snowflake.com/api/event/?chapter=143)
- [b.telligent blog (sitemap, 211 posts)](https://www.btelligent.com/en/blog)
- [synvert blog (sitemap, 221 German posts)](https://synvert.com/de-de/synvert-blog/)
- [inovex blog WordPress API search=dbt](https://www.inovex.de/wp-json/wp/v2/posts?search=dbt)
- [Woodmark blog sitemap](https://www.woodmark.de/sitemap.xml)
- [GitHub GraphQL: dbt repos with Munich/Bavaria owners](https://github.com/search?q=topic%3Adbt&type=repositories)
- [dev.to dbt and analytics engineering authors](https://dev.to/t/dbt) (nothing useful)
- [Medium feeds: inside-personio, celonis-engineering, others](https://medium.com/feed/celonis-engineering) (nothing useful)
- [Data Engineering Munich (data-engineering-muc)](https://www.meetup.com/data-engineering-muc/) (nothing useful)
- [Munich Open Source Data Infrastructure Meetup](https://www.meetup.com/munich-open-source-data-infrastructure-meetup/) (nothing useful)
- [PyCon DE & PyData 2025/2026 schedules (pretalx export)](https://pretalx.com/pyconde-pydata-2026/schedule/) (nothing useful)
- [dbt developer blog authors.yml](https://github.com/dbt-labs/docs.getdbt.com/blob/current/website/blog/authors.yml) (nothing useful)
- [PyLadies Munich past events and hosts (Meetup gql2)](https://www.meetup.com/pyladiesmunich/)
- [WiDS Munich 2024 speakers and agenda](https://sites.google.com/view/widsmunich/past-events/wids-2024/agenda)
- [WiDS Munich 2026 event and team](https://widsmunich.de/team/)
- [Google Women Techmakers Munich (Meetup gql2)](https://www.meetup.com/Google-Women-in-Technology-Munchen/) (nothing useful)
- [GDG Cloud Munich events API (Women Techmakers)](https://gdg.community.dev/gdg-cloud-munich/)
- [Data & Digital Skills Study Club and Women thinktank (Meetup gql2)](https://www.meetup.com/data-digital-skills-study-club/) (nothing useful)
- [Women on Snowflake events](https://usergroups.snowflake.com/women-on-snowflake/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

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

## 5. Before outreach

- [ ] **Check tier-1 consultancy authors for dbt.** 9 of the 20 tier-1 people have no item that mentions dbt. Most are consultancy authors.
- [ ] **Confirm each b.telligent, synvert, inovex and Woodmark author's office.** None of the author boxes states a city.
- [ ] **Check the name-only matches.** Thomas Lindner and Mathias Heinze are placed in Munich from a Meetup profile with a matching name only.
- [ ] **Check the duplicates with the Rhein-Ruhr file.** Mathias Heinze and Benedikt Buchert appear in both files.
- [ ] **Match both spellings of Matthias Nohl.** The event listing spells the name "Mathias Nohl".
- [ ] **Check guessed details.** The mohrstade founders' titles come from the company name. Qing Ye's and Cassio Bolba's employers come from short GitHub fields ("IFX" and "HSE").
- [ ] **Decide on borderline locations.** Bergzeit's office is in Otterfing, about 25 km south of Munich. Athar Nawaz is in Ingolstadt, about 70 km away.
- [ ] **Check stale roles.** Helena Steurer's and Stephanie Hubert's Bergzeit roles date from 2022. Jorrit Posor has left FINN.
- [ ] **dbt Labs staff are labelled.** Stephan Durry works there. Stephan Durry can speak, but check the line-up has practitioners first.

## 6. Next run

- **Sources to try first:**
  - **November 2025 chapter event:** read it through meetup.com, since it has no talks on record.
  - **Community events:** new events of the Munich dbt Meetup, Munich Snowflake User Group (through its event API), Munich Datageeks, Kaggle Munich, Analytics Pioneers, WiDS Munich, AWS Women's User Group and PyLadies Munich.
  - **Blogs:** new posts on the b.telligent and synvert blogs (sitemaps plus author lines), inovex and Woodmark. Then GitHub dbt repositories with Munich or Bavaria owners.
  - **Speakers left out:** their event pages name no employer. They are Martin Worzalla, Jan Behnke and Aychin Gasimov (Snowflake user group, May 2025), and Daniel Schmidt and Beatrix Stade (Analytics Pioneers). Annalena Wiesheu and Miriam Deml (AWS Women's User Group) are now recorded under an unstated employer.
- **Women-in-data communities not yet reachable:**
  - **WiDS Munich 2026:** read the speakers and workshop hosts when they are announced, before the 11 December 2026 conference.
  - **WiDS Munich 2023:** its [speaker page](https://sites.google.com/view/widsmunich/past-events/WiDS-2023/speakers-2023) was not read.
  - **Women Techmakers Munich:** ask Aiman Saeed whether the group still runs events.
  - **R-Ladies, Women in Big Data, Girls in Tech and She Loves Data:** no Munich chapter or event was found.
- **People from the women-in-data pass:** the 16 people added have no LinkedIn search. Annalena Wiesheu and Miriam Deml have no employer on record.
- **People to locate:** 17 people have no known location.
  - **Searched once on LinkedIn, no match:** Benita Zeug, John Held, Lennart Werner, Viola Oduola, Giuliano Gaub, Hiroshi Hamano, Almuth Hattwich, Niels Warnecke, Tobias Walter and Kimia Karamzadeh.
  - **Never searched on LinkedIn:** Christopher Gutknecht, Michal Lapinski, Pradeep Srikakolapu, Tim Hiebenthal, Allan Mitchell, Geethu Uday and Polina Galkin. Start with Christopher Gutknecht.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `munich/munich_dbt_companies.json`, the Munich dbt Meetup, `../enriched/munich-dbt-meetup.json` and the region above. Add: "Use the Munich Snowflake User Group event API for its line-ups."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build, from one research pass and a LinkedIn Jobs scan. 52 companies, 32 people and 24 dbt job ads at 18 companies. 25 proven speakers, 6 featured and 1 emerging voice. 16 people had spoken at the chapter. 11 people had LinkedIn profiles. |
| 2026-10-01 | 2 | Extension run through meetup.com, the Snowflake user group API, consultancy blogs and GitHub. 41 people and 13 companies added, for 73 people and 65 companies. Emerging voices rose from 1 to 23. Tier 1 rose from 1 to 20. |
| 2026-10-01 | 2 | Location pass from public pages. 18 people placed: 10 in the region and 8 elsewhere. Unknown locations fell from 40 to 22. |
| 2026-10-01 | 2 | LinkedIn pass on 15 people. 5 placed: 1 in the region and 4 elsewhere. 17 locations are still unknown, and 16 people now have LinkedIn profiles. |
| 2026-10-01 | 3 | Women-in-data pass. Checked WiDS Munich (2024 agenda and 2026 team), AWS Women's User Group Munich, PyLadies Munich (past events and hosts), Women Techmakers Munich (through Meetup and GDG Cloud Munich), two new Meetup groups and Women on Snowflake. Added 16 people with `sourced_via: women_in_data_community`: 7 speakers and 9 organisers as connectors. Added a talk to Patricia Goldberg. Added community channels for the WiDS Munich 2024 agenda, Google Women Techmakers Munich and GDG Cloud Munich. |
| 2026-10-01 | 4 | Company pass from open job boards (Greenhouse, Lever, Ashby, arbeitnow), HN Who is hiring, dbt Labs case studies and Meetup gql2 line-ups. 5 companies added, for 78. 2 of them have a strong dbt signal: FlixMobility and Yazio. 4 companies raised to strong: Siemens AG, FINN, Project A Ventures and mohrstade. People are unchanged. |
