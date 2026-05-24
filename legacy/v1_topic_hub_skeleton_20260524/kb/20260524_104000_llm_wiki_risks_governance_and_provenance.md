# LLM Wiki 的风险、治理与 provenance 边界

这个节点的工作定义是：LLM Wiki 的风险不是泛化的“AI governance”问题，而是 raw source、compile/wiki artifact、human/agent writeback、lint/audit、citation/provenance 之间的边界问题。当前证据只支持一个有限结论：LLM Wiki 需要把来源、编译、审查、状态迁移和引用审计做成可追踪对象；这不等于证明它安全、合规、企业可用，或比相邻系统更可靠。[^1][^2][^3][^13]

**来源支持的 provenance 风险。** `llm-wiki-compiler` README 记录了 page frontmatter 的 source attribution、paragraph source markers、claim-level line-range citations，以及 lint 对 missing source files、malformed citations、impossible ranges 和 out-of-range references 的检查。这个实现事实说明：LLM Wiki 的 provenance 不是装饰字段，而是需要被机器和人审查的约束面。相反，若引用缺失、过宽、过期、局部支持或事后补贴，generated wiki page 可能把弱来源包装成 canonical-looking text。这里的后半句是基于实现证据与 ALCE 相邻 citation-evaluation 证据的解释，不是已观测的 LLM Wiki 事故。[^1][^4]

**引用存在不等于引用忠实。** ALCE 是相邻证据：它要求系统检索 supporting evidence 并生成 citations，同时把 fluency、correctness 和 citation quality 分开评估；其材料还讨论 partial support、citation recall/precision 与 NLI limits。把这个边界迁移到 LLM Wiki，只能得到谨慎规则：claim-level citation 需要审计，不能把“有 citation target”当成“claim 已被充分支持”。[^4]

**来源支持的 compile/maintenance 风险。** WiCER 直接讨论 LLM Wiki compilation gap：blind compilation 可能在把 raw documents 编译成 wiki 时丢掉 critical facts；WiCER 的 evaluate-diagnose-recompile loop 用 diagnostic probes 发现 dropped facts 并把 preservation constraints 带入后续编译。这个证据支持“编译与维护必须可评估、可修订”，但不支持把 WiCER 写成普遍生产可靠性证明；论文自己的限制包括硬件/模型特定性、RAG baseline 限制、验证范围和 LLM-as-judge 限制。[^3][^5]

**实现证据中的治理控制。** 两个 README 提供的是 implementation-specific controls：`llm-wiki-compiler` 有 `compile --review`、review approve/reject/archive、candidate queue、confidence/provenance/contradiction metadata、low-confidence 与 contradiction lint、read-only viewer 的 provenance/citation chips；`obsidian-local-wiki` 记录 source question、selected source pages、source page body hashes，拒绝覆盖人工编辑过的 synthesis，并提供 interactive draft review、rejection feedback、low-confidence/single-source annotations、stale linting 和 knowledge item ledger。它们证明这些控制在具体实现里被设计或实现过，不证明控制本身已经测得有效。[^1][^2]

**状态迁移边界。** 在当前证据内，最稳妥的 governance model 是 state-change discipline：source ingest 要保留来源与 hash；compile/wiki update 要留下 citation/provenance metadata；draft/generated content 要经过 review/approve/reject；lint/audit 要暴露 low confidence、contradictions、uncited prose、stale articles 或 malformed citations；人工编辑与自动重写之间要有保护；rollback、audit、source lifecycle、freshness report 和 durable operation log 在 `llm-wiki-compiler` 里仍是 roadmap 项，不应写成已成熟能力。[^1][^2]

**相邻安全威胁只能做类比。** eTAMP 说明 persistent web-agent memory 可因 environmental observation 被污染并跨 session/site 激活；PoisonedRAG 说明 RAG knowledge database 是可被 injected malicious texts 利用的 attack surface；GraphRAG poisoning 说明 raw text 到 structured graph 的 construction step 可被小规模文本修改扭曲。这些论文支撑“LLM Wiki 的 source ingestion、persistent wiki memory、compiled structure 有相邻 threat model 需要审计”的类比，但不支持说 LLM Wiki 已发生同类事件，也不支持迁移 attack success rate。[^6][^7][^8]

**相邻治理框架只提供词汇。** Memory as Metabolism 把个人 wiki-style memory 放在 drift、entrenchment、source preservation、audit record 和 AUDIT sensitivity 的框架里，适合作为 governance/drift vocabulary。OWASP LLM/agentic pages、NIST GAI Profile 和 Microsoft Agent Governance Toolkit docs 只能在本节点中作为 broad framework 或 control vocabulary：它们说明外部社区有 LLM/agentic security framework、voluntary GAI risk-management vocabulary、policy/approval/tracing/sandbox/kill-switch 等控制词汇；它们不是 LLM Wiki-specific obligations，也不是合规充分性证据。[^9][^10][^11][^12]

**早期 discourse 是风险提示，不是技术权威。** HN thread 中有人强调 raw source backlinks 对 staleness、correctness、drift 的必要性，也有人担心 contradiction lint scaling、second-order information、LLM-generated wiki noise 和 review burden。这些评论可以解释为什么本节点关注 source traceability、lint scalability、review gates 和 second-order error accumulation；但它们只能作为 discourse seed，不能替代 implementation README、WiCER 或安全论文。[^14]

**可采用的窄结论。** LLM Wiki 的首版风险/治理/provenance 边界可以写成四条：第一，provenance 是 citation target、source hash、line range、source marker、metadata 与 audit record 的组合，而不是单个脚注；第二，compile/wiki maintenance 有 dropped-fact、staleness、contradiction、drift 和 overcanonicalization 风险；第三，review、lint、weak-evidence labels、hand-edit protection、source preservation、rollback/audit roadmap 都是有证据的控制面或待实现边界；第四，security/governance analogies 必须保留 source type 标签，不能把相邻系统结果写成 LLM Wiki 事实。[^1][^2][^3][^13]

**证据缺口。** 当前材料不足以支持 direct LLM Wiki incident evidence、measured mitigation effectiveness、enterprise access-control sufficiency、legal/compliance sufficiency、source licensing policy、multi-user governance、privacy guarantees、detailed OWASP category claims 或 broad adoption/scale conclusions。后续若要写这些，应先保存并 source-mine 对应原始材料，而不是在本节点中扩写。[^15][^16]

## References

### [R1] llm-wiki-compiler README

target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
citation_role: primary_implementation_source
why_cited: Provides direct implementation evidence for source attribution, claim-level provenance, lint, review queue, uncertainty/contradiction metadata, viewer provenance chips, and roadmap boundaries.
evidence_summary: The README is the strongest source for concrete LLM Wiki provenance and review controls in this node.

### [R2] obsidian-local-wiki README

target: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
citation_role: primary_implementation_source
why_cited: Provides direct implementation evidence for local-first source hashes, review feedback, hand-edit protection, weak-evidence annotations, stale linting, and source-supported item ledger.
evidence_summary: The README documents traceability and review controls in an Obsidian-local LLM Wiki implementation.

### [R3] WiCER paper

target: data/raw/arxiv/arxiv-wicer/text.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-wicer/text.txt
citation_role: primary_llm_wiki_research_source
why_cited: Provides LLM Wiki-specific research evidence for compilation gap, dropped facts, and evaluate/refine.
evidence_summary: WiCER supports compile/maintenance risk and bounded evaluate/refine controls.

### [R4] WiCER source bundle

target: data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
citation_role: primary_llm_wiki_method_source
why_cited: Provides method and limitation details needed to avoid overclaiming WiCER's results.
evidence_summary: The bundle documents diagnostic probes, fact pinning, failure-set behavior, limitations, and deployment caveats.

### [R5] ALCE source bundle

target: data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
citation_role: adjacent_citation_evaluation_source
why_cited: Provides adjacent evidence that citation generation requires citation-quality evaluation and can have partial-support edge cases.
evidence_summary: ALCE separates citation quality from correctness and fluency and discusses citation recall, precision, human evaluation, and NLI limitations.

### [R6] eTAMP paper

target: data/raw/arxiv/arxiv-etamp-memory-poisoning/text.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-etamp-memory-poisoning/text.txt
citation_role: adjacent_security_source
why_cited: Provides adjacent persistent-memory poisoning vocabulary for untrusted observations entering durable memory.
evidence_summary: eTAMP is used only as a threat-model analogy for persistent memory, not as LLM Wiki incident evidence.

### [R7] PoisonedRAG paper

target: data/raw/arxiv/arxiv-poisonedrag/text.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-poisonedrag/text.txt
citation_role: adjacent_security_source
why_cited: Provides adjacent RAG knowledge-database poisoning vocabulary for external knowledge stores.
evidence_summary: PoisonedRAG is used only to frame database/source poisoning risk by analogy.

### [R8] GraphRAG poisoning paper

target: data/raw/arxiv/arxiv-graph-poisoning/text.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-graph-poisoning/text.txt
citation_role: adjacent_security_source
why_cited: Provides adjacent graph-construction poisoning vocabulary for compiled structures derived from raw text.
evidence_summary: The paper supports a source-transformation attack-surface analogy, not direct LLM Wiki exploitation.

### [R9] Memory as Metabolism source bundle

target: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
citation_role: adjacent_governance_source
why_cited: Provides adjacent governance vocabulary for drift, entrenchment, source preservation, audit records, and audit sensitivity.
evidence_summary: The source is normative/theoretical and is used for framing, not measured LLM Wiki effectiveness.

### [R10] OWASP LLM Top 10 2025 landing page

target: data/raw/webpage/owasp-llm-top10-2025/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/owasp-llm-top10-2025/text.txt
citation_role: broad_framework_source
why_cited: Provides only broad LLM application security framework context.
evidence_summary: The local capture supports framework existence, not detailed category claims.

### [R11] OWASP Agentic Top 10 2026 landing page

target: data/raw/webpage/owasp-agentic-top10-2026/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/owasp-agentic-top10-2026/text.txt
citation_role: broad_framework_source
why_cited: Provides only broad agentic application security framework context.
evidence_summary: The local capture supports framework existence, not LLM Wiki-specific obligations.

### [R12] NIST GAI Profile

target: data/raw/webpage/nist-gai-profile/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/nist-gai-profile/text.txt
citation_role: broad_governance_source
why_cited: Provides voluntary GAI risk-management vocabulary.
evidence_summary: The source is used for general governance vocabulary, not compliance sufficiency.

### [R13] Microsoft Agent Governance Toolkit docs

target: data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt
citation_role: vendor_control_vocabulary_source
why_cited: Provides control vocabulary such as policy enforcement, sandboxing, tracing, lifecycle, and kill switch.
evidence_summary: The docs are vendor documentation and are not used as proof of LLM Wiki control effectiveness.

### [R14] Hacker News original thread

target: data/raw/hacker_news/hacker-news-original-thread/text.txt
target_version: raw_snapshot
pinned_version: data/raw/hacker_news/hacker-news-original-thread/text.txt
citation_role: discourse_context_source
why_cited: Provides early discourse around staleness, correctness, drift, source backlinks, lint scaling, review, and second-order information.
evidence_summary: The thread is used as discourse only and not as technical authority.

### [R15] Evidence scope for cand_008

target: .llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/evidence_scope.yaml
target_version: planning_snapshot
pinned_version: .llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/evidence_scope.yaml
citation_role: process_scope_source
why_cited: Pins allowed source categories, forbidden uses, retrieval status, and prior-KB limits for this candidate.
evidence_summary: The planning scope is used to keep the node bounded and audit-ready.

### [R16] Source gap review

target: reports/source_gap_review.md
target_version: process_snapshot
pinned_version: reports/source_gap_review.md
citation_role: process_gap_source
why_cited: Provides KB-internal evidence gaps that block broader governance, legal, privacy, enterprise, and incident claims.
evidence_summary: The report documents under-covered risk/governance areas and deferred retrieval needs.

### [R17] Adopted origin/canon node

target: kb/20260524_062000_llm_wiki_origin_and_canon.md
target_version: "1.0"
pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around LLM Wiki canon and overclaim boundaries without serving as new risk/governance evidence.
evidence_summary: The prior node is used only as a terminology and scope anchor.

### [R18] Adopted working definition node

target: kb/20260524_072000_llm_wiki_working_definition.md
target_version: "1.0"
pinned_version: nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around LLM Wiki as source-preserving maintained artifact without serving as primary risk evidence.
evidence_summary: The prior node anchors the local definition but does not support new governance facts.

### [R19] Adopted three-layer architecture node

target: kb/20260524_080000_llm_wiki_three_layer_architecture.md
target_version: "1.0"
pinned_version: nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around raw/wiki/schema layers and helps keep risk claims tied to layer boundaries.
evidence_summary: The prior node is a boundary anchor only.

### [R20] Adopted ingest/compile/query/lint workflow node

target: kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md
target_version: "1.0"
pinned_version: nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around LLM Wiki workflow terms such as ingest, compile, query, file-back, and lint.
evidence_summary: The prior node anchors workflow vocabulary only.

### [R21] Adopted LLM Wiki vs RAG/write-loop node

target: kb/20260524_094000_llm_wiki_vs_rag_write_loop.md
target_version: "1.0"
pinned_version: nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around artifact/workflow boundaries between LLM Wiki and adjacent retrieval or memory systems.
evidence_summary: The prior node is used only to avoid scope drift, not as primary evidence for risk, governance, or security facts.

## Footnotes
[^1]:
    target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    citation_role: primary_implementation_support
    why_cited: Supports implementation-specific claims about source attribution, paragraph markers, claim-level line ranges, lint validation, review queue, confidence/provenance/contradiction metadata, viewer provenance chips, and roadmap boundaries.
    evidence_summary: The README documents source frontmatter, paragraph and line-range citations, lint checks for malformed or impossible citations, review approve/reject flow, metadata and lint rules, read-only viewer provenance/citation chips, and future roadmap items for rollback, audit, stale checks, freshness reports, and durable operation logs.

[^2]:
    target: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
    citation_role: primary_implementation_support
    why_cited: Supports implementation-specific claims about source hashes, selected-source traceability, hand-edit protection, draft review, rejection feedback, low-confidence/single-source annotations, stale linting, and source-supported item ledger.
    evidence_summary: The README describes persisted source question/selected pages/source page body hashes, update-in-place refusal after manual edits, interactive review and rejection feedback, low-confidence and single-source annotations, stale linting, and conservative knowledge item handling.

[^3]:
    target: data/raw/arxiv/arxiv-wicer/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-wicer/text.txt
    citation_role: primary_llm_wiki_research_support
    why_cited: Supports the direct LLM Wiki claim that blind compilation can drop critical facts and that WiCER addresses the compilation gap with evaluate/refine.
    evidence_summary: The abstract frames LLM Wiki as compiling domain knowledge into a persistent artifact, identifies a compilation gap from blind compilation discarding critical facts, and summarizes WiCER's evaluate/refine approach and reported bounded results.

[^4]:
    target: data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
    citation_role: adjacent_citation_audit_support
    why_cited: Supports the bounded analogy that generated citations need separate citation-quality evaluation and may only partially support a claim.
    evidence_summary: ALCE defines citation quality through citation recall and precision, requires retrieval of supporting evidence, discusses partial-support cases and NLI limits, and separates citation quality from correctness and fluency.

[^5]:
    target: data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
    citation_role: primary_llm_wiki_method_and_limit_support
    why_cited: Supports details of the WiCER evaluate-diagnose-recompile method and the limits that prevent overgeneralizing WiCER into universal production reliability.
    evidence_summary: The bundle describes diagnostic probes, failure diagnosis, preservation constraints, targeted fact pinning, random knowledge displacement, and limitations around hardware, model, RAG baseline, validation scope, and LLM-as-judge.

[^6]:
    target: data/raw/arxiv/arxiv-etamp-memory-poisoning/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-etamp-memory-poisoning/text.txt
    citation_role: adjacent_security_threat_model
    why_cited: Supports only the adjacent threat model that persistent agent memory can become a cross-session attack surface through untrusted observations.
    evidence_summary: The abstract describes environment-injected trajectory-based agent memory poisoning, where observations can contaminate memory and activate during later sessions or sites; the card does not transfer its measured rates to LLM Wiki.

[^7]:
    target: data/raw/arxiv/arxiv-poisonedrag/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-poisonedrag/text.txt
    citation_role: adjacent_security_threat_model
    why_cited: Supports only the adjacent analogy that external knowledge databases in retrieval systems can be attack surfaces for malicious text injection.
    evidence_summary: The abstract states that RAG grounds generation on an external knowledge database and proposes knowledge corruption attacks by injecting malicious texts; the card excludes transfer of reported attack rates.

[^8]:
    target: data/raw/arxiv/arxiv-graph-poisoning/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-graph-poisoning/text.txt
    citation_role: adjacent_security_threat_model
    why_cited: Supports only the adjacent analogy that transforming raw text into a compiled structure can introduce poisoning risks.
    evidence_summary: The abstract describes GraphRAG converting raw text into structured knowledge graphs and shows that modifying source text can manipulate graph construction and downstream reasoning; the card does not claim direct LLM Wiki exploitation.

[^9]:
    target: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
    citation_role: adjacent_governance_framing
    why_cited: Provides adjacent governance vocabulary for drift, entrenchment, source preservation, audit records, and audit sensitivity without serving as empirical incident evidence.
    evidence_summary: The source frames personal wiki-style memory systems around TRIAGE, DECAY, CONTEXTUALIZE, CONSOLIDATE, and AUDIT; it requires preserving linkouts/original sources and audit records before state transitions while noting audit sensitivity as an open problem.

[^10]:
    target: data/raw/webpage/owasp-llm-top10-2025/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/owasp-llm-top10-2025/text.txt
    citation_role: broad_framework_vocabulary
    why_cited: Supports only the existence of a broad OWASP LLM application security framework, not detailed LLM Wiki-specific category claims.
    evidence_summary: The captured page describes the OWASP Top 10 for LLM Applications as a community-driven effort about AI application security issues; detailed category bodies were not used.

[^11]:
    target: data/raw/webpage/owasp-agentic-top10-2026/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/owasp-agentic-top10-2026/text.txt
    citation_role: broad_framework_vocabulary
    why_cited: Supports only the existence of a broad agentic AI security framework, not LLM Wiki-specific obligations.
    evidence_summary: The captured page describes the OWASP Top 10 for Agentic Applications 2026 as a peer-reviewed framework for autonomous and agentic AI system risks.

[^12]:
    target: data/raw/webpage/nist-gai-profile/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/nist-gai-profile/text.txt
    citation_role: broad_governance_vocabulary
    why_cited: Supports only voluntary GAI risk-management vocabulary and does not impose LLM Wiki-specific compliance requirements.
    evidence_summary: The page identifies the NIST GAI Profile as a cross-sectoral companion to AI RMF 1.0, intended for voluntary use in risk management.

[^13]:
    target: .llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/evidence_scope.yaml
    target_version: planning_snapshot
    pinned_version: .llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/evidence_scope.yaml
    citation_role: scope_boundary
    why_cited: Pins the planner-authorized evidence boundaries, source categories, prior-KB limits, and forbidden claim classes for this candidate.
    evidence_summary: The evidence scope separates primary LLM Wiki evidence, adjacent evidence, framework/discourse/process sources, and prior-KB anchors; it forbids detailed OWASP claims, enterprise sufficiency, incident-rate claims, and measured effectiveness.

[^14]:
    target: data/raw/hacker_news/hacker-news-original-thread/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/hacker_news/hacker-news-original-thread/text.txt
    citation_role: early_discourse_seed
    why_cited: Supports only early discourse around staleness, correctness, drift, lint scaling, review, second-order information, and source backlinks.
    evidence_summary: The thread includes comments about raw-source backlinks, staleness, correctness, drift, contradiction lint scaling, reviewing documentation changes, and concerns about LLM-generated wiki noise.

[^15]:
    target: reports/source_gap_review.md
    target_version: process_snapshot
    pinned_version: reports/source_gap_review.md
    citation_role: process_gap_boundary
    why_cited: Supports the explicit evidence-gap list and prevents unsupported expansion into enterprise, compliance, privacy, security, licensing, and incident claims.
    evidence_summary: The report marks risks/governance coverage as medium and identifies missing evidence around privacy/security, access control, legal/compliance, poisoning, prompt injection, licensing, and institutional review.

[^16]:
    target: data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt
    citation_role: vendor_control_vocabulary
    why_cited: Provides only vendor control vocabulary for governance mechanisms such as policy, sandboxing, tracing, lifecycle, and kill-switch style controls.
    evidence_summary: The captured docs list runtime governance concepts including policy enforcement, zero-trust identity, execution sandboxing, SRE, kill switch, monitoring, lifecycle, compliance checks, and audit-related mechanisms.
