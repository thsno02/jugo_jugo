# Migration Plan

decision:: execute_minimal_section_order_migration

## Steps

1. Re-scan all `kb/*.md` and `nodes/*/versions/*/card.md` files for the footnote layout gate.
2. Use the previous legacy audit as a seed list, but trust the fresh scan for the final failing set.
3. For each failing file, move the complete `## Footnotes` section to the end of the file.
4. Preserve the `## Footnotes` block text byte-for-byte except for its location in the document and surrounding section separator newlines.
5. Preserve the `## References` block text and every other section body.
6. Run card/node validators, view/index/citation/backlink/impact/status refresh scripts, and the full layout gate after refresh.

## Expected Failing Set

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

## Expected Non-Failing Set

- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`
