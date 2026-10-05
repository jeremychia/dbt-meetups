# Taipei: city notes

This file holds what is specific to Taipei. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Taipei dbt Meetup](https://www.meetup.com/taipei-dbt-meetup/), data in `taipei_dbt_companies.json`
- **Region:** the Taipei metro area. That is Taipei, New Taipei and Keelung, so Hsintien and Yungho count. Taoyuan counts too, as a commuter town. Hsinchu does not.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-01)

| | Count |
|---|---|
| Companies | 52 |
| People | 87 |
| Tier 1 leads | 31 |
| First-time speakers (publish, no talk yet) | 23 |
| Proven speakers | 55 |
| Spoke at this chapter before | 30 |
| Based in the region | 48 |
| Based elsewhere | 6 |
| Location unknown | 33 |
| With a LinkedIn profile | 20 |
| Job ads mentioning dbt | 7 |
| Past chapter meetups | 46 |
<!-- at-a-glance:end -->

## 1. Where to look in Taipei

Much of the content is in Chinese. Posts and talks are recorded under their own titles, with an English description.

### Blogs and writing platforms

- **[iThome 鐵人賽](https://ithelp.ithome.com.tw/tags/articles/dbt):** iThome's yearly 30-day writing challenge, and the richest source of first-time speakers in Taiwan. About 300 articles were read for author, series and date. Each article page gives the handle, series and date, and loads with curl and a browser user agent.
  - **Data-engineering searches:** [these searches](https://ithelp.ithome.com.tw/search?tab=ironman&search=BigQuery) found the new names. The terms were analytics engineer, 資料倉儲, BigQuery, data pipeline, Snowflake, 資料工程, Airflow, 資料治理, 資料建模, DuckDB, Databricks, ELT, Lakehouse and Metabase.
  - **The dbt tag:** gave 11 dbt series from 2023 to 2025. Most come from the chapter's own writing teams, so the authors are past speakers.
- **[dbt-local-taiwan on Medium](https://medium.com/dbt-local-taiwan):** the chapter's own publication. 10 posts were read through the [r.jina.ai](https://r.jina.ai/) reader service, because Medium blocks direct fetches.
- **[Recce blog](https://blog.reccehq.com/):** posts by Karen Hsieh, Kent Chen and Even Wei.
- **[dbt-local-taipei GitHub org](https://github.com/dbt-local-taipei):** book repositories whose contributors are past speakers.
- **[GitHub user search](https://github.com/search?q=dbt+location%3ATaiwan&type=users):** two usable profiles. Most hits are students.

### Meetups and conferences

- **[DevOps Taiwan on KKTIX](https://devops.kktix.cc/):** KKTIX is Taiwan's event-ticket site, and each organiser feed (`<org>.kktix.cc/events.json`) lists names and employers. It gave the [#70 data panel](https://devops.kktix.cc/events/meetup-70-data), co-hosted with the chapter on 2025-05-23, and a [#67 talk](https://devops.kktix.cc/events/meetup-67).
- **[COSCUP](https://coscup.org/2025/json/session.json):** Taiwan's open-source conference. The 2024 and 2025 session data gave few dbt talks, but did give an Airflow committer and some warehouse talks.
- **Meetup GraphQL:** a group search around Taipei's coordinates listed the local data groups, with past events, hosts and RSVPs with profile cities.
- **[R-Ladies Taipei](https://www.meetup.com/rladies-taipei/):** the one active women-in-data group on Meetup, with 83 past events and speaker bios that name employers. The organisers Kristen Chan, Ning Chen and Ben Chen are recorded as connectors. The talks are mostly about R and generative AI, not dbt.
- **[Taipei Women in Tech](https://www.meetup.com/taipeiwomenintech/):** 226 past events, with one data warehouse speaker since 2023.
- **Women-in-data yield:** 7 people from both groups, all tier 2 or 3 or connectors.
- **Chapter history:** every named speaker from `../enriched/taipei-dbt-meetup.json` was added. That added 27 people, and 30 people in the file have spoken at the chapter.

### Job ads

- **[Yourator](https://www.yourator.co/jobs?term[]=dbt) search API:** works, and returned 2 ads, at [Rayark](https://www.yourator.co/companies/rayark/jobs/35836) and [PChome](https://www.yourator.co/companies/PChome/jobs/40514). The ad text was never read, so neither proves dbt use.
- **[freehire.me API](https://freehire.me/api/v1/jobs/search?skills=dbt&countries=TW):** the JSON API behind freehire.me answers a plain fetch. It returns only 3 Taiwanese ads tagged dbt. The search results cut each ad at about 1,000 characters, so read `/api/v1/jobs/<slug>` for the full text. It found [Berry AI](https://jobs.ashbyhq.com/berry-ai/42cf7a6d-b3a7-4f05-b351-e77c40772f8a), a Neihu start-up that builds dbt models, and a Coupang analyst ad.
- **Greenhouse, Lever and Ashby boards:** about 55 employer slugs were tried. Appier, Dcard, Coupang, Ubiquiti, OKX and Lalamove have Taipei ads. Only Berry AI and Coupang mention dbt.

### Locations

- **Meetup `gql2`:** returns each event's hosts and RSVPs with the profile city. It was read for 36 in-person or hybrid chapter events and for R-Ladies Taipei. A host or an RSVP to the event where the person spoke gave high confidence.
- **Speaker pages and profiles:** the KKTIX pages for DevOps Taiwan #67 and #70, COSCUP 2025 speaker bios, GitHub profile pages and the OSYS (新立資訊) company site gave the rest. GitHub HTML profile pages still show the location when the API is rate-limited.
- **Medium-confidence matches:** an in-person talk in the last 2 years at an employer with a Taipei office gave medium confidence. So did a Meetup member with the same name in Taipei, Yungho or Hsintien.
- **Location pass yield:** 23 people placed, 22 in the region and 1 outside it.
- **LinkedIn search results:** 15 people were searched. It placed 1, Katy Yuan, in the San Francisco Bay Area.
- **Result:** 23 people are in the region, 2 are outside it and 44 are unknown. The evidence rules are in [location rules](../research/README.md#6-location-rules).

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[WiDS Taipei](https://www.widstaipei.org/):** the best source. Taiwanese in Data Science runs a one-day conference of women data scientists each May, in person and on Zoom. The [2024](https://www.widstaipei.org/conference-2024-chinese) and [2026](https://www.widstaipei.org/conference-2026-chinese) pages name 8 speakers each with employers, but no talk titles. The [Medium feed](https://medium.com/feed/women-in-data-science-taipei) has a write-up of each 2025 and 2026 talk with the speaker's bio. It reads with a plain fetch.
- **WiDS Taipei data talks:** Tricia Tsai (RHINOSHIELD) on building a data team from zero (2025). 姜乃文 (CommonWealth Magazine Group) on generative BI (2026). 林蒧均 (Chung-Hua Institution for Economic Research) on data cleaning for decisions (2026). AnLei Huang (Databricks, Singapore) on trustworthy analytics agents (2026). Alyssa Chen, Karen Hsieh and Lany Liu, already in the file, also spoke. 9 ambassadors from 2024 to 2026 are recorded as connectors.
- **[WTM Taipei](https://gdg.community.dev/gdg-taipei/):** Women Techmakers Taipei runs through GDG Taipei. The GDG events API (chapter 748) holds every event's details. The [Design x Data Meetup](https://gdg.community.dev/e/my8yxb/) (September 2025, at Dcard) had talks by Jamin Fan and Ricky Yu, both past chapter speakers. The other WTM events since 2024 are career workshops.
- **Also ask:** the WiDS Taipei organisers and Alyssa Chen's 數聚村莊 community for speakers.

## 2. What didn't work here

- **Web search:** ran out after 3 calls, so there was no LinkedIn search during research and no job-ad search. The rest of the run used direct page fetches, open APIs and each site's own search.
- **Job boards:** Cloudflare blocks the ad pages on [Yourator](https://www.yourator.co/jobs?term[]=dbt), [Cake](https://www.cake.me/jobs/dbt), 104 and Medium. The reader service does not get through.
- **The iThome dbt tag on its own:** mostly returns the chapter's own writing teams, who are already past speakers. Use the data-engineering searches too.
- **GitHub API:** returned a rate-limit error on the first call.
- **Company feeds on Medium:** [Dcard](https://medium.com/dcardlab), Pinkoi, Hahow and others had no dbt posts in the recent feeds.
- **Other local groups:** [PyData Taipei](https://www.meetup.com/pydata-taipei/), GDG Taipei, Taipei.py and AI Engineers in Taiwan had no data-stack talks since 2023.
- **[PyCon TW](https://tw.pycon.org/):** the talk list needs a login, so it was not read.
- **Women-in-data sources with nothing new:** Meetup's group search near Taipei found only R-Ladies Taipei and Taipei Women in Tech, both already covered. [PyLadies Taiwan on KKTIX](https://pyladies.kktix.cc/events.json) has had no event since 2014. [Girls in Tech Taiwan](https://girlsintech.org/taiwan/) did not respond. The WiDS Taipei 2025 page shows speakers only in images.
- **[104 job bank API](https://www.104.com.tw/jobs/search/api/jobs?keyword=dbt):** returns a Cloudflare challenge.
- **[Yourator search API](https://www.yourator.co/api/v4/jobs?term[]=dbt):** matches DDT and DBA as well as dbt. The ad pages are still blocked.
- **Meetup `gql2` near Taipei:** no data, Snowflake, Databricks or BigQuery group beyond the chapter. Venues since 2024 are Dcard and AppWorks, both already in the file.
- **GitHub code search:** no public `dbt_project.yml` in the Dcard, 91APP, Appier, Gogoro, KKday, Hahow or iKala organisations. Pinkoi and CakeResume hit the rate limit.
- **Hacker News Who is hiring:** no Taiwanese role mentions dbt.

## 3. Companies looked at

- **The most active chapter:** the Taipei dbt Meetup is the most active dbt chapter worldwide, with 46 past meetups from 2022-08-17 to 2026-08-26.
- **Employer not identified:** 25 people sit under this placeholder because no employer was found. Most are iThome authors.
- **Recce:** the employer of Karen Hsieh, who organises the chapter, and of two first-time speakers, Kent Chen and Even Wei.

<!-- companies:start -->
51 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (20)</summary>

Berry AI, Census (local presence not confirmed), Databricks (local presence not confirmed), Datacoves (local presence not confirmed), Dcard, DeepHow (local presence not confirmed), Ethyca (local presence not confirmed), ex-ByteDance (local presence not confirmed), foodpanda (local presence not confirmed), Infinite Lambda (local presence not confirmed), Junyi Academy (均一平台教育基金會), KKday (local presence not confirmed), Migo, NTNU (local presence not confirmed), Pinkoi (local presence not confirmed), Recce (InfuseAI), Replware (睿博資訊), Teamson (local presence not confirmed), TVBS, Wise (formerly Transferwise) (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (4)</summary>

91APP, iCook (愛料理), Xtraspots Inc (local presence not confirmed), 線性成長數位 (Linear Growth Digital)

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

Coupang

</details>

<details><summary><b>Not verified</b> (11)</summary>

Appier, AppWorks School, E.Sun Bank (玉山銀行), Microsoft Taiwan (台灣微軟), Partipost, PChome Online, StashAway (local presence not confirmed), Taiwan Kadokawa (台灣角川), Trend Micro (趨勢科技), 瑞嘉軟體 (Ruijia Software), 雷亞遊戲 Rayark Inc.

</details>

<details><summary><b>Uses a different stack</b> (15)</summary>

AILogora (local presence not confirmed), Chung-Hua Institution for Economic Research (中華經濟研究院), CommonWealth Magazine Group (天下雜誌), COSCUP, DevOps Taiwan, Employer not identified (local presence not confirmed), Financial-sector employer (not named) (local presence not confirmed), Greenpeace East Asia (綠色和平), iThome (iT 邦幫忙), R-Ladies Taipei, RHINOSHIELD (犀牛盾), Taipei Women in Tech, Taiwanese in Data Science (TWiDS) / WiDS Taipei, The Reporter (報導者) (local presence not confirmed), 新立資訊 OSYS

</details>

<details><summary><b>Blogs and sites scanned</b> (3)</summary>

- https://docs.getdbt.com/community/spotlight/karen-hsieh
- https://ithelp.ithome.com.tw/articles/10314288
- https://ithelp.ithome.com.tw/articles/10317471

</details>

<details><summary><b>Other sources checked</b> (31)</summary>

- [iThome 鐵人賽 dbt search and tag](https://ithelp.ithome.com.tw/tags/articles/dbt)
- [iThome 鐵人賽 data-engineering searches](https://ithelp.ithome.com.tw/search?tab=ironman&search=BigQuery)
- [dbt-local-taiwan Medium publication](https://medium.com/dbt-local-taiwan)
- [Recce blog](https://blog.reccehq.com/)
- [DevOps Taiwan on KKTIX](https://devops.kktix.cc/)
- [R-Ladies Taipei (Meetup GraphQL)](https://www.meetup.com/rladies-taipei/)
- [Taipei Women in Tech (Meetup GraphQL)](https://www.meetup.com/taipeiwomenintech/)
- [COSCUP 2024 and 2025 sessions](https://coscup.org/2025/json/session.json)
- [PyData Taipei, GDG Taipei, Taipei.py, AI Engineers in Taiwan (Meetup GraphQL)](https://www.meetup.com/pydata-taipei/) (nothing useful)
- [GitHub user search (dbt / analytics engineer, Taiwan)](https://github.com/search?q=dbt+location%3ATaiwan&type=users)
- [dbt-local-taipei GitHub org](https://github.com/dbt-local-taipei) (nothing useful)
- [Yourator job search (dbt)](https://www.yourator.co/jobs?term[]=dbt) (nothing useful)
- [104, Cake job boards](https://www.cake.me/jobs/dbt) (nothing useful)
- [Taiwanese company Medium feeds (Dcard, Pinkoi, Hahow and others)](https://medium.com/dcardlab) (nothing useful)
- [PyCon TW talk API](https://tw.pycon.org/) (nothing useful)
- [Meetup gql2 groupSearch near Taipei](https://www.meetup.com/gql2)
- [WiDS Taipei 2024 conference](https://www.widstaipei.org/conference-2024-chinese)
- [WiDS Taipei 2025 conference](https://www.widstaipei.org/conference-2025-chinese)
- [WiDS Taipei 2026 conference](https://www.widstaipei.org/conference-2026-chinese)
- [WiDS Taipei Medium feed](https://medium.com/feed/women-in-data-science-taipei)
- [WiDS Worldwide site search (Taipei)](https://www.widsworldwide.org/wp-json/wp/v2/search?search=Taipei)
- [GDG Taipei events API (WTM Taipei)](https://gdg.community.dev/api/event_slim/for_chapter/748/?status=Completed&page_size=200) (nothing useful)
- [WTM Taipei Design x Data Meetup](https://gdg.community.dev/e/my8yxb/)
- [PyLadies Taiwan on KKTIX](https://pyladies.kktix.cc/events.json) (nothing useful)
- [Girls in Tech Taiwan](https://girlsintech.org/taiwan/) (nothing useful)
- [freehire.me API, Taiwan, skill dbt](https://freehire.me/api/v1/jobs/search?skills=dbt&countries=TW)
- [Greenhouse, Lever and Ashby boards](https://api.ashbyhq.com/posting-api/job-board/berry-ai)
- [Yourator search API](https://www.yourator.co/api/v4/jobs?term[]=dbt) (nothing useful)
- [104 job bank API](https://www.104.com.tw/jobs/search/api/jobs?keyword=dbt) (nothing useful)
- [GitHub code search for dbt_project.yml](https://github.com/search?q=filename%3Adbt_project.yml&type=code) (nothing useful)
- [Hacker News Who is hiring (Algolia)](https://hn.algolia.com/api/v1/search?query=dbt%20taipei&tags=comment) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **阿晟 (`a-sheng-ithome`):** wrote a 2024 30-day series on [adopting dbt after BigQuery stored procedures](https://ithelp.ithome.com.tw/articles/10352522). It includes [why the team did not use the dbt Semantic Layer](https://ithelp.ithome.com.tw/articles/10365950). The employer is not stated. This may be 高晟 from Junyi Academy, who co-presented at the chapter in November 2023.
  - **Kent Chen (Recce):** wrote [Designing Reliable AI Agents for dbt Data Reviews](https://blog.reccehq.com/designing-reliable-ai-agents-for-dbt-data-reviews) in 2026.
  - **Shawn:** wrote a 2024 [DataOps series](https://ithelp.ithome.com.tw/articles/10351379) on Airflow, dbt and dbt Power User. The employer is not stated.
  - **mengchieh_30435:** wrote [30 天從 BI 走向 Data Engineering](https://ithelp.ithome.com.tw/articles/10381168) in 2025, on moving from BI to data engineering with BigQuery and Looker Studio.
  - **Even Wei (Recce):** wrote [Session Base per PR: Why Data Reviews Lie](https://blog.reccehq.com/session-base-per-pr-why-data-reviews-lie) in 2026. Check for earlier talks elsewhere.
- **Anchor speakers:**
  - **Mars Su (Trend Micro):** Staff Data Engineer, on the [DevOps Taiwan #70 data panel](https://devops.kktix.cc/events/meetup-70-data). dbt use at Trend Micro is not confirmed.
  - **Ted Liang (91APP):** a Director who gave [From Data Team to BizDevOps Team](https://devops.kktix.cc/events/meetup-67) and sat on the #70 panel. This is probably the "Ted" who spoke at the chapter in 2022-12.
  - **KC (Edison) Lai (TVBS):** wrote a 3-part series on the TVBS data stack, starting with [TVBS數據架構大解密 (1)](https://medium.com/dbt-local-taiwan/tvbs-modern-data-stack-1-6d5f3049d724). This is probably the "Edison" who spoke at the chapter in 2024-08.
  - **Joshua Lin (Migo):** wrote [在 DBT 上管理 BigQuery UDF](https://medium.com/dbt-local-taiwan/%E5%9C%A8-dbt-%E4%B8%8A%E7%AE%A1%E7%90%86-bigquery-udf-205eb04cad76) and a [30-day dbt series](https://ithelp.ithome.com.tw/articles/10350436) in 2024.
- **Connectors:**
  - **Chapter organisers and hosts:** Karen Hsieh (Recce, [Meetup profile](https://www.meetup.com/members/148619732/)), Laurence Chen (Replware, [Meetup profile](https://www.meetup.com/members/199851159/)) and Allen Wang ([Meetup profile](https://www.meetup.com/members/164426832/)) host the chapter's in-person events.
  - **[R-Ladies Taipei](https://www.meetup.com/rladies-taipei/):** Kristen Chan (Microsoft), Ning Chen and Ben Chen run it. Ask the organisers for introductions to women in the Taipei data community.
  - **孫玉峰 (Taiwan Kadokawa):** co-organises the Taiwan R User Group and hosts R-Ladies Taipei events ([Meetup profile](https://www.meetup.com/members/110970552/)).
  - **[DevOps Taiwan](https://devopstw.club/):** has co-hosted with the chapter and runs a speaker call at [cfs.devopstw.club](https://cfs.devopstw.club/).
  - **Chapter channels:** the [dbt Slack](https://www.getdbt.com/community/join-the-community) channel #local-taipei (about 300 members in 2024), the [YouTube channel](https://www.youtube.com/@dbt-local-taipei) and the [鬼鴞說資料 podcast](https://open.spotify.com/show/4F9G9SIKKl8Days5W91suM), which featured the chapter in 2024.

## 5. Before outreach

- [ ] **Confirm real names:** about 20 people are known only by a handle or a Chinese name. Most iThome authors write under a handle, and some only give a Chinese name. Confirm the name and its spelling before writing.
- [ ] **Check the romanisation:** each person's `name` is shown exactly as published. Each `id` is an ASCII version of it. A handle keeps its spelling plus `-ithome` (e.g. `mengchieh-ithome`). A Chinese name is spelled out in Hanyu Pinyin (e.g. 孫玉峰 → `sun-yu-feng`, 狸貓 → `limao-ithome`). Many people in Taiwan use a different romanisation, so confirm the spelling with each person.
- [ ] **Match first-name and Chinese-name speakers:** some past speakers are listed by first name only (Sam at Dcard, Joshua, Edison, Stephen, Ellen) or by Chinese name only (the Junyi Academy trio). These cannot be matched to other records by name.
- [ ] **Confirm the probable past speakers:** Joshua Lin, KC (Edison) Lai and Ted Liang are probably chapter speakers listed by first name. 阿晟 may be 高晟 of Junyi Academy.
- [ ] **Check tier 1:** the tier rule puts every first-time speaker with writing from 2024 onwards in tier 1. That includes authors whose posts touch dbt only lightly, such as 狸貓 (PostHog), summerzoe (marketing tech) and liviachen (a dbt beginner). Read each suggested talk angle first.
- [ ] **Check cities shown without evidence:** many people have Taipei as the city but an unknown location. The city came from the listing, not from evidence.
- [ ] **Check Ning Chen's location:** the Meetup profile says Seattle, but Ning Chen co-hosts R-Ladies Taipei events held in person in 2025. The location stays unknown.
- [ ] **Check two-city and name-only calls:** Ian Ma's GitHub location reads "New Jersey / Taipei", so Ian Ma is in region at medium only. CL Kao, Joshua Lin, Bruce Huang, Bowen Kuo, Ping-Lin Chang and douenergy are in region from name-only Meetup matches.
- [ ] **Check people likely elsewhere:** Terrence Toh's employer is in Singapore. Datacoves and Infinite Lambda have no confirmed Taipei office, so Noel Gomez and Michael Han stay unknown.
- [ ] **Skip people outside the region:** Zhe-You (Jason) Liu is in Tainan and Katy Yuan is in the San Francisco Bay Area.

## 6. Next run

- **Sources to try first:**
  - **iThome 鐵人賽:** new series from the data-engineering search terms, not only the dbt tag. Fetch with curl and a browser user agent.
  - **Events:** new chapter, R-Ladies Taipei and DevOps Taiwan events through Meetup `gql2` and `<org>.kktix.cc/events.json`.
  - **Blogs:** the dbt-local-taiwan and Recce blogs, with Medium through r.jina.ai.
  - **Job ads:** try LinkedIn Jobs (logged out) and Lever, Greenhouse and Ashby `site:` searches. Taiwan's own job boards block page fetches.
  - **[PyCon TW](https://tw.pycon.org/):** read the talks through the browser, since the talk list needs a login.
- **People to locate:**
  - **LinkedIn:** search the tier 1 and 2 people not yet searched. Check the unsure results first.
  - **Ricky Yu:** a likely Dcard profile in Taipei, but nothing ties it to the chapter talk.
  - **Even Wei and Shih Mei-Cheng:** the search summaries named New Taipei and Taipei, but no result showed the profile.
  - **Kevin Chien (DeepHow) and Tom Sung (Bitfinex):** the results gave only "Taiwan".
  - **Michael Han (Infinite Lambda):** the result showed no location.
  - **Past speakers with no employer:** Jamin Fan, Ricky Yu and Benny Xu spoke in region but have no employer on record. Find one, and the medium rule can then place all three. Ricky Yu also gave a WTM Taipei talk in person at Dcard in September 2025.
  - **簡妙蓉:** check whether the [R-Ladies Taipei talk](https://www.meetup.com/rladies-taipei/events/305306204/) was given in person.
- **Women-in-data communities not yet reachable:**
  - **WiDS Taipei 2024 talk titles:** the conference page gives none. Ask the organisers, or read the 2024 posts on Medium through r.jina.ai.
  - **WiDS Taipei 2025 speakers:** shown only in images. 4 of them were found through the Medium feed.
  - **PyLadies Taiwan and Girls in Tech Taiwan:** no current event page was found.
  - **Women Who Code Taipei:** Women Who Code closed in 2024. Taipei Women in Tech carries on its alumni.
- **People from the women-in-data pass:** the 18 people added have no LinkedIn search.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `taipei/taipei_dbt_companies.json`, the Taipei dbt Meetup, `../enriched/taipei-dbt-meetup.json` and the Taipei metro area (Taipei, New Taipei and Keelung, plus Taoyuan; not Hsinchu). Add: "Search in Traditional Chinese and English. Show each name as published, and give each an ASCII id: the handle plus `-ithome`, or Hanyu Pinyin."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. iThome 鐵人賽, the chapter's Medium publication, the Recce blog, DevOps Taiwan on KKTIX, COSCUP, R-Ladies Taipei and Taipei Women in Tech, GitHub and Yourator, plus chapter history. 69 people at 44 companies, 30 of them past chapter speakers. 23 emerging voices and 30 tier-1 leads. 2 job ads, neither read. |
| 2026-10-01 | 1 | Location pass from public pages: Meetup hosts and RSVPs, KKTIX and COSCUP speaker pages, GitHub profiles and recent in-person talks. 23 people placed, 22 of them in the region. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 15 people searched and 1 placed, outside the region. With the location pass, 23 people are in the region, 2 outside it and 44 unknown. |
| 2026-10-01 | 2 | Women-in-data pass. Checked WiDS Taipei (2024 to 2026 and its Medium feed), WTM Taipei through GDG Taipei, PyLadies Taiwan and Girls in Tech Taiwan. Added 18 people with `sourced_via: women_in_data_community`: 9 speakers and 9 WiDS Taipei ambassadors as connectors. Added talks for Alyssa Chen, Karen Hsieh, Lany Liu, Jamin Fan and Ricky Yu. Added 2 community channels. |
| 2026-10-01 | 3 | Company pass from job ads: the freehire.me API and Greenhouse, Lever and Ashby boards. 2 companies added: Berry AI (strong) and Coupang (nice-to-have). The 104, Yourator, Meetup and GitHub checks found nothing new. |
