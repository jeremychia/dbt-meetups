"""Turns find_local_speakers.py candidates into an assemble.py raw file, without lookups.

usage, from the repo root:
  python3 research/add_local_people.py <candidates.json> <city folder> "<town>,<town>" <raw out.json> [--github-only] [--github-cap 100]
  python3 research/assemble.py <raw out.json> <city file> --base <city file>

- speakers at in-person data talks since 2024 become proven speakers with an unverified location: a talk at a local event
  does not show where someone lives. a free-text speaker field is split into people, titles and self-stated pronouns.
- organisers of local data groups become connectors.
- github data people whose location names one of the towns become tier 3 attendee leads, ranked by how close their bio is
  to analytics engineering and capped per city. a country or state alone is not a town.
- a linkedin link from an event record counts only when its slug fits the person's name: one record can carry a co-speaker's link.
"""
import json,re,sys,unicodedata
CAND,city,places,OUT=sys.argv[1],sys.argv[2],[p.strip() for p in sys.argv[3].split(',')],sys.argv[4]
gh_only='--github-only' in sys.argv
CAP=int(sys.argv[sys.argv.index('--github-cap')+1]) if '--github-cap' in sys.argv else 100
TALK=re.compile(r"\b(data|analytics|dbt|sql|model(l)?ing|warehous|lakehouse|pipeline|\bbi\b|dashboard|tableau|power ?bi|snowflake|databricks|governance|quality|semantic|etl|elt|airflow|dagster|duckdb|iceberg|spark|kafka|stream|metrics|looker|bigquery|redshift|fabric|catalog|lineage)",re.I)
CORE=re.compile(r"\b(dbt|analytics engineer|model(l)?ing|semantic|data quality|governance|warehous|lakehouse)",re.I)
GROUP=re.compile(r"\b(data|analytics|dbt|sql|snowflake|databricks|tableau|power ?bi|fabric|pydata|pyladies|r-?ladies|women in (data|tech)|wids|big data|postgres|data engineering)",re.I)
NOTGROUP=re.compile(r"android|yoga|meditation|cyber|security|crypto|blockchain|real estate|life science|biotech",re.I)
STUDENT=re.compile(r"\b(student|intern|aspiring|enthusiast|undergrad|graduate student|open to work|seeking|looking for|learner|bootcamp|candidate|class of)\b",re.I)
SENIOR=re.compile(r"\b(engineer|analyst|architect|manager|lead|head|director|consultant|scientist|developer|founder|principal|staff|senior)\b",re.I)
ORG=re.compile(r'\b(numfocus|community|user groups?|events|labs|social|meetup|team|group|dbt)\b',re.I)

TITLE_WORDS=re.compile(r"\b(cto|ceo|coo|cfo|founder|co-?founder|director|head|lead|manager|engineer|architect|analyst|scientist|consultant|developer|mvp|advocate|evangelist|specialist|officer|president|vp|principal|staff|senior|professor|mentor|researcher|student|data|at)\b",re.I)
ORGNAME=re.compile(r"\b(software|solutions|consulting|italia|inc|ltd|llc|gmbh|group|team|community|association|foundation|university|labs?)\b",re.I)
SUFFIX=re.compile(r",?\s*\b(ph\.?\s?d\.?|mba|m\.?s\.?|m\.?eng|p\.?eng|mpa|mvp|dr\.?)\b\.?",re.I)
PRONOUNS=re.compile(r"\((she|he|they)\s*[/,]\s*(her|him|them|hers|his|theirs)\)",re.I)
def people_in(raw):
    """splits a free-text speaker field into (name, company, title, pronouns): several names, a title after the name, stated pronouns."""
    s=re.sub(r"https?://\S+","",raw or "").strip()
    pron=[f"{a.lower()}/{b.lower()}" for a,b in PRONOUNS.findall(s)]
    s=PRONOUNS.sub("",s)
    if re.search(r"\b(is an?|wrote|has been|i am|i'm)\b",s,re.I):  # a bio in the name field: keep the leading name only
        s=re.split(r"\b(is an?|wrote|has been|i am|i'm)\b",s,flags=re.I)[0]
    parts=[x for x in re.split(r"\s*(?:\||;|&|\band\b|---|\d+\.\s)\s*",s) if x and x.strip()]
    out=[]
    for part in parts:
        raw_bits=[b.strip() for b in part.split(",") if b.strip()]
        firm={re.sub(r"\(.*?\)","",b).strip(): (re.search(r"\(([^)]+)\)",b) or [None,None])[1] for b in raw_bits}  # each name keeps its own (company)
        bits=[b for b in firm if b]
        names=[b for b in bits if not TITLE_WORDS.search(b) and not SUFFIX.fullmatch(b) and not ORGNAME.search(b)]
        title=", ".join(b for b in bits if TITLE_WORDS.search(b)) or None
        for n in (names if len(names)>1 and all(len(x.split())>=2 for x in names) else names[:1]):
            company=firm.get(n)
            if company and (TITLE_WORDS.search(company) or re.search(r"\beng\b",company,re.I)):  # (data architect) is a role, not a company
                title, company = title or company, None
            n=re.sub(r"\(.*?\)","",n); n=SUFFIX.sub("",n)
            n=re.split(r"\s+(?:-|–|@|at)\s+",n)[0].strip(" .,-–")
            n=re.sub(r"(?<=[a-z])[A-Z][a-z]+$","",n).strip()  # a name run into the next word: RussoMarco
            if 2<=len(n.split())<=5 and re.fullmatch(r"[^\d@:/]+",n): out.append((n,company,title,pron[0] if pron else None))
    return out

def norm(s): return " ".join(re.sub(r"[^a-z ]"," ",unicodedata.normalize("NFKD",re.sub(r"\(.*?\)","",s or "")).encode("ascii","ignore").decode().lower()).split())
towns=[norm(p) for p in places if len(norm(p))>2]
d=json.load(open(CAND))
sp,ho,gh={},{},{}
for r in d['candidates']:
    if r['known'] or len(norm(r['name']).split())<2: continue
    if r['source']=='github':
        loc=norm(r.get('location')); bio=r.get('title') or ''
        if STUDENT.search(bio) or not SENIOR.search(bio+' '+(r.get('company') or '')) or not any(t in loc for t in towns): continue
        gh.setdefault(r['name'],r)
    elif gh_only: continue
    elif r['role']=='host':
        if GROUP.search(r['group']) and not NOTGROUP.search(r['group']) and r['date']>='2024-01-01' and not ORG.search(r['name']): ho.setdefault(r['name'],r)
    elif r.get('in_person') and r['date']>='2024-01-01' and TALK.search(r['event']) and not NOTGROUP.search(r['group']):
        sp.setdefault(r['name'],[]).append(r)

GH_WEIGHTS=[(re.compile(r'\bdbt\b',re.I),5),(re.compile(r'analytics engineer',re.I),4),(re.compile(r'snowflake|looker|bigquery|redshift|warehouse|data model',re.I),2),(re.compile(r'business intelligence|\bbi\b|tableau|power ?bi',re.I),2),(re.compile(r'data engineer',re.I),2),(re.compile(r'analyst|data architect|data platform',re.I),1)]
AE_ROLE=re.compile(r"\b(dbt|analytics engineer|analytics engineering|data engineer|data engineering|analyst|business intelligence|\bbi\b|data architect|data platform|warehouse|snowflake|looker|tableau|power ?bi|data model)",re.I)
def gh_score(r): return sum(w for rx,w in GH_WEIGHTS if rx.search(r.get('title') or ''))+(1 if r.get('company') else 0)+(1 if any('linkedin.com/in/' in l or 'x.com' in l or 'twitter.com' in l for l in r['links']) else 0)
gh=dict(sorted(((n,r) for n,r in gh.items() if AE_ROLE.search(r.get('title') or '')),key=lambda nr:gh_score(nr[1]),reverse=True)[:CAP])
def topics(t):
    t=' '+t.lower(); out=[]
    for k,v in [('model','data modeling'),('semantic','semantic layer'),('quality','data quality & testing'),('governance','data governance'),('warehous','data warehouse & platforms'),('lakehouse','data warehouse & platforms'),('snowflake','data warehouse & platforms'),('databricks','data warehouse & platforms'),('tableau','business intelligence'),('power bi','business intelligence'),('dashboard','business intelligence'),('pipeline','data engineering'),('stream','data engineering'),('kafka','data engineering'),('spark','data engineering'),('airflow','orchestration & ci/cd'),('dagster','orchestration & ci/cd'),('dbt','analytics engineering'),('analytics','analytics engineering'),(' ai','genai & llm'),('llm','genai & llm'),('data','data engineering')]:
        if k in t and v not in out: out.append(v)
    return (out or ['community'])[:3]
comps={}
def add(emp,p): comps.setdefault(emp,{'name':emp,'type':'independent' if emp.startswith('Independent') else 'employer','cities':[places[0]],'local_presence':'not_confirmed','dbt_signal':'weak','stack_signals':[],'job_postings':[],'other_evidence':[],'notes':None,'people':[]})['people'].append(p)
expanded={}
for raw_name,rs in sp.items():
    ho.pop(raw_name,None)
    for name,comp,title,pron in people_in(raw_name):
        expanded.setdefault(name,{'rs':[],'company':comp,'title':title,'pronouns':pron})['rs']+=rs
for name,x in expanded.items():
    rs=x['rs']
    sys.path.insert(0,'research'); from harvest_profiles import slug_fits_name, matches_name, tokens
    fits=lambda u: (lambda slug: slug_fits_name(slug,{'name':name}) or matches_name(slug,tokens(name)))(u.rstrip('/').split('/in/')[-1].split('?')[0])
    li=[l for l in rs[0]['links'] if '/in/' in l and 'ACoAA' not in l and fits(l)][:1]  # an event record can carry a co-speaker's link
    li=[('https://'+u if not u.startswith('http') else u).split('?')[0] for u in li]
    ev=[{'type':'talk','event':r['group'],'title':r['event'],'date':r['date'],'url':r['url'],'co_authors':[],'description':'speaker named in the event record','topics':topics(r['event']),'url_precision':'direct','confidence':'high'} for r in rs[:3]]
    add(rs[0].get('company') or x['company'] or 'Independent / no company',{'name':name,'title':rs[0].get('title') or x['title'],'city':None,'based_in_region':None,'pronouns':x['pronouns'],'linkedin_urls':li,'linkedin_confidence':'medium' if li else 'not_searched','lead_type':'proven_speaker','sourced_via':['conference_or_meetup_agenda'],'priority_tier':'2' if any(CORE.search(r['event']) for r in rs) else '3','confidence':'Medium','suggested_talk_angle':None,'notes':'speaker at a local data group; location unverified, since a talk at a local event does not show where someone lives' + ('; linkedin linked from the event record' if li else ''),'speaker_evidence':ev})
hosts={}
for raw_name,r in ho.items():
    for name,comp,title,pron in people_in(raw_name):
        if name not in expanded: hosts.setdefault(name,r)
for name,r in hosts.items():
    ev=[{'type':'organiser','event':r['group'],'title':f"organiser, {r['group']}",'date':r['date'],'url':r['url'],'co_authors':[],'description':'host of the event in the meetup record','topics':['community'],'url_precision':'direct','confidence':'high'}]
    add('Independent / no company',{'name':name,'title':None,'city':None,'based_in_region':True,'pronouns':None,'linkedin_urls':[],'linkedin_confidence':'not_searched','lead_type':'proven_speaker','sourced_via':['conference_or_meetup_agenda'],'priority_tier':'connector','confidence':'Medium','suggested_talk_angle':None,'notes':'organiser of an in-person local data group','speaker_evidence':ev})
for raw_name,r in gh.items():
    found=people_in(raw_name)
    if not found: continue
    name=found[0][0]
    li=[s for s in r['links'] if 'linkedin.com/in/' in s][:1]
    prof=[{'type':'github','url':r['url'],'source':'github user search by location'}]+[{'type':'x','url':s.replace('twitter.com','x.com'),'source':r['url']+' profile'} for s in r['links'] if 'x.com' in s or 'twitter.com' in s][:1]
    add(r.get('company') or 'Independent / no company',{'name':name,'title':r.get('title'),'city':r.get('location'),'based_in_region':True,'pronouns':None,'linkedin_urls':li,'linkedin_confidence':'high' if li else 'not_searched','profile_urls':prof,'lead_type':'no_public_content','sourced_via':['github'],'priority_tier':'3','confidence':'High','suggested_talk_angle':None,'notes':f"github profile {r['url']} gives the location {r.get('location')}",'speaker_evidence':[]})
f=__import__('glob').glob(f'{city}/*_dbt_companies.json')[0]; base=json.load(open(f)); src=base['sources'] or {}
raw={'city':places[0],'chapter_name':base['metadata']['region'].split('(',1)[-1].rstrip(')') if '(' in base['metadata']['region'] else places[0],'enriched_file':src.get('past_meetups_derived_from'),'chapter_url':src.get('chapter_past_events'),
     'method':'people pass with research/find_local_speakers.py and no lookups: speakers and organisers of local data groups and bevy chapters, and github data people with a town in the region. speakers keep an unverified location.' if not gh_only else 'github pass with the faster find_local_speakers.py: data people with a town in the region.',
     'lessons':[],'caveats':['Speakers found through local groups have an unverified location: a talk at a local event does not show where someone lives.'] if not gh_only else [],'sources_checked':[],'community_channels':[{'name':v,'url':f'https://www.meetup.com/{k}/','note':'local data group found by groupSearch'} for k,v in d['meetup_groups'].items() if GROUP.search(v) and not NOTGROUP.search(v)] if not gh_only else [],'companies':list(comps.values())}
json.dump(raw,open(OUT,'w'),ensure_ascii=False,indent=1)
print(f'{city}: speakers {len(sp)} organisers {len(ho)} github {len(gh)}')
