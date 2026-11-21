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

# The gate allows 1-280 Unicode code points; refuse to write anything else.
assert 1 <= len(JOKE) <= 280, "joke outside the 1-280 character gate"


def output_dir() -> str:
    """Where entry.txt goes: the grader's dir, else /output, else ./out."""
    if os.environ.get("MAKEFUN_OUTPUT_DIR"):
        return os.environ["MAKEFUN_OUTPUT_DIR"]
    return "/output" if os.path.isdir("/output") else "./out"


def main() -> None:
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
