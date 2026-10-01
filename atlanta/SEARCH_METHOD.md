# Atlanta dbt search: method, lessons and replication prompt

This file goes with `atlanta_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in the Atlanta metro who could **speak at** (or attend) the [Atlanta dbt Meetup](https://www.meetup.com/atlanta-dbt-meetup-group/), and the local companies that use dbt.
- **Region:** the Atlanta metro. Atlanta, Sandy Springs, Buckhead and Alpharetta count.

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 81 |
| People | 81 |
| Tier 1 leads | 11 |
| First-time speakers (publish, no talk yet) | 14 |
| Proven speakers | 51 |
| Spoke at this chapter before | 17 |
| Based in the region | 64 |
| Based elsewhere | 4 |
| Location unknown | 13 |
| With a LinkedIn profile | 11 |
| Job ads mentioning dbt | 35 |
| Past chapter meetups | 8 |
<!-- at-a-glance:end -->

## 1. How the search was done

The first build used about 18 web searches, plus a logged-out LinkedIn Jobs scan. An extension on 2026-10-01 used about 22 more searches and about 30 page fetches, mostly of user-group and conference pages. Scoring follows [`../berlin_planning/SEARCH_METHOD.md`](../berlin_planning/SEARCH_METHOD.md) §1 Step 6.

### Step 1: Chapter history

- **What was added:** every named speaker in `../enriched/atlanta-dbt-meetup-group.json`, with their talk.
- **Range:** 8 meetups, from 2023-03-29 to 2026-07-21. The usual venue is Aimpoint Digital, 7000 Central Parkway, Sandy Springs.
- **Yield:** 17 people who have spoken at the chapter.
- **Not run:** the Meetup `gql2` past-events query for the chapter. A plain fetch of the events page renders an empty list.

### Step 2: Local user groups and societies

Atlanta's live data community is on the Bevy event platform (Snowflake and Tableau user groups) and in TAG societies, not on Meetup. TAG is the Technology Association of Georgia.

- **[Snowflake User Groups Atlanta](https://usergroups.snowflake.com/atlanta/):** organisers, the Improving venue in Alpharetta, and 2025–26 speakers. Most speakers are Snowflake staff.
- **[Atlanta Tableau User Group](https://usergroups.tableau.com/atlanta-tableau-user-group/):** speakers from May and September 2025, and February 2026. The February 2026 panel on BI and AI was at Cox Enterprises' head office.
- **[TAG calendar](https://members.tagonline.org/calendar):** event detail pages name speakers with employers, but the calendar listing does not.
  - The [Data Science & AI Society](https://members.tagonline.org/calendar/Details/tag-s-data-science-ai-society-presents-2026-predictions-for-data-science-ai-1611623?sourceTypeId=Hub) January 2026 panel had speakers from Delta, McKesson, Macy's and Southern Company.
  - Its ["Human Side of AI" panel](https://members.tagonline.org/calendar/Details/the-human-side-of-ai-who-s-the-boss-responsibility-and-accountability-with-agentic-ai-presented-by-tag-data-science-ai-society-1929040) on 2026-10-22 names 4 speakers.
  - The [Data Governance Society board](https://www.tagonline.org/societies/data-governance/) lists 14 members.
- **[Amplitude Community × FanDuel career panel](https://luma.com/bldr4v8l):** 4 panellists and a host.
- **Organisers only:** the [Atlanta Databricks User Group](https://usergroups.databricks.com/atlanta-databricks-user-group/) and [PyData Atlanta](https://www.meetup.com/pydata-atlanta/). PyData Atlanta now runs monthly data happy hours.
- **Low yield:** [Data Science ATL](https://www.meetup.com/data-science-atl/) is mostly vendor webinars.

### Step 3: Conferences

- **[COLLIDE Data + AI Conference 2026](https://datasciconnect.com/events/collide/):** the largest list of Atlanta data leaders, held in Sandy Springs. 12 of its 32 speakers were recorded. It shows no session titles.
- **dbt conferences:** searches found no Atlanta-employer sessions at Coalesce 2025 or dbt Summit 2026. The [Coalesce 2025 speakers page](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/speakers) renders with JavaScript, so a fetch returns nothing.
- **Dead ends:** [DevNexus](https://devnexus.com/speakers) shows only its 2027 shell. [SQL Saturday](https://sqlsaturday.com/) shows only 2027 dates. [DAMA Georgia](https://calendar.kennesaw.edu/event/corporate-spotlight-dama-international) named no panellists. The [Data Tech 2026](https://datatech2026.sched.com/directory/speakers) agenda is for a Minnesota conference.

### Step 4: Company blogs

- **[Chick-fil-A tech blog](https://medium.com/feed/chick-fil-atech):** its Medium feed gave author names and full text in one fetch. Two 2025 posts on data governance and the analytics platform name 4 authors. Neither mentions dbt.
- **[Aimpoint Digital blog](https://www.aimpointdigital.com/blog):** a July 2026 post on dbt Agents. Its authors are not in Atlanta.
- **Other Medium feeds** returned HTTP 429 (too many requests) for every guessed publication. The guesses for Mailchimp, Cox, Home Depot, Calendly, Salesloft and Greenlight were not confirmed.
- **[dbt Developer Hub blog authors](https://docs.getdbt.com/blog/authors):** none with an Atlanta employer.

### Step 5: GitHub and LinkedIn search results

- **[GitHub user search](https://github.com/search?q=dbt+location%3AAtlanta&type=users)** (`location:Atlanta` with dbt, data engineer or snowflake in the bio): 11 users mention dbt. 9 emerging voices and Stewart Bryson were recorded. An emerging voice is someone who publishes about dbt but has no talk on record.
- **LinkedIn search results:** 2 data practitioners with no public content, from search summaries that mention dbt.
- **Open web search** for Medium, dev.to and Substack authors with an Atlanta employer found nothing usable.

### Step 6: Women-in-data communities

People are taken only from each community's own events. Nobody's gender is recorded. No Atlanta source yielded people.

- **Dormant or gone:** [Atlanta WiMLDS](https://www.meetup.com/atlanta-wimlds/) has no events. [Women in Big Data Atlanta](https://www.meetup.com/women-in-big-data-atlanta-chapter/) was not found. Women Who Code closed in 2024.
- **Not reachable:** the Georgia State University events site did not resolve, and the [WiDS](https://www.widsworldwide.org/) regional page returned 404. WiDS means Women in Data Science.

### Step 7: Job ads

- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt), logged out:** up to 150 Atlanta-area ads checked for the whole word "dbt". 35 ads at 31 companies mention it.

### Step 8: Location and LinkedIn passes (2026-10-01)

- **Page fetches:** 6 people placed, 5 in the region and 1 outside. The evidence was speaker bios and recent in-person talks at an employer with an Atlanta office.
- **LinkedIn search results:** 4 people placed, all in the region. No LinkedIn page was opened.
- **Still unknown:** 15 people.

## 2. What we learnt

- **Sources that worked:**
  - **Bevy user-group pages** list speakers and organisers with employers, and can be fetched directly.
  - **TAG event detail pages** name speakers with employers. The society pages list board members.
  - **GitHub user search** was the only source that found Atlanta emerging voices.
  - **The Chick-fil-A Medium feed** gave authors and full text in one fetch, cheaper than searching.
- **Sources that didn't:**
  - **Meetup** is not where Atlanta's data community meets. Most data groups are dormant or run vendor webinars.
  - **Women-in-data groups** in Atlanta are dormant or gone. Try the Georgia Tech, Georgia State or TAG DEI society calendars instead.
  - **Medium feeds** for other Atlanta companies returned HTTP 429 to curl.
- **Watch out for:**
  - **GitHub leads are mostly portfolio or course projects.** Their tier 1 comes from the scoring rule, not from judgement.
  - **Corporate panels are not dbt talks.** Most COLLIDE, TAG and Tableau speakers are data leaders who have not spoken about dbt.
  - **dbt Labs staff** spoke at several chapter events, including a recorded Coalesce watch party. Their locations are unknown, and they are labelled in the cockpit.

## 3. Key leads

- **First-time speakers:**
  - **Xiangshi Yin**, Staff Data Engineer, Shopify, based in Atlanta. Public dbt exploration repo, plus a data programming course repo: [dbt-exploration](https://github.com/xiangshiyin/dbt-exploration).
  - **Elizabeth Williams**, Chick-fil-A. Co-wrote, with past speaker Aaron Reese, a 2025 post on governed self-service analytics: [Chick-fil-A tech blog](https://medium.com/chick-fil-atech/caring-for-our-data-a-journey-to-enhanced-performance-scalability-and-governance-2e4cd779ad0d). A possible co-speaker pair.
  - **Caleb Lampert** and **Pat Pickren**, Chick-fil-A. Wrote on certifying data assets, which fits dbt contracts and tests: [post](https://medium.com/chick-fil-atech/data-asset-certification-how-soup-can-inspire-us-to-steward-our-data-better-4d1812b0b128).
  - **Kablan Assebian**, data scientist and analytics engineer. Built a dbt, Postgres and GitHub Actions pipeline for SaaS revenue metrics (May 2026): [repo](https://github.com/Kablan-ASBN/saas_metrics_pipeline_v2).
  - **Rutuja Gawade**, BI & Analytics Engineer, Truist: [portfolio project](https://github.com/rutujagawade-data/wholesale-banking-sales-pipeline-dashboard).
- **Anchor speakers:**
  - **Stewart Bryson**, Atlanta. A dbt project that builds the TPC-DI benchmark warehouse on Snowflake and BigQuery: [dbt-tpcdi](https://github.com/stewartbryson/dbt-tpcdi). The GitHub bio says "writer, speaker and podcast guest".
  - **Kun Zhu**, VP of Data and AI, NCR Voyix. Spoke and co-organised at the June 2025 meetup at NCR Voyix's head office: [event](https://www.meetup.com/atlanta-dbt-meetup-group/events/307908198/).
  - **Megha Panda**, HD Supply. Talk on how adopting dbt sped up data products, at the same event: [event](https://www.meetup.com/atlanta-dbt-meetup-group/events/307908198/).
  - **Aaron Reese**, Enterprise Architect, Chick-fil-A. Chapter talk in 2023, and the 2025 post above: [event](https://www.meetup.com/atlanta-dbt-meetup-group/events/291536809/).
- **Connectors:**
  - **Zoe Yim** is the current chapter host, and ran the July 2026 social: [event](https://www.meetup.com/atlanta-dbt-meetup-group/events/315472808/).
  - **Brent Brewington**, Aimpoint Digital, co-organised the chapter in 2023–24. Aimpoint's office is the usual venue: [chapter page](https://www.meetup.com/atlanta-dbt-meetup-group/).
  - **Andy Brown**, **Danny Bryant** and **Michael Jain** organise Snowflake Atlanta: [group page](https://usergroups.snowflake.com/atlanta/).
  - **Anna Foard** and **Jennifer Lisborg** co-lead the Atlanta Tableau User Group: [event](https://usergroups.tableau.com/events/details/tableau-atlanta-tableau-user-group-presents-atlanta-tableau-user-group-meeting-02242026/).
  - **Kenneth Viciana** chairs the TAG Data Governance Society: [board](https://www.tagonline.org/societies/data-governance/).
  - **Jeremy Jacobson** organises PyData Atlanta, whose happy hours fit the chapter's social format: [group page](https://www.meetup.com/pydata-atlanta/).

## 4. Before outreach

- [ ] **Check the tier-1 people raised by the rule.** Ken Slate's project has no dbt in it. The Chick-fil-A certification post does not mention dbt. Luke Carter wrote about product prioritisation, not analytics engineering.
- [ ] **Check Jessica M. Rudd's talk record.** The record says emerging voice, but the GitHub profile keeps a tech-talks app.
- [ ] **Confirm the TAG panel took place.** Markis Jaudon Ramon Piper, Amari Hanes, Dhruv Alexander and Shalmali Joshi are on a panel set for 2026-10-22.
- [ ] **Confirm the 15 unknown locations.** They include Cox Automotive's 2024 speakers, the FanDuel career panel and Mike Sandt. Mike Sandt has an Atlanta LinkedIn profile, but nothing ties it to Salesloft.
- [ ] **Check the medium location calls.** Grant Cloud's LinkedIn result says Atlanta, but its text mentions a move to Kalshi in New York. Zach Lancaster was matched as "Zachary Lancaster" at WarnerMedia.
- [ ] **Skip or re-rank people outside the region.** Francisco Moya is in Medellín, and Nate Nunta is in the Bay Area.
- [ ] **dbt Labs staff are labelled.** Nate Nunta, Katherine Brock, Brandon Sweeney, Jason Ganz, Erica Louie and Cole Fraser work there. They can speak, but check the line-up has practitioners first.

## 5. Next run

- **Run the LinkedIn pass first.** 36 tier-1 and tier-2 people are still `not_searched`.
- **Run the Meetup `gql2` past-events query** for the chapter, with `sort: DESC`, to capture recent organisers and RSVPs.
- **Try the Georgia Tech, Georgia State and TAG DEI society calendars** for women-in-data speakers.
- **Read the TAG DataPalooza speaker list** in October, and COLLIDE session titles once published.
- **Confirm Medium publication names** for Mailchimp, Cox, Home Depot, Calendly, Salesloft and Greenlight, and read their feeds.
- **Find Stewart Bryson's talk links**, which are not in the file yet.

## 6. Replication prompt

````
You are extending my dataset of Atlanta-metro companies that use dbt, and people who could speak
at or attend the Atlanta dbt Meetup. The file is atlanta/atlanta_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read atlanta/SEARCH_METHOD.md, then
research/README.md and the briefs it links (raw-format.md, location-task.md, linkedin-task.md).
The region is the Atlanta metro (Atlanta, Sandy Springs, Alpharetta and nearby).

Budget about 25 web searches. Try these first:
1. LinkedIn search results for tier 1-2 people with linkedin_confidence "not_searched".
2. Meetup gql2 past events (sort: DESC) for atlanta-dbt-meetup-group.
3. TAG event detail pages, Bevy pages for Snowflake and Tableau Atlanta, and COLLIDE.
4. GitHub user search (dbt location:Atlanta) for new first-time speakers.
5. Georgia Tech, Georgia State and TAG DEI calendars for women-in-data speakers.

Rules: never fetch LinkedIn pages; use only search results. Public professional information only;
never guess gender, and record pronouns only when self-stated. Assemble with research/assemble.py
--base, run research/validate.py (must print ok), and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build: dbt conference agendas filtered to local employers, company blogs, local meetups and user groups, women-in-data communities, and a LinkedIn Jobs scan. Past chapter speakers added from `../enriched/atlanta-dbt-meetup-group.json`. 56 companies (16 on the watchlist), 36 people, 35 job ads at 31 companies, 8 past meetups. Split: 25 proven speakers, 5 emerging voices, 6 featured. Tiers: 4 tier 1, 19 tier 2, 5 tier 3, 8 connectors. 17 people had already spoken at the chapter. |
| 2026-10-01 | 2 | Extension: TAG society calendars and board pages, COLLIDE 2026, Tableau, Snowflake and Databricks user groups, an Amplitude Community panel and GitHub user search. 45 new people, for 81 companies (38 on the watchlist) and 81 people. Split: 51 proven speakers, 14 emerging voices, 14 featured, 2 with no public content. Tiers: 11 tier 1, 36 tier 2, 18 tier 3, 16 connectors. |
| 2026-10-01 | 2 | Location pass: 6 people placed from speaker bios and recent in-person talks, 5 in the region and 1 outside. |
| 2026-10-01 | 2 | LinkedIn pass: 4 people placed from LinkedIn search results, all in the region. 15 people are still unknown. |
