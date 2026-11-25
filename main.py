"""One Line, Big Laugh - variant 2.

Writes a single original funny line (1-200 characters) to /output/entry.txt.
Deterministic, stdlib only, no network, no clock, no randomness.
"""

LINE = (
    "My dentist said I grind my teeth at night. "
    "Turns out my jaw is just rehearsing the argument I lost in 2019."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(line: str, path: str) -> None:
    """Write one line to path as UTF-8, enforcing the competition gate."""
    text = line.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


def main() -> None:
    write_entry(LINE, OUTPUT_PATH)


if __name__ == "__main__":
    main()
