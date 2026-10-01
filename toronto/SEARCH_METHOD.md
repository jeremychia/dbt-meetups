# Toronto: city notes

This file holds what is specific to Toronto. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Toronto dbt Meetup](https://www.meetup.com/toronto-dbt-meetup/), data in `toronto_dbt_companies.json`
- **Region:** the Greater Toronto Area, including the Waterloo region.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 4, 2026-10-01)

| | Count |
|---|---|
| Companies | 112 |
| People | 76 |
| Tier 1 leads | 4 |
| First-time speakers (publish, no talk yet) | 8 |
| Proven speakers | 52 |
| Spoke at this chapter before | 4 |
| Based in the region | 68 |
| Based elsewhere | 2 |
| Location unknown | 6 |
| With a LinkedIn profile | 16 |
| Job ads mentioning dbt | 83 |
| Past chapter meetups | 4 |
<!-- at-a-glance:end -->

## 1. Where to look in Toronto

Two research runs built the file. The first build (2026-09-24) used about 18 web searches and a job ad scan. The extension (2026-10-01) used about 20 web searches, then direct page fetches once the session limit was reached. Leads are scored by the [central scoring rules](../research/README.md#3-scoring-rules).

### User groups and meetups

- **[Snowflake Toronto User Group](https://usergroups.snowflake.com/toronto/):** the best source of 2025 and 2026 local speakers and organisers. The Bevy pages fetch cleanly. The [Meetup copy of the group](https://www.meetup.com/snowflake-usergroup-toronto/) added 11 events, including 2026 expert tables.
- **[Toronto Databricks User Group](https://usergroups.databricks.com/toronto-databricks-user-group/):** July 2026 speakers. dbt Labs is a local sponsor.
- **[Toronto Modern Data Stack](https://www.meetup.com/toronto-modern-data/):** the city's 2022 to 2024 dbt speaker pool. The group is now dormant and has rebranded as Toronto Enterprise AI. Read it with Meetup `gql2`, and re-check the speakers' current roles.
- **Meetup `gql2` with plain `curl`:** one `groupSearch` call by latitude and longitude listed 25 Toronto and Waterloo groups. The ones that yielded were:
  - **[Toronto Apache Airflow Meetup](https://www.meetup.com/toronto-apache-airflow-meetup/):** three speakers at an in-person event in May 2025.
  - **[Toronto Apache Kafka Ecosystem Meetup](https://www.meetup.com/toronto-kafka/):** Geotab data platform talks in September 2026.
  - **[Toronto Data Engineering Meetup with ClickHouse](https://luma.com/8p8unbnw):** 2026 speakers from FiveOneFour and Evidence.
- **[Data Engineers in Toronto](https://www.meetup.com/data-engineers-in-toronto/):** organiser only. The group runs online talks centred on Microsoft Fabric.
- **Chapter history:** every named speaker in [`../enriched/toronto-dbt-meetup.json`](../enriched/toronto-dbt-meetup.json) was added as a person. That file holds 4 meetups, from 2025-09-17 to 2026-08-19. The first was a social with no talks. 4 people in the file have spoken at the chapter. A speaker listed by first name only, "Michelle" (November 2025), was skipped.

### Conferences

- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** matching Toronto employer names against the page text found only KOHO, with Célia Bru and Gabriel Gambacorta.
- **[Databricks Data + AI World Tour Toronto 2025](https://dataaisummit.databricks.com/flow/db/wt25yyz/scheduler/page/catalog):** customer speakers from CIBC, Manulife, Intact, Apotex and Canadian Tire, mostly senior leaders.
- **[Generative AI Summit Toronto](https://world.aiacceleratorinstitute.com/location/toronto/speakers):** data leaders from Wealthsimple, RBC, TD and Interac, on AI topics.

### Company blogs

- **[Loblaw Digital on Medium](https://medium.com/loblaw-digital):** the best Toronto company blog for dbt authors. A post on generating dbt documentation with LLMs, and a Data as a Service series, name 7 authors. Medium blocks direct fetches, so the feeds were read through `api.rss2json.com`, which returns a publication's last 10 posts with full text.
- **[Shopify Data](https://medium.com/data-shopify):** dbt posts from 2020 only.
- **GitHub user search:** one person, Hubert Chan (Granum).

### Women-in-data communities

Speakers come from women-focused groups' own events. Nobody's gender is recorded or guessed. 12 people are tagged `women_in_data_community`.

- **[PyLadies Toronto](https://www.meetup.com/PyLadies-Toronto/):** the organiser and 2 hosts are recorded as connectors. The group is back in person from April 2026. Its [April lightning-talk night](https://www.meetup.com/pyladies-toronto/events/314245447/) had a City of Toronto collisions data pipeline on Airflow, and a talk on moving into data analytics and BI. The speakers are not named.
- **[AWS User Group Women in Tech Ontario](https://www.meetup.com/aws-women-in-tech-user-group-ontario/):** the organiser is recorded as a connector. The group runs online talks. Its [May 2026 talk](https://www.meetup.com/aws-women-in-tech-user-group-ontario/events/314598442/) was by Soumil Shah (Zeta Global), on writing data into more than 10,000 Amazon S3 tables.
- **Women Techmakers Toronto:** the ambassadors post on a small Meetup group, [Beyond Networking - Women in Tech](https://www.meetup.com/north-york-wisdom-business-network-meetup-group/), and register on Luma. The [May 2026 Luma page](https://luma.com/hcub806p) names 4 hosts, recorded as connectors. Their events are for networking, with no talks.
- **[R-Ladies Toronto](https://www.meetup.com/R-Ladies-Toronto/):** one lightning-talk speaker.
- **[WiDS Toronto @ Dataiku](https://www.widsworldwide.org/events/event/wids-toronto-dataiku/):** names event ambassadors only, not panellists.

### Job ads and locations

- **LinkedIn Jobs (first build):** a logged-out scan for "dbt" in the Toronto area. Up to 150 ads were checked for the whole word "dbt". 70 ads at 52 companies mention it.
- **Company job boards (open JSON):** the Greenhouse, Lever and Ashby APIs return every open ad with its full text. About 40 Toronto employers were tried. Super.com ads say the data team are long-time dbt users, which raised it to strong. Instacart has remote Analytics Engineer roles open to Ontario that require dbt. 1Password, PointClickCare (Mississauga) and Docebo list dbt among other tools. Cohere lists it as a plus.
- **[HN Who is hiring](https://hn.algolia.com/api/v1/search?query=dbt%20canada&tags=comment):** the Algolia API, searched for dbt with Toronto, Ontario, Canada or Waterloo. Posts were kept when they place the role in Toronto. Gave Borrowell and Squaredance, both from 2023. Most Canadian posts are remote with no Toronto office.
- **Meetup venues:** the Toronto Modern Data Stack meetup, now Toronto Enterprise AI, was hosted by Cohere in February 2024 and by Georgian with Dagster in October 2024.
- **Location pass (page fetches):** 6 people placed under the [central location rules](../research/README.md#6-location-rules), 4 in the region and 2 elsewhere.
  - **Daria Sukhareva:** a Tableau Public profile linked from kwwhat.com.
  - **Archie Sarre Wood:** a GitHub profile.
  - **Nicole Kim and Jessie Lamontagne:** in-person chapter talks in August 2026, at a Toronto-based employer.
  - **Nicolas Joseph (Portland) and John Miner (Providence):** each person's own GitHub and Sessionize profiles.
- **LinkedIn pass (search results only):** 1 person searched. The result for Josh Harris gave Toronto, but it may describe the company rather than the person. The profile link is recorded and the location stays unknown.

## 2. What didn't work here

- **[Toronto Data Professionals Community](https://www.meetup.com/toronto-data-professionals-meetup-group/):** one intro-to-dbt talk, by a speaker from outside the region.
- **Other local groups:** [Waterloo Data Science and Data Engineering](https://www.meetup.com/waterloo-data-science/), ODSC, Analytics.Club and Toronto AI groups had no dbt or analytics engineering talks since 2024.
- **JavaScript pages:** the [Coalesce 2025 speaker pages](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/speakers) and the [Snowflake World Tour Toronto 2026 speakers](https://www.snowflake.com/en/world-tour/toronto/speakers/) are rendered by JavaScript.
- **[Big Data & Analytics Summit Canada](https://bigdatasummitcanada.com/all-speakers/):** not fetched.
- **Blogs with no dbt posts:** [Shopify Engineering](https://shopify.engineering/), [Wealthsimple Engineering](https://engineering.wealthsimple.com/), [Faire](https://craft.faire.com/all?topic=engineering), and the latest 10 posts of the [Wealthsimple Medium feed](https://medium.com/wealthsimple).
- **Medium:** blocks `curl` and direct fetches. rss2json rate-limits after about 10 new feeds.
- **[dev.to](https://dev.to/t/dbt) and GitHub location search:** job-seeker portfolios, not speakers, and not worth the calls.
- **Women-in-data groups:** [PyData Toronto](https://www.meetup.com/pydata-toronto/), Toronto Women's Data Group and Women in Big Data Toronto had no local speaker events since mid-2024.
- **More women-in-data groups with no people:**
  - **[Toronto WiMLDS](https://www.meetup.com/Toronto-Women-in-Machine-Learning-and-Data-Science/):** last met in March 2022.
  - **[Women in Big Data Toronto](https://www.meetup.com/women-in-big-data-toronto/):** last met on Meetup in June 2023.
  - **GDG Toronto and GDG Cloud Toronto:** their IWD pages for 2024 to 2026 name only the organisers. This includes the 2025 event run with Women Techmakers Toronto.
  - **[WiDS Toronto](https://www.widsworldwide.org/events/event/wids-toronto/):** an online event in June 2023 with no speakers listed.
  - **[QueerTech Toronto](https://www.meetup.com/queertech-toronto/):** runs career and networking events, with no data talks.
  - **Not on Meetup:** She Loves Data, Lesbians Who Tech, Women in AI and Data + Women have no Toronto group.
- **Web search:** the session limit stopped the extension after about 20 searches.
- **GitHub code and repository search:** no public dbt project at Wealthsimple, KOHO, Wattpad, 1Password, Cohere, Loblaw, Geotab, ecobee or Faire.
- **[dbt Labs case studies](https://www.getdbt.com/sitemap-0.xml):** none for a Toronto company. Fullscript is in Ottawa and Symend is in Calgary.
- **Company job boards with no Toronto dbt ads:** Faire, Mejuri, Geotab, KOHO, Clearco, Dialpad, Wattpad, Waabi, Float, League, Granum, Achievers, PolicyMe, Wave and Ritual. Rootly, Ada, Borrowell, Questrade, ecobee, Clio, FreshBooks, Top Hat and Vena have no open Greenhouse, Lever or Ashby board. The Greenhouse slug `super` belongs to a different company. Super.com is on Ashby.

## 3. Companies looked at

- **Leaders, not practitioners:** the Databricks World Tour and AI summit agendas give senior bank and insurer leaders. These suit panels better than technical talks, and most sit in tier 3.
- **Loblaw Digital** supplied all 7 first-time speakers added in the extension. The posts are from 2023, and the authors' titles were not stated.
- **Vendor speakers:** Snowflake, Astronomer, FiveOneFour, Evidence and Artemis staff fill several slots.
- **KOHO is based in Toronto.** Célia Bru, Gabriel Gambacorta and Ian Whitestone also appear in the Montreal file.

<!-- companies:start -->
111 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (8)</summary>

Instacart (local presence not confirmed), KOHO Financial, Secoda, SELECT, Shopify, Super.com, Toronto Modern Data Stack (now 'Toronto Enterprise AI'), Wealthsimple

</details>

<details><summary><b>Some dbt signal</b> (62)</summary>

1Password, Agoda, Akkodis, AnswerLayer, Artemis (local presence not confirmed), Autodesk, Aviva Canada, Bayview Asset Management, LLC, Big Viking Games, Borrowell, CGI, CI Financial, Clio, Clutch, Coforge, commonsku, CoStar Group, Direct IT Recruiting Inc., Docebo, eBay, ecobee, Enterprise Solutions Inc., FacilityOS, Felix, Financeit, Generac, Granum (local presence not confirmed), HelloFresh, Homebase, Kake, Lakeview Loan Servicing, LLC., Loblaw Digital, Lyft, MaintainX, McKesson, Millennium Software and Staffing Inc, Movable Ink, Pacific Smoke International Inc., Passage, PointClickCare, Princeton IT Services, Inc, Propel, Propel Holdings, RAVL, RBC, Relay, Scotiabank, Sienna Senior Living, Slalom, Spaulding Ridge, Spectrum Health Care (SHC), Squaredance, Tactable, TekRek, Thomson Reuters, Thumbtack, Toptal, Toronto Databricks User Group, Venterra Realty, Wave Financial, ZoomInfo, Zynga

</details>

<details><summary><b>dbt as a nice-to-have</b> (4)</summary>

Archetype Consulting Inc., Cohere, Snowflake Toronto User Group, Zeta Global (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (34)</summary>

Apotex, Astronomer (local presence not confirmed), Canadian Tire Corporation, CBC, CIBC, Cineplex, Compass Data + AI (local presence not confirmed), Create Music Group (local presence not confirmed), Data Engineers in Toronto, Databricks (local presence not confirmed), Dataiku (local presence not confirmed), dbt Labs (local presence not confirmed), Evidence (local presence not confirmed), Faire (local presence not confirmed), FiveOneFour (local presence not confirmed), Georgian, Geotab, Intact Financial Corporation, Interac, kWwhat (local presence not confirmed), Manulife, Mejuri, MHS Analytics Inc. (local presence not confirmed), Moneris, New Stadium, OneEleven, Polar Labs, Rootly, Sanofi, Snowflake, TD Bank, Toronto Apache Airflow Meetup, Viafoura (local presence not confirmed), Women in Big Data Toronto

</details>

<details><summary><b>Uses a different stack</b> (3)</summary>

AWS User Group Women in Tech Ontario, PyLadies Toronto, Women Techmakers Toronto

</details>

<details><summary><b>Blogs and sites scanned</b> (7)</summary>

- https://craft.faire.com/all?topic=engineering
- https://engineering.wealthsimple.com/
- https://medium.com/loblaw-digital
- https://shopify.engineering/
- https://usergroups.snowflake.com/toronto/
- https://www.secoda.co/authors/lindsay-murphy
- https://www.womeninbigdata.org/event/women-in-big-data-toronto-lead-with-data/

</details>

<details><summary><b>Other sources checked</b> (41)</summary>

- [Toronto dbt Meetup past events (Meetup gql2)](https://www.meetup.com/toronto-dbt-meetup/)
- [dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers)
- [Coalesce 2025 speakers (Cvent)](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/speakers) (nothing useful)
- [Toronto Modern Data Stack (Meetup gql2)](https://www.meetup.com/toronto-modern-data/)
- [Snowflake Toronto User Group (Bevy + Meetup)](https://usergroups.snowflake.com/toronto/)
- [Toronto Databricks User Group](https://usergroups.databricks.com/toronto-databricks-user-group/)
- [Data Engineers in Toronto (Meetup gql2)](https://www.meetup.com/data-engineers-in-toronto/)
- [PyData Toronto / PyLadies Toronto / R-Ladies Toronto / Toronto Women's Data Group / Women in Big Data Toronto (Meetup gql2)](https://www.meetup.com/pydata-toronto/) (nothing useful)
- [WiDS Toronto @ Dataiku](https://www.widsworldwide.org/events/event/wids-toronto-dataiku/)
- [Shopify Engineering blog](https://shopify.engineering/) (nothing useful)
- [Wealthsimple Engineering blog](https://engineering.wealthsimple.com/) (nothing useful)
- [Faire The Craft](https://craft.faire.com/all?topic=engineering) (nothing useful)
- [Toronto Data Professionals Community](https://torontodpc.ca/) (nothing useful)
- [Big Data & Analytics Summit Canada](https://bigdatasummitcanada.com/all-speakers/) (nothing useful)
- [LinkedIn Jobs guest API (keywords=dbt, Toronto-area)](https://www.linkedin.com/jobs/search?keywords=dbt)
- [Toronto Snowflake User Group (Meetup gql2)](https://www.meetup.com/snowflake-usergroup-toronto/)
- [Toronto Apache Airflow Meetup (Meetup gql2)](https://www.meetup.com/toronto-apache-airflow-meetup/)
- [Toronto Apache Kafka Ecosystem Meetup (Meetup gql2)](https://www.meetup.com/toronto-kafka/)
- [Toronto Data Engineering Meetup with ClickHouse (Luma)](https://luma.com/8p8unbnw)
- [Databricks Data + AI World Tour Toronto 2025](https://dataaisummit.databricks.com/flow/db/wt25yyz/scheduler/page/catalog)
- [Generative AI Summit Toronto speakers](https://world.aiacceleratorinstitute.com/location/toronto/speakers)
- [Loblaw Digital Medium (rss2json)](https://medium.com/loblaw-digital)
- [Shopify Data Medium and shopify.engineering atom feed](https://medium.com/data-shopify)
- [Wealthsimple and Faire Medium feeds](https://medium.com/wealthsimple) (nothing useful)
- [Toronto Data Professionals Community (Meetup gql2)](https://www.meetup.com/toronto-data-professionals-meetup-group/) (nothing useful)
- [PyLadies / R-Ladies / AWS Women in Tech Ontario (Meetup gql2)](https://www.meetup.com/PyLadies-Toronto/)
- [Waterloo Data Science and Data Engineering, Toronto Data Engineering and Cloud, ODSC, Analytics.Club, Toronto AI groups (Meetup gql2)](https://www.meetup.com/waterloo-data-science/) (nothing useful)
- [Snowflake World Tour Toronto 2026 speakers](https://www.snowflake.com/en/world-tour/toronto/speakers/) (nothing useful)
- [dev.to tag dbt / GitHub user search by location](https://dev.to/t/dbt) (nothing useful)
- [Meetup gql2 groupSearch near Toronto (women-in-data queries)](https://www.meetup.com/gql2)
- [AWS User Group Women in Tech Ontario past events (Meetup gql2)](https://www.meetup.com/aws-women-in-tech-user-group-ontario/events/314598442/)
- [PyLadies Toronto April 2026 lightning talks](https://www.meetup.com/pyladies-toronto/events/314245447/)
- [Women Techmakers Toronto: Beyond Networking (Luma)](https://luma.com/hcub806p)
- [Toronto WiMLDS (Meetup gql2)](https://www.meetup.com/Toronto-Women-in-Machine-Learning-and-Data-Science/) (nothing useful)
- [Women in Big Data Toronto (Meetup gql2)](https://www.meetup.com/women-in-big-data-toronto/) (nothing useful)
- [GDG Toronto events API and IWD pages](https://gdg.community.dev/api/event_slim/for_chapter/959/?status=Completed&page_size=300) (nothing useful)
- [GDG Cloud Toronto events API and IWD 2024](https://gdg.community.dev/api/event_slim/for_chapter/259/?status=Completed&page_size=300) (nothing useful)
- [WiDS Toronto (online, 2023)](https://www.widsworldwide.org/events/event/wids-toronto/) (nothing useful)
- [QueerTech Toronto (Meetup gql2)](https://www.meetup.com/queertech-toronto/) (nothing useful)
- [Women in STEM/Finance career Meetup Group](https://www.meetup.com/women-in-stem-finance-career-meetup-group/) (nothing useful)
- [She Loves Data, Lesbians Who Tech, Women in AI and Data + Women Toronto on Meetup](https://www.meetup.com/she-loves-data-toronto/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Joseph Jing (Loblaw Digital):** lead author of ["Leveraging LLMs to generate AI driven dbt documentation"](https://medium.com/loblaw-digital/leveraging-llms-to-generate-ai-driven-dbt-documentation-c4735faa6ca5) (2023-11).
  - **Indrani Gorti (Loblaw Digital):** co-wrote the dbt documentation post and the [Data as a Service series](https://medium.com/loblaw-digital/part-2-data-as-a-service-simplifying-real-time-data-ingestion-and-delivery-ef7cb22e144d).
  - **Colin Barber (Loblaw Digital):** lead author of the [Data as a Service series](https://medium.com/loblaw-digital/part-2-data-as-a-service-simplifying-real-time-data-ingestion-and-delivery-ef7cb22e144d), on real-time BigQuery pipelines (2023-09).
  - **Lindsay Murphy (Secoda):** wrote ["Implementing Data Contracts with dbt and across the MDS"](https://www.secoda.co/blog/implementing-data-contracts-with-dbt). Also a connector: co-ran Toronto Modern Data Stack in 2022 and 2023.
- **Anchor speakers:**
  - **Célia Bru and Gabriel Gambacorta (KOHO Financial):** ["Before the agents: what self-serve analytics actually needs"](https://www.getdbt.com/dbt-summit/speakers/celia-bru), dbt Summit 2026.
  - **Ian Whitestone (SELECT):** ["Proven methods for optimizing your dbt project"](https://c.select.dev/blog/proven-methods-for-optimizing-your-dbt-project-dbt-coalesce-2023), Coalesce 2023. Attended the Snowflake Toronto User Group in person in July 2026.
  - **Xiao Ma and Wenyang Liu (Geotab):** [data platform talks](https://www.meetup.com/toronto-kafka/events/316272838/) at the Toronto Kafka meetup, September 2026.
  - **Alvira Narshidani (Scotia Global Asset Management):** led a [BI and AI storytelling table](https://www.meetup.com/snowflake-usergroup-toronto/events/315505233/) at the Snowflake Toronto User Group, July 2026. One of few non-vendor practitioners on recent agendas.
- **Connectors:**
  - **Eddy Zulkifly:** [Toronto dbt Meetup](https://www.meetup.com/toronto-dbt-meetup/) organiser.
  - **Augusto Rosa (Archetype Consulting) and Ryan Ovas (Polar Labs):** organisers of the [Snowflake Toronto User Group](https://usergroups.snowflake.com/toronto/).
  - **Kevin Poulton (Databricks):** leads the [Toronto Databricks User Group](https://usergroups.databricks.com/toronto-databricks-user-group/) organiser team.
  - **Jill Cates:** organiser of [PyLadies Toronto](https://www.meetup.com/PyLadies-Toronto/).
  - **Vijayanirmala Gopal:** organiser of [AWS User Group Women in Tech Ontario](https://www.meetup.com/aws-women-in-tech-user-group-ontario/).
  - **Michael Olafusi (MHS Analytics):** organiser of [Data Engineers in Toronto](https://www.meetup.com/data-engineers-in-toronto/).

## 5. Before outreach

- [ ] **Check "in region" calls.** 62 people are marked in the region, but only 4 of those calls come from the location pass. Most came from a local event or the employer's head office during research.
- [ ] **Check unknown locations.** 5 people: Josh Harris, Josh Gray, Constance Martineau, Amanda Milberg and Jacqueline Kuo.
- [ ] **Check Gabriel Gambacorta.** No title was captured, and Toronto is assumed from KOHO's head office.
- [ ] **Check tier-1 people raised by the rule.** Toronto has only 4 tier-1 people. Samara Xiang reached tier 1 by the rule, but the post is about machine learning experiments, not dbt.
- [ ] **Check current roles** for Loblaw Digital authors and Toronto Modern Data Stack speakers from 2022 and 2023.
- [ ] **Coordinate with the Montreal chapter** on Célia Bru, Gabriel Gambacorta and Ian Whitestone.
- [ ] **Check who is already booked.** Nicole Kim, Jessie Lamontagne, Josh Harris and Daria Sukhareva spoke in 2026.
- [ ] **Check the line-up has practitioners first.** Muneeb Master works at dbt Labs and is labelled.

## 6. Next run

- **Sources to try first:**
  - **Medium feeds:** Ritual, Wattpad, KOHO, League, Super.com, Clio, Infostrux and the dbt tag feed. Use rss2json and space the calls out.
  - **User groups:** new events of the Snowflake Toronto and Databricks Toronto user groups, and Toronto data groups through Meetup `gql2` `groupSearch`, with `curl`.
  - **Job ads:** refresh with `site:` searches on Lever, Greenhouse and Ashby for dbt Toronto. The 70 ads date from 2026-09-24.
  - **Pages not read yet:** Coalesce 2025 speakers (needs a browser), Snowflake World Tour Toronto 2026, Day of Data Toronto 2026, Big Data & Analytics Summit Canada and dbt Summit speaker pages.
  - **PyLadies Toronto:** ask the organisers for the April 2026 lightning-talk speakers. The talks on the City of Toronto collisions pipeline and on moving into BI are good fits.
  - **Women-in-data panels with no published names:** the Women in Big Data Toronto "Lead with Data" panel (March 2025) and the GDG Toronto IWD 2025 panel. Ask the organisers for the panellists.
  - **Waterloo:** no Waterloo group had dbt talks, so try Waterloo company blogs.
- **People to locate:** 66 people are still `not_searched` on LinkedIn. Start with tier 1 and tier 2, and the 5 unknown locations.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `toronto/toronto_dbt_companies.json`, the chapter `toronto-dbt-meetup`, `../enriched/toronto-dbt-meetup.json` and the region "the Greater Toronto Area, including the Waterloo region". Budget about 25 web searches.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build from one research run and a LinkedIn Jobs scan: 84 companies, 31 people, 70 job ads at 52 companies, 4 past meetups. Tiers: 2 tier 1, 11 tier 2, 10 tier 3, 8 connectors. Lead types: 24 proven speakers, 1 emerging voice, 6 featured. |
| 2026-10-01 | 2 | Extension run: 38 people and 19 companies added, giving 69 people and 103 companies. 7 new emerging voices, all Loblaw Digital authors. Tiers: 4 tier 1, 22 tier 2, 33 tier 3, 10 connectors. |
| 2026-10-01 | 2 | Location pass from public pages: 6 people placed, 4 in the region and 2 elsewhere. |
| 2026-10-01 | 2 | LinkedIn pass from search results: 1 person searched; the profile link was recorded but the location stays unknown. 5 people are still unknown. |
| 2026-10-01 | 3 | Women-in-data pass: AWS User Group Women in Tech Ontario, PyLadies Toronto and Women Techmakers Toronto. 7 new people: 1 speaker, and 6 organisers as connectors. |
| 2026-10-01 | 4 | Company pass with fetches only: HN Who is hiring, company job boards, dbt Labs case studies, GitHub code and repository search, and Meetup venues. 105 to 112 companies. 7 added: Instacart with a strong dbt signal, and 1Password, PointClickCare, Borrowell, Squaredance, Cohere and Georgian. Super.com raised from weak to strong. Job ads added at Wealthsimple and Docebo. |
