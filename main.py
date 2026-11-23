#!/usr/bin/env python3
"""One-line pitch entry for the make.fun bounty
"A Day of One-Line Pitches".

Writes a single original sentence to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
The sentence is the whole entry: no code, no explanation.
"""

import os
from pathlib import Path

ENTRY = (
    "Tell it the app idea you've been carrying around in your head, "
    "and watch it take shape while you sip your coffee \u2014 "
    "no code, nothing to install, and if you don't like it, "
    "you just say so and it changes."
)


def main() -> None:
    """Write the pitch, checking the bounty gate as we go."""
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    assert text and not text.isspace()
    # Exactly one sentence: a single terminal full stop, no other periods.
    assert text.count(".") == 1 and text.endswith(".")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
