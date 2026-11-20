"""Copy entry.png to the output directory.

Standard library only: the scoring sandbox has no third-party packages,
so this program imports nothing beyond os, shutil and pathlib.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    if not SRC.is_file():
        raise SystemExit("entry.png is missing next to main.py")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # A plain copy: the image is the entry, so both runs must write
    # exactly the same bytes.
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
