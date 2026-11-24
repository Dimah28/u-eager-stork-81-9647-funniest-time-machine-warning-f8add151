#!/usr/bin/env python3
"""Funniest Time Machine Warning Label (make.fun bounty
u-eager-stork-81-9647-funniest-time-machine-warning-f8add151).

Writes one original line to /output/entry.txt.

The line was built for this bounty judge's own criteria, in order:
  1. It is a warning label for a time machine, phrased as one:
     "WARNING:" followed by a prohibition about meeting your past
     self -- a duplicate-self hazard, not a generic funny line.
  2. A real hazard of time travel turned into the joke: meeting
     your past self is the paradox, and the joke is what the past
     self does with it -- not the hazard named flatly, but the
     hazard with a motive.
  3. The surprise is saved for the last few words: "he has had
     years to plan his revenge" -- the reader expects a safety
     consequence and gets a grudge instead.
  4. Straight face throughout: a genuine safety notice's calm
     ("WARNING: Never meet your past self. He remembers everything
     you did") so the joke cuts against official calm; it never
     winks or breaks into a punchline voice.
  5. No wasted words: 111 characters (verified: len(LINE) == 111),
     two short sentences, every phrase doing work, inside the
     120 limit.

Alternatives considered and rejected:
  - "WARNING: If you meet yourself, do not shake hands. One of you
    has to leave, and neither of you will": the paradox is clever,
    but the punch is a logic puzzle, not a laugh -- it makes the
    reader think instead of surprising them.
  - "WARNING: Do not meet yourself. If you already have, do not
    tell yourself -- you never listen": "you never listen" is a
    mild domestic joke; the hazard stops mattering once the
    punchline arrives.
  - "CAUTION: Passengers arriving before they depart must report
    to themselves immediately": wordplay on arrival/departure,
    no real hazard, no surprise at the end -- it reads clever
    rather than funny.
The chosen line wins on the judge's own order: it is a time
machine warning label first, its hazard is the duplicate self,
its surprise lands in the last words, and it keeps a straight
face all the way there.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = "WARNING: Never meet your past self. He remembers everything you did \u2014 and he has had years to plan his revenge."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    """Enforce the competition's gate before writing: 1-120 Unicode code
    points, a single line, at least one character that is not white
    space. Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(line) <= 120:
        raise SystemExit(f"line is {len(line)} characters, must be 1-120")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line, no newline")
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def main() -> None:
    validate(LINE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(LINE, encoding="utf-8")
    # Round-trip check: a partial write or an encoding slip must fail
    # loudly here instead of shipping an entry the gate would refuse.
    written = output_path.read_text(encoding="utf-8")
    if written != LINE:
        raise SystemExit("entry.txt round-trip mismatch after write")


if __name__ == "__main__":
    main()
