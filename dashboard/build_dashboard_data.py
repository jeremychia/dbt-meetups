import json, glob, re, os, time, datetime
from collections import Counter, defaultdict
from chapter_geo import CHAPTER_GEO
from chapter_names import CHAPTER_DISPLAY_NAMES
from regions import region_for

DASHBOARD_DIR = os.path.dirname(os.path.abspath(__file__))
ANALYSIS_DIR = os.path.dirname(DASHBOARD_DIR)
# Env overrides let the pipeline build against a copy of the data (tests).
ENRICHED_DIR = os.environ.get('DASHBOARD_ENRICHED_DIR', os.path.join(ANALYSIS_DIR, 'enriched'))
SPEAKER_ID_FILE = os.environ.get('DASHBOARD_SPEAKER_FILE', os.path.join(ANALYSIS_DIR, 'pipeline', 'speaker-identities.json'))
OUTPUT_FILE = os.environ.get('DASHBOARD_OUTPUT_FILE', os.path.join(DASHBOARD_DIR, 'dashboard_data.json'))

DAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Rolls each of the 26 enrichment topics (pipeline/past-meetups.md
# "topic vocabulary") up into one of 8 display categories. Kept as a plain
# dict (rather than generated from past-meetups.md) so the two must be
# updated in lockstep by hand; tests/test_build_dashboard_data.py asserts
# every topic in the vocabulary has an entry here so drift is caught.
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


def in_trailing_year(date_str, today_iso, trailing_start):
    return bool(date_str) and trailing_start <= date_str <= today_iso


def in_prior_trailing_year(date_str, prior_trailing_start, prior_trailing_end):
    return bool(date_str) and prior_trailing_start <= date_str < prior_trailing_end


def parse_start_hour(time_str):
    # time_str like "18:00-21:00" -> 18
    if not time_str:
        return None
    m = re.match(r'^(\d{1,2}):(\d{2})', time_str)
    if not m:
        return None
    return int(m.group(1))


def chapter_slug(fname):
    return fname.replace('-dbt-meetup-group.json', '').replace('-dbt-meetup.json', '').replace('.json', '')


def load_canon_map(speaker_id_file):
    with open(speaker_id_file) as f:
        speaker_data = json.load(f)
    canon = {}
    for m in speaker_data['canonical_merges']:
        for v in m['variants']:
            canon[v] = m['canonical_name']
    return canon


def build_output(enriched_dir, speaker_id_file, today=None):
    """Reads every enriched/<slug>.json + speaker-identities.json and returns
    the full dashboard_data.json dict. Pure function of its inputs (plus
    `today`, which only affects trailing-window/active-status fields) - no
    file writes, so it's safe to call from tests with fixture directories.
    """
    today = today or datetime.date.today()
    today_iso = today.isoformat()
    trailing_start = (today - datetime.timedelta(days=365)).isoformat()
    prior_trailing_start = (today - datetime.timedelta(days=730)).isoformat()
    prior_trailing_end = trailing_start
    at_risk_cutoff = (today - datetime.timedelta(days=270)).isoformat()

    canon = load_canon_map(speaker_id_file)

    def canon_name(n):
        return canon.get(n.strip(), n.strip())

    chapters = {}
    all_talks = []  # flat list with chapter, date, topics, category, speaker
    topic_counter = Counter()
    category_counter = Counter()
    region_category_counter = defaultdict(Counter)  # region_group -> {category: count}
    topic_sample_talks = defaultdict(list)  # category -> [{title, speaker, chapter, date, attendees}]
    speaker_chapters = defaultdict(set)
    speaker_talk_count = Counter()
    monthly_events = Counter()  # YYYY-MM -> count
    yearly_events = Counter()
    format_counter = Counter()  # online vs in-person
    weekday_counter = Counter()  # 'Monday'.. -> count
    day_of_month_counter = Counter()  # 1..31 -> count
    start_hour_counter = Counter()  # 0..23 -> count
    region_yearly_events = defaultdict(Counter)  # region_group -> {year: count}
    trailing_events_total = 0
    prior_trailing_events_total = 0
    trailing_talks_total = 0
    prior_trailing_talks_total = 0
    trailing_attendees_total = 0

    for path in sorted(glob.glob(f'{enriched_dir}/*.json')):
        fname = path.split('/')[-1]
        if fname.startswith('_'):  # pipeline state files, not chapter data
            continue
        slug = chapter_slug(fname)
        geo = CHAPTER_GEO.get(slug)
        region_info = region_for(geo['country']) if geo and geo.get('country') else {'sub_region': None, 'region_group': None}
        with open(path) as f:
            data = json.load(f)
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
        ch_trailing_events = 0
        ch_prior_trailing_events = 0
        ch_trailing_talks = 0
        ch_trailing_attendees = []

        for event in events:
            d = event.get('date')
            if d:
                ch_dates.append(d)
                ym = d[:7]
                monthly_events[ym] += 1
                yearly_events[d[:4]] += 1
                ch_yearly[d[:4]] += 1
                try:
                    weekday_counter[DAY_NAMES[datetime.date.fromisoformat(d).weekday()]] += 1
                    day_of_month_counter[datetime.date.fromisoformat(d).day] += 1
                except ValueError:
                    pass
                if region_info['region_group']:
                    region_yearly_events[region_info['region_group']][d[:4]] += 1
                if in_trailing_year(d, today_iso, trailing_start):
                    trailing_events_total += 1
                    ch_trailing_events += 1
                if in_prior_trailing_year(d, prior_trailing_start, prior_trailing_end):
                    prior_trailing_events_total += 1
                    ch_prior_trailing_events += 1
            hour = parse_start_hour(event.get('time'))
            if hour is not None:
                start_hour_counter[hour] += 1
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
                if d and in_trailing_year(d, today_iso, trailing_start):
                    trailing_attendees_total += a
                    ch_trailing_attendees.append(a)

            event_talks_detail = []

            for talk in (event.get('talks') or []):
                ch_talks += 1
                if d and in_trailing_year(d, today_iso, trailing_start):
                    trailing_talks_total += 1
                    ch_trailing_talks += 1
                if d and in_prior_trailing_year(d, prior_trailing_start, prior_trailing_end):
                    prior_trailing_talks_total += 1
                topics = talk.get('topics') or []
                primary_cat = CATEGORY_MAP.get(topics[0], None) if topics else None
                for t in topics:
                    topic_counter[t] += 1
                    ch_topics[t] += 1
                if primary_cat:
                    category_counter[primary_cat] += 1
                    ch_categories[primary_cat] += 1
                    if region_info['region_group']:
                        region_category_counter[region_info['region_group']][primary_cat] += 1
                    topic_sample_talks[primary_cat].append({
                        'title': talk.get('title'),
                        'description': talk.get('description'),
                        'speaker': talk.get('speaker_name'),
                        'chapter': slug,
                        'date': d,
                        'attendees': a,
                        'event_url': event.get('event_url'),
                    })

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
                'start_hour': hour,
                'is_online': is_online,
            })

        if geo is None:
            print(f'WARNING: {slug} missing from chapter_geo.py — add it (skipping map placement)')
            geo = {'city': slug, 'country': None, 'lat': None, 'lon': None}

        last_event_date = max(ch_dates) if ch_dates else None
        is_active = bool(last_event_date) and last_event_date >= trailing_start
        is_at_risk = is_active and last_event_date < at_risk_cutoff

        chapters[slug] = {
            'slug': slug,
            'display_name': CHAPTER_DISPLAY_NAMES.get(slug, slug),
            'city': geo['city'],
            'country': geo['country'],
            'lat': geo['lat'],
            'lon': geo['lon'],
            'region_group': region_info['region_group'],
            'sub_region': region_info['sub_region'],
            'total_events': len(events),
            'total_talks': ch_talks,
            'avg_talks_per_event': round(ch_talks / len(events), 2) if events else 0,
            'avg_attendees': round(sum(ch_attendees) / len(ch_attendees), 1) if ch_attendees else None,
            'min_attendees': min(ch_attendees) if ch_attendees else None,
            'max_attendees': max(ch_attendees) if ch_attendees else None,
            'total_attendee_appearances': sum(ch_attendees) if ch_attendees else 0,
            'unique_speakers': len(ch_speakers),
            'top_topics': ch_topics.most_common(5),
            'top_categories': ch_categories.most_common(),
            'first_event_date': min(ch_dates) if ch_dates else None,
            'last_event_date': last_event_date,
            'online_events': ch_online,
            'in_person_events': ch_inperson,
            'yearly_events': dict(sorted(ch_yearly.items())),
            'events_detail': sorted(ch_events_detail, key=lambda e: e['date'] or '', reverse=True),
            'is_active': is_active,
            'is_at_risk': is_at_risk,
            'trailing_12mo_events': ch_trailing_events,
            'prior_trailing_12mo_events': ch_prior_trailing_events,
            'trailing_12mo_talks': ch_trailing_talks,
            'trailing_12mo_avg_attendees': round(sum(ch_trailing_attendees) / len(ch_trailing_attendees), 1) if ch_trailing_attendees else None,
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

    active_chapters = [c for c in chapters.values() if c['is_active']]
    dormant_chapters = [c for c in chapters.values() if not c['is_active']]
    at_risk_chapters = [c for c in chapters.values() if c['is_at_risk']]

    # chapters "active last year": any event fell within the prior 12mo window
    prior_active_count = sum(1 for c in chapters.values() if c['prior_trailing_12mo_events'] > 0)
    active_chapters_yoy_pct = (
        round(100 * (len(active_chapters) - prior_active_count) / prior_active_count, 1)
        if prior_active_count else None
    )

    events_yoy_pct = (
        round(100 * (trailing_events_total - prior_trailing_events_total) / prior_trailing_events_total, 1)
        if prior_trailing_events_total else None
    )

    all_speaker_names = set(speaker_chapters.keys())

    output = {
        'generated': time.strftime('%Y-%m-%d'),
        'date_computed_as_of': today_iso,
        'summary': {
            'total_chapters': len(chapters),
            'total_events': sum(c['total_events'] for c in chapters.values()),
            'total_talks': sum(c['total_talks'] for c in chapters.values()),
            'total_unique_speakers': len(all_speaker_names),
            'date_range': [min(monthly_events.keys()) if monthly_events else None, max(monthly_events.keys()) if monthly_events else None],
            'format_split': dict(format_counter),
            'active_chapters': len(active_chapters),
            'dormant_chapters': len(dormant_chapters),
            'at_risk_chapters': len(at_risk_chapters),
            'active_chapters_yoy_pct': active_chapters_yoy_pct,
            'trailing_12mo_events': trailing_events_total,
            'prior_trailing_12mo_events': prior_trailing_events_total,
            'events_yoy_pct': events_yoy_pct,
            'trailing_12mo_talks': trailing_talks_total,
            'prior_trailing_12mo_talks': prior_trailing_talks_total,
            'trailing_12mo_avg_talks_per_event': round(trailing_talks_total / trailing_events_total, 2) if trailing_events_total else None,
            'trailing_12mo_attendees': trailing_attendees_total,
        },
        'chapters': chapters,
        'topic_distribution': topic_counter.most_common(),
        'category_distribution': category_counter.most_common(),
        'region_category_distribution': {
            region: counter.most_common() for region, counter in region_category_counter.items()
        },
        'category_topics': {
            cat: sorted(t for t, c in CATEGORY_MAP.items() if c == cat)
            for cat in sorted(set(CATEGORY_MAP.values()))
        },
        'topic_sample_talks': {
            cat: sorted(talks, key=lambda t: t['date'] or '', reverse=True)[:8]
            for cat, talks in topic_sample_talks.items()
        },
        'monthly_event_counts': dict(sorted(monthly_events.items())),
        'yearly_event_counts': dict(sorted(yearly_events.items())),
        'region_yearly_events': {region: dict(sorted(years.items())) for region, years in region_yearly_events.items()},
        'weekday_event_counts': {day: weekday_counter.get(day, 0) for day in DAY_NAMES},
        'day_of_month_event_counts': {str(d): day_of_month_counter.get(d, 0) for d in range(1, 32)},
        'start_hour_event_counts': {str(h): start_hour_counter.get(h, 0) for h in range(24)},
        'repeat_speakers': repeat_speakers,
        'all_talks': all_talks,
    }
    return output


def main():
    output = build_output(ENRICHED_DIR, SPEAKER_ID_FILE)

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print('Chapters:', output['summary']['total_chapters'])
    print('Total events:', output['summary']['total_events'])
    print('Total talks:', output['summary']['total_talks'])
    print('Unique speakers:', output['summary']['total_unique_speakers'])
    print('Repeat speakers:', len(output['repeat_speakers']))
    print('Category distribution:', output['category_distribution'])


if __name__ == '__main__':
    main()
