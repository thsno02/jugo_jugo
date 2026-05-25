# Source Scope

run_id:: run_20260524_132000_worker_source_mining_evaluation_evidence
target_candidate:: cand_007_evaluation_evidence
scope_decision:: local_corpus_first
retrieval_required_before_build:: false

## Candidate Boundary

This mining run supports a bounded first-version node about LLM Wiki evaluation/evidence. The node may describe what should be evaluated and which evidence classes are currently available: source traceability, claim/citation support, compile/evaluate/refine loops, retrieval and generation diagnostics, maintenance/staleness checks, confidence/contradiction labels, review gates, and explicit source gaps.

It must not claim that LLM Wiki generally beats RAG, GraphRAG, PKM, agent memory, or documentation systems. It must not make production ROI, enterprise readiness, market adoption, model-quality ranking, or broad benchmark-leadership claims.

## In-Scope Sources

### Primary / Direct LLM Wiki Evaluation Sources

- `arxiv-wicer`
  - type: arXiv paper
  - paths: `data/raw/arxiv/arxiv-wicer/text.txt`, `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt`, `data/raw/arxiv/arxiv-wicer/metadata.json`
  - role: strongest direct LLM Wiki evaluation source; compile/evaluate/refine algorithm and benchmark-style evidence.
- `arxiv-knowledge-compounding`
  - type: arXiv paper, PDF-only local e-print
  - paths: `data/raw/arxiv/arxiv-knowledge-compounding/text.txt`, `data/raw/arxiv/arxiv-knowledge-compounding/metadata.json`
  - role: direct but narrower economic/token-cost experiment; use cautiously because local corpus has abstract metadata and PDF-only source, not extracted full experiment logs.
- `repo-atomicstrata-llm-wiki-compiler`
  - type: GitHub repo README
  - path: `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
  - role: implementation evidence for claim-level provenance, lint validation, confidence/contradiction metadata, review queue, and explicit future evaluation harness.
- `repo-kytmanov-obsidian-local`
  - type: GitHub repo README
  - path: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`
  - role: implementation evidence for compare previews, source hashes, non-overwrite behavior, item audit, rejection feedback, and low-confidence/single-source draft annotations.

### Adjacent Evaluation Sources

- `arxiv-alce`
  - type: arXiv paper
  - paths: `data/raw/arxiv/arxiv-alce/text.txt`, `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`, `data/raw/arxiv/arxiv-alce/metadata.json`
  - role: adjacent citation-generation and citation-quality evaluation evidence.
- `arxiv-ragas`
  - type: arXiv paper
  - paths: `data/raw/arxiv/arxiv-ragas/text.txt`, `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt`, `data/raw/arxiv/arxiv-ragas/metadata.json`
  - role: adjacent RAG evaluation dimensions: faithfulness, answer relevance, context relevance.
- `arxiv-ares`
  - type: arXiv paper
  - paths: `data/raw/arxiv/arxiv-ares/text.txt`, `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt`, `data/raw/arxiv/arxiv-ares/metadata.json`
  - role: adjacent RAG evaluation system with context relevance, answer faithfulness, answer relevance, PPI/human-validation boundary, and domain-shift limitations.
- `arxiv-ragchecker`
  - type: arXiv paper
  - paths: `data/raw/arxiv/arxiv-ragchecker/text.txt`, `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`, `data/raw/arxiv/arxiv-ragchecker/metadata.json`
  - role: adjacent fine-grained RAG diagnostic framework based on claim extraction and entailment.
- `repo-amazon-ragchecker` and `repo-stanford-ares`
  - type: GitHub repo READMEs
  - paths: `data/raw/github_repo/repo-amazon-ragchecker/repo/README.md`, `data/raw/github_repo/repo-stanford-ares/repo/README.md`
  - role: implementation documentation for adjacent evaluation tooling, not LLM Wiki evidence.

### Secondary / Process Sources

- `reports/coverage_framework.md`
  - role: process framework for evaluation dimensions, evidence grades, claim records, citation discipline, and judgment gates.
- `reports/source_gap_review.md`
  - role: local corpus gap review; process evidence for what remains missing.

### Prior KB Anchors

Adopted KB anchors were read only for continuity and boundaries. They are not new evidence sources for final claims.

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`
- `kb/20260524_122000_llm_wiki_implementation_ecosystem.md`

## Readability / Byte Verification

Local command checks verified non-empty readable files before mining:

- arXiv scope files: `wc -c` reported nonzero byte sizes for ALCE, Ragas, ARES, RAGChecker, WiCER, Knowledge Compounding, and Memory as Metabolism text/source bundles.
- implementation/process scope files: `wc -c` reported nonzero byte sizes for Atomicstrata README, Kytmanov README, RAGChecker README, ARES README, `reports/coverage_framework.md`, and `reports/source_gap_review.md`.

No scoped source was declared empty.
