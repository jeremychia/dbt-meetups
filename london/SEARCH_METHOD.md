# London: city notes

This file holds what is specific to London. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [London dbt Meetup](https://www.meetup.com/london-dbt-meetup/), data in `london_dbt_companies.json`
- **Region:** Greater London. Commuter towns are local for this chapter, so Oxford and Brighton count too.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-01)

| | Count |
|---|---|
| Companies | 104 |
| People | 134 |
| Tier 1 leads | 38 |
| First-time speakers (publish, no talk yet) | 11 |
| Proven speakers | 109 |
| Spoke at this chapter before | 33 |
| Based in the region | 99 |
| Based elsewhere | 6 |
| Location unknown | 29 |
| With a LinkedIn profile | 35 |
| Job ads mentioning dbt | 34 |
| Past chapter meetups | 22 |
<!-- at-a-glance:end -->

## 1. Where to look in London

### Meetups and conferences

- **[London Analytics Engineering Meetup](https://www.meetup.com/london-analytics-engineering-meetup/events/?type=past):** 27 events from 2022 to 2026. Every event lists speakers with their employer and talk title. This was the richest London source. The recruiter Cognify runs it.
- **[Data Engineers London](https://www.meetup.com/data-engineers-london/events/?type=past):** 15 events since 2023. Some are joint events with the [London Snowflake User Group](https://usergroups.snowflake.com/london/), which gave its organisers and one 2024 line-up.
- **Older events:** a 2022 analytics engineering meetup by [Burns Sheehan](https://www.burnssheehan.co.uk/events/data-meetup-analytics-engineering-the-life-cycle/s107469/), hosted at Dojo.
- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** individual speaker pages found through search gave the Virgin Media O2 talk.

### Company and consultancy blogs

- **[The Information Lab](https://www.theinformationlab.co.uk/sitemap-0.xml):** 15 dbt posts with named authors. Its sitemap lists every post, and each post's page-data file gives the author, job title and date. The Information Lab hosts the chapter.
- **Monzo:** the [Data @ Monzo Medium feed](https://medium.com/feed/data-monzo) had 8 posts, 2 about dbt. The [Monzo blog's data topic](https://monzo.com/blog/topic/data) had a 2026 data mesh post with three authors.
- **Wise:** the [Wise Engineering feed](https://medium.com/feed/wise-engineering) had a tech stack post that names dbt.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[Data + Women London](https://usergroups.tableau.com/data-women-london/):** the best source. It is a Tableau user group. Its 2024 and 2025 event pages list speakers with employers, including a dbt talk and a hands-on dbt lab in June 2025.
- **Panels at other meetups:** the Allies of Women in Data panels at the London Analytics Engineering Meetup, and the Data Engineers London International Women's Day panel.
- **[Women in Data UK podcast](https://womenindata.co.uk/):** the posts API (`womenindata.co.uk/wp-json/wp/v2/posts`) lists each episode with the guest's name and role. It gave Lauren Dixon (Chief Data Officer, FCA), Gemma Trailor (Analytics Manager, B&Q), Kinnari Ladha and Michelle Adebayo. The hosts, Karen Jean-Francois and Cecilia Oliveira, are recorded as connectors.
- **[PyLadies London](https://www.meetup.com/pyladieslondon/):** the [July 2025 meetup at OakNorth](https://www.meetup.com/pyladieslondon/events/308836457/) had a data mesh talk by Anitha, a senior data engineer. The page gives only the first name.
- **[WiDS London](https://www.widsworldwide.org/events/event/wids-london-university-of-greenwich/):** two 2024 upskill workshops. The pages name only the ambassadors, Abhigya Chetna and Samiya Khan, who are recorded as connectors.
- **Result:** 43 people are tagged `women_in_data_community`.

### Job ads

- **Built In London and a green-jobs board:** 3 ads at 2 companies, Infinite Lambda and Octopus Energy. None of the 3 search snippets showed the word dbt, so `dbt_mentioned_in_text` is null for all three.
- **Company job boards:** the open JSON boards at Greenhouse, Lever and Ashby, tried for about 100 London employers. 54 boards answered, and 22 had a London ad whose text has the word dbt. New companies that require dbt include Lendable, Multiverse, Trainline, Zego, Beamery, Kaluza, Marshmallow and ElevenLabs. The boards also confirmed London offices for Moneybox, Taptap Send, Voy, Dojo, Lawhive and Snowflake.
- **HN Who is hiring:** the Algolia API, queried once per monthly thread since January 2023 (45 threads) and filtered to comments with the word dbt. It gave 2 London ads, at Amazon and Google DeepMind.
- **[dbt Labs case studies](https://www.getdbt.com/llms-full-case-studies.txt):** this one file holds every case study as text. Four companies have a London headquarters: Secret Escapes, Plentific, LendInvest and Car & Classic. Each study names a data lead.
- **GitHub code search:** `filename:dbt_project.yml org:<org>` found public dbt projects at Octopus Energy ([dbt-intervals](https://github.com/octoenergy/dbt-intervals)) and Orchestra ([orchestra-blueprints](https://github.com/orchestra-hq/orchestra-blueprints)).
- **Meetup hosts:** gql2 past events of the London Snowflake User Group, Databricks London, Data Engineering London and The Friendly Data Meetup name the venue hosts. Dremio hosted a dbt talk at its London office. Theodo UK, MMC Ventures, Slalom, Sigma Computing and CFC Underwriting hosted or sponsored events.

### Chapter history and locations

- **Chapter history:** every named speaker in [`../enriched/london-dbt-meetup.json`](../enriched/london-dbt-meetup.json) was added as a person. That file holds 22 meetups, from 2019-04-04 to 2026-05-27. 33 people in the file have spoken at the chapter. Four people found by the research were already past speakers with newer talks: Gordon Curzon, Holly Foster, Pablo Fernandez and Ash Sultan.
- **GitHub profiles:** the company field ties a profile to the person, and the location field places them. Most of the 13 people placed from public pages came from GitHub. Four more came from recent in-person talks at an employer with a London office.
- **LinkedIn search results:** 12 people searched and 3 placed, all in London: [Gordon Curzon](https://www.linkedin.com/in/gordon-curzon-714a1713/), [Pearl Prakash](https://www.linkedin.com/in/pearl-prakash/) and [Christelle Xu](https://www.linkedin.com/in/christellexu/).

## 2. What didn't work here

- **Web search:** the session limit stopped the first run after 26 searches. About 40 direct page fetches covered the rest.
- **Medium:** HTTP 429 (too many requests) after two feeds. The Bumble, Just Eat, Skyscanner, Starling, Octopus Energy and ASOS blogs were not scanned.
- **No dbt posts:** the [Gousto](https://medium.com/feed/gousto-engineering-techbrunch) and [Deliveroo](https://deliveroo.engineering/feed.xml) blogs.
- **[Infinite Lambda blog](https://infinitelambda.com/wp-json/wp/v2/posts?search=dbt):** it has dbt posts, but its authors could not be placed in London.
- **[dbt developer blog authors page](https://docs.getdbt.com/blog/authors):** no confirmed London community authors.
- **[dbt Summit 2026 speaker list](https://www.getdbt.com/dbt-summit/speakers):** rendered by JavaScript, so a fetch returns nothing.
- **[Coalesce on the Road London 2025](https://www.getdbt.com/events/roadshow/coalesce-on-the-road-london):** the page returned 404.
- **[PyLadies London](https://www.meetup.com/pyladieslondon/), Data Science Festival and GDG Cloud London:** no dbt talks from 2024 onwards with full speaker names. PyLadies London has held no event since July 2025.
- **Inactive women-in-data groups:** [London WiMLDS](https://www.meetup.com/London-Women-in-Machine-Learning-and-Data-Science/) last met in October 2023 and [R-Ladies London](https://www.meetup.com/rladies-london/) in October 2022.
- **Women-in-tech groups with no data talks:** [Women Coding Community](https://www.meetup.com/women-coding-community/) (AI agents, Java, book clubs), [Ladies of Code](https://www.meetup.com/ladies-of-code-uk/), [Rise London Tech Ladies](https://www.meetup.com/we-rise/), [SuperWomen in Tech](https://www.meetup.com/sgi-superwomen-in-tech/) and Girlies in Tech London.
- **Women Techmakers and IWD at GDG London:** the [events API](https://gdg.community.dev/api/event_slim/for_chapter/995/?status=Completed&page_size=200) lists IWD 2024, IWD 2025 and a May 2026 evening. None had data talks. The IWD 2025 site did not respond.
- **[PyData London 2025 call for papers](https://cfp.pydata.org/london2025/speaker/):** no dbt or analytics engineering talks. The PyData London schedule is rendered by JavaScript.
- **[Women in Data UK meet-ups archive](https://womenindata.co.uk/category/meet-ups/):** it stops in 2020.
- **Job boards under the obvious name:** Octopus Energy, Checkout.com, Starling, Lyst, Depop, Gousto, Secret Escapes, Not On The High Street, Tails.com, Simply Business, RVU, Beauty Pie, Ocado, ClearScore and Huel have no open Greenhouse, Lever or Ashby board under that name. Wise, GoCardless, Tide, Wayve and Synthesia have boards, but no London ad mentions dbt.
- **HN keyword search:** a search for "dbt london" returns mostly unrelated comments. Query each Who is hiring thread instead.
- **GitHub code search:** no public dbt projects for Monzo, GoCardless, Deliveroo, Wise, the BBC, GOV.UK, the ONS, the Financial Times or Skyscanner. The Ministry of Justice has only a test project. The limit is about 10 calls a minute and other sessions share it, so many calls had to wait.
- **Meetup groups with no company hosts:** the London Apache Airflow group (mostly online) and Analytics.Club London (online job fairs).

## 3. Companies looked at

- **The host dominates:** 11 people work at The Information Lab, including the organiser Ed Hayter. 6 of the 11 first-time speakers work there too. Plan one speaker per company per event.
- **Proven speakers outnumber first-time speakers:** London has 11 first-time speakers against 104 proven speakers.
- **Cognify:** the recruiter runs the London Analytics Engineering Meetup, the richest source of London talks.

<!-- companies:start -->
102 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (57)</summary>

Amazon, Beamery, Biztory, Car & Classic, Cleo, Comcast (local presence not confirmed), Crisp (local presence not confirmed), Datatonic, dbt Labs, Depop (local presence not confirmed), Dojo, Dremio, ElevenLabs, Euno (local presence not confirmed), Farfetch (local presence not confirmed), Fishtown Analytics (local presence not confirmed), Freelance consultant (local presence not confirmed), Fresha, GoCardless, Growth Street (local presence not confirmed), Infinite Lambda, Kaluza, Lawhive, Lendable, LendInvest, Lightdash, Lyst, Marshmallow, Moneybox, Monzo, Multiverse, Octopus Energy, Orchestra, Paddle (local presence not confirmed), Paradime (local presence not confirmed), Plentific, Rittman Analytics (local presence not confirmed), RVU (local presence not confirmed), Sahaj Software, Sainsbury's, Secret Escapes, SELECT (local presence not confirmed), Simply Business (local presence not confirmed), Snowflake, Spectacles CI (local presence not confirmed), SYNQ, Tails.com (local presence not confirmed), Talan (local presence not confirmed), Taptap Send, Tesco, The Information Lab, Trainline, Virgin Media O2, Voy, VTS (local presence not confirmed), Wise, Zego

</details>

<details><summary><b>Some dbt signal</b> (14)</summary>

Checkout.com, Codat, Cognify, Compare the Market (local presence not confirmed), Count, Data Engineers London, Deliveroo, Gelato (local presence not confirmed), Google DeepMind, Not On The High Street (local presence not confirmed), Spotify, Starling Bank (local presence not confirmed), Zilch, Zopa

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

Moonpig

</details>

<details><summary><b>Not verified</b> (25)</summary>

Astrato Analytics, Baringa, Beauty Pie (local presence not confirmed), CFC Underwriting, Co-op, Day1Data (local presence not confirmed), Entain (local presence not confirmed), Global (local presence not confirmed), Gousto, HP Inc (local presence not confirmed), IAG (local presence not confirmed), John Lewis Partnership, Kubrick, Lloyds Banking Group, Medik8 (local presence not confirmed), MMC Ventures, Reward (local presence not confirmed), Sigma Computing, Slalom, Spark Foundry (local presence not confirmed), Tem (local presence not confirmed), Theodo UK, TXOdds (local presence not confirmed), Tyme Technologies (local presence not confirmed), Venatus (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (5)</summary>

B&Q (local presence not confirmed), Financial Conduct Authority, OakNorth, QuantumBlack (McKinsey) (local presence not confirmed), Women in Data UK

</details>

<details><summary><b>Blogs and sites scanned</b> (5)</summary>

- https://deliveroo.engineering/feed.xml
- https://medium.com/feed/data-monzo
- https://medium.com/feed/gousto-engineering-techbrunch
- https://medium.com/feed/wise-engineering
- https://www.theinformationlab.co.uk/sitemap-0.xml

</details>

<details><summary><b>Other sources checked</b> (28)</summary>

- [London Analytics Engineering Meetup (gql2)](https://www.meetup.com/london-analytics-engineering-meetup/events/?type=past)
- [Data Engineers London (gql2)](https://www.meetup.com/data-engineers-london/events/?type=past)
- [The Information Lab blog sitemap](https://www.theinformationlab.co.uk/sitemap-0.xml)
- [Data + Women London (Tableau User Group)](https://usergroups.tableau.com/data-women-london/)
- [Data @ Monzo Medium feed](https://medium.com/feed/data-monzo)
- [Monzo blog data topic](https://monzo.com/blog/topic/data)
- [Wise Engineering Medium feed](https://medium.com/feed/wise-engineering)
- [Gousto Medium feed](https://medium.com/feed/gousto-engineering-techbrunch) (nothing useful)
- [Deliveroo engineering feed](https://deliveroo.engineering/feed.xml) (nothing useful)
- [Other Medium feeds (Bumble, Just Eat, Skyscanner, Starling, Octopus, ASOS and more)](https://medium.com/feed/bumble-tech) (nothing useful)
- [dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers)
- [Coalesce on the Road London 2025](https://www.getdbt.com/events/roadshow/coalesce-on-the-road-london) (nothing useful)
- [London Snowflake User Group](https://usergroups.snowflake.com/london/)
- [PyData London 2025 CfP](https://cfp.pydata.org/london2025/speaker/) (nothing useful)
- [PyLadies London, Data Science Festival, GDG Cloud London (gql2)](https://www.meetup.com/pyladieslondon/) (nothing useful)
- [Women in Data UK meet-ups](https://womenindata.co.uk/category/meet-ups/) (nothing useful)
- [dbt developer blog authors](https://docs.getdbt.com/blog/authors) (nothing useful)
- [Infinite Lambda blog API](https://infinitelambda.com/wp-json/wp/v2/posts?search=dbt) (nothing useful)
- [Burns Sheehan data meetup](https://www.burnssheehan.co.uk/events/data-meetup-analytics-engineering-the-life-cycle/s107469/)
- [Meetup gql2 groupSearch near London (women-in-data queries)](https://www.meetup.com/gql2#groupSearch-london-wid)
- [PyLadies London (Meetup gql2 past events)](https://www.meetup.com/pyladieslondon/events/?type=past)
- [London WiMLDS (Meetup gql2)](https://www.meetup.com/London-Women-in-Machine-Learning-and-Data-Science/) (nothing useful)
- [R-Ladies London (Meetup gql2)](https://www.meetup.com/rladies-london/) (nothing useful)
- [Women Coding Community (Meetup gql2)](https://www.meetup.com/women-coding-community/) (nothing useful)
- [Ladies of Code UK, Rise (London Tech Ladies), SuperWomen in Tech, Girlies in Tech (Meetup gql2)](https://www.meetup.com/ladies-of-code-uk/) (nothing useful)
- [Women in Data UK posts API](https://womenindata.co.uk/wp-json/wp/v2/posts?per_page=30)
- [WiDS London event pages](https://www.widsworldwide.org/events/event/wids-london-university-of-greenwich/)
- [GDG London events API (Women Techmakers and IWD)](https://gdg.community.dev/api/event_slim/for_chapter/995/?status=Completed&page_size=200) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Antonia Badarau, Irina Mugford and Massimo Frangiamore (Monzo):** co-wrote ["A meshy approach to Data"](https://monzo.com/blog/a-meshy-approach-to-data) (2026-04). It covers a dbt project of 12,000+ models used by 100+ teams.
  - **Jake Curtis (Monzo):** wrote about [incremental dbt models over 3bn+ events a day](https://medium.com/data-monzo/how-monzo-uses-incremental-modelling-to-handle-billions-of-events-every-day-45b2bc9ebe89) (2024-05).
  - **Trea McElhone (The Information Lab):** wrote ["dbt Fusion Explained"](https://www.theinformationlab.co.uk/community/blog/dbt-fusion-explained) (2026-04).
  - **Louisa O'Brien (The Information Lab):** wrote ["Right Test, Right Place"](https://www.theinformationlab.co.uk/community/blog/right-test-right-place-how-dbt-can-improve-tableau-development), on dbt tests for Tableau work (2025-02).
  - **Harriet Owen (The Information Lab):** wrote ["Inside dbt Wizard"](https://www.theinformationlab.co.uk/community/blog/inside-dbt-wizard-the-agent-built-for-analytics-engineers) (2026-06).
- **Anchor speakers:**
  - **Gordon Curzon and Melissa Simpson (Virgin Media O2):** [moving 300 dbt users to Fusion](https://www.getdbt.com/dbt-summit/speakers/melissa-simpson), dbt Summit 2026. Gordon Curzon has spoken at the chapter before.
  - **Carmen Mardiros (Sahaj Software):** [practical AI for data engineering](https://www.meetup.com/data-engineers-london/events/313209661/), including dbt with Claude Code, Data Engineers London, 2026-02.
  - **Katie Wiedmann and Priscila Fischer (GoCardless):** ["Monolithic to Mesh - dbt at GoCardless"](https://www.meetup.com/london-analytics-engineering-meetup/events/300711591/), 2024-06.
  - **Toby Henley Smith (Moneybox) and Rakhee Modha-Lobo (Starling Bank):** both spoke at the [London Analytics Engineering Meetup in 2026-02](https://www.meetup.com/london-analytics-engineering-meetup/events/312843994/).
- **Connectors:**
  - **Anna Aleshko and Luke Ashe-Browne:** organisers of [Data Engineers London](https://www.meetup.com/data-engineers-london/).
  - **Piers Batchelor and Tony Burton:** leads of the [London Snowflake User Group](https://usergroups.snowflake.com/london/).
  - **Kerine Taylor, Hannah Bartholomew and Lydia Wren:** leaders of [Data + Women London](https://usergroups.tableau.com/data-women-london/).
  - **Cognify:** runs the [London Analytics Engineering Meetup](https://www.meetup.com/london-analytics-engineering-meetup/) and the [Stacked Pathways](https://cognifysearch.com/stackedpathways/) mentoring scheme. Its organisers are not named on the listings.

## 5. Before outreach

- [ ] **Check unknown locations.** 17 people have no known location. They include Melissa Simpson, Konrad Maliszewski, Richard Persaud, Lucy Kendrick and Sarah Levy, whose LinkedIn result was too vague to place.
- [ ] **Check tier-1 people raised by the rule.** Milon James (Wise) is tier 1, but dbt is one line in a tech stack post.
- [ ] **dbt Labs staff are labelled.** Kshitij Aranke and Richard Persaud are tier 1 and work there. They can speak, but check the line-up has practitioners first.
- [ ] **Check current employers.** Talks from 2022 and 2023 give the employer at the time. Andrea Salvati, Naomi Johnson, Katie Hindson, Danny Jones, Madalina Ghita and Andrew Jones may have moved.
- [ ] **Check a possible duplicate.** Jean Dupuis may be the "Jean D." who gave a later dbt Fusion talk.
- [ ] **Fill missing talk titles.** Several 2026 London Analytics Engineering Meetup listings name speakers but no title.
- [ ] **Check who is already booked.** Compare leads with the chapter's upcoming events.

## 6. Next run

- **Sources to try first:**
  - **Medium:** the Bumble, Just Eat, Skyscanner, Starling, Octopus Energy and ASOS blogs, for first-time speakers. Space the requests out.
  - **Meetups:** new events of the London Analytics Engineering Meetup, Data Engineers London and Data + Women London.
  - **Blogs:** new posts on The Information Lab and Monzo blogs, Infinite Lambda authors, Datatonic, and dbt Labs case studies of London companies.
  - **dbt Summit 2026 speaker pages:** through the getdbt.com sitemap, for more London employers.
  - **Job ads:** only 3 were found. Try `site:` searches on Lever, Greenhouse and Ashby with "dbt London".
  - **Women-in-data sources:** new Women in Data UK podcast episodes through the posts API, and new Data + Women London events. Find Anitha's full name through OakNorth. The IWD 2025 GDG London site did not respond, so retry it.
  - **Beyond the host:** look past The Information Lab for first-time speakers, so the line-up does not depend on the host.
- **People to locate:** 17 people have no known location, and 96 are still `not_searched` on LinkedIn. Start with the unknown locations.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `london/london_dbt_companies.json`, the London dbt Meetup, `../enriched/london-dbt-meetup.json` and the region Greater London, with Oxford and Brighton counted as local.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build from one research run: 75 companies, 120 people, 3 job ads at 2 companies, 22 past meetups. 33 people had spoken at the chapter. Tiers: 38 tier 1, 55 tier 2, 19 tier 3, 7 connectors, 1 organiser. Lead types: 104 proven speakers, 11 emerging voices, 1 featured, 4 with no public content. |
| 2026-10-01 | 1 | Location pass from public pages: 13 people placed, 9 in the region and 4 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 12 people searched, 3 placed in London. 21 people are still unknown. |
| 2026-10-01 | 2 | Women-in-data pass: the Women in Data UK podcast, PyLadies London and WiDS London. 9 people added: 5 speakers and podcast guests, plus 4 connectors. London WiMLDS and R-Ladies London are inactive. Women Coding Community, Ladies of Code, Rise and GDG London had no data talks. |
| 2026-10-01 | 3 | Company pass from fetches: company job boards, HN Who is hiring, the dbt Labs case-study file, GitHub code search and Meetup hosts. Companies went from 79 to 104, and job ads from 3 to 34. 15 new companies have a strong dbt signal. Secret Escapes, Octopus Energy, Taptap Send and Voy were raised to strong, and 7 companies now have a confirmed London office. 5 data leads named in case studies were added as featured people. |
