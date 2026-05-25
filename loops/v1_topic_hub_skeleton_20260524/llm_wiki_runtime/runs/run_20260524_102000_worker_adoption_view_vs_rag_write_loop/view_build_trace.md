# View Build Trace

run_id:: run_20260524_102000_worker_adoption_view_vs_rag_write_loop
executor_role:: worker_executor
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
version:: 1.0

## Commands Run

- `/opt/homebrew/bin/python3 scripts/kb_build_view.py`
  - result: `rendered 5 adopted cards and wrote kb/_index.yaml`
- `/opt/homebrew/bin/python3 scripts/kb_build_index.py`
  - result: `wrote kb/_index.yaml with 5 adopted nodes`
- `/opt/homebrew/bin/python3 scripts/kb_parse_citations.py`
  - result: `wrote generated/citation_graph.yaml and generated/backlinks.yaml with 73 edges`
- `/opt/homebrew/bin/python3 scripts/kb_compute_impact.py`
  - result: `wrote generated/impact_queue.yaml with 0 impacts`
- `/opt/homebrew/bin/python3 scripts/kb_status.py`
  - result: `adopted_nodes=5 citation_edges=73 impact_queue_open=0`

## Built / Refreshed Outputs

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `kb/_index.yaml`
- `generated/citation_graph.yaml`
- `generated/backlinks.yaml`
- `generated/impact_queue.yaml`
- `generated/status.yaml`

## Counts

- adopted nodes count: 5
- citation edge count: 73
- open impact count: 0

