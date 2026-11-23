#!/usr/bin/env python3
"""Build the Run manager's migration dry-run project (plan-run-manager.md, the migration path).

Usage: python3 build.py DEST

Makes DEST/Lighthouse/: the project before the migration run, with its run state (.runs/run-state.json)
holding no open run and the earlier run's history, handled list, and unit index. The files that stand in
for the migrator and the migration-verifier stay in prepared/ beside this file; steps.md says which to
copy where. Refuses if DEST/Lighthouse already exists. Copies only from source/ beside this file.
Standard library only.
"""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "source" / "Lighthouse"


def main(argv):
    if len(argv) != 2:
        print("usage: python3 build.py DEST", file=sys.stderr)
        return 2
    dest = Path(argv[1]).expanduser().resolve()
    target = dest / "Lighthouse"
    if target.exists():
        print(f"refused: {target} already exists", file=sys.stderr)
        return 1
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, target)
    print(f"built {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
