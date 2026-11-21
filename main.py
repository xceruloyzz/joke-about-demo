#!/usr/bin/env python3
"""Write one original one-line joke about working beside AI coding agents.

Deterministic: the joke is a hardcoded string. No network, no randomness,
no clock, no external files. Writes to $MAKEFUN_OUTPUT_DIR, else /output,
else ./out.
"""

import os

JOKE = (
    "The demo crashed, my agent apologised, fixed it, crashed it again, "
    "and apologised so sincerely I almost thanked it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "./out"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
