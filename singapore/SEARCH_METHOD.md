# Singapore: city notes

This file holds what is specific to Singapore. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Singapore dbt Meetup](https://www.meetup.com/singapore-dbt-meetup/), data in `singapore_dbt_companies.json`
- **Region:** Singapore. Kuala Lumpur, Ho Chi Minh City and Sydney do not count.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-01)

| | Count |
|---|---|
| Companies | 136 |
| People | 89 |
| Tier 1 leads | 20 |
| First-time speakers (publish, no talk yet) | 14 |
| Proven speakers | 66 |
| Spoke at this chapter before | 28 |
| Based in the region | 70 |
| Based elsewhere | 5 |
| Location unknown | 14 |
| With a LinkedIn profile | 47 |
| Job ads mentioning dbt | 211 |
| Past chapter meetups | 16 |
<!-- at-a-glance:end -->

## 1. Where to look in Singapore

### Meetups and conferences

- **[GovTech STACK [Data] meetups](https://www.developer.tech.gov.sg/communities/events/stack-meetups/):** the richest source of Singapore data speakers. 8 monthly events from 2025-11 to 2026-09 gave 25 named speakers. Each page lists every speaker with title and agency. No talk mentions dbt.
- **[Snowflake User Group Singapore](https://usergroups.snowflake.com/singapore/):** 4 events. It gave Grab and Infinite Lambda speakers and the group's organisers.
- **[DataScience SG](https://www.meetup.com/datascience-sg-singapore/):** 7 events in 2025 and 2026, mostly on AI. Meetup group pages give past events through the `__NEXT_DATA__` block.
- **[PyCon Singapore 2026](https://pycon.sg/speakers.html):** few data talks. It gave some Grab machine learning engineers.
- **[PyLadies Singapore](https://pyladies.sg):** the team and the PyCon Singapore 2025 track. 3 people are tagged from it and from Women Devs SG.
- **Chapter history:** every named speaker from `../enriched/singapore-dbt-meetup.json` was added. That covers 16 events, from 2022-07-07 to 2026-09-23. The research added new evidence for 2 past speakers, Michael Han and Cliff Chew.

### Blogs and authors

- **[Infinite Lambda case studies](https://infinitelambda.com/case-studies/):** name dbt users that no job ad shows. Mandai Wildlife Group and Keppel use dbt. Only Mandai has a job ad, and its text does not name dbt.
- **[Grab tech blog](https://engineering.grab.com/feed.xml):** the data mesh series and a post on AI in analytics. No post mentions dbt.
- **[Holistics blog](https://www.holistics.io/blog/):** posts on analytics as code.
- **[DEV dbt tags](https://dev.to/t/dbt):** 231 authors checked, and 1 is in Singapore.
- **[GitHub user search](https://github.com/search?q=dbt+location%3ASingapore&type=users):** mostly students. One weak lead was kept.

### Job ads

- **[freehire.me](https://freehire.me/jobs?countries=sg&skills=dbt):** the one job board that fetches without a login. 4 of its 10 pages were read, 80 ads in all. Direct employers include Endowus, Grasshopper, Secretlab, Traveloka, OCBC and LTA. About half the ads are from recruiters with unnamed clients.
- **[TheirStack](https://theirstack.com/en/technology/dbt/sg):** the top 10 of 137 companies that use dbt are visible without a login.
- **Yield:** 21 job ads at 19 companies.
- **[MyCareersFuture API](https://api.mycareersfuture.gov.sg/v2/jobs?search=dbt&limit=100):** the government job board answers a plain fetch with the full ad text, the registered employer name and the posting date. A search for dbt returns 36 ads. Searches for data engineer, snowflake and bigquery, filtered for the whole word dbt, found no more. It added Workato, Pluang and many recruiters.
- **[freehire.me API](https://freehire.me/api/v1/jobs/search?skills=dbt&countries=SG):** the JSON API behind freehire.me answers a plain fetch. Two calls return all 200 Singapore ads tagged dbt. The search results cut each ad at about 1,000 characters, so read `/api/v1/jobs/<slug>` for the full text. It added Wise, Coda, Ascenda, Agilent, Sofina, Boku and Flo Energy.
- **Greenhouse, Lever and Ashby boards:** about 100 employer slugs were tried. Airwallex, Workato, Coinhako and Thunes have Singapore ads that mention dbt.
- **Yield of the company pass:** 190 more job ads and 76 new companies. About a third of the new companies are recruiters.

### Locations

- **Meetup `gql2`:** gave every past chapter event with hosts, RSVPs and member cities. An RSVP to the event where the person spoke gave high confidence.
- **Recent chapter talks:** an in-person chapter talk in the last 2 years, at an employer with a Singapore office, gave medium confidence.
- **LinkedIn search results:** 15 people were searched. It placed 5 in Singapore and 1 in Sydney. 3 LinkedIn URLs were carried over from the Kuala Lumpur file.
- **Yield:** 17 people placed across both passes, and 14 still unknown. The evidence rules are in [location rules](../research/README.md#6-location-rules).

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[Women Devs SG](https://www.meetup.com/women-devs-sg/):** the most active women-in-tech group, with 45 events since June 2024. Two were data events: [Web3 data analytics](https://www.meetup.com/women-devs-sg/events/301544159/) (July 2024) and a [Dataiku data science walkthrough](https://www.meetup.com/women-devs-sg/events/303595492/) (October 2024). The event pages rarely name speakers. The hosts Victoria Lo, Saloni, Toshal Patel and Diya Naresh are recorded as connectors. Aishwarya E, already in the file, is the main host.
- **[R-Ladies Singapore](https://www.meetup.com/rladies-singapore-sg/):** founded in 2024, with 4 events to January 2025. The organiser, Liang Tian, is a connector.
- **[WiDS Singapore @ Dataiku](https://www.widsworldwide.org/events/event/wids-singapore-dataiku/):** an in-person regional conference in May 2023. The Dataiku ambassador, Nasim Bano Sheena Nasim, is a connector.
- **WiDS Taipei:** AnLei Huang, a Databricks solution engineer in Singapore, [spoke at WiDS Taipei 2026](https://medium.com/women-in-data-science-taipei/wids-taipei-2026-building-trustworthy-systems-through-imperfection-by-anlei-huang-2685a5372a8f) on trustworthy analytics agents and semantics. This is the strongest data speaker from this pass.
- **Also ask:** the Women Devs SG hosts to share the call for speakers, and Dataiku for the WiDS Singapore network.

## 2. What didn't work here

- **Web search:** ran out after about 12 calls. The rest of the run used direct fetches of pages, plus the GitHub and DEV APIs.
- **[Singapore Data & AI Engineering Meetup](https://www.meetup.com/singapore-data-ai-engineering-meetup/):** AI and Ray talks, with no dbt.
- **dbt Labs events:** none of the 227 dbt Summit and case-study pages in the [getdbt.com sitemap](https://www.getdbt.com/sitemap-0.xml) names a Singapore company. The dbt World Tour stops in Sydney, Melbourne, Auckland and Tokyo, but not Singapore.
- **Medium publications:** foodpanda data, ShopBack, Traveloka, Ninja Van, GovTech's data science division, Carousell and Airwallex had no post that mentions dbt. Medium returns HTTP 429, so they were read through [rss2json](https://api.rss2json.com/). rss2json worked for about 6 publications, then rate-limited too.
- **[Indeed Singapore](https://sg.indeed.com/q-dbt-jobs.html):** HTTP 403.
- **JavaScript-rendered pages:** the [Luma DataScience SG calendar](https://luma.com/datascienceSG) and the [Databricks User Group Singapore](https://community.databricks.com/t5/singapore/databricks-user-group-singapore-meetup/m-p/124414) page came back empty.
- **GitHub API:** rate-limited, and code search hit its limit.
- **Grab and Holistics author pages:** list posts only, with no location.
- **Women-in-data groups:** no Singapore women-in-data group was found with dbt talks.
- **Other women-in-data sources:** [Singapore WiMLDS](https://www.meetup.com/singapore-women-in-machine-learning-and-data-science/) has held no event since 2023. The Women Techmakers International Women's Day events with [GDG Singapore](https://gdg.community.dev/gdg-singapore/) (2024 and 2025) had AI workshops and named no speakers. [She Loves Data](https://www.shelovesdata.com/) now runs global online AI courses, and its events page returns 404. Girls in Tech Singapore did not resolve. Women Who Code closed in 2024.
- **Company job boards:** Grab, Shopee, Carousell, ShopBack, PropertyGuru, Endowus, Gojek and foodpanda have no public Greenhouse, Lever or Ashby board.
- **Hacker News Who is hiring:** no Singapore role mentions dbt. The only hit was a global remote ad.
- **GitHub code search:** no public `dbt_project.yml` in the Grab, Carousell, GovTech, Open Government Products, data.gov.sg or Traveloka organisations.
- **Ads left out:** remote ads, an ad in French, and ads where DBT means digital business transformation.

## 3. Companies looked at

- **Almost no public dbt content:** most Singapore leads are data engineers who spoke about pipelines, data mesh or semantic layers. GovTech's Data Practice, Singapore Customs and Grab show strong data teams but no public dbt use.
- **Recruiters:** about half the job ads have unnamed clients. For speaker sourcing, filter on `type == "employer"`.
- **Infinite Lambda:** a consultancy whose clients Mandai and Keppel use dbt. Michael Han of Infinite Lambda can introduce a client speaker.
- **Overlap with Kuala Lumpur:** Feng Cheng and Chang Boon Heng appear in both datasets.

<!-- companies:start -->
135 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (46)</summary>

Agilent Technologies, Allium, almapay, Ascenda, BAH Partners, Boku, CFGI Singapore, Coda, dbt Labs, Endowus, ExpressVPN, Flo Energy, foodpanda, Grasshopper, Hyphen Connect, Infinite Lambda, Intellect Minds, Keppel, Lightdash (local presence not confirmed), Mandai Wildlife Group, Meta (local presence not confirmed), Michael Faith HR Consultants, OCBC, OX Consultancy, PathSource Consulting, Pluang, Principle Partners, Qualcomm, Randstad, Razer, Sciente International, Secretlab, ShopBack, Snowflake, Snowplow (local presence not confirmed), Sofina, Spenmo (local presence not confirmed), Techcom Solutions, Teleport (local presence not confirmed), Toggl (local presence not confirmed), Traveloka, Trinity HR Solutions, Unchain Data, Vinted (local presence not confirmed), Wise, Workato

</details>

<details><summary><b>Some dbt signal</b> (61)</summary>

3 Cubed Business Consulting, Accord Innovations, Airwallex, Apple, Argyll Scott, Assurity Trusted Solutions, Career International, Cartier, Centience, CI&T, Coinhako, Console Connect, Dell Technologies, dtcpay, Dyson (local presence not confirmed), Eames Consulting Group, Evolution Recruitment Solutions, EY, Firmus, FPT Software, GIC, GlobalCatalyst International, Goodnotes, Google, GovTech Singapore (Government Technology Agency), heymax, Holistics Software (local presence not confirmed), HTX (Home Team Science & Technology Agency), Intrepid Asia (local presence not confirmed), JCO Analytics, Jobster, JonDavidson, K2 Partnering Solutions, Klook (local presence not confirmed), Kopi Recruit, Kris Infotech, Land Transport Authority (LTA), Merck, Michael Page, Momcozy, NAS Education, NCS, OneByZero, Optimum Solutions, Paradex, PERSOL Singapore, Rakuten Viki, Rapsys Technologies, Red Alpha Cybersecurity, ScienTec Personnel, SensorFlow (local presence not confirmed), Skinlab The Medical Spa, Straive (local presence not confirmed), Talentreq Partners, Temasek, Thunes, TikTok, Trinity Consulting Services, Valor Capital Group, Vinova, Websparks

</details>

<details><summary><b>dbt as a nice-to-have</b> (8)</summary>

A*STAR, AIM Global Talent, Climate Impact X, JPMorgan Chase, Minden.ai, Simular, Supermetrics, Western Digital

</details>

<details><summary><b>Not verified</b> (14)</summary>

Amazon Web Services (AWS), Carousell, ClickHouse (local presence not confirmed), Grab, Health Promotion Board (HPB), Infocomm Media Development Authority (IMDA), Microsoft, Ninja Van, Open Government Products (OGP) / data.gov.sg, Redis, Singapore Customs, Tata Consultancy Services (TCS), Tech in Asia, Urban Redevelopment Authority (URA)

</details>

<details><summary><b>Uses a different stack</b> (6)</summary>

Databricks, Dataiku, DataScience SG, PyLadies Singapore, R Ladies Singapore, Women Devs SG

</details>

<details><summary><b>Blogs and sites scanned</b> (9)</summary>

- https://engineering.grab.com/feed.xml
- https://medium.com/airwallex-engineering
- https://medium.com/carousell-insider
- https://medium.com/dsaid-govtech
- https://medium.com/foodpanda-data
- https://medium.com/ninjavan-tech
- https://medium.com/shopback-tech-blog
- https://medium.com/traveloka-engineering
- https://www.holistics.io/blog/

</details>

<details><summary><b>Other sources checked</b> (32)</summary>

- [GovTech STACK [Data] meetups](https://www.developer.tech.gov.sg/communities/events/stack-meetups/)
- [Snowflake User Group Singapore](https://usergroups.snowflake.com/singapore/)
- [freehire.me dbt jobs, Singapore](https://freehire.me/jobs?countries=sg&skills=dbt)
- [TheirStack dbt in Singapore](https://theirstack.com/en/technology/dbt/sg)
- [Indeed Singapore](https://sg.indeed.com/q-dbt-jobs.html) (nothing useful)
- [DataScience SG meetup](https://www.meetup.com/datascience-sg-singapore/)
- [Singapore Data & AI Engineering Meetup](https://www.meetup.com/singapore-data-ai-engineering-meetup/)
- [PyCon Singapore 2026](https://pycon.sg/speakers.html)
- [PyLadies Singapore](https://pyladies.sg)
- [Grab tech blog](https://engineering.grab.com/feed.xml)
- [Medium feeds (foodpanda-data, shopback-tech-blog, traveloka-engineering, ninjavan-tech, dsaid-govtech, carousell-insider, airwallex-engineering)](https://medium.com/foodpanda-data)
- [getdbt.com summit agenda and case-study pages](https://www.getdbt.com/sitemap-0.xml) (nothing useful)
- [Infinite Lambda case studies](https://infinitelambda.com/case-studies/)
- [Holistics blog](https://www.holistics.io/blog/)
- [DEV Community dbt tags](https://dev.to/t/dbt)
- [GitHub users in Singapore mentioning dbt](https://github.com/search?q=dbt+location%3ASingapore&type=users) (nothing useful)
- [Databricks User Group Singapore](https://community.databricks.com/t5/singapore/databricks-user-group-singapore-meetup/m-p/124414) (nothing useful)
- [Luma DataScience SG calendar](https://luma.com/datascienceSG) (nothing useful)
- [Meetup gql2 groupSearch near Singapore](https://www.meetup.com/gql2)
- [Women Devs SG past events (Meetup gql2)](https://www.meetup.com/women-devs-sg/)
- [R Ladies Singapore (Meetup gql2)](https://www.meetup.com/rladies-singapore-sg/)
- [Singapore WiMLDS (Meetup gql2)](https://www.meetup.com/singapore-women-in-machine-learning-and-data-science/) (nothing useful)
- [GDG Singapore events API (Women Techmakers)](https://gdg.community.dev/api/event_slim/for_chapter/495/?status=Completed&page_size=300) (nothing useful)
- [WiDS Singapore @ Dataiku](https://www.widsworldwide.org/events/event/wids-singapore-dataiku/)
- [WiDS Singapore (online)](https://www.widsworldwide.org/events/event/wids-singapore/) (nothing useful)
- [She Loves Data](https://www.shelovesdata.com/) (nothing useful)
- [Girls in Tech Singapore](https://girlsintech.org/singapore/) (nothing useful)
- [MyCareersFuture API](https://api.mycareersfuture.gov.sg/v2/jobs?search=dbt&limit=100)
- [freehire.me API, Singapore, skill dbt](https://freehire.me/api/v1/jobs/search?skills=dbt&countries=SG)
- [Greenhouse, Lever and Ashby boards](https://api.ashbyhq.com/posting-api/job-board/airwallex)
- [Hacker News Who is hiring (Algolia)](https://hn.algolia.com/api/v1/search?query=dbt%20singapore&tags=comment) (nothing useful)
- [getdbt.com case studies (llms-full-case-studies.txt)](https://www.getdbt.com/llms-full-case-studies.txt) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
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
- **Connectors:**
  - **Jing Yu Lim (Spenmo):** hosts [every chapter event](https://www.meetup.com/singapore-dbt-meetup/events/316411854/) and has given 3 talks.
  - **Yap Ghim Eng (GovTech):** hosts the [STACK data meetups](https://www.developer.tech.gov.sg/communities/events/stack-meetups/), the route to public-sector speakers and a venue.
  - **Suteja Kanuri, Yun Fei Choo (Snowflake) and Piyush Gupta (Temasek):** organise the [Snowflake User Group Singapore](https://usergroups.snowflake.com/singapore/), a natural co-host.
  - **Koo Ping Shung:** co-founded [DataScience SG](https://luma.com/datascienceSG).
  - **Hwee Shan Tay:** co-chairs [PyLadies Singapore](https://pyladies.sg). Ask the co-chairs to share the call for speakers.

## 5. Before outreach

- [ ] **Check most "in region" calls:** only 13 of the people marked in Singapore have a location note with evidence. The rest were placed from the employer or event during research.
- [ ] **Ask about dbt use:** most leads have no public dbt content. Ask each one whether the team uses dbt.
- [ ] **Check tier 1:** the first-time speaker rule raised the Grab and Holistics authors to tier 1, but the posts don't mention dbt. Treat these authors as speakers on a data topic.
- [ ] **Check approximate titles:** several Grab, foodpanda and data.gov.sg titles come from bylines without roles.
- [ ] **Check two name-only matches:** Chin Hwee Ong and Umesh Ramakrishnan are placed at medium from Meetup RSVPs that match on name only.
- [ ] **Check one LinkedIn match:** Feng Cheng's result shows the name surname first, "Cheng Feng - Grab".
- [ ] **Check Michael Han's title:** the 2026-09 meetup lists "General Manager", and GovTech lists "Head of APAC, Infinite Lambda".
- [ ] **Balance dbt Labs staff:** Mark Wan and Sin Ta Poon work there and are labelled. Both can speak, but check the line-up has practitioners first. Mark Wan's location is unknown, and LinkedIn found no matching profile, so check whether Mark Wan is still at dbt Labs.
- [ ] **Skip the backup:** the backup speaker is a Vinted colleague based in Berlin.
- [ ] **Check speakers based elsewhere:** Nas Radev and Hamzah Chaudhary are in London, Thanh Dinh Khac in Ho Chi Minh City, and Josh Beemster in Sydney.

## 6. Next run

- **Sources to try first:**
  - **The chapter and STACK:** new GovTech STACK [Data] meetups, and new Singapore dbt Meetup and Snowflake User Group Singapore events through Meetup `gql2`.
  - **Conference agendas:** the Coalesce and dbt Summit speaker lists, and the Snowflake and Databricks World Tour Singapore agendas, were not covered.
  - **Job ads:** read the remaining 6 freehire.me pages, keeping ads that contain the whole word "dbt". Add the Lever, Greenhouse and Ashby `site:` searches.
  - **Women-in-data:** ask PyLadies Singapore and Women Devs SG for speakers on data topics. Read new Women Devs SG and R-Ladies Singapore events.
- **Women-in-data communities not yet reachable:**
  - **Women Devs SG speakers:** the 2024 Web3 analytics and Dataiku events name no speakers. Ask the hosts.
  - **Women Techmakers Singapore:** the GDG event pages name no speakers or ambassadors. Ask GDG Singapore.
  - **Girls in Tech Singapore and She Loves Data:** no Singapore event page was found.
  - **WiDS Singapore since 2024:** no event is listed on the WiDS site.
- **People from the women-in-data pass:** the 7 people added have no LinkedIn search. Saloni is known only by a Meetup first name.
- **People to locate:**
  - **Past speakers:** 14 people are still unknown, mostly past chapter speakers from 2023 and 2024. LinkedIn found no profile with a matching title for Aezo Teo, Houren Chen, Shuguang Xiang, Adam Bagaskarta and Jia Ler Chew. Try the Grab or ShopBack author pages.
  - **Auxten Wang:** gave 2 in-person Singapore talks in 2026. Confirm whether ClickHouse has a Singapore office.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `singapore/singapore_dbt_companies.json`, the Singapore dbt Meetup, `../enriched/singapore-dbt-meetup.json` and Singapore. Add: "Tag recruiters as type "recruiter". Ask whether each data speaker uses dbt before raising that speaker to tier 1."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. GovTech STACK, Snowflake User Group, DataScience SG, PyCon and PyLadies Singapore events, freehire.me and TheirStack job ads, Grab, Medium, Holistics and Infinite Lambda blogs, and DEV authors, plus chapter history. 82 people at 57 companies, 28 of them past chapter speakers. 21 dbt job ads. |
| 2026-10-01 | 1 | Location pass from public pages: Meetup hosts and RSVPs, and recent in-person chapter talks. 11 people placed, 8 in Singapore and 3 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 6 people placed, 5 in Singapore and 1 in Sydney. With the location pass, 17 people placed and 14 still unknown. |
| 2026-10-01 | 2 | Women-in-data pass. Checked Women Devs SG, R-Ladies Singapore, Singapore WiMLDS, Women Techmakers through GDG Singapore, WiDS Singapore, She Loves Data and Girls in Tech Singapore. Added 7 people with `sourced_via: women_in_data_community`: 1 speaker (AnLei Huang, Databricks, from WiDS Taipei 2026) and 6 connectors. Added 4 community channels. |
| 2026-10-01 | 3 | Company pass from job ads: the MyCareersFuture API, the freehire.me API and Greenhouse, Lever and Ashby boards. 76 companies and 190 job ads added. OCBC, Razer, PathSource, BAH Partners and Sciente raised to strong. Airwallex and Temasek raised to medium. almapay, Momcozy and Paradex now confirmed in Singapore. |
