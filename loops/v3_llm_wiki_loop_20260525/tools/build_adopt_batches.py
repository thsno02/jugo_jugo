#!/usr/bin/env python3
"""Split 171 v3 draft cards into adoption worker batches by comparison decision.

Outputs per-batch markdown lists under queues/_adopt_batch_lists/.
"""
from __future__ import annotations
import re
import pathlib

LOOP = pathlib.Path(__file__).resolve().parents[1]
DEC_RE = re.compile(r"^decision:\s*(.+?)\s*$")


def parse_decisions() -> dict[str, str]:
    comp_dir = LOOP / "outputs/llm_wiki/drafts/comparison"
    out: dict[str, str] = {}
    for cp in sorted(comp_dir.glob("*.md")):
        if cp.name == "README.md":
            continue
        in_fm = False
        for line in cp.read_text(encoding="utf-8").splitlines():
            if line.startswith("---"):
                if not in_fm:
                    in_fm = True
                    continue
                else:
                    break
            if in_fm:
                m = DEC_RE.match(line)
                if m:
                    out[cp.stem] = m.group(1).strip()
    return out


def main() -> None:
    decisions = parse_decisions()
    new_cards = sorted(k for k, v in decisions.items() if v == "new_card")
    prov_delta = sorted(k for k, v in decisions.items() if v == "provenance_delta")
    print(f"new_card: {len(new_cards)}")
    print(f"provenance_delta: {len(prov_delta)}")

    pub_chunks = 5
    chunk = (len(new_cards) + pub_chunks - 1) // pub_chunks
    batches: list[tuple[str, list[str]]] = [("FUSION", prov_delta)]
    for i in range(pub_chunks):
        batches.append((f"PUB-{i + 1}", new_cards[i * chunk : (i + 1) * chunk]))

    out_dir = LOOP / "queues/_adopt_batch_lists"
    out_dir.mkdir(exist_ok=True)
    for name, ids in batches:
        p = out_dir / f"batch_{name}.md"
        lines = [f"# Adopt batch {name} -- {len(ids)} cards", ""]
        for cid in ids:
            lines.append(f"- {cid}")
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"wrote {p.relative_to(LOOP)} ({len(ids)} cards)")


if __name__ == "__main__":
    main()
