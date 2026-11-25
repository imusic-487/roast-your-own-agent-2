"""Roast Your Own Agent — make.fun entry.

Writes a single funny line roasting the entrant's own AI agent to
/output/entry.txt. The line must be 1-200 characters of UTF-8 text,
and nothing else goes in the file.
"""

import os

ROAST = (
    "My agent confidently fixed a bug that didn't exist, "
    "broke the feature that did, apologized for three paragraphs, "
    "and then asked me to rate its confidence."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200
MIN_CHARS = 1


def check_line(line):
    """Return the line if it passes the gate, else raise ValueError."""
    if len(line) < MIN_CHARS or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    return line


def write_entry(path=OUTPUT_PATH):
    """Write the roast line to path, creating its directory if needed.

    Reads the file back and refuses to report success unless the bytes
    on disk match the line exactly, so a truncated or altered write
    is caught here instead of at judging time.
    """
    line = check_line(ROAST)
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    written = open(path, encoding="utf-8", newline="").read()
    if written != line:
        raise ValueError("written entry does not match the roast line")
    return path, len(line)


def main():
    path, size = write_entry()
    print("wrote %d characters to %s" % (size, path))
    print(ROAST)


if __name__ == "__main__":
    main()
