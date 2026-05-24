# Source Inventory

run_id:: run_20260524_132000_worker_source_mining_evaluation_evidence
target_candidate:: cand_007_evaluation_evidence

| source_id | source_type | path | role | source_grade_for_candidate | retrieval_state |
| --- | --- | --- | --- | --- | --- |
| arxiv-wicer | arXiv paper | `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` | Direct LLM Wiki compile/evaluate/refine evidence | primary direct | local_ok |
| arxiv-wicer | arXiv abstract page text | `data/raw/arxiv/arxiv-wicer/text.txt` | Metadata/title/date/abstract support | primary direct metadata | local_ok |
| arxiv-knowledge-compounding | arXiv abstract page text | `data/raw/arxiv/arxiv-knowledge-compounding/text.txt` | Direct economic/token experiment claim source | primary direct but narrow | local_ok_pdf_only |
| repo-atomicstrata-llm-wiki-compiler | GitHub README | `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md` | LLM Wiki implementation evidence for provenance/lint/review/eval-harness gap | primary implementation | local_ok |
| repo-kytmanov-obsidian-local | GitHub README | `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` | LLM Wiki implementation evidence for compare, non-overwrite, review, low-confidence annotations | primary implementation | local_ok |
| arxiv-alce | arXiv paper | `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` | Citation-quality and support evaluation | adjacent primary | local_ok |
| arxiv-ragas | arXiv paper | `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` | RAG faithfulness/context/answer evaluation dimensions | adjacent primary | local_ok |
| arxiv-ares | arXiv paper | `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` | RAG context relevance, answer faithfulness/relevance, PPI, domain-shift limits | adjacent primary | local_ok |
| arxiv-ragchecker | arXiv paper | `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` | Claim-level RAG diagnostic metrics and human-correlation meta-evaluation | adjacent primary | local_ok |
| repo-amazon-ragchecker | GitHub README | `data/raw/github_repo/repo-amazon-ragchecker/repo/README.md` | Adjacent tool README for RAGChecker | adjacent implementation | local_ok |
| repo-stanford-ares | GitHub README | `data/raw/github_repo/repo-stanford-ares/repo/README.md` | Adjacent tool README for ARES | adjacent implementation | local_ok |
| reports/coverage_framework.md | process report | `reports/coverage_framework.md` | Evidence-grade, citation, and evaluation-dimension contract | process | local_ok |
| reports/source_gap_review.md | process report | `reports/source_gap_review.md` | Local source gap status and missing evidence | process | local_ok |
| adopted KB anchors | prior KB | `kb/*.md` selected adopted nodes | Continuity and boundaries only | prior anchor, not new evidence | local_ok |

## Inventory Decision

Local corpus is sufficient for a bounded first-version evaluation/evidence node. Dynamic retrieval is not required before build because direct WiCER evidence plus local implementation controls and adjacent evaluation papers support a careful node about evaluation criteria and evidence boundaries.
