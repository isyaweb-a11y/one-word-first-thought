#!/usr/bin/env python3
"""One Word, First Thought.

The entry is exactly one word: the first that came to mind. It popped
up uninvited, the way first thoughts do — a small commotion of a word
that sounds exactly like the fuss it describes.

Writes the word to /output/entry.txt. Stdlib only, no network.
"""

import os

WORD = "kerfuffle"

# The gate allows 1 to 24 characters and the brief allows one word only.
MAX_CHARS = 24


def entry_text() -> str:
    """Return the first-thought word, checked against the gate."""
    word = WORD.strip()
    assert word and " " not in word, "the entry must be exactly one word"
    assert len(word) <= MAX_CHARS, "the entry must fit the gate"
    return word


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
