"""One Word for Your Wi-Fi entry for make.fun: one word describing your Wi-Fi."""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 20

# One word for my Wi-Fi: ghosting — it vanishes mid-call, exactly when you need it most.
ENTRY = "ghosting"


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert " " not in ENTRY and ENTRY.strip() == ENTRY, "entry must be a single word"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
