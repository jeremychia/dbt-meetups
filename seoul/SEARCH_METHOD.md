# Seoul dbt search: method, lessons and replication prompt

This file goes with `seoul_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-10-01
- **Goal:** find people in the Seoul Capital Area who could **speak at** (or attend) the [Seoul dbt Meetup](https://www.meetup.com/seoul-dbt-meetup/), and the local companies that use dbt.
- **Region:** the Seoul Capital Area. That is Seoul, Incheon and Gyeonggi, so Bucheon and Seongnam (Pangyo) count. Sejong does not.

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 59 |
| People | 58 |
| Tier 1 leads | 20 |
| First-time speakers (publish, no talk yet) | 8 |
| Proven speakers | 48 |
| Spoke at this chapter before | 20 |
| Based in the region | 45 |
| Based elsewhere | 2 |
| Location unknown | 11 |
| With a LinkedIn profile | 1 |
| Job ads mentioning dbt | 28 |
| Past chapter meetups | 12 |
<!-- at-a-glance:end -->

## 1. How the search was done

Web search ran out after 15 calls, in English and Korean. The rest of the run used direct fetches and open APIs only. Korean names are romanised family name first, unless the person shows their own spelling.

### Step 1: Other local meetups and user groups

- **[Apache Airflow Korea User Group](https://www.meetup.com/korea-apache-airflow-user-group/):** 6 meetups, read through Meetup's `gql2` endpoint, the [forum](https://discourse.airflow-kr.org/) and the [YouTube channel](https://www.youtube.com/@Airflow-users-Korea). It gave one dbt talk and one semantic layer talk, plus many Airflow speakers.
- **[Snowflake Korea User Group (Flakers)](https://usergroups.snowflake.com/seoul/):** 5 meetups from 2023 to 2024, read through the Snowflake user-group API. It gave a Snowflake + dbt + Airflow session.
- **[AWSKRUG](https://www.meetup.com/awskrug/):** 600 events scanned, with few data warehouse talks.
- **Empty:** the [Databricks Korea User Group](https://usergroups.databricks.com/databricks-korea-user-group-krug/) lists no events. [Snowflake World Tour Seoul 2026](https://www.snowflake.com/events/snowflake-world-tour-seoul/) names no speakers. The [dbt Summit agenda](https://www.getdbt.com/dbt-summit/agenda) and dbt Champions pages show no Korean companies.

### Step 2: Job ads

- **[wanted.co.kr](https://www.wanted.co.kr/search?query=dbt):** its open search API (`api/chaos/search/v1/position`) and job detail API (`api/v4/jobs/<id>`) need no login.
- **Queries:** dbt, analytics engineer, data engineer, Snowflake and BigQuery.
- **Yield:** 284 ads read, and 28 ads at 24 companies that mention the word dbt are in the file. Examples are Toss Income, Hyperconnect, Buzzvil, Next Securities and AITRICS.
- **No posting dates:** the fields read do not include one. All ads are recorded as seen on 2026-10-01.

### Step 3: Blogs and open source

- **[velog dbt tag](https://velog.io/tags/dbt):** 18 posts. The page is server-rendered and lists author handles and dates. Most posts are study notes with no employer.
- **Tech blog feeds:** about 30 were read.
  - [Toss tech blog](https://toss.tech/): a Toss Securities post confirms its batch pipelines run on dbt.
  - [SOCAR tech blog](https://tech.socar.kr/data/2022/07/25/analytics-engineering-with-dbt): a 2022 dbt post by a past chapter speaker.
  - [Woowahan](https://techblog.woowahan.com/), Kakao, Hyperconnect, Buzzvil, Banksalad, Kakaobank, Devsisters, Inflab and Ohouse: no dbt posts.
  - [Karrot (Daangn)](https://medium.com/daangn) and most other Korean blogs on Medium were blocked (HTTP 403 and 429).
- **GitHub user search** (location Seoul or Korea): one strong open-source lead, and several profiles with no public content.

### Step 4: Women-in-data communities

This step looks for speakers through women-focused groups' own events. It never labels or guesses anyone's gender.

- **[PyLadies Seoul](https://www.meetup.com/seoul-pyladies-meetup/):** 39 events. Its talks are Python and data analysis, not dbt. 2 speakers are tagged from it.
- **Not found:** Women Who Code, R-Ladies and WiMLDS have no Seoul groups on Meetup.

### Step 5: Chapter history

- **Past speakers and hosts:** every named speaker from `../enriched/seoul-dbt-meetup.json` was added. That covers 12 events, from meetup #0 (2023-08-24) to meetup #10 (2026-09-17).
- **All in person:** every past Seoul dbt event was held in person, mostly in Gangnam.

### Step 6: Location pass and LinkedIn pass

- **Location pass:** people were placed from public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
  - Meetup's `gql2` endpoint returns each event's hosts and RSVPs with their profile city. A host or an RSVP to the event where the person spoke gave high confidence.
  - The velog profile API gave bios and GitHub links. GitHub HTML profile pages still show the location after the API's rate limit.
  - An in-person talk in the last 2 years at an employer with a Seoul office gave medium confidence.
- **LinkedIn pass:** search results only, never a LinkedIn page. It placed 1 person, Jean-Christophe Gnansounou (Cartier, Seoul).
- **Yield:** 15 people placed across both passes, and 12 still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **Airflow Korea and Flakers.** Seoul's dbt-related talks happen at these two user groups, not at dbt-only events.
  - **wanted.co.kr's open APIs.** They are the fastest way to find Seoul dbt employers.
  - **Meetup `gql2`.** It gave past events, venues, hosts and RSVPs with profile cities in one call.
  - **velog.** The tag page and profile API give handles, dates, bios and GitHub links.
- **Sources that didn't:**
  - **Medium** blocked fetches, so the authors of the Karrot and other company dbt posts could not be confirmed.
  - **Snowflake and dbt Labs event pages** name no Korean speakers.
  - **LinkedIn** found a tied profile for only 1 of the 11 people searched.
- **Watch out for:**
  - **Romanised names.** Most new names come from Korean listings. Check the spelling with each person.
  - **"Independent / no company".** 21 people sit here because no employer was found. Many are Airflow Korea speakers.
  - **One multi-speaker talk.** Meetup #2 had four speakers on one talk. Their titles came through as one string: "dbt Labs; Snowflake; Pinnu Analytics; DataMarketingKorea".
  - **Organisers' Meetup cities are stale.** Joshua Kim's profile says Toronto, and Kyung-jun Lee's says Sejong. Both organise in-person events in Seoul.

## 3. Key leads

- **First-time speakers** (people who publish about dbt but have no talk on record):
  - **Byungsu Kang (Toss Securities):** leads the realtime data team. A [post on lineage](https://toss.tech/article/toss-securities-visualize-lineage) says the batch pipelines all run on dbt.
  - **PresentJay (AB180):** built [dbt-plan](https://github.com/PresentJay/dbt-plan), which flags breaking schema changes before `dbt run`. The real name is not shown.
  - **Moon Ju-eun:** wrote [Establishing DBT standards](https://velog.io/@juliy9812/Establishing-DBT-standards) and a post on dbt model performance. No employer is stated.
  - **Seokjin Han:** wrote [why the default incremental strategy is slow on PostgreSQL with Citus](https://velog.io/@hsjni0110/DBT-PostgreSQL-Citus-%EC%97%90%EC%84%9C%EB%8A%94-%EA%B8%B0%EB%B3%B8-Incremental-%EC%A0%84%EB%9E%B5%EC%9D%B4-%EB%B9%84%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B4%EB%8B%A4).
  - **Henry (Karrot):** wrote [7 problems adopting dbt and Airflow](https://medium.com/daangn/dbt%EC%99%80-airflow-%EB%8F%84%EC%9E%85%ED%95%98%EB%A9%B0-%EB%A7%88%EC%A3%BC%ED%95%9C-7%EA%B0%80%EC%A7%80-%EB%AC%B8%EC%A0%9C%EB%93%A4-61250a9904ab). Only the first name is known, and the post date was not read.
- **Anchor speakers:**
  - **Tan Morgan Kim:** [ran Airflow DAGs by dbt design principles](https://www.youtube.com/watch?v=P7ize0MLY8w) at Airflow Korea, 2025-02.
  - **Chris Song:** Snowflake + dbt + Airflow sessions at [Flakers](https://usergroups.snowflake.com/seoul/) in 2023 and a [2024 startup meetup](https://discourse.airflow-kr.org/t/49).
  - **Seongyun Byeon (Kyle School):** ex-SOCAR director of data and Google Cloud expert, with [dbt + BigQuery posts](https://zzsza.github.io/data-engineering/2025/01/30/dbt-with-bigquery/) in 2025.
  - **Riven Lee (Wrtn):** [spoke at meetup #9](https://www.meetup.com/seoul-dbt-meetup/events/315240680/) on migrating from dbt Core to dbt Fusion.
- **Connectors** (people who can introduce others):
  - **Chapter hosts:** Herick Jee and Abi Adebayo hosted [meetups #0 to #7](https://www.meetup.com/seoul-dbt-meetup/events/312130999/). Thomas Kim (Fivetran) and Hangyeol Seo co-host [the recent ones](https://www.meetup.com/seoul-dbt-meetup/events/316380348/).
  - **Yeonguk Choo:** organises [Airflow Korea](https://www.meetup.com/korea-apache-airflow-user-group/) and is an Apache Airflow committer. The group already lets the chapter post meetups on its forum.
  - **Soo Lee and Jihwan Hyun:** lead the [Snowflake Korea User Group](https://usergroups.snowflake.com/seoul/).
  - **Seongyun Byeon:** ran 글또, a developer writing group of 639 members.
  - **[PyLadies Seoul](https://www.meetup.com/seoul-pyladies-meetup/):** ran a 2025 workshop that helped women submit their first talks. Ask the organisers for introductions.

## 4. Before outreach

- **Check most "in region" calls.** Only 13 of the people marked in the region have a location note with evidence. The rest were placed in Seoul from their listing during research.
- **Merge one duplicate.** Joshua Kim appears twice, as `joshua-kim` and `joshua-kim-jinsuk-kim` (IoTrust), with the same three chapter talks.
- **Check possible duplicates:**
  - **Jihwan Hyun:** the dbt Project on Snowflake talk lists only "지환" of the dbt Seoul community.
  - **Kyung-jun Lee:** "이경준", who spoke at the 4th Airflow Korea meetup, may be the same person, so was not added again.
  - **Chris Song:** probably the same person as 송호연, formerly VP at NFTBank.
- **Check two organisers' locations.** Joshua Kim and Kyung-jun Lee stay unknown because their Meetup cities conflict with their Seoul roles.
- **Check tier 1.** Jung Won-hyung is a job seeker who writes about dbt. The tier rule put this lead in tier 1, but a lightning talk fits better.
- **Skip dbt Labs staff.** Benoit Perigaud is excluded from outreach and is in Madrid.
- **Check speakers based elsewhere.** Zoe Yim spoke at meetup #9 but is in Atlanta.

## 5. Next run

- **LinkedIn:** search the past speakers still unknown and not yet searched: Louis Lee and Wynn Park.
- **Blogs on Medium:** try the browser, or the publication's RSS feed, for Karrot, IoTrust, Musinsa and Yogiyo.
- **GitHub locations:** check the accounts linked from Seokjin Han's and zuckerfrei's velog bios.
- **Job ads:** re-run the wanted.co.kr queries, and add the Lever, Greenhouse and Ashby `site:` searches.
- **Women-in-data:** ask PyLadies Seoul about speakers from its first-talk workshop.

## 6. Replication prompt

````
You are extending my dataset of Seoul Capital Area companies that use dbt, and people who could
speak at or attend the Seoul dbt Meetup. The file is seoul/seoul_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read seoul/SEARCH_METHOD.md first, then
research/README.md, research/raw-format.md, research/location-task.md and
research/linkedin-task.md. Keep the shared schema (berlin_planning/SEARCH_METHOD.md §3).

Try first: new Airflow Korea and Snowflake Korea (Flakers) events through Meetup gql2 and
discourse.airflow-kr.org/search.json; new Seoul dbt Meetup events; the wanted.co.kr search API
(api/chaos/search/v1/position) for ads that contain the whole word "dbt"; the velog dbt tag;
and Korean company blogs on Medium through the browser. Romanise Korean names family name
first unless the person shows their own spelling, and give each an ASCII id.

Rules: never fetch LinkedIn pages, only use search results; public professional information
only; never guess gender, and record pronouns only when self-stated. Assemble with
research/assemble.py --base, place people with research/apply_locations.py, then run
research/validate.py and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Airflow Korea, Flakers, AWSKRUG and PyLadies Seoul events, wanted.co.kr job ads, velog, about 30 tech blog feeds and GitHub search, plus chapter history. 59 people at 59 companies, 21 of them past chapter speakers and hosts. 28 dbt job ads at 24 companies. |
| 2026-10-01 | 1 | Location pass from public pages: Meetup hosts and RSVPs, velog bios, GitHub profiles and recent in-person talks. 14 people placed. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 1 person placed. With the location pass, 15 people placed and 12 still unknown. |
