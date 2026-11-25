#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "The Best Meal You Ever Had".
Candidates compared: a 3 a.m. gas-station onigiri (concrete but reads
as a snack, not a best meal), a street-cart corn line (vivid but no
personal stake), and the selected grandmother's miso soup line: one
sentence with a place, an age, steam on glasses and the quiet detail
of thirds nobody mentioned - concrete, personal and memorable.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "My grandmother's miso soup, eaten at her low table the winter I turned twelve, when the steam fogged my glasses and she pretended not to notice I had seconds three times."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")
    if body.count(".") != 1 or not body.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
