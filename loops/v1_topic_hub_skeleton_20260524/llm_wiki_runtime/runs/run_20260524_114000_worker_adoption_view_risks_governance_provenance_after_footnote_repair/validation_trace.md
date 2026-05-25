# Validation Trace

decision:: validation_passed

## Validators

- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`
  - `card validation passed: 1 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all`
  - `card validation passed: 12 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance`
  - `node validation passed: 1 nodes`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all`
  - `node validation passed: 6 nodes`

## Footnote Layout Gate

- target version card: PASS
  - path: `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`
  - `## References` line: 25
  - `## Footnotes` line: 216
  - final top-level section: `## Footnotes`
- target KB view: PASS
  - path: `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`
  - `## References` line: 25
  - `## Footnotes` line: 216
  - final top-level section: `## Footnotes`

## Count Checks

- `generated/status.yaml` adopted_nodes: 6
- `kb/_index.yaml` node_count: 6
- `generated/status.yaml` citation_edges: 110
- `generated/citation_graph.yaml` edge_count: 110
- `generated/status.yaml` impact_queue_open: 0
- `generated/impact_queue.yaml` impact_count: 0

## Protected File Check

`git diff -- nodes/.../versions/1.0/card.md nodes/.../versions/1.0/provenance.md nodes/.../versions/1.0/change.md` produced no output after this worker's edits; this worker did not rewrite protected body files.
