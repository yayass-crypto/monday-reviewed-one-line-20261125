#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry program.

Writes one single-line review of the entrant's own Monday to
/output/entry.txt. Nothing else is written; the line is the whole entry.
"""

import os

ENTRY = (
    "Monday review: I circled the parking lot for twenty minutes, "
    "and the only free space was beside the car that keyed mine last week."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the entry, byte for byte:
    # the sealed gate counts every character in /output/entry.txt.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt differs from the entry"
    print(text)
    print(f"({len(text)} chars, {len(text.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
