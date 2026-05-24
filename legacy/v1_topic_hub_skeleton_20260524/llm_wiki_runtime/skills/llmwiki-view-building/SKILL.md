---
name: llmwiki-view-building
description: Build adopted LLM Wiki KB consumption views and generated graph artifacts. Use after adoption to render kb/ cards, rebuild kb/_index.yaml, parse citation graph/backlinks, compute impact queues, and refresh generated/status.yaml.
---

# LLM Wiki View Building

## Purpose

Use this skill after adoption. `nodes/` remains the source of truth; `kb/` and `generated/` are consumption and post-processing views.

## Workflow

1. Run node/card validators.
2. Run the footnote layout gate: `## References` must appear before the final `## Footnotes`, and `## Footnotes` must be the last top-level section.
3. If adopting a version, write root `nodes/<node_id>/node.yaml` and update only the selected `versions/<version>/node.yaml` adoption metadata fields needed for validator consistency.
4. Render adopted versions into `kb/`.
5. Rebuild `kb/_index.yaml`.
6. Parse card citations into `generated/citation_graph.yaml`.
7. Build backlinks.
8. Compute or refresh `generated/impact_queue.yaml`.
9. Refresh `generated/status.yaml`.

## Hard Rules

- Do not render candidate versions into `kb/`.
- Do not leave an adopted root pointing at a `versions/<version>/node.yaml` that still says `candidate`, `candidate_pending_audit`, or `pending_audit`.
- Adoption/view workers may update version metadata adoption fields after an audit pass, but must not rewrite `card.md`, `provenance.md`, `change.md`, or evidence content unless a repair task explicitly permits it.
- Do not modify archived demo artifacts.
- Do not treat generated files as source of truth for card claims.
- Record build failures in the run artifact and route them to skill evaluation.

## Suggested Commands

- `python3 scripts/kb_validate_node.py --all`
- `python3 scripts/kb_validate_card.py --all`
- `python3 scripts/kb_build_index.py`
- `python3 scripts/kb_build_view.py`
- `python3 scripts/kb_parse_citations.py`
- `python3 scripts/kb_compute_impact.py`
- `python3 scripts/kb_status.py`

## Skill Evolution Notes

Patch this skill when generated state drifts from adopted nodes or a build failure lacks a durable trace.
