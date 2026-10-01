# Melbourne dbt search: method, lessons and replication prompt

This file goes with `melbourne_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-09-24
- **Goal:** find people in Greater Melbourne who could **speak at** (or attend) the [Melbourne dbt Meetup](https://www.meetup.com/melbourne-dbt-meetup/), and the local companies that use dbt.
- **Region:** Greater Melbourne, including Docklands and Port Melbourne. Sydney and Adelaide do not count.

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 70 |
| People | 56 |
| Tier 1 leads | 13 |
| First-time speakers (publish, no talk yet) | 2 |
| Proven speakers | 51 |
| Spoke at this chapter before | 7 |
| Based in the region | 52 |
| Based elsewhere | 2 |
| Location unknown | 2 |
| With a LinkedIn profile | 12 |
| Job ads mentioning dbt | 35 |
| Past chapter meetups | 4 |
<!-- at-a-glance:end -->

## 1. How the search was done

One research run used about 18 web searches, plus a logged-out LinkedIn Jobs scan. Tier 1 was kept strict: people in Melbourne, or with an unknown location, who have a dbt item from 2024 onwards. First-time speakers were raised to tier 1 under the shared rule.

### Step 1: dbt Labs events

- **[Coalesce on the Road Melbourne 2025](https://www.getdbt.com/events/roadshow/coalesce-in-melbourne)** (2025-11-11): the best single source. It gave RMIT, REA, MECCA, John Holland, Pepperstone, Marketplacer and David Jones speakers.
- **[dbt World Tour Melbourne 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-melbourne)** (2026-10-06, Fortress Melbourne): RMIT, Onyx Gaming and Suncorp speakers.
- **How to read them:** the speakers sit in the page's embedded data. Change the slug to `coalesce-in-<city>` or `dbt-world-tour-<city>` and parse the `speakersArray` JSON.
- **No Melbourne speakers:** [Coalesce on the Road Sydney 2025](https://www.getdbt.com/events/roadshow/coalesce-in-sydney) had one Envato speaker with an unknown city. [dbt World Tour Sydney 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-sydney) had none.

### Step 2: Other local meetups and conferences

- **[Snowflake User Group Melbourne](https://usergroups.snowflake.com/melbourne/):** 932 members and 145 to 250 RSVPs per event. Its pages fetch cleanly.
- **[Data Engineering Melbourne](https://www.meetup.com/data-engineering-melbourne/):** 6,890 members and a monthly talk. Mantel hosted it until 2025-05, then Thoughtworks, MYOB, Fabric Group and Vivanti.
- **[Melbourne Databricks User Group](https://www.meetup.com/melbourne-databricks-user-group/):** 1,359 members, mostly Databricks platform speakers.
- **[DataEngBytes Melbourne 2026](https://dataengbytes.com/2026/melbourne):** read through `/api/2026/users`, which includes self-stated pronouns and LinkedIn URLs. The 2025 archive does not load.
- **[PyCon AU 2025](https://pretalx.com/pycon-au-2025/schedule/):** held in Melbourne. Titles were cut short, and only one talk was clearly relevant.
- **[Microsoft Fabric & Power BI Melbourne](https://www.meetup.com/power-bi-melbourne/):** BI only.

### Step 3: Company blogs and newsletters

- **[Cevo blog](https://cevo.com.au/tech-insights/):** one dbt article, from 2026-02.
- **[Canva engineering blog](https://www.canva.dev/blog/engineering/):** a Snowflake monitoring post from 2024-11.
- **[Pipeline To Insights](https://pipeline2insights.substack.com/about):** a Melbourne-written Substack with a dbt series.
- **No result:** the [EdgeRed](https://edgered.com.au/technology_partner/dbt-solutions-partner/) partner page names no Melbourne authors. Searches for REA, Seek, Culture Amp, Linktree and carsales blogs returned nothing, and realestate.com.au is blocked by the search tool.

### Step 4: Job ads

- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt), logged out:** search `keywords=dbt` for the Melbourne area. Up to 150 ads were checked for the whole word dbt.
- **Yield:** 35 job ads at 31 companies, for example REA, carsales, Xero, Kogan.com and MECCA Brands. Recruiters are recorded with type `other` and a "RECRUITER" note.

### Step 5: Women-in-data communities

This step looks for speakers through women-focused groups' own events. It never labels or guesses anyone's gender.

- **[R-Ladies+ Melbourne](https://www.meetup.com/rladies-melbourne/):** 2,583 members, but event pages do not name speakers.
- **Not found:** PyLadies, She Loves Data, WiDS and Women in Data have no Melbourne Meetup groups under the names tried.
- **Result:** no candidate came from this step.

### Step 6: Chapter history

- **Past speakers:** every named speaker from `../enriched/melbourne-dbt-meetup.json` was added. That covers 4 events, from 2024-02-15 to 2025-06-24.
- **All at Mantel Group:** every chapter event was held at Mantel's Melbourne office, 452 Flinders St.

### Step 7: Location pass and LinkedIn pass

- **Location pass:** people were placed from public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
  - 3 people spoke in person in Melbourne in the last 2 years, at employers with a Melbourne office. They are placed at medium confidence.
  - Tristan Handy's GitHub profile gives Philadelphia.
- **LinkedIn pass:** search results only, never a LinkedIn page. 5 people were searched. It placed 3 in Melbourne and 1 in Adelaide.
- **Yield:** 8 people placed across both passes, and 2 still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **getdbt.com roadshow pages.** Their embedded JSON names every speaker, company and title.
  - **The Snowflake User Group and Data Engineering Melbourne.** Both are large and meet often.
  - **The DataEngBytes API.** It gives self-stated pronouns and LinkedIn URLs.
- **Sources that didn't:**
  - **Women-in-data groups.** None names speakers, so the line-up needs introductions instead.
  - **The DataEngBytes 2025 archive** does not load.
  - **Company blogs.** Most Melbourne tech companies have no searchable dbt posts.
- **Watch out for:**
  - **Mantel dominates.** It hosted every chapter event and several other user groups. Plan for one speaker per company per event.
  - **Sydney overlap.** Rob Scriva (Canva) and Margie Iliescu (Mantel) are in both datasets. Rob Scriva is in Adelaide.
  - **Head-office locations.** Mantel's LinkedIn location is its Sydney head office, so it does not place a Melbourne employee.

## 3. Key leads

- **First-time speakers** (people who publish about dbt but have no talk on record):
  - **Domenico Campagnolo (Cevo):** wrote [on-demand dbt execution in secure cloud set-ups](https://cevo.com.au/post/on-demand-dbt-execution-rethinking-analytics-engineering-in-secure-cloud-environments/), with dbt-core containers on ECS Fargate. A LinkedIn result places Domenico Campagnolo in Greater Melbourne.
- **Ready for a first dbt talk** (proven speakers whose talks so far are not about dbt):
  - **Erfan Hesami (Airmaster):** writes the [dbt in Action series](https://pipeline2insights.substack.com/p/dbt-in-action-1-fundamentals) on Pipeline To Insights. The only talk on record is on dlt.
  - **Calvin Wang (Canva):** a Staff Analytics Engineer and 2026 Snowflake Data Superhero, on a [Snowflake user group panel](https://usergroups.snowflake.com/events/details/snowflake-melbourne-presents-snowflake-user-group-melbourne-march-2026/).
- **Anchor speakers:**
  - **Sarah Taylor and Dan Lawson (RMIT):** [the day we broke dbt Platform](https://www.getdbt.com/events/roadshow/coalesce-in-melbourne), at Coalesce Melbourne 2025. Sarah Taylor also spoke on RMIT's data mesh at [DataEngBytes 2026](https://dataengbytes.com/2026/melbourne).
  - **Lachlan Clulow and Leandro Bezerra Silva (REA Group):** [lessons from moving to dbt Platform](https://www.getdbt.com/events/roadshow/coalesce-in-melbourne).
  - **David Zmood, Nick Stansfield and Steve Preece (John Holland):** a [three-person dbt journey talk](https://www.getdbt.com/events/roadshow/coalesce-in-melbourne).
  - **Samuel Ellett (Pepperstone):** spoke at the [2024-05 chapter event](https://www.meetup.com/melbourne-dbt-meetup/events/299757694/) and in a Coalesce Melbourne 2025 fireside chat.
- **Connectors** (people who can introduce others):
  - **Margie Iliescu (Mantel):** organised the [2024 chapter events](https://www.meetup.com/melbourne-dbt-meetup/). The first contact for bringing the venue back.
  - **Priyanka Srivastava (Slalom):** leads the [Snowflake User Group Melbourne](https://usergroups.snowflake.com/melbourne/), a natural co-host.
  - **Emily Melhuish and Choonyin Yeap:** organise [DataEngBytes Melbourne](https://dataengbytes.com/2026/melbourne).
  - **[Data Engineering Melbourne](https://www.meetup.com/data-engineering-melbourne/):** a good co-host partner. Thoughtworks (360 Collins St) is its main venue.

## 4. Before outreach

- **Check most "in region" calls.** Only 6 of the people marked in Greater Melbourne have a location note with evidence. The rest were placed from their employer or event during the first build.
- **Check people already booked.** RMIT (Vishesh Jain and Will Chan), Onyx Gaming (Aaron Pratt and Edmond Yeo) and Suncorp (Sudheer Chalamcharla) speak at dbt World Tour Melbourne on 2026-10-06.
- **Merge duplicate companies.** Examples are MECCA and MECCA Brands, Cevo and Cevo Australia, and Wesfarmers and Workwear Group (Wesfarmers).
- **Check one spelling.** The dbt Labs page spells Samuel Ellett as "Samuel Ellet".
- **Skip dbt Labs staff.** Tristan Handy and Pat Kearns are excluded from outreach.
- **Use pronouns only where recorded.** 6 people stated their pronouns on DataEngBytes. Everyone else has none.

## 5. Next run

- **After 2026-10-06:** add the dbt World Tour Melbourne recordings and any new speakers.
- **People still without a location:** 2. Evan Williams's LinkedIn result shows only Mantel's Sydney head office. Pat Kearns works at dbt Labs and is excluded anyway.
- **Women-in-data:** try Eventbrite and Luma directly for She Loves Data, WiDS and PyLadies Melbourne, and ask R-Ladies+ Melbourne for its speakers.
- **Blogs:** try REA, Seek, Culture Amp and carsales blogs through direct fetches instead of web search.
- **Job ads:** add the Lever, Greenhouse and Ashby `site:` searches for dbt Melbourne.

## 6. Replication prompt

````
You are extending my dataset of Greater Melbourne companies that use dbt, and people who could
speak at or attend the Melbourne dbt Meetup. The file is melbourne/melbourne_dbt_companies.json
in /Users/jeremychia/Documents/Github/dbt-meetups. Read melbourne/SEARCH_METHOD.md first, then
research/README.md, research/raw-format.md, research/location-task.md and
research/linkedin-task.md. Keep the shared schema (berlin_planning/SEARCH_METHOD.md §3).

Try first: the dbt World Tour Melbourne 2026 recordings and the speakersArray JSON on
getdbt.com roadshow pages; new Snowflake User Group Melbourne, Data Engineering Melbourne and
Melbourne Databricks User Group events; DataEngBytes /api/<year>/users; women-in-data events on
Eventbrite and Luma; and job ads through Lever, Greenhouse and Ashby site: searches. Count
Docklands as Melbourne, and never place someone from a head-office location alone.

Rules: never fetch LinkedIn pages, only use search results; public professional information
only; never guess gender, and record pronouns only when self-stated. Assemble with
research/assemble.py --base, place people with research/apply_locations.py, then run
research/validate.py and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build. dbt Labs roadshow agendas, local meetups and user groups, company blogs, women-in-data communities and a LinkedIn Jobs scan, plus chapter history. 56 people at 70 companies, 7 of them past chapter speakers. 35 dbt job ads at 31 companies. |
| 2026-10-01 | 2 | Location pass from public pages: in-person talks at employers with a Melbourne office, and a GitHub profile. 4 people placed, 3 in Melbourne and 1 elsewhere. |
| 2026-10-01 | 2 | LinkedIn pass from search results: 4 people placed, 3 in Melbourne and 1 in Adelaide. With the location pass, 8 people placed and 2 still unknown. |
