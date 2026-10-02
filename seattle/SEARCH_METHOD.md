# Seattle: city notes

This file holds what is specific to Seattle. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Seattle dbt Meetup](https://www.meetup.com/seattle-dbt-meetup/), data in `seattle_dbt_companies.json`
- **Region:** the Seattle metro. Seattle, Bellevue, Redmond, Bothell and Mercer Island count. Commuter towns are local for this chapter, so Olympia and Mount Vernon count too.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 4, 2026-10-01)

| | Count |
|---|---|
| Companies | 122 |
| People | 97 |
| Tier 1 leads | 2 |
| First-time speakers (publish, no talk yet) | 2 |
| Proven speakers | 81 |
| Spoke at this chapter before | 16 |
| Based in the region | 65 |
| Based elsewhere | 9 |
| Location unknown | 23 |
| With a LinkedIn profile | 42 |
| Job ads mentioning dbt | 81 |
| Past chapter meetups | 7 |
<!-- at-a-glance:end -->

## 1. Where to look in Seattle

The first build covered conferences, other local meetups, women-in-data communities, company blogs and job ads. Leads are scored by the [central scoring rules](../research/README.md#3-scoring-rules).

### Chapter history and conferences

- **Past chapter speakers:** every named speaker in `../enriched/seattle-dbt-meetup.json`, with the talk. 7 meetups, from 2023-04-27 to 2026-05-07, gave 16 people who have spoken at the chapter.
- **[dbt Summit 2026 speakers directory](https://www.getdbt.com/dbt-summit/speakers):** the best source. It is static HTML with every speaker and company, so filtering by Seattle employers is cheap. Speaker pages give session titles but not cities.
- **[Airflow Summit 2025](https://airflowsummit.org/sessions/2025/):** held in Seattle. Several talks cover dbt, semantic layers and data quality, but most speakers are not from Seattle.
- **[PyData Seattle 2025](https://cfp.pydata.org/seattle2025/speaker/):** full speaker bios, but few analytics engineering talks. The [organisers page](https://pydata.org/seattle2025/organizers) names the PyLadies and WiMLDS leads.

### Local meetups and user groups

- **[Seattle Data, AI & Security](https://www.seattledataai.org/speakers):** a large speaker roster with LinkedIn links. Most speakers are from Microsoft, executive or security roles.
- **[Data Engineer Things Seattle](https://www.dataengineerthings.org/team):** the Seattle lead, plus speakers taken from search summaries of its Meetup event pages. The group is moving to Luma.
- **[Seattle Tableau User Group](https://usergroups.tableau.com/seattle-tableau-user-group/) (SeaTUG):** the pages on the Bevy event platform are fully readable, with speakers, hosts and LinkedIn links.
- **[Snowflake User Groups Seattle](https://usergroups.snowflake.com/seattle-2/):** organiser and host names, with LinkedIn links on the Bevy pages. Most events are virtual partner talks.
- **[MotherDuck events](https://motherduck.com/events/past/):** confirmed a MotherDuck Seattle office that hosts events, and a dbt talk at one of them.

### Women-in-data communities

People were taken only from each community's own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.

- **[WiDS Puget Sound 2026](https://www.widspugetsound.org/2026-conference):** WiDS means Women in Data Science. The richest women-in-data source, with speakers, panellists and organisers. It names data engineers and analytics leaders at Expedia, Amazon, Pfizer and JumpCloud. The page needs a browser, because it renders empty for a plain fetch.
- **[WiDS Puget Sound 2025 recap](https://www.widsworldwide.org/get-inspired/blog/celebrating-connection-and-innovation-the-2025-wids-puget-sound-conference/):** names only, with no employers.
- **[Seattle PyLadies](https://www.meetup.com/seattle-pyladies/):** monthly open source nights in Bellevue, run with PyData Seattle, Seattle Spark + AI and GDG Bellevue. Databricks sponsors most of them, and line-ups include speakers of all genders. The [Playing with Data mini-conference](https://www.meetup.com/seattle-pyladies/events/301012521/) in May 2024 gave Fabiana Clemente (YData), Evis Drenova (Neosync), and Jasmine Wang and Weston Pace (LanceDB). The [April 2025 night](https://www.meetup.com/seattle-pyladies/events/305396007/) gave Ryan Boyd (MotherDuck) and Tim Hesterberg (Instacart). Other talks gave Denny Lee and Ginger Holt (Databricks), Gavita Regunath (Advancing Analytics), Saurabh Sarkar (Chicory AI) and Riya Joshi. The organisers Mae LaPresta (Google) and Hemie Choi are connectors.
- **[R-Ladies Seattle](https://www.meetup.com/rladies-seattle/):** the [R Pirate Day](https://www.meetup.com/rladies-seattle/events/302526506/) in September 2024 gave data visualisation and NLP workshops by Kim Dill-McFarland, Micheleen Harris and Simran Saxena. Kim Dill-McFarland hosts most events. A joint talk with PyLadies gave Courtney Armour (UW School of Medicine). An [R Consortium interview](https://r-consortium.org/posts/diving-into-r-with-isabella-velasquez-perspectives-from-r-ladies-seattle/) gave one more co-organiser.
- **[WiMLDS Seattle](https://www.meetup.com/seattle-women-in-machine-learning-and-data-science/):** Women in Machine Learning and Data Science, chaired by Micheleen Harris. It co-runs events with PyLadies Seattle. A January 2026 tutorial gave Rachel Wagner-Kaiser on dataset curation.
- **[Power BI Women](https://www.meetup.com/power-bi-women/):** an online Power BI group registered in Bellevue, with organisers outside Washington. It gave Jackie Kiadii (organiser, Atlanta) and Allison Kennedy. Most event pages give only a first name for the speaker.

### Company blogs, news and job ads

- **[dbt Developer Blog](https://docs.getdbt.com/blog/authors/nate-sooter):** a 2022 post on founding Smartsheet's analytics engineering team.
- **[GeekWire](https://www.geekwire.com/2025/seattle-startup-gable-lands-20m-to-coordinate-data-changes-between-teams/):** good for confirming a startup is in Seattle (SDF Labs, Gable).
- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt&location=Seattle%2C%20Washington%2C%20United%20States), logged out:** 250 ads listed and checked, and 48 mention the whole word "dbt".
- **Applicant tracking systems:** `site:` searches on [Lever](https://jobs.lever.co), [Greenhouse](https://job-boards.greenhouse.io) and [Ashby](https://jobs.ashbyhq.com) added 17 more ads. Examples are Rover, AllTrails, Anthropic, Gusto, Plaid and Thumbtack.
- **[HN Who is hiring](https://hn.algolia.com/api/v1/search?query=dbt&tags=comment):** the Algolia API searched each monthly thread since January 2023 for dbt, one call per thread. Posts were kept when the header names the Seattle area and the text uses the whole word dbt. Gave Adora AI (on site in Seattle) as a new strong lead, plus Delfina and DigitalOcean.
- **Company job boards (open JSON):** the Greenhouse, Lever and Ashby APIs return every open ad with its full text. About 40 employers were checked, and ads located in the Seattle area that use the word dbt were kept. Seattle office ads at Plaid raised it to strong. Ads at Anthropic, Headway, Brex and Snowflake Bellevue added evidence to existing records.

### Locations

- **Location pass (2026-10-01):** page fetches placed 18 people, 16 in the region and 2 outside. The Meetup `gql2` endpoint gave the profile city of each chapter event's hosts and RSVPs, and placed most past chapter speakers. GitHub profiles, speaker bios and recent in-person talks at an employer with a Seattle office gave the rest.
- **LinkedIn pass (2026-10-01):** LinkedIn search results placed 5 people, 1 in the region and 4 outside. No LinkedIn page was opened.

## 2. What didn't work here

- **Seattle Data, AI & Security:** gives names but no talk titles or dates, so its speakers are hard to rank.
- **meetup.com pages:** not opened in the first build, so the chapter's own organisers were not captured. The [Seattle Data Meetup Group](https://www.meetup.com/seattle-data-engineering-meetup-group/events/?type=past) (last event November 2023) and [seattle-daml](https://www.meetup.com/seattle-daml/) were not opened either.
- **[PyLadies Seattle site](https://seattle.pyladies.com/):** lists placeholder organisers. Use the [Meetup group](https://www.meetup.com/seattle-pyladies/) instead.
- **Women-focused Meetup groups with no data talks:** [GDG Bellevue](https://www.meetup.com/bellevue-gdg/) only cross-posts the PyLadies events. [Ladies in Seattle Tech](https://www.meetup.com/ladies-in-seattle-tech/) runs repeated AI product demos. [Power Platform Women](https://www.meetup.com/power-platform-women/) has no events.
- **[Women in Big Data](https://www.womeninbigdata.org/?s=seattle):** no Seattle chapter events since 2024.
- **Data + Women:** no Seattle chapter was found.
- **Women-in-data groups not checked in depth:** Women Who Code Seattle, Ada Developers Academy and [Women in Analytics](https://www.womeninanalytics.com/speakers-bureau).
- **Seattle company blogs:** publish almost nothing about dbt. [Zillow Tech Hub](https://medium.com/feed/zillow-tech-hub) has had no posts since February 2021. [Expedia Group Tech](https://medium.com/feed/expedia-group-tech) is active but has no dbt posts. Redfin and Remitly returned nothing.
- **Grouped web searches** for Seattle consumer brands (Starbucks, REI, Alaska Airlines, Zillow and others) returned only generic dbt content.
- **Eastside job ads:** no Bellevue, Redmond or Kirkland ads were confirmed, because the location filter was not applied.
- **GitHub code search for `dbt_project.yml`:** found nothing in 16 Seattle orgs, among them zillow, redfin, Nordstrom, expedia, remitly, smartsheet, AllTrails and roverdotcom.
- **Meetup venue scan:** Seattle Spark+AI and Seattle-DAML events since 2024 were held at Databricks Bellevue, Snowflake Bellevue, Blueprint Technologies, Microsoft and GitHub. None of the events mentions dbt.
- **Job boards with no open JSON:** most large Seattle employers use Workday or their own sites. Zillow, Redfin, Nordstrom, Expedia, Remitly, Avalara, Highspot, Porch and Wizards of the Coast answered none of the three APIs. Smartsheet, OfferUp, Amperity, Textio and Tanium had no ad that uses the word dbt.
- **HN posts skipped:** posts that name dbt only as an investor or as a product integration, and posts with no company name, were not counted as dbt users.

## 3. Companies looked at

- **dbt Labs has a Seattle team**, from the purchase of SDF Labs. The staff are labelled.
- **Locations from a head office.** Many first-build cities come from the employer's Seattle or Bellevue head office, not from the person. Priya Tanwar, Nadine Bruxel and Nate Sooter are examples.
- **Tier 1 is small.** Only 2 people meet the strict rule, so most strong leads sit in tier 2.

<!-- companies:start -->
121 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (26)</summary>

Adora AI, AllTrails, Anthropic, Axon, Cambia Health Solutions, dbt Labs (Seattle / ex-SDF Labs), DigitalOcean, DocuSign, Gusto, Haus, Headway, IT Labs, Microsoft, MotherDuck, Nordstrom, Okta (Auth0) (local presence not confirmed), Plaid, Redfin, Rover.com, Russell Investments, Seattle dbt Meetup, Smartsheet, Snowflake, WEX, Weyerhaeuser, Wizards of the Coast

</details>

<details><summary><b>Some dbt signal</b> (32)</summary>

Agoda, Amazon / AWS, Aritzia, Brex, Databricks, Delfina, DoorDash, Expedia Group, Gable, Golden Analytics, Hasbro, Haus Analytics, Jobgether, Mercury, Metropolis, Otter, phData (local presence not confirmed), QXO, RentSpree, Seattle Storm, Slalom, SmithRx, SoFi, Storable, Superhuman, Tableau / Salesforce, TechWish, Thumbtack, Valorem Reply, Weights & Biases, Whatnot, Zillow

</details>

<details><summary><b>Not verified</b> (52)</summary>

Adobe (local presence not confirmed), AgentSync (local presence not confirmed), Alaska Airlines, Amazon (local presence not confirmed), Amazon Web Services (local presence not confirmed), AMD (local presence not confirmed), Amperity, Analytic Endeavors (local presence not confirmed), Astronomer (local presence not confirmed), Babylist (local presence not confirmed), BECU, Confluent (local presence not confirmed), Consultant (local presence not confirmed), Convoy (local presence not confirmed), Data Engineer Things Seattle, Data Literacy (local presence not confirmed), Disney (local presence not confirmed), Diversity in Data Science (local presence not confirmed), Genesis Computing (local presence not confirmed), Google Cloud (local presence not confirmed), JumpCloud (local presence not confirmed), LanceDB (local presence not confirmed), LaunchDarkly (local presence not confirmed), Lincoln Financial (local presence not confirmed), Monaghan Medical Corporation (local presence not confirmed), Netflix (local presence not confirmed), Northwell Health (local presence not confirmed), OfferUp, Onehouse (local presence not confirmed), Outreach, Perceptive Analytics (local presence not confirmed), Pfizer (local presence not confirmed), Porch, Push.ai (local presence not confirmed), PyData Seattle, QBiz, Inc. (local presence not confirmed), Rad Power Bikes (local presence not confirmed), REI, Remitly, Rover, Seattle Data Guy (local presence not confirmed), Seattle Data, AI & Security, Seattle Tableau User Group (SeaTUG), Skagit Valley College (local presence not confirmed), Snowflake User Groups Seattle, Starbucks, T-Mobile, Textio, Unify Consulting, University of Washington iSchool (local presence not confirmed), WiDS Puget Sound / Diversity in Data Science, Zulily (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (11)</summary>

Advancing Analytics (local presence not confirmed), Chicory AI (local presence not confirmed), Google (local presence not confirmed), Instacart (local presence not confirmed), Neosync (local presence not confirmed), Power BI Women (local presence not confirmed), PyLadies Seattle, R-Ladies Seattle, University of Washington School of Medicine, WiMLDS Seattle, YData (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (21)</summary>

- https://amperity.github.io/
- https://cfp.pydata.org/seattle2025/speaker/
- https://docs.getdbt.com/blog
- https://docs.getdbt.com/blog/authors/nate-sooter
- https://medium.com/feed/expedia-group-tech
- https://medium.com/feed/redfin-engineering
- https://medium.com/feed/remitly-engineering
- https://medium.com/feed/zillow-tech-hub
- https://motherduck.com/events/
- https://motherduck.com/events/past/
- https://pydata.org/seattle2025/organizers
- https://usergroups.snowflake.com/seattle-2/
- https://www.dataengineerthings.org/team
- https://www.getdbt.com/dbt-summit/speakers
- https://www.meetup.com/seattle-data-engineering-meetup-group/events/?type=past
- https://www.runtime.news/how-t-mobile-uses-snowflake-and-databricks/
- https://www.seattledataai.org/events/
- https://www.seattledataai.org/speakers
- https://www.widspugetsound.org/2026-conference
- https://www.widsworldwide.org/get-inspired/blog/celebrating-connection-and-innovation-the-2025-wids-puget-sound-conference/
- https://www.zillow.com/tech/feed/

</details>

<details><summary><b>Other sources checked</b> (53)</summary>

- [Seattle dbt Meetup (meetup.com)](https://www.meetup.com/seattle-dbt-meetup/) (nothing useful)
- [Data Engineer Things Seattle](https://www.dataengineerthings.org/team)
- [Seattle Data, AI & Security speakers page](https://www.seattledataai.org/speakers)
- [Seattle Data, AI & Security events](https://www.seattledataai.org/events/) (nothing useful)
- [PyData Seattle 2025 speakers (pretalx)](https://cfp.pydata.org/seattle2025/speaker/)
- [PyData Seattle 2025 organizers](https://pydata.org/seattle2025/organizers)
- [Snowflake User Groups Seattle](https://usergroups.snowflake.com/events/details/snowflake-seattle-presents-wed-mar-12-seattle-user-group-meetup-hands-on-lab-community-app-build/)
- [Seattle Tableau User Group](https://usergroups.tableau.com/seattle-tableau-user-group/)
- [WiDS Puget Sound 2026 conference](https://www.widspugetsound.org/2026-conference)
- [WiDS Puget Sound 2025 recap (WiDS Worldwide blog)](https://www.widsworldwide.org/get-inspired/blog/celebrating-connection-and-innovation-the-2025-wids-puget-sound-conference/)
- [WiDS Puget Sound 2025 Luma page](https://luma.com/widsps2025) (nothing useful)
- [PyLadies Seattle site](https://seattle.pyladies.com/) (nothing useful)
- [R-Ladies Seattle (R Consortium interview)](https://r-consortium.org/posts/diving-into-r-with-isabella-velasquez-perspectives-from-r-ladies-seattle/)
- [Airflow Summit 2025 sessions (held in Seattle)](https://airflowsummit.org/sessions/2025/)
- [Ben Rogojan / Seattle Data Guy](https://airflowsummit.org/speakers/ben-rogojan/)
- [seattle-daml meetup](https://www.meetup.com/seattle-daml/) (nothing useful)
- [Databricks user group Seattle](https://usergroups.databricks.com/events/) (nothing useful)
- [Seattle Apache Airflow meetup](https://airflow.apache.org/meetups/) (nothing useful)
- [Data + Women Seattle (Tableau)](https://usergroups.tableau.com/chapters/) (nothing useful)
- [Seattle WiMLDS (meetup.com)](https://www.meetup.com/seattle-women-in-machine-learning-and-data-science/) (nothing useful)
- [Women Who Code Seattle archive / Ada Developers Academy / Women in Analytics](https://www.womeninanalytics.com/speakers-bureau) (nothing useful)
- [Zillow Tech Hub RSS (Medium)](https://medium.com/feed/zillow-tech-hub) (nothing useful)
- [Zillow tech feed](https://www.zillow.com/tech/feed/) (nothing useful)
- [Expedia Group Tech RSS](https://medium.com/feed/expedia-group-tech) (nothing useful)
- [Redfin Engineering RSS](https://medium.com/feed/redfin-engineering) (nothing useful)
- [Remitly Engineering RSS](https://medium.com/feed/remitly-engineering) (nothing useful)
- [dbt Summit 2026 speakers directory](https://www.getdbt.com/dbt-summit/speakers)
- [PyData Seattle 2025 schedule (pretalx JSON)](https://cfp.pydata.org/seattle2025/schedule/export/schedule.json) (nothing useful)
- [Snowflake User Groups Seattle](https://usergroups.snowflake.com/seattle-2/)
- [Seattle Data Meetup Group (Onehouse) past events](https://www.meetup.com/seattle-data-engineering-meetup-group/events/?type=past) (nothing useful)
- [Data Engineer Things Seattle, Jul 2025 event](https://www.meetup.com/data-engineer-things-seattle-meetup/events/308773412/) (nothing useful)
- [Airflow Summit 2025 sessions (held in Seattle)](https://airflowsummit.org/sessions/2025/) (nothing useful)
- [MotherDuck events (upcoming + past)](https://motherduck.com/events/past/)
- [dbt Developer Blog author page (Nate Sooter)](https://docs.getdbt.com/blog/authors/nate-sooter)
- [GeekWire (SDF Labs, Gable)](https://www.geekwire.com/2025/seattle-startup-gable-lands-20m-to-coordinate-data-changes-between-teams/)
- [Runtime newsletter (T-Mobile)](https://www.runtime.news/how-t-mobile-uses-snowflake-and-databricks/) (nothing useful)
- [LinkedIn Jobs guest API](https://www.linkedin.com/jobs/search?keywords=dbt&location=Seattle%2C%20Washington%2C%20United%20States) (nothing useful)
- [WebSearch site:jobs.lever.co dbt Seattle](https://jobs.lever.co)
- [WebSearch site:job-boards.greenhouse.io dbt Seattle](https://job-boards.greenhouse.io)
- [WebSearch site:jobs.ashbyhq.com dbt Seattle](https://jobs.ashbyhq.com)
- [WebSearch analytics engineer dbt Seattle](https://www.builtinseattle.com/jobs/data-analytics/data-engineering) (nothing useful)
- [WebSearch site:jobs.lever.co analytics engineer dbt Bellevue/Redmond/Kirkland](https://jobs.lever.co) (nothing useful)
- [WebSearch site:job-boards.greenhouse.io analytics engineer dbt Seattle, WA](https://job-boards.greenhouse.io)
- [LinkedIn Jobs guest API (keywords=dbt, Seattle WA)](https://www.linkedin.com/jobs/search?keywords=dbt&location=Seattle%2C%20Washington%2C%20United%20States)
- [Meetup gql2 groupSearch near Seattle (women-in-data queries)](https://www.meetup.com/gql2#seattle-wid)
- [Seattle PyLadies (Meetup)](https://www.meetup.com/seattle-pyladies/)
- [R-Ladies Seattle (Meetup)](https://www.meetup.com/rladies-seattle/)
- [WiMLDS Seattle (Meetup gql2)](https://www.meetup.com/seattle-women-in-machine-learning-and-data-science/events/)
- [Power BI Women (Meetup)](https://www.meetup.com/power-bi-women/)
- [GDG Bellevue / Women Techmakers Seattle](https://www.meetup.com/bellevue-gdg/) (nothing useful)
- [Ladies in Seattle Tech](https://www.meetup.com/ladies-in-seattle-tech/) (nothing useful)
- [Power Platform Women](https://www.meetup.com/power-platform-women/) (nothing useful)
- [Women in Big Data (Seattle)](https://www.womeninbigdata.org/?s=seattle) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers at this chapter:**
  - **Nate Sooter**, Smartsheet. Wrote about founding Smartsheet's first analytics engineering team (2022): [dbt Developer Blog](https://docs.getdbt.com/blog/founding-an-analytics-engineering-team-smartsheet). Publishes about dbt, with no talk on record.
  - **Maggie Stark**, Staff Data Engineer, Astronomer, based in Seattle. Airflow Summit 2025 talk on data quality, contracts, and soft versus hard failures: [session](https://airflowsummit.org/sessions/2025/orchestrating-data-quality-quality-data-brought-to-you-by-airflow/).
  - **Catherine Nelson**, author of *Software Engineering for Data Scientists*. Talks at PyData Seattle and WiDS Puget Sound on moving from notebooks to production code: [WiDS Puget Sound 2026](https://www.widspugetsound.org/2026-conference).
  - **Stephanie Chen**, product analytics leader, Expedia Group. WiDS Puget Sound 2026 talk on agentic AI at Expedia: [conference page](https://www.widspugetsound.org/2026-conference).
- **Anchor speakers:**
  - **Priya Tanwar** and **Nadine Bruxel**, Nordstrom. dbt Summit 2026 talk on dbt governance as an advantage for AI: [session](https://www.getdbt.com/dbt-summit/agenda/governed-by-default-how-data-teams-at-nordstrom-turn-dbt-governance-into-an-ai-advantage).
  - **Bishal Gupta** (3 chapter talks) and **Sundar Subramanyam** (2 chapter talks), DocuSign. Topics include moving stored procedures to dbt and AI-written unit tests: [March 2025 event](https://www.meetup.com/seattle-dbt-meetup/events/305524780/).
  - **Ryan Bordo**, Netflix, based in Redmond. Talk on running dbt Core inside Spark and Maestro at Netflix: [May 2026 event](https://www.meetup.com/seattle-dbt-meetup/events/314108748/).
  - **Chad Sanderson**, Gable. Known for data contracts. Gable is a vendor, so ask for a practitioner-style talk: [panel](https://www.gable.ai/blog/panel-shift-left-across-the-data-lifecycle--data-contracts-transformations-observability-and-catalogs-prukalpa-sankar-tristan-handy-barr-moses-chad-sanderson-shift-left-data-conference-2025).
- **Connectors:**
  - **Eloisa Elias T** founded PyData Seattle and chairs PyLadies Seattle. The best route into Seattle's women-in-data networks: [PyData organisers](https://pydata.org/seattle2025/organizers).
  - **Saransh Arora** leads Data Engineer Things Seattle, a natural co-host for a joint night: [team page](https://www.dataengineerthings.org/team).
  - **Padma Ayala** runs Seattle Data, AI & Security, which claims 15,000+ members: [site](https://www.seattledataai.org/speakers).
  - **Karrie Cardiff** and **Russell Spangler** co-lead SeaTUG: [group page](https://usergroups.tableau.com/seattle-tableau-user-group/).
  - **Angela Harney** hosts the Snowflake user group labs at Snowflake's Bellevue office: [event](https://usergroups.snowflake.com/events/details/snowflake-seattle-presents-wed-mar-12-seattle-user-group-meetup-hands-on-lab-community-app-build/).

## 5. Before outreach

- [ ] **Confirm locations taken from a head office.** Priya Tanwar, Nadine Bruxel, Nate Sooter and Vikas Ranjan are placed by the employer's office only.
- [ ] **Confirm the 12 unknown locations.** Brandyn Lee (AgentSync) and Irina Virnik (JumpCloud) are very likely in Seattle, from truncated LinkedIn results. Andres Astorga Espriella may be in Mexico City and at Qbiz rather than independent.
- [ ] **Check the weak location calls.** Wendy Grus and Mira Winkel were placed by a name match to a chapter member only.
- [ ] **Skip or re-rank people outside the region.** Pooja Crahen is in New York, Ben Rogojan in Denver, Mitesh Mangaonkar in Austin and Britton Stamper in San Francisco. Bernardo Dionisi is in Durham, North Carolina, Ivan Perez Avellaneda in Plattsburgh and Dipankar Mazumdar in Canada. Ben Rogojan, the "Seattle Data Guy", has moved to Denver, according to a podcast title.
- [ ] **Confirm current roles** for people whose evidence is old: Nate Sooter (2022), Deepak Konidena (Zillow, before 2024) and Vikas Ranjan (T-Mobile, 2023).
- [ ] **Check the line-up has practitioners first.** Elias DeFaria, Lukas Schulte, William Weld, Alexander Bogdanowicz and Wolfram Shulte work at dbt Labs and are labelled.

## 6. Next run

- **Sources to try first:**
  - **LinkedIn pass:** 24 tier-1 and tier-2 people are still `not_searched`.
  - **Meetup `gql2`:** pull the chapter's organisers.
  - **GitHub user search** (`dbt location:Seattle`) for first-time speakers with public dbt work. It was the best source of first-time speakers in Atlanta, and Seattle has only 2.
  - **New events:** WiDS Puget Sound, SeaTUG and Snowflake Seattle events since `metadata.generated_at`.
  - **Women-in-data groups not yet checked:** Ada Developers Academy, Women in Analytics, Girl Develop It Seattle/Tacoma and Girls in Tech Seattle. Women Who Code closed in 2024.
  - **Power BI Women:** most speakers are named by first name only. Open the event pages in a browser to find surnames and employers.
  - **Eastside job ads** (Bellevue, Redmond, Kirkland): re-run the LinkedIn Jobs guest scan with a working location filter, plus Lever, Greenhouse and Ashby `site:` searches.
- **People to locate:** the 12 unknown locations in section 5, starting with Brandyn Lee and Irina Virnik.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `seattle/seattle_dbt_companies.json`, the chapter `seattle-dbt-meetup`, `../enriched/seattle-dbt-meetup.json` and the region "the Seattle metro (Seattle, Bellevue, Redmond and nearby), with commuter towns such as Olympia and Mount Vernon". Budget about 25 web searches.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build: dbt Summit 2026, Airflow Summit 2025 and PyData Seattle 2025, local meetups and user groups, WiDS Puget Sound and other women-in-data communities, company blogs, a LinkedIn Jobs scan and ATS searches. Past chapter speakers added from `../enriched/seattle-dbt-meetup.json`. 110 companies (49 on the watchlist), 79 people, 65 job ads at 44 companies, 7 past meetups. Split: 64 proven speakers, 2 emerging voices, 13 featured. Tiers: 2 tier 1, 40 tier 2, 22 tier 3, 15 connectors. 16 people had already spoken at the chapter. |
| 2026-10-01 | 2 | Location pass: 18 people placed from Meetup host and RSVP profiles, GitHub, speaker bios and recent in-person talks, 16 in the region and 2 outside. |
| 2026-10-01 | 2 | LinkedIn pass: 5 people placed from LinkedIn search results, 1 in the region and 4 outside. 12 people are still unknown. |
| 2026-10-01 | 3 | Women-in-data pass beyond WiDS Puget Sound, with fetches only: 18 people added from Seattle PyLadies, R-Ladies Seattle, WiMLDS Seattle and Power BI Women, and new talks added for Micheleen Harris and Weston Pace. 11 companies added. 9 women-focused communities checked. |
| 2026-10-01 | 4 | Company pass with fetches only: HN Who is hiring, company job boards, GitHub code search and Meetup venues. 120 to 122 companies. Adora AI added with a strong dbt signal, and Delfina added. Plaid raised to strong. Job ads 65 to 81. |
