# Validation Trace

decision:: validation_passed

## Validators

- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all`
  - result: pass
  - output: `card validation passed: 12 cards`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all`
  - result: pass
  - output: `node validation passed: 6 nodes`

## Mechanical Refresh Commands

- `/opt/homebrew/bin/python3 scripts/kb_build_view.py`
  - result: pass
  - output: `rendered 6 adopted cards and wrote kb/_index.yaml`
- `/opt/homebrew/bin/python3 scripts/kb_build_index.py`
  - result: pass
  - output: `wrote kb/_index.yaml with 6 adopted nodes`
- `/opt/homebrew/bin/python3 scripts/kb_parse_citations.py`
  - result: pass
  - output: `wrote generated/citation_graph.yaml and generated/backlinks.yaml with 110 edges`
- `/opt/homebrew/bin/python3 scripts/kb_compute_impact.py`
  - result: pass
  - output: `wrote generated/impact_queue.yaml with 0 impacts`
- `/opt/homebrew/bin/python3 scripts/kb_status.py`
  - result: pass
  - output: `adopted_nodes=6 citation_edges=110 impact_queue_open=0`

## Footnote Layout Gate

Full post-refresh gate over `kb/*.md` and `nodes/*/versions/*/card.md`:

- checked: 12
- fixed in this run: 10
- remaining failures: 0
- result: pass

Passing files:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`: References line 21, Footnotes line 59
- `kb/20260524_072000_llm_wiki_working_definition.md`: References line 21, Footnotes line 77
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`: References line 19, Footnotes line 84
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`: References line 25, Footnotes line 99
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`: References line 25, Footnotes line 144
- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`: References line 25, Footnotes line 216
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`: References line 21, Footnotes line 59
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`: References line 21, Footnotes line 77
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`: References line 19, Footnotes line 84
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`: References line 25, Footnotes line 99
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`: References line 25, Footnotes line 144
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`: References line 25, Footnotes line 216

## Adopted KB Status

- adopted_nodes: 6
- kb_view_cards: 6
- citation_edges: 110
- impact_queue_open: 0
- remaining layout failures: 0
