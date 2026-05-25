#!/usr/bin/env python3
"""Inspect required worker delivery files for one iteration."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LOOP_ROOT = ROOT / "llm_wiki" / "loop"
REQUIRED = ["task.md", "loop_status.md", "loop_delivery.md", "read_log.md"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iteration_id")
    args = parser.parse_args()

    iteration_dir = LOOP_ROOT / "iterations" / args.iteration_id
    missing = [name for name in REQUIRED if not (iteration_dir / name).exists()]
    delivery = iteration_dir / "loop_delivery.md"
    marker_ok = False
    if delivery.exists():
        text = delivery.read_text(encoding="utf-8")
        marker_ok = "LOOP_DONE" in text or "LOOP_BLOCKED" in text

    if missing or not marker_ok:
        print("delivery_inspection: fail")
        for name in missing:
            print(f"missing: {name}")
        if not marker_ok:
            print("missing: LOOP_DONE_or_LOOP_BLOCKED")
        return 1

    print("delivery_inspection: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
