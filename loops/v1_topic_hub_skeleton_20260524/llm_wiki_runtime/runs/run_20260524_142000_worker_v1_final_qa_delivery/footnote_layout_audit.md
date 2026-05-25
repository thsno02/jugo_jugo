# Footnote Layout Audit

Run: `run_20260524_142000_worker_v1_final_qa_delivery`
Gate: all adopted selected-version `card.md` files and all `kb/*.md` views

## Contract

- `## References` must appear before `## Footnotes`.
- `## Footnotes` must be the final top-level section.
- No later top-level section may appear after final `## Footnotes`.

## Result

- checked: 16
- pass: 16
- fail: 0

## Files Checked

Selected-version cards:

- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/card.md`
- `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md`

KB views:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`
- `kb/20260524_122000_llm_wiki_implementation_ecosystem.md`
- `kb/20260524_132000_llm_wiki_evaluation_evidence.md`

No layout repair was required in this run.
