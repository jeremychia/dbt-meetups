# San Francisco dbt search: method, lessons and replication prompt

This file goes with `san_francisco_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-10-01
- **Goal:** find people in the SF Bay Area who could **speak at** (or attend) the [San Francisco dbt Meetup](https://www.meetup.com/san-francisco-dbt-meetup/), and the local companies that use dbt.
- **Region:** the nine SF Bay Area counties. San Francisco, the Peninsula (San Mateo, Menlo Park, Portola Valley) and the South Bay (Sunnyvale) count. Santa Cruz, San Diego and Irvine do not.

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 61 |
| People | 76 |
| Tier 1 leads | 23 |
| First-time speakers (publish, no talk yet) | 10 |
| Proven speakers | 51 |
| Spoke at this chapter before | 36 |
| Based in the region | 39 |
| Based elsewhere | 11 |
| Location unknown | 26 |
| With a LinkedIn profile | 7 |
| Job ads mentioning dbt | 3 |
| Past chapter meetups | 13 |
<!-- at-a-glance:end -->

## 1. How the search was done

The first build had about 20 web searches before the shared session limit ran out. The rest came from about 50 page fetches and the GitHub API. Scoring follows [`../berlin_planning/SEARCH_METHOD.md`](../berlin_planning/SEARCH_METHOD.md) §1 Step 6.

### Step 1: Chapter history

- **What was added:** every named speaker in `../enriched/san-francisco-dbt-meetup.json`, with their talk.
- **Range:** 13 meetups, from 2019-06-12 to 2026-08-26.
- **Yield:** 36 people who have spoken at the chapter. One of them, Dori Wilson, was merged with a newer record at Chime.

### Step 2: dbt conference agendas

- **[dbt Summit 2026 sessions by role](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role):** the best page. It names speakers and companies at Zipline, Sigma, LangChain, DoorDash and Okta on one page.
- **[dbt Summit 2026 keynotes](https://www.getdbt.com/blog/dbt-summit-2026-keynotes-product-sessions):** dbt Labs staff only.
- **[Coalesce 2025 sessions overview](https://www.getdbt.com/blog/what-to-expect-from-sessions-at-coalesce-2025):** Okta and Cribl sessions, but most speakers are not named.
- **Session pages:** the individual dbt Summit and Coalesce session pages returned 404.

### Step 3: Vendor customer stories and blogs

- **[Hex customer stories](https://hex.tech/customers/):** Chime, LangChain, Figma, Notion and Modern Treasury. Each names Bay Area analytics staff and states their stack.
- **[Omni blog and case studies](https://omni.co/blog):** Cribl and Handshake, plus posts by Omni staff.
- **[Monte Carlo case studies](https://montecarlo.ai/case-studies/):** PagerDuty and Credit Karma. Neither mentions dbt.
- **[dbt Developer Blog authors](https://docs.getdbt.com/blog/authors):** authors at Mainspring Energy, Merit, Census, Mode and Fivetran. Most posts are from 2022–23.

### Step 4: Women-in-data communities

People were taken only from each community's own events. Nobody's gender is recorded.

- **[Snowflake Women in Data Bay Area](https://www.snowflake.com/event/women-in-data-bay-area-20260128) (January 2026):** 5 speakers, from DoorDash, Ross Stores, CrowdStrike, Engage3 and Snowflake.
- **[Hightouch Women in Data SF](https://hightouch.com/events/women-in-data-meetup) (February 2023):** 1 keynote speaker.
- **[WiDS Berkeley](https://wids.berkeley.edu/speakers):** WiDS means Women in Data Science. The page shows the 2023 line-up, including an analytics engineering leader at Meta.
- **[Women in Big Data Bay Area](https://www.meetup.com/women-in-big-data-bay-area/):** the group no longer exists.

### Step 5: Other local meetups and company blogs

- **[Snowflake Bay Area User Group](https://usergroups.snowflake.com/san-francisco/):** lists its 2 leaders, but not its event speakers.
- **[MotherDuck SF meetups](https://motherduck.com/events/motherduck-duckdb-july-meetup-2026.md):** DuckDB and agent talks, with no dbt speakers.
- **[AI Council Bay Area](https://www.aicouncil.com/bay-2025):** Data Council was renamed, and the page lists no speakers.
- **Company Medium feeds:** [Gusto](https://medium.com/feed/gusto-engineering) and Faire had no dbt posts. [Airbnb](https://medium.com/feed/airbnb-engineering), Lyft and Instacart returned HTTP 429 (too many requests).

### Step 6: GitHub and job ads

- **[GitHub user search](https://github.com/search?q=dbt+location%3A%22San+Francisco%22&type=users)** for "dbt" in the bio and a San Francisco location: mostly job-seeker portfolios. Two people were kept.
- **Job ads:** only 3, found through web search, at World, Perplexity and Slash. No LinkedIn Jobs scan was run.

### Step 7: Location and LinkedIn passes (2026-10-01)

- **Page fetches:** 18 people placed, 12 in the region and 6 outside.
  - The Meetup `gql2` endpoint gave the profile city of each event's hosts and RSVPs.
  - GitHub profiles gave the rest.
- **LinkedIn search results:** 7 people placed, 3 in the region and 4 outside. No LinkedIn page was opened.
- **Still unknown:** 27 people.

## 2. What we learnt

- **Sources that worked:**
  - **The dbt Summit "sessions by role" post** names speakers and companies on one page. It is the cheapest way to find Bay Area talks.
  - **Hex and Omni customer stories** name analytics engineers at San Francisco companies and state their stack. They are the cheapest route to practitioners.
  - **Meetup `gql2` RSVPs** placed most past chapter speakers. The member must be the RSVP or host of the event they spoke at.
- **Sources that didn't:**
  - **Medium feeds** for Airbnb, Lyft and Instacart returned HTTP 429, so Bay Area company tech blogs are still unscanned.
  - **dbt Summit and Coalesce session pages** returned 404. So did the getdbt.com case studies and the Datafold and Lightdash customer pages.
  - **GitHub user search** finds mostly job-seeker portfolios. Only a few are usable speaker leads.
- **Watch out for:**
  - **Vendors dominate the Bay Area.** Hex, Omni, Sigma, Fivetran and dbt Labs staff publish the most. Treat them below practitioners at non-vendor companies.
  - **Fivetran and dbt Labs have merged.** Decide whether Fivetran and Census staff fall under the dbt Labs outreach exclusion. This affects Toby Mao and Donny Flynn (Fivetran) and Boris Jabes (Census). Dave Fowler already sits under dbt Labs.
  - **Featured people:** a featured person is quoted or profiled in someone else's content, but has no talk or post of their own. Many San Francisco leads are featured, so ask them for a first talk rather than a repeat.

## 3. Key leads

- **First-time speakers** (practitioners with dbt material and no talk on record):
  - **Priya Gupta**, Head of Data, Cribl. Quoted at length on dbt docs as the single source of truth for AI analytics: [Omni case study](https://omni.co/blog/case-study-cribl).
  - **Jordan Farrer**, Director of Data Science & Analytics, Chime. Featured on Chime's AI context and evaluation set-up on Snowflake and dbt: [Hex story](https://hex.tech/customers/chime/).
  - **Tyler Ritter**, Senior Analytics Engineer, Handshake. Featured on migrating a ten-year-old analytics estate in eight weeks: [Omni case study](https://omni.co/blog/case-study-handshake).
  - **Chang Sun**, Analytics Engineering Lead, Modern Treasury: [Hex story](https://hex.tech/customers/modern-treasury/).
  - **Charlie Summers**, Staff Software Engineer, Merit. Wrote about turning event streams into tables with dbt (2022): [dbt Developer Blog](https://docs.getdbt.com/blog/demystifying-event-streams).
- **Anchor speakers:**
  - **Harsha Reddy**, DoorDash. dbt Summit 2026 talk on DoorDash's analytics development process with dbt and ThoughtSpot: [agenda](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role).
  - **Logan Cochran**, Analytics Engineer, LangChain. dbt Summit 2026 talk on keeping AI agents to agreed definitions: [agenda](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role).
  - **Matt Senick**, Senior Analytics Engineer, Sigma. dbt Summit 2026 talk and a post on the semantic layer with dbt and Dagster: [Sigma blog](https://www.sigmacomputing.com/blog/semantic-layer-dbt-dagster). Sigma is a vendor.
  - **Josh Wills**, DatologyAI. Creator of dbt-duckdb, based in San Francisco: [GitHub](https://github.com/jwills).
- **Connectors:**
  - **Vince Faller** organised the 2026-08-26 chapter meetup and has spoken there twice: [Meetup profile](https://www.meetup.com/members/481607209/).
  - **Divya Koppolu** and **John Miller** run the [Snowflake Bay Area User Group](https://usergroups.snowflake.com/san-francisco/), which has about 8,700 members.
  - **Karen Hsieh** organised the 2025-04, 2025-10 and 2026-06 chapter meetups: [chapter page](https://www.meetup.com/san-francisco-dbt-meetup/).

## 4. Before outreach

- [ ] **Check the tier-1 people raised by the rule.** An emerging voice is someone who publishes about dbt but has no talk on record. The rule raises any emerging voice with a post from 2024 onwards to tier 1. That includes 4 vendor bloggers: Katie Bauer and Rachel Herrera (Hex), and Jamie Davidson and Colin Zima (Omni). Deepanshu Girsa is tier 1 on one personal repo.
- [ ] **Skip or re-rank tier-1 people outside the region.** Lexi Galantino is in San Diego, Pooja Crahen in New York and Emily Hawkins in Boston. Hamzah Chaudhary is in London and Juan Manuel Perafan in Norwalk. Izzy Miller is tier 2 because Santa Cruz is outside the nine counties. Raise Izzy Miller back to tier 1 if you count it.
- [ ] **Confirm the 27 unknown locations.** They include Matt Senick, Logan Cochran and Harsha Reddy. Harsha Reddy has two possible LinkedIn matches, in Fremont and Santa Clara.
- [ ] **Check the weak location calls.** Jason Lally, Boris Jabes, Raul Maldonado and Pradnesh Patil were placed by a name match to a chapter member only.
- [ ] **Resolve conflicting profiles.** Karen Hsieh's Meetup accounts say Taipei. Gleb Mezhanskiy's Meetup profile says San Francisco but GitHub says New York.
- [ ] **Confirm current employers.** The Chime story lists Dori Wilson at Chime, not Recce. Several dbt Developer Blog authors' roles date from 2022–23.
- [ ] **Leave out dbt Labs staff** (excluded from outreach), and decide on Fivetran and Census staff.

## 5. Next run

- **Run the LinkedIn pass first.** 53 tier-1 and tier-2 people are still `not_searched`.
- **Run a LinkedIn Jobs guest scan.** The file has only 3 job ads, all from web search.
- **Use the dbt Summit speaker pages** (`getdbt.com/dbt-summit/speakers/<slug>`), which give session titles. They worked for Boston and Seattle.
- **Retry the Medium feeds** for Airbnb, Lyft and Instacart. Find the author of Instacart's "Adopting dbt" post.
- **Search for named speakers** at DocuSign, Figma and Instacart, which have a dbt talk but no named speaker.
- **Find GitHub logins** for the unknown-location people at Hex, Omni, LangChain, DoorDash, Zipline, Sigma and Okta.

## 6. Replication prompt

````
You are extending my dataset of SF Bay Area companies that use dbt, and people who could speak at
or attend the San Francisco dbt Meetup. The file is san_francisco/san_francisco_dbt_companies.json
in /Users/jeremychia/Documents/Github/dbt-meetups. Read san_francisco/SEARCH_METHOD.md, then
research/README.md and the briefs it links (raw-format.md, location-task.md, linkedin-task.md).
The region is the nine SF Bay Area counties.

Budget about 25 web searches. Try these first:
1. LinkedIn search results for tier 1-2 people with linkedin_confidence "not_searched".
2. A LinkedIn Jobs guest scan (keywords=dbt, San Francisco Bay Area); keep ads with the whole word dbt.
3. dbt Summit speaker pages (getdbt.com/dbt-summit/speakers/<slug>) for Bay Area employers.
4. Hex, Omni and Sigma customer stories published since metadata.generated_at.
5. Medium feeds for Airbnb, Lyft and Instacart (medium.com/feed/<publication>).

Rules: never fetch LinkedIn pages; use only search results. Public professional information only;
never guess gender, and record pronouns only when self-stated. Assemble with research/assemble.py
--base, run research/validate.py (must print ok), and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build: dbt Summit 2026 and Coalesce 2025 agendas, vendor customer stories (Hex, Omni, Monte Carlo), the dbt Developer Blog, the Snowflake Bay Area User Group, 3 women-in-data events, GitHub user search and job ads from web search. Past chapter speakers added from `../enriched/san-francisco-dbt-meetup.json`. 61 companies (36 on the watchlist), 76 people, 3 job ads, 13 past meetups. Split: 51 proven speakers, 10 emerging voices, 13 featured, 2 with no public content. Tiers: 24 tier 1, 41 tier 2, 9 tier 3, 2 connectors. 36 people had already spoken at the chapter. |
| 2026-10-01 | 1 | Location pass: 18 people placed from Meetup host and RSVP profiles and GitHub, 12 in the region and 6 outside. |
| 2026-10-01 | 1 | LinkedIn pass: 7 people placed from LinkedIn search results, 3 in the region and 4 outside. 27 people are still unknown. |
