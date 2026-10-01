# London dbt search: method, lessons and replication prompt

This file goes with `london_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-10-01
- **Goal:** find people in Greater London who could **speak at** (or attend) the [London dbt Meetup](https://www.meetup.com/london-dbt-meetup/), and the local companies that use dbt.
- **Region:** Greater London.

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 75 |
| People | 120 |
| Tier 1 leads | 38 |
| First-time speakers (publish, no talk yet) | 11 |
| Proven speakers | 104 |
| Spoke at this chapter before | 33 |
| Based in the region | 92 |
| Based elsewhere | 7 |
| Location unknown | 21 |
| With a LinkedIn profile | 3 |
| Job ads mentioning dbt | 3 |
| Past chapter meetups | 22 |
<!-- at-a-glance:end -->

## 1. How the search was done

One research run covered London. It used 26 web searches before the session limit stopped it, then about 40 direct page fetches.

### Step 1: Other London meetups

- **What was checked:** past events of London data meetups, read through Meetup's `gql2` endpoint with a plain `curl` request. Sorting by date, newest first, gave full line-ups without a browser.
- **[London Analytics Engineering Meetup](https://www.meetup.com/london-analytics-engineering-meetup/events/?type=past):** 27 events from 2022 to 2026. Every event lists speakers with their employer and talk title. This was the richest London source. The recruiter Cognify runs it.
- **[Data Engineers London](https://www.meetup.com/data-engineers-london/events/?type=past):** 15 events since 2023. Some are joint events with the [London Snowflake User Group](https://usergroups.snowflake.com/london/), which gave its organisers and one 2024 line-up.
- **Older events:** a 2022 analytics engineering meetup by [Burns Sheehan](https://www.burnssheehan.co.uk/events/data-meetup-analytics-engineering-the-life-cycle/s107469/), hosted at Dojo.
- **No yield:** [PyLadies London](https://www.meetup.com/pyladieslondon/), Data Science Festival and GDG Cloud London had no dbt talks from 2024 onwards with full speaker names. The [PyData London 2025 call for papers](https://cfp.pydata.org/london2025/speaker/) had no dbt or analytics engineering talks.

### Step 2: Company and consultancy blogs

- **[The Information Lab](https://www.theinformationlab.co.uk/sitemap-0.xml):** 15 dbt posts with named authors. Its sitemap lists every post. Each post's page-data file gives the author, job title and date. The Information Lab hosts the chapter.
- **Monzo:** the [Data @ Monzo Medium feed](https://medium.com/feed/data-monzo) had 8 posts, 2 about dbt. The [Monzo blog's data topic](https://monzo.com/blog/topic/data) had a 2026 data mesh post with three authors.
- **Wise:** the [Wise Engineering feed](https://medium.com/feed/wise-engineering) had a tech stack post that names dbt.
- **No dbt posts:** the [Gousto](https://medium.com/feed/gousto-engineering-techbrunch) and [Deliveroo](https://deliveroo.engineering/feed.xml) blogs.
- **Blocked:** Medium returned HTTP 429 (too many requests) after two feeds. Bumble, Just Eat, Skyscanner, Starling, Octopus Energy and ASOS were not scanned.
- **Not confirmed in London:** the [Infinite Lambda blog](https://infinitelambda.com/wp-json/wp/v2/posts?search=dbt) has dbt posts, but its authors could not be placed in London. The [dbt developer blog authors page](https://docs.getdbt.com/blog/authors) had no confirmed London community authors.

### Step 3: Conferences

- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** the list is rendered by JavaScript, so a fetch returns nothing. Individual speaker pages found through search gave the Virgin Media O2 talk.
- **[Coalesce on the Road London 2025](https://www.getdbt.com/events/roadshow/coalesce-on-the-road-london):** the page returned 404.

### Step 4: Women-in-data communities

This step finds speakers through women-focused groups' own events. It never records or guesses anyone's gender.

- **[Data + Women London](https://usergroups.tableau.com/data-women-london/):** the best source. It is a Tableau user group. Its 2024 and 2025 event pages list speakers with employers, including a dbt talk and a hands-on dbt lab in June 2025.
- **Panels at other meetups:** the Allies of Women in Data panels at the London Analytics Engineering Meetup, and the Data Engineers London International Women's Day panel.
- **No yield:** the [Women in Data UK meet-ups archive](https://womenindata.co.uk/category/meet-ups/) stops in 2020.
- **Result:** 34 people are tagged `women_in_data_community`.

### Step 5: Job ads

- **What was found:** 3 ads at 2 companies, Infinite Lambda and Octopus Energy, from Built In London and a green-jobs board.
- **Weak evidence:** none of the 3 search snippets showed the word dbt. So `dbt_mentioned_in_text` is null for all three.

### Step 6: Chapter history

- **Source:** every named speaker in [`../enriched/london-dbt-meetup.json`](../enriched/london-dbt-meetup.json) was added as a person. That file holds 22 meetups, from 2019-04-04 to 2026-05-27.
- **Result:** 33 people in the file have spoken at the chapter. Four people found by the research were already past speakers with newer talks: Gordon Curzon, Holly Foster, Pablo Fernandez and Ash Sultan.

### Step 7: Location pass and LinkedIn pass

The location rules are in [`../research/README.md`](../research/README.md). In short, a location needs the person's own profile, or a recent in-person local talk plus a local office.

- **Location pass (page fetches):** 13 people placed, 7 in London and 6 elsewhere. Most came from GitHub profiles that name the person's company. Four came from recent in-person talks at an employer with a London office.
- **LinkedIn pass (search results only):** 12 people searched and 3 placed, all in London: [Gordon Curzon](https://www.linkedin.com/in/gordon-curzon-714a1713/), [Pearl Prakash](https://www.linkedin.com/in/pearl-prakash/) and [Christelle Xu](https://www.linkedin.com/in/christellexu/).
- **Still unknown:** 21 people.

## 2. What we learnt

- **Sources that worked:**
  - **Meetup `gql2`:** it answers a plain `curl` request with `groupByUrlname`, and `sort:DESC` returns the newest events first.
  - **London Analytics Engineering Meetup:** every event names speakers, employers and talk titles.
  - **The Information Lab site:** its sitemap and page-data files give author, job title and date for every post.
  - **Data + Women London event pages:** they list speakers with employers.
  - **GitHub profiles:** the company field ties a profile to the person, and the location field places them.
- **Sources that didn't:**
  - **Medium:** HTTP 429 after two feeds, so most London company blogs are unread.
  - **Web search:** the session limit stopped the run after 26 searches.
  - **JavaScript pages:** the dbt Summit speaker list and the PyData London schedule return nothing to a fetch.
  - **Women in Data UK:** no meetups listed after 2020.
- **Watch out for:**
  - **Few first-time speakers:** a first-time speaker (an "emerging voice") is someone who publishes about dbt but has no talk on record. London has 11, against 104 proven speakers. 6 of the 11 work at The Information Lab.
  - **The host dominates:** 11 people work at The Information Lab, including the organiser Ed Hayter. Plan one speaker per company per event.
  - **Stale employers:** talks from 2022 and 2023 give the employer at the time. Andrea Salvati, Naomi Johnson, Katie Hindson, Danny Jones, Madalina Ghita and Andrew Jones may have moved.
  - **Missing talk titles:** several 2026 London Analytics Engineering Meetup listings name speakers but no title.
  - **Possible duplicate:** Jean Dupuis may be the "Jean D." who gave a later dbt Fusion talk.

## 3. Key leads

A tier is a priority level. Tier 1 means a person in London (or not known to be elsewhere) with a dbt item from 2024 onwards, or a first-time speaker with a post from 2024 onwards.

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
- **Connectors:** community organisers who can introduce people.
  - **Anna Aleshko and Luke Ashe-Browne:** organisers of [Data Engineers London](https://www.meetup.com/data-engineers-london/).
  - **Piers Batchelor and Tony Burton:** leads of the [London Snowflake User Group](https://usergroups.snowflake.com/london/).
  - **Kerine Taylor, Hannah Bartholomew and Lydia Wren:** leaders of [Data + Women London](https://usergroups.tableau.com/data-women-london/).
  - **Cognify:** runs the [London Analytics Engineering Meetup](https://www.meetup.com/london-analytics-engineering-meetup/) and the [Stacked Pathways](https://cognifysearch.com/stackedpathways/) mentoring scheme. Its organisers are not named on the listings.

## 4. Before outreach

- [ ] **Check unknown locations.** 21 people have no known location. They include Melissa Simpson, Konrad Maliszewski, Sarah Levy and Lucy Kendrick.
- [ ] **Check tier-1 people raised by the rule.** Milon James (Wise) is tier 1, but dbt is one line in a tech stack post.
- [ ] **Skip dbt Labs staff.** dbt Labs is excluded from outreach. Kshitij Aranke and Richard Persaud are tier 1 but work there.
- [ ] **Check current employers.** 2022 and 2023 talks may show an old employer.
- [ ] **Check who is already booked.** Compare leads with the chapter's upcoming events.

## 5. Next run

- **Retry Medium first.** Read the Bumble, Just Eat, Skyscanner, Starling, Octopus Energy and ASOS blogs for emerging voices. Space the requests out.
- **Finish LinkedIn.** 108 people are still `not_searched`. Start with the 21 unknown locations.
- **Add job ads.** Only 3 were found. Try `site:` searches on Lever, Greenhouse and Ashby with "dbt London".
- **Read more blogs:** Infinite Lambda authors, Datatonic, and dbt Labs case studies of London companies.
- **Check the dbt Summit 2026 speaker pages** through the getdbt.com sitemap for more London employers.
- **Look beyond The Information Lab** for emerging voices, so the line-up does not depend on the host.

## 6. Replication prompt

````
You are extending my dataset of London companies that use dbt, and people who could speak at or
attend the London dbt Meetup. The file is london/london_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Region: Greater London.
Read london/SEARCH_METHOD.md first, then research/README.md, research/raw-format.md,
research/location-task.md and research/linkedin-task.md.

Budget about 25 web searches. Try these first:
1. Medium feeds of Bumble, Just Eat, Skyscanner, Starling, Octopus Energy and ASOS (space requests out).
2. New events of the London Analytics Engineering Meetup, Data Engineers London and
   Data + Women London, through Meetup gql2 with curl.
3. New posts on The Information Lab and Monzo blogs; dbt Summit speaker pages from the getdbt.com sitemap.
4. Job ads: site: searches on Lever, Greenhouse and Ashby for dbt London.

Rules: never fetch LinkedIn pages, use only search results. Public professional information only;
never record or guess gender; pronouns only when self-stated. Skip past chapter speakers; the
assembler adds them. Assemble with research/assemble.py --base, run research/validate.py (must
print ok), then add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build from one research run: 75 companies, 120 people, 3 job ads at 2 companies, 22 past meetups. 33 people had spoken at the chapter. Tiers: 38 tier 1, 55 tier 2, 19 tier 3, 7 connectors, 1 organiser. Lead types: 104 proven speakers, 11 emerging voices, 1 featured, 4 with no public content. |
| 2026-10-01 | 1 | Location pass from public pages: 13 people placed, 7 in London and 6 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 12 people searched, 3 placed in London. 21 people are still unknown. |
