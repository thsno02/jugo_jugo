# Migration Trace

decision:: migration_applied

## Fresh Pre-Migration Scan

Checked 12 files:

- 6 adopted `kb/*.md` view cards.
- 6 adopted selected-version `nodes/*/versions/*/card.md` files.

Pre-migration result:

- checked: 12
- passing: 2
- failing: 10

Failing files matched the previous legacy audit exactly: the five legacy adopted nodes and their five KB views still had `## Footnotes` before `## References`; the `cand_008` node and KB view already passed.

## Migration Operation

For each failing file, moved the complete `## Footnotes` section to the end of the file. No claims, inline footnote markers, footnote ids, reference entries, citation targets, `why_cited`, `evidence_summary`, or node metadata were changed.

## Files Reordered

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`

## Mechanical Refresh

Ran the existing view/index/citation/status scripts after the source card migration:

- `scripts/kb_build_view.py`
- `scripts/kb_build_index.py`
- `scripts/kb_parse_citations.py`
- `scripts/kb_compute_impact.py`
- `scripts/kb_status.py`

The refresh preserved the adopted KB counts and citation counts:

- adopted_nodes: 6
- citation_edges: 110
- impact_queue_open: 0
