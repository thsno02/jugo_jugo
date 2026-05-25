# Evidence Scope

run_id:: run_20260524_105000_worker_node_planning_risks_governance_provenance
target_candidate:: cand_008_risks_governance_provenance
target_node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
source_mining_run:: .llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance

## Included As Primary LLM Wiki Evidence

- `repo-atomicstrata-llm-wiki-compiler`: implementation evidence for source attribution, paragraph markers, line-range citations, lint validation, review queue, confidence/provenance/contradiction metadata, and explicit roadmap gaps.
- `repo-kytmanov-obsidian-local`: implementation evidence for source hashes, selected-source traceability, manual edit overwrite protection, draft review, low-confidence/single-source annotations, stale linting, and source-supported item ledger.
- `arxiv-wicer`: direct LLM Wiki research evidence for compilation-loss/dropped-fact risk, evaluate/refine control pattern, and limitations.

## Included As Adjacent Evidence

- `arxiv-memory-as-metabolism`: governance/drift/source-preservation/audit-record framing for wiki-like memory systems; not empirical incident-rate evidence.
- `arxiv-alce`: citation-quality and citation-audit difficulty; not an LLM Wiki benchmark.
- `arxiv-etamp-memory-poisoning`: persistent-memory poisoning threat model; not direct LLM Wiki exploit evidence.
- `arxiv-poisonedrag`: RAG knowledge-database poisoning threat model; attack rates cannot be transferred.
- `arxiv-graph-poisoning`: GraphRAG construction-poisoning analogy; not direct LLM Wiki evidence.

## Included As Process, Vocabulary, Or Discourse Only

- `hacker-news-original-thread`: early discourse about staleness, correctness, drift, contradiction-lint scaling, second-order information, and review.
- `owasp-llm-top10-2025`: broad LLM application security framework existence only.
- `owasp-agentic-top10-2026`: broad agentic application security framework existence only.
- `nist-gai-profile`: voluntary GAI governance vocabulary only.
- `microsoft-agent-governance-toolkit-docs`: vendor control vocabulary only.
- `reports/coverage_framework.md`: KB process scope and evidence standards only.
- `reports/source_gap_review.md`: KB process gap boundary only.

## Prior KB Anchors

The adopted origin/canon, working definition, architecture, workflow, and vs-RAG/write-loop nodes may be used only as continuity anchors for terminology and scope. They must not be cited as new evidence for security, governance, incident, or effectiveness claims.

## Excluded Or Deferred Evidence

- Detailed OWASP category claims are deferred until detailed category pages or whitepapers are preserved and mined.
- Enterprise governance primary sources are deferred.
- Reddit/community discourse is deferred because locally available Reddit evidence is blocked or unavailable.
- Legal advice, compliance sufficiency, source licensing policy, privacy implementation guarantees, multi-user access-control sufficiency, and measured risk reduction are out of scope for this node.
