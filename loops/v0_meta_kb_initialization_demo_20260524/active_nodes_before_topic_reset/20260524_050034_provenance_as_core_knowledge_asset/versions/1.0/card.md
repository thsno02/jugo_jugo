# Provenance 是核心知识资产，不是附录

在初始化 contract 中，`card.md` 写知识结果，`provenance.md` 写这个结果为什么存在、用了哪些输入、哪些部分是 synthesis、citation 为什么这样选、为什么允许 adoption，以及什么情况会触发 revision。[^1]

这使 provenance 成为可复用知识对象的一部分，而不是事后说明。Source preservation 给 auditor 材料可查，但 provenance 解释 agent 如何从材料走到 adopted node。[^2]

如果缺少 provenance，后续 agent 即使找到 raw files，也可能无法理解 synthesis boundary、adoption rationale 或被拒绝的 evidence。[^3]

## Footnotes

[^1]:
    target: loop_plan_init_kb.md
    target_version: plan_snapshot_2026-05-24
    pinned_version: loop_plan_init_kb.md
    citation_role: process_contract
    why_cited: 该文件定义了本 demo 的初始化 loop、version bundle、provenance、citation、adoption 与 impact 规则。
    evidence_summary: 计划明确要求 nodes 是版本化知识对象库，kb/ 是 adopted view，citation 驱动 impact，动态检索必须受控并沉淀为 data asset。

[^2]:
    target: kb/20260524_050033_source_preservation_precondition_trust.md
    target_version: 1.0
    pinned_version: nodes/20260524_050033_source_preservation_precondition_trust/versions/1.0/card.md
    citation_role: claim_support
    why_cited: 支持 audit 依赖可检查 source paths 和 source records 的主张。
    evidence_summary: 被引 node 说明 preserved evidence 为什么是后续信任检查的前提。

[^3]:
    target: data/raw/arxiv/arxiv-alce/text.txt
    target_version: source_snapshot_2026-05-21
    pinned_version: data/raw/arxiv/arxiv-alce/text.txt
    citation_role: research_context
    why_cited: 支持 citation 不能只看形式存在，还需要评价 citation quality 与 verifiability。
    evidence_summary: ALCE 摘要把 citation 作为提升事实正确性和可验证性的机制，并提出自动评价 citation quality。
    source_path: data/raw/arxiv/arxiv-alce

## References

### [R1] 工作定义
    target: kb/20260524_050031_llm_wiki_working_definition.md
    target_version: 1.0
    pinned_version: nodes/20260524_050031_llm_wiki_working_definition/versions/1.0/card.md
    citation_role: background_definition
    why_cited: 提供 provenance 所处的 source-backed maintained-wiki 语境。
    evidence_summary: 被引 node 把 KB 定义为 grounded in preserved sources 的 maintained artifact。

### [R2] Source gap review
    target: reports/source_gap_review.md
    target_version: source_snapshot_2026-05-21
    pinned_version: reports/source_gap_review.md
    citation_role: evidence_inventory
    why_cited: 该报告总结了本地 raw corpus、覆盖状态和硬性 evidence gap。
    evidence_summary: 报告记录了 origin/workflow/implementation 证据，也记录了 Reddit 与 AICritique 等受阻来源。
