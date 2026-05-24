# Validation Trace

run_id:: run_20260524_140000_worker_adoption_view_evaluation_evidence
executor_role:: worker_executor
candidate:: cand_007_evaluation_evidence
node_id:: 20260524_132000_llm_wiki_evaluation_evidence
version:: 1.0
decision:: validation_passed

## Pre-View Checks

- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md`
  - result: pass
  - output: `card validation passed: 1 cards`
- `footnote_layout_gate` on version card:
  - result: pass
  - `## References` line 17
  - `## Footnotes` line 217
  - final top-level section: `## Footnotes`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_132000_llm_wiki_evaluation_evidence`
  - result: expected intermediate failure before view render
  - output: `paths.kb_view does not exist: kb/20260524_132000_llm_wiki_evaluation_evidence.md`
  - resolution: ran view build, then target node validation passed.

## Post-Adoption Validators

- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_132000_llm_wiki_evaluation_evidence`
  - result: pass
  - output: `node validation passed: 1 nodes`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all`
  - result: pass
  - output: `node validation passed: 8 nodes`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md`
  - result: pass
  - output: `card validation passed: 1 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py kb/20260524_132000_llm_wiki_evaluation_evidence.md`
  - result: pass
  - output: `card validation passed: 1 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all`
  - result: pass
  - output: `card validation passed: 16 cards`

## Footnote Layout Gate

- Version card: pass. `## References` line 17; `## Footnotes` line 217; final top-level section `## Footnotes`.
- KB view: pass. `## References` line 17; `## Footnotes` line 217; final top-level section `## Footnotes`.

## YAML Parse Check

- YAML parse passed for 9 files:
  - `.llmwiki/control/state.yaml`
  - `.llmwiki/control/action_queue.yaml`
  - `kb/_index.yaml`
  - `generated/status.yaml`
  - `generated/citation_graph.yaml`
  - `generated/backlinks.yaml`
  - `generated/impact_queue.yaml`
  - `nodes/20260524_132000_llm_wiki_evaluation_evidence/node.yaml`
  - `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml`

## Final Counts

- adopted nodes count: 8
- citation edge count: 185
- open impact count: 0

