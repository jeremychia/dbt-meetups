# Seoul: city notes

This file holds what is specific to Seoul. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Seoul dbt Meetup](https://www.meetup.com/seoul-dbt-meetup/), data in `seoul_dbt_companies.json`
- **Region:** the Seoul Capital Area. That is Seoul, Incheon and Gyeonggi, so Bucheon and Seongnam (Pangyo) count. Sejong does not.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-01)

| | Count |
|---|---|
| Companies | 71 |
| People | 69 |
| Tier 1 leads | 20 |
| First-time speakers (publish, no talk yet) | 8 |
| Proven speakers | 51 |
| Spoke at this chapter before | 20 |
| Based in the region | 52 |
| Based elsewhere | 3 |
| Location unknown | 14 |
| With a LinkedIn profile | 14 |
| Job ads mentioning dbt | 38 |
| Past chapter meetups | 12 |
<!-- at-a-glance:end -->

## 1. Where to look in Seoul

Search in English and Korean. Korean names are romanised family name first, unless the person shows a preferred spelling.

### Meetups and user groups

- **[Apache Airflow Korea User Group](https://www.meetup.com/korea-apache-airflow-user-group/):** Seoul's dbt-related talks happen here and at Flakers, not at dbt-only events. 6 meetups were read through Meetup's `gql2` endpoint, the [forum](https://discourse.airflow-kr.org/) and the [YouTube channel](https://www.youtube.com/@Airflow-users-Korea). It gave one dbt talk and one semantic layer talk, plus many Airflow speakers.
- **[Snowflake Korea User Group (Flakers)](https://usergroups.snowflake.com/seoul/):** 5 meetups from 2023 to 2024, read through the Snowflake user-group API. It gave a Snowflake + dbt + Airflow session.
- **[AWSKRUG](https://www.meetup.com/awskrug/):** 600 events scanned, with few data warehouse talks.
- **[PyLadies Seoul](https://www.meetup.com/seoul-pyladies-meetup/):** 39 events. The talks are Python and data analysis, not dbt. 2 speakers are tagged from it.
- **Chapter history:** every named speaker from `../enriched/seoul-dbt-meetup.json` was added. That covers 12 events, from meetup #0 (2023-08-24) to meetup #10 (2026-09-17). Every past Seoul dbt event was held in person, mostly in Gangnam.

### Job ads

- **[wanted.co.kr](https://www.wanted.co.kr/search?query=dbt):** the fastest way to find Seoul dbt employers. The open search API (`api/chaos/search/v1/position`) and job detail API (`api/v4/jobs/<id>`) need no login. The queries were dbt, analytics engineer, data engineer, Snowflake and BigQuery. 284 ads were read, and 28 ads at 24 companies that mention the word dbt are in the file. Examples are Toss Income, Hyperconnect, Buzzvil, Next Securities and AITRICS.
- **wanted.co.kr, second pass:** 7 queries, including 데이터 분석가 and 데이터 플랫폼, read 970 more ads and skipped those already in the file. 9 new ads at 8 companies. Most list dbt only as a plus (우대 사항), such as Yeogi Eottae, Bagelcode, PaytaLab and CJ Olive Young. A Wrtn Technologies ad confirms its Seoul office.
- **Company job boards:** the Greenhouse, Lever and Ashby boards of about 45 employers. Only Coupang had a Seoul ad that says dbt, as a plus.

### Blogs and open source

- **[velog dbt tag](https://velog.io/tags/dbt):** 18 posts. The page is server-rendered and lists author handles and dates. The velog profile API gives bios and GitHub links. Most posts are study notes with no employer.
- **[Toss tech blog](https://toss.tech/):** a Toss Securities post confirms its batch pipelines run on dbt.
- **[SOCAR tech blog](https://tech.socar.kr/data/2022/07/25/analytics-engineering-with-dbt):** a 2022 dbt post by a past chapter speaker.
- **GitHub user search** (location Seoul or Korea): one strong open-source lead, and several profiles with no public content.

### Locations

- **Meetup `gql2`:** returns each event's hosts and RSVPs with the profile city, along with past events and venues, in one call. A host or an RSVP to the event where the person spoke gave high confidence.
- **velog and GitHub:** the velog profile API gave bios and GitHub links. GitHub HTML profile pages still show the location after the API's rate limit.
- **Recent chapter talks:** an in-person talk in the last 2 years at an employer with a Seoul office gave medium confidence.
- **LinkedIn search results:** placed 1 person, Jean-Christophe Gnansounou (Cartier, Seoul). A tied profile came back for only 1 of the 11 people searched.
- **Yield:** 15 people placed across both passes, and 12 still unknown. The evidence rules are in [location rules](../research/README.md#6-location-rules).

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[AWSKRUG Women In Cloud](https://www.meetup.com/awskrug/):** the best source. It is the women's subgroup of AWSKRUG and has held 22 meetups since October 2023. Its events sit inside the AWSKRUG Meetup group, so filter AWSKRUG's past events for "Women In Cloud". Most talks are about careers and cloud. Kim Naheon, a senior data engineer at Spotify, [spoke in person](https://www.meetup.com/awskrug/events/305434782/) in January 2025. The 7 Meetup hosts are recorded as connectors. Winter Lee also hosts the AWSKRUG data group. The group has a #women-in-cloud Slack channel and an open speaker form.
- **[PyLadies Seoul](https://www.meetup.com/seoul-pyladies-meetup/):** events since 2025 were re-read. The October 2025 DuckDB workshop is already recorded. The hosts geni, Hwayoung and saerom were added as connectors. geni also hosts Women In Cloud.
- **[WiDS Seoul](https://www.widsworldwide.org/events/event/wids-lahore-3/):** one watch party of the WiDS Worldwide conference, in September 2023. The ambassador, Imai Jen-La Plante, is a connector.
- **Also ask:** the Women In Cloud hosts and Winter Lee for data speakers. Post the call for speakers in #women-in-cloud.

## 2. What didn't work here

- **Web search:** ran out after 15 calls, in English and Korean. The rest of the run used direct fetches and open APIs only.
- **[Databricks Korea User Group](https://usergroups.databricks.com/databricks-korea-user-group-krug/):** lists no events.
- **[Snowflake World Tour Seoul 2026](https://www.snowflake.com/events/snowflake-world-tour-seoul/):** names no speakers.
- **[dbt Summit agenda](https://www.getdbt.com/dbt-summit/agenda) and dbt Champions pages:** show no Korean companies.
- **wanted.co.kr posting dates:** the fields read do not include one. All ads are recorded as seen on 2026-10-01.
- **HN Who is hiring:** no Seoul ad since 2023 mentions dbt.
- **GitHub:** code search hit the shared rate limit after 3 calls. Repository lists of 20 Korean organisations, such as Karrot, Toss, Devsisters and Bucketplace, show no dbt project of their own.
- **dbt Labs case studies:** none for a Korean company.
- **Tech blog feeds without dbt posts:** about 30 feeds were read. [Woowahan](https://techblog.woowahan.com/), Kakao, Hyperconnect, Buzzvil, Banksalad, Kakaobank, Devsisters, Inflab and Ohouse had none.
- **Medium:** [Karrot (Daangn)](https://medium.com/daangn) and most other Korean blogs on Medium were blocked (HTTP 403 and 429). The authors of the Karrot and other company dbt posts could not be confirmed.
- **Women-in-data groups:** Women Who Code, R-Ladies and WiMLDS have no Seoul groups on Meetup. Women Who Code closed in 2024.
- **Other women-in-data sources:** Meetup's group search near Seoul found only social groups and AWS student clubs. [GDG Seoul](https://gdg.community.dev/gdg-seoul/) has held no Women Techmakers event since 2019. [Girls in Tech Korea](https://girlsintech.org/korea/) did not respond. The Women in AI Korea page returned HTTP 404. [event-us.kr](https://event-us.kr/) search renders by JavaScript.

## 3. Companies looked at

- **No employer found:** 21 people sit under "Independent / no company". Many are Airflow Korea speakers.
- **Confirmed dbt users:** Toss Securities runs its batch pipelines on dbt, and the job ads add 24 companies that name dbt.

<!-- companies:start -->
69 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (27)</summary>

AB180, Ajeong Networks, Boosters, Buzzvil, Cartier (local presence not confirmed), Databricks (local presence not confirmed), DataMarketingKorea (local presence not confirmed), dbt Community Korea (local presence not confirmed), dbt Labs (local presence not confirmed), Fivetran (local presence not confirmed), Gear Second, Hyperconnect, Imagoworks, IoTrust (local presence not confirmed), Karrot (Daangn Market), Konny by Erin, National Vision Inc. (local presence not confirmed), NFTBank (local presence not confirmed), Pinnu Analytics (local presence not confirmed), Snowflake (local presence not confirmed), Snowflake Korea, SOCAR (local presence not confirmed), Toss Income, Toss Securities, Willog, Wrtn Technologies, Zigbang (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (12)</summary>

Apache Airflow Korea User Group, Cubig, Deloitte Korea, F&L Corporation, Fairsquare Lab, Healingpaper (Gangnam Unni), Hwahae Global, Macaron Factory, Medit, Megazone Cloud, Snowflake Korea User Group (Flakers), Woongjin Thinkbig

</details>

<details><summary><b>dbt as a nice-to-have</b> (13)</summary>

AITRICS, Asta, Bagelcode (베이글코드), CJ Olive Young (CJ올리브영), Coupang, iShopCare, Next Securities, PaytaLab (Passorder) (페이타랩), Seers Technology, Turtle Knowledge (터틀날리지), UMOS ONE (유모스원), Wished, Yeogi Eottae (여기어때컴퍼니)

</details>

<details><summary><b>Not verified</b> (9)</summary>

ABLY, Bucketplace (Ohouse), Dataknows, Datarize, DK BMC, Loplat, Nexon Korea, NSUSLAB, The Pinkfong Company

</details>

<details><summary><b>Uses a different stack</b> (8)</summary>

AWSKRUG data group, AWSKRUG Women In Cloud, Channel Corp, Devsisters, Musinsa, PyLadies Seoul, Spotify (local presence not confirmed), WiDS Seoul (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (1)</summary>

- https://medium.com/daangn

</details>

<details><summary><b>Other sources checked</b> (24)</summary>

- [wanted.co.kr search and job APIs](https://www.wanted.co.kr/search?query=dbt)
- [Apache Airflow Korea User Group (Meetup, forum, YouTube)](https://www.meetup.com/korea-apache-airflow-user-group/)
- [Snowflake Korea User Group (Flakers)](https://usergroups.snowflake.com/seoul/)
- [PyLadies Seoul](https://www.meetup.com/seoul-pyladies-meetup/)
- [AWSKRUG data group](https://www.meetup.com/awskrug/)
- [velog dbt tag](https://velog.io/tags/dbt)
- [Toss tech blog](https://toss.tech/)
- [SOCAR tech blog](https://tech.socar.kr/data/2022/07/25/analytics-engineering-with-dbt)
- [Karrot (Daangn) Medium](https://medium.com/daangn) (nothing useful)
- [Databricks Korea User Group (KRUG)](https://usergroups.databricks.com/databricks-korea-user-group-krug/) (nothing useful)
- [Woowahan, Kakao, Hyperconnect, Buzzvil, Banksalad, Kakaobank, Devsisters, Inflab, Ohouse feeds](https://techblog.woowahan.com/) (nothing useful)
- [Snowflake World Tour Seoul 2026](https://www.snowflake.com/events/snowflake-world-tour-seoul/) (nothing useful)
- [dbt Summit agenda and dbt Champions pages](https://www.getdbt.com/dbt-summit/agenda) (nothing useful)
- [Women Who Code, R-Ladies, WiMLDS Seoul](https://www.meetup.com/) (nothing useful)
- [Meetup gql2 groupSearch near Seoul](https://www.meetup.com/gql2)
- [PyLadies Seoul events since 2025 (Meetup gql2)](https://www.meetup.com/seoul-pyladies-meetup/events/?type=past)
- [GDG Seoul events API](https://gdg.community.dev/api/event_slim/for_chapter/786/?status=Completed&page_size=200) (nothing useful)
- [WiDS Seoul](https://www.widsworldwide.org/events/event/wids-lahore-3/)
- [WiDS Worldwide site search (Korea)](https://www.widsworldwide.org/wp-json/wp/v2/search?search=Korea) (nothing useful)
- [Girls in Tech Korea](https://girlsintech.org/korea/) (nothing useful)
- [Women in AI Korea](https://www.womeninai.co/korea) (nothing useful)
- [event-us.kr search (여성 데이터)](https://event-us.kr/search?keyword=%EC%97%AC%EC%84%B1%20%EB%8D%B0%EC%9D%B4%ED%84%B0) (nothing useful)
- [wanted.co.kr search and job APIs](https://www.wanted.co.kr/api/chaos/search/v1/position?query=dbt)
- [GitHub organisation repositories](https://api.github.com/orgs/daangn/repos) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
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
- **Connectors:**
  - **Chapter hosts:** Herick Jee and Abi Adebayo hosted [meetups #0 to #7](https://www.meetup.com/seoul-dbt-meetup/events/312130999/). Thomas Kim (Fivetran) and Hangyeol Seo co-host [the recent ones](https://www.meetup.com/seoul-dbt-meetup/events/316380348/).
  - **Yeonguk Choo:** organises [Airflow Korea](https://www.meetup.com/korea-apache-airflow-user-group/) and is an Apache Airflow committer. The group already lets the chapter post meetups on its forum.
  - **Soo Lee and Jihwan Hyun:** lead the [Snowflake Korea User Group](https://usergroups.snowflake.com/seoul/).
  - **Seongyun Byeon:** ran 글또, a developer writing group of 639 members.
  - **[PyLadies Seoul](https://www.meetup.com/seoul-pyladies-meetup/):** ran a 2025 workshop that helped women submit first talks. Ask the organisers for introductions.

## 5. Before outreach

- [ ] **Check most "in region" calls:** only 13 of the people marked in the region have a location note with evidence. The rest were placed in Seoul from the listing during research.
- [ ] **Check romanised names:** most new names come from Korean listings. Check the spelling with each person.
- [ ] **Merge one duplicate:** Joshua Kim appears twice, as `joshua-kim` and `joshua-kim-jinsuk-kim` (IoTrust), with the same three chapter talks.
- [ ] **Check Jihwan Hyun:** the dbt Project on Snowflake talk lists only "지환" of the dbt Seoul community.
- [ ] **Check Kyung-jun Lee:** "이경준", who spoke at the 4th Airflow Korea meetup, may be the same person, so was not added again.
- [ ] **Check Chris Song:** probably the same person as 송호연, formerly VP at NFTBank.
- [ ] **Split one multi-speaker talk:** meetup #2 had four speakers on one talk. The titles came through as one string: "dbt Labs; Snowflake; Pinnu Analytics; DataMarketingKorea".
- [ ] **Check two organisers' locations:** Joshua Kim's Meetup profile says Toronto, and Kyung-jun Lee's says Sejong. Both organise in-person events in Seoul, so both stay unknown.
- [ ] **Check tier 1:** Jung Won-hyung is a job seeker who writes about dbt. The tier rule put Jung Won-hyung in tier 1, but a lightning talk fits better.
- [ ] **Balance dbt Labs and Fivetran staff:** Benoit Perigaud works at dbt Labs and is in Madrid. Thomas Kim works at Fivetran, so is labelled too. Both can speak, but check the line-up has practitioners first.
- [ ] **Check speakers based elsewhere:** Zoe Yim spoke at meetup #9 but is in Atlanta.

## 6. Next run

- **Sources to try first:**
  - **Airflow Korea and Flakers:** new events through Meetup `gql2` and `discourse.airflow-kr.org/search.json`.
  - **The chapter:** new Seoul dbt Meetup events.
  - **Job ads:** re-run the wanted.co.kr queries, keeping ads that contain the whole word "dbt". Add the Lever, Greenhouse and Ashby `site:` searches.
  - **velog:** new posts on the dbt tag.
  - **Blogs on Medium:** try the browser, or the publication's RSS feed, for Karrot, IoTrust, Musinsa and Yogiyo.
  - **Women-in-data:** ask PyLadies Seoul about speakers from its first-talk workshop. Read new AWSKRUG Women In Cloud events.
- **Women-in-data communities not yet reachable:**
  - **Women Techmakers Korea:** no Seoul chapter page with recent events was found.
  - **Girls in Tech Korea and Women in AI Korea:** the sites did not respond. Try them in a browser.
  - **event-us.kr and festa.io:** search women's tech events in a browser.
- **People from the women-in-data pass:** the 11 people added have no LinkedIn search. Most hosts are known only by a Meetup first name. Kim Naheon may be based outside Korea.
- **People to locate:**
  - **LinkedIn:** search the past speakers still unknown and not yet searched: Louis Lee and Wynn Park.
  - **GitHub:** check the accounts linked from Seokjin Han's and zuckerfrei's velog bios.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `seoul/seoul_dbt_companies.json`, the Seoul dbt Meetup, `../enriched/seoul-dbt-meetup.json` and the Seoul Capital Area. Add: "Search in English and Korean. Romanise Korean names family name first unless the person shows a preferred spelling, and give each an ASCII id."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Airflow Korea, Flakers, AWSKRUG and PyLadies Seoul events, wanted.co.kr job ads, velog, about 30 tech blog feeds and GitHub search, plus chapter history. 59 people at 59 companies, 21 of them past chapter speakers and hosts. 28 dbt job ads at 24 companies. |
| 2026-10-01 | 1 | Location pass from public pages: Meetup hosts and RSVPs, velog bios, GitHub profiles and recent in-person talks. 14 people placed. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 1 person placed. With the location pass, 15 people placed and 12 still unknown. |
| 2026-10-01 | 2 | Women-in-data pass. Checked AWSKRUG Women In Cloud, PyLadies Seoul, WiDS Seoul, GDG Seoul, Girls in Tech Korea, Women in AI Korea and event-us. Added 11 people with `sourced_via: women_in_data_community`: 1 speaker (Kim Naheon, Spotify) and 10 connectors. Added 2 community channels. The assembler also added 1 past chapter speaker from the enriched file. |
| 2026-10-01 | 3 | Company pass from wanted.co.kr and company job boards. 7 companies added, all with dbt as a plus: Yeogi Eottae, Bagelcode, PaytaLab, CJ Olive Young, UMOS ONE, Turtle Knowledge and Coupang. Wrtn Technologies' Seoul presence confirmed. 10 job ads added, now 38. |
