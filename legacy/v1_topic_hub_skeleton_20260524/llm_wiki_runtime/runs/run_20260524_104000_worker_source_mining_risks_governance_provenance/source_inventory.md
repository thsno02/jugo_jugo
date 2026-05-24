# Source Inventory

| source_id | source_type | local_path | role | source_grade_for_candidate |
|---|---|---|---|---|
| `repo-atomicstrata-llm-wiki-compiler` | github_repo | `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md` | Direct implementation evidence for provenance/review/lint controls. | A for implementation features; B for generalizing to the pattern. |
| `repo-kytmanov-obsidian-local` | github_repo | `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` | Direct implementation evidence for local-first review, hashes, citations, hand-edit protection, and low-confidence annotations. | A for implementation features; B for generalizing. |
| `arxiv-wicer` | paper | `data/raw/arxiv/arxiv-wicer/text.txt`; `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` | LLM Wiki-specific empirical source for compilation loss and evaluate/refine mitigation. | A for reported benchmark/limitations; B for broad deployment generalization. |
| `arxiv-memory-as-metabolism` | paper | `data/raw/arxiv/arxiv-memory-as-metabolism/text.txt`; `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` | LLM Wiki-adjacent governance/drift theory source. | B for governance framing; C for empirical risk magnitude. |
| `arxiv-alce` | paper | `data/raw/arxiv/arxiv-alce/text.txt`; `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` | Adjacent citation-generation/evaluation evidence. | B for LLM Wiki citation-risk analogy; A for ALCE's own benchmark claims. |
| `arxiv-etamp-memory-poisoning` | paper | `data/raw/arxiv/arxiv-etamp-memory-poisoning/text.txt`; `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` | Adjacent persistent-memory poisoning threat model. | B for analogy to agent-readable memory; not direct LLM Wiki incident evidence. |
| `arxiv-poisonedrag` | paper | `data/raw/arxiv/arxiv-poisonedrag/text.txt`; `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` | Adjacent RAG knowledge-base poisoning threat model. | B for source/database poisoning analogy; not direct LLM Wiki incident evidence. |
| `arxiv-graph-poisoning` | paper | `data/raw/arxiv/arxiv-graph-poisoning/text.txt`; `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` | Adjacent graph-construction poisoning threat model. | B for compiled-structure poisoning analogy; not direct LLM Wiki incident evidence. |
| `hacker-news-original-thread` | discussion | `data/raw/hacker_news/hacker-news-original-thread/text.txt` | Early discourse seed for stale claims, drift, contradiction scaling, human review, and second-order information. | C as discourse, not technical authority. |
| `owasp-llm-top10-2025` | webpage | `data/raw/webpage/owasp-llm-top10-2025/text.txt` | Process/security framework existence and broad LLM app risk framing. | B for framework existence; C for LLM Wiki-specific claims. |
| `owasp-agentic-top10-2026` | webpage | `data/raw/webpage/owasp-agentic-top10-2026/text.txt` | Agentic application security framework existence and operational risk framing. | B for framework existence; C for LLM Wiki-specific claims. |
| `nist-gai-profile` | webpage | `data/raw/webpage/nist-gai-profile/text.txt` | Voluntary GAI risk-management profile source. | B for governance vocabulary; not LLM Wiki-specific. |
| `microsoft-agent-governance-toolkit-docs` | docs | `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` | Vendor/toolkit control vocabulary for policy, authorization, approval, tracing, sandboxing, DLP, red-team testing. | B for available controls vocabulary; C for LLM Wiki necessity. |
| `reports/coverage_framework.md` | process report | `reports/coverage_framework.md` | Defines KB evidence standards and required risk/governance coverage. | Process source only. |
| `reports/source_gap_review.md` | process report | `reports/source_gap_review.md` | Summarizes local coverage and gaps. | Process source only. |

