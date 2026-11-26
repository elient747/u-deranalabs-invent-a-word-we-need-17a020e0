#!/usr/bin/env python3
"""Invent a Word We Need — one original line, 1 to 140 characters:
a freshly coined English word with its one-line definition.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
# Revised: the line is built inside write_entry(); entry.txt mirrors it
# exactly. (Rev 2: "nodrift" — nod + drift, one word for the gap of
# nodding along to a conversation you stopped following. The definition
# lands in one reading and names the fear underneath: being asked.)
import os


def write_entry():
    line = (
        "Nodrift (n.) — nodding along to a conversation you stopped "
        "following three minutes ago, hoping nobody asks your opinion."
    )
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
