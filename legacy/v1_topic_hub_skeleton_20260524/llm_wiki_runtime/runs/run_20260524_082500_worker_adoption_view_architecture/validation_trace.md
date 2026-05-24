# Validation Trace

run_id:: run_20260524_082500_worker_adoption_view_architecture
executor_role:: adoption_view_worker
status:: pass_after_view_build

```text
$ /opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md
card validation passed: 1 cards

$ /opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_080000_llm_wiki_three_layer_architecture
nodes/20260524_080000_llm_wiki_three_layer_architecture/node.yaml: paths.kb_view does not exist: kb/20260524_080000_llm_wiki_three_layer_architecture.md
node validation failed: 1 errors across 1 nodes

$ /opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_080000_llm_wiki_three_layer_architecture
node validation passed: 1 nodes
```

The first node validation was run after root adoption metadata was written but before `kb_build_view.py` rendered the adopted `kb_view`. The allowed rerun after view build passed.
