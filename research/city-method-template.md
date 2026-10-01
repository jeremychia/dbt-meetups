# <City> dbt search: method, lessons and replication prompt

This file goes with `<city>_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** <date>
- **Goal:** find people in <region> who could **speak at** (or attend) the <chapter name>, and the local companies that use dbt.
- **Region:** <what counts as in region, e.g. "Greater London" or "the Netherlands">

<!-- at-a-glance:start -->
<!-- at-a-glance:end -->

## 1. How the search was done

One `### Step N: <source group>` per source group the run used, in the order they mattered. For each, say what was checked and what it yielded, in 2–5 bullets. Typical groups:

- chapter history (past speakers, added by the assembler)
- other local meetups and conferences
- company and consultancy blogs
- women-in-data communities, sourced through their own events
- job ads
- location pass (page fetches) and LinkedIn pass

## 2. What we learnt

- **Sources that worked:** bullets, each naming the source and why it worked.
- **Sources that didn't:** bullets, each naming the source and what went wrong.
- **Watch out for:** city-specific traps (a consultancy that dominates, stale titles, a placeholder employer, duplicates).

## 3. Key leads

- **First-time speakers:** the 3–5 strongest, each with name, employer, what they wrote and a link.
- **Anchor speakers:** 2–4 proven speakers for a line-up.
- **Connectors:** community organisers who can introduce people.

## 4. Before outreach

Bullets: what the organiser must check (unverified locations, tier-1 people raised by the rule, possible duplicates, people already booked).

## 5. Next run

Bullets: sources not yet searched, people still without a location, and what to try first.

## 6. Replication prompt

A fenced prompt, about 15 lines, that a new session can paste to extend this city. It names the file, the region, the briefs in `../research/`, the sources to try first, and the rules (no LinkedIn page fetches, only search results; professional information only; validate before finishing).

## Change log

| Date | Version | Change |
|---|---|---|
| <date> | <n> | <one line per run: what was added, with counts> |
