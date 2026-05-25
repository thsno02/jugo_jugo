# Legacy Layout Audit

decision:: repair_validated

## Scope

Checked `kb/*.md` and `nodes/*/versions/*/card.md` for the footnote layout gate:

- `## References` before `## Footnotes`
- `## Footnotes` is the final top-level section

## Results

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`: FAIL refs=[63] footnotes=[21] last=(63, '## References')
- `kb/20260524_072000_llm_wiki_working_definition.md`: FAIL refs=[71] footnotes=[21] last=(71, '## References')
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`: FAIL refs=[77] footnotes=[19] last=(77, '## References')
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`: FAIL refs=[91] footnotes=[25] last=(91, '## References')
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`: FAIL refs=[99] footnotes=[25] last=(99, '## References')
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`: FAIL refs=[63] footnotes=[21] last=(63, '## References')
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`: FAIL refs=[71] footnotes=[21] last=(71, '## References')
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`: FAIL refs=[77] footnotes=[19] last=(77, '## References')
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`: FAIL refs=[91] footnotes=[25] last=(91, '## References')
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`: FAIL refs=[99] footnotes=[25] last=(99, '## References')
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`: PASS refs=[25] footnotes=[216] last=(216, '## Footnotes')

## Note

Legacy failures were recorded only. They were not repaired because this worker was scoped to the cand_008 candidate card and skill contract update.

