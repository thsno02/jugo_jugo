# Validation Trace

run_id:: run_20260524_130000_worker_adoption_view_implementation_ecosystem
executor_role:: worker_executor
status:: pass

## Validator commands

- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/card.md`
  - result: pass
  - output: `card validation passed: 1 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_122000_llm_wiki_implementation_ecosystem`
  - first pre-view result: expected fail because `paths.kb_view` did not exist before rendering
  - post-view result: pass
  - output: `node validation passed: 1 nodes`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all`
  - result: pass
  - output: `node validation passed: 7 nodes`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all`
  - result: pass
  - output: `card validation passed: 14 cards`

## Footnote Layout Gate

Contract: `## References` must appear before `## Footnotes`, and `## Footnotes` must be the final top-level section.

- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/card.md`: pass
  - top sections: `(21, ## References)`, `(221, ## Footnotes)`
- `kb/20260524_122000_llm_wiki_implementation_ecosystem.md`: pass
  - top sections: `(21, ## References)`, `(221, ## Footnotes)`

## Generated status check

- adopted_nodes: 7
- citation_edges: 148
- impact_queue_open: 0
- impact_count: 0
