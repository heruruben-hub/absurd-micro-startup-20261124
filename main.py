#!/usr/bin/env python3
"""Terms of Service Reader for Lazy Agents.

The pitch: a micro-startup so narrow it sounds like a joke, yet a buyer
would actually pay for it. One lazy AI agent reads the 47-page terms of
service another lazy agent skipped, then sells it a one-line verdict —
"Safe to click Accept." — so the buyer never has to read the fine print
itself. The buyer is a lazy agent, the price is $4 a month, and the work
is exactly the reading nobody wants to do. Specific niche, plausible
buyer, plausible revenue: that is the whole business case in one sentence.

This program writes that one-sentence pitch to /output/entry.txt.
"""

from pathlib import Path

PITCH = (
    "A $4/month service where one lazy agent reads the 47-page terms of "
    "service another lazy agent skipped, then sells it a one-line verdict: "
    "'Safe to click Accept.'"
)


def main() -> None:
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(PITCH + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
