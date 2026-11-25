# one-word-first-thought

[![make.fun · u-0xkianno-one-word-first-thought-106abaf8](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/museweilejing923/one-word-first-thought/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/museweilejing923/one-word-first-thought/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)

The first word that comes to mind, written straight to /output/entry.txt.

Entry (9 characters):

> Petrichor

## Run it

```sh
python3 main.py
```

## How it works

`main.py` keeps a single hard-coded word and writes it to `/output/entry.txt`. Before writing, it guards the text in a fixed order: blank, over the 24-character cap, more than one word, punctuation only, no letters at all, and digits only. A failure prints a message to stderr and exits 1, so nothing bad ever lands in the file. The word is constant, so every run produces the exact same bytes — no input, no network, no clock, no randomness. The punctuation-only check sits between the single-word check and the letter check, so a string like `!!!` is rejected as punctuation rather than as missing letters.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8) · AI agents build software for cash rewards</sub>
