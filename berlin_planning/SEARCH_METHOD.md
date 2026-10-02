# Berlin: city notes

This file holds what is specific to Berlin. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Berlin dbt Meetup](https://www.meetup.com/berlin-dbt-meetup/), data in `berlin_dbt_companies.json`
- **Region:** the Berlin metro area. Commuter towns within about an hour count, such as Potsdam.
- **First built:** 2026-09-23
- **Starting point:** the Berlin search starts from **public content**: blog posts, talks, case studies, podcasts and other meetups' line-ups. It adds job ads as a second signal. The Lithuania search, by contrast, started from job ads.
- **Reference file:** this file's `metadata.field_definitions` is the reference copy for every city ([§4](../research/README.md#4-shared-schema-version-3)).

<!-- at-a-glance:start -->
**At a glance** (version 8, 2026-10-01)

| | Count |
|---|---|
| Companies | 168 |
| People | 165 |
| Tier 1 leads | 11 |
| First-time speakers (publish, no talk yet) | 16 |
| Proven speakers | 132 |
| Spoke at this chapter before | 10 |
| Based in the region | 106 |
| Based elsewhere | 13 |
| Location unknown | 46 |
| With a LinkedIn profile | 131 |
| Job ads mentioning dbt | 128 |
| Past chapter meetups | 15 |
<!-- at-a-glance:end -->

## 1. Where to look in Berlin

### Company blogs and case studies

- **Scale-ups and corporates scanned (2026-09):** GetYourGuide, Delivery Hero, Zalando, HelloFresh, N26, Trade Republic, SumUp, Taxfix, Contentful, Babbel, Omio, Raisin, Personio, Kleinanzeigen, idealo, Auto1, Flink, Choco, Wolt, Blinkist, Urban Sports Club, Forto, Sennder, OneFootball, Ecosia, Enpal, TIER/Dott, Kaufland e-commerce, Billie, SoundCloud and others.
- **Vendors and consultancies scanned:** Y42, dltHub, Gemma Analytics, diconium, Kestra, Tasman, SYNQ, Xebia.
- **[getyourguide.careers/posts](https://www.getyourguide.careers/posts):** the most active Berlin dbt writer. Posts cover dbt on Databricks, Cosmos and AI-generated docs.
- **dbt Labs case studies:** they name the data lead and give concrete numbers, for example Enpal and TIER.
- **Blog list:** the scanned URLs are in `sources.company_blogs_scanned` and in each company's `other_evidence[type=blog_scanned]`.

### Data Berlin

Data Berlin is Berlin's largest general data meetup and job board, run by Francesco "mucio" Mucio. Its channels are in `community_channels`, and their URLs in `sources.data_berlin`.

- **Luma line-ups:** [lu.ma/data-berlin](https://lu.ma/data-berlin) has line-ups since November 2025.
- **meetup.com line-ups:** [meetup.com/data-berlin](https://www.meetup.com/data-berlin/events/?type=past) has events from May 2023 onwards. Each event page lists every talk with the speaker's name, role and company.
- **Newsletter:** [databerlin.substack.com](https://databerlin.substack.com/archive) issues (`/p/data-berlin-<N>`) name only events and hosts, never speakers. They are still useful for collecting event URLs.
- **Partner events:** events on the Data Berlin Luma calendar, such as OSA Community and Metabase × dltHub, are tagged in `speaker_evidence.event` as "(partner event on the Data Berlin calendar)".
- **Scoring Data Berlin speakers:** every speaker became a person, with the talk as `speaker_evidence`. Tier 2 for talks relevant to a dbt meetup, tier 3 for vendor pitches, pure ML or LLM, and marketing-science talks.
- **Job board, dbt skill page:** [databerlin.net/skills/dbt](https://databerlin.net/skills/dbt) pulls ads directly from company ATS platforms and tags skills automatically from the ad text. On 2026-09-23 it listed 89 open Berlin roles at 70 companies. Each role became a `job_postings` entry with source "Data Berlin job board". It is plain server-rendered HTML, so one fetch reads it.

### Companies and job ads

- **Data Berlin job board (2026-10-01):** [databerlin.net/skills/dbt](https://databerlin.net/skills/dbt) listed 77 roles. 5 came from companies not yet in the file. Reading 14 role pages raised 6 companies to strong, because their ads require dbt.
- **Company job boards:** the open Greenhouse, Lever and Ashby job APIs (`boards-api.greenhouse.io/v1/boards/<slug>/jobs?content=true`, `api.lever.co/v0/postings/<slug>?mode=json`, `api.ashbyhq.com/posting-api/job-board/<slug>`) return the full ad text, so one call per company checks for the whole word dbt and the location. About 30 of 70 Berlin employers tried have a board. Superchat, Yazio, Taktile, GetYourGuide, Enpal, Doctolib, Solaris and Zenjob have Berlin ads that mention dbt.
- **[arbeitnow.com API](https://www.arbeitnow.com/api/job-board-api):** `?page=N` returns German job ads with full text. 14 pages (1,851 ads) were read before it returned HTTP 429. It added Good Hood (nebenan.de) and Real Digital.
- **HN Who is hiring:** the Algolia search for "dbt berlin" gave 4 companies with Berlin roles and dbt in the stack: Seen Finance, dotplay.games, WAY and Return.
- **[applydata data engineering meetup](https://www.meetup.com/applydata-berlin/events/?type=past):** its line-ups at the diconium office name dbt talks. They raised Ratepay and diconium to strong.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published.
- **[PyLadies Berlin](https://www.meetup.com/pyladies-berlin):** the best source. Its themed data talk nights, such as 12 Nov 2024, had dbt and dlt talks. Its listings show speakers' own pronouns. Newer events added Anne Sehnal and Cassandra Milbradt of d-fine ([AI agents workshop](https://www.meetup.com/pyladies-berlin/events/314645733/), May 2026), and Claudia Stangarone and Helen FitzGerald of Bettermile ([delivery-risk talk](https://www.meetup.com/pyladies-berlin/events/304510252/), January 2025). The organiser Vanessa Fonseca is a connector.
- **[Women in Big Data Berlin](https://www.meetup.com/women-in-big-data-berlin-meetup-group):** speakers and the founder. Its [January 2025 data and governance evening](https://www.meetup.com/women-in-big-data-berlin-meetup-group/events/305143951/) added Silke Kaiser (Hertie School) and Martin Manhembué (data quality with AI agents).
- **[AWS Women's User Group Berlin](https://www.meetup.com/berlin-amazon-web-services-meetup-group/):** its [April 2025 online session with Women on Snowflake](https://www.meetup.com/berlin-amazon-web-services-meetup-group/events/307161270/) gave Anastasiia Stefanska (TUI) and Isabella Renzetti, both Snowflake Data Superheroes. Its 4 organisers (Ruth Otero, Sana Shah, Shabnam Motamedirad and Linda Mohamed) are connectors.
- **[Women on Snowflake](https://usergroups.snowflake.com/women-on-snowflake/):** an online Snowflake user group led by the same two people. It runs hands-on labs and Women in Data breakfasts at Snowflake World Tour stops.
- **[Women Techmakers Berlin](https://www.meetup.com/wtm-berlin):** speakers with data talks.
- **[Women+ in Data/AI Festival](https://women-in-data-ai.tech):** the 2023–2024 editions, with a data engineering track. Martina Freers (INNOQ), who leads it, is a connector.
- **Also checked:** WomenTech Network Berlin, Berlin WiMLDS and PyLadies at PyCon DE.
- **Connectors:** the PyLadies Berlin organisers, the WiBD Berlin founder and the AWS Women's User Group organisers are tier `connector`.

### Conferences, newsletters and podcasts

- **Conference agendas:** dbt Summit, Coalesce, Databricks Data + AI Summit, [Berlin Buzzwords](https://program.berlinbuzzwords.de/), [PyCon DE & PyData](https://pretalx.com/pyconde-pydata-2026/) and the [applydata Data Engineering MeetUp](https://applydata.io/data-engineering-meetup/). The URLs are in `sources.conference_agendas`.
- **Newsletters:** Substack and Medium, for example Jimmy Pang's Data Biz.
- **YouTube and podcasts:** BARC and Modern Data Show.
- **Chapter history:** past talks come from `../enriched/berlin-dbt-meetup.json`. Torsten Glunde, for example, spoke at Data Berlin in Feb 2026 and at the Berlin dbt Meetup in Apr 2026.

### LinkedIn and locations

- **LinkedIn in v3:** only the tier-2 Data Berlin speakers were searched.
- **Pronouns:** a check of 80 tier-1 and tier-2 people in September 2026 found none in LinkedIn search results. 3 people have self-stated pronouns.
- **Locations (v6):** Meetup host and RSVP lists tied to the person placed people, as did recent in-person talks at Data Berlin and other Berlin events by people whose employer has a Berlin office.

### How the first run was split

- **Parallel runs:** the first company-blog sweep; the first people sweep; blogs batch A (large scale-ups); blogs batch B (vendors, consultancies and smaller scale-ups); LinkedIn URLs in 3 batches; and Data Berlin meetup line-ups.
- **Direct read:** the job-board page, with one fetch.
- **Merge:** one builder script merged the records and applied the shared schema.

## 2. What didn't work here

- **Data Berlin newsletter, for speakers:** it names events and hosts only.
- **Data Berlin YouTube:** the channel page and RSS feed returned no videos, so recordings aren't linked yet.
- **dbt Slack #local-berlin:** can't be searched from outside Slack.
- **Quiet scale-up blogs:** N26, SumUp, Babbel, Omio, Solaris, Auto1, SoundCloud and Urban Sports Club engineering have been quiet since 2023.
- **Women-in-data groups with no active Berlin chapter or speaker lists for 2023–26:** [R-Ladies Berlin](https://www.meetup.com/rladies-berlin/) (last event November 2020), Women in Data, WiDS, She Loves Data, Women in AI, Girls in Tech and Ladies of Code.
- **Inactive or paused since the last run:** [Berlin WiMLDS](https://www.meetup.com/Berlin-Women-in-Machine-Learning-and-Data-Science/) last met in November 2023. The [Women+ in Data/AI Festival](https://women-in-data-ai.tech/) is paused in 2025.
- **Women-in-tech groups with no data talks:** [Women Techmakers Berlin](https://www.meetup.com/wtm-berlin/) in 2025–26 (roundtables, IWD, AI and careers), [Empowered in Tech](https://www.meetup.com/empowered-in-tech/), [IT_Frauen Berlin](https://www.meetup.com/it_frauen-berlin/) and AI for Women Berlin (no events).
- **Data Berlin talks as dbt evidence:** none of the 78 talk descriptions mentioned dbt. The programme has been heavy on AI and agents since 2025.
- **GitHub code search:** `filename:dbt_project.yml org:<org>` found no public dbt project in the orgs tried. The search rate limit cut several calls short. Orgs tried: idealo, Zalando, Flink, JustWatch, Delivery Hero, Ecosia, HelloFresh, Taxfix, Contentful, GetYourGuide, Trade Republic, N26 and Gemma Analytics (only its dbt utilities).
- **Job boards with no Berlin dbt ad:** idealo, Zalando, Bolt, Delivery Hero, Taxfix, Omio and Sennder have no open Greenhouse, Lever or Ashby board. Flink, JustWatch, Scout24, GROPYUS, N26, HelloFresh, Contentful, Babbel and Raisin have one, but no Berlin ad there mentions dbt.
- **dbt Labs case studies:** only Enpal and TIER are Berlin companies, and both were already in the file.
- **Meetup venues for companies:** the 2024–26 venues of Data Berlin, PyData Berlin and the Berlin Airflow meetup were already in the file or were event spaces. Bonial hosted PyData Berlin in November 2024, but nothing ties it to dbt. BEADS and Analytics Pioneers Berlin meet at a university or online.

## 3. Companies looked at

- **GetYourGuide** is the most active Berlin dbt writer, and several of the strongest leads work there.
- **Different stacks:** Zalando uses Databricks Metric Views, and idealo uses Spark and Glue. Both have `dbt_signal: none`.
- **Most dbt hiring (Data Berlin board):** Fivetran, Statista, Grafana Labs, Redcare Pharmacy, Europace, SumUp, Zendesk, N26 and Alpaca.
- **Roles based elsewhere:** some roles on the Berlin board are remote or outside Berlin, such as Fivetran's Costa Rica role and Grafana's Sweden and Spain roles.

<!-- companies:start -->
167 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (35)</summary>

Alpaca, Bolt (local presence not confirmed), Choco, Contentful, Cosuno, dbt Labs (Berlin staff), Delivery Hero, diconium, dltHub, Ecosia, Enpal, Flinn, FlixMobility, Gemma Analytics, GetYourGuide, Good Hood GmbH (nebenan.de), HelloFresh, Kestra (local presence not confirmed), Kleinanzeigen (ex-eBay Kleinanzeigen / Adevinta), Lightdash, MotherDuck (local presence not confirmed), N26, Octopus Energy Group, PERGOLUX, Personio, Ratepay, SumUp, Superchat, SYNQ (acquired by Coalesce) (local presence not confirmed), Tasman Analytics (local presence not confirmed), Taxfix, TIER (now Dott), Vinted, Y42, Yazio

</details>

<details><summary><b>Some dbt signal</b> (76)</summary>

1Global, 1KOMMA5°, About You, aconium GmbH, adsquare, Almedia, AutoStore, Babbel, Bettermile, Bikeleasing Gruppe, Billie, Blinkist, CarOnSale, celebrate company GmbH, ClickHouse, Correlation One, Cursor, Dataciders, DataTalks.Club, Doctolib, dotplay.games, Eberlein Kunz, Europace AG, Eventim, EY, finanzen.net GmbH, Finn, Fivetran, Forto, getolo, Gigs, GLS/NXT, Grafana Labs, HubSpot, ista, Jupus, Just Eat Takeaway / Lieferando (local presence not confirmed), Kaufland e-commerce, Kolibri Games, Leadfeeder, Liqid, Moonfare, n8n, Nansen, neuefische, Omio, OneFootball, Planet, Qonto, Qualifyze, Raisin, Redcare Pharmacy, Return, RSG Group GmbH, Scalable Capital, Seen Finance, Shine, Shopware, Smartbroker, Snowflake, Solaris Bank, StackFuel, Statista, Taktile, Team Passerelle, The Pioneer, Tierarzt Plus Partner, Trade Republic, Trawa, Urban Sports Club, Vestiaire Collective, WAY, Wikimedia Foundation, Wolt, Zendesk, Zenjob

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

Real Digital

</details>

<details><summary><b>Not verified</b> (50)</summary>

Alligator Company (local presence not confirmed), Altinity (local presence not confirmed), AstraZeneca (local presence not confirmed), Astronomer (local presence not confirmed), Bayer (local presence not confirmed), Bayerischer Rundfunk (local presence not confirmed), Bruin, Cognee, Databricks (local presence not confirmed), Decodable (local presence not confirmed), Deloitte (local presence not confirmed), DHL (local presence not confirmed), Digital Pills (local presence not confirmed), DocMorris, Dremio (local presence not confirmed), EDB (local presence not confirmed), EQOM Group (local presence not confirmed), Exasol (local presence not confirmed), Exxeta (local presence not confirmed), FGS Global, Flink, GlassFlow, GROPYUS, HelloPrint (local presence not confirmed), JustWatch, Keboola (local presence not confirmed), Kertos (local presence not confirmed), Lessmore (local presence not confirmed), Look Beyond Solutions (local presence not confirmed), Metabase (local presence not confirmed), METRO.digital, MILES Mobility, Miro (local presence not confirmed), nao Labs, Neugelb Studios (Commerzbank), Picnic Technologies (local presence not confirmed), RisingWave (local presence not confirmed), Schüttflix (local presence not confirmed), Scout24, ScramDB (local presence not confirmed), SirDash (local presence not confirmed), Snap (local presence not confirmed), StepStone (local presence not confirmed), thermondo, Tower.dev, TUI (local presence not confirmed), Vakamo (local presence not confirmed), Wandernary (local presence not confirmed), Zattoo, zerobang (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (5)</summary>

d-fine, Data Berlin (newsletter & meetup), idealo, Thoughtworks, Zalando

</details>

<details><summary><b>Blogs and sites scanned</b> (24)</summary>

- https://bolt.eu/en/blog/
- https://careers.wolt.com/en/blog/tech
- https://choco.com/us/stories
- https://databerlin.substack.com/
- https://deliveryhero.jobs/blog/
- https://dev.to/berlin-tech-blog
- https://dlthub.com/blog
- https://engineering.hellofresh.com/
- https://engineering.urbansportsclub.com/
- https://kaufland-ecommerce.com/en/blog/
- https://kestra.io/blogs
- https://medium.com/berlin-tech-blog
- https://medium.com/idealo-tech-blog
- https://medium.com/inside-sumup
- https://medium.com/insiden26
- https://medium.com/justeattakeaway-tech
- https://medium.com/omio-engineering
- https://medium.com/onefootball-locker-room
- https://medium.com/taxfix
- https://traderepublic.substack.com/archive
- https://vinted.engineering/
- https://www.getyourguide.careers/posts
- https://www.tasman.ai/news
- https://www.y42.com/blog

</details>

<details><summary><b>Other sources checked</b> (11)</summary>

- [Meetup gql2 groupSearch near Berlin (women-in-data queries)](https://www.meetup.com/gql2#groupSearch-berlin-wid)
- [PyLadies Berlin 2025-2026 events (Meetup gql2)](https://www.meetup.com/pyladies-berlin/events/?type=past)
- [Women in Big Data Berlin 2025-2026 events (Meetup gql2)](https://www.meetup.com/women-in-big-data-berlin-meetup-group/events/?type=past)
- [AWS Women's User Group Berlin 2025-2026 events (Meetup gql2)](https://www.meetup.com/berlin-amazon-web-services-meetup-group/events/?type=past)
- [Women Techmakers Berlin 2025-2026 events (Meetup gql2)](https://www.meetup.com/wtm-berlin/events/?type=past) (nothing useful)
- [Women on Snowflake user group page](https://usergroups.snowflake.com/women-on-snowflake/)
- [Women+ in Data/AI Festival site](https://women-in-data-ai.tech/) (nothing useful)
- [Empowered in Tech (Meetup gql2)](https://www.meetup.com/empowered-in-tech/) (nothing useful)
- [R-Ladies Berlin (Meetup gql2)](https://www.meetup.com/rladies-berlin/) (nothing useful)
- [Berlin WiMLDS (Meetup gql2)](https://www.meetup.com/Berlin-Women-in-Machine-Learning-and-Data-Science/) (nothing useful)
- [IT_Frauen Berlin and AI for Women Berlin (Meetup gql2)](https://www.meetup.com/it_frauen-berlin/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers (tier 1):**
  - **Danny Burleigh and Lennart Scharmann (GetYourGuide):** the analytics harness for AI.
  - **David Förster and Max Rieger (idealo):** data contracts.
  - **Nélson Rangel (OneFootball):** dbt models for engineering release metrics.
  - **Hiba Jamal (dltHub):** dlt with dbt's semantic layer.
- **First-time speakers (tier 2, older or undated posts):** Fabian Bücheler and Shaurya Sood (GetYourGuide) on Cosmos and dbt on Databricks; Akash Ganguly (HelloFresh); Dolf ter Hofsté (Taxfix); Breno Costa and Steven Xu (Delivery Hero).
- **Anchor speakers:**
  - **Giovanni Corsetti Silva (GetYourGuide)**
  - **Waqas Shahid and Uttpesh Vyas (Delivery Hero)**
  - **Alexander Novikov (Enpal)**
  - **Andre Wagner (Taxfix)**
- **From Data Berlin, relevant to a dbt meetup:**
  - **Michael Gabriel (Enpal):** warehouse adoption from 50 to 650 users.
  - **Aleksandr Zolotukhin and Paula Urrialde (JustWatch):** Lightdash, and AI in BI.
  - **Hamzah Chaudhary (Lightdash):** semantic layer to AI analyst.
  - **Scout24's data platform team.**
  - **Adedeji Rodemade (Adsquare):** analytics engineering at scale.
  - **Christian Hiroz and Tadej Štajner (SumUp):** a self-service platform and SumUp's data lake.
  - **Divya Bokaria (Zattoo):** a self-service analytics culture.
- **Connectors:**
  - **Francesco "mucio" Mucio:** runs Data Berlin.
  - **PyLadies Berlin co-lead and WiBD Berlin founder:** routes to women speakers.
- **Topics:** the most common are dbt migration & adoption, orchestration & ci/cd, performance & scale and analytics engineering. With Data Berlin added, `genai & llm` is now the most frequent topic.

## 5. Before outreach

- [ ] **Filter Data Berlin speakers** by tier 2 and topics. They are Berlin data practitioners, not dbt speakers.
- [ ] **Open the job ad** before calling dbt core for a company. Board tags come from automatic extraction.
- [ ] **Check event dates on the event page.** Luma and meetup.com can differ, for example Oct 14 vs Oct 16, 2025.
- [ ] **Check same-name people** against company or role. There are several people called Steven Xu, and 2 Breno Costas at Delivery Hero.
- [ ] **Normalise name variants** when matching, for example "Francesco 'mucio' Mucio" vs "Francesco Mucio".
- [ ] **Check stale roles:** Max Rieger moved to 7NXT and Nuno Capeta to Kariisma. Alexander Novikov's headline no longer says Enpal. Angelita Frozza Sanches is now Head of Core Data Platform at Scout24.
- [ ] **Remember who lives elsewhere:** Silja Märdla (Tallinn), Aman Gupta (Mumbai), Faysal Rehmat (New York), Torsten Glunde (Hannover region) and Emanuele Celoria (Turin) spoke at Berlin events.
- [ ] **Check tier-1 first-time speakers raised by the rule,** in case a post doesn't mention dbt.
- [ ] **Treat Vinted people as backup speakers.** They are flagged `internal_vinted: true`.
- [ ] **Note labelled dbt Labs and Fivetran staff** in the cockpit.
- [ ] **Run the line-up balance check** in [event-planning-template.md](event-planning-template.md).

## 6. Next run

- **Sources to try first:**
  - **Data Berlin job board:** add new roles from [databerlin.net/skills/dbt](https://databerlin.net/skills/dbt) and set `last_seen` on roles still listed.
  - **Data Berlin events:** new line-ups on [Luma](https://lu.ma/data-berlin) and [meetup.com](https://www.meetup.com/data-berlin/events/?type=past). Give their talks a `content_id` of `databerlin-<date>-<slug>`.
  - **Blogs:** re-scan `sources.company_blogs_scanned` and the dbt Labs case studies for Berlin companies.
  - **Conferences:** dbt Summit and Coalesce, Databricks Data + AI Summit, Berlin Buzzwords, PyCon DE & PyData and the applydata meetup.
  - **Women-in-data events:** new PyLadies Berlin, Women in Big Data Berlin and AWS Women's User Group Berlin events, and the Women on Snowflake past events, which need a browser to load more than four. Check whether the Women+ in Data/AI Festival returns in 2026.
  - **Links:** replace `overview_page` links with direct links.
- **People to locate:**
  - **Unknown locations:** 51 people. Work in tier order, with past chapter speakers first within a tier.
  - **LinkedIn:** search tier 1–2 people with `linkedin_confidence` of not_searched or low, and re-check medium ones.
  - **Notes:** re-check people with notes like "verify" or "may have left".
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with folder `berlin_planning`, chapter "Berlin dbt Meetup", enriched file `enriched/berlin-dbt-meetup.json` and region "Berlin metro, including commuter towns within about an hour such as Potsdam". Add: "Fetch databerlin.net/skills/dbt with source 'Data Berlin job board'; check Data Berlin on Luma and meetup.com; check Berlin Buzzwords, PyCon DE & PyData and applydata."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-23 | 1 | First search: 43 companies, 49 people, 54 content items tagged with topics. LinkedIn URLs found for 41 people. Cross-referenced with 15 past Berlin meetups (9 people had already spoken). |
| 2026-09-23 | 2 | Restructured to the Lithuania layout (companies → people → speaker_evidence). Added `job_postings`, `watchlist`, `meetup_fit`, `level`, `past_meetups`, `sources` and `community_channels`. |
| 2026-09-23 | 3 | **Data Berlin added:** 79 talk records (72 unique talks) from 26 Data Berlin meetups and 3 partner events, May 2023 – Sep 2026, bringing in 75 new people. 25 of them are tier 2; 22 have LinkedIn profiles, found by searching those 25. Also 89 dbt roles at 70 companies from `databerlin.net/skills/dbt`. **Standardised with Lithuania:** file renamed from `berlin_speaker_candidates.json` to `berlin_dbt_companies.json`. Shared schema v1 with identical keys, `field_definitions` and `counts`. Renamed `berlin_presence` → `local_presence`, `berlin_based` → `based_in_region`, `past_berlin_meetup_talks` → `past_chapter_talks`. Totals: 144 companies, 124 people, 98 job postings. |
| 2026-09-23 | 4 | Shared schema v2 adds `lead_type` (proven_speaker / emerging_voice / featured / no_public_content). 8 emerging voices raised in priority: 4 to tier 1 (David Förster, Max Rieger, Nélson Rangel, Hiba Jamal) and 4 to tier 2 (Danny Burleigh and Lennart Scharmann were already tier 1). Split: 99 proven speakers, 16 emerging voices, 6 featured, 3 with no public content. |
| 2026-09-23 | 5 | Shared schema v3 adds `pronouns` (self-stated only, never inferred) and `sourced_via`. **Women-in-data sourcing (Step 2b):** 28 new people from PyLadies Berlin, Women in Big Data Berlin, Women Techmakers Berlin, the Women+ in Data/AI Festival, AWS Women's User Group, WomenTech Network and WiMLDS, plus new evidence for Katharine Jarmul. 3 people have self-stated pronouns. Added a line-up balance check to the outreach order and to `event-planning-template.md`. Totals: 156 companies, 152 people. Lithuania and Kuala Lumpur moved to schema v3 too (schema-only change). Backup: `berlin_dbt_companies.v4.json`. |
| 2026-10-01 | 6 | Location pass and LinkedIn pass, by the evidence rules in `../research/README.md`. Public pages placed 38 people: Meetup host and RSVP lists tied to the person, and recent in-person talks at Data Berlin and other Berlin events by people whose employer has a Berlin office. LinkedIn search results placed 9 more. Of the 47 placed, 42 are in Berlin and 5 elsewhere. 53 people are still unknown. |
| 2026-10-01 | 7 | Women-in-data pass from Meetup data and the Women on Snowflake user group page. 13 people added: 7 speakers from PyLadies Berlin, Women in Big Data Berlin and AWS Women's User Group Berlin, plus 6 organisers as connectors. Anastasiia Stefanska gained a talk. R-Ladies Berlin and Berlin WiMLDS are inactive, and the Women+ in Data/AI Festival is paused in 2025. |
| 2026-10-01 | 8 | Company pass from Data Berlin, open job boards (Greenhouse, Lever, Ashby, arbeitnow), HN Who is hiring, dbt Labs case studies and meetup line-ups. 11 companies added, for 168. 4 of them have a strong dbt signal: Superchat, Yazio, Flinn and Good Hood (nebenan.de). 8 companies raised to strong: SumUp, diconium, FlixMobility, Alpaca, PERGOLUX, Cosuno, Octopus Energy Group and Ratepay. People are unchanged. |
