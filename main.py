#!/usr/bin/env python3
"""Put the first word that springs to mind into /output/entry.txt.

No network, no clock, no random numbers: the same bytes come out
on every single run.
"""

import os
import string
import sys

WORD = "Petrichor"
CAP = 24
TARGET = "/output/entry.txt"


def guard(text):
    """Reject anything that is not one plain word within the cap."""
    stripped = text.strip()
    if stripped == "":
        raise ValueError("entry is blank")
    if len(text) > CAP:
        raise ValueError("entry is too long")
    if len(stripped.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if all(mark in string.punctuation for mark in stripped):
        raise ValueError("entry cannot be punctuation only")
    if not any(letter.isalpha() for letter in text):
        raise ValueError("entry needs at least one letter")
    if text.isdigit():
        raise ValueError("entry cannot be digits alone")
    return text


def run():
    try:
        good = guard(WORD)
    except ValueError as problem:
        print(f"bad entry: {problem}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(good)
    return 0


if __name__ == "__main__":
    sys.exit(run())
