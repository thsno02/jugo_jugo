# View Build Trace

run_id:: run_20260524_140000_worker_adoption_view_evaluation_evidence
executor_role:: worker_executor
candidate:: cand_007_evaluation_evidence
node_id:: 20260524_132000_llm_wiki_evaluation_evidence
version:: 1.0
decision:: view_refreshed

## Commands Run

- `/opt/homebrew/bin/python3 scripts/kb_build_view.py`
  - result: pass
  - output: `rendered 8 adopted cards and wrote kb/_index.yaml`
- `/opt/homebrew/bin/python3 scripts/kb_build_index.py`
  - result: pass
  - output: `wrote kb/_index.yaml with 8 adopted nodes`
- `/opt/homebrew/bin/python3 scripts/kb_parse_citations.py`
  - result: pass
  - output: `wrote generated/citation_graph.yaml and generated/backlinks.yaml with 185 edges`
- `/opt/homebrew/bin/python3 scripts/kb_compute_impact.py`
  - result: pass
  - output: `wrote generated/impact_queue.yaml with 0 impacts`
- `/opt/homebrew/bin/python3 scripts/kb_status.py`
  - result: pass
  - output: `adopted_nodes=8 citation_edges=185 impact_queue_open=0`

## Generated Counts

- adopted nodes count: 8
- citation edge count: 185
- open impact count: 0

## View Outputs Refreshed

- `kb/20260524_132000_llm_wiki_evaluation_evidence.md`
- `kb/_index.yaml`
- `generated/citation_graph.yaml`
- `generated/backlinks.yaml`
- `generated/impact_queue.yaml`
- `generated/status.yaml`

`kb_build_view.py` mechanically re-rendered adopted KB card views from selected adopted cards.

