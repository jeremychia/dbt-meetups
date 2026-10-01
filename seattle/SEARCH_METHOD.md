# Seattle dbt search: method, lessons and replication prompt

This file goes with `seattle_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in the Seattle metro who could **speak at** (or attend) the [Seattle dbt Meetup](https://www.meetup.com/seattle-dbt-meetup/), and the local companies that use dbt.
- **Region:** the Seattle metro. Seattle, Bellevue, Redmond, Bothell and Mercer Island count. Commuter towns are local for this chapter, so Olympia and Mount Vernon count too.

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 109 |
| People | 79 |
| Tier 1 leads | 2 |
| First-time speakers (publish, no talk yet) | 2 |
| Proven speakers | 64 |
| Spoke at this chapter before | 16 |
| Based in the region | 60 |
| Based elsewhere | 7 |
| Location unknown | 12 |
| With a LinkedIn profile | 25 |
| Job ads mentioning dbt | 65 |
| Past chapter meetups | 7 |
<!-- at-a-glance:end -->

## 1. How the search was done

The first build covered conferences, other local meetups, women-in-data communities, company blogs and job ads. Scoring follows [`../berlin_planning/SEARCH_METHOD.md`](../berlin_planning/SEARCH_METHOD.md) §1 Step 6.

### Step 1: Chapter history

- **What was added:** every named speaker in `../enriched/seattle-dbt-meetup.json`, with their talk.
- **Range:** 7 meetups, from 2023-04-27 to 2026-05-07.
- **Yield:** 16 people who have spoken at the chapter.

### Step 2: Conferences

- **[dbt Summit 2026 speakers directory](https://www.getdbt.com/dbt-summit/speakers):** the best source. It is static HTML with every speaker and company. Speaker pages give session titles but not cities.
- **[Airflow Summit 2025](https://airflowsummit.org/sessions/2025/):** it was held in Seattle. Several talks cover dbt, semantic layers and data quality, but most speakers are not from Seattle.
- **[PyData Seattle 2025](https://cfp.pydata.org/seattle2025/speaker/):** full speaker bios, but few analytics engineering talks. Its [organisers page](https://pydata.org/seattle2025/organizers) names the PyLadies and WiMLDS leads.

### Step 3: Other local meetups

- **[Seattle Data, AI & Security](https://www.seattledataai.org/speakers):** a large speaker roster with LinkedIn links. It has no talk titles or dates, and most speakers are from Microsoft, executive or security roles.
- **[Data Engineer Things Seattle](https://www.dataengineerthings.org/team):** the Seattle lead, plus speakers taken from search summaries of its Meetup event pages. The group is moving to Luma.
- **[Seattle Tableau User Group](https://usergroups.tableau.com/seattle-tableau-user-group/) (SeaTUG):** its pages on the Bevy event platform are fully readable, with speakers, hosts and LinkedIn links.
- **[Snowflake User Groups Seattle](https://usergroups.snowflake.com/seattle-2/):** organiser and host names. Most events are virtual partner talks.
- **[MotherDuck events](https://motherduck.com/events/past/):** confirmed a MotherDuck Seattle office that hosts events, and a dbt talk at one of them.
- **Not opened:** the [Seattle Data Meetup Group](https://www.meetup.com/seattle-data-engineering-meetup-group/events/?type=past) (last event November 2023) and [seattle-daml](https://www.meetup.com/seattle-daml/).

### Step 4: Women-in-data communities

People were taken only from each community's own events. Nobody's gender is recorded.

- **[WiDS Puget Sound 2026](https://www.widspugetsound.org/2026-conference):** WiDS means Women in Data Science. The richest source, with speakers, panellists and organisers. The page needs a browser, because it renders empty for a plain fetch.
- **[WiDS Puget Sound 2025 recap](https://www.widsworldwide.org/get-inspired/blog/celebrating-connection-and-innovation-the-2025-wids-puget-sound-conference/):** names only, with no employers.
- **[R-Ladies Seattle](https://r-consortium.org/posts/diving-into-r-with-isabella-velasquez-perspectives-from-r-ladies-seattle/):** one co-organiser, from an interview.
- **Weak or empty:** the [PyLadies Seattle site](https://seattle.pyladies.com/) lists placeholder organisers. No Seattle chapter of Data + Women was found.
- **Not checked in depth:** Women Who Code Seattle, Ada Developers Academy and [Women in Analytics](https://www.womeninanalytics.com/speakers-bureau).

### Step 5: Company blogs and news

- **[dbt Developer Blog](https://docs.getdbt.com/blog/authors/nate-sooter):** a 2022 post on founding Smartsheet's analytics engineering team.
- **[GeekWire](https://www.geekwire.com/2025/seattle-startup-gable-lands-20m-to-coordinate-data-changes-between-teams/):** good for confirming a startup is in Seattle (SDF Labs, Gable).
- **Medium feeds:** [Zillow Tech Hub](https://medium.com/feed/zillow-tech-hub) has had no posts since February 2021. [Expedia Group Tech](https://medium.com/feed/expedia-group-tech) is active but has no dbt posts. Redfin and Remitly returned nothing.
- **Grouped web searches** for Seattle consumer brands (Starbucks, REI, Alaska Airlines, Zillow and others) returned only generic dbt content.

### Step 6: Job ads

- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt&location=Seattle%2C%20Washington%2C%20United%20States), logged out:** 250 ads listed and checked, and 48 mention the whole word "dbt".
- **ATS searches:** an ATS is an applicant tracking system that hosts a company's job ads. `site:` searches on [Lever](https://jobs.lever.co), [Greenhouse](https://job-boards.greenhouse.io) and [Ashby](https://jobs.ashbyhq.com) added 17 more. Examples are Rover, AllTrails, Anthropic, Gusto, Plaid and Thumbtack.
- **Eastside:** no Bellevue, Redmond or Kirkland ads were confirmed, because the location filter was not applied.

### Step 7: Location and LinkedIn passes (2026-10-01)

- **Page fetches:** 18 people placed, 16 in the region and 2 outside.
  - The Meetup `gql2` endpoint gave the profile city of each chapter event's hosts and RSVPs.
  - GitHub profiles, speaker bios and recent in-person talks at an employer with a Seattle office gave the rest.
- **LinkedIn search results:** 5 people placed, 1 in the region and 4 outside. No LinkedIn page was opened.
- **Still unknown:** 12 people.

## 2. What we learnt

- **Sources that worked:**
  - **The dbt Summit speakers directory** lists every speaker and company in static HTML. Filtering by Seattle employers is cheap.
  - **WiDS Puget Sound** is the strongest women-in-data source. It names data engineers and analytics leaders at Expedia, Amazon, Pfizer and JumpCloud.
  - **Bevy pages** (Tableau and Snowflake user groups) name speakers, hosts and organisers, with LinkedIn links.
  - **Meetup `gql2` RSVPs** placed most past chapter speakers.
- **Sources that didn't:**
  - **Seattle company blogs** publish almost nothing about dbt. Zillow's is dormant, and Redfin's and Remitly's feeds were empty.
  - **Seattle Data, AI & Security** gives names but no talk titles or dates, so its speakers are hard to rank.
  - **meetup.com pages** were not opened in the first build, so the chapter's own organisers were not captured.
- **Watch out for:**
  - **Tier 1 is small.** Only 2 people meet the strict rule: a local or unknown location plus a dbt item from 2024 onwards. Most strong leads sit in tier 2.
  - **Locations from a head office.** Many first-build cities come from the employer's Seattle or Bellevue head office, not from the person. Priya Tanwar, Nadine Bruxel and Nate Sooter are examples.
  - **dbt Labs has a Seattle team**, from its purchase of SDF Labs. Its staff are labelled in the cockpit. They can speak, but check the line-up has practitioners first.
  - **The "Seattle Data Guy" has moved.** Ben Rogojan is now in Denver, according to a podcast title.

## 3. Key leads

- **First-time speakers at this chapter:**
  - **Nate Sooter**, Smartsheet. Wrote about founding Smartsheet's first analytics engineering team (2022): [dbt Developer Blog](https://docs.getdbt.com/blog/founding-an-analytics-engineering-team-smartsheet). This is an emerging voice: someone who publishes about dbt but has no talk on record.
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

## 4. Before outreach

- [ ] **Confirm locations taken from a head office.** Priya Tanwar, Nadine Bruxel, Nate Sooter and Vikas Ranjan are placed by their employer's office only.
- [ ] **Confirm the 12 unknown locations.** Brandyn Lee (AgentSync) and Irina Virnik (JumpCloud) are very likely in Seattle, from truncated LinkedIn results. Andres Astorga Espriella may be in Mexico City and at Qbiz rather than independent.
- [ ] **Check the weak location calls.** Wendy Grus and Mira Winkel were placed by a name match to a chapter member only.
- [ ] **Skip or re-rank people outside the region.** Pooja Crahen is in New York, Ben Rogojan in Denver, Mitesh Mangaonkar in Austin and Britton Stamper in San Francisco. Bernardo Dionisi is in Durham, North Carolina, Ivan Perez Avellaneda in Plattsburgh and Dipankar Mazumdar in Canada.
- [ ] **Confirm current roles** for people whose evidence is old: Nate Sooter (2022), Deepak Konidena (Zillow, before 2024) and Vikas Ranjan (T-Mobile, 2023).
- [ ] **dbt Labs staff are labelled.** Elias DeFaria, Lukas Schulte, William Weld, Alexander Bogdanowicz and Wolfram Shulte work there. They can speak, but check the line-up has practitioners first.

## 5. Next run

- **Run the LinkedIn pass first.** 24 tier-1 and tier-2 people are still `not_searched`.
- **Pull the chapter's organisers** and the Seattle WiMLDS and PyLadies events through the Meetup `gql2` endpoint.
- **Scan the women-in-data groups not yet checked:** Women Who Code Seattle, Ada Developers Academy and Women in Analytics.
- **Search the Eastside for job ads** (Bellevue, Redmond, Kirkland), with a working location filter.
- **Look for first-time speakers** through GitHub user search (`dbt location:Seattle`). It was the best source of emerging voices in Atlanta, and Seattle has only 2.

## 6. Replication prompt

````
You are extending my dataset of Seattle-metro companies that use dbt, and people who could speak
at or attend the Seattle dbt Meetup. The file is seattle/seattle_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read seattle/SEARCH_METHOD.md, then
research/README.md and the briefs it links (raw-format.md, location-task.md, linkedin-task.md).
The region is the Seattle metro (Seattle, Bellevue, Redmond and nearby). Commuter towns such as
Olympia and Mount Vernon count as local.

Budget about 25 web searches. Try these first:
1. LinkedIn search results for tier 1-2 people with linkedin_confidence "not_searched".
2. Meetup gql2 for the chapter's organisers, Seattle WiMLDS and PyLadies Seattle events.
3. GitHub user search (dbt location:Seattle) for first-time speakers with public dbt work.
4. New WiDS Puget Sound, SeaTUG and Snowflake Seattle events since metadata.generated_at.
5. A LinkedIn Jobs guest scan re-run, plus Lever/Greenhouse/Ashby site: searches for the Eastside.

Rules: never fetch LinkedIn pages; use only search results. Public professional information only;
never guess gender, and record pronouns only when self-stated. Assemble with research/assemble.py
--base, run research/validate.py (must print ok), and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build: dbt Summit 2026, Airflow Summit 2025 and PyData Seattle 2025, local meetups and user groups, WiDS Puget Sound and other women-in-data communities, company blogs, a LinkedIn Jobs scan and ATS searches. Past chapter speakers added from `../enriched/seattle-dbt-meetup.json`. 110 companies (49 on the watchlist), 79 people, 65 job ads at 44 companies, 7 past meetups. Split: 64 proven speakers, 2 emerging voices, 13 featured. Tiers: 2 tier 1, 40 tier 2, 22 tier 3, 15 connectors. 16 people had already spoken at the chapter. |
| 2026-10-01 | 2 | Location pass: 18 people placed from Meetup host and RSVP profiles, GitHub, speaker bios and recent in-person talks, 16 in the region and 2 outside. |
| 2026-10-01 | 2 | LinkedIn pass: 5 people placed from LinkedIn search results, 1 in the region and 4 outside. 12 people are still unknown. |
