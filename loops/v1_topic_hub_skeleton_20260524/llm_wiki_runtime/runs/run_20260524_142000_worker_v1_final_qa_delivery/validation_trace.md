# Validation Trace

Run: `run_20260524_142000_worker_v1_final_qa_delivery`
Decision: `v1_delivered`

## Required Validators

| Gate | Command | Result |
| --- | --- | --- |
| node validator | `/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all` | pass: `node validation passed: 8 nodes` |
| card validator | `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all` | pass: `card validation passed: 16 cards` |

Both validators were run before control-plane lifecycle sync and again after sync. Final post-sync results remained pass.

## Mechanical Refresh / Generated Artifacts

| Artifact class | Command | Result |
| --- | --- | --- |
| adopted KB views + index | `/opt/homebrew/bin/python3 scripts/kb_build_view.py` | pass: rendered 8 adopted cards and wrote `kb/_index.yaml` |
| index | `/opt/homebrew/bin/python3 scripts/kb_build_index.py` | pass: wrote `kb/_index.yaml` with 8 adopted nodes |
| citation graph + backlinks | `/opt/homebrew/bin/python3 scripts/kb_parse_citations.py` | pass: wrote `generated/citation_graph.yaml` and `generated/backlinks.yaml` with 185 edges |
| impact queue | `/opt/homebrew/bin/python3 scripts/kb_compute_impact.py` | pass: wrote `generated/impact_queue.yaml` with 0 impacts |
| status | `/opt/homebrew/bin/python3 scripts/kb_status.py` | pass: adopted_nodes=8, citation_edges=185, impact_queue_open=0 |

No separate backlinks-only script exists in `scripts/`; backlinks are built by `scripts/kb_parse_citations.py`.

## YAML Parse Gate

Checked 27 YAML files:

- control: orchestration gates, knowledge frontier, action queue, state, skill registry, skill eval log
- generated: status, impact queue, citation graph, backlinks
- index: `kb/_index.yaml`
- node metadata: 8 root `node.yaml` files and 8 selected-version `versions/1.0/node.yaml` files

Result: pass, 27/27 parsed.

## Final Generated Status

- adopted_nodes: 8
- kb_view_cards: 8
- citation_edges: 185
- impact_queue_open: 0
- major_candidates: 0

Note: `generated/status.yaml` still uses the generic script recommendation `run_dynamic_retrieval_test`; control-plane state now records v1 delivery complete and treats retrieval as future non-blocking work.
