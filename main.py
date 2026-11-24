"""The Vacuum's Alibi: One Line, 200 Characters — make.fun entry.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = 'I did not miss the spot. I performed a strategic retreat after the dust bunny filed a restraining order.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
