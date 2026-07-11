"""Incremental speaker-identity update.

Recomputes repeat_speakers_across_chapters in speaker-identities.json from the
current enriched/*.json, applying the existing canonical_merges. New name
variants are handled conservatively:

- names that are identical after normalization (case, diacritics, whitespace)
  are auto-merged and appended to canonical_merges with method
  "auto-exact-normalized";
- fuzzy near-matches (difflib ratio >= 0.87) involving names not seen before
  are written to a "pending_review" list for a human to confirm — they are
  NOT merged automatically, matching how the original file was built.

Idempotent: rerunning without new data changes nothing.
"""

import json
import re
import time
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher

import config

FUZZY_THRESHOLD = 0.87
SPLIT_RE = re.compile(r",| & |\band\b")


def normalize(name: str) -> str:
    n = unicodedata.normalize("NFD", name.strip().casefold())
    n = "".join(c for c in n if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", n)


def collect_speakers() -> dict[str, set[str]]:
    """raw speaker name -> set of short chapter slugs where they appeared."""
    speakers = defaultdict(set)
    for path in sorted(config.ENRICHED_DIR.glob("*.json")):
        if path.name.startswith("_"):
            continue
        chapter = config.chapter_slug(path.name)
        data = json.loads(path.read_text())
        for event in data.get("events", []):
            for talk in event.get("talks") or []:
                raw = talk.get("speaker_name")
                if not raw:
                    continue
                for part in SPLIT_RE.split(raw):
                    part = part.strip()
                    if part:
                        speakers[part].add(chapter)
    return speakers


def main():
    identities = json.loads(config.SPEAKER_ID_FILE.read_text())
    canon = {}
    for merge in identities.get("canonical_merges", []):
        for variant in merge["variants"]:
            canon[variant] = merge["canonical_name"]
    known_names = set(canon)
    for entry in identities.get("repeat_speakers_across_chapters", []):
        known_names.add(entry["canonical_name"])
    confirmed_different = set()
    for entry in identities.get("confirmed_different_people", []):
        confirmed_different.add(frozenset(entry["names"]))

    speakers = collect_speakers()

    # 1. Auto-merge exact-normalized duplicates not yet covered by a merge.
    by_norm = defaultdict(list)
    for name in speakers:
        by_norm[normalize(name)].append(name)
    new_merges = 0
    for variants in by_norm.values():
        if len(variants) < 2:
            continue
        unmapped = [v for v in variants if v not in canon]
        if not unmapped:
            continue
        existing_canonical = next((canon[v] for v in variants if v in canon), None)
        # Prefer the variant with diacritics/most characters as canonical.
        canonical = existing_canonical or max(variants, key=len)
        merge = next(
            (
                m
                for m in identities["canonical_merges"]
                if m["canonical_name"] == canonical
            ),
            None,
        )
        if merge is None:
            merge = {
                "canonical_name": canonical,
                "variants": [],
                "method": "auto-exact-normalized",
            }
            identities["canonical_merges"].append(merge)
        for v in variants:
            if v not in merge["variants"]:
                merge["variants"].append(v)
            canon[v] = canonical
        merge["variants"].sort()
        new_merges += 1

    # 2. Flag fuzzy candidates involving names not previously reviewed.
    def canonical_name(n: str) -> str:
        return canon.get(n, n)

    all_names = sorted(speakers)
    new_names = [n for n in all_names if n not in known_names]
    pending = {frozenset(p["names"]) for p in identities.get("pending_review", [])}
    new_pending = []
    for new in new_names:
        n_new = normalize(new)
        for other in all_names:
            if other == new or canonical_name(other) == canonical_name(new):
                continue
            n_other = normalize(other)
            if n_new == n_other:
                continue  # handled by exact merge above
            ratio = SequenceMatcher(None, n_new, n_other).ratio()
            if ratio < FUZZY_THRESHOLD:
                continue
            pair = frozenset([new, other])
            if pair in confirmed_different or pair in pending:
                continue
            pending.add(pair)
            new_pending.append(
                {
                    "names": sorted(pair),
                    "similarity": round(ratio, 3),
                    "note": "fuzzy match involving a new speaker name — review and either add to canonical_merges or confirmed_different_people",
                }
            )
    if new_pending:
        identities.setdefault("pending_review", []).extend(new_pending)

    # 3. Recompute repeat speakers across chapters (fully derivable).
    chapters_by_canonical = defaultdict(set)
    count_by_canonical = defaultdict(int)
    for name, chapters in speakers.items():
        cn = canonical_name(name)
        chapters_by_canonical[cn] |= chapters
        count_by_canonical[cn] += len(chapters)
    repeat = [
        {
            "canonical_name": cn,
            "chapters": sorted(chs),
            "appearance_count": count_by_canonical[cn],
        }
        for cn, chs in chapters_by_canonical.items()
        if len(chs) > 1
    ]
    repeat.sort(
        key=lambda r: (-len(r["chapters"]), -r["appearance_count"], r["canonical_name"])
    )
    identities["repeat_speakers_across_chapters"] = repeat
    identities["generated"] = time.strftime("%Y-%m-%d")

    config.SPEAKER_ID_FILE.write_text(
        json.dumps(identities, indent=2, ensure_ascii=False)
    )
    print(
        f"speakers: {len(speakers)} raw names, {new_merges} exact-normalized merge(s) added, "
        f"{len(new_pending)} new pending-review pair(s), {len(repeat)} repeat speakers across chapters"
    )


if __name__ == "__main__":
    main()
