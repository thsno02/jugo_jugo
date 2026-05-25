# Provenance

node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
version:: 1.0

## Why this version exists

This first version exists because `cand_008_risks_governance_provenance` reached `ready_to_build` with `evidence_state: enough_for_first_version`. The bundle creates a candidate node for the bounded risk, governance, provenance, traceability, and citation-audit boundary around LLM Wiki source ingestion, compile/wiki maintenance, and writeback.

This version is a candidate only. It does not adopt root metadata, write a `kb/` view, update generated indexes, or perform citation/adoption audit.

## Inputs used

### Existing data

Read and used as primary LLM Wiki evidence:

- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`
- `data/raw/arxiv/arxiv-wicer/text.txt`
- `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt`

Read and used as adjacent evidence:

- `data/raw/arxiv/arxiv-memory-as-metabolism/text.txt`
- `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-alce/text.txt`
- `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-etamp-memory-poisoning/text.txt`
- `data/raw/arxiv/arxiv-poisonedrag/text.txt`
- `data/raw/arxiv/arxiv-graph-poisoning/text.txt`

Read and used only as process, vocabulary, or discourse:

- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/webpage/owasp-llm-top10-2025/text.txt`
- `data/raw/webpage/owasp-agentic-top10-2026/text.txt`
- `data/raw/webpage/nist-gai-profile/text.txt`
- `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt`
- `reports/coverage_framework.md`
- `reports/source_gap_review.md`

Read but not used as substantive authority:

- Existing adopted node examples under `nodes/*/versions/1.0/` for local schema and citation formatting convention.
- `.llmwiki/control/action_queue.yaml`, `.llmwiki/control/state.yaml`, `.llmwiki/control/standing_status.md`, and `.llmwiki/control/summary_state.md` for status update conventions.

### Dynamic retrieval, if any

None. No network retrieval was used.

### Prior KB nodes

Read and used only as boundary continuity anchors:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`

### Process artifacts

Read and used:

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`
- `.llmwiki/skills/llmwiki-provenance-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-change-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/next_task_packet.md`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/node_plan.yaml`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/evidence_scope.md`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_inventory.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_notes.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_mining.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/retrieval_requests.md`

Out-of-scope reads were limited to existing examples and control-status convention files. They were not used as authority for risk, governance, or security claims.

## Production rationale

The card centers on LLM Wiki-specific failure surfaces: provenance and citation audit, compile/wiki maintenance, source ingestion, durable memory/writeback, and state-change governance. Primary claims use implementation READMEs and WiCER. ALCE, Memory as Metabolism, eTAMP, PoisonedRAG, and GraphRAG poisoning are explicitly labeled as adjacent. OWASP, NIST, and Microsoft are used only for broad framework or control vocabulary. HN is used only as early discourse.

## Citation rationale

Implementation claims cite the two README files. Compilation-loss and evaluate/refine claims cite WiCER. Citation-audit difficulty cites ALCE as adjacent evidence. Poisoning/security risk is framed through adjacent persistent-memory, RAG-database, and GraphRAG-construction sources. Governance/drift vocabulary cites Memory as Metabolism, OWASP/NIST/Microsoft, and process scope files with explicit limits. Prior KB references are included only as continuity anchors.

## Synthesis decisions

- Source-backed observation: concrete LLM Wiki implementations expose source attribution, source hashes, review gates, lint rules, weak-evidence annotations, and hand-edit protection.
- Source-backed observation: WiCER reports a compilation gap where blind wiki compilation can discard critical facts and uses evaluate/refine to force preservation of dropped facts.
- Adjacent interpretation: citation quality must be audited claim-by-claim because citation presence does not imply complete support.
- Adjacent interpretation: persistent memory, external knowledge databases, and raw-text-to-graph construction provide plausible threat-model vocabulary for LLM Wiki, but not direct LLM Wiki incident evidence.
- Process rationale: OWASP/NIST/Microsoft sources provide broad governance/security vocabulary only.
- Discourse note: HN comments help explain why staleness, review, drift, second-order information, and lint scaling matter, but are not technical authority.
- Evidence gap: no measured mitigation effectiveness, enterprise compliance sufficiency, legal advice, privacy guarantee, access-control sufficiency, direct incident rate, adoption, or scale claim is made.

## Audit trail

The version bundle was generated by `worker_executor` from `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/next_task_packet.md`. The generation entry decision in the task packet was `pass`. The allowed output paths were limited to the candidate version bundle and generation run artifacts, with optional control status updates. Root node metadata, `kb/`, and `generated/` were intentionally not written.

## Adoption rationale

Adoption is pending audit. This version is acceptable as a candidate because it separates primary LLM Wiki evidence from adjacent/security/framework/discourse/prior-KB evidence, preserves evidence gaps, avoids generic AI governance expansion, and keeps the root metadata adoption gate closed. It should not be adopted until citation and adoption audit confirms parseability, source support, source-category separation, overclaim control, provenance completeness, and absence of root adoption metadata.

## Limits and uncertainty

This candidate does not claim that LLM Wiki is secure, compliant, enterprise-ready, privacy-preserving, legally sufficient, measurably safer, widely adopted, or resistant to poisoning. It does not claim OWASP/NIST/Microsoft prescribe LLM Wiki-specific controls. It does not transfer attack success rates from eTAMP, PoisonedRAG, or GraphRAG poisoning. It treats detailed OWASP category pages, enterprise governance primary sources, and blocked Reddit/community discourse as deferred retrieval gaps.

## Revision triggers

- Audit finds citation parsing errors, unresolved paths, unsupported claims, or source-category confusion.
- Audit finds generic AI governance filler, enterprise/compliance sufficiency claims, measured effectiveness claims, or incident-rate claims.
- Audit finds adjacent security papers presented as direct LLM Wiki incidents.
- Audit finds prior KB anchors used as new factual evidence.
- New source mining preserves detailed OWASP category pages, enterprise governance primary sources, incident reports, licensing/privacy evidence, or accessible community discourse.
- Any prior adopted LLM Wiki anchor receives a major update that changes the working definition, architecture, workflow, or adjacent-system boundary.
