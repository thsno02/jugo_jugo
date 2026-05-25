# Source Notes

## Direct Implementation Evidence

`repo-atomicstrata-llm-wiki-compiler` is the strongest implementation source for provenance controls. It documents source attribution in frontmatter, paragraph markers, line-range claim citations, lint validation for missing source files and malformed/impossible ranges, candidate review queues, confidence and contradiction metadata, read-only viewer provenance/citation chips, and a roadmap that still lists rollback/audit/source lifecycle and stale-claim checks as future work.

`repo-kytmanov-obsidian-local` is a useful local-first implementation source. It documents source hashes for synthesized pages, refusal to overwrite manually edited syntheses, interactive draft review, review feedback injection, low-confidence and single-source annotations, stale-article linting, inline source citations, isolated provider-switch previews, and a conservative rule that named references should not become concept articles unless source content supports them.

## LLM Wiki / Wiki-Memory Research Evidence

`arxiv-wicer` is direct LLM Wiki research evidence. It frames the pattern as compiling domain knowledge into a persistent artifact and identifies a compilation gap: blind compilation can discard critical facts. Its reported benchmark is strong enough to support a bounded claim that compilation and maintenance must be evaluated and refined, but it must not be generalized into production reliability or universal effectiveness.

`arxiv-memory-as-metabolism` is governance/drift evidence for personal wiki-style memory architectures. It directly names LLM Wiki as part of a 2026 cluster and proposes governance obligations around drift, source preservation, audit, and retention. It is more normative/theoretical than empirical, so use it for design obligations and failure-mode vocabulary, not measured incident rates.

## Citation / Provenance Evaluation Evidence

`arxiv-alce` is adjacent but important. It shows that citation generation/evaluation is itself hard: systems retrieve supporting evidence and generate citations, citation quality is evaluated separately, and even strong models can lack complete citation support. Use it to argue that LLM Wiki provenance must be validated claim-by-claim; do not treat ALCE as an LLM Wiki evaluation.

## Adjacent Security Evidence

`arxiv-etamp-memory-poisoning` supports a persistent-memory threat model: memory creates cross-session attack surfaces when untrusted observations become future context. For LLM Wiki, this maps only by analogy to agent-readable persistent wiki memory and source ingestion; it is not a documented LLM Wiki exploit.

`arxiv-poisonedrag` supports a knowledge-database poisoning threat model for RAG. It should be cited as adjacent evidence that external knowledge stores can be an attack surface. Do not claim the same attack success rates for LLM Wikis.

`arxiv-graph-poisoning` supports a GraphRAG construction-poisoning threat model: modifying source text can distort generated structures and downstream reasoning. For LLM Wiki, this maps to compiled wiki/source transformation risk by analogy only.

## Framework / Process Evidence

`owasp-llm-top10-2025` and `owasp-agentic-top10-2026` are high-level pages in the local corpus. The captured text supports that OWASP has community/peer-reviewed security frameworks for LLM and agentic applications, but the local page text does not include detailed category bodies. Use only for broad security framing.

`nist-gai-profile` is a government risk-management profile page for GAI, voluntary and cross-sectoral. It is useful for governance vocabulary, not LLM Wiki-specific requirements.

`microsoft-agent-governance-toolkit-docs` lists concrete governance mechanisms: policy engines, approval workflows, prompt injection detection, DLP, sandboxing, signing, observability/tracing, kill switch, rate limiting, lifecycle, compliance verification, liability/attribution, and offline receipts. Because it is vendor/toolkit documentation, use it as control vocabulary, not independent proof of effectiveness.

## Early Discourse Evidence

`hacker-news-original-thread` provides early criticism and support: raw-source backlinks as a defense against staleness/correctness/drift, concern that linting inconsistencies may scale poorly, concern that LLM-generated wiki pages accumulate second-order errors, and emphasis that documentation changes should be reviewed. Treat as discourse, not a benchmark.

## Evidence Boundary

The local corpus is enough for a bounded v1 node on risk taxonomy and governance controls. It is not enough for enterprise compliance sufficiency, real-world incident rates, legal advice, measured risk reduction, or broad multi-user deployment claims.

