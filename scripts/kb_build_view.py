#!/usr/bin/env python3
"""Render adopted node versions into the kb/ consumption view."""

from __future__ import annotations

import shutil

from kb_build_index import build_index
from kb_common import KB_DIR, ROOT, adopted_nodes, root_relative, write_yaml


def main() -> int:
    KB_DIR.mkdir(parents=True, exist_ok=True)
    rendered = 0
    for old_view in KB_DIR.glob("*.md"):
        old_view.unlink()

    for node in adopted_nodes():
        paths = node.get("paths", {})
        card_path = ROOT / paths.get("card", "")
        if not card_path.exists():
            raise FileNotFoundError(f"missing adopted card for {node.get('id')}: {card_path}")
        target = KB_DIR / f"{node['id']}.md"
        shutil.copyfile(card_path, target)
        rendered += 1

    index_path = KB_DIR / "_index.yaml"
    index = build_index()
    write_yaml(index_path, index)
    print(f"rendered {rendered} adopted cards and wrote {root_relative(index_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
