# Düsseldorf: city notes

This file holds what is specific to Düsseldorf and the Rhein-Ruhr area. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Rhein-Ruhr dbt Meetup](https://www.meetup.com/rhein-ruhr-dbt-meetup/), data in `dusseldorf_dbt_companies.json`
- **Region:** Düsseldorf, Cologne, Essen, Dortmund, Bonn and nearby towns. Commuter towns count as local, so Münster is in the region. Leipzig is outside.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 4, 2026-10-01)

| | Count |
|---|---|
| Companies | 78 |
| People | 87 |
| Tier 1 leads | 22 |
| First-time speakers (publish, no talk yet) | 20 |
| Proven speakers | 53 |
| Spoke at this chapter before | 5 |
| Based in the region | 47 |
| Based elsewhere | 10 |
| Location unknown | 30 |
| With a LinkedIn profile | 41 |
| Job ads mentioning dbt | 54 |
| Past chapter meetups | 2 |
<!-- at-a-glance:end -->

## 1. Where to look in Düsseldorf

### Chapter history

- **Chapter events:** the chapter has held two in-person events, both in Cologne. The first was on 2024-12-05 at [adesso](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/304543797/). The second was on 2025-05-15 at [taod](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/307198615/). They gave 5 past speakers, added from `../enriched/rhein-ruhr-dbt-meetup.json`. The meetup.com event pages also gave full agendas and organiser names. The chapter has had no events since May 2025.

### Meetups and conferences

- **Databricks User Group Rhein-Ruhr:** the [group](https://www.meetup.com/databricks-user-group-rhein-ruhr/) gave the most local data-platform speakers. They work at Deichmann, Handelsblatt, BarmeniaGothaer and FIEGE.
- **Microsoft data community:** [Data Saturday Rheinland](https://datasaturdays.com/Event/20260711-datasaturday0084) (2025 and 2026) lists about 60 sessions. Its Sessionize embeds give speaker names and taglines. The [Data Platform Usergroup Rheinland](https://www.meetup.com/pass-microsoft-data-platform-usergroup-rheinland/) and [Datamonsters Ruhrgebiet](https://www.meetup.com/pass-germany-regional-group-ruhrgebiet/) added more. Most talks are on the Microsoft stack, and many speakers come from outside the region.
- **Smaller meetups:** the [trivago Tech, Data & Product meetup](https://www.meetup.com/trivago-tech-data-product/) ran a data-platform evening in August 2025. [Engineering Kiosk Rhine-Ruhr](https://www.meetup.com/engineering-kiosk-rhine-ruhr/), [Data Analytics & AI Köln](https://www.meetup.com/data-analytics-ai-koeln/) and the [Power Platform & Fabric User Group Cologne](https://www.meetup.com/power-platform-ug-cologne/) each added a few speakers.
- **Online trainings:** [Analytics Pioneers](https://www.meetup.com/analytics-pioneers-dusseldorf/) ran a dbt modelling course in May 2024. Its organisers are in Munich.
- **Group search:** a meetup.com search around the Rhein-Ruhr centre listed about 120 local groups. The past events of 20 data groups were read.

### Company blogs

- **adesso:** the [blog feed](https://www.adesso.de/de/news/blog/blog-rss.xml) and each post's author box gave 9 emerging voices. The author boxes give name and role, but rarely the office. Only two adesso posts mention dbt.
- **ORAYLIS:** the [blog feed](https://www.oraylis.de/feed) gave 6 emerging voices. The posts cover Microsoft Fabric and Databricks, not dbt.
- **b.telligent:** the [blog](https://www.btelligent.com/en/blog) has one dbt post, from August 2026.
- **GitHub:** a user search by NRW city found 3 people with their own dbt projects.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[Women in Big Data NRW](https://www.meetup.com/women-in-big-data-nrw/):** the best source. Its 2023 and 2024 event descriptions name speakers with employer and talk title. They gave 11 speakers:
  - **[June 2023 at Picnic, Düsseldorf](https://www.meetup.com/women-in-big-data-nrw/events/293491997/):** Anna Maria Steffens (taod) on a data consultant's working day, Juliette Aucamp (Vodafone) on getting the business to adopt analytics, and Friederike Kulik (Picnic) on workforce planning.
  - **[November 2023, Düsseldorf](https://www.meetup.com/women-in-big-data-nrw/events/296624784/):** Angela Music-Siedler on building a BI department from scratch.
  - **[June 2024 at Thoughtworks, Cologne](https://www.meetup.com/women-in-big-data-nrw/events/301414751/):** Inna Zykova on ML platforms, and Eva Bledau (Volvo Car Deutschland) on vehicle data.
  - **[September 2024 at Point 8, Dortmund](https://www.meetup.com/women-in-big-data-nrw/events/301614472/):** Adrian Krug (Vaillant Group) on data architecture and data mesh, and Lena Linhoff and Vanessa Müller (Point 8) on data projects in mechanical engineering.
  - **[December 2024, Frankfurt](https://www.meetup.com/women-in-big-data-nrw/events/304321711/):** Philipp Szutta (ABN AMRO) on data warehouses in finance, and Laura Traverso (Slalom) on AI ethics. Both are outside the region.
  - **Since mid-2025:** the group runs "Data Dates" discussion evenings in Düsseldorf, on data quality, data bias and data skills, with no speakers.
  - **Hosts:** Meetup's event-host data names 4 more hosts besides Liisel Jessop: Corinna Meier, Olga Schneider, Anastasia Dobasis and Julia Kannenberg. They are connectors.
- **[Recap of the 2025 Thoughtworks evening](https://www.womeninbigdata.org/women-in-big-data-nrw-x-thoughtworks-event/):** it named two speakers and two hosts.
- **[Women in AI Cologne #3](https://www.ki.nrw/women-in-ai-cologne-meetup-3/):** one speaker, on AI transformation.
- **[Female Dev Club](https://www.meetup.com/female-dev-club/):** monthly talks in Düsseldorf, mostly on software and careers. A May 2023 SQL talk and a September 2026 data privacy talk don't name the speaker. Its organisers, Anna Maier and Jennifer Lucifero, are connectors.
- **[R-Ladies Cologne](https://www.meetup.com/rladies-cologne/):** online events, including a reproducible analytical pipelines book club (2023 to 2024) and R package workshops (2025). The speakers and both organisers, Cosima Meyer and Gabe Winter, are based outside the region.
- **Also ask:** data leads at dbt companies to suggest people on their teams.

### Job ads

- **LinkedIn Jobs:** a search for dbt around Düsseldorf and the Rhein-Ruhr area. 49 ads at 24 companies mention dbt. adesso posted 18 of the 49 ads. viadee and Redcare Pharmacy posted 4 each.
- **[dbt Labs case studies](https://www.getdbt.com/sitemap-0.xml):** the sitemap lists 61 `/case-studies/` pages. Each page states the company headquarters. The [DISH Digital Solutions case study](https://www.getdbt.com/case-studies/dish-digital-solutions) names Düsseldorf as headquarters and raised DISH to strong.
- **Personio job feeds:** `https://<company>.jobs.personio.de/xml` returns every open ad with full text. Scalefree has a Cologne "dbt Engineer" role, which raised it to strong.
- **[arbeitnow.com API](https://www.arbeitnow.com/api/job-board-api):** `?page=N` returns German job ads with full text. 14 pages (1,851 ads) were read before it returned HTTP 429. It added Real Digital and cbs Corporate Business Solutions (Dortmund), both with dbt as a plus, and a new METYCLE ad in Cologne.
- **Meetup gql2 venues:** Milestone Consult (Kamp-Lintfort) hosts most Datamonsters Ruhrgebiet meetings and prodot (Duisburg) runs its own data and Azure meetups. Both were added for local presence only.

### Locations

- **meetup.com RSVP and host lists:** the best location source here. They give the profile city of the person who spoke at that event.
- **LinkedIn search results:** the 15 tier-1 blog authors without a location were searched. Michael Peichl was placed in Leipzig, outside the region. Jonas Thiele was placed in Münster, which counts as local.

## 2. What didn't work here

- **Web search:** NRW dbt queries mostly returned job ads.
- **Medium and dev.to:** rate-limited, so no Medium or dev.to authors were scanned.
- **Snowflake user groups:** there is no NRW chapter. The Köln Snowflake and PyData Cologne-Bonn groups no longer exist.
- **Company blogs with no dbt content:** [trivago tech blog](https://tech.trivago.com/), [codecentric](https://www.codecentric.de/feed), [inovex](https://www.inovex.de/de/blog/?s=dbt), [areto](https://areto.de/blog/) and [datadice](https://www.datadice.io/en/blog/).
- **Large corporates:** REWE, METRO, Henkel and Vodafone publish nothing on dbt.
- **Women-in-data groups with no data speakers:** PyCologne, PyData Dortmund, inovex Cologne and [Women in Tech Köln](https://www.meetup.com/women-in-tech-koln/), which runs career workshops.
- **Women-in-data networks with no NRW chapter:** gdg.community.dev has no GDG chapter for Düsseldorf, Cologne, Essen, Dortmund or Bonn, so there is no Women Techmakers route. [PyLadies](https://pyladies.com/locations/) has no NRW chapter, and [Women on Snowflake](https://usergroups.snowflake.com/women-on-snowflake/) has held no NRW event. A new Cologne group, [Networking in IT und Tech von Frauen für Frauen](https://www.meetup.com/networking-im-umfeld-von-it-und-digitalisierung/), had no past events.
- **HN Who is hiring:** searches for dbt with Düsseldorf, Cologne, Essen, Dortmund, Bonn and NRW found no role placed in the region.
- **Company job boards:** trivago, DeepL, IONOS, StepStone, Gigs and FREE NOW have open boards, but no Rhein-Ruhr ad there mentions dbt. Douglas, REWE digital, METRO.digital, Henkel, ERGO and Ströer have no open Greenhouse, Lever or Ashby board.
- **Personio feeds with no dbt ad:** METYCLE and Schüttflix. taod, ORAYLIS, viadee, Infomotion and oh22 have no open Personio feed.
- **Meetup line-ups:** the trivago, Databricks User Group Rhein-Ruhr, Fabric Rhein-Ruhr, Datamonsters Ruhrgebiet and Data Analytics & AI Köln events since 2024 never mention dbt.

## 3. Companies looked at

- **taod hosts the chapter's latest event.** taod hosted the May 2025 event at its Cologne office and runs its own Cologne event series. adesso hosted the first event.
- **adesso dominates the leads.** It has 9 of the 20 emerging voices and 18 of the 49 job ads. Plan one speaker per company per event.
- **Consultancy authors rarely state an office.** That is why most tier-1 people have no known location.
- **Large NRW employers use a different stack.** REWE, METRO, Henkel and Vodafone show no public dbt use.

<!-- companies:start -->
77 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (8)</summary>

Analytics Pioneers (local presence not confirmed), b.telligent (local presence not confirmed), dbt Labs (local presence not confirmed), DISH Digital Solutions (METRO), Scalefree, Schüttflix (local presence not confirmed), taod Consulting, Xebia (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (24)</summary>

adesso SE, Agoda, AVS Verkehrssicherung GmbH, AXA, codecentric AG, Cognitive Group, DeepL, Deutsche Glasfaser Unternehmensgruppe, Douglas, E.ON Deutschland, EY, eye-level consulting GmbH, Founderful, Intersnack IT KG, Inverto / A BCG Company, ISR Information Products AG, Metycle, Redcare Pharmacy, REWE Group, ruhr.agency, SKOPOS, Thermengruppe Josef Wund, Trianel GmbH, viadee Unternehmensberatung AG

</details>

<details><summary><b>dbt as a nice-to-have</b> (2)</summary>

cbs Corporate Business Solutions, Real Digital

</details>

<details><summary><b>Not verified</b> (38)</summary>

ABN AMRO Bank (Frankfurt Branch) (local presence not confirmed), Accenture / intions (Essen Innovation Hub), ALDI SÜD, BarmeniaGothaer, Borussia Mönchengladbach, Data Natives Düsseldorf & Köln (local presence not confirmed), Databricks (local presence not confirmed), Databricks User Group Rhein-Ruhr, Deichmann SE, Düsseldorf Data Science Meetup, Female Dev Club (local presence not confirmed), FIEGE Logistik (local presence not confirmed), GDS Business Intelligence GmbH (local presence not confirmed), Handelsblatt Media Group, Infomotion, Milestone Consult, noventum consulting (local presence not confirmed), oh22data AG (local presence not confirmed), oh22information services GmbH, ORAYLIS, Picnic (local presence not confirmed), Point 8 (local presence not confirmed), prodot, PyMC Labs (local presence not confirmed), R-Ladies Cologne (local presence not confirmed), REWE digital, Slalom (local presence not confirmed), StepStone, SumUp (local presence not confirmed), teccle group (local presence not confirmed), Thoughtworks (Cologne), trivago, Unstated employer (Rhein-Ruhr) (local presence not confirmed), Vaillant Group (local presence not confirmed), Vodafone (local presence not confirmed), Volvo Car Deutschland (local presence not confirmed), Women in AI Cologne, Women in Big Data NRW

</details>

<details><summary><b>Uses a different stack</b> (5)</summary>

Data Platform Usergroup Rheinland, Data Saturday Rheinland, Datamonsters Ruhrgebiet / Niederrhein, Google (local presence not confirmed), Microsoft (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (12)</summary>

- https://taod.de/events
- https://tech.trivago.com/
- https://tech.trivago.com/categories/data-analytics
- https://www.adesso.de/de/news/blog/blog-rss.xml
- https://www.btelligent.com/en/blog
- https://www.ki.nrw/women-in-ai-cologne-meetup-3/
- https://www.meetup.com/big-data-dusseldorf-koln/
- https://www.meetup.com/databricks-user-group-rhein-ruhr/
- https://www.meetup.com/dusseldorf-data-science-meetup/
- https://www.meetup.com/women-in-big-data-dusseldorf/
- https://www.oraylis.de/feed
- https://www.taod.de/pressemitteilungen/data-ai-after-hours

</details>

<details><summary><b>Other sources checked</b> (46)</summary>

- [Rhein-Ruhr dbt Meetup group page](https://www.meetup.com/rhein-ruhr-dbt-meetup/)
- [Rhein-Ruhr dbt Meetup event 307198615](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/307198615/)
- [Rhein-Ruhr dbt Meetup event 304543797](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/304543797/)
- [Built-in browser (meetup.com gql2)](https://www.meetup.com/rhein-ruhr-dbt-meetup/events/?type=past) (nothing useful)
- [trivago tech blog](https://tech.trivago.com/)
- [Databricks User Group Rhein-Ruhr](https://www.meetup.com/databricks-user-group-rhein-ruhr/)
- [Düsseldorf Data Science Meetup](https://www.meetup.com/dusseldorf-data-science-meetup/)
- [Women in Big Data NRW](https://www.meetup.com/women-in-big-data-dusseldorf/)
- [WiBD NRW x Thoughtworks recap](https://www.womeninbigdata.org/women-in-big-data-nrw-x-thoughtworks-event/)
- [Women in AI Cologne #3 (KI.NRW)](https://www.ki.nrw/women-in-ai-cologne-meetup-3/)
- [taod events + press](https://taod.de/events)
- [Snowflake User Group Köln (meetup)](https://www.meetup.com/snowflake-user-group-koln/) (nothing useful)
- [PyData Cologne-Bonn (meetup)](https://www.meetup.com/pydata-cologne-bonn/) (nothing useful)
- [Data Natives Düsseldorf & Köln](https://www.meetup.com/big-data-dusseldorf-koln/) (nothing useful)
- [WebSearch: Coalesce/dbt Summit NRW employer speakers](https://sessionize.com/coalesce-2024/) (nothing useful)
- [WebSearch: REWE/METRO/Henkel/Vodafone dbt blogs](https://www.rewe-digital.com/en) (nothing useful)
- [LinkedIn Jobs guest API (keywords=dbt, Düsseldorf/Rhein-Ruhr)](https://www.linkedin.com/jobs/search?keywords=dbt)
- [meetup.com gql2 group search (lat 51.3, lon 6.9, radius 50)](https://www.meetup.com/gql2)
- [trivago Tech, Data & Product meetup](https://www.meetup.com/trivago-tech-data-product/)
- [Data Platform Usergroup Rheinland](https://www.meetup.com/pass-microsoft-data-platform-usergroup-rheinland/)
- [Datamonsters Ruhrgebiet / Niederrhein](https://www.meetup.com/pass-germany-regional-group-ruhrgebiet/)
- [Data Saturday Rheinland 2025 and 2026 (Sessionize)](https://datasaturdays.com/Event/20260711-datasaturday0084)
- [Power Platform & Fabric User Group Cologne](https://www.meetup.com/power-platform-ug-cologne/)
- [Engineering Kiosk Rhine-Ruhr](https://www.meetup.com/engineering-kiosk-rhine-ruhr/)
- [Analytics Pioneers (Düsseldorf/Köln groups)](https://www.meetup.com/analytics-pioneers-dusseldorf/)
- [Data Analytics & AI Köln (taod)](https://www.meetup.com/data-analytics-ai-koeln/)
- [PyCologne, PyData Dortmund, inovex Cologne, Female Dev Club, Women in Tech Köln](https://www.meetup.com/pycologne/) (nothing useful)
- [adesso blog RSS](https://www.adesso.de/de/news/blog/blog-rss.xml)
- [ORAYLIS blog feed](https://www.oraylis.de/feed)
- [b.telligent blog](https://www.btelligent.com/en/blog)
- [codecentric feed and blog](https://www.codecentric.de/feed) (nothing useful)
- [inovex blog search for dbt](https://www.inovex.de/de/blog/?s=dbt) (nothing useful)
- [areto consulting blog (Cologne)](https://areto.de/blog/) (nothing useful)
- [datadice blog](https://www.datadice.io/en/blog/) (nothing useful)
- [GitHub user search (dbt / data engineer, NRW cities)](https://github.com/search?type=users)
- [Medium feeds (datadice, StepStone) via WebFetch and rss2json](https://medium.com/feed/the-stepstone-group-tech-blog) (nothing useful)
- [dev.to API tag=dbt](https://dev.to/api/articles?tag=dbt) (nothing useful)
- [Snowflake user groups Germany](https://usergroups.snowflake.com/germany/) (nothing useful)
- [Women in Big Data NRW past events and hosts (Meetup gql2)](https://www.meetup.com/women-in-big-data-nrw/)
- [R-Ladies Cologne (Meetup gql2)](https://www.meetup.com/rladies-cologne/)
- [Female Dev Club (Meetup gql2)](https://www.meetup.com/female-dev-club/)
- [Women in Tech Köln (Meetup gql2)](https://www.meetup.com/women-in-tech-koln/) (nothing useful)
- [Networking in IT und Tech von Frauen für Frauen (Meetup gql2)](https://www.meetup.com/networking-im-umfeld-von-it-und-digitalisierung/) (nothing useful)
- [GDG chapter search for NRW cities](https://gdg.community.dev/chapters/) (nothing useful)
- [PyLadies locations](https://pyladies.com/locations/) (nothing useful)
- [Women on Snowflake events](https://usergroups.snowflake.com/women-on-snowflake/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

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

## 5. Before outreach

- [ ] **Check tier-1 blog authors for dbt.** 16 of the 22 tier-1 people have no item that mentions dbt. Most are adesso and ORAYLIS authors writing about Fabric, Databricks or Snowflake.
- [ ] **Confirm each consultancy author's office.** None of the adesso, ORAYLIS or b.telligent author boxes states a city.
- [ ] **Check the LinkedIn hints that had no profile link.** Search summaries put Lasse Jenzen, Insa Menzel, Nils Kux and Tobias Jasinski in Düsseldorf, but no profile carried the evidence.
- [ ] **Check Inna Zykova.** A LinkedIn result from the Berlin search places Inna Zykova in Düsseldorf. This file still records the location as unknown.
- [ ] **Check the duplicates with the Munich file.** Mathias Heinze (b.telligent) and Benedikt Buchert (Analytics Pioneers) appear in both. The Munich file places Mathias Heinze in Munich, on a name match only.
- [ ] **Match both spellings of Hicham Babahmed.** The name is also spelled "Hisham". Hicham Babahmed organised the first event while at adesso, and now works at dbt Labs, with a Frankfurt profile.
- [ ] **Treat visiting speakers as visitors.** Pádraic Slattery is in Amsterdam, Stephan Durry in Berlin, and Sascha Dittmann and Hicham Babahmed in Frankfurt.
- [ ] **dbt Labs staff are labelled.** Stephan Durry and Hicham Babahmed work there. They can speak, but check the line-up has practitioners first.

## 6. Next run

- **Sources to try first:**
  - **taod and adesso:** ask which of their authors work in the region.
  - **Medium and dev.to authors:** never scanned, because both were rate-limited. Try them from a fresh session.
  - **Community events:** new events of the Rhein-Ruhr dbt Meetup, Databricks User Group Rhein-Ruhr, trivago Tech, Data & Product, Datamonsters Ruhrgebiet, Data Saturday Rheinland, Women in Big Data NRW and Women in AI Cologne.
  - **Blog feeds:** new posts on the adesso, ORAYLIS and b.telligent feeds, with each author box.
- **Women-in-data communities not yet reachable:**
  - **Women in Big Data NRW:** the Data Dates evenings name no speakers. Ask the hosts for a talk evening on analytics engineering, and for the SQL speaker at Female Dev Club.
  - **WiDS, Women Techmakers, She Loves Data and Girls in Tech:** no NRW chapter or event was found.
  - **Networking in IT und Tech von Frauen für Frauen:** a new Cologne group. Check its first events.
- **People from the women-in-data pass:** the 18 people added have no LinkedIn search. Angela Music-Siedler and the Point 8 and Vaillant speakers have no title on record.
- **People to locate:** 32 people have no known location. 13 tier-1 blog authors were searched on LinkedIn without a match. These 19 were never searched on LinkedIn:
  - **Tier 1:** Siver Rajab (adesso).
  - **Tier 2:** Alex Rupp, Anastasia Senitz, Hanna Schwab, Benedikt Buchert, Daniel Schmidt, Diana Ackermann, Jake Mongaya, Marco Nielinger, Mario Müller and Simon Schröder.
  - **Tier 3:** Andreas Schiffer, Benjamin Kirsche, Christopher König, Frank Geisler, Moritz Bauer, Sebastian Grünwald and Stephan Dahlmann.
  - **Connector:** Oliver Engels.
  - **First to search:** Alex Rupp, as a past chapter speaker.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `dusseldorf/dusseldorf_dbt_companies.json`, the Rhein-Ruhr dbt Meetup, `../enriched/rhein-ruhr-dbt-meetup.json` and the region above. Add: "Most NRW dbt searches return job ads, so prefer direct fetches."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build, from one research pass and a LinkedIn Jobs scan. 49 companies, 23 people and 49 dbt job ads at 24 companies. 16 proven speakers, 6 featured and 1 emerging voice. 5 people had spoken at the chapter. 7 people had LinkedIn profiles. |
| 2026-10-01 | 2 | Extension run through meetup.com, Sessionize, consultancy blog feeds and GitHub. 46 people and 15 companies added, for 69 people and 64 companies. Emerging voices rose from 1 to 20. Tier 1 rose from 1 to 21. |
| 2026-10-01 | 2 | Location pass from public pages. 16 people placed: 12 in the region and 4 elsewhere. Unknown locations fell from 51 to 35. |
| 2026-10-01 | 2 | LinkedIn pass on the 15 tier-1 blog authors without a location. 2 people placed: 1 in the region and 1 elsewhere. 33 locations are still unknown. |
| 2026-10-01 | 3 | Women-in-data pass. Checked Women in Big Data NRW (past events and hosts), Female Dev Club, R-Ladies Cologne, Women in Tech Köln, GDG chapters in NRW, PyLadies and Women on Snowflake. Added 18 people with `sourced_via: women_in_data_community`: 10 Women in Big Data NRW speakers and 8 hosts and organisers as connectors. Added a talk to Inna Zykova. Added community channels for the current Women in Big Data NRW page, R-Ladies Cologne and Female Dev Club. |
| 2026-10-01 | 4 | Company pass from open job boards (Greenhouse, Lever, Ashby, Personio, arbeitnow), HN Who is hiring, dbt Labs case studies and Meetup gql2 line-ups. 4 companies added, for 78, none with a strong dbt signal. 3 raised to strong: DISH Digital Solutions (METRO), Scalefree and Analytics Pioneers. People are unchanged. |
