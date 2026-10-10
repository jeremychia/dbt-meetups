# Stockholm: city notes

This file holds what is specific to Stockholm. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Stockholm dbt Meetup](https://www.meetup.com/stockholm-dbt-meetup/), data in `stockholm_dbt_companies.json`
- **Region:** the Stockholm metro area. Commuter towns count as local, so Uppsala is in the region.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 7, 2026-10-06)

| | Count |
|---|---|
| Companies | 173 |
| People | 241 |
| Tier 1 leads | 1 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 82 |
| Spoke at this chapter before | 19 |
| Based in the region | 222 |
| Based elsewhere | 8 |
| Location unknown | 11 |
| With a LinkedIn profile | 124 |
| Job ads mentioning dbt | 66 |
| Past chapter meetups | 7 |
<!-- at-a-glance:end -->

## 1. Where to look in Stockholm

- **[Data & AI Stockholm](https://dataaistockholm.com/):** the best source, and the city's most active data community. Its [Substack recaps](https://dataaistockholm1.substack.com/p/data-ai-in-practice-from-foundations) name speakers with their employers. Its [summit page](https://dataaistockholm.com/summit) lists 18 speakers with LinkedIn links. The summit is on 14 October 2026. The recaps and summit page are far more efficient than company blogs.
- **Chapter events:** 7 events, from January 2023 to June 2025. The early events were at Regeringsgatan 25. Since May 2024 they have been at Solita. They gave 19 past speakers, added from `../enriched/stockholm-dbt-meetup.json`. The chapter has had no events since the [June 2025 meetup](https://www.meetup.com/stockholm-dbt-meetup/events/307908713/).
- **[Snowflake User Group Stockholm](https://usergroups.snowflake.com/stockholm/):** its event pages render on the server. They list speakers, organisers and LinkedIn links without a browser. One 2026 session covered dbt.
- **LinkedIn Jobs:** a search for dbt around Stockholm. 62 ads at 55 companies mention dbt. The ads are spread thinly. Storytel, Solita, NOBA Bank, Lovable, Etraveli, Avalanche Studios and Adavo posted 2 each.
- **A Luma event page:** the page for a [Nextory talk](https://luma.com/4f8lqzsp) confirmed a speaker's role.
- **meetup.com RSVP lists:** the best location source. They placed most of the past chapter speakers.
- **LinkedIn search results:** 7 past chapter speakers without a location were searched. Filip Vitez was placed in Stockholm. Niklas Kullberg was placed in the Uppsala area, which counts as local. Salma Bakouk was placed in New York.

### Companies and job ads

- **[dbt Labs case studies](https://www.getdbt.com/sitemap-0.xml):** the sitemap lists 61 `/case-studies/` pages. Each page states the company headquarters. The [Rebtel](https://www.getdbt.com/case-studies/rebtel) and [McDonald's Nordics](https://www.getdbt.com/case-studies/mcdonalds-nordics) case studies both name Stockholm as headquarters.
- **HN Who is hiring:** the Algolia search for "dbt stockholm" gave Anyfin, with BigQuery and dbt in its stack.
- **Company job boards:** the open Greenhouse, Lever and Ashby job APIs (`boards-api.greenhouse.io/v1/boards/<slug>/jobs?content=true`, `api.lever.co/v0/postings/<slug>?mode=json`, `api.ashbyhq.com/posting-api/job-board/<slug>`) return the full ad text, so one call per company checks for the whole word dbt and the location. Spotify and Wolt have Stockholm ads that mention dbt.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[Women in Tech Sweden](https://womenintech.se/speakers/):** the best women-in-data source here. Its speakers page lists every conference speaker with title and employer. Each speaker page links the session title and year, and each session page names co-speakers. It gave 12 data and analytics speakers from the 2024, 2025 and 2026 conferences:
  - **ICA:** Annie von Heijne and Maaret Malinen on [building a data-driven business with data governance](https://womenintech.se/play/the-journey-towards-datadriven-business/) (2024), and Heaven Bereket (2026).
  - **EasyPark:** Jing Zhao, Doreh Bovelet and Sindhusha Marakani on [scaling analytics as data demands grow](https://womenintech.se/play/scaling-success-addressing-organizational-growth-data-demands-and-overcoming-challenges/) (2024).
  - **Electrolux:** Anna Bärlund, Vida Ahmadi and Hajar El Hanafi on [experimenting with AI](https://womenintech.se/play/embracing-ai-dare-to-experiment-and-learn/) (2025).
  - **Others:** Frida Värnlund (Visma) on [democratising product analytics with AI agents](https://womenintech.se/play/how-visma-democratises-data-at-scale-with-internal-ai-agents/) (2026), Lisa Olsson (Snowflake, 2025) and Gabrielle Dolinder (CEMIT Digital, 2025).
- **[Women on Snowflake](https://usergroups.snowflake.com/events/details/snowflake-women-on-snowflake-presents-deep-dive-dbt-projects-on-snowflake/cohost-stockholm):** co-hosted a dbt-on-Snowflake deep dive with the Stockholm user group in January 2026. It gave the only tier-1 lead. In September 2026 it ran a [Semantic Views lab at Snowflake World Tour Stockholm](https://usergroups.snowflake.com/e/mn74k4/) and a [session at ODSC Stockholm](https://usergroups.snowflake.com/e/mjuh2v/). Neither page names speakers.
- **[WiDS Sweden 2025](https://wids.confetti.events/wids2025):** mostly machine learning and AI. Its organisers include people who run data platforms at Handelsbanken, H&M and Spotify.
- **[PyLadies Stockholm](https://www.meetup.com/pyladiesstockholm/):** mostly Python talks. An [April 2025 evening at Svenska Kraftnät](https://www.meetup.com/pyladiesstockholm/events/307271864/) covered data analytics and forecasting, but names no speaker. Meetup's event-host data names 3 organisers: Anwesha Das, Beatriz Uezu and Alenka Gucek. They are connectors.
- **[AWS Women's User Group Sweden](https://www.meetup.com/aws-womens-user-group-sweden/):** started in April 2025. One data talk: Darya Petrashka (SLB) on [talking to the business](https://www.meetup.com/aws-womens-user-group-sweden/events/315186079/), online in June 2026. Its organisers Jagoda Čubrilo, Suzana Melo and Caroline Cah (Knightec, Gothenburg) are connectors.
- **[Women Techmakers through GDG Stockholm](https://gdg.community.dev/e/mpcqyv/):** one online International Women's Day event in March 2025, with AI and career talks. Its co-organisers Zahra Mirzaei (Devoteam) and Marina Dushkina (ICA) are connectors.
- **Also ask:** data leads at dbt companies to suggest people on their teams.

## 2. What didn't work here

- **Company blogs:** no emerging voices were found. The [Epidemic Sound Medium feed](https://medium.com/feed/epidemicsound) was empty. The [Klarna engineering feed](https://engineering.klarna.com/feed) timed out.
- **Robert Sahlin's Medium feed:** the [feed](https://medium.com/feed/@robertsahlin) is empty because Robert Sahlin now writes on Substack.
- **Conference speaker pages:**
  - **Data Innovation Summit:** the [page](https://datainnovationsummit.com/region/nordics/data-engineering-dataops-summit/) shows only a few speakers.
  - **dbt Summit:** the [speaker list](https://www.getdbt.com/dbt-summit/speakers) has no Swedish-employer speakers.
  - **Snowflake World Tour Stockholm:** the [speakers](https://www.snowflake.com/en/world-tour/stockholm/speakers/) render in the browser only.
- **Stockholm Open Source Data Infrastructure meetup:** the [past events](https://www.meetup.com/stockholm-open-source-data-infrastructure-meetup/events/?type=past) render in the browser only.
- **dev.events:** the [Stockholm data listing](https://dev.events/meetups/EU/SE/Stockholm/data) shows only online events and two summits.
- **Dormant or new women-in-data groups:** [R-Ladies Stockholm](https://www.meetup.com/rladies-stockholm/) has had no events since 2019. Two groups founded in 2026, Let's Talk (for women and non-binary people in tech) and SoHer Society, have held discussion and café evenings with no talks.
- **WiDS Sweden 2026:** no page was found. The wids2026 page and the confetti.events site root return 404.
- **Women in Tech Sweden partner meetups:** the [meetups archive](https://womenintech.se/wp-json/wp/v2/meetups) ends in 2023. Its January 2023 SEB data meetup falls before the window for talks.
- **Company job boards with no Stockholm dbt ad:** Mentimeter, Lovable, Legora, Trustly, Truecaller, Paradox, Lunar, Pleo, Betsson and Kambi. Klarna, King, Voi, Epidemic Sound, Storytel, Kivra and most other Swedish employers tried use Teamtailor or Workday, which have no open job API.
- **GitHub code search:** `filename:dbt_project.yml org:<org>` found no public dbt project in the orgs tried. The search rate limit cut several calls short. Orgs tried: Spotify, Klarna, Epidemic Sound, Kivra and Voi.
- **Meetup line-ups:** the Stockholm MLOps, Power BI and Fabric, SQL, ClickHouse, GDG Cloud and Real Time Data groups since 2024 never mention dbt. The Stockholm Snowflake Meetup group on meetup.com has no events, because it now runs on the Snowflake user group site.

## 3. Companies looked at

- **Solita hosts the chapter.** Every event since May 2024 has been at Solita.
- **Stockholm's dbt signal is indirect.** It comes through semantic-layer and BI talks, often by Omni customers, rather than dbt-branded content.
- **No company dominates the job ads.** 62 ads are spread across 55 companies.

<!-- companies:start -->
172 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (5)</summary>

Drake Analytics, Epidemic Sound, McDonald's Nordics, Rebtel, Solita

</details>

<details><summary><b>Some dbt signal</b> (57)</summary>

Academedia, Adavo, Agio, Agoda, ANIMARUM, Anyfin, Avalanche Studios Group, Bokadirekt, Bravura Sverige, Cognizant, Confidential, CoreChange Group, Ctrl Digital, Deploja, Devoteam / Google Cloud Partner, Doktor.Se, Epico Tech, Etraveli Group, FDJ UNITED, Fortnox, Haypp Group, Ictech, Kivra, Knowit, Liminity AB, Lovable, Marginalen Bank, Natlink, Netlight, Nexer Group, Nion, NOBA Bank Group, Norrin, Novax, Omni (local presence not confirmed), Playground Tech, Qliro, Sambla Group, Schibsted, Snowflake User Group Stockholm / Women on Snowflake, Spiris / Visma, Spotify, Steep, Storytel, Strawberry, StressTerapi, Stretch AB, SVT, Tandem Health, Tenth Revolution Group, Tieto, Toca Boca, Vitamin Well Group, VNTRS, Voyado, Wolt, WPP Media

</details>

<details><summary><b>Not verified</b> (108)</summary>

0TO9 (local presence not confirmed), A_SPACE (local presence not confirmed), Acast, acast-tech (local presence not confirmed), Adage-AB (local presence not confirmed), Adapteo Group (local presence not confirmed), AKLYON Consulting / PwC Sweden (local presence not confirmed), AWS Women's User Group Sweden (local presence not confirmed), Bannerflow (local presence not confirmed), Blackhole Consulting AB (local presence not confirmed), CAG Arete (local presence not confirmed), CEMIT Digital (local presence not confirmed), CGI (local presence not confirmed), Company (local presence not confirmed), Coop Sverige AB (local presence not confirmed), Dalarna university (local presence not confirmed), Data & AI Stockholm (DAIS), Data Engineer (Open to Work) (local presence not confirmed), Datatonic (local presence not confirmed), DBT Capital (local presence not confirmed), dbt Labs (local presence not confirmed), Dometic (local presence not confirmed), EasyPark Group (local presence not confirmed), Einride (local presence not confirmed), Electrolux (local presence not confirmed), Electrolux Group (local presence not confirmed), epidemicsound (local presence not confirmed), EQT (local presence not confirmed), Ericsson (local presence not confirmed), extenda (local presence not confirmed), Forefront Consulting (local presence not confirmed), Freelance (local presence not confirmed), Freelancer (local presence not confirmed), Freelancing Full Stack Web Developer (local presence not confirmed), Funnel (local presence not confirmed), Funnel AB (local presence not confirmed), Globhe (local presence not confirmed), Google Cloud (local presence not confirmed), Grafana Labs (local presence not confirmed), Greenely (local presence not confirmed), H&M (local presence not confirmed), H&M Group (local presence not confirmed), Handelsbanken (local presence not confirmed), Hassan Shah Consulting AB (local presence not confirmed), Hive Streaming (local presence not confirmed), ICA Gruppen (local presence not confirmed), ICA Sverige (local presence not confirmed), imeto Consulting AB (local presence not confirmed), innofactor (local presence not confirmed), Iver Sverige (local presence not confirmed), King, klarna (local presence not confirmed), Klarna AB (local presence not confirmed), Knightec Group (local presence not confirmed), Kognity (local presence not confirmed), Krafthem (local presence not confirmed), KTH Royal Institute of Technology (local presence not confirmed), Lawline (local presence not confirmed), majority (local presence not confirmed), ManpowerGroup (local presence not confirmed), MetaSolutions AB (local presence not confirmed), Millnet BI (local presence not confirmed), Nackademin (local presence not confirmed), Netlight Consulting (local presence not confirmed), Nexer insight (local presence not confirmed), Nextory, Nordea (local presence not confirmed), NordicFeel (local presence not confirmed), Northridge Analytics (local presence not confirmed), Northvolt (local presence not confirmed), OKQ8 (local presence not confirmed), Once Upon (local presence not confirmed), Pickles Auctions (local presence not confirmed), Pricer AB (local presence not confirmed), PyLadies Stockholm (local presence not confirmed), Qred (local presence not confirmed), RaySearch Laboratories AB (local presence not confirmed), Redfield-AB (local presence not confirmed), SciLifeLab & Karolinska Institutet (local presence not confirmed), SciLifeLab Data Center (local presence not confirmed), ScilifelabDataCentre (local presence not confirmed), SEB (local presence not confirmed), Sifflet (local presence not confirmed), SLB (local presence not confirmed), SmallPDF (local presence not confirmed), Snowflake (local presence not confirmed), Sogeti @husqvarnagroup (local presence not confirmed), Sovereign by Source (local presence not confirmed), Statskontoretdatalabb (local presence not confirmed), Stockholm University (local presence not confirmed), Supercargo (local presence not confirmed), Svedea, Sveriges Radio (local presence not confirmed), SYNQ (local presence not confirmed), Tele2, Telia Company (local presence not confirmed), telia-company (local presence not confirmed), Tibber (local presence not confirmed), TolveAB (local presence not confirmed), Truecaller (local presence not confirmed), TUI (local presence not confirmed), Uppsala University (local presence not confirmed), viaplaygroup (local presence not confirmed), Visma Group (local presence not confirmed), Visma Software International AS (local presence not confirmed), Voi (local presence not confirmed), WiDS (AI & ML) Sweden, zero-plus-x (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (2)</summary>

Embark Studios (local presence not confirmed), TELETID (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (8)</summary>

- https://dataaistockholm.com/
- https://dataaistockholm1.substack.com/feed
- https://dataaistockholm1.substack.com/p/getting-everyone-on-the-same-page
- https://dataaistockholm1.substack.com/p/scaling-metrics-at-spotify-the-story
- https://dataaistockholm1.substack.com/p/speedrunning-insurance
- https://medium.com/feed/epidemicsound
- https://usergroups.snowflake.com/stockholm/
- https://wids.confetti.events/wids2025

</details>

<details><summary><b>Other sources checked</b> (29)</summary>

- Local chapter history (enriched/stockholm-dbt-meetup.json): `enriched/stockholm-dbt-meetup.json`
- [Data & AI Stockholm site + Substack feed](https://dataaistockholm.com/)
- [DAIS Summit 2026](https://dataaistockholm.com/summit)
- [Snowflake User Group Stockholm](https://usergroups.snowflake.com/stockholm/)
- [WiDS Sweden 2025](https://wids.confetti.events/wids2025)
- [Andres Vourakis Luma talk](https://luma.com/4f8lqzsp)
- [Data Innovation Summit 2026 (Data Engineering & DataOps stage)](https://datainnovationsummit.com/region/nordics/data-engineering-dataops-summit/) (nothing useful)
- [dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers) (nothing useful)
- [Snowflake World Tour Stockholm speakers](https://www.snowflake.com/en/world-tour/stockholm/speakers/) (nothing useful)
- [meetup.com Stockholm dbt / Open Source Data Infra past events](https://www.meetup.com/stockholm-open-source-data-infrastructure-meetup/events/?type=past) (nothing useful)
- [Epidemic Sound Medium feed](https://medium.com/feed/epidemicsound) (nothing useful)
- [Klarna Engineering feed](https://engineering.klarna.com/feed) (nothing useful)
- [Robert Sahlin Medium feed](https://medium.com/feed/@robertsahlin) (nothing useful)
- [dev.events Stockholm data meetups](https://dev.events/meetups/EU/SE/Stockholm/data) (nothing useful)
- [LinkedIn Jobs guest API (keywords=dbt, Stockholm-area)](https://www.linkedin.com/jobs/search?keywords=dbt)
- [Meetup gql2 groupSearch around Stockholm](https://www.meetup.com/gql2)
- [PyLadies Stockholm past events and hosts (Meetup gql2)](https://www.meetup.com/pyladiesstockholm/)
- [AWS Women's User Group Sweden (Meetup gql2)](https://www.meetup.com/aws-womens-user-group-sweden/)
- [R-Ladies Stockholm (Meetup gql2)](https://www.meetup.com/rladies-stockholm/) (nothing useful)
- [Let's Talk and SoHer Society (Meetup gql2)](https://www.meetup.com/lets-talk-kvinnor-och-ickebinara-inom-tech-swedish/) (nothing useful)
- [Women on Snowflake events](https://usergroups.snowflake.com/women-on-snowflake/)
- [GDG Stockholm events API (Women Techmakers)](https://gdg.community.dev/gdg-cloud-stockholm/)
- [Women in Tech Sweden speakers and sessions](https://womenintech.se/speakers/)
- [Women in Tech Sweden meetups (WordPress API)](https://womenintech.se/wp-json/wp/v2/meetups) (nothing useful)
- [Data & AI Stockholm Substack archive](https://dataaistockholm1.substack.com/archive)
- [Snowflake User Group Stockholm startups event](https://usergroups.snowflake.com/events/details/snowflake-stockholm-presents-startups-on-snowflake-unlock-quick-insights-at-scale/) (nothing useful)
- [Databricks User Group Stockholm, Adlibris event](https://usergroups.databricks.com/events/details/databricks-user-groups-stockholm-databricks-user-group-presents-databricks-customer-data-journey-with-adlibris/) (nothing useful)
- [Coalesce speaker search result](https://coalesce.getdbt.com/speakers/quentin-coviaux)
- [Data Innovation Summit 2025 search](https://allai.events/event/data-innovation-summit-2025) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:** none were found. These are the strongest leads who have not yet spoken at the chapter:
  - **Daniele Abbatelli**, Drake Analytics: [Deep dive: dbt projects on Snowflake](https://usergroups.snowflake.com/events/details/snowflake-women-on-snowflake-presents-deep-dive-dbt-projects-on-snowflake/cohost-stockholm) (January 2026). This is the only tier-1 lead. The tier-1 rule needs a dbt item from 2024 onwards, so most proven speakers here stay in tier 2.
  - **Carl Niblaeus**, Nextory: [getting everyone on the same page](https://dataaistockholm1.substack.com/p/getting-everyone-on-the-same-page), on an 18-month rebuild with production SQL generated from specs (September 2026).
  - **Andres Vourakis**, Nextory: [the road towards agentic analytics](https://dataaistockholm1.substack.com/p/data-ai-in-practice-from-foundations), a Slackbot built on semantic models (March 2026).
  - **Gabriel Moosman**, Acast: [lessons from replatforming BI at Acast](https://dataaistockholm.com/summit), at the October 2026 summit.
  - **Rasmus Säfvenberg**, Svedea: [moving fast in a regulated industry](https://dataaistockholm1.substack.com/p/speedrunning-insurance) (August 2026). Check the stack for dbt first.
- **Anchor speakers:**
  - **Abraham Setiawan**, Rebtel: [how Rebtel increased data product value](https://www.meetup.com/stockholm-dbt-meetup/events/307908713/) at the chapter (June 2025).
  - **Johan Baltzar**, Steep: [next-level use cases for the semantic layer](https://www.meetup.com/stockholm-dbt-meetup/events/306047342/) at the chapter (March 2025).
  - **Manish Ramrakhiani**, 0TO9: [P&L, risk and reconciliation on Snowflake](https://usergroups.snowflake.com/events/details/snowflake-stockholm-presents-finance-meets-data-snowflake-stockholm-meetup/) (May 2026). Also a past chapter speaker on dbt exposures.
- **Connectors:**
  - **Vanessa Andersson**: founder of [Data & AI Stockholm](https://dataaistockholm.com/). This is the best co-host for a relaunch.
  - **Muhammad Fasih Ullah**, NordicFeel, and **Fredrik Viksten**: organisers of the [Snowflake User Group Stockholm](https://usergroups.snowflake.com/stockholm/).
  - **Anastasiia Stefanska**, TUI: Women on Snowflake chapter leader, who co-hosted the [dbt-on-Snowflake deep dive](https://usergroups.snowflake.com/events/details/snowflake-women-on-snowflake-presents-deep-dive-dbt-projects-on-snowflake/cohost-stockholm).
  - **Anna Baecklund**, Handelsbanken: organiser of [WiDS Sweden](https://wids.confetti.events/wids2025), and head of data and analytics platforms.

## 5. Before outreach

- [ ] **Confirm current roles** of the past chapter speakers before asking them back. Most of the 19 spoke in 2023.
- [ ] **Check stale employers.** Filip Vitez is recorded at Northvolt, but the LinkedIn result shows a newer employer, veyra.
- [ ] **Check for dbt use** at Svedea, Tele2, Adapteo and Funnel. Their speakers talk about data platforms, but dbt is not confirmed.
- [ ] **Check unconfirmed details.** Ece Kural's employer is not stated. Baaba Bonuedie's city is not confirmed, since Nordea has several Nordic hubs.
- [ ] **Treat visiting speakers as visitors.** Ernesto Ongaro is in Dublin, Kshitij Aranke and Stephen Murphy in London, and Salma Bakouk in New York.
- [ ] **dbt Labs staff are labelled.** Ernesto Ongaro, Kshitij Aranke, Lucas Paes and Mike Burke work there. They can speak, but check the line-up has practitioners first.
- [ ] **Check Ludwig Sewall's employer.** Ludwig Sewall is recorded at Solita, but the June 2025 chapter talk lists a dbt Labs role. The record is not labelled as dbt Labs staff.

## 6. Next run

- **Sources to try first:**
  - **meetup.com group search:** search data groups around Stockholm, then read each group's past events. Use the meetup.com `gql2` endpoint, which the first build could not use. This is the best way to find first-time speakers in other meetups' line-ups.
  - **Substack, Medium and company blogs:** look for Stockholm authors who write about dbt, and record each author's employer. The city has no emerging voices yet.
  - **Community events:** new Data & AI Stockholm recaps, Snowflake User Group Stockholm events, and WiDS Sweden and Women on Snowflake events.
  - **Data Innovation Summit:** the full speaker list.
- **Women-in-data communities not yet reachable:**
  - **WiDS Sweden 2026:** look for a new event page, or ask the organisers already recorded.
  - **Women in Tech Sweden:** about 300 speaker pages were not read. Read the rest of the data, analytics and BI speakers, and the 2026 programme.
  - **Women on Snowflake Stockholm events:** ask Anastasiia Stefanska who led the September 2026 lab and the ODSC session.
  - **PyLadies Stockholm:** ask the organisers for the Svenska Kraftnät speakers.
  - **She Loves Data, Girls in Tech and Women in Big Data:** no Stockholm chapter or event was found.
- **People from the women-in-data pass:** the 21 people added have no LinkedIn search. Jing Zhao and Sindhusha Marakani have no location on record.
- **People to locate:** 7 people have no known location.
  - **Searched twice on LinkedIn, no profile link:** Mauro Luzzatto, Guillaume Fetter, Linus Wågberg and Erik Lehto.
  - **Never searched on LinkedIn:** Mike Burke and Isabella Renzetti.
  - **LinkedIn profile found, location still unknown:** Akanksha Bhagwanani.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `stockholm/stockholm_dbt_companies.json`, the Stockholm dbt Meetup, `../enriched/stockholm-dbt-meetup.json` and the region above. Add: "The city has no first-time speakers yet, so search Substack, Medium and company blogs for Stockholm authors first."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build, from one research pass and a LinkedIn Jobs scan. 90 companies, 51 people and 62 dbt job ads at 55 companies. 40 proven speakers, 11 featured and no emerging voices. 19 people had spoken at the chapter. 17 people had LinkedIn profiles. |
| 2026-10-01 | 2 | Location pass from public pages. 11 people placed: 8 in the region and 3 elsewhere. Unknown locations fell from 21 to 10. |
| 2026-10-01 | 2 | LinkedIn pass on 7 past chapter speakers. 3 placed: 2 in the region and 1 elsewhere. 7 locations are still unknown, and 20 people now have LinkedIn profiles. |
| 2026-10-01 | 3 | Women-in-data pass. Checked Women in Tech Sweden (speakers and sessions), PyLadies Stockholm and AWS Women's User Group Sweden (past events and hosts), Women on Snowflake, Women Techmakers through GDG Stockholm, WiDS Sweden, R-Ladies Stockholm and two new Meetup groups. Added 21 people with `sourced_via: women_in_data_community`: 13 speakers and 8 organisers as connectors. Added new events for Anastasiia Stefanska and Isabella Renzetti. Added 6 community channels. |
| 2026-10-01 | 4 | Company pass from open job boards (Greenhouse, Lever, Ashby), HN Who is hiring, dbt Labs case studies and Meetup gql2 line-ups. 2 companies added, for 102. McDonald's Nordics has a strong dbt signal. Rebtel raised to strong. People are unchanged. |
| 2026-10-05 | 5 | 4 more people, including Quentin Coviaux (Rebtel), a dbt Summit speaker. Searches for local dbt authors returned only job ads. |
| 2026-10-05 | 6 | 106 more people from `find_local_speakers.py`: 23 organisers of local data groups, 83 data people from GitHub with a town in the region. Speakers count only when a LinkedIn lookup placed them in the region. Speaker lookups stopped after 3 people, so this city's speakers are not added yet. |
