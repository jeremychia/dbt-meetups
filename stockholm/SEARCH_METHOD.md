# Stockholm: city notes

This file holds what is specific to Stockholm. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Stockholm dbt Meetup](https://www.meetup.com/stockholm-dbt-meetup/), data in `stockholm_dbt_companies.json`
- **Region:** the Stockholm metro area. Commuter towns count as local, so Uppsala is in the region.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 90 |
| People | 51 |
| Tier 1 leads | 1 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 40 |
| Spoke at this chapter before | 19 |
| Based in the region | 40 |
| Based elsewhere | 4 |
| Location unknown | 7 |
| With a LinkedIn profile | 20 |
| Job ads mentioning dbt | 62 |
| Past chapter meetups | 7 |
<!-- at-a-glance:end -->

## 1. Where to look in Stockholm

- **[Data & AI Stockholm](https://dataaistockholm.com/):** the best source, and the city's most active data community. Its [Substack recaps](https://dataaistockholm1.substack.com/p/data-ai-in-practice-from-foundations) name speakers with their employers. Its [summit page](https://dataaistockholm.com/summit) lists 18 speakers with LinkedIn links. The summit is on 14 October 2026. The recaps and summit page are far more efficient than company blogs.
- **Chapter events:** 7 events, from January 2023 to June 2025. The early events were at Regeringsgatan 25. Since May 2024 they have been at Solita. They gave 19 past speakers, added from `../enriched/stockholm-dbt-meetup.json`. The chapter has had no events since the [June 2025 meetup](https://www.meetup.com/stockholm-dbt-meetup/events/307908713/).
- **[Snowflake User Group Stockholm](https://usergroups.snowflake.com/stockholm/):** its event pages render on the server. They list speakers, organisers and LinkedIn links without a browser. One 2026 session covered dbt.
- **[Women on Snowflake](https://usergroups.snowflake.com/events/details/snowflake-women-on-snowflake-presents-deep-dive-dbt-projects-on-snowflake/cohost-stockholm):** co-hosted a dbt-on-Snowflake deep dive with the Stockholm user group in January 2026. It gave the only tier-1 lead.
- **[WiDS Sweden 2025](https://wids.confetti.events/wids2025):** mostly machine learning and AI. Its organisers include people who run data platforms at Handelsbanken, H&M and Spotify.
- **LinkedIn Jobs:** a search for dbt around Stockholm. 62 ads at 55 companies mention dbt. The ads are spread thinly. Storytel, Solita, NOBA Bank, Lovable, Etraveli, Avalanche Studios and Adavo posted 2 each.
- **A Luma event page:** the page for a [Nextory talk](https://luma.com/4f8lqzsp) confirmed a speaker's role.
- **meetup.com RSVP lists:** the best location source. They placed most of the past chapter speakers.
- **LinkedIn search results:** 7 past chapter speakers without a location were searched. Filip Vitez was placed in Stockholm. Niklas Kullberg was placed in the Uppsala area, which counts as local. Salma Bakouk was placed in New York.

## 2. What didn't work here

- **Company blogs:** no emerging voices were found. The [Epidemic Sound Medium feed](https://medium.com/feed/epidemicsound) was empty. The [Klarna engineering feed](https://engineering.klarna.com/feed) timed out.
- **Robert Sahlin's Medium feed:** the [feed](https://medium.com/feed/@robertsahlin) is empty because Robert Sahlin now writes on Substack.
- **Conference speaker pages:**
  - **Data Innovation Summit:** the [page](https://datainnovationsummit.com/region/nordics/data-engineering-dataops-summit/) shows only a few speakers.
  - **dbt Summit:** the [speaker list](https://www.getdbt.com/dbt-summit/speakers) has no Swedish-employer speakers.
  - **Snowflake World Tour Stockholm:** the [speakers](https://www.snowflake.com/en/world-tour/stockholm/speakers/) render in the browser only.
- **Stockholm Open Source Data Infrastructure meetup:** the [past events](https://www.meetup.com/stockholm-open-source-data-infrastructure-meetup/events/?type=past) render in the browser only.
- **dev.events:** the [Stockholm data listing](https://dev.events/meetups/EU/SE/Stockholm/data) shows only online events and two summits.

## 3. Companies looked at

- **Solita hosts the chapter.** Every event since May 2024 has been at Solita.
- **Stockholm's dbt signal is indirect.** It comes through semantic-layer and BI talks, often by Omni customers, rather than dbt-branded content.
- **No company dominates the job ads.** 62 ads are spread across 55 companies.

<!-- companies:start -->
89 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (3)</summary>

Drake Analytics, Epidemic Sound, Solita

</details>

<details><summary><b>Some dbt signal</b> (57)</summary>

Academedia, Adavo, Agio, Agoda, ANIMARUM, Avalanche Studios Group, Bokadirekt, Bravura Sverige, Cognizant, Confidential, CoreChange Group, Ctrl Digital, Deploja, Devoteam / Google Cloud Partner, Doktor.Se, Epico Tech, Etraveli Group, FDJ UNITED, Fortnox, Haypp Group, Ictech, Kivra, Knowit, Liminity AB, Lovable, Marginalen Bank, Natlink, Netlight, Nexer Group, Nion, NOBA Bank Group, Norrin, Novax, Omni (local presence not confirmed), Playground Tech, Qliro, Rebtel, Sambla Group, Schibsted, Snowflake User Group Stockholm / Women on Snowflake, Spiris / Visma, Spotify, Steep, Storytel, Strawberry, StressTerapi, Stretch AB, SVT, Tandem Health, Tenth Revolution Group, Tieto, Toca Boca, Vitamin Well Group, VNTRS, Voyado, Wolt, WPP Media

</details>

<details><summary><b>Not verified</b> (29)</summary>

0TO9 (local presence not confirmed), Acast, Adapteo Group (local presence not confirmed), AKLYON Consulting / PwC Sweden (local presence not confirmed), Data & AI Stockholm (DAIS), dbt Labs (local presence not confirmed), Einride (local presence not confirmed), EQT (local presence not confirmed), Funnel (local presence not confirmed), Google Cloud (local presence not confirmed), Grafana Labs (local presence not confirmed), H&M Group (local presence not confirmed), Handelsbanken (local presence not confirmed), Iver Sverige (local presence not confirmed), King, Nextory, Nordea (local presence not confirmed), NordicFeel (local presence not confirmed), Northridge Analytics (local presence not confirmed), Northvolt (local presence not confirmed), Once Upon (local presence not confirmed), Sifflet (local presence not confirmed), Supercargo (local presence not confirmed), Svedea, SYNQ (local presence not confirmed), Tele2, TUI (local presence not confirmed), Voi (local presence not confirmed), WiDS (AI & ML) Sweden

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

<details><summary><b>Other sources checked</b> (15)</summary>

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
