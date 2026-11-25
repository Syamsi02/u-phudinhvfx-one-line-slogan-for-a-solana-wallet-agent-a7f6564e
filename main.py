"""One-line slogan for a Solana wallet agent.

Writes the slogan to /output/entry.txt (the gate checks UTF-8 text of
1 to 140 characters, a single line, at most twenty words).
Pure standard library, deterministic: the same slogan every run.
"""

import os

SLOGAN = (
    "Your Solana wallet, with a mind of its own: "
    "it pays, swaps, and tidies up while you sleep."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    slogan = " ".join(SLOGAN.split())
    assert 1 <= len(slogan) <= 140, "slogan must be 1-140 characters"
    assert len(slogan.split()) <= 20, "slogan must be at most 20 words"
    assert "\n" not in slogan, "slogan must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(slogan + "\n")
    # Read it back so a bad write fails loudly instead of silently.
    with open(OUTPUT_PATH, encoding="utf-8") as handle:
        assert handle.read().strip() == slogan
    print(slogan)


if __name__ == "__main__":
    main()
