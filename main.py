#!/usr/bin/env python3
"""Print the postmortem entry for the make.fun bounty.

Reads entry.txt next to this file and prints it, enforcing the
400-character limit the bounty sets for the postmortem text."""

from pathlib import Path


MAX_CHARS = 400


def load_entry() -> str:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").strip()
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()
