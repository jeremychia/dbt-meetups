# Kuala Lumpur: city notes

This file holds what is specific to Kuala Lumpur and Malaysia. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** none yet. The goal is speakers and co-organisers for a first Kuala Lumpur dbt Meetup. Data in `kuala_lumpur_dbt_companies.json`, which the organiser page reads under the chapter key `kuala_lumpur`, goal `speakers`.
- **Region:** Malaysia, with Kuala Lumpur and the Klang Valley first. People in Penang and Putrajaya count as in the region.
- **First built:** 2026-09-23

<!-- at-a-glance:start -->
**At a glance** (version 8, 2026-10-05)

| | Count |
|---|---|
| Companies | 102 |
| People | 55 |
| Tier 1 leads | 5 |
| First-time speakers (publish, no talk yet) | 8 |
| Proven speakers | 32 |
| Spoke at this chapter before | 0 |
| Based in the region | 42 |
| Based elsewhere | 5 |
| Location unknown | 8 |
| With a LinkedIn profile | 47 |
| Job ads mentioning dbt | 92 |
| Past chapter meetups | 0 |
<!-- at-a-glance:end -->

## 1. Where to look in Kuala Lumpur

Almost nobody in Malaysia publishes about dbt. So the search starts from public talks at other Kuala Lumpur data meetups, and uses job ads to find the companies that run dbt. The best speaker leads are data leads at dbt companies who already speak publicly about something else.

### Meetups and communities

- **Data Council KL (DCKL) on Luma:** the best source, and the main Kuala Lumpur data community. Its event pages ([dckl8](https://lu.ma/dckl8), [t5fcsqb6](https://luma.com/t5fcsqb6), [ykeg7loq](https://lu.ma/ykeg7loq), [aufuyvtq](https://lu.ma/aufuyvtq), [m3nydr6r](https://luma.com/m3nydr6r)) give each speaker's name, role, company and host venue, plus committee names. Open [luma.com/dckl](https://luma.com/dckl) in the browser, then fetch event pages from inside the tab. DCKL's last event was in June 2025.
- **[Snowflake User Group KL](https://usergroups.snowflake.com/kuala-lumpur/):** named speakers with titles. It led to MoneyLion and CelcomDigi. Its last event was in April 2025.
- **Snowflake World Tour and Data for Breakfast KL:** the agenda pages don't name customer speakers. LinkedIn post snippets about the events were the only way to name them.
- **Other communities:** PyData KL, PyCon MY, AWS User Groups MY, GDG KL and DevFest KL, Microsoft Fabric Community MY and KL Data Science were checked. The organisers of PyData KL, the AWS user groups and the Microsoft Fabric community are recorded as connectors.

### Job ads

- **LinkedIn Jobs:** [a dbt search with `location=Malaysia`](https://www.linkedin.com/jobs/search?keywords=dbt&location=Malaysia), scanned with the in-page script from `../baltics/SEARCH_METHOD.md` Appendix A. It returned 627 unique listings, and pages stop after `start=630`. Only the 488 data-titled ads were opened. 27 ads at 24 employers contained the whole word "dbt", and most hits came in the first ~250 results. Two parallel workers at 1.5 s spacing hit 94 HTTP 429 errors, all recovered by the back-off.
- **[freehire.me](https://freehire.me/jobs?countries=my&skills=dbt):** about 65 Malaysian jobs tagged dbt in four fetches, often with full ad text. It mirrors Workday, Ashby and Zoho ads that don't render when fetched.
- **[Indeed Malaysia](https://malaysia.indeed.com/q-dbt-jobs.html):** readable with a plain fetch, including `?start=10`. It found Wilhelmsen, Coforge, Rapsodo, Rotate and a recruiter ad that LinkedIn missed.
- **[freehire.me API](https://freehire.me/api/v1/jobs/search?skills=dbt&countries=MY):** the JSON API behind freehire.me answers a plain fetch. One call returns all 52 Malaysian ads tagged dbt. The search results cut each ad at about 1,000 characters, so read `/api/v1/jobs/<slug>` for the full text. It added Faculty Digital, MetaComp and Focal Consulting, and new ads for GXBank, onsemi and ams OSRAM.

### People

- **Data leads at dbt employers:** named data leads at the strong-dbt employers, such as Ryt Bank, GXBank, foodpanda, Funding Societies, Deriv, Intrepid Asia, Star Media, TIME dotCom and Synogize.
- **Personal blogs and GitHub:** found the only Kuala Lumpur dbt talk (Lee Boon Keong, DCKL 2020) and an open-source dbt platform (Syakeer Rahman).
- **Company blogs:** the only substantial dbt posts are ShopBack's 2021 series and Wei Jian's 2022 posts.

### Locations

- **`my.linkedin.com/in/...` profiles:** the Malaysian subdomain is a useful stand-in for "based in Malaysia" when no city is shown.
- **Third-party profile sites and GitHub:** Apollo, Datanyze and GitHub gave location and job history where LinkedIn had no match. They placed Wei Jian in Penang, still at ShopBack, and Syakeer Rahman in Putrajaya.
- **In-person talks:** a talk at a Snowflake community meetup in Kuala Lumpur placed Chang Boon Heng.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[PyLadies Kuala Lumpur](https://kl.pyladies.com):** launched in 2025, with a committee of 8. It co-ran the [PyLadies x PyData KL meetup](https://www.meetup.com/pydatakl/events/311302096/) on 30 October 2025. Hong Vin Koay of PyData KL hosted it. The meetup had two data talks: "The Danger of Missing Data" by Cheuk Ting Ho (JetBrains) and "Healthcare Data Analytics" by Kim-Ann Git. The about page gave 5 connectors: Daphne Choong (founder), Chong Siow Yen, Delyn Choong, Gamei Chin and Jenna Kassim (Software AG). The site reads with a plain fetch.
- **Women Techmakers Ambassadors Kuala Lumpur:** they run International Women's Day and October events with [GDG Kuala Lumpur](https://gdg.community.dev/gdg-kuala-lumpur/) every year. The GDG events API lists every event, and each event page names speakers with employer and title. [IWD 2024](https://gdg.community.dev/events/details/google-gdg-kuala-lumpur-presents-international-womens-day-iwd-kuala-lumpur-2024/) gave two speakers. Surabhi Pandey (Mindvalley) spoke on trust in data with Google Cloud. Christine Tee (Turing Enterprises) spoke on Gemini with BigQuery. IWD 2023, IWD 2025, Code Pink 2024 and Redefine Resilience 2025 had only AI and career talks. The event pages don't name the ambassadors.
- **[R-Ladies Kuala Lumpur](https://www.meetup.com/rladies-kuala-lumpur/):** 69 members since 2020. It has never held an event.
- **No local activity found:** Meetup's group search found no other women-in-data group near Kuala Lumpur. [WiDS](https://www.widsworldwide.org/) and [She Loves Data](https://www.shelovesdata.com/) list no Kuala Lumpur event. The [Girls in Tech Malaysia](https://girlsintech.org/malaysia/) site timed out. The Women in Tech Malaysia domain did not resolve.
- **Also ask:** data leads at dbt companies to suggest people on their teams.

## 2. What didn't work here

- **Company blogs:** two batches were checked, and little dbt writing was found. Most Malaysian companies have no public data blog. Grab has no dbt content. Deriv's blog now redirects to an AI Substack.
  - **Large Malaysian and regional companies:** Grab (PJ), AirAsia and Capital A, the incumbent banks, GXBank, Boost, AEON Bank, TNG Digital, Petronas and Setel, the telcos (CelcomDigi, Maxis, TM, Axiata), Carsome, Deriv, Shopee, Lazada and foodpanda MY, Agoda KL, PropertyGuru, MR DIY, Genting and the conglomerates.
  - **Startups, vendors and consultancies:** StoreHub, Fave, iPrice, Funding Societies, MoneyLion, ShopBack, Xendit, Employment Hero, SEEK and Jobstreet, Experian, Wise, Snowflake, Databricks, Fivetran and dbt Labs, Synogize, G-AsiaPacific and the global dbt partners.
- **PyCon MY:** the pretalx pages ([cfp.pycon.my/pyconmy-2025](https://cfp.pycon.my/pyconmy-2025/), [pycon.my](https://pycon.my)) load by JavaScript. The browser was refused and plain fetches were empty. The slug is `pyconmy-2025`, not `pycon-my-2025`.
- **JobStreet:** [my.jobstreet.com/dbt-jobs](https://my.jobstreet.com/dbt-jobs) is JavaScript-only.
- **getdbt.com case studies and partner directory:** JavaScript-only, with no Malaysian partner list.
- **Generic searches:** queries such as "dbt Kuala Lumpur speaker" and "analytics engineer Malaysia dbt" return global results. The search tool mostly ignores the location words.
- **Private meetup.com groups:** DCKL and KL Data Science hide their speakers. Use Luma instead.
- **dbt Community Forum, Coalesce speakers and "dbt certified" searches:** no Malaysians found.
- **Singapore dbt Meetup speakers:** `../enriched/singapore-dbt-meetup.json` was checked, and none is based in Kuala Lumpur.
- **Search snippets that swap employers:** a snippet credited GXBank's "dbt within Snowflake" ad to AirAsia. Always open the ad.
- **Snippet summaries:** they go stale, but result titles don't. Lee Boon Keong's summary still said MoneyLion, while the title said Lance Data.
- **Hacker News Who is hiring:** no Malaysian role mentions dbt.
- **GitHub code search:** no public `dbt_project.yml` in the Carsome or Deriv organisations.
- **freehire.me ads tagged Malaysia that are elsewhere:** some ads are for Singapore, Karachi or Dubai, and one Danish ad is placed in Kelantan. They were left out.

## 3. Companies looked at

- **No Kuala Lumpur dbt meetup or Coalesce watch party has ever run.** The only dbt talk found was at Data Council KL in May 2020. Both general data communities, DCKL and the Snowflake User Group KL, have gone quiet. There is room for a new meetup, and both are natural co-hosts.
- **Best venues and hosts:** MoneyLion (TRX), Xendit (KL Sentral), SEEK (Cap Square), Setel (Bangsar South) and AWS (Mid Valley). All have hosted DCKL or the Snowflake user group.
- **Clearest dbt use:** Ryt Bank, GXBank, foodpanda KL, Funding Societies, Intrepid Asia, Star Media, TIME dotCom, Wilhelmsen, ROCKWOOL, Nitka (Johor) and onsemi. The most common topics are data warehouses and platforms, GenAI and LLMs, and data governance. Topics tagged with dbt itself are rare, which confirms the gap.
- **Many large firms are on the watchlist.** 55 of the 94 companies are watchlisted, mostly large Malaysian firms checked without finding dbt. They are kept so they are not researched again. Grab, Shopee, Lazada and Xendit have their data teams mostly in Singapore, Indonesia or China.

<!-- companies:start -->
100 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (19)</summary>

ams OSRAM (Kulim), Askheadhunter / Timesconsult (recruiter, unnamed telco client), BonusLink, Fivetran / dbt Labs (merged 2026) (local presence not confirmed), foodpanda Malaysia (Delivery Hero), KL analytics hub, Funding Societies | Modalku (Malaysia), GXBank, Ikano Retail (IKEA franchisee), Intrepid Asia, Nitka Technologies, onsemi (Malaysia), ROCKWOOL (Malaysia), Ryt Bank (YTL Digital Bank), ShopBack (local presence not confirmed), Star Media Group Berhad, TIME dotCom Berhad, Vinted (local presence not confirmed), Wilhelmsen (KL GBS Data & Analytics), Xendit (Malaysia office, KL Sentral)

</details>

<details><summary><b>Some dbt signal</b> (25)</summary>

Agoda (KL office), AirAsia / Capital A / airasia MOVE / Teleport / BigPay, Airwallex (local presence not confirmed), Alphv Recruit, Bank Islam Malaysia, CloudMile, Coforge, Decube (local presence not confirmed), Deriv, DFI Retail Group (PJ), Employment Hero (local presence not confirmed), Endava (KL), Faculty Digital, Focal Consulting, G-AsiaPacific, MetaComp, MoneyLion (Gen Digital), KL tech hub, Oxydata Software Sdn Bhd, Pan Asia Group, Prudential Services Asia, Rapsodo (KL), Sime Darby Industrial, Snowflake Malaysia / Snowflake User Group KL, SolveIT Consultant, Synogize (KL office)

</details>

<details><summary><b>dbt as a nice-to-have</b> (7)</summary>

Concentrix (KL), K3 Advisory Group (incl. Quantuma), ONL Biz Solutions, Reap (KL), Rotate (KL), Standard Chartered (KL), WPP Media (KL)

</details>

<details><summary><b>Not verified</b> (35)</summary>

Ant International (KL), Astro, Media Prima, Sunway, Sime Darby, 99 Speedmart, Hap Seng, Atome (Advance Intelligence Group) (local presence not confirmed), Axiata / ADA, Maxis, U Mobile, Telekom Malaysia, Boost / Boost Bank, AEON Bank, Carsome, CelcomDigi, Consultancies checked, no Malaysian dbt evidence (Thoughtworks MY, Aimpoint Digital, Infinite Lambda, Tiger Analytics, Artefact, phData, Tasman, Fusionex, Mesiniaga, Revolution Analytics, Datamics, NCS, Bizfinity) (local presence not confirmed), Data Council Kuala Lumpur (DCKL), Fasset (KL), Fave, Fuku, iPrice Group, KAF Digital Bank, Lalamove (local presence not confirmed), Lance Data, Maybank, CIMB, RHB, Public Bank, Hong Leong, AmBank, Bank Negara Malaysia, Mindvalley, MNC service centres checked (HSBC KL, Shell Business Operations, Dyson MY, Accenture MY, Deloitte MY), OCBC Malaysia, One Credit, Other Malaysian startups checked (EasyStore, Kakitangan/Deel, Bukku, Aspirasi, Hiredly, GoGet, Supahands, RinggitPlus, Loanstreet, Carro/myTukar, Pos Malaysia, Aerodyne, Tapway, Kaodim, Speedhome, Fashion Valet), Petronas / Petronas Digital, RBC Shared Services Malaysia, Roche (KL), S P Setia, SD Guthrie, Setel (Petronas), Shopee MY, Lazada MY, Ninja Van MY, J&T (local presence not confirmed), Software AG (local presence not confirmed), StarHub (PJ), StoreHub (incl. Beep), Touch 'n Go / TNG Digital, Turing Enterprises Inc. (local presence not confirmed), Wise (KL office)

</details>

<details><summary><b>Uses a different stack</b> (14)</summary>

AWS Malaysia, AWS User Groups Malaysia, BentoML (local presence not confirmed), Databricks Malaysia, Employer not identified (local presence not confirmed), Experian Malaysia, Genting Malaysia, Grab (PJ/KL tech centre) (local presence not confirmed), JetBrains (local presence not confirmed), Microsoft Fabric Community Malaysia, MR DIY International, PropertyGuru / iProperty (local presence not confirmed), PyLadies Kuala Lumpur, SEEK / Jobstreet (KL tech hub)

</details>

<details><summary><b>Blogs and sites scanned</b> (8)</summary>

- https://deriv.com/derivtech/feed/data-engineering-at-deriv-building-robust-infrastructure
- https://engineering.grab.com/feed.xml
- https://medium.com/feed/agoda-engineering
- https://medium.com/feed/fsmk-engineering
- https://medium.com/feed/propertyguru-engineering
- https://medium.com/feed/shopback-tech-blog/tagged/dbt
- https://medium.com/feed/xendit-engineering
- https://www.aimpointdigital.com/partners/dbt-labs

</details>

<details><summary><b>Other sources checked</b> (29)</summary>

- [Meetup gql2 groupSearch near Kuala Lumpur](https://www.meetup.com/gql2)
- [R-Ladies Kuala Lumpur (Meetup gql2)](https://www.meetup.com/rladies-kuala-lumpur/) (nothing useful)
- [PyData KL past events (Meetup gql2)](https://www.meetup.com/pydatakl/)
- [PyLadies Kuala Lumpur site](https://kl.pyladies.com)
- [GDG Kuala Lumpur events API](https://gdg.community.dev/api/event_slim/for_chapter/486/?status=Completed&page_size=100)
- [Women Techmakers IWD Kuala Lumpur 2024](https://gdg.community.dev/events/details/google-gdg-kuala-lumpur-presents-international-womens-day-iwd-kuala-lumpur-2024/)
- [Women Techmakers IWD Kuala Lumpur 2023](https://gdg.community.dev/events/details/google-gdg-kuala-lumpur-presents-international-womens-day-iwd-kuala-lumpur-2023/) (nothing useful)
- [Women Techmakers IWD 2025: Redefine Possible](https://gdg.community.dev/events/details/google-gdg-kuala-lumpur-presents-international-womens-day-iwd-2025-redefine-possible/) (nothing useful)
- [Women Techmakers Code Pink 2024](https://gdg.community.dev/events/details/google-gdg-kuala-lumpur-presents-code-pink-breast-cancer-awareness-month/) (nothing useful)
- [Women Techmakers Redefine Resilience 2025](https://gdg.community.dev/events/details/google-gdg-kuala-lumpur-presents-redefine-resilience/) (nothing useful)
- [Girls in Tech Malaysia](https://girlsintech.org/malaysia/) (nothing useful)
- [She Loves Data](https://www.shelovesdata.com/) (nothing useful)
- [WiDS Worldwide site search](https://www.widsworldwide.org/wp-json/wp/v2/search?search=Malaysia) (nothing useful)
- [Women in Tech Malaysia](https://womenintechmalaysia.com/) (nothing useful)
- [Luma Kuala Lumpur discover](https://api.lu.ma/discover/get-paginated-events?discover_place_api_id=discplace-O15L1VZiYe0GYGm) (nothing useful)
- [freehire.me API, Malaysia, skill dbt](https://freehire.me/api/v1/jobs/search?skills=dbt&countries=MY)
- [Hacker News Who is hiring (Algolia)](https://hn.algolia.com/api/v1/search?query=dbt%20malaysia&tags=comment) (nothing useful)
- [getdbt.com case studies (llms-full-case-studies.txt)](https://www.getdbt.com/llms-full-case-studies.txt) (nothing useful)
- [Data Council Talks #10 (Luma)](https://lu.ma/ykeg7loq)
- [Data Council Talks #11 (Luma)](https://luma.com/aufuyvtq)
- [Data Council KL calendar (Luma)](https://luma.com/dckl) (nothing useful)
- [PyLadies x PyData KL meetup, 30 Oct 2025](https://www.meetup.com/pydatakl/events/311302096/) (nothing useful)
- [PyData KL past events (Meetup)](https://www.meetup.com/pydatakl/events/?type=past) (nothing useful)
- [Snowflake User Group KL](https://usergroups.snowflake.com/kuala-lumpur) (nothing useful)
- [DevFest 2025 KL (GDG KL x GDG Cloud KL)](https://gdg.community.dev/events/details/google-gdg-kuala-lumpur-presents-devfest-2025-kl-gdg-kl-x-gdg-cloud-kl/cohost-gdg-cloud-kl/) (nothing useful)
- [Chief Digital & Data Officer Malaysia Summit 2026](https://www.cdotrends.com/event/chief-digital-officer-asia-summit/2026/kuala-lumpur/) (nothing useful)
- [Databricks Data + AI World Tour Malaysia 2023](https://www.imoney.my/articles/dataai-world-tour-malaysia) (nothing useful)
- [Snowflake World Tour Kuala Lumpur 2026](https://www.snowflake.com/en/world-tour/kuala-lumpur/?lang=ko) (nothing useful)
- [d-Conference 2026 agenda](https://d-conference.com.my/2026-agenda/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **Tier 1 here:** a person in Malaysia who spoke publicly in 2025–26 and leads a team whose ads require dbt, or who has given a dbt talk.
- **First-time speakers:**
  - **Syakeer Rahman**, independent, Putrajaya: [an open-source data platform with Airflow, dbt, Trino and Ollama](https://github.com/SyakeerRahman/Data_Engineering_Open_Source_Data_Platform_Airflow_dbt_Trino_Ollama_AI) (2026).
  - **Zi Qin Yeow**, Grab, Malaysia: co-wrote [Data Mesh at Grab (Part III): operationalizing data reliability](https://engineering.grab.com/data-mesh-at-grab-part-three) (August 2026).
  - **Katie Huang Xiemin**, independent (DataLemur): [learning dbt, Snowflake and Dagster](https://www.linkedin.com/posts/katiehuangx_dataengineering-activity-7064127275838947328-Bs3Q) (May 2023).
  - **Azwan Zuharimi**, SEEK and Jobstreet, Kuala Lumpur: [a post on DuckDB, SQL and data warehousing](https://www.linkedin.com/posts/azwan-zuharimi_duckdb-python-sql-activity-7114625829048918016-wFv2) (October 2023).
- **Anchor speakers:**
  - **Lee Boon Keong**, Lance Data: gave the [2020 dbt talk at DCKL](http://1bk.dev/blog/2020/05/22/data-council-dbt-presentation), still builds dbt projects, and sits on the DCKL committee. This is the first person to approach, as speaker and co-organiser.
  - **Au Yong Min Hao**, Head of Data, Ryt Bank: Ryt Bank's ads require dbt and Snowflake. Au Yong Min Hao writes about hiring analytics engineers, and spoke on a [DCKL fireside chat](https://luma.com/m3nydr6r) (June 2025).
  - **Bee Teng Lim**, GXBank: presented GXBank's [BI Bytes story](https://www.linkedin.com/posts/changboon_snowflakeworldtour-dataengineering-ai-activity-7502542545151864832-zGWJ) at Snowflake World Tour KL 2026. GXBank's ads require dbt on Snowflake.
  - **Wilbert Chong**, **Dafuallah Esameldien** and **Goh Pei Xuan**, MoneyLion: experienced speakers. Ask whether MoneyLion uses dbt or SQLMesh.
- **Connectors:** used a lot here. They cover community organisers (DCKL, PyData KL, AWS user groups, Microsoft Fabric), vendor staff (Snowflake, AWS) and senior sponsors. They are the route to venues and co-hosts.
  - **Chang Boon Heng**, Snowflake Malaysia: spoke at the [Snowflake community meetup](https://usergroups.snowflake.com/events/details/snowflake-kuala-lumpur-presents-snowflake-community-meetup-kuala-lumpur-24th-april-2025/) in April 2025.
  - **Caroline Chong**, Head of Data, GXBank: a senior sponsor.
- **The ex-MoneyLion network** runs through Kuala Lumpur data. Au Yong Min Hao, Lee Boon Keong, Shawn Loh and Yudhiesh Ravindranath all came from MoneyLion.

## 5. Before outreach

- [ ] **Check the tier-1 people raised by the rule.** Syakeer Rahman and Zi Qin Yeow are emerging voices raised to tier 1, not proven speakers.
- [ ] **Check stale roles and moves.** Yudhiesh Ravindranath moved from MoneyLion to One Credit. Au Yong Min Hao moved from MoneyLion to Ryt Bank. Piyush Palkar's Carsome Chief Data Officer role dates from 2023.
- [ ] **Ask which tool runs in production.** MoneyLion's ads say "dbt or SQLMesh" and Deriv's say "dbt or Dataform".
- [ ] **Check same-name people.** There is another Goh Pei Xuan at Apave Singapore. Wei Jian is a very common name. Laxman Damodar has two profiles.
- [ ] **Treat Singapore-based people as visitors.** Yun Fei Choo, Harvey Li and Feng Cheng (Grab) are in Singapore.

## 6. Next run

- **Sources to try first:**
  - **PyCon MY 2024 and 2025 schedules:** open them in a browser.
  - **dbt Slack:** check `#local-malaysia` and `#local-kuala-lumpur` by hand.
  - **Community events:** new events of Data Council KL, Snowflake User Group KL, Snowflake World Tour and Data for Breakfast KL, PyData KL, PyCon MY, AWS Community Day MY and GDG KL, and any new Kuala Lumpur dbt meetup events.
  - **Job ads:** LinkedIn Jobs with `location=Malaysia`, freehire.me and Indeed Malaysia. Exclude therapy "DBT" ads.
  - **Named data leads:** foodpanda KL, Funding Societies MY, Deriv, Intrepid Asia (a Head of Data role is open) and Star Media.
  - **After the first meetup:** add the group to `../pipeline/dbt-meetup-groups.json` and run `../pipeline/run_pipeline.sh`. Then fill `past_meetups` and `past_chapter_talks` from `../enriched/<kl-group>.json`.
- **Women-in-data communities not yet reachable:**
  - **MMU TechGirls:** no public event page was found.
  - **Girls in Tech Malaysia:** the site timed out. Try it in a browser.
  - **Women in Tech Malaysia and WiDS Kuala Lumpur:** no site or chapter event was found.
  - **Women Techmakers Ambassadors KL:** ask GDG KL for the ambassadors' names, and for the speaker of "Data Science in Healthcare" at Code Pink 2024.
  - **PyLadies KL on Instagram, Facebook and Peatix:** not read. Check them for events after PyCon MY 2025.
- **People from the women-in-data pass:** the 9 people added have no LinkedIn search and no known location.
- **People to locate:** 3 people have no known location: Ng Ser Jie (MoneyLion), Michael Rorig (Ikano Retail) and David Lexa (Xendit).
- **LinkedIn profiles still missing:** Wei Jian, Syakeer Rahman, Ng Ser Jie and Michael Rorig. Try other name spellings, or ask Lee Boon Keong or DCKL for introductions.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `kuala_lumpur/kuala_lumpur_dbt_companies.json`, no chapter or enriched file yet, and the region above. Add: "There is no chapter yet, so look for co-organisers as well as speakers. Read Data Council KL event pages on Luma from inside a browser tab. Scan LinkedIn Jobs with location=Malaysia, plus freehire.me and Indeed Malaysia."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-23 | 1 | First search. 89 companies (51 on the watchlist), 44 people, 50 job postings at 36 companies, 43 unique content items. 3 tier-1 leads (Lee Boon Keong, Au Yong Min Hao, Bee Teng Lim), 14 tier-2, 12 connectors. LinkedIn URLs for 26 people; 16 not searched after the session hit the 200-web-search cap. Chapter `kuala_lumpur` added to `dashboard/build_organiser_data.py`. |
| 2026-09-23 | 2 | Moved to shared schema v2 (`lead_type`): 26 proven speakers, 8 emerging voices, 1 featured, 9 with no public content; tier 1 now 6. LinkedIn pass in a new session: 18 people searched, 14 URLs found (38 of 44 people now have one). Location fixes: Yun Fei Choo and Harvey Li are Singapore-based; Zi Qin Yeow is Malaysia-based; Wei Jian is in Penang; Syakeer Rahman is in Putrajaya. Backup of v1 at `kuala_lumpur_dbt_companies.v1.json`. |
| 2026-09-23 | 3 | Added a `HIGHLIGHT` prefix in `notes` for some people (removed in version 6). No schema change. Organiser page rebuilt with the Kuala Lumpur chapter. |
| 2026-09-23 | 4 | Shared schema v3 adds `pronouns` (self-stated only, never inferred; none recorded yet) and `sourced_via`, which is derived from evidence (e.g. `women_in_data_community` for the PyLadies x PyData KL speaker). The field list is in `../berlin_planning/SEARCH_METHOD.md` §3. For women-in-data sourcing and the line-up balance check, see that file's Step 2b and §1 Step 6. Backup: `kuala_lumpur_dbt_companies.v3.json`. |
| 2026-10-01 | 5 | Location pass and LinkedIn pass, by the evidence rules in `../research/README.md`. An in-person talk at a Snowflake community meetup in Kuala Lumpur placed Chang Boon Heng. LinkedIn search results placed Izzudin Hafiz in Kuala Lumpur and Feng Cheng in Singapore. 3 people are still unknown. |
| 2026-10-01 | 6 | Women-in-data pass. Removed the `HIGHLIGHT` notes. Checked PyLadies KL, Women Techmakers Ambassadors KL (through GDG KL), R-Ladies KL, WiDS, She Loves Data, Girls in Tech Malaysia and Women in Tech Malaysia. Added 9 people with `sourced_via: women_in_data_community`: 4 speakers (Cheuk Ting Ho, Kim-Ann Git, Surabhi Pandey, Christine Tee) and 5 PyLadies KL organisers as connectors. Added community channels for Women Techmakers KL and R-Ladies KL. |
| 2026-10-01 | 7 | Company pass from job ads: the freehire.me API. 7 companies and 42 job ads added. BonusLink, Ikano Retail and ams OSRAM raised to strong. AirAsia raised to medium. The file has no chapter, so `enriched_file` is null. |
| 2026-10-05 | 8 | 2 more people, both tier 3 (an MLOps talk and a Singapore-based speaker). Search ignores location words, so most results were global. |
