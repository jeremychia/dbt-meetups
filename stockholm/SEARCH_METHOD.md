# Stockholm dbt search: method, lessons and replication prompt

This file goes with `stockholm_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in the Stockholm area who could **speak at** (or attend) the [Stockholm dbt Meetup](https://www.meetup.com/stockholm-dbt-meetup/), and the local companies that use dbt.
- **Region:** the Stockholm metro area. Uppsala counts as outside.

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
| Based in the region | 37 |
| Based elsewhere | 7 |
| Location unknown | 7 |
| With a LinkedIn profile | 20 |
| Job ads mentioning dbt | 62 |
| Past chapter meetups | 7 |
<!-- at-a-glance:end -->

## 1. How the search was done

### Step 1: Chapter history

- **What was checked:** 7 chapter events, from January 2023 to June 2025. The early events were at Regeringsgatan 25. Since May 2024 they have been at Solita.
- **What it yielded:** 19 past speakers, added from `../enriched/stockholm-dbt-meetup.json`.
- **Activity:** the chapter has had no events since the [June 2025 meetup](https://www.meetup.com/stockholm-dbt-meetup/events/307908713/).

### Step 2: Other local meetups and conferences

- **[Data & AI Stockholm](https://dataaistockholm.com/):** the best source. Its [Substack recaps](https://dataaistockholm1.substack.com/p/data-ai-in-practice-from-foundations) name speakers with their employers. Its [summit page](https://dataaistockholm.com/summit) lists 18 speakers with LinkedIn links. The summit is on 14 October 2026.
- **[Snowflake User Group Stockholm](https://usergroups.snowflake.com/stockholm/):** its event pages render on the server. They list speakers, organisers and LinkedIn links. One 2026 session covered dbt.
- **A Luma event page** for a [Nextory talk](https://luma.com/4f8lqzsp) confirmed a speaker's role.
- **Low yield:**
  - The [Data Innovation Summit](https://datainnovationsummit.com/region/nordics/data-engineering-dataops-summit/) page shows only a few speakers.
  - The [dbt Summit speaker list](https://www.getdbt.com/dbt-summit/speakers) has no Swedish-employer speakers.
  - The [Snowflake World Tour Stockholm](https://www.snowflake.com/en/world-tour/stockholm/speakers/) speakers render in the browser only.
  - The [Stockholm Open Source Data Infrastructure meetup](https://www.meetup.com/stockholm-open-source-data-infrastructure-meetup/events/?type=past) renders in the browser only.
  - [dev.events](https://dev.events/meetups/EU/SE/Stockholm/data) lists only online events and two summits.

### Step 3: Company blogs

- **No dbt content:** the [Epidemic Sound Medium feed](https://medium.com/feed/epidemicsound) was empty. The [Klarna engineering feed](https://engineering.klarna.com/feed) timed out.
- **Moved elsewhere:** [Robert Sahlin's Medium feed](https://medium.com/feed/@robertsahlin) is empty because the writing is now on Substack.
- **Result:** no emerging voices were found. An emerging voice is someone who publishes about dbt but has no talk on record.

### Step 4: Women-in-data communities

- **[WiDS Sweden 2025](https://wids.confetti.events/wids2025):** mostly machine learning and AI. Its organisers include people who run data platforms at Handelsbanken, H&M and Spotify.
- **[Women on Snowflake](https://usergroups.snowflake.com/events/details/snowflake-women-on-snowflake-presents-deep-dive-dbt-projects-on-snowflake/cohost-stockholm):** co-hosted a dbt-on-Snowflake deep dive with the Stockholm user group in January 2026. It gave the only tier-1 lead.
- **Rule:** speakers were taken only from the communities' own events. No one's gender is recorded or guessed.

### Step 5: Job ads

- **LinkedIn Jobs, logged out:** a search for dbt around Stockholm. Up to 150 ads were checked for the whole word "dbt". 62 ads at 55 companies mention it.
- **Who is hiring:** the ads are spread thinly. Storytel, Solita, NOBA Bank, Lovable, Etraveli, Avalanche Studios and Adavo posted 2 each.

### Step 6: Location pass

- **Method:** each person's base was looked up on public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
- **Best source:** meetup.com RSVP lists. They give the profile city of the person who spoke at that event.
- **Result:** 11 people were placed, 6 in the region and 5 elsewhere. Unknown locations fell from 21 to 10.

### Step 7: LinkedIn pass

- **Method:** up to two LinkedIn searches per person, using search results only. No LinkedIn page was opened.
- **Who:** 7 past chapter speakers without a location.
- **Result:** 3 people were placed. Filip Vitez is in Stockholm. Niklas Kullberg is in the Uppsala area and Salma Bakouk in New York. 7 locations are still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **Data & AI Stockholm** is the city's most active data community. Its recaps and summit page are far more efficient than company blogs.
  - **Snowflake user group pages** list speakers, hosts and LinkedIn links without a browser. Use them for any city where meetup.com renders in the browser only.
  - **meetup.com RSVP lists** placed most of the past chapter speakers.
- **Sources that didn't:**
  - **Swedish company engineering blogs** were empty or unreachable.
  - **Conference speaker pages** (dbt Summit, Snowflake World Tour, Data Innovation Summit) gave almost nothing.
- **Watch out for:**
  - **Stockholm's dbt signal is indirect.** It comes through semantic-layer and BI talks, often by Omni customers, rather than dbt-branded content.
  - **Tier 1 has one person.** The strict tier-1 rule needs a dbt item from 2024 onwards, so most proven speakers stay in tier 2.
  - **The past speakers are old.** Most of the 19 spoke in 2023, so their roles may have changed.
  - **Stale employers:** Filip Vitez is recorded at Northvolt, but the LinkedIn result shows a newer employer, veyra.
  - **dbt Labs staff:** Ludwig Sewall is recorded at Solita, but the June 2025 chapter talk lists a dbt Labs role. Lucas Paes also works at dbt Labs.

## 3. Key leads

- **First-time speakers:** none were found. These are the strongest leads who have not yet spoken at the chapter:
  - **Daniele Abbatelli**, Drake Analytics: [Deep dive: dbt projects on Snowflake](https://usergroups.snowflake.com/events/details/snowflake-women-on-snowflake-presents-deep-dive-dbt-projects-on-snowflake/cohost-stockholm) (January 2026). This is the only tier-1 lead.
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

## 4. Before outreach

- [ ] **Confirm current roles** of the 2023 chapter speakers before asking them back.
- [ ] **Check for dbt use** at Svedea, Tele2, Adapteo and Funnel. Their speakers talk about data platforms, but dbt is not confirmed.
- [ ] **Check unconfirmed details.** Ece Kural's employer is not stated. Baaba Bonuedie's city is not confirmed, since Nordea has several Nordic hubs.
- [ ] **Decide on Uppsala.** Mammar Rahmani, Fernando Brito and Niklas Kullberg are marked outside. Flip them if commuter towns count.
- [ ] **Treat visiting speakers as visitors.** Ernesto Ongaro is in Dublin, Kshitij Aranke and Stephen Murphy in London, and Salma Bakouk in New York.
- [ ] **Exclude dbt Labs staff** from speaker outreach: Ernesto Ongaro, Kshitij Aranke, Lucas Paes, Mike Burke and probably Ludwig Sewall.

## 5. Next run

- **People still without a location:** 7.
  - Searched twice on LinkedIn, no profile link: Mauro Luzzatto, Guillaume Fetter, Linus Wågberg and Erik Lehto.
  - Never searched on LinkedIn: Mike Burke, Akanksha Bhagwanani and Isabella Renzetti.
- **Sources not yet searched:**
  - Substack and Medium authors who write about dbt. The city has no emerging voices yet.
  - Stockholm data groups through the meetup.com `gql2` endpoint, which the first build could not use.
  - The full Data Innovation Summit speaker list.
- **What to try first:** a `gql2` group search around Stockholm, to find first-time speakers in other meetups' line-ups.

## 6. Replication prompt

````
You are extending the Stockholm dbt dataset: stockholm/stockholm_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. The region is the Stockholm metro area;
Uppsala counts as outside. Read stockholm/SEARCH_METHOD.md first, then research/README.md
and the briefs it links (raw-format.md, location-task.md, linkedin-task.md).

Budget about 25 web searches. Prefer direct fetches and APIs.

1. First-time speakers: the city has none yet. Search Substack, Medium and company blogs for
   Stockholm authors who write about dbt, and record each author's employer.
2. New talks: a meetup.com gql2 groupSearch around Stockholm, then the past events of each
   data group. Also new Data & AI Stockholm recaps and Snowflake User Group Stockholm events.
3. Women-in-data: new WiDS Sweden and Women on Snowflake events. Take speakers only from
   the community's own events.
4. Locations: the 7 people still unknown, listed in SEARCH_METHOD.md §5.
Rules: never open LinkedIn pages, use only search results. Record professional information
only, never gender, and pronouns only when self-stated. Assemble with research/assemble.py
--base, apply locations with research/apply_locations.py, and run research/validate.py.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build, from one research pass and a LinkedIn Jobs scan. 90 companies, 51 people and 62 dbt job ads at 55 companies. 40 proven speakers, 11 featured and no emerging voices. 19 people had spoken at the chapter. 17 people had LinkedIn profiles. |
| 2026-10-01 | 2 | Location pass from public pages. 11 people placed: 6 in the region and 5 elsewhere. Unknown locations fell from 21 to 10. |
| 2026-10-01 | 2 | LinkedIn pass on 7 past chapter speakers. 3 placed: 1 in the region and 2 elsewhere. 7 locations are still unknown, and 20 people now have LinkedIn profiles. |
