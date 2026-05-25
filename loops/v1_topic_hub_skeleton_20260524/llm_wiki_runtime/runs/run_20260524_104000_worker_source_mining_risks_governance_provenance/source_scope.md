# Source Scope

run_id:: run_20260524_104000_worker_source_mining_risks_governance_provenance
target_candidate:: cand_008_risks_governance_provenance

## In-Scope Source Batch

This batch covers four evidence classes:

1. Direct LLM Wiki implementation evidence for provenance, review, lint, source markers, confidence/contradiction metadata, source hashes, draft review, hand-edit protection, and stale checks.
2. LLM Wiki / wiki-memory research evidence for compilation loss, maintenance drift, audit/refinement loops, and evaluation limits.
3. Adjacent LLM/RAG/GraphRAG/agent-memory security evidence for poisoning and persistent memory attack surfaces.
4. Process/governance framework evidence for risk-management vocabulary and operational guardrails.

## Primary / Direct LLM Wiki Sources

| source_id | type | path | readable state | scoped use |
|---|---|---|---|---|
| `repo-atomicstrata-llm-wiki-compiler` | github_repo README | `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md` | readable, 23143 bytes | Implementation evidence for paragraph/claim-level provenance, review queue, lint checks, confidence/contradiction metadata, read-only viewer, roadmap gaps around rollback/audit/stale claims. |
| `repo-kytmanov-obsidian-local` | github_repo README | `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` | readable, 34490 bytes | Implementation evidence for source hashes, review/reject feedback, hand-edit protection, inline citations, low-confidence/single-source annotations, deterministic cleanup, stale article linting. |
| `arxiv-wicer` | arxiv paper | `data/raw/arxiv/arxiv-wicer/text.txt`; `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` | readable, 5146 and 223004 bytes | LLM Wiki-specific empirical evidence for compilation gap, catastrophic failure rates, dropped facts, evaluate/refine loop, and limitations. |

## Governance / Drift Source

| source_id | type | path | readable state | scoped use |
|---|---|---|---|---|
| `arxiv-memory-as-metabolism` | arxiv paper | `data/raw/arxiv/arxiv-memory-as-metabolism/text.txt`; `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` | readable, 5495 and 156462 bytes | Governance/drift source for companion memory, user-coupled drift, TRIAGE/DECAY/CONTEXTUALIZE/CONSOLIDATE/AUDIT, minority-hypothesis retention, source preservation, audit records. |

## Citation / Provenance Evaluation Source

| source_id | type | path | readable state | scoped use |
|---|---|---|---|---|
| `arxiv-alce` | arxiv paper | `data/raw/arxiv/arxiv-alce/text.txt`; `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` | readable, 5177 and 223004 bytes | Adjacent citation evaluation evidence: citation quality remains hard; even best models in ELI5 lacked complete citation support 50% of the time; citation precision/recall evaluation has limits. |

## Adjacent Security / Poisoning Sources

| source_id | type | path | readable state | scoped use |
|---|---|---|---|---|
| `arxiv-etamp-memory-poisoning` | arxiv paper | `data/raw/arxiv/arxiv-etamp-memory-poisoning/text.txt`; `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` | readable, 5496 bytes plus source bundle | Adjacent agent-memory threat model: persistent memory attack surface across websites/sessions through environmental observation. |
| `arxiv-poisonedrag` | arxiv paper | `data/raw/arxiv/arxiv-poisonedrag/text.txt`; `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` | readable, 5619 bytes plus source bundle | Adjacent RAG knowledge-database poisoning threat: injected malicious texts can corrupt retrieved evidence and generated answers. |
| `arxiv-graph-poisoning` | arxiv paper | `data/raw/arxiv/arxiv-graph-poisoning/text.txt`; `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` | readable, 5543 bytes plus source bundle | Adjacent GraphRAG poisoning threat: small source-text modifications can distort constructed graphs and downstream reasoning. |

## Governance / Process Sources

| source_id | type | path | readable state | scoped use |
|---|---|---|---|---|
| `owasp-llm-top10-2025` | webpage | `data/raw/webpage/owasp-llm-top10-2025/text.txt` | readable, 2196 bytes | Process source showing OWASP's AI application security framing; use only as high-level security framework evidence, not as category-detail authority from this text. |
| `owasp-agentic-top10-2026` | webpage | `data/raw/webpage/owasp-agentic-top10-2026/text.txt` | readable, 2456 bytes | Process source for agentic AI security framework existence and operational framing. |
| `nist-gai-profile` | webpage | `data/raw/webpage/nist-gai-profile/text.txt` | readable, 4916 bytes | Process source for voluntary cross-sector GAI risk-management profile; not LLM Wiki-specific. |
| `microsoft-agent-governance-toolkit-docs` | docs page | `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt` | readable, 6743 bytes | Vendor/toolkit docs showing governance control vocabulary: policy, authorization, approval workflows, observability, kill switch, sandboxing, prompt injection detection, DLP. |

## Early Discourse Seed

| source_id | type | path | readable state | scoped use |
|---|---|---|---|---|
| `hacker-news-original-thread` | discussion thread | `data/raw/hacker_news/hacker-news-original-thread/text.txt`; `data/raw/hacker_news/hacker-news-original-thread/item.json` | readable, 50430 bytes plus item JSON | Early discourse only: staleness, correctness, drift, N*N lint scaling, second-order information, human review/thinking-offload concerns. |

## Manifest / Planning Support

- `data/manifests/sources.jsonl` confirms local acquisition status and source ids.
- `data/manifests/claims.jsonl` and `data/manifests/claim_source_links.jsonl` include existing risk/governance/ethics claim records `claim_000037` through `claim_000041`.
- `reports/coverage_framework.md` defines risk/governance coverage criteria and evidence discipline.
- `reports/source_gap_review.md` records local corpus strengths and gaps, including medium risks/governance coverage and missing enterprise/privacy/access-control evidence.

## Prior KB Anchors

Adopted KB anchors for origin, definition, architecture, workflow, and vs-RAG were checked only to preserve topic boundary. They are not used as new primary evidence for external risk, governance, poisoning, security, or citation-evaluation facts.

