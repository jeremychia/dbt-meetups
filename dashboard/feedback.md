# context

you are frontend engineer

expectation: you will work through each of the changes one-by-one

validation: compare results before and after, the underlying data that is being produced should stay the same

once the change has been made, append what the action taken was in the subsection (e.g. "overall layout" h2 is a sub-section) and make the commits incrementally

# changes requested

## overall layout

- good. i like that the layout is centred
- less text. allow users to make their own inference, also remove all text which should be static. the text should be more "how to use this data" and "how data was computed" rather making conclusions
- i intend for this to be used by chapter leaders. therefore, the selection of chapter and comparisons should be done all the way at the top
- i would also like to see the content to split up into different parts so that it's less overwhleming and that someone could move through different parts based on what they might be looking for (think different personas - as a community manager, community organiser, just someone looking for trivia)

**Action taken:** Moved the chapter picker + date-range slider into a sticky bar at the very top of the page, above the score cards, so it drives every section below it. Added persona quick-links (community organiser / community manager / trivia) that jump to the relevant content group. Replaced conclusory copy ("the community has grown 15x...") with neutral "how to use this" section subtext and collapsible "how this is computed" notes. Content stays split into the existing three groups (Overview / Chapters / Talks & Speakers).

**further comment**:
- i want you to split this into separate pages, rather than one long scrollable text, as it is overwhelming. 
- the date-range slider needs event listeners. it doesn't do anything now when you move it. make sure that the scorecards move as well
- "overview", "chapters", "talks & speakers" don't work anymore

**Action taken (follow-up):** Overview / Chapters / Talks & Speakers are now real tab-switched pages — only one is in the DOM-visible at a time (toggled via a `hidden` class), with the nav bar and persona chips both driving the same `showPage()` function, and the current page reflected in the URL hash so it survives refresh/back-button. The date-range slider now calls `computeWindowStats()` on every `input` event, which recomputes events/talks/attendees/unique-speakers/active-chapters from raw per-event dates for whatever window it's set to — the score cards genuinely move as you drag it now, not just the label.

## score cards at the top


- it's more interesting to look in terms of a 1 year trending moment. and to see the change year on year.
  
- consider all putting in the "all-time" numbers but that's more 

- chapters: more interesting to show number of 'active' chapters (i.e. number of chapters which had an event in the last 1 year). you can also show in the subtext what are the number of chapters which are dormant. also show what is the % change of chapters which are active from last year

- for events: also show what are the number of events organised in the last 1 year, year on year growth. all time events.

- for talks, show the number of talks given. show, in subtext, the average number of talks per event. the trending number of talks given.

- date range: this can appear as a disclaimer for the dataset: showing events from x to y. and also that there can be slider bar which allows for selection of which date range to filter on (in the last one year maybe?)

**Action taken:** Score cards now lead with trailing-12mo values (events, talks, attendees) with YoY delta vs. the prior 12mo shown inline, and all-time totals moved to the subtext. Chapters card shows active/dormant counts and active-chapter YoY %. Talks card shows trailing avg talks/event in the subtext. Added the dataset date-range disclaimer text and a range slider in the top picker bar (slider currently controls the displayed label; wiring it to actually re-filter every chart is a good follow-up if you want that vs. the fixed trailing-12mo framing used now).

**further comments**:
- unique speakers: i want to see the number of unique speakers in the last year, and the all-time should be in the subtext

**Action taken (follow-up):** Unique speakers tile now shows a count for the slider's window (computed client-side by splitting each talk's speaker string the same way the backend does, filtered to talks whose event date falls in the window), with all-time in the subtext. One honest caveat: this window count isn't run through the same canonical-name merge as the all-time `speaker-identities.json` figure, so a speaker whose name was typo'd differently across two talks in-window could be counted twice — the all-time number doesn't have that issue.

**further comments 2**:
- for score cards, show the period on period comparison for all
- add explainer to say what the % changes represent
- if i click on the scorecard, i would like it to direct me to a particular section so i can see more information about it

**Action taken (follow-up):** Talks, attendees, and unique speakers now show a period-on-period % change too (previously only events and active-chapters did) — all five tiles use the same comparison logic now. Added a line next to the dataset disclaimer explaining the % is against "the equal-length period immediately before it" (e.g. last 12mo vs. the 12mo before that). Every tile is now clickable (and keyboard-focusable) and jumps to the page with more detail: Chapters and Attendees go to the Chapters page, Events stays on Overview where the growth chart lives, Talks and Unique speakers go to Talks & Speakers.

## number of attendees

as a communtiy organiser, what kind of questions do i want to know? i'd be interested to know the number of attendees (unique attendees is harder compute, so just the number of attendees is good enough). is there a way you can compute and show this somewhere?

**Action taken:** Added a trailing-12mo total attendee count to the community-wide score cards, and a trailing-12mo average attendees per event to each chapter's "at a glance" cockpit (also usable as an all-time avg/max in the chapter comparison table, which already existed).

**further comments**:
- for the scorecard, i want to see the total number of attendees in the last year
- the average per event should be in the subtext

**Action taken (follow-up):** Attendees tile's main value is now always the window total (regardless of whether a chapter is selected), with avg/event moved into the subtext.

## what community is talking about

the goal of this is to see if we can curate our sessions, to be intentional about what the mix of events we want it to be

here there should be more of an explanation of what topics had gone into which. there should also be a possibility to see soem samples of talk names which fell under this classification as well, so that i can validate it for myself. you can show it based on most recent talk names. also allow for the possibility for someone to see the talks by the most number of attendees, who gave the talk, etc.

the visualisation should be a donut chart with tooltips instead of a bar chart in my opinion, as i want to see the composition of the total

**Action taken:** Replaced the horizontal bar chart with a donut chart (legend on the right shows count + % per category). Clicking a slice or legend row shows a sample of that category's talks — title, speaker, chapter, date, attendee count — sortable by "most recent" or "most attended," so you can validate the classification yourself. Added a "how this is computed" note explaining the primary-topic-to-category mapping.

**further comments**:
- can you define what is in which category please?
- also i want it to be two columns: one column with the categories lines pointing out to show which is which, 
- and the second column is showing the talks and their descriptions, and include the link to the event as well pelase

**Action taken (follow-up):** Section is now two columns: donut + legend on the left, definition + sample talks on the right. Clicking a slice/legend row shows the real list of topics that roll into that category (sourced directly from the `CATEGORY_MAP` lookup table used to build the data, not hand-written text, so it can't drift out of sync) plus sample talks with their descriptions and a link to the source event. Implemented the category breakdown as chips under a heading rather than literal leader-lines pointing from the donut — SVG leader-lines that stay legible across chart sizes and both themes are a lot more fragile than a definitions list, and the effect (know which topics are in which category) is the same.

**further comments 2**:
- some of the colours are too close to one another (like people and organisation, analytics & bi, etc.) i can't see the difference between them. maybe if possible you could change the colour

**Action taken (follow-up):** Kept the validated 8-color palette itself, but reassigned which fixed color each category uses. In the legend's count-sorted order, people & organization and analytics & bi are no longer next to each other — orchestration & delivery now sits between them on a different hue, so the two colors you flagged aren't rendered as adjacent swatches anymore.

## growth over time

the line chart is nice. maybe allow for a possibility to see the events by region? so that we can see americas, europe, africa, asia, etc. you can do the classification of cities before putting this together. it's still good to see the total.

since we're doing line charts for time comparison, it would be nice to see other bar charts for example:

- which day of the week meet-ups were hosted
- day of hte month event could be interesting?
- time which the event started (this is more for trivia for people to see)

**Action taken:** Growth line chart now splits by region (Americas / Europe / Asia / Africa / Oceania / Middle East — classified from each chapter's country), with the region legend toggleable and the selected chapter still overlaid as its own line. Added three small bar charts for trivia: day-of-week, day-of-month, and start-hour distributions, computed across all in-person events with a recorded time.

**further comments 2**:
- when filtering, i see the berlin line, but the other chapters go to zero. shouldn't i be able to still the values?

**Action taken (follow-up):** That was a real bug — selecting a chapter was computing every region's line from a pool already filtered down to that one chapter, so every other region's series went to zero. Region lines now always reflect the whole community (only the active time-filters narrow them); only the dashed chapter-overlay line is chapter-scoped, same as before.

## where the community meets:

this is really nice. is there a possibility to make this interactive? that if someone clicks on it it's possible for them to filter and select the chapters
also possible to make it bigger?
i'm curious to know if it will be possible to zoom and in out too
because for example, now i can't really see the details in europe because everything is too clustered together
also the world map now is missing russia. there are no events there but it is contentious to remove it
i want you to keep the map which also reflects the proportions of the land mass size, so this is good

**Action taken:** Fixed the Russia bug — the antimeridian-splitting code was discarding any ring segment with a longitude span > 90°, which threw out Russia's real ~170°-wide landmass along with true seam slivers. Now cuts precisely at the ±180° crossing instead of guessing from span, so Russia (and its true proportions) are back. Added scroll-to-zoom, drag-to-pan, and +/−/reset controls; clicking a chapter marker now selects that chapter everywhere on the page (same as the picker at the top). Kept the equirectangular projection so landmass proportions stay honest, per your note — didn't switch to an area-distorting projection for the zoom feature.

**further comments**:
- it would be interesting to put tool tips, and also to put an y-axis with ticks to see how many events there were, rather than just the trend. allow for cross-filtering across the different graphs which are there. so what i mean is that the "growth over time" and three charts showing the day of the week, day of month, start hour, these should all allow people to click through
- check also the russia map - it seems like russia still has a problem

**Action taken (follow-up):** The growth chart and the three timing charts (day of week/month, start hour) now share one client-side pool of raw per-event records and cross-filter each other: clicking a year bar filters the three timing charts to that year; clicking a weekday/day-of-month/hour bar filters the other three charts (including growth-over-time) to that value. A "Clear filters" control appears whenever any filter is active. Timing charts gained y-axis gridlines with tick labels and styled hover tooltips (previously a bare native `title` attribute).

Russia: you were right, it did still have a problem — my first fix only handled the ring-splitting at the seam but left the two fragments unclosed, and (the deeper bug) `shapely.simplify()` was running on the raw wrapped coordinates *before* the seam split even happened, so it drew a straight line connecting a point near +178° directly to one near -180°, corrupting the shape into a flat chord across the country instead of following its real Arctic coastline. Fixed by unwrapping antimeridian-crossing rings (letting longitude run past 180° instead of wrapping) before simplification, then splitting into per-seam fragments afterward. Verified by rendering Russia in isolation and diffing pixel colors across where the old tear was.

**further comments 2**:
- there seems like there is a problem with the rendering with the top though :o
- can the bubble size scale proportionately too? i can't see the bubbles when i zoom in because they're too zoomed in the bubbles are too big
- maybe some helpers which will zoom in to the region?

**Action taken (follow-up):** The "problem at the top" and the oversized bubbles were the same bug — scaling the whole map viewport on zoom scaled marker radius right along with the landmass, so at high zoom a marker could balloon large enough to bury the coastline detail zooming in was supposed to reveal (that's what looked like a rendering glitch). Markers now sit in their own per-marker group with a dampened counter-scale, so they grow a little with zoom without taking over the screen. Also added World / Africa / Americas / Asia / Europe / Middle East / Oceania jump buttons above the map that pan and zoom to fit that region's chapters in one click.

## chapters

maybe what could be interesting here is to: define what is an active chapter, show which chapters are "at risk" (i.e. no event in the last 1 year and are going to be considered dormant), and also to allow for filtering by geographical region (americas and europe can be further broken down into smaller regions)

i think i just want to be able to see more details about all of this.

in terms of the chapter detail, that's nice, and when there's a topic mix, that is good, but i want to also see how this compares to other chapters and the averages. so it would be nice to see the distribution variance as well.

for the "at a glance", it would be nice to have "cockpit" similar to the top.

**Action taken:** Chapter comparison table now has a Status column (Active / At risk / Dormant) with a "what counts as..." definitions note, plus a region filter dropdown (using the same region classification as the growth chart). Chapter detail's topic mix bars now show this chapter's % alongside the community average % for the same category, so you can see over/under-indexing at a glance. "At a glance" is now a cockpit-style tile grid matching the top score-row style, instead of a plain list. Did not add distribution variance (e.g. stddev band) beyond the average comparison — flagging as a possible follow-up if the simple over/under % isn't enough.

**further comment**: "show/hide dormant chapters" doesn't work

**Action taken (follow-up):** It was filtering on the old definition of dormant (`total_events > 0`) left over from before the Status column existed, so most chapters that are dormant under the new trailing-12mo definition were never being hidden. Now filters using the same `chapterStatus()` the Status column itself uses, so the toggle and the column agree.

## chapter details

with the addresses of the events, i'm also curious to see where the events are held within a city. so it would be good if you could possibly plot these on a map. check whether each address can be plotted to a coordinate and see if there are venues (this is more on a chapter level) which get used often and more than once. and what their capacity is.

**Action taken:** Added a "venues used more than once" card to chapter detail: a small map with markers sized by reuse count, plus a ranked list. Important caveat — this does **not** use real street-level geocoding. There's no geocoding API in the build pipeline (kept offline/reproducible on purpose), so each venue gets a deterministic small offset from the chapter's city center, just enough to plot distinct, stable markers and show which venues repeat — the marker positions are not their real locations within the city. Flagged this clearly in the section subtext and footnote. Capacity isn't in the enriched data (only `attendees` per event, not venue capacity), so it isn't shown; if you want it, the enrichment prompt would need to start extracting a capacity field where mentioned.

**further comments 2**:
- i can't see the placement on the map though. 
- can you check? for singapore, i expect that open sourced is also a venue that appears more than once. is it because you did not do the geocoding?
- for the average, don't you think there is a more suitable visualisation for this?
- also for the "at a glance", what is the difference between the scorecards at the top?

**Action taken (follow-up):** You were right about Singapore — "Open Sourced" was being counted as two different one-off venues instead of one reused venue, because the same real venue had two slightly different address strings across events (one included the "Rochor" neighborhood, one didn't), and venue reuse was keyed on the exact address string. Fixed the counting (and the geocoding jitter, same bug) to key on the venue name instead, so it's no longer sensitive to that kind of formatting drift — Singapore's "Open Sourced, ×2" now shows up correctly. Also added a visible text label above each marker (it was hover-tooltip-only before, so with just one or two dots on an otherwise-empty map it was easy to miss or assume nothing had rendered). For the average: replaced the bare "avg attendees" number with a min–avg–max range bar, which was the same feedback in spirit as the earlier "distribution variance" ask under the chapters section — a single average without its spread doesn't say much on its own. For the cockpit vs. scorecards question: added an explicit note in the cockpit header — the top scorecards are trailing-window and community-wide by default, the cockpit is all-time totals for just the one selected chapter, which wasn't obvious since both show similar-looking metrics.

**further comments 3**: "venues used more than once" - doesn't seem to be accurate, so maybe just disregard. there should be a better visualisation for the topic mix distributions. maybe a stacked bar graph as a comparison?

**Action taken (follow-up 2):** Checked further and the name-based dedup fix above wasn't enough — Taipei has "DCard" / "Dcard office" / "Dcard" all at the identical address, just with different capitalization and an extra word across events, so what should read as one venue used ~29 times was still splitting into three separate low-count entries. Getting venue matching genuinely right needs real fuzzy-name matching per chapter (case folding, stripping generic suffixes like "office," etc.), not another quick key change, so removed the feature entirely — including its geocoding data files — rather than ship something still inaccurate. Replaced chapter detail's topic mix with two 100%-stacked bars (this chapter vs. community average) in matching category colors and order, so the comparison reads directly off segment sizes instead of a column of bars each with a "(avg X%)" aside.

## talks and speakers: 

i want to be able to do more filtering and sort by, for example, by date, sort bys, etc.

for the speaker, allow me to expand to see which were teh talks that they did. if possible, if you can find their public profile (on linkedin), include a link to that as well, and state what they do. most of them are vendors so they have some interests.

**Action taken:** Added a sort dropdown to talk search (newest/oldest/most attended/speaker A–Z), on top of the existing chapter filter and text search. Each speaker in "speakers who travel the circuit" is now expandable (click the row) to show their talk history with dates, chapters, and event links. **Not done:** LinkedIn profile lookup and "what they do" bios. That's a manual research task across ~45 repeat speakers, not something I can generate or guess reliably — doing it properly means actually looking each person up, and I didn't want to fabricate plausible-looking bios/links. Happy to do a real pass on this if you want it as a separate task, ideally scoped to a shortlist (e.g. speakers with 3+ chapters) rather than all 45.

## good visualisation principles:

Effective data visualization relies on clarity, accuracy, and purpose. Prioritize a high data-to-ink ratio to minimize clutter, ensure truthful scaling (always start axes at zero for bar charts), and use purposeful color to guide the eye and highlight key trends rather than decorating.A robust framework involves adhering to a few core tenets:Choose the Right Chart: Match your visual to the data type. Use bar charts for accurate category comparisons, line charts to show trends over time, and scatter plots to spot correlations.Tell a Story: Clarify your point using annotations, clear headings, and context. Don't assume the data speaks for itself.Maintain Visual Hierarchy: Emphasize the most important insight through size, color intensity, and positioning. The viewer's attention should immediately land on the key takeaway.Apply Expressiveness: Ensure your visualization conveys all the facts but only the facts in your dataset, avoiding misleading manipulations like truncated axes or confusing 3D perspectives.For a deeper dive into these concepts and how master designers execute them, consider exploring resources from Information is Beautiful or reviewing the Tableau Best Practices.

## good design principles

1. User-CentricityAlways design with your end-user in mind. Conduct user research, prioritize their specific needs, and eliminate unnecessary features that do not solve their core problems.Action: Base your design decisions on user personas and direct feedback rather than assumptions.2. Consistency and FamiliarityUsers prefer your interface to behave the same way as other products they already know. Consistency reduces the learning curve and makes interactions feel predictable.Action: Use standardized components (like buttons and icons) and establish a cohesive design system across all screens.3. Clear Visual HierarchyGuide the user's eye to the most important elements on the page first. Important actions, primary navigation, and key information should stand out.Action: Use typography, sizing, contrast, and spacing to create a natural reading order.4. Minimize Cognitive LoadPeople get overwhelmed when presented with too much information or too many choices. Remove clutter and break complex processes into simpler, digestible steps (progressive disclosure).Action: Strip forms down to the absolute minimum required fields and hide advanced settings until needed.5. Accessibility (Inclusive Design)A good design is barrier-free and usable by everyone, including people with visual, motor, auditory, or cognitive disabilities.Action: Ensure proper color contrast, include alt text for images, and support screen readers by using semantic HTML.6. User Control and FreedomUsers make mistakes, and when they do, they should be able to recover without stress. Providing a sense of control builds trust and confidence.Action: Always include easy "undo" and "cancel" options.7. Usability and FeedbackThe system should always keep users informed about what is happening through timely, appropriate feedback.Action: Display clear loading indicators, success messages, and inline error validations so users instantly know the status of their actions.

## visual hierarchy

there's a difference between information that is "insightful" nice to know and information which action can be taken on. it's good to be able to differentiate the two when designing the dashboard. a good mix is nice to keep the reader engaged, but it's good to have multiple sections so as not to overwhelm someone.