import json, glob, re, os
from collections import Counter, defaultdict
from chapter_geo import CHAPTER_GEO
from chapter_names import CHAPTER_DISPLAY_NAMES

DASHBOARD_DIR = os.path.dirname(os.path.abspath(__file__))
ANALYSIS_DIR = os.path.dirname(DASHBOARD_DIR)
ENRICHED_DIR = os.path.join(ANALYSIS_DIR, 'enriched')
SPEAKER_ID_FILE = os.path.join(ANALYSIS_DIR, 'speaker-identities.json')
OUTPUT_FILE = os.path.join(DASHBOARD_DIR, 'dashboard_data.json')

CATEGORY_MAP = {
    'dbt best practices': 'dbt engineering practices',
    'dbt fundamentals': 'dbt engineering practices',
    'data modeling': 'dbt engineering practices',
    'developer workflow': 'dbt engineering practices',
    'project structure': 'dbt engineering practices',
    'data quality & testing': 'data quality & governance',
    'data governance': 'data quality & governance',
    'modern data stack': 'platform & architecture',
    'data warehouse & platforms': 'platform & architecture',
    'data engineering': 'platform & architecture',
    'performance & scale': 'platform & architecture',
    'data mesh': 'platform & architecture',
    'orchestration & ci/cd': 'orchestration & delivery',
    'semantic layer': 'orchestration & delivery',
    'tools & ecosystem': 'orchestration & delivery',
    'dbt product features': 'dbt product',
    'dbt product updates': 'dbt product',
    'dbt migration & adoption': 'dbt product',
    'analytics engineering': 'analytics & bi',
    'business intelligence': 'analytics & bi',
    'domain-specific use cases': 'analytics & bi',
    'team & org design': 'people & organization',
    'career development': 'people & organization',
    'community': 'people & organization',
    'genai & llm': 'emerging & trends',
    'industry trends': 'emerging & trends',
}

speaker_data = json.load(open(SPEAKER_ID_FILE))
CANON = {}
for m in speaker_data['canonical_merges']:
    for v in m['variants']:
        CANON[v] = m['canonical_name']

def canon_name(n):
    n = n.strip()
    return CANON.get(n, n)

def chapter_slug(fname):
    return fname.replace('-dbt-meetup-group.json', '').replace('-dbt-meetup.json', '').replace('.json', '')

chapters = {}
all_talks = []  # flat list with chapter, date, topics, category, speaker
topic_counter = Counter()
category_counter = Counter()
speaker_chapters = defaultdict(set)
speaker_talk_count = Counter()
monthly_events = Counter()  # YYYY-MM -> count
yearly_events = Counter()
format_counter = Counter()  # online vs in-person

for path in sorted(glob.glob(f'{ENRICHED_DIR}/*.json')):
    fname = path.split('/')[-1]
    slug = chapter_slug(fname)
    data = json.load(open(path))
    events = data.get('events', [])

    ch_talks = 0
    ch_attendees = []
    ch_topics = Counter()
    ch_categories = Counter()
    ch_speakers = set()
    ch_dates = []
    ch_online = 0
    ch_inperson = 0
    ch_yearly = Counter()
    ch_events_detail = []

    for event in events:
        d = event.get('date')
        if d:
            ch_dates.append(d)
            ym = d[:7]
            monthly_events[ym] += 1
            yearly_events[d[:4]] += 1
            ch_yearly[d[:4]] += 1
        loc = (event.get('location') or '')
        is_online = 'online' in loc.lower()
        if is_online:
            ch_online += 1
            format_counter['online'] += 1
        else:
            ch_inperson += 1
            format_counter['in-person'] += 1
        a = event.get('attendees')
        if a is not None:
            ch_attendees.append(a)

        event_talks_detail = []

        for talk in (event.get('talks') or []):
            ch_talks += 1
            topics = talk.get('topics') or []
            primary_cat = CATEGORY_MAP.get(topics[0], None) if topics else None
            for t in topics:
                topic_counter[t] += 1
                ch_topics[t] += 1
            if primary_cat:
                category_counter[primary_cat] += 1
                ch_categories[primary_cat] += 1

            raw_speaker = talk.get('speaker_name')
            if raw_speaker:
                # split multi-speaker strings on comma/& for per-person attribution
                parts = re.split(r',| & |\band\b', raw_speaker)
                for p in parts:
                    p = p.strip()
                    if not p:
                        continue
                    cn = canon_name(p)
                    ch_speakers.add(cn)
                    speaker_chapters[cn].add(slug)
                    speaker_talk_count[cn] += 1

            all_talks.append({
                'chapter': slug,
                'event_name': event.get('event_name'),
                'event_url': event.get('event_url'),
                'date': d,
                'title': talk.get('title'),
                'description': talk.get('description'),
                'speaker': raw_speaker,
                'speaker_title': talk.get('speaker_title'),
                'topics': topics,
                'category': primary_cat,
            })

            event_talks_detail.append({
                'title': talk.get('title'),
                'description': talk.get('description'),
                'speaker': raw_speaker,
                'speaker_title': talk.get('speaker_title'),
                'topics': topics,
            })

        ch_events_detail.append({
            'event_name': event.get('event_name'),
            'event_url': event.get('event_url'),
            'date': d,
            'location': loc,
            'attendees': a,
            'talks': event_talks_detail,
        })

    geo = CHAPTER_GEO[slug]
    chapters[slug] = {
        'slug': slug,
        'display_name': CHAPTER_DISPLAY_NAMES[slug],
        'city': geo['city'],
        'country': geo['country'],
        'lat': geo['lat'],
        'lon': geo['lon'],
        'total_events': len(events),
        'total_talks': ch_talks,
        'avg_talks_per_event': round(ch_talks / len(events), 2) if events else 0,
        'avg_attendees': round(sum(ch_attendees) / len(ch_attendees), 1) if ch_attendees else None,
        'max_attendees': max(ch_attendees) if ch_attendees else None,
        'total_attendee_appearances': sum(ch_attendees) if ch_attendees else 0,
        'unique_speakers': len(ch_speakers),
        'top_topics': ch_topics.most_common(5),
        'top_categories': ch_categories.most_common(),
        'first_event_date': min(ch_dates) if ch_dates else None,
        'last_event_date': max(ch_dates) if ch_dates else None,
        'online_events': ch_online,
        'in_person_events': ch_inperson,
        'yearly_events': dict(sorted(ch_yearly.items())),
        'events_detail': sorted(ch_events_detail, key=lambda e: e['date'] or '', reverse=True),
    }

# repeat speakers across chapters, sorted
repeat_speakers = []
for name, chs in speaker_chapters.items():
    if len(chs) > 1:
        repeat_speakers.append({
            'name': name,
            'chapters': sorted(chs),
            'chapter_count': len(chs),
            'talk_count': speaker_talk_count[name],
        })
repeat_speakers.sort(key=lambda x: (-x['chapter_count'], -x['talk_count']))

output = {
    'generated': '2026-07-05',
    'summary': {
        'total_chapters': len(chapters),
        'total_events': sum(c['total_events'] for c in chapters.values()),
        'total_talks': sum(c['total_talks'] for c in chapters.values()),
        'total_unique_speakers': len(speaker_chapters) + sum(1 for n, chs in speaker_chapters.items() if len(chs)==1) - len(speaker_chapters) + len(speaker_chapters),
        'date_range': [min(monthly_events.keys()) if monthly_events else None, max(monthly_events.keys()) if monthly_events else None],
        'format_split': dict(format_counter),
    },
    'chapters': chapters,
    'topic_distribution': topic_counter.most_common(),
    'category_distribution': category_counter.most_common(),
    'monthly_event_counts': dict(sorted(monthly_events.items())),
    'yearly_event_counts': dict(sorted(yearly_events.items())),
    'repeat_speakers': repeat_speakers,
    'all_talks': all_talks,
}

# fix total_unique_speakers properly
all_speaker_names = set(speaker_chapters.keys())
output['summary']['total_unique_speakers'] = len(all_speaker_names)

with open(OUTPUT_FILE, 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print('Chapters:', len(chapters))
print('Total events:', output['summary']['total_events'])
print('Total talks:', output['summary']['total_talks'])
print('Unique speakers:', output['summary']['total_unique_speakers'])
print('Repeat speakers:', len(repeat_speakers))
print('Category distribution:', output['category_distribution'])
