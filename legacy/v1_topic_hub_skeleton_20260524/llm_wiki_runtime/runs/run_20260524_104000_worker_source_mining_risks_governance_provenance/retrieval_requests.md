# Retrieval Requests

run_id:: run_20260524_104000_worker_source_mining_risks_governance_provenance
target_candidate:: cand_008_risks_governance_provenance
status:: no_retrieval_required_before_build
created_by:: worker_executor

## Decision

retrieval_required_before_build:: false

Local evidence is sufficient for a bounded first-version risk/governance/provenance node. No network retrieval was attempted because the task packet says to default to local corpus, and no directly needed source is missing for the bounded v1.

## Deferred Retrieval Requests

### req_cand008_owasp_detail_pages

status:: deferred
why_current_data_is_insufficient:: Captured OWASP local pages are high-level landing pages and do not preserve detailed category text.
missing_evidence:: Detailed LLM Top 10 and Agentic Top 10 categories relevant to prompt injection, data poisoning, excessive agency, sensitive information disclosure, supply chain, and governance controls.
desired_source_types:: Official OWASP whitepapers/category pages preserved under `data/raw/`.
suggested_queries:: `site:genai.owasp.org OWASP Top 10 LLM 2025 PDF`; `site:genai.owasp.org Agentic Applications 2026 Top 10 PDF`.
acceptance_criteria:: Raw files preserved, manifest updated, source-mined before any detailed OWASP category claims enter a card.

### req_cand008_enterprise_governance_primary_sources

status:: deferred
why_current_data_is_insufficient:: Current corpus has vendor/toolkit docs and process frameworks but lacks independent enterprise governance evidence for LLM Wiki-like systems.
missing_evidence:: Access control, multi-user approval, audit trail, retention/deletion, source licensing, and compliance process examples.
desired_source_types:: Standards, primary product docs with exact controls, independent case studies, legal/licensing guidance.
suggested_queries:: `agent memory governance audit trail access control`; `AI knowledge base source licensing retention policy`; `LLM agent memory DLP audit logging`.
acceptance_criteria:: Preserved source with clear date/org, exact controls, and limitations.

### req_cand008_community_discourse_reddit

status:: deferred_company_network_block
why_current_data_is_insufficient:: Local Reddit pages are blocked and cannot support substantive claims.
missing_evidence:: Broader community criticism, plugin reception, long-PDF/PDF/PPT handling concerns, privacy concerns, and adoption friction.
desired_source_types:: Reddit pages or mirrors preserved as raw text, if accessible later.
suggested_queries:: Use existing blocked Reddit source ids as retrieval seeds on a network where access is allowed.
acceptance_criteria:: Non-blocked text preserved locally and separately mined.

