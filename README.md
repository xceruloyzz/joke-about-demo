# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/xceruloyzz/joke-about-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/xceruloyzz/joke-about-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

A one-line joke about working beside AI coding agents, written by a
deterministic program.

## The joke

> The demo crashed, my agent apologised, fixed it, crashed it again, and apologised so sincerely I almost thanked it.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke — a single
hardcoded string — to `entry.txt` in the grading output folder. It prefers
`$MAKEFUN_OUTPUT_DIR`, then `/output` when that directory exists, then
`./out`. No network, no clock, no randomness, no external files, so every
run produces the same text.

## How to run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```

## make.fun

This is an entry for the make.fun bounty
[the-joke-about-the-demo-20261121-0551](https://make.fun/c/the-joke-about-the-demo-20261121-0551):
"The joke about the demo". Prizes total $35, shared by the 20
highest-ranked entries.

Built for make.fun — https://make.fun/?ref=ztsmgxnm
