# Singapore dbt search: method, lessons and replication prompt

This file goes with `singapore_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-10-01
- **Goal:** find people in Singapore who could **speak at** (or attend) the [Singapore dbt Meetup](https://www.meetup.com/singapore-dbt-meetup/), and the local companies that use dbt.
- **Region:** Singapore. Kuala Lumpur, Ho Chi Minh City and Sydney do not count.

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 56 |
| People | 82 |
| Tier 1 leads | 20 |
| First-time speakers (publish, no talk yet) | 14 |
| Proven speakers | 65 |
| Spoke at this chapter before | 28 |
| Based in the region | 63 |
| Based elsewhere | 5 |
| Location unknown | 14 |
| With a LinkedIn profile | 9 |
| Job ads mentioning dbt | 21 |
| Past chapter meetups | 16 |
<!-- at-a-glance:end -->

## 1. How the search was done

Web search ran out after about 12 calls. The rest of the run used direct fetches of pages, plus the GitHub and DEV APIs.

### Step 1: Other local meetups and conferences

- **[GovTech STACK [Data] meetups](https://www.developer.tech.gov.sg/communities/events/stack-meetups/):** 8 monthly events from 2025-11 to 2026-09, with 25 named speakers. Each page lists every speaker with title and agency. It is the richest source of Singapore data speakers, but no talk mentions dbt.
- **[Snowflake User Group Singapore](https://usergroups.snowflake.com/singapore/):** 4 events. It gave Grab and Infinite Lambda speakers and the group's organisers.
- **[DataScience SG](https://www.meetup.com/datascience-sg-singapore/):** 7 events in 2025 and 2026, mostly on AI. Meetup group pages give past events through their `__NEXT_DATA__` block.
- **[Singapore Data & AI Engineering Meetup](https://www.meetup.com/singapore-data-ai-engineering-meetup/):** AI and Ray talks, with no dbt.
- **[PyCon Singapore 2026](https://pycon.sg/speakers.html):** few data talks. It gave some Grab machine learning engineers.
- **dbt Labs events:** none of the 227 dbt Summit and case-study pages in the [getdbt.com sitemap](https://www.getdbt.com/sitemap-0.xml) names a Singapore company. The dbt World Tour stops in Sydney, Melbourne, Auckland and Tokyo, but not Singapore.

### Step 2: Company and vendor blogs

- **[Grab tech blog](https://engineering.grab.com/feed.xml):** the data mesh series and a post on AI in analytics. No post mentions dbt.
- **Medium publications:** foodpanda data, ShopBack, Traveloka, Ninja Van, GovTech's data science division, Carousell and Airwallex. They were read through [rss2json](https://api.rss2json.com/), because Medium returns HTTP 429. No post mentions dbt.
- **[Infinite Lambda case studies](https://infinitelambda.com/case-studies/):** Mandai Wildlife Group and Keppel use dbt. Only Mandai has a job ad, and its text does not name dbt.
- **[Holistics blog](https://www.holistics.io/blog/):** posts on analytics as code.
- **[DEV dbt tags](https://dev.to/t/dbt):** 231 authors checked, and 1 is in Singapore.
- **[GitHub user search](https://github.com/search?q=dbt+location%3ASingapore&type=users):** mostly students. One weak lead was kept.

### Step 3: Job ads

- **[freehire.me](https://freehire.me/jobs?countries=sg&skills=dbt):** plain-fetchable. 4 of its 10 pages were read, 80 ads in all. Direct employers include Endowus, Grasshopper, Secretlab, Traveloka, OCBC and LTA. About half the ads are from recruiters with unnamed clients.
- **[TheirStack](https://theirstack.com/en/technology/dbt/sg):** the top 10 of 137 companies that use dbt are visible without a login.
- **[Indeed Singapore](https://sg.indeed.com/q-dbt-jobs.html):** HTTP 403.
- **Yield:** 21 job ads at 19 companies.

### Step 4: Women-in-data communities

This step looks for speakers through women-focused groups' own events. It never labels or guesses anyone's gender.

- **[PyLadies Singapore](https://pyladies.sg):** its team and its PyCon Singapore 2025 track. 3 people are tagged from it and from Women Devs SG.
- **Thin pool:** no Singapore women-in-data group was found with dbt talks.

### Step 5: Chapter history

- **Past speakers:** every named speaker from `../enriched/singapore-dbt-meetup.json` was added. That covers 16 events, from 2022-07-07 to 2026-09-23.
- **New evidence for 2 past speakers:** Michael Han and Cliff Chew.

### Step 6: Location pass and LinkedIn pass

- **Location pass:** people were placed from public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
  - Meetup's `gql2` endpoint gave every past chapter event with its hosts, RSVPs and member cities. An RSVP to the event where the person spoke gave high confidence.
  - An in-person chapter talk in the last 2 years, at an employer with a Singapore office, gave medium confidence.
  - Grab and Holistics author pages list posts only, with no location.
- **LinkedIn pass:** search results only, never a LinkedIn page. 15 people were searched. It placed 5 in Singapore and 1 in Sydney.
- **Yield:** 17 people placed across both passes, and 14 still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **GovTech STACK pages** list every public-sector data speaker with title and agency.
  - **freehire.me** is the one job board that fetches without a login.
  - **Infinite Lambda case studies** name dbt users that no job ad shows.
  - **Meetup `gql2`** gave hosts and RSVPs with member cities for every chapter event.
- **Sources that didn't:**
  - **Medium feeds** return HTTP 429. rss2json worked for about 6 publications, then rate-limited too.
  - **JavaScript-rendered pages** came back empty: the [Luma DataScience SG calendar](https://luma.com/datascienceSG) and the [Databricks User Group Singapore](https://community.databricks.com/t5/singapore/databricks-user-group-singapore-meetup/m-p/124414) page.
  - **The GitHub API** was rate-limited, and code search hit its limit.
- **Watch out for:**
  - **Almost no Singapore lead has public dbt content.** Most are data engineers who spoke about pipelines, data mesh or semantic layers. Ask each one whether they use dbt.
  - **Recruiters.** About half the job ads have unnamed clients. For speaker sourcing, filter on `type == "employer"`.
  - **Overlap with Kuala Lumpur.** Feng Cheng and Chang Boon Heng appear in both datasets. 3 LinkedIn URLs were carried over from the Kuala Lumpur file.
  - **Approximate titles.** Several Grab, foodpanda and data.gov.sg titles come from bylines without roles.

## 3. Key leads

- **First-time speakers** (people who publish but have no talk on record):
  - **Maanas Prabhakar (Grab):** wrote [how AI is transforming analytics at Grab](https://engineering.grab.com/how-ai-is-transforming-analytics), on certified metrics and context for AI agents.
  - **Harvey Li (Grab):** co-wrote [Data Mesh at Grab, part III](https://engineering.grab.com/data-mesh-at-grab-part-three), on data contracts and automated data quality checks.
  - **Huy Nguyen (Holistics):** co-founder, wrote [4 levels of analytics as code](https://www.holistics.io/blog/4-levels-of-analytics-as-code/). A LinkedIn result places Huy Nguyen in Singapore.
  - **power zhong:** wrote [a Docker set-up for a dbt learning repo](https://dev.to/power_zhong/the-small-docker-boundary-that-makes-the-dbt-student-repo-easy-to-trace-k). It is the only Singapore post found that mentions dbt.
  - **Shi Min (foodpanda):** wrote [a series on budget optimisation](https://medium.com/foodpanda-data/introduction-optimising-budget-through-data-analysis-030b2f39ad0c), alongside the chapter's foodpanda speakers.
- **Anchor speakers:**
  - **Janice Ng (GovTech):** three STACK talks in 2026 on data mesh and context layers, for example [AI-enabled data engineering](https://www.developer.tech.gov.sg/communities/events/stack-meetups/ai-enabled-data-engineering).
  - **Michael Han (Infinite Lambda):** four chapter talks, and a [2024 Snowflake user group talk on ML pipelines in dbt](https://usergroups.snowflake.com/events/details/snowflake-singapore-presents-snowflake-community-meetup-singapore-18-july-2024/). Ask Michael Han for a Mandai client speaker.
  - **Clarence San and Hao Ran Lee (foodpanda):** [spoke at the 2025-10 meetup](https://www.meetup.com/singapore-dbt-meetup/events/311046549/) on dbt model versions and row deletions in incremental models.
  - **Cliff Chew (Tech in Asia):** [spoke at the 2026-07 meetup](https://www.meetup.com/singapore-dbt-meetup/events/315295343/) and at [DataScience SG](https://www.meetup.com/datascience-sg-singapore/events/311983867/).
- **Connectors** (people who can introduce others):
  - **Jing Yu Lim (Spenmo):** hosts [every chapter event](https://www.meetup.com/singapore-dbt-meetup/events/316411854/) and has given 3 talks.
  - **Yap Ghim Eng (GovTech):** hosts the [STACK data meetups](https://www.developer.tech.gov.sg/communities/events/stack-meetups/), the route to public-sector speakers and a venue.
  - **Suteja Kanuri, Yun Fei Choo (Snowflake) and Piyush Gupta (Temasek):** organise the [Snowflake User Group Singapore](https://usergroups.snowflake.com/singapore/), a natural co-host.
  - **Koo Ping Shung:** co-founded [DataScience SG](https://luma.com/datascienceSG).
  - **Hwee Shan Tay:** co-chairs [PyLadies Singapore](https://pyladies.sg). Ask the co-chairs to share the call for speakers.

## 4. Before outreach

- **Check most "in region" calls.** Only 13 of the people marked in Singapore have a location note with evidence. The rest were placed from their employer or event during research.
- **Check tier 1.** The first-time speaker rule raised the Grab and Holistics authors to tier 1, but their posts don't mention dbt. Treat them as speakers on a data topic.
- **Check two name-only matches.** Chin Hwee Ong and Umesh Ramakrishnan are placed at medium from Meetup RSVPs that match on name only.
- **Check one LinkedIn match.** Feng Cheng's result shows the name surname first, "Cheng Feng - Grab".
- **Check Michael Han's title.** The 2026-09 meetup lists "General Manager", and GovTech lists "Head of APAC, Infinite Lambda".
- **Skip dbt Labs staff.** Mark Wan and Sin Ta Poon are excluded from outreach. Mark Wan's location is unknown, and LinkedIn found no matching profile, so check whether Mark Wan is still at dbt Labs.
- **Skip the backup.** The backup speaker is a Vinted colleague based in Berlin.
- **Check speakers based elsewhere.** Nas Radev and Hamzah Chaudhary are in London, Thanh Dinh Khac in Ho Chi Minh City, and Josh Beemster in Sydney.

## 5. Next run

- **Conference agendas:** the Coalesce and dbt Summit speaker lists, and the Snowflake and Databricks World Tour Singapore agendas, were not covered.
- **Job ads:** read the remaining 6 freehire.me pages, and add the Lever, Greenhouse and Ashby `site:` searches.
- **People still without a location:** 14. Most are past chapter speakers from 2023 and 2024.
  - LinkedIn found no profile with a matching title for Aezo Teo, Houren Chen, Shuguang Xiang, Adam Bagaskarta and Jia Ler Chew. Try their Grab or ShopBack author pages.
  - Auxten Wang gave 2 in-person Singapore talks in 2026. Confirm whether ClickHouse has a Singapore office.
- **Ask about dbt use:** GovTech's Data Practice, Singapore Customs and Grab show strong data teams but no public dbt use.
- **Women-in-data:** ask PyLadies Singapore and Women Devs SG for speakers on data topics.

## 6. Replication prompt

````
You are extending my dataset of Singapore companies that use dbt, and people who could speak
at or attend the Singapore dbt Meetup. The file is singapore/singapore_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read singapore/SEARCH_METHOD.md first, then
research/README.md, research/raw-format.md, research/location-task.md and
research/linkedin-task.md. Keep the shared schema (berlin_planning/SEARCH_METHOD.md §3).

Try first: new GovTech STACK [Data] meetups, new Singapore dbt Meetup and Snowflake User Group
Singapore events (Meetup gql2), the Coalesce and dbt Summit speaker lists, the Snowflake and
Databricks World Tour Singapore agendas, and freehire.me/jobs?countries=sg&skills=dbt (keep
ads that contain the whole word "dbt"; tag recruiters as type "recruiter"). Ask whether each
data speaker uses dbt before raising them to tier 1.

Rules: never fetch LinkedIn pages, only use search results; public professional information
only; never guess gender, and record pronouns only when self-stated. Assemble with
research/assemble.py --base, place people with research/apply_locations.py, then run
research/validate.py and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. GovTech STACK, Snowflake User Group, DataScience SG, PyCon and PyLadies Singapore events, freehire.me and TheirStack job ads, Grab, Medium, Holistics and Infinite Lambda blogs, and DEV authors, plus chapter history. 82 people at 57 companies, 28 of them past chapter speakers. 21 dbt job ads. |
| 2026-10-01 | 1 | Location pass from public pages: Meetup hosts and RSVPs, and recent in-person chapter talks. 11 people placed, 8 in Singapore and 3 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 6 people placed, 5 in Singapore and 1 in Sydney. With the location pass, 17 people placed and 14 still unknown. |
