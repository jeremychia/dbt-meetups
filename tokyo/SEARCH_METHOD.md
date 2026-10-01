# Tokyo dbt search: method, lessons and replication prompt

This file goes with `tokyo_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-10-01
- **Goal:** find people in Greater Tokyo who could **speak at** (or attend) the [Tokyo dbt Meetup](https://www.meetup.com/tokyo-dbt-meetup/), and the local companies that use dbt.
- **Region:** Greater Tokyo. That includes Saitama and Chiba, so a GitHub location of Kawagoe or Saitama counts. Kyoto, Okinawa and Fukushima do not.

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

## 1. How the search was done

Most of the content is in Japanese. Titles are kept as written, with an English description.

### Step 1: Zenn and Qiita

- **Zenn:** the JSON API ([`zenn.dev/api/articles?topicname=dbt&order=latest&page=N`](https://zenn.dev/api/articles?topicname=dbt&order=latest)) lists every dbt article with its author and company publication. About 800 of the newest and most-liked articles were read.
- **Qiita:** the API ([`qiita.com/api/v2/items?query=tag:dbt`](https://qiita.com/api/v2/items?query=tag:dbt)) works without a token and shows the author's organisation. Posts since 2024-06 were read. It added CyberAgent, NTT DATA, ZOZO and DeNA authors.
- **What was kept:** authors who wrote in a company publication from 2024 onwards. Their Zenn bios gave titles and self-stated roles, such as Snowflake Data Superhero.
- **Yield:** about 110 company-publication articles since 2024-06. Most people in the file come from here.

### Step 2: Company tech blogs

- **Hatena blogs:** Hatena-based company blogs answer `/search?q=dbt` with plain HTML, so no web searches were needed.
  - [Timee](https://tech.timee.co.jp/): data reliability team posts on dbt snapshots, unit tests and DuckDB checks.
  - [LayerX](https://tech.layerx.co.jp/): two open-source dbt packages for Snowflake governance.
  - [ZOZO](https://techblog.zozo.com/): dbt adoption on Cloud Composer.
- **No dbt posts:** [SmartHR](https://tech.smarthr.jp/) and [Money Forward](https://moneyforward-dev.jp/). Money Forward's Zenn publication had one.
- **Did not render:** the [Mercari engineering blog](https://engineering.mercari.com/blog/) search page.

### Step 3: Conferences and other meetups

- **[dbt World Tour Tokyo 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-tokyo)** (2026-10-20): Sony Bank and Mynavi have customer sessions, but the speakers are not named. Both are recorded as companies with no people.
- **[Coalesce on the Road Tokyo 2025](https://www.getdbt.com/jp/coalesce-in-tokyo):** mostly dbt Labs speakers, and customer speakers are not named.
- **[connpass](https://connpass.com/search/?q=dbt):** it returns HTTP 403 to plain fetches, so the Data Engineering Study line-ups were not read.

### Step 4: Women-in-data communities

This step looks for speakers through women-focused groups' own events. It never labels or guesses anyone's gender.

- **[Women Tech Terrace 2024](https://www.cyberagent.co.jp/way/list/detail/id=30486)** (CyberAgent): no data talks.
- **[WiDS Tokyo @ IBM](https://www.widsworldwide.org/events/event/wids-tokyo-ibm-2/):** a 2024 event with no speakers listed.
- **[PyLadies Tokyo](https://techplay.jp/event/924859):** TECH PLAY returned HTTP 403.
- **Result:** no candidate came from this step.

### Step 5: Chapter history

- **Past speakers:** every named speaker from `../enriched/tokyo-dbt-meetup.json` was added, with their talk as evidence. That covers 19 events, from meetup #4 (2022-08-23) to meetup #21 (2026-07-29).
- **Organisers:** the two hosts of meetup #21 are recorded as organisers. The writer of the chapter's [meetup reports on Zenn](https://zenn.dev/p/dbttokyo) is recorded as a connector, meaning someone who can introduce people.

### Step 6: Location pass and LinkedIn pass

- **Location pass:** people were placed from public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
  - GitHub profiles linked from a Zenn profile gave high-confidence locations.
  - An in-person talk at a Tokyo dbt Meetup since 2025, at an employer with a Tokyo office, gave medium confidence. Venues come from `past_meetups`.
  - The [estie](https://www.estie.co.jp/company) and [Mitsumore](https://meetsmore.com/company) contact pages confirmed their Tokyo offices.
- **LinkedIn pass:** search results only, never a LinkedIn page. It placed 2 people in Greater Tokyo and 2 elsewhere (Naha and Seattle).
- **Yield:** 22 people placed across both passes, and 24 still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **The Zenn API** is the best single source. One call per page lists each dbt article with its author and company. The [topic page](https://zenn.dev/topics/dbt) itself renders nothing when fetched.
  - **The Qiita API** needs no token and names the author's organisation.
  - **Hatena blog search** returns plain HTML, which saves web searches.
  - **GitHub profiles** linked from Zenn give a stated city. Zenn and Qiita location fields were empty for every handle checked.
  - **The getdbt.com roadshow pages** carry speaker names and companies as JSON in the raw HTML.
- **Sources that didn't:**
  - **connpass and TECH PLAY** return HTTP 403, so most Tokyo meetup line-ups were not read.
  - **Most Japanese company sites** load by JavaScript, so no office address came back.
  - **Web search** ran out after about 12 calls. No job ads were collected, and the Mercari, SmartHR and CyberAgent sweeps were only partly done.
- **Watch out for:**
  - **Handles, not names.** Most authors publish under a handle. Names are recorded as written, with an ASCII id.
  - **Names in Japanese script only.** The assembler strips names to ASCII before matching, so two names in Japanese script merge silently. Add a handle to each name, for example "山口歩夢 (gussan_a)".
  - **Blog authors who are past speakers under another name.** These were left out to avoid duplicates: okiyuki is Motoyuki Oki, Yoshi-ken is Yoshiken, harry/gappy is Harry, sisisin is Shimenyan, t-hiroto is Hiroto Takahashi and ryosuke839 is Ryosuke Lin Yamamoto.
  - **One name may be misspelt.** ZOZO's 栁澤 (@i_125) is Satoko Yanagisawa on Qiita. The chapter file has "Yoshiko Yanagisawa".
  - **Chura Data is based in Okinawa.** Its CTO is in Naha, but two of its writers have GitHub locations in Saitama.
  - **Finatext dominates.** Its Zenn publication has 8 people in the file. Plan for one speaker per company per event.

## 3. Key leads

- **First-time speakers** (people who publish about dbt but have no talk on record):
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
  - **[Snowflake Data Heroes](https://zenn.dev/p/dataheroes):** the Japanese Snowflake community, with many dbt users. Ask them for introductions to balance the line-up.

## 4. Before outreach

- **Check most "in region" calls.** Only 17 of the people marked in the region have a location note with evidence. The rest were placed in Tokyo from their employer's Tokyo head office during research.
- **Check tier 1.** It holds 103 people because any first-time speaker with a post from 2024 onwards is raised to tier 1. 14 of them have no item that mentions dbt, for example bigmegaphone and chanyou. Sort by how recent and how deep the dbt work is.
- **Confirm real names.** Most new people are recorded by their Zenn or Qiita handle.
- **Check possible duplicates and misspellings:**
  - **Yanagisawa:** confirm whether the past speaker is Satoko or Yoshiko.
  - **Toshitei Ito** may be Toshitaka Ito, a dbt Labs solutions architect in Tokyo.
  - **Company records:** several companies appear twice, once from research and once from the chapter history. Examples are Kurashiru (dely) and dely Inc., and Finatext Holdings (Finatext / Nowcast) and Nowcast Inc.
- **Fix placeholder employers.** One company record is named "Inc.". "Anthropic Japan G.K." holds Tristan Handy, which comes from the talk text.
- **Skip dbt Labs staff.** Mark Wan, Andrew Escay and Elias DeFaria are excluded from outreach. Elias DeFaria is in Seattle.
- **Check one weak location.** AZEGAMI Kazuya's Zenn bio suggests Sukagawa, Fukushima, but names no home city. The employer, youthful days, lists an office in Nagano. The location stays unknown.
- **Check people already booked.** Sony Bank and Mynavi speak at dbt World Tour Tokyo on 2026-10-20.

## 5. Next run

- **Job ads:** none were collected. Run the ATS searches (`site:jobs.lever.co`, `site:job-boards.greenhouse.io`, `site:jobs.ashbyhq.com` with dbt Tokyo) first.
- **connpass line-ups:** try the browser for Data Engineering Study and other dbt events.
- **Blog sweeps:** finish Mercari, SmartHR and CyberAgent.
- **Women-in-data:** try other groups' own events, and ask the chapter hosts and Snowflake Data Heroes for introductions.
- **People still without a location:** 24, mostly past chapter speakers from 2022 to 2024. detaneeee, ReQ_HY and fujidev were searched on LinkedIn with no match. Search LinkedIn for the past speakers not yet searched, such as Hiroki Ishitada and Junya Morita.
- **Manual add:** Motoyuki Oki's LinkedIn result shows a data engineer at the Digital Agency in Tokyo. It failed the matching rule only because the employer is recorded as independent.
- **dbt World Tour Tokyo 2026:** after 2026-10-20, add the Sony Bank and Mynavi speakers if the recordings name them.

## 6. Replication prompt

````
You are extending my dataset of Greater Tokyo companies that use dbt, and people who could
speak at or attend the Tokyo dbt Meetup. The file is tokyo/tokyo_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read tokyo/SEARCH_METHOD.md first, then
research/README.md, research/raw-format.md, research/location-task.md and
research/linkedin-task.md. Keep the shared schema (berlin_planning/SEARCH_METHOD.md §3).

Try first: job ads (Lever, Greenhouse and Ashby site: searches for dbt Tokyo), connpass
line-ups through the browser, new Zenn articles (zenn.dev/api/articles?topicname=dbt&order=latest)
and Qiita posts (qiita.com/api/v2/items?query=tag:dbt) since metadata.generated_at, and the
Mercari, SmartHR and CyberAgent blogs. Add a handle to any name written only in Japanese script.

Rules: never fetch LinkedIn pages, only use search results; public professional information
only; never guess gender, and record pronouns only when self-stated. Assemble with
research/assemble.py --base, place people with research/apply_locations.py, then run
research/validate.py and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Zenn and Qiita APIs, Hatena company blogs, dbt Labs Tokyo agendas and women-in-tech events, plus chapter history. 126 people at 75 companies, 40 of them past chapter speakers. No job ads, because web search ran out. |
| 2026-10-01 | 1 | Location pass from public pages: GitHub profiles, in-person chapter talks and company contact pages. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 2 people placed in Greater Tokyo and 2 elsewhere. With the location pass, 22 people placed and 24 still unknown. |
