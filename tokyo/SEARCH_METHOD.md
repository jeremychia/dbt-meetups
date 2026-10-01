# Tokyo: city notes

This file holds what is specific to Tokyo. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Tokyo dbt Meetup](https://www.meetup.com/tokyo-dbt-meetup/), data in `tokyo_dbt_companies.json`
- **Region:** Greater Tokyo. That includes Saitama and Chiba, so a GitHub location of Kawagoe or Saitama counts. Kyoto, Okinawa and Fukushima do not.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 73 |
| People | 126 |
| Tier 1 leads | 103 |
| First-time speakers (publish, no talk yet) | 80 |
| Proven speakers | 44 |
| Spoke at this chapter before | 40 |
| Based in the region | 97 |
| Based elsewhere | 5 |
| Location unknown | 24 |
| With a LinkedIn profile | 4 |
| Job ads mentioning dbt | 0 |
| Past chapter meetups | 19 |
<!-- at-a-glance:end -->

## 1. Where to look in Tokyo

Most of the content is in Japanese. Titles are kept as written, with an English description.

### Writing platforms

- **Zenn API:** the best single source, and most people in the file come from here. [`zenn.dev/api/articles?topicname=dbt&order=latest&page=N`](https://zenn.dev/api/articles?topicname=dbt&order=latest) lists each dbt article with its author and company publication, one call per page. About 800 of the newest and most-liked articles were read. Authors who wrote in a company publication from 2024 onwards were kept, from about 110 articles since 2024-06. Zenn bios gave titles and self-stated roles, such as Snowflake Data Superhero.
- **Qiita API:** [`qiita.com/api/v2/items?query=tag:dbt`](https://qiita.com/api/v2/items?query=tag:dbt) works without a token and names the author's organisation. Posts since 2024-06 were read. It added CyberAgent, NTT DATA, ZOZO and DeNA authors.

### Company tech blogs

- **Hatena blog search:** Hatena-based company blogs answer `/search?q=dbt` with plain HTML, so no web searches were needed.
- **[Timee](https://tech.timee.co.jp/):** data reliability team posts on dbt snapshots, unit tests and DuckDB checks.
- **[LayerX](https://tech.layerx.co.jp/):** two open-source dbt packages for Snowflake governance.
- **[ZOZO](https://techblog.zozo.com/):** dbt adoption on Cloud Composer.
- **Money Forward on Zenn:** one dbt post on its Zenn publication.

### Conferences and the chapter

- **Chapter history:** every named speaker from `../enriched/tokyo-dbt-meetup.json` was added, with the talk as evidence. That covers 19 events, from meetup #4 (2022-08-23) to meetup #21 (2026-07-29). The two hosts of meetup #21 are recorded as organisers. The writer of the chapter's [meetup reports on Zenn](https://zenn.dev/p/dbttokyo) is recorded as a connector.
- **getdbt.com roadshow pages:** speaker names and companies sit as JSON in the raw HTML.
- **[dbt World Tour Tokyo 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-tokyo)** (2026-10-20): Sony Bank and Mynavi have customer sessions, but the speakers are not named. Both are recorded as companies with no people.
- **[Coalesce on the Road Tokyo 2025](https://www.getdbt.com/jp/coalesce-in-tokyo):** mostly dbt Labs speakers. Customer speakers are not named.

### Locations

- **GitHub profiles:** a GitHub profile linked from a Zenn profile gives a stated city, at high confidence. Zenn and Qiita location fields were empty for every handle checked.
- **Recent chapter talks:** an in-person talk at a Tokyo dbt Meetup since 2025, at an employer with a Tokyo office, gave medium confidence. Venues come from `past_meetups`.
- **Company contact pages:** the [estie](https://www.estie.co.jp/company) and [Mitsumore](https://meetsmore.com/company) pages confirmed both Tokyo offices.
- **LinkedIn search results:** placed 2 people in Greater Tokyo and 2 elsewhere (Naha and Seattle).
- **Yield:** 22 people placed across both passes, and 24 still unknown. The evidence rules are in [location rules](../research/README.md#6-location-rules).

## 2. What didn't work here

- **[Zenn topic page](https://zenn.dev/topics/dbt):** renders nothing when fetched. Use the API instead.
- **[connpass](https://connpass.com/search/?q=dbt):** returns HTTP 403 to plain fetches, so the Data Engineering Study line-ups and most Tokyo meetup line-ups were not read.
- **[TECH PLAY](https://techplay.jp/event/924859):** returns HTTP 403, so the PyLadies Tokyo event was not read.
- **[Mercari engineering blog](https://engineering.mercari.com/blog/):** the search page did not render.
- **[SmartHR](https://tech.smarthr.jp/) and [Money Forward](https://moneyforward-dev.jp/) blogs:** no dbt posts.
- **Japanese company sites:** most load by JavaScript, so no office address came back.
- **Web search:** ran out after about 12 calls. No job ads were collected, and the Mercari, SmartHR and CyberAgent sweeps were only partly done.
- **Women-in-data events:** [Women Tech Terrace 2024](https://www.cyberagent.co.jp/way/list/detail/id=30486) (CyberAgent) had no data talks. [WiDS Tokyo @ IBM](https://www.widsworldwide.org/events/event/wids-tokyo-ibm-2/) was a 2024 event with no speakers listed. No candidate came from this step.

## 3. Companies looked at

- **Finatext dominates:** its Zenn publication has 8 people in the file. Plan for one speaker per company per event.
- **Chura Data is based in Okinawa:** its CTO is in Naha, but two of its writers have GitHub locations in Saitama.
- **Customer speakers at dbt Labs events:** Sony Bank and Mynavi speak at dbt World Tour Tokyo on 2026-10-20.

<!-- companies:start -->
72 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (51)</summary>

10X Inc. (local presence not confirmed), Anthropic Japan G.K. (local presence not confirmed), Chura Data (local presence not confirmed), commmune Inc. (local presence not confirmed), CyberAgent, DATUM STUDIO, dbt Labs (local presence not confirmed), dbt Tokyo Crew, DMM.com, estie Inc. (local presence not confirmed), Fez, Finatext Holdings (Finatext / Nowcast), GA technologies, GENDA, GMO Pepabo, hokan, istyle, IVRy, JINS, Knowledge Work, Kurashiru (dely), LayerX, Macbee Planet, MeDiCU, Mitsumore Inc. (local presence not confirmed), Mizuho Research & Technologies (local presence not confirmed), Money Forward, Mynavi, newmo Inc. (local presence not confirmed), Nowcast Inc. (local presence not confirmed), NTT DATA, PIVOT, pixiv, primeNumber, RAKSUL, RAKUDEJI (local presence not confirmed), Rehab for JAPAN, Sansan, SIGNATE Inc. (local presence not confirmed), Snowflake Data Heroes (Japan), Sony Bank, stable Inc. (local presence not confirmed), Stanby, Supership, Timee, truestar, Ubie, VALUES, Works Human Intelligence, ZOZO, Zucks Ad Products Division (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (20)</summary>

Antway, Bandai Namco Nexus, COTEN, Cybozu, DeNA, Headwaters, INTAGE, KDDI Agile Development Center, Loglass, MBK Digital, PKSHA Technology, Quick Network (local presence not confirmed), READYFOR, Rec Technology Consulting (local presence not confirmed), Saison Technology, SimpleForm (local presence not confirmed), TRIBEAU, USEN ICT Solutions, Yappli, youthful days (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

mybest

</details>

<details><summary><b>Blogs and sites scanned</b> (53)</summary>

- https://qiita.com/Himeka_Kawaguchi/items/8d2c28a8b41ce586f755
- https://qiita.com/ReQ_HY/items/e1043eb0cb6e9313c86f
- https://qiita.com/RyutoYoda/items/365b42d8d1b92e451d33
- https://qiita.com/Toyo_m/items/3bbbff1ba96e8cac2222
- https://qiita.com/ao_flower/items/3c69440b2c2916f01ba7
- https://qiita.com/imaik_/items/5c20b8a629f189c2a0f4
- https://qiita.com/kairi_sekiya/items/c987514ad741c4f23075
- https://qiita.com/n-gondo123/items/b33baeb75f5559aefbe2
- https://qiita.com/osshy/items/cd12cd5c32fae528da21
- https://qiita.com/y_ishiguro/items/a8cf45a37f9593a08c4e
- https://tech.layerx.co.jp/
- https://tech.timee.co.jp/
- https://techblog.zozo.com/
- https://techblog.zozo.com/entry/dbt-adoption
- https://zenn.dev/antway
- https://zenn.dev/coten
- https://zenn.dev/cybozu_data
- https://zenn.dev/dataheroes
- https://zenn.dev/dmmdata
- https://zenn.dev/fez_tech
- https://zenn.dev/gatechnologies
- https://zenn.dev/hokan_blog
- https://zenn.dev/intage_tech
- https://zenn.dev/ivry
- https://zenn.dev/jins
- https://zenn.dev/loglass
- https://zenn.dev/macbee_planet
- https://zenn.dev/mbk_digital
- https://zenn.dev/moneyforward
- https://zenn.dev/p/churadata
- https://zenn.dev/p/dataheroes
- https://zenn.dev/p/datum_studio
- https://zenn.dev/p/dbttokyo
- https://zenn.dev/p/dely_jp
- https://zenn.dev/p/finatext
- https://zenn.dev/p/genda_jp
- https://zenn.dev/p/headwaters
- https://zenn.dev/p/medicu
- https://zenn.dev/p/nttdata_tech
- https://zenn.dev/p/truestar
- https://zenn.dev/p/ubie_dev
- https://zenn.dev/pepabo
- https://zenn.dev/pivotmedia
- https://zenn.dev/pixiv
- https://zenn.dev/pksha
- https://zenn.dev/primenumber
- https://zenn.dev/qn_tech
- https://zenn.dev/raksul_data
- https://zenn.dev/readyfor_blog
- https://zenn.dev/rehabforjapan
- https://zenn.dev/tribeau
- https://zenn.dev/usen_ict
- https://zenn.dev/youthfuldays

</details>

<details><summary><b>Other sources checked</b> (14)</summary>

- [Zenn dbt topic (API)](https://zenn.dev/topics/dbt)
- [Qiita dbt tag (API)](https://qiita.com/tags/dbt)
- [Timee tech blog](https://tech.timee.co.jp/)
- [LayerX tech blog](https://tech.layerx.co.jp/)
- [ZOZO tech blog](https://techblog.zozo.com/)
- [SmartHR tech blog](https://tech.smarthr.jp/) (nothing useful)
- [Money Forward developers blog](https://moneyforward-dev.jp/) (nothing useful)
- [Mercari engineering blog](https://engineering.mercari.com/blog/) (nothing useful)
- [dbt World Tour Tokyo 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-tokyo)
- [Coalesce on the Road Tokyo 2025](https://www.getdbt.com/jp/coalesce-in-tokyo) (nothing useful)
- [connpass (Data Engineering Study, dbt events)](https://connpass.com/search/?q=dbt) (nothing useful)
- [Women Tech Terrace 2024 (CyberAgent)](https://www.cyberagent.co.jp/way/list/detail/id=30486) (nothing useful)
- [WiDS Tokyo @ IBM](https://www.widsworldwide.org/events/event/wids-tokyo-ibm-2/) (nothing useful)
- [PyLadies Tokyo](https://techplay.jp/event/924859) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Ryuichi Shimajiri (Finatext):** [automated dbt tag checks on Snowflake](https://zenn.dev/finatext/articles/snowflake-dbt-tag-validation) with dbt-elementary.
  - **rami (ramish8), Macbee Planet:** [rebuilt a platform on dbt and cut BigQuery scans by over 90%](https://zenn.dev/macbee_planet/articles/85c8ef4aeb063b).
  - **wxy_zzz (IVRy):** [marks certified data on Databricks with dbt tags](https://zenn.dev/ivry/articles/ivry-dbx-certification-status-with-dbt-20260901).
  - **Yuto (yuto_data_dev), DMM:** [event-driven data marts with dbt state](https://zenn.dev/dmmdata/articles/dbt-state-event-driven-data-marts).
  - **tadaken3 (Chura Data):** [co-wrote a Japanese dbt book](https://zenn.dev/churadata/articles/dbt-book-cover-design-2026). GitHub gives Saitama as the location.
- **Anchor speakers:**
  - **civitaspo (LayerX):** two sessions at Snowflake World Tour Tokyo 2026, and the [dbt-authorized-models](https://tech.layerx.co.jp/entry/dbt-authorized-models) package.
  - **けびん (kevinrobot34), Finatext:** Snowflake Data Superhero and the most prolific writer on the Finatext blog, for example [dbt incremental models at scale](https://zenn.dev/finatext/articles/dbt-high-performance-incremental-model).
  - **Hiroto Takahashi (Nowcast):** [spoke at meetup #19](https://www.meetup.com/tokyo-dbt-meetup/events/313179574/) on understanding dbt-core through query logs.
  - **Yuki Wada (Sansan):** [spoke at meetup #20](https://www.meetup.com/tokyo-dbt-meetup/events/315004575/) on rolling out dbt Core across the company.
- **Connectors:**
  - **Shinya Takimoto and Kazuya Araki:** the [chapter's organisers](https://www.meetup.com/tokyo-dbt-meetup/events/315495411/) (dbt Tokyo Crew).
  - **Yuta YAMAMOTO:** writes the [chapter's meetup reports](https://zenn.dev/dbttokyo/articles/b73a3256f38228).
  - **しんや (shinyaa31), truestar:** has written over 600 event reports, including [one on meetup #15](https://zenn.dev/truestar/articles/6c3ebfebc4831a).
  - **[Snowflake Data Heroes](https://zenn.dev/p/dataheroes):** the Japanese Snowflake community, with many dbt users. Ask the community for introductions to balance the line-up.

## 5. Before outreach

- [ ] **Check most "in region" calls:** only 17 of the people marked in the region have a location note with evidence. The rest were placed in Tokyo from the employer's Tokyo head office during research.
- [ ] **Check tier 1:** it holds 103 people, because any first-time speaker with a post from 2024 onwards is raised to tier 1. 14 of these people have no item that mentions dbt, for example bigmegaphone and chanyou. Sort by how recent and how deep the dbt work is.
- [ ] **Confirm real names:** most authors publish under a handle, and most new people are recorded by Zenn or Qiita handle. Names are recorded as written, with an ASCII id.
- [ ] **Add a handle to names in Japanese script only:** the assembler strips names to ASCII before matching, so two names in Japanese script merge silently. Write each as, for example, "山口歩夢 (gussan_a)".
- [ ] **Keep known aliases out:** these blog authors are past speakers under another name, so were left out to avoid duplicates. okiyuki is Motoyuki Oki, Yoshi-ken is Yoshiken, harry/gappy is Harry, sisisin is Shimenyan, t-hiroto is Hiroto Takahashi and ryosuke839 is Ryosuke Lin Yamamoto.
- [ ] **Confirm Yanagisawa:** ZOZO's 栁澤 (@i_125) is Satoko Yanagisawa on Qiita. The chapter file has "Yoshiko Yanagisawa". Confirm which name the past speaker has.
- [ ] **Check Toshitei Ito:** may be Toshitaka Ito, a dbt Labs solutions architect in Tokyo.
- [ ] **Merge duplicate companies:** several appear twice, once from research and once from the chapter history. Examples are Kurashiru (dely) and dely Inc., and Finatext Holdings (Finatext / Nowcast) and Nowcast Inc.
- [ ] **Fix placeholder employers:** one company record is named "Inc.". "Anthropic Japan G.K." holds Tristan Handy, which comes from the talk text.
- [ ] **Balance dbt Labs staff:** Mark Wan, Andrew Escay and Elias DeFaria work there and are labelled. Elias DeFaria is in Seattle. All three can speak, but check the line-up has practitioners first.
- [ ] **Check one weak location:** AZEGAMI Kazuya's Zenn bio suggests Sukagawa, Fukushima, but names no home city. The employer, youthful days, lists an office in Nagano. The location stays unknown.
- [ ] **Check people already booked:** Sony Bank and Mynavi speak at dbt World Tour Tokyo on 2026-10-20.

## 6. Next run

- **Sources to try first:**
  - **Job ads:** none were collected. Run the ATS searches (`site:jobs.lever.co`, `site:job-boards.greenhouse.io`, `site:jobs.ashbyhq.com` with dbt Tokyo) first.
  - **connpass line-ups:** try the browser for Data Engineering Study and other dbt events.
  - **Zenn and Qiita:** read new articles from both APIs since `metadata.generated_at`.
  - **Blog sweeps:** finish Mercari, SmartHR and CyberAgent.
  - **Women-in-data:** try other groups' own events, and ask the chapter hosts and Snowflake Data Heroes for introductions.
  - **dbt World Tour Tokyo 2026:** after 2026-10-20, add the Sony Bank and Mynavi speakers if the recordings name them.
- **People to locate:**
  - **Past speakers:** 24 people are still unknown, mostly past chapter speakers from 2022 to 2024. detaneeee, ReQ_HY and fujidev were searched on LinkedIn with no match. Search LinkedIn for the past speakers not yet searched, such as Hiroki Ishitada and Junya Morita.
  - **Motoyuki Oki:** add by hand. The LinkedIn result shows a data engineer at the Digital Agency in Tokyo. It failed the matching rule only because the employer is recorded as independent.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `tokyo/tokyo_dbt_companies.json`, the Tokyo dbt Meetup, `../enriched/tokyo-dbt-meetup.json` and Greater Tokyo. Add: "Search in Japanese. Add a handle to any name written only in Japanese script."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Zenn and Qiita APIs, Hatena company blogs, dbt Labs Tokyo agendas and women-in-tech events, plus chapter history. 126 people at 75 companies, 40 of them past chapter speakers. No job ads, because web search ran out. |
| 2026-10-01 | 1 | Location pass from public pages: GitHub profiles, in-person chapter talks and company contact pages. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 2 people placed in Greater Tokyo and 2 elsewhere. With the location pass, 22 people placed and 24 still unknown. |
