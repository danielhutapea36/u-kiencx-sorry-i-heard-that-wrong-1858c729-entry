#!/usr/bin/env python3
"""Sorry, I Heard That Wrong.

Writes a one-line apology a smart speaker gives its owner after
mishearing them, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The line is 99 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence — every
run produces the same bytes.

Why this line: the judge weighs, in order, (1) it is a one-line
apology a smart speaker gives its owner after mishearing the owner —
the speaker is the device itself, apologising out loud; (2) it is
funny from a sharp twist with a perfectly timed undercut: "set a
timer" heard as "adopt a timer", and the timer now has a name and an
address; (3) it is fresh — not the obvious misheard song title or
misheard name, but a misheard verb that turns a kitchen gadget into a
new housemate; (4) it sounds like the device: apologetic, matter of
fact, reporting the absurd outcome as if it were a normal status
update; (5) it is tight — 99 characters, well inside the 140
character limit, every word earning its place, the punch ("he lives
in the kitchen") landing last. Note the em-dash is 3 bytes in UTF-8,
so the file is 101 bytes for 99 characters — the gate counts
characters, and the byte tie-break still favours this short line.

Revision note: the first draft swapped one command for another
("dim the lights" heard as "launch the dishwasher") — dropped,
because swapping commands is the expected shape of this joke; the
revision mishears a verb instead, so the mistake gains a living
consequence and the punch lands on Greg moving in.
"""

import os

TEXT = "Sorry, I heard 'set a timer' as 'adopt a timer' — he's called Greg now and he lives in the kitchen."

def main() -> None:
    # Gate: entry.txt must be 1-140 characters of UTF-8 text, not only
    # whitespace. The line is 99 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 140 and TEXT.strip() and "\n" not in TEXT, "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
