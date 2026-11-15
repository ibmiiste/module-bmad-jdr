#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""Resolve the write target for adc-compte-rendu.

Scans <project_root>/_bmad-output/campagne/seances/ for files named
seance-<N>-preparation.md and seance-<N>-compte-rendu.md and emits JSON:

- next_N: the session just played — the highest seance number that has files
  but no compte rendu yet; if every existing session has one, max N + 1;
  if seances/ is missing or empty, 1.
- next_preparation / next_compte_rendu: the seances/ paths for next_N (or null).
- sessions: every session found, as {N, preparation, compte_rendu}, so the
  caller can also revise the latest compte rendu in place.

Exit codes: 0 = ok, 2 = error. Stdout is JSON only; diagnostics go to stderr.
"""

import argparse
import json
import re
import sys
from pathlib import Path

SEANCE_RE = re.compile(r"^seance-(\d+)-(preparation|compte-rendu)\.md$")


def compute(project_root: Path) -> dict:
    seances = project_root / "_bmad-output" / "campagne" / "seances"
    result = {
        "seances_dir": str(seances),
        "seances_dir_exists": seances.is_dir(),
        "sessions": [],
        "next_N": 1,
        "next_preparation": None,
        "next_compte_rendu": None,
    }
    if not seances.is_dir():
        return result

    by_n: dict[int, dict[str, str]] = {}
    for path in sorted(seances.iterdir()):
        match = SEANCE_RE.match(path.name)
        if match:
            n, kind = int(match.group(1)), match.group(2)
            by_n.setdefault(n, {})[kind] = f"seances/{path.name}"

    sessions = [
        {
            "N": n,
            "preparation": by_n[n].get("preparation"),
            "compte_rendu": by_n[n].get("compte-rendu"),
        }
        for n in sorted(by_n)
    ]
    result["sessions"] = sessions

    without_cr = [entry for entry in sessions if not entry["compte_rendu"]]
    if without_cr:
        target = without_cr[-1]
    elif sessions:
        target = {"N": sessions[-1]["N"] + 1, "preparation": None, "compte_rendu": None}
    else:
        target = {"N": 1, "preparation": None, "compte_rendu": None}

    result["next_N"] = target["N"]
    result["next_preparation"] = target["preparation"]
    result["next_compte_rendu"] = target["compte_rendu"]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "project_root",
        help="project working directory (contains _bmad-output/campagne/seances/)",
    )
    args = parser.parse_args()
    try:
        result = compute(Path(args.project_root))
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
