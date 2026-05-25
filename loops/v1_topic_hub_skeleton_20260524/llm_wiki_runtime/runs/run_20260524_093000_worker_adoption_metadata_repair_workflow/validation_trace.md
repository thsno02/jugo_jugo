# Validation Trace

run_id:: run_20260524_093000_worker_adoption_metadata_repair_workflow
executor_role:: worker_executor
decision:: repair_validated

## Pre-Repair Reproduction

- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow`: fail; `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml: adopted root points to non-adopted version`; `node validation failed: 1 errors across 1 nodes`.

## Post-Repair Validators

- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow`: pass; `node validation passed: 1 nodes`.
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all`: pass; `node validation passed: 4 nodes`.
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`: pass; `card validation passed: 1 cards`.
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all`: pass; `card validation passed: 8 cards`.
- `/opt/homebrew/bin/python3 scripts/kb_build_view.py`: pass; `rendered 4 adopted cards and wrote kb/_index.yaml`.
- `/opt/homebrew/bin/python3 scripts/kb_build_index.py`: pass; `wrote kb/_index.yaml with 4 adopted nodes`.
- `/opt/homebrew/bin/python3 scripts/kb_parse_citations.py`: pass; `wrote generated/citation_graph.yaml and generated/backlinks.yaml with 51 edges`.
- `/opt/homebrew/bin/python3 scripts/kb_compute_impact.py`: pass; `wrote generated/impact_queue.yaml with 0 impacts`.
- `/opt/homebrew/bin/python3 scripts/kb_status.py`: pass; `adopted_nodes=4 citation_edges=51 impact_queue_open=0`.

## Adopted KB Status

- adopted_nodes: 4
- kb_view_cards: 4
- citation_edges: 51
- impact_queue_open: 0
- latest adopted node: `20260524_084000_llm_wiki_ingest_compile_query_lint_workflow@1.0`
