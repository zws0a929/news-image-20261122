#!/usr/bin/env python3
"""Sum up 22 November 2026's world news in one image.

The entry image is a newspaper front page: COP31 collapses in Antalya,
sea drones strike a warship off Benghazi, tankers on alert near Hormuz,
BepiColombo reaches Mercury, Delta's outage delays thousands of flights,
and a factory fire in Cikande, Indonesia. The program copies the finished
front page to /output/entry.png. Deterministic: same bytes every run.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path("/output/entry.png")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
