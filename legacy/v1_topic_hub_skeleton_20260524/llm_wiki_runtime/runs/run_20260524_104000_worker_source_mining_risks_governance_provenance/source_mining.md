# Source Mining

run_id:: run_20260524_104000_worker_source_mining_risks_governance_provenance
target_candidate:: cand_008_risks_governance_provenance
decision:: ready_to_plan

## Source-Backed Observations

| type | source_id/path | observation | candidate use | confidence |
|---|---|---|---|---|
| implementation evidence | `repo-atomicstrata-llm-wiki-compiler` / README | The implementation supports source attribution in page frontmatter, paragraph source markers, and claim-level line-range citations. Its lint validates malformed citations, missing files, impossible ranges, and out-of-range references. | Direct support for provenance/traceability controls and citation-audit boundaries. | high for implementation fact; medium for pattern-level generalization |
| implementation evidence | `repo-atomicstrata-llm-wiki-compiler` / README | The implementation has a candidate review queue where generated pages can be inspected, approved, rejected, or archived before landing in the wiki. | Direct support for human review / approval gate as a governance control. | high |
| implementation evidence | `repo-atomicstrata-llm-wiki-compiler` / README | Compiled pages can carry confidence, provenance state, and contradiction metadata; lint surfaces low-confidence pages, contradicted pages, and excess uncited paragraphs. | Direct support for uncertainty labels, conflict surfacing, and overclaim detection. | high |
| implementation evidence | `repo-atomicstrata-llm-wiki-compiler` / README | The roadmap lists rollback/audit/source lifecycle, stale-claim checks, freshness reports, and durable operation logs as planned rather than fully implemented items. | Supports boundary: do not claim mature rollback/audit/freshness in current implementation. | high |
| implementation evidence | `repo-kytmanov-obsidian-local` / README | Synthesized pages store source question, selected source pages, and source page hashes; update-in-place refuses to overwrite a manually edited synthesis. | Direct support for source-hash traceability and hand-edit protection. | high |
| implementation evidence | `repo-kytmanov-obsidian-local` / README | Drafts can be reviewed interactively; rejection feedback is injected into later compile prompts; drafts with low confidence or sparse sources get visible editor annotations. | Supports human review and weak-evidence warning controls. | high |
| implementation evidence | `repo-kytmanov-obsidian-local` / README | Named references are preserved as candidate items and should not become concept articles unless source content supports them. | Supports anti-hallucination and source-support gate. | high |
| observed fact | `arxiv-wicer` | The paper reports that blind LLM Wiki compilation can catastrophically discard critical facts and gives measured failure rates in its RepLiQA setup. | Direct support for compilation-loss/maintenance risk in LLM Wiki systems. | high for reported result; medium for generalization |
| method | `arxiv-wicer` | WiCER evaluates compiled wikis against diagnostic probes, diagnoses dropped facts, and forces preservation in later compilations. | Supports evaluate/refine and dropped-fact diagnosis as a governance/quality control. | high |
| gap/limitation | `arxiv-wicer` | The paper's limitations include hardware/model specificity, fixed RAG baseline, partial validation, and LLM-as-judge limitations. | Supports citation constraint: do not overgeneralize WiCER into universal production reliability. | high |
| interpretation | `arxiv-memory-as-metabolism` | The paper frames personal wiki-style memory systems, including LLM Wiki, as subject to user-coupled drift and entrenchment; it proposes TRIAGE, DECAY, CONTEXTUALIZE, CONSOLIDATE, and AUDIT. | Supports maintenance/governance risk and audit-cycle vocabulary. | medium-high |
| method | `arxiv-memory-as-metabolism` | The paper states external sources should be preserved rather than discarded after compression and that state transitions require audit records. | Supports source preservation and audit-record requirements as governance obligations. | medium-high |
| gap/limitation | `arxiv-memory-as-metabolism` | The paper is explicit that its single-agent safety story is partial and includes open problems around audit sensitivity and user evidence. | Supports bounded claims and retrieval/defer gaps around empirical governance. | high |
| observed fact | `arxiv-alce` | ALCE requires systems to retrieve supporting evidence and generate answers with citations, evaluates fluency/correctness/citation quality, and reports that even best models can lack complete citation support. | Adjacent evidence that citations require explicit evaluation and cannot be trusted merely because they exist. | high for ALCE; medium for LLM Wiki analogy |
| gap/limitation | `arxiv-alce` | The paper notes citation precision/recall evaluation limitations, including partial support cases and NLI limits. | Supports nuanced citation audit boundaries. | high |
| risk | `arxiv-etamp-memory-poisoning` | Persistent agent memory can become an attack surface when untrusted environmental observations are stored and later retrieved across sessions/sites. | Adjacent threat model for LLM Wiki source ingestion and agent-readable persistent memory; not direct incident evidence. | medium |
| risk | `arxiv-poisonedrag` | RAG knowledge databases can be poisoned by injected malicious texts that induce target answers; reported defenses were insufficient in that setup. | Adjacent source/database poisoning analogy for LLM Wiki source layer; do not transfer attack rates. | medium |
| risk | `arxiv-graph-poisoning` | GraphRAG construction can be distorted by small source-text edits because the pipeline extracts structure from raw text. | Adjacent compiled-structure poisoning analogy for LLM Wiki compilation. | medium |
| discourse note | `hacker-news-original-thread` | Early discussion highlighted raw-source backlinks as needed for staleness/correctness/drift, questioned contradiction-lint scaling, warned about second-order information, and emphasized review of documentation changes. | Early-discourse seed; supports cand_011 merge into cand_008. | medium-low |
| process note | `owasp-llm-top10-2025` | Local text shows OWASP's LLM application security framework exists as a community-driven effort for AI application risks. | Broad security framing only. | medium |
| process note | `owasp-agentic-top10-2026` | Local text describes a peer-reviewed framework for critical risks facing autonomous and agentic AI systems. | Broad agentic risk framing only. | medium |
| process note | `nist-gai-profile` | Local text identifies a cross-sector Generative AI profile of the AI RMF for voluntary risk management. | Governance vocabulary and external risk-management framing. | medium |
| process note | `microsoft-agent-governance-toolkit-docs` | Docs list policy engines, approval workflows, prompt-injection detection, DLP, sandboxing, SBOM/signing, observability/tracing, kill switches, lifecycle, compliance, and attribution controls. | Control vocabulary for node non-goals and governance options; vendor docs only. | medium |
| process note | `reports/coverage_framework.md` | The framework defines LLM Wiki governance coverage around provenance, maintenance, privacy/security, legal/licensing, epistemic risk, and evidence standards. | KB-internal scope and evidence discipline, not external factual authority. | high as process |
| gap | `reports/source_gap_review.md` | Local gap review says risks/governance coverage is medium and missing privacy/security, access control, multi-user governance, audit trails, legal/compliance, poisoning, prompt injection, source licensing, and institutional review. | Supports explicit gaps while allowing bounded v1. | high as process |

## Candidate Synthesis

The first-version node can be bounded as:

LLM Wiki risk is not one generic AI-governance bucket. It comes from the interaction of source preservation, LLM-mediated compilation, persistent wiki artifacts, agent/human writeback, and later reuse. The highest-evidence v1 risks are:

- provenance risk: citations can be broken, broad, malformed, stale, partial, or post-hoc; generated wiki pages can overgeneralize or launder source authority;
- maintenance risk: compiled pages can drop facts, become stale, accumulate contradictions, or drift through repeated updates;
- poisoning/security risk: source, retrieval/database, graph-construction, and persistent-memory poisoning papers provide adjacent threat models for untrusted inputs entering a durable knowledge layer;
- governance risk: agent writes require explicit boundaries for ingest, compile, review, approve, reject, audit, rollback, deletion, and sensitive-source handling;
- epistemic risk: weak sources can become canonical, exploratory synthesis can appear settled, and human thinking/review can be bypassed.

## Evidence Boundary

Ready for node planning with `retrieval_required_before_build: false`, provided the node:

- uses implementation READMEs and WiCER as the strongest LLM Wiki-specific evidence;
- uses ALCE, eTAMP, PoisonedRAG, and GraphRAG poisoning as adjacent evidence only;
- uses OWASP/NIST/Microsoft governance pages for high-level process/control vocabulary only;
- does not claim enterprise readiness, compliance sufficiency, incident rates, measured risk reduction, or real-world LLM Wiki attacks.

