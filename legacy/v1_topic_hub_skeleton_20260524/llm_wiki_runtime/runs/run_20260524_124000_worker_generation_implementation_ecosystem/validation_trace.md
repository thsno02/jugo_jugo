# Validation Trace

run_id:: run_20260524_124000_worker_generation_implementation_ecosystem
executor_role:: worker_executor
worker_role:: cand_006_implementation_ecosystem generation worker
status:: passed

## Planned checks

- Schema sanity: candidate metadata should remain under `nodes/<node_id>/versions/1.0/` and must not mark the node adopted.
- Card citation sanity: run `scripts/kb_validate_card.py` against the candidate card.
- Footnote layout gate: ensure `## References` appears before `## Footnotes`, and `## Footnotes` is the final top-level section.
- Scope sanity: no root node metadata, `kb/`, or `generated/` writes.
- Claim sanity: no adoption, package download, plugin install, quality, maturity, enterprise readiness, production deployment, or market-ranking claims.

## Results

- Card validator command:
  - `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/card.md`
  - Result: `card validation passed: 1 cards`
- Footnote layout gate command:
  - `/opt/homebrew/bin/python3 -c "..."`
  - Result: `footnote_layout_gate: pass`
  - Observed top-level sections: `['## References', '## Footnotes']`
- Scope write gate:
  - Result: `scope_write_gate: pass`
  - Confirmed no `nodes/20260524_122000_llm_wiki_implementation_ecosystem/node.yaml`.
  - Confirmed no `kb/20260524_122000_llm_wiki_implementation_ecosystem.md`.
- Candidate bundle validator note:
  - No root adoption validator was run because this generation task explicitly forbids writing adopted root metadata before audit.
  - The candidate `node.yaml` marks `status: candidate`, `version_status: pending_audit`, `adoption_status: pending_audit`, `adopted: false`, and `selected: false`.

## Sanity check summary

- The card contains parseable `## References` and `## Footnotes` blocks with required citation fields.
- `## References` appears before `## Footnotes`.
- `## Footnotes` is the final top-level section.
- The card does not claim package downloads, plugin installs, active users, production deployment, quality, maturity, enterprise readiness, market ranking, or broad adoption.
- Prior KB anchors are labeled as continuity/boundary anchors.
- Adjacent OpenKB and MCP/graph-vault sources are labeled as adjacent or source-specific.
