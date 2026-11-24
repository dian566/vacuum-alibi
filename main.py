#!/usr/bin/env python3
"""Generate the one-line entry for The Vacuum's Alibi bounty."""

from pathlib import Path

ENTRY = "I did not miss the spot. I performed a strategic retreat after the dust bunny filed a restraining order."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
