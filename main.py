#!/usr/bin/env python3
"""Everyday Things, Two Lines — zipper entry for make.fun.

Writes the two-line explanation to /output/entry.txt.

Line 1: one vivid sentence, one analogy — a zipper is the teacher who
walks between two lines of children, joining their hands as she steps
forward and letting go as she steps back.
Line 2: one sentence on what the analogy maps (the slider locking the
two sides tooth by tooth, in order) and what it leaves out (the hard
metal teeth that pinch skin and snag shirts).
"""

import os

LINE_1 = (
    "A zipper is the teacher who walks between two lines of children, "
    "joining their hands as she steps forward and letting go as she "
    "steps back."
)
LINE_2 = (
    "It maps how the slider locks the two sides tooth by tooth in order, "
    "but it leaves out the hard metal teeth that pinch your skin and "
    "snag your shirt."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    # Self-check the gate before writing: exactly two lines, 1-400 chars.
    lines = ENTRY.strip("\n").split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
