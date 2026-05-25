# View Build Trace

decision:: view_built

## Commands

- `/opt/homebrew/bin/python3 scripts/kb_build_view.py`
  - `rendered 6 adopted cards and wrote kb/_index.yaml`
- `/opt/homebrew/bin/python3 scripts/kb_build_index.py`
  - `wrote kb/_index.yaml with 6 adopted nodes`
- `/opt/homebrew/bin/python3 scripts/kb_parse_citations.py`
  - `wrote generated/citation_graph.yaml and generated/backlinks.yaml with 110 edges`
- `/opt/homebrew/bin/python3 scripts/kb_compute_impact.py`
  - `wrote generated/impact_queue.yaml with 0 impacts`
- `/opt/homebrew/bin/python3 scripts/kb_status.py`
  - `wrote generated/status.yaml`
  - `adopted_nodes=6 citation_edges=110 impact_queue_open=0`

## Outputs Refreshed

- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`
- `kb/_index.yaml`
- `generated/citation_graph.yaml`
- `generated/backlinks.yaml`
- `generated/impact_queue.yaml`
- `generated/status.yaml`

## Counts

- adopted nodes count: 6
- KB index node count: 6
- citation edge count: 110
- open impact count: 0
