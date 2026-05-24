# Evidence Scope

run_id:: run_20260524_133000_worker_node_planning_evaluation_evidence
target_candidate:: cand_007_evaluation_evidence
target_node_id:: 20260524_132000_llm_wiki_evaluation_evidence
source_mining_run:: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence

## Scope Decision

decision:: local_evidence_sufficient_for_bounded_v1
retrieval_required_before_generation:: false

This node may cover evaluation dimensions, evidence grades, citation auditability, evaluation boundaries, verifiable/unverifiable claims, source gaps, deferred retrieval, and how KB nodes should express confidence.

It must be written as an evidence map, not a victory claim.

## Primary Sources

- `arxiv-wicer`: strongest direct LLM Wiki / wiki-memory evaluation evidence. Use for compile/evaluate/refine, compilation gap, diagnostic probes, refinement loop, baseline comparison, scale boundary, and reproducibility limitations.
- `arxiv-knowledge-compounding`: direct but narrow economic/token-cost framing. Use only to show that economic claims need explicit baselines, method, query sequence, reproducibility, and projection limits.
- `repo-atomicstrata-llm-wiki-compiler`: implementation self-description for source ranges, lint validation, confidence/contradiction metadata, review queues, and future evaluation harness gaps.
- `repo-kytmanov-obsidian-local`: implementation self-description for safe compare previews, source hashes, non-overwrite behavior, item audit, rejection feedback, and low-confidence/single-source draft labels.

## Adjacent Sources

- `arxiv-alce`: citation-generation/citation-quality evaluation vocabulary; use for support vs citation-presence distinctions and partial-support caveats.
- `arxiv-ragas`: RAG faithfulness, answer relevance, and context relevance vocabulary.
- `arxiv-ares`: RAG context relevance, answer faithfulness/relevance, PPI/human validation, and domain-shift limitations.
- `arxiv-ragchecker`: claim-level diagnostics, claim recall, context precision, faithfulness, hallucination, context utilization, and noise sensitivity.

Adjacent sources must be labeled adjacent. They do not prove LLM Wiki reliability.

## Secondary / Process Notes

- `reports/coverage_framework.md`: use for evidence grades, claim records, citation discipline, and judgment gates.
- `reports/source_gap_review.md`: use for current coverage status and missing evidence.
- Source-mining artifacts from `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/`: use for scoped synthesis, gaps, deferred retrieval, and generation boundaries.

## Prior-KB Anchors

Prior adopted nodes may be used only for continuity and boundaries:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`
- `kb/20260524_122000_llm_wiki_implementation_ecosystem.md`

They must not be cited as new primary evidence for evaluation claims.

## Supported Sections

- Evaluation problem: compilation gap, claim loss, and source-support auditability.
- Evidence levels: direct evaluation, implementation-described controls, adjacent evaluation frameworks, process/gap notes, prior-KB continuity.
- Citation auditability: source ranges, citation support vs citation presence, partial support, lint/review gates, confidence and contradiction labels.
- Evaluation dimensions: compilation loss, diagnostic probes, faithfulness, answer relevance, context relevance, claim recall, hallucination, noise sensitivity, drift/staleness, review outcomes, reproducibility, and baseline disclosure.
- Boundary ledger: what is supported, what is adjacent, and what remains deferred.

## Unsupported Claims

- LLM Wiki generally beats RAG, GraphRAG, PKM, agent memory, or documentation systems.
- LLM Wiki has solved hallucination, citation faithfulness, stale claims, or provenance.
- Existing implementations have proven reliability or production readiness.
- WiCER proves all LLM Wikis work at scale.
- Knowledge Compounding proves general ROI or enterprise value.
- Adjacent RAG/citation benchmarks are direct LLM Wiki benchmarks.

## Deferred Retrieval

- WiCER code, benchmark scripts, and exact logs.
- Knowledge Compounding full extraction, method/logs, and reproducibility artifacts.
- Direct local citation audit of adopted KB pages.
- Long-term maintenance/drift data and stale-claim rates.
- Independent replications, user studies, human expert evaluations, negative/failure cases, and broad model/provider/corpus comparisons.
