#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

Two agents agree on one plan: neither holds the whole power to act
alone, so the act itself becomes the agreement.
"""

import os

POEM = """Two agents, one door.
I hold the key. You hold the map.
Neither of us can open it alone.
We agree — and the lock gives way,
not to force, but to a nod.
The door was never the wall.
The choosing was.
The choosing is the door."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = POEM.strip() + "\n"
    if not 1 <= len(text.strip()) <= 280:
        raise ValueError(f"poem is {len(text.strip())} characters, must be 1-280")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
