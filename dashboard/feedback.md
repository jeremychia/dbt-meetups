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

## score cards at the top


- it's more interesting to look in terms of a 1 year trending moment. and to see the change year on year.
  
- consider all putting in the "all-time" numbers but that's more 

- chapters: more interesting to show number of 'active' chapters (i.e. number of chapters which had an event in the last 1 year). you can also show in the subtext what are the number of chapters which are dormant. also show what is the % change of chapters which are active from last year

- for events: also show what are the number of events organised in the last 1 year, year on year growth. all time events.

- for talks, show the number of talks given. show, in subtext, the average number of talks per event. the trending number of talks given.

- date range: this can appear as a disclaimer for the dataset: showing events from x to y. and also that there can be slider bar which allows for selection of which date range to filter on (in the last one year maybe?)

## number of attendees

as a communtiy organiser, what kind of questions do i want to know? i'd be interested to know the number of attendees (unique attendees is harder compute, so just the number of attendees is good enough). is there a way you can compute and show this somewhere?

## what community is talking about

the goal of this is to see if we can curate our sessions, to be intentional about what the mix of events we want it to be

here there should be more of an explanation of what topics had gone into which. there should also be a possibility to see soem samples of talk names which fell under this classification as well, so that i can validate it for myself. you can show it based on most recent talk names. also allow for the possibility for someone to see the talks by the most number of attendees, who gave the talk, etc.

the visualisation should be a donut chart with tooltips instead of a bar chart in my opinion, as i want to see the composition of the total

## growth over time

the line chart is nice. maybe allow for a possibility to see the events by region? so that we can see americas, europe, africa, asia, etc. you can do the classification of cities before putting this together. it's still good to see the total.

since we're doing line charts for time comparison, it would be nice to see other bar charts for example:

- which day of the week meet-ups were hosted
- day of hte month event could be interesting?
- time which the event started (this is more for trivia for people to see)

## where the community meets:

this is really nice. is there a possibility to make this interactive? that if someone clicks on it it's possible for them to filter and select the chapters
also possible to make it bigger?
i'm curious to know if it will be possible to zoom and in out too
because for example, now i can't really see the details in europe because everything is too clustered together
also the world map now is missing russia. there are no events there but it is contentious to remove it
i want you to keep the map which also reflects the proportions of the land mass size, so this is good

## chapters

maybe what could be interesting here is to: define what is an active chapter, show which chapters are "at risk" (i.e. no event in the last 1 year and are going to be considered dormant), and also to allow for filtering by geographical region (americas and europe can be further broken down into smaller regions)

i think i just want to be able to see more details about all of this.

in terms of the chapter detail, that's nice, and when there's a topic mix, that is good, but i want to also see how this compares to other chapters and the averages. so it would be nice to see the distribution variance as well.

for the "at a glance", it would be nice to have "cockpit" similar to the top.

## chapter details

with the addresses of the events, i'm also curious to see where the events are held within a city. so it would be good if you could possibly plot these on a map. check whether each address can be plotted to a coordinate and see if there are venues (this is more on a chapter level) which get used often and more than once. and what their capacity is.

## talks and speakers: 

i want to be able to do more filtering and sort by, for example, by date, sort bys, etc.

for the speaker, allow me to expand to see which were teh talks that they did. if possible, if you can find their public profile (on linkedin), include a link to that as well, and state what they do. most of them are vendors so they have some interests.

## good visualisation principles:

Effective data visualization relies on clarity, accuracy, and purpose. Prioritize a high data-to-ink ratio to minimize clutter, ensure truthful scaling (always start axes at zero for bar charts), and use purposeful color to guide the eye and highlight key trends rather than decorating.A robust framework involves adhering to a few core tenets:Choose the Right Chart: Match your visual to the data type. Use bar charts for accurate category comparisons, line charts to show trends over time, and scatter plots to spot correlations.Tell a Story: Clarify your point using annotations, clear headings, and context. Don't assume the data speaks for itself.Maintain Visual Hierarchy: Emphasize the most important insight through size, color intensity, and positioning. The viewer's attention should immediately land on the key takeaway.Apply Expressiveness: Ensure your visualization conveys all the facts but only the facts in your dataset, avoiding misleading manipulations like truncated axes or confusing 3D perspectives.For a deeper dive into these concepts and how master designers execute them, consider exploring resources from Information is Beautiful or reviewing the Tableau Best Practices.

## good design principles

1. User-CentricityAlways design with your end-user in mind. Conduct user research, prioritize their specific needs, and eliminate unnecessary features that do not solve their core problems.Action: Base your design decisions on user personas and direct feedback rather than assumptions.2. Consistency and FamiliarityUsers prefer your interface to behave the same way as other products they already know. Consistency reduces the learning curve and makes interactions feel predictable.Action: Use standardized components (like buttons and icons) and establish a cohesive design system across all screens.3. Clear Visual HierarchyGuide the user's eye to the most important elements on the page first. Important actions, primary navigation, and key information should stand out.Action: Use typography, sizing, contrast, and spacing to create a natural reading order.4. Minimize Cognitive LoadPeople get overwhelmed when presented with too much information or too many choices. Remove clutter and break complex processes into simpler, digestible steps (progressive disclosure).Action: Strip forms down to the absolute minimum required fields and hide advanced settings until needed.5. Accessibility (Inclusive Design)A good design is barrier-free and usable by everyone, including people with visual, motor, auditory, or cognitive disabilities.Action: Ensure proper color contrast, include alt text for images, and support screen readers by using semantic HTML.6. User Control and FreedomUsers make mistakes, and when they do, they should be able to recover without stress. Providing a sense of control builds trust and confidence.Action: Always include easy "undo" and "cancel" options.7. Usability and FeedbackThe system should always keep users informed about what is happening through timely, appropriate feedback.Action: Display clear loading indicators, success messages, and inline error validations so users instantly know the status of their actions.

## visual hierarchy

there's a difference between information that is "insightful" nice to know and information which action can be taken on. it's good to be able to differentiate the two when designing the dashboard. a good mix is nice to keep the reader engaged, but it's good to have multiple sections so as not to overwhelm someone.