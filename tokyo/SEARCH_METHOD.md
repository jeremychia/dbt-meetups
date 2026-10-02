# Tokyo: city notes

This file holds what is specific to Tokyo. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Tokyo dbt Meetup](https://www.meetup.com/tokyo-dbt-meetup/), data in `tokyo_dbt_companies.json`
- **Region:** Greater Tokyo. That includes Saitama and Chiba, so a GitHub location of Kawagoe or Saitama counts. Kyoto, Okinawa and Fukushima do not.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-01)

| | Count |
|---|---|
| Companies | 135 |
| People | 146 |
| Tier 1 leads | 103 |
| First-time speakers (publish, no talk yet) | 80 |
| Proven speakers | 55 |
| Spoke at this chapter before | 40 |
| Based in the region | 108 |
| Based elsewhere | 5 |
| Location unknown | 33 |
| With a LinkedIn profile | 13 |
| Job ads mentioning dbt | 47 |
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

### Companies and job ads

- **[green-japan.com dbt search](https://www.green-japan.com/search?keyword=dbt):** the best source of Tokyo dbt employers. Search pages and ad pages answer a plain fetch and embed `__NEXT_DATA__` JSON. Each ad has separate fields for the work, the requirements and the welcome skills, plus the work prefectures. 160 ads in 8 pages; one ad per company was read. It added 42 Tokyo companies, 14 of them strong, such as MonotaRO, TimeTree, CARTA HOLDINGS, Marui Group and Hacobu. It also raised DeNA, TRIBEAU and unerry to strong. An ad open to every prefecture does not confirm a Tokyo office.
- **Zenn company publications:** the dbt topic API groups posts by company publication. Reading the post bodies added Skyfall, StoreHero, COUNTERWORKS, M&A Cloud and YUMEMI. It raised 10 companies from medium to strong, such as PKSHA Technology, Loglass, COTEN and READYFOR.
- **[dbt Labs Japan case studies](https://www.getdbt.com/jp/blog/case-study-telecy):** the getdbt.com sitemap lists Telecy's case study. It moved from dbt Core to dbt platform.

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

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[Snowflake女子会](https://note.com/snowvillage_wmn):** the best source. It is a women-led Snowflake user community, and anyone may attend. Its [joint hands-on with primeNumber User Group](https://pug.connpass.com/event/389174/) on 28 April 2026 had two data talks. 宮原栞梨 (INTAGE) spoke on loading panel data into Snowflake with TROCCO. 山下由紀子 (Infotech) spoke on a sales data pipeline with TROCCO, Snowflake and Cortex AI. The same page names all 11 organisers with employers, and they are recorded as connectors. The [meetup #8 report](https://note.com/snowvillage_wmn/n/n2c596a3d08c9) (27 August 2026) gave 3 career talks by organisers. The note feed reads with a plain fetch.
- **[ML女子部](https://women-ml.connpass.com/):** a women-run ML and data analysis group at Google Shibuya. Its [generative AI and data analysis meetup](https://women-ml.connpass.com/event/366580/) on 14 November 2025 gave 3 speakers. Satoru Nakamura spoke on a data analysis agent with BigQuery. KT (Canva Japan, founder of DATA Saber) and マスクドアナライズ also spoke. The organiser Sayaka Ito (unerry CTO) moderated the panel and is a connector.
- **[Women in AI Japan](https://www.meetup.com/women-in-ai-japan/):** 16 events since 2023, found through Meetup's group search. Taku Ogawa (HAPPY ANALYTICS) gave a [web analytics interview](https://www.meetup.com/women-in-ai-japan/events/306097652/) in February 2025. Yoko Ono, the WiDS Tokyo @ Yokohama City University ambassador, gave a [data science interview](https://www.meetup.com/women-in-ai-japan/events/297367669/) in November 2023. The hosts Eriko Toda and Kana Minami are connectors.
- **[Women Techmakers Tokyo](https://wtm-tokyo.connpass.com/event/342888/):** the International Women's Day 2025 event at LayerX had career talks only. It confirmed Sayaka Ito as a speaker.
- **connpass:** event and search pages now answer a plain fetch with a browser user agent. Search connpass for Japanese community names, because Japanese groups rarely use Meetup.
- **Also ask:** the Snowflake女子会 organisers and Snowflake Data Heroes for introductions to balance the line-up.

## 2. What didn't work here

- **[Zenn topic page](https://zenn.dev/topics/dbt):** renders nothing when fetched. Use the API instead.
- **[connpass](https://connpass.com/search/?q=dbt):** returned HTTP 403 to plain fetches in the first build, so the Data Engineering Study line-ups and most Tokyo meetup line-ups were not read. It answered a fetch with a browser user agent in the women-in-data pass.
- **[TECH PLAY](https://techplay.jp/event/924859):** returns HTTP 403, so the PyLadies Tokyo event was not read.
- **[Mercari engineering blog](https://engineering.mercari.com/blog/):** the search page did not render.
- **[SmartHR](https://tech.smarthr.jp/) and [Money Forward](https://moneyforward-dev.jp/) blogs:** no dbt posts.
- **Japanese company sites:** most load by JavaScript, so no office address came back.
- **Web search:** ran out after about 12 calls. No job ads were collected, and the Mercari, SmartHR and CyberAgent sweeps were only partly done.
- **[findy-code.io](https://findy-code.io/companies?keyword=dbt):** a fetch ignores the keyword and returns every company.
- **HN Who is hiring:** no Tokyo ad since 2023 mentions dbt.
- **dbt Labs Japan event pages:** the How-to and partner pages name no customer speakers. The customer session page names only Timee.
- **Women-in-data events:** [Women Tech Terrace 2024](https://www.cyberagent.co.jp/way/list/detail/id=30486) (CyberAgent) had no data talks. [WiDS Tokyo @ IBM](https://www.widsworldwide.org/events/event/wids-tokyo-ibm-2/) was a 2024 event with no speakers listed. No candidate came from this step.
- **Women-in-data groups with no data talks:** [PyLadies Tokyo](https://pyladies-tokyo.connpass.com/) meetups since 2024 are Python and AI workshops, and speakers are not named. [Tokyo WiMLDS](https://www.meetup.com/tokyo-women-in-machine-learning-and-data-science/) has held one event, in 2019. The [GTUG Girls and PyLadies data analysis workshop](https://gtuggirls.connpass.com/event/304447/) (January 2024) named no speakers.
- **Women-in-data sites that failed:** wids-tokyo.jp now hosts an unrelated blog. womendevsummit.jp did not resolve. connpass has no Women in Data Japan or Data + Women group. Snowflake女子会's TECH PLAY page returned HTTP 403.

## 3. Companies looked at

- **Finatext dominates:** its Zenn publication has 8 people in the file. Plan for one speaker per company per event.
- **Chura Data is based in Okinawa:** its CTO is in Naha, but two of its writers have GitHub locations in Saitama.
- **Customer speakers at dbt Labs events:** Sony Bank and Mynavi speak at dbt World Tour Tokyo on 2026-10-20.

<!-- companies:start -->
134 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (84)</summary>

10X Inc. (local presence not confirmed), ANDPAD (アンドパッド), Anthropic Japan G.K. (local presence not confirmed), Antway, CARTA HOLDINGS, Chura Data (local presence not confirmed), Cograph (コグラフ株式会社), commmune Inc. (local presence not confirmed), COTEN, COUNTERWORKS (local presence not confirmed), CyberAgent, Cybozu, DATUM STUDIO, dbt Labs (local presence not confirmed), dbt Tokyo Crew, DeNA, DMM.com, estie Inc., Fez, Finatext Holdings (Finatext / Nowcast), GA technologies, GENDA, GMO Pepabo, Hacobu, Headwaters, hokan, istyle, IVRy, jinjer, JINS, Knowledge Work, Kurashiru (dely), LayerX, Loglass, M&A Cloud (M&Aクラウド) (local presence not confirmed), Macbee Planet, Management Solutions (MSOL), Marui Group (丸井グループ), MeDiCU, Mitsumore Inc. (local presence not confirmed), Mizuho Research & Technologies (local presence not confirmed), Money Forward, MonotaRO, Mynavi, newmo Inc. (local presence not confirmed), Nowcast Inc. (local presence not confirmed), NTT DATA, PIVOT, pixiv, PKSHA Technology, PLEX (株式会社プレックス), primeNumber, Quick Network (local presence not confirmed), RAKSUL, RAKUDEJI (local presence not confirmed), READYFOR, Rehab for JAPAN, Sansan, Shimauma Print (しまうまプリント), SIGNATE Inc. (local presence not confirmed), Skyfall (local presence not confirmed), Snowflake Data Heroes (Japan), Sony Bank, Squad (株式会社Squad), stable Inc. (local presence not confirmed), Stanby, StoreHero (local presence not confirmed), Supership, Tech Lab (株式会社Tech Lab), Telecy (株式会社テレシー) (local presence not confirmed), Timee, TimeTree, TRIBEAU, truestar, TSR (TSR株式会社), Ubie, unerry, USEN ICT Solutions, VALUES, Works Human Intelligence, youthful days (local presence not confirmed), YUMEMI (ゆめみ) (local presence not confirmed), ZOZO, Zucks Ad Products Division (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (19)</summary>

Almondo, AMBL, Bandai Namco Nexus, DSS (株式会社ディーエスエス), FLARETECH (local presence not confirmed), HERP, INTAGE, Kauche (カウシェ), KDDI Agile Development Center, Lightcode (ライトコード), MBK Digital, Monstar Lab (モンスターラボ), Rec Technology Consulting (local presence not confirmed), Saison Technology, Sharing Innovations, SimpleForm (local presence not confirmed), Triarrow (トライアロー), TSUIDE, Yappli

</details>

<details><summary><b>dbt as a nice-to-have</b> (17)</summary>

bitA (ビットエー), Data One (データ・ワン), Exture (エクスチュア), Fellowship (フェローシップ), freee, Geekly (ギークリー), Japan System (ジャパンシステム), JMDC, KIYONO, LegalOn Technologies, Makip (メイキップ), oneroots, OpenStreet, SORAMICHI, Trustline (トラストライン), WealthNavi (ウェルスナビ), YOUTRUST

</details>

<details><summary><b>Uses a different stack</b> (14)</summary>

Canva Japan, CCCMK Holdings / V Point Marketing (local presence not confirmed), Daihatsu Motor (local presence not confirmed), HAPPY ANALYTICS (local presence not confirmed), IHI (local presence not confirmed), Infotech (インフォテック株式会社) (local presence not confirmed), Methodologic (株式会社メソドロジック) (local presence not confirmed), ML女子部 (Women in ML Japan), MOTEX (local presence not confirmed), mybest, Snowflake (Japan), Snowflake女子会 (Snowflake women's community), Women in AI Japan, Yokohama City University

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

<details><summary><b>Other sources checked</b> (32)</summary>

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
- [Meetup gql2 groupSearch near Tokyo](https://www.meetup.com/gql2)
- [Women in AI Japan past events (Meetup gql2)](https://www.meetup.com/women-in-ai-japan/)
- [Tokyo WiMLDS (Meetup gql2)](https://www.meetup.com/tokyo-women-in-machine-learning-and-data-science/) (nothing useful)
- [Snowflake女子会 x pUG hands-on (connpass)](https://pug.connpass.com/event/389174/)
- [Snowflake女子会 note feed](https://note.com/snowvillage_wmn/rss)
- [Snowflake女子会 on TECH PLAY](https://techplay.jp/community/snowvillage_wmn) (nothing useful)
- [ML女子部 (connpass)](https://women-ml.connpass.com/event/)
- [PyLadies Tokyo (connpass)](https://pyladies-tokyo.connpass.com/) (nothing useful)
- [PyLadies Tokyo site](https://tokyo.pyladies.com/) (nothing useful)
- [WTM Tokyo (connpass)](https://wtm-tokyo.connpass.com/event/)
- [GTUG Girls x PyLadies data analysis workshop](https://gtuggirls.connpass.com/event/304447/) (nothing useful)
- [WiDS Worldwide site search (Tokyo, Japan)](https://www.widsworldwide.org/wp-json/wp/v2/search?search=Tokyo)
- [wids-tokyo.jp](https://wids-tokyo.jp/) (nothing useful)
- [connpass searches: Women in Data, Data+Women, Women Techmakers Tokyo, 女子会 データ](https://connpass.com/search/?q=Women+in+Data) (nothing useful)
- [Women Developers Summit](https://womendevsummit.jp/) (nothing useful)
- [green-japan.com dbt search](https://www.green-japan.com/search?keyword=dbt)
- [Zenn dbt topic API](https://zenn.dev/api/articles?topicname=dbt&order=latest)
- [findy-code.io company search](https://findy-code.io/companies?keyword=dbt) (nothing useful)

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
  - **Women-in-data:** ask the chapter hosts and Snowflake Data Heroes for introductions.
- **Women-in-data communities not yet reachable:**
  - **Snowflake女子会 on TECH PLAY:** the community's own event pages return HTTP 403. Open them in a browser for meetups #1 to #7.
  - **WiDS Tokyo:** the @ IBM, @ Shotoku and @ Yokohama City University pages list no speakers. Ask Yoko Ono for recent line-ups.
  - **Women in Data Japan and Data + Women Japan:** no group page was found.
  - **Women Who Code Tokyo:** Women Who Code closed in 2024. The Women Who Go Tokyo group on connpass is a Go language group.
- **People from the women-in-data pass:** the 20 people added have no LinkedIn search, and most have no known location beyond the Tokyo venue.
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
| 2026-10-01 | 2 | Women-in-data pass. Checked Snowflake女子会, ML女子部, Women in AI Japan, Women Techmakers Tokyo, PyLadies Tokyo, Tokyo WiMLDS, GTUG Girls and WiDS Tokyo. Added 20 people with `sourced_via: women_in_data_community`: 5 speakers and 15 connectors, 6 of whom also gave talks. Added organiser evidence to あれ (allllllllez). Added 6 community channels. The assembler also added 2 past chapter speakers from the enriched file. |
| 2026-10-01 | 3 | Company pass from green-japan.com, Zenn company publications and the dbt Labs sitemap. 48 companies added: 42 from job ads (14 strong, 11 medium, 17 nice-to-have), 5 from Zenn and Telecy from a case study. 13 companies raised to strong, and estie's Tokyo presence confirmed. 47 job ads added; the file had none before. |
