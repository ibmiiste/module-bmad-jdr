#!/usr/bin/env python3
"""Tests for next-seance.py.

Covers the output schema and the <N> derivation: missing/empty seances dir,
partial compte rendus, all sessions closed, and non-seance files ignored.
Run with: uv run --with pytest -m pytest test_next_seance.py
(or plain `uv run test_next_seance.py` for a lightweight self-check).
"""

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "next-seance.py"

spec = importlib.util.spec_from_file_location("next_seance", SCRIPT)
next_seance = importlib.util.module_from_spec(spec)
spec.loader.exec_module(next_seance)


def make_seances(root: Path, files: list[str]) -> Path:
    seances = root / "_bmad-output" / "campagne" / "seances"
    seances.mkdir(parents=True, exist_ok=True)
    for name in files:
        (seances / name).write_text("# fixture\n", encoding="utf-8")
    return seances


def test_missing_seances_dir_defaults_to_one():
    with tempfile.TemporaryDirectory() as tmp:
        result = next_seance.compute(Path(tmp))
    assert result["seances_dir_exists"] is False
    assert result["next_N"] == 1
    assert result["next_preparation"] is None
    assert result["next_compte_rendu"] is None
    assert result["sessions"] == []


def test_empty_seances_dir_defaults_to_one():
    with tempfile.TemporaryDirectory() as tmp:
        make_seances(Path(tmp), [])
        result = next_seance.compute(Path(tmp))
    assert result["seances_dir_exists"] is True
    assert result["next_N"] == 1
    assert result["sessions"] == []


def test_highest_session_without_compte_rendu_wins():
    with tempfile.TemporaryDirectory() as tmp:
        make_seances(Path(tmp), [
            "seance-1-preparation.md", "seance-1-compte-rendu.md",
            "seance-2-preparation.md",
            "seance-3-preparation.md",
        ])
        result = next_seance.compute(Path(tmp))
    assert result["next_N"] == 3
    assert result["next_preparation"] == "seances/seance-3-preparation.md"
    assert result["next_compte_rendu"] is None
    assert [s["N"] for s in result["sessions"]] == [1, 2, 3]


def test_all_sessions_closed_goes_to_next_number():
    with tempfile.TemporaryDirectory() as tmp:
        make_seances(Path(tmp), [
            "seance-1-preparation.md", "seance-1-compte-rendu.md",
            "seance-2-compte-rendu.md",
        ])
        result = next_seance.compute(Path(tmp))
    assert result["next_N"] == 3
    assert result["next_compte_rendu"] is None


def test_non_seance_files_are_ignored():
    with tempfile.TemporaryDirectory() as tmp:
        make_seances(Path(tmp), ["notes.md", "seance-x-preparation.md", "seance-1-compte-rendu.txt"])
        result = next_seance.compute(Path(tmp))
    assert result["sessions"] == []
    assert result["next_N"] == 1


def test_cli_emits_valid_json():
    with tempfile.TemporaryDirectory() as tmp:
        make_seances(Path(tmp), ["seance-1-preparation.md"])
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), tmp],
            capture_output=True, text=True,
        )
    assert proc.returncode == 0
    payload = json.loads(proc.stdout)
    assert payload["next_N"] == 1
    assert payload["next_preparation"] == "seances/seance-1-preparation.md"


if __name__ == "__main__":
    for name, fn in sorted(list(globals().items())):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok {name}")
    print("all tests passed")
