"""Write the brave entry text to entry.txt.

The text is a single short piece, written fresh for this bounty.
It is held here as a constant so the program's output is
deterministic: the same bytes on every run. One image carries it —
a stone the river moves around all afternoon, still there by morning.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "All afternoon the river has moved around one stone, and the stone "
    "has not moved. The water finds its way past, slow and clear, and "
    "the stone stays cool in the current, still there when the light "
    "goes, still there in the morning."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY_TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
