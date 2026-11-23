#!/usr/bin/env python3
"""Build the Run manager's dry-run project (plan-run-manager.md, Milestone 6).

Usage: python3 build.py DEST

Makes DEST/Lighthouse/ (the research project before the run) and DEST/prepared/
(what the research workflow would return, laid out as a mirror of the project).
Refuses if DEST already holds either. Copies only from source/ beside this file.
Standard library only.
"""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "source"


def main(argv):
    if len(argv) != 2:
        print("usage: python3 build.py DEST", file=sys.stderr)
        return 2
    dest = Path(argv[1]).expanduser().resolve()
    for name in ("Lighthouse", "prepared"):
        if (dest / name).exists():
            print(f"refused: {dest / name} already exists", file=sys.stderr)
            return 1
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE / "project" / "Lighthouse", dest / "Lighthouse")
    shutil.copytree(SOURCE / "prepared", dest / "prepared")
    print(f"built {dest / 'Lighthouse'}")
    print(f"built {dest / 'prepared'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
