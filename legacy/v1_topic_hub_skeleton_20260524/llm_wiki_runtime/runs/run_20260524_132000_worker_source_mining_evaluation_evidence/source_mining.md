# Source Mining

run_id:: run_20260524_132000_worker_source_mining_evaluation_evidence
target_candidate:: cand_007_evaluation_evidence

## Mined Observations

### Direct LLM Wiki Evaluation

- observed fact: `arxiv-wicer` directly studies an LLM Wiki / wiki-memory compile-evaluate-refine workflow and makes "compilation gap" the central evaluation problem: a generated wiki can drop critical facts while compressing raw documents.
- observed fact: `arxiv-wicer` reports benchmark-style results over 17 RepLiQA domains and 6,800 questions, comparing full-context/KV-cache, RAG, blind compilation, and WiCER refinement.
- observed fact: `arxiv-wicer` defines a repair loop where diagnostic probes identify dropped facts and subsequent compilations preserve them.
- risk/gap: `arxiv-wicer` is recent and scoped: Apple M4 Pro, Llama 3.1 8B, fixed RAG baseline, partial WiCER validation, LLM-as-judge evaluation, and no broad independent replication in the local corpus.
- candidate knowledge: A first-version LLM Wiki evaluation node can safely say that direct evaluation evidence exists but is bounded: it supports compilation-loss, diagnostic-probe, refinement, baseline, scale, and reproducibility criteria; it does not support general superiority.

### Citation And Claim Support

- observed fact: `arxiv-alce` defines citation generation evaluation around fluency, correctness, and citation quality; it evaluates whether answer statements are fully supported by cited passages and whether citations are relevant.
- observed fact: `arxiv-alce` reports that automatic citation-quality metrics correlate with human judgements, but also records limitations around NLI support detection, partial support, open-ended correctness, and excluded task types.
- candidate knowledge: LLM Wiki nodes should distinguish "claim has a citation" from "citation fully supports the claim"; partial support and unsupported generalization should be explicit audit categories.

### Adjacent RAG Evaluation Dimensions

- observed fact: `arxiv-ragas` identifies faithfulness, answer relevance, and context relevance as central RAG evaluation dimensions, emphasizing whether generated answer claims are grounded in retrieved context.
- observed fact: `arxiv-ares` uses context relevance, answer faithfulness, and answer relevance; it adds synthetic data, lightweight judges, PPI confidence intervals, and human validation data, while recording domain-shift limits.
- observed fact: `arxiv-ragchecker` decomposes answers into claims and evaluates both retrieval and generation modules with metrics such as claim recall, context precision, faithfulness, hallucination, context utilization, and noise sensitivity.
- interpretation: These adjacent frameworks provide useful vocabulary for LLM Wiki query/synthesis evaluation, but they do not evaluate persistent wiki maintenance, source writeback, stale-claim handling, or compiled node trust by themselves.

### Implementation Evidence For Auditability

- observed fact: `repo-atomicstrata-llm-wiki-compiler` documents paragraph source markers, claim-level line-range citations, lint validation of source ranges, low-confidence/contradiction metadata, review queues, and a future evaluation harness for answer quality, citation accuracy, update drift, retrieval recall, and scale curves.
- observed fact: `repo-kytmanov-obsidian-local` documents side-effect-free provider/model compare previews, source page hashes for synthesis pages, refusal to overwrite manually edited synthesis pages, item audit, rejection feedback, auto-block after repeated rejection, and low-confidence/single-source draft warnings.
- implementation evidence: These controls show concrete ways LLM Wiki implementations can express trust state and make claims inspectable, but they are not measurements of reliability.

### Process And Evidence Boundaries

- process note: `reports/coverage_framework.md` requires empirical claims to include baseline and method; it defines evidence grades, claim records, citation discipline, and judgment gates.
- process note: `reports/source_gap_review.md` says current evaluation/quality coverage is medium: WiCER is strongest benchmark-style evidence, while independent replication, broader models/providers, human expert evaluation, citation accuracy audits, long-term drift, and maintenance reliability remain missing.
- candidate knowledge: The first-version node should be an evaluation/evidence map, not a verdict. It can say what a trustworthy LLM Wiki evaluation should measure and which local evidence supports each dimension.

## Candidate Synthesis

`cand_007_evaluation_evidence` is ready for bounded node planning. The strongest defensible statement is:

LLM Wiki evaluation evidence should be expressed as a layered evidence model: direct wiki-memory evidence currently supports compile/evaluate/refine, compilation-loss, scale, and reproducibility boundaries; adjacent RAG/citation frameworks provide reusable metrics for answer grounding, citation support, context relevance, claim recall, faithfulness, hallucination, and noise sensitivity; implementation repos show auditability mechanisms such as source ranges, lint, confidence/contradiction labels, review queues, and safe compare previews; process reports require explicit confidence, missing evidence, and deferred retrieval. This does not prove broad empirical superiority or production reliability.
