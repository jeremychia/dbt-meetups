"""Gives a person the linkedin profile their record in another city file already has, when the name and employer match.

usage, from the repo root: python3 research/copy_across_cities.py [--apply]   (without --apply it lists the matches)

a speaker often sits in several chapters, and a search can find them in one and miss them in another. a match needs the same
full name and the same employer, so "Independent / no company" never matches. the profile goes through apply_contacts.py,
so rejected_matches.json and the location check still apply.
"""

import glob, json, os, re, subprocess, sys, tempfile, unicodedata
from collections import defaultdict
from validate import reachable


def norm(s):
    return " ".join(re.sub(r"[^a-z ]", " ", unicodedata.normalize("NFKD", re.sub(r"\(.*?\)", "", s or "")).encode("ascii", "ignore").decode().lower()).split())


def employer(s):
    return re.sub(r"\b(inc|ltd|llc|gmbh|group|the|ag|sa|bv)\b", "", norm(s)).strip()


def matches():
    have, need = defaultdict(list), []
    for f in sorted(glob.glob("*/*_dbt_companies.json")):
        for c in json.load(open(f))["companies"]:
            for p in c["people"]:
                row = (f, p, norm(p["name"]), employer(c["name"]))
                if p["has_linkedin"]:
                    have[row[2]].append(row)
                elif not reachable(p):
                    need.append(row)
    out = {}
    for f, p, name, emp in need:
        if len(name.split()) < 2 or not emp or "independent" in emp:
            continue
        found = {o["linkedin_urls"][0]: of for of, o, _, oe in have.get(name, []) if of != f and oe and (emp == oe or emp in oe or oe in emp)}
        if len(found) == 1:  # two different profiles for one name and employer is a miss
            url, of = next(iter(found.items()))
            out.setdefault(f, {})[p["id"]] = {"linkedin_url": url, "evidence": f"same name and employer as the record in {os.path.dirname(of)}", "confidence": "medium", "based_in_region": None, "city": None}
    return out


if __name__ == "__main__":
    found = matches()
    for f, patch in found.items():
        for pid, v in patch.items():
            print(f"{os.path.dirname(f)}/{pid}: {v['linkedin_url']} ({v['evidence']})")
    if "--apply" in sys.argv:
        for f, patch in found.items():
            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as t:
                json.dump(patch, t)
            subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "apply_contacts.py"), f, t.name], check=True)
            os.unlink(t.name)
