# View Build Trace

run_id:: run_20260524_091000_worker_adoption_view_workflow
executor_role:: adoption_view_worker
status:: pass

```text
$ /opt/homebrew/bin/python3 scripts/kb_build_view.py
rendered 4 adopted cards and wrote kb/_index.yaml

$ /opt/homebrew/bin/python3 scripts/kb_build_index.py
wrote kb/_index.yaml with 4 adopted nodes

$ /opt/homebrew/bin/python3 scripts/kb_parse_citations.py
wrote generated/citation_graph.yaml and generated/backlinks.yaml with 51 edges

$ /opt/homebrew/bin/python3 scripts/kb_compute_impact.py
wrote generated/impact_queue.yaml with 0 impacts

$ /opt/homebrew/bin/python3 scripts/kb_status.py
wrote generated/status.yaml
adopted_nodes=4 citation_edges=51 impact_queue_open=0
```

## Build Counts

- adopted_nodes: 4
- citation_edges: 51
- impact_queue_open: 0

