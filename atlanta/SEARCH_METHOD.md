# Atlanta: city notes

This file holds what is specific to Atlanta. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Atlanta dbt Meetup](https://www.meetup.com/atlanta-dbt-meetup-group/), data in `atlanta_dbt_companies.json`
- **Region:** the Atlanta metro. Atlanta, Sandy Springs, Buckhead and Alpharetta count.
- **First built:** 2026-09-24

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

## 1. Where to look in Atlanta

The first build used about 18 web searches, plus a logged-out LinkedIn Jobs scan. The 2026-10-01 extension used about 22 more searches and about 30 page fetches, mostly of user-group and conference pages. Leads are scored by the [central scoring rules](../research/README.md#3-scoring-rules).

Atlanta's live data community is on the Bevy event platform (Snowflake and Tableau user groups) and in TAG societies, not on Meetup. TAG is the Technology Association of Georgia.

### Chapter history

- **Past chapter speakers:** every named speaker in `../enriched/atlanta-dbt-meetup-group.json`, with the talk. 8 meetups, from 2023-03-29 to 2026-07-21, gave 17 people who have spoken at the chapter. The usual venue is Aimpoint Digital, 7000 Central Parkway, Sandy Springs.

### User groups and societies

- **[Snowflake User Groups Atlanta](https://usergroups.snowflake.com/atlanta/):** organisers, the Improving venue in Alpharetta, and 2025–26 speakers. Most speakers are Snowflake staff. Bevy pages list speakers and organisers with employers, and can be fetched directly.
- **[Atlanta Tableau User Group](https://usergroups.tableau.com/atlanta-tableau-user-group/):** speakers from May and September 2025, and February 2026. The February 2026 panel on BI and AI was at Cox Enterprises' head office.
- **[TAG calendar](https://members.tagonline.org/calendar):** event detail pages name speakers with employers, but the calendar listing does not. The society pages list board members.
  - **Data Science & AI Society, January 2026:** the [panel](https://members.tagonline.org/calendar/Details/tag-s-data-science-ai-society-presents-2026-predictions-for-data-science-ai-1611623?sourceTypeId=Hub) had speakers from Delta, McKesson, Macy's and Southern Company.
  - **"Human Side of AI" panel:** the [event](https://members.tagonline.org/calendar/Details/the-human-side-of-ai-who-s-the-boss-responsibility-and-accountability-with-agentic-ai-presented-by-tag-data-science-ai-society-1929040) on 2026-10-22 names 4 speakers.
  - **Data Governance Society board:** the [board page](https://www.tagonline.org/societies/data-governance/) lists 14 members.
- **[Amplitude Community × FanDuel career panel](https://luma.com/bldr4v8l):** 4 panellists and a host.
- **Organisers only:** the [Atlanta Databricks User Group](https://usergroups.databricks.com/atlanta-databricks-user-group/) and [PyData Atlanta](https://www.meetup.com/pydata-atlanta/). PyData Atlanta now runs monthly data happy hours.

### Conferences

- **[COLLIDE Data + AI Conference 2026](https://datasciconnect.com/events/collide/):** the largest list of Atlanta data leaders, held in Sandy Springs. 12 of its 32 speakers were recorded. It shows no session titles.

### Company blogs, GitHub and job ads

- **[Chick-fil-A tech blog](https://medium.com/feed/chick-fil-atech):** the Medium feed gave author names and full text in one fetch, cheaper than searching. Two 2025 posts on data governance and the analytics platform name 4 authors. Neither mentions dbt.
- **[Aimpoint Digital blog](https://www.aimpointdigital.com/blog):** a July 2026 post on dbt Agents. The authors are not in Atlanta.
- **[GitHub user search](https://github.com/search?q=dbt+location%3AAtlanta&type=users):** `location:Atlanta` with dbt, data engineer or snowflake in the bio. 11 users mention dbt. 9 first-time speakers and Stewart Bryson were recorded. This was the only source that found Atlanta first-time speakers.
- **LinkedIn search results:** 2 data practitioners with no public content, from search summaries that mention dbt.
- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt), logged out:** up to 150 Atlanta-area ads checked for the whole word "dbt". 35 ads at 31 companies mention it.

### Locations

- **Location pass (2026-10-01):** page fetches placed 6 people, 5 in the region and 1 outside. The evidence was speaker bios and recent in-person talks at an employer with an Atlanta office.
- **LinkedIn pass (2026-10-01):** LinkedIn search results placed 4 people, all in the region. No LinkedIn page was opened.

## 2. What didn't work here

- **Meetup:** not where Atlanta's data community meets. Most data groups are dormant or run vendor webinars. [Data Science ATL](https://www.meetup.com/data-science-atl/) is mostly vendor webinars.
- **Chapter events page:** a plain fetch renders an empty list. The Meetup `gql2` past-events query was not run.
- **dbt conferences:** searches found no Atlanta-employer sessions at Coalesce 2025 or dbt Summit 2026. The [Coalesce 2025 speakers page](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/speakers) renders with JavaScript, so a fetch returns nothing.
- **[DevNexus](https://devnexus.com/speakers):** shows only its 2027 shell.
- **[SQL Saturday](https://sqlsaturday.com/):** shows only 2027 dates.
- **[DAMA Georgia](https://calendar.kennesaw.edu/event/corporate-spotlight-dama-international):** named no panellists.
- **[Data Tech 2026](https://datatech2026.sched.com/directory/speakers):** the agenda is for a Minnesota conference.
- **Other Medium feeds:** every guessed publication returned HTTP 429 (too many requests). The guesses for Mailchimp, Cox, Home Depot, Calendly, Salesloft and Greenlight were not confirmed.
- **[dbt Developer Hub blog authors](https://docs.getdbt.com/blog/authors):** none with an Atlanta employer.
- **Open web search:** Medium, dev.to and Substack authors with an Atlanta employer gave nothing usable.
- **Women-in-data communities:** no Atlanta source yielded people. [Atlanta WiMLDS](https://www.meetup.com/atlanta-wimlds/) has no events. [Women in Big Data Atlanta](https://www.meetup.com/women-in-big-data-atlanta-chapter/) was not found. Women Who Code closed in 2024.
- **Unreachable sites:** the Georgia State University events site did not resolve. The [WiDS](https://www.widsworldwide.org/) (Women in Data Science) regional page returned 404.

## 3. Companies looked at

- **Chapter host:** Aimpoint Digital's Sandy Springs office is the usual venue. NCR Voyix hosted the June 2025 meetup at its head office.
- **Chick-fil-A** gave the most first-time speakers, through its tech blog.
- **Corporate panels are not dbt talks.** Most COLLIDE, TAG and Tableau speakers are data leaders who have not spoken about dbt.
- **GitHub leads are mostly portfolio or course projects.** The tier 1 on these comes from the scoring rule, not from judgement.

<!-- companies:start -->
80 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (3)</summary>

Aimpoint Digital, Cox Automotive / Cox Enterprises, NCR Voyix

</details>

<details><summary><b>Some dbt signal</b> (32)</summary>

Agoda, AT&T, CapTech, Chick-fil-A, CNN, Cox Automotive, Credigy, DiversiTech Corporation, FanDuel, FIS, Foxit, Grant Thornton (US), GreenSky, Greystar, HD Supply / The Home Depot, Incident IQ, Intuit Mailchimp, Massive, Navanta, OneTrust, Pyramid Consulting, Inc, Safe-Guard Products International, SCP Health, Slalom, Sovos, Stord, Talon Hiring Solutions, Tata Consultancy Services, Thought Logic Consulting, Trella Health, Waystar, Workday

</details>

<details><summary><b>Not verified</b> (45)</summary>

Allegro Analytics (local presence not confirmed), Americold, Amplitude (local presence not confirmed), Analytic Vizion (local presence not confirmed), Apex Systems (local presence not confirmed), Asian American Power Network, Atlanta Databricks User Group, Atlanta Tableau User Group, BlackRock, Cargill (local presence not confirmed), Cut-Thru Consulting (local presence not confirmed), Dagster (local presence not confirmed), Data Science ATL (DataSciConnect), Dataiku (local presence not confirmed), dbt Labs (local presence not confirmed), Delta Air Lines (local presence not confirmed), Elevance Health (local presence not confirmed), Equifax, Fox Corporation (local presence not confirmed), Georgia Tech Athletic Association, Georgia-Pacific, GoTo Foods, HD Supply (local presence not confirmed), Improving (Alpharetta), Institute for Insight, Georgia State University (local presence not confirmed), Johnson Controls (local presence not confirmed), McKesson (local presence not confirmed), Piedmont (local presence not confirmed), PrizePicks (local presence not confirmed), PyData Atlanta, Salesforce (Tableau), Salesloft (local presence not confirmed), Shopify, Snowflake (local presence not confirmed), Snowflake User Groups Atlanta, Southern Company (local presence not confirmed), TAG Data Governance Society, TAG Data Science & AI Society, The Coca-Cola Company, Truist, TSYS, Vanrish Technology, WBD (local presence not confirmed), Yum! Brands (local presence not confirmed), Zaxby's (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (3)</summary>

- https://medium.com/chick-fil-atech
- https://usergroups.snowflake.com/atlanta/
- https://www.aimpointdigital.com/blog

</details>

<details><summary><b>Other sources checked</b> (32)</summary>

- Local enriched chapter file: `enriched/atlanta-dbt-meetup-group.json`
- [Meetup past events (Atlanta dbt)](https://www.meetup.com/atlanta-dbt-meetup-group/events/?type=past) (nothing useful)
- [Coalesce 2025 speakers](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/speakers) (nothing useful)
- [Chick-fil-A tech blog RSS](https://medium.com/feed/chick-fil-atech)
- [Aimpoint Digital blog](https://www.aimpointdigital.com/blog)
- [Snowflake User Groups Atlanta](https://usergroups.snowflake.com/atlanta/)
- [Atlanta Tableau User Group Feb 2026](https://usergroups.tableau.com/events/details/tableau-atlanta-tableau-user-group-presents-atlanta-tableau-user-group-meeting-02242026/)
- [TAG Data Science & AI Society](https://members.tagonline.org/calendar/Details/tag-s-data-science-ai-society-presents-2026-predictions-for-data-science-ai-1611623?sourceTypeId=Hub)
- [PyData Atlanta](https://www.meetup.com/pydata-atlanta/)
- [Data Science ATL](https://www.meetup.com/data-science-atl/) (nothing useful)
- [Atlanta WiMLDS](https://www.meetup.com/atlanta-wimlds/) (nothing useful)
- [Women in Big Data Atlanta](https://www.meetup.com/women-in-big-data-atlanta-chapter/) (nothing useful)
- [Women in Data / WiDS Atlanta / R-Ladies / PyLadies Atlanta search](https://www.womenindata.org/) (nothing useful)
- [Databricks DAIS speaker page (Aaron Reese)](https://databricks.com/dataaisummit/speaker/aaron-reese) (nothing useful)
- [LinkedIn Jobs guest API (keywords=dbt, Atlanta-area)](https://www.linkedin.com/jobs/search?keywords=dbt)
- [Amplitude Community x FanDuel analytics career panel](https://luma.com/bldr4v8l)
- [TAG calendar (data, DEI and women-in-tech societies)](https://members.tagonline.org/calendar)
- [TAG DS&AI 'The Human Side of AI' (2026-10-22)](https://members.tagonline.org/calendar/Details/the-human-side-of-ai-who-s-the-boss-responsibility-and-accountability-with-agentic-ai-presented-by-tag-data-science-ai-society-1929040)
- [TAG CX & DEI 'Human Intelligence' panel (2026-10-21)](https://members.tagonline.org/calendar/Details/human-intelligence-how-teams-win-with-customer-and-employee-insights-presented-by-tag-cx-and-tag-dei-societies-1935704) (nothing useful)
- [TAG Data Governance Society board](https://www.tagonline.org/societies/data-governance/)
- [COLLIDE Data + AI Conference 2026](https://datasciconnect.com/events/collide/)
- [Atlanta Tableau User Group events 2025](https://usergroups.tableau.com/atlanta-tableau-user-group/)
- [Snowflake Atlanta 2025-26 event pages](https://usergroups.snowflake.com/events/details/snowflake-atlanta-presents-deep-dive-on-snowflake-aim/)
- [Atlanta Databricks User Group](https://usergroups.databricks.com/atlanta-databricks-user-group/)
- [GitHub user search (Atlanta, dbt / data engineer / snowflake)](https://github.com/search?q=dbt+location%3AAtlanta&type=users)
- [dbt Developer Hub blog authors](https://docs.getdbt.com/blog/authors) (nothing useful)
- [Data Tech 2026 speakers (sched)](https://datatech2026.sched.com/directory/speakers) (nothing useful)
- [DAMA Georgia at Kennesaw State](https://calendar.kennesaw.edu/event/corporate-spotlight-dama-international) (nothing useful)
- [DevNexus speakers](https://devnexus.com/speakers) (nothing useful)
- [Georgia State Institute for Insight events / WiDS regional events](https://www.widsworldwide.org/) (nothing useful)
- [SQL Saturday Atlanta](https://sqlsaturday.com/) (nothing useful)
- [Medium feeds for Atlanta companies (curl)](https://medium.com/feed/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

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

## 5. Before outreach

- [ ] **Check the tier-1 people raised by the rule.** Ken Slate's project has no dbt in it. The Chick-fil-A certification post does not mention dbt. Luke Carter wrote about product prioritisation, not analytics engineering.
- [ ] **Check Jessica M. Rudd's talk record.** The record says first-time speaker, but the GitHub profile keeps a tech-talks app.
- [ ] **Confirm the TAG panel took place.** Markis Jaudon Ramon Piper, Amari Hanes, Dhruv Alexander and Shalmali Joshi are on a panel set for 2026-10-22.
- [ ] **Confirm the 13 unknown locations.** They include Cox Automotive's 2024 speakers, the FanDuel career panel and Mike Sandt. Mike Sandt has an Atlanta LinkedIn profile, but nothing ties it to Salesloft.
- [ ] **Check the medium location calls.** Grant Cloud's LinkedIn result says Atlanta, but the text mentions a move to Kalshi in New York. Zach Lancaster was matched as "Zachary Lancaster" at WarnerMedia.
- [ ] **Skip or re-rank people outside the region.** Francisco Moya is in Medellín, and Nate Nunta is in the Bay Area.
- [ ] **Check the line-up has practitioners first.** Nate Nunta, Katherine Brock, Brandon Sweeney, Jason Ganz, Erica Louie and Cole Fraser work at dbt Labs and are labelled. All spoke at chapter events, including a recorded Coalesce watch party. Katherine Brock, Brandon Sweeney and Cole Fraser have unknown locations.

## 6. Next run

- **Sources to try first:**
  - **LinkedIn pass:** 36 tier-1 and tier-2 people are still `not_searched`.
  - **Meetup `gql2` past-events query:** run it for the chapter, with `sort: DESC`, to capture recent organisers and RSVPs.
  - **Women-in-data calendars:** the Georgia Tech, Georgia State and TAG DEI society calendars.
  - **TAG and COLLIDE:** the TAG DataPalooza speaker list in October, and COLLIDE session titles once published.
  - **Medium publications:** confirm the names for Mailchimp, Cox, Home Depot, Calendly, Salesloft and Greenlight, and read their feeds.
  - **GitHub and Bevy:** GitHub user search (`dbt location:Atlanta`) for new first-time speakers, and the Bevy pages for Snowflake and Tableau Atlanta.
- **People to locate:** the 13 unknown locations in section 5. Stewart Bryson's talk links are not in the file yet.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `atlanta/atlanta_dbt_companies.json`, the chapter `atlanta-dbt-meetup-group`, `../enriched/atlanta-dbt-meetup-group.json` and the region "the Atlanta metro (Atlanta, Sandy Springs, Alpharetta and nearby)". Budget about 25 web searches.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build: dbt conference agendas filtered to local employers, company blogs, local meetups and user groups, women-in-data communities, and a LinkedIn Jobs scan. Past chapter speakers added from `../enriched/atlanta-dbt-meetup-group.json`. 56 companies (16 on the watchlist), 36 people, 35 job ads at 31 companies, 8 past meetups. Split: 25 proven speakers, 5 emerging voices, 6 featured. Tiers: 4 tier 1, 19 tier 2, 5 tier 3, 8 connectors. 17 people had already spoken at the chapter. |
| 2026-10-01 | 2 | Extension: TAG society calendars and board pages, COLLIDE 2026, Tableau, Snowflake and Databricks user groups, an Amplitude Community panel and GitHub user search. 45 new people, for 81 companies (38 on the watchlist) and 81 people. Split: 51 proven speakers, 14 emerging voices, 14 featured, 2 with no public content. Tiers: 11 tier 1, 36 tier 2, 18 tier 3, 16 connectors. |
| 2026-10-01 | 2 | Location pass: 6 people placed from speaker bios and recent in-person talks, 5 in the region and 1 outside. |
| 2026-10-01 | 2 | LinkedIn pass: 4 people placed from LinkedIn search results, all in the region. 15 people are still unknown. |
