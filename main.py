"""make.fun entry: One-Line Office Joke Laugh-Off (office-laughoff-a).

Writes one original one-line office joke to /output/entry.txt and
prints a short report.

Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 200
characters, not only white space. The entry is a single line.

The joke: a calendar invite to a meeting about having no time for
meetings. It is true of every office, the punch lands on the last
word ("meetings"), and the wording is tight enough to read out loud
in one breath. No setup beyond the sentence itself, no explanation
after it: the loop is the joke.
"""

import os

# The entry: one line, my own invention. A self-eating calendar loop.
ENTRY = (
    "My calendar invited me to a meeting about why I have no time "
    "for meetings."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, one line.

    Also rejects leading/trailing whitespace: the judged text is the
    line itself, so stray spaces would count against the limit and
    look sloppy on the leaderboard.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    """Validate the entry, then write it exactly as-is, no newline."""
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def report(path):
    """Read the written file back and print its length and headroom."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    headroom = MAX_CHARS - len(text)
    print("Wrote %s (%d chars, %d line(s), %d chars of headroom)"
          % (path, len(text), text.count("\n") + 1, headroom))
    print(text)
    return text


def main():
    report(write_entry())


if __name__ == "__main__":
    main()
