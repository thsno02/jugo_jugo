# 动态检索是受控 fallback，不是临时补料

动态检索只在现有 evidence 不足以支持某个目标 claim 或 node 时才允许，并且必须先把 gap 写下来再搜索。[^1]

本地 source review 已经记录了硬性缺口，包括被 blocked 的 Reddit captures 和被拦截的 enterprise article。这些缺口可以触发 retrieval request，但不能被 unsupported synthesis 静默替代。[^2]

当 retrieval 被使用时，新 source 必须进入 `data/raw/`，写入 source manifest，并出现在 provenance 中；否则 KB 只是多了一段文字，却没有增加 auditability。[^3]

## Footnotes

[^1]:
    target: loop_plan_init_kb.md
    target_version: plan_snapshot_2026-05-24
    pinned_version: loop_plan_init_kb.md
    citation_role: process_contract
    why_cited: 该文件定义了本 demo 的初始化 loop、version bundle、provenance、citation、adoption 与 impact 规则。
    evidence_summary: 计划明确要求 nodes 是版本化知识对象库，kb/ 是 adopted view，citation 驱动 impact，动态检索必须受控并沉淀为 data asset。

[^2]:
    target: reports/source_gap_review.md
    target_version: source_snapshot_2026-05-21
    pinned_version: reports/source_gap_review.md
    citation_role: evidence_inventory
    why_cited: 该报告总结了本地 raw corpus、覆盖状态和硬性 evidence gap。
    evidence_summary: 报告记录了 origin/workflow/implementation 证据，也记录了 Reddit 与 AICritique 等受阻来源。

[^3]:
    target: kb/20260524_050033_source_preservation_precondition_trust.md
    target_version: 1.0
    pinned_version: nodes/20260524_050033_source_preservation_precondition_trust/versions/1.0/card.md
    citation_role: claim_support
    why_cited: 支持新 evidence 必须先保存才能支撑可信 synthesis 的要求。
    evidence_summary: 被引 node 说明 source preservation 是后续 audit 的前提。

## References

### [R1] 当前初始化 loop
    target: kb/20260524_050032_current_kb_initialization_loop.md
    target_version: 1.0
    pinned_version: nodes/20260524_050032_current_kb_initialization_loop/versions/1.0/card.md
    citation_role: process_context
    why_cited: 把受控 retrieval 放回整个 initialization loop。
    evidence_summary: 被引 node 描述了 0-1 node loop、audit、adoption 和 generated artifacts。

### [R2] Source manifest
    target: data/manifests/sources.jsonl
    target_version: source_snapshot_2026-05-24
    pinned_version: data/manifests/sources.jsonl
    citation_role: source_manifest
    why_cited: 该 manifest 记录 source id、采集状态、本地路径、标签和来源类型。
    evidence_summary: 它是本地 source provenance 的入口，也记录了动态检索新增的成功与失败来源。
