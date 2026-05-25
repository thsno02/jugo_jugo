# Source Notes

run_id:: run_20260524_132000_worker_source_mining_evaluation_evidence
target_candidate:: cand_007_evaluation_evidence

## Direct LLM Wiki / Wiki-Memory Evidence

### arxiv-wicer

- observed fact: WiCER frames the LLM Wiki pattern as compiling domain knowledge into a persistent artifact and serving it via KV-cache/full-context inference.
- observed fact: It names the key evaluation failure as a "compilation gap": raw documents distilled into a wiki may discard critical facts.
- observed fact: It tests across 17 RepLiQA domains / 6,800 questions and reports that blind compilation can catastrophically fail; the paper proposes a compile-evaluate-refine loop that diagnoses dropped facts and preserves them in later compilations.
- observed fact: It discloses limitations including hardware specificity, model specificity, a fixed RAG baseline, partial validation scope, and LLM-as-judge concerns.
- candidate use: primary source for saying LLM Wiki evaluation must include compilation-loss detection, diagnostic probes, iteration/refinement, baseline comparison, scale/attention-dilution boundaries, and reproducibility constraints.
- limitation: single recent paper; results should not be generalized to all LLM Wikis, all models, all corpora, or production settings.

### arxiv-knowledge-compounding

- observed fact: The abstract describes a controlled four-query experiment and dynamic ROI model for self-evolving knowledge wikis, comparing a compounding regime against a matched RAG baseline.
- candidate use: cautious evidence that economic/token-cost claims require explicit baseline, task sequence, query concentration, and reproducibility details.
- limitation: local acquisition is PDF-only for the e-print and this run mined the abstract page text, not full logs or independent replication.

### repo-atomicstrata-llm-wiki-compiler

- observed fact: README documents paragraph source markers, claim-level line-range citations, source-range validation in lint, confidence/contradiction metadata, candidate review queues, and read-only viewer provenance/citation chips.
- observed fact: README lists an "Evaluation harness" as future work for answer quality, citation accuracy, update drift, retrieval recall, and scale curves against serious retrieval baselines.
- candidate use: implementation evidence for auditable claims/citations and for treating full evaluation harnesses as partially missing in current tools.
- limitation: author/project documentation; not independent proof that controls are correct or effective.

### repo-kytmanov-obsidian-local

- observed fact: README describes side-effect-free compare preview vaults, source-question/body-hash frontmatter for synthesis pages, duplicate/non-overwrite behavior, item audit, rejection feedback loops, and low-confidence/single-source draft annotations.
- candidate use: implementation evidence for evaluation-adjacent controls: safe comparison, review state, confidence labels, and source-backed publication boundaries.
- limitation: local-first implementation source; not an abstract requirement or independent benchmark.

## Adjacent Evaluation Evidence

### arxiv-alce

- observed fact: ALCE evaluates citation-augmented generation with dimensions including fluency, correctness, and citation quality.
- observed fact: It separates citation recall and citation precision and uses NLI-based support checks with human evaluation.
- observed fact: It states limitations: NLI cannot detect partial support cleanly, open-ended correctness claims may be incomplete, and benchmark coverage misses multi-hop/math/code scenarios.
- candidate use: adjacent evidence for claim/citation support audits and for explicitly marking "partial support" and benchmark-scope limitations.
- limitation: not an LLM Wiki benchmark.

### arxiv-ragas

- observed fact: Ragas identifies RAG evaluation dimensions of faithfulness, answer relevance, and context relevance, with faithfulness defined as whether answer claims are grounded in the provided context.
- observed fact: It emphasizes reference-free evaluation when human annotations or reference answers are unavailable.
- candidate use: adjacent vocabulary for evaluating LLM Wiki query/synthesis output and cited context quality.
- limitation: RAG setting, not persistent wiki maintenance.

### arxiv-ares

- observed fact: ARES evaluates RAG systems along context relevance, answer faithfulness, and answer relevance; it uses synthetic training data, lightweight judges, PPI, and a small human preference validation set.
- observed fact: It reports domain-shift limitations: stronger shifts such as language, text-to-code, extraction, webpages, or citations require reconfiguration or generalize poorly.
- candidate use: adjacent support for requiring in-domain validation and human-check calibration before trusting automated evaluators.
- limitation: evaluates RAG triples, not LLM Wiki compiled artifacts or maintenance state.

### arxiv-ragchecker

- observed fact: RAGChecker decomposes responses into claims and uses entailment to compute overall, retriever, and generator metrics.
- observed fact: It distinguishes retrieval-side claim recall/context precision and generation-side faithfulness, hallucination, context utilization, and noise sensitivity.
- candidate use: adjacent support for claim-level evaluation, module diagnosis, and avoiding a single aggregate "quality" score.
- limitation: RAG diagnostic framework; transfer to LLM Wiki must be framed as analogy or reusable method, not direct proof.

## Process / Gap Evidence

### reports/coverage_framework.md

- process note: lists evaluation dimensions: answer quality, retrieval quality, source fidelity, maintenance quality, agent performance, human usability, cost, robustness, and governance.
- process note: requires empirical claims to include baselines and methods; defines evidence grades and claim records.
- candidate use: local process authority for how this KB should express confidence, claim type, source support, and missing evidence.

### reports/source_gap_review.md

- process note: says evaluation/quality coverage is medium, with WiCER strongest benchmark-style evidence, but independent replication, broader provider tests, long-term drift, citation audits, and human expert evaluation remain missing.
- candidate use: gap framing for a bounded v1 node and deferred retrieval/action items.

## Prior KB Anchors

Adopted KB nodes provide continuity: LLM Wiki is already bounded as raw sources, compiled wiki/node artifact, schema/instruction layer, maintenance workflow, RAG/write-loop comparison, risk/provenance boundary, and implementation ecosystem. They must not be cited as new primary evidence for evaluation claims.
