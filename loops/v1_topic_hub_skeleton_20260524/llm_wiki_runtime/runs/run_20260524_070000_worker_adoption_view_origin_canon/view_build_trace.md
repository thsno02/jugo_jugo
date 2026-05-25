# View Build Trace

executor_role:: adoption_view_worker
status:: LOOP_DONE
target_node_id:: 20260524_062000_llm_wiki_origin_and_canon
target_version:: 1.0

## Commands

```text
/opt/homebrew/bin/python3 scripts/kb_build_view.py
```

Result:

```text
rendered 1 adopted cards and wrote kb/_index.yaml
```

```text
/opt/homebrew/bin/python3 scripts/kb_parse_citations.py
```

Result:

```text
wrote generated/citation_graph.yaml and generated/backlinks.yaml with 9 edges
```

```text
/opt/homebrew/bin/python3 scripts/kb_compute_impact.py
```

Result:

```text
wrote generated/impact_queue.yaml with 0 impacts
```

```text
/opt/homebrew/bin/python3 scripts/kb_status.py
```

Result:

```text
wrote generated/status.yaml
adopted_nodes=1 citation_edges=9 impact_queue_open=0
```

## Generated Outputs

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/_index.yaml`
- `generated/citation_graph.yaml`
- `generated/backlinks.yaml`
- `generated/impact_queue.yaml`
- `generated/status.yaml`

## Final Counts

- adopted nodes: 1
- KB view cards: 1
- citation edges: 9
- impact queue open: 0
