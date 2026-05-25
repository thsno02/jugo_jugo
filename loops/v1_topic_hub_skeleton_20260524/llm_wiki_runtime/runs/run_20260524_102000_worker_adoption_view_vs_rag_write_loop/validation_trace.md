# Validation Trace

run_id:: run_20260524_102000_worker_adoption_view_vs_rag_write_loop
executor_role:: worker_executor
target_node_id:: 20260524_094000_llm_wiki_vs_rag_write_loop
version:: 1.0

## Pre-view Card Validation

- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`
  - result: `card validation passed: 1 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all`
  - result: `card validation passed: 9 cards`

## Post-adoption Validation

- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_094000_llm_wiki_vs_rag_write_loop`
  - result: `node validation passed: 1 nodes`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all`
  - result: `node validation passed: 5 nodes`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
  - result: `card validation passed: 1 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all`
  - result: `card validation passed: 10 cards`

## Summary

- card validator target: pass
- card validator all: pass
- node validator target: pass
- node validator all: pass
- adopted nodes count: 5
- citation edge count: 73
- open impact count: 0

