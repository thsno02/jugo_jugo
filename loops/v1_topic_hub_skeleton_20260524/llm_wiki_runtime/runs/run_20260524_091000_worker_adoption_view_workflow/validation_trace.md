# Validation Trace

run_id:: run_20260524_091000_worker_adoption_view_workflow
executor_role:: adoption_view_worker
status:: pass_with_recorded_validator_contract_caveat

```text
$ /opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md
card validation passed: 1 cards

$ /opt/homebrew/bin/python3 scripts/kb_validate_card.py --all
card validation passed: 7 cards

$ /opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow
nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml: adopted root points to non-adopted version
node validation failed: 1 errors across 1 nodes
```

## Interpretation

Card validation passes for the adopted workflow card and all current version/KB cards. View/index/citation/impact/status scripts also pass and report `adopted_nodes=4`, `citation_edges=51`, and `impact_queue_open=0`.

The node validator failure is a recorded contract mismatch: the validator expects the version bundle metadata to be flipped to `version_status: adopted` when root metadata is adopted. This run's task explicitly forbids writing `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/*`, so the adoption worker did not repair that mismatch by mutating the candidate bundle.

