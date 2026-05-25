# 当前 KB 初始化 loop 把 raw data 转化为可审计 adopted nodes

当前 demo loop 从已经保存的本地 data 出发，创建小型 node version bundle，记录 provenance，审计 citation，把通过审计的版本 adopted 到 `kb/`，再从 citation 派生 graph 和 impact artifacts，而不是手写维护 graph。[^1]

这个流程把 LLM Wiki 工作定义落实为 filesystem contract：raw sources 留在 `data/`，维护层知识对象放在 `nodes/`，adopted cards 渲染到 `kb/`，可重建的后处理结果放在 `generated/`。[^2]

这个 loop 的目标很窄：它不是一次性写出完美百科，而是验证 agent 能不能持续生产、采纳、审计、解释和更新可追溯知识对象。[^3]

## Footnotes

[^1]:
    target: loop_plan_init_kb.md
    target_version: plan_snapshot_2026-05-24
    pinned_version: loop_plan_init_kb.md
    citation_role: process_contract
    why_cited: 该文件定义了本 demo 的初始化 loop、version bundle、provenance、citation、adoption 与 impact 规则。
    evidence_summary: 计划明确要求 nodes 是版本化知识对象库，kb/ 是 adopted view，citation 驱动 impact，动态检索必须受控并沉淀为 data asset。

[^2]:
    target: kb/20260524_050031_llm_wiki_working_definition.md
    target_version: 1.0
    pinned_version: nodes/20260524_050031_llm_wiki_working_definition/versions/1.0/card.md
    citation_role: background_definition
    why_cited: 提供本 loop 正在操作化的 adopted working definition。
    evidence_summary: 被引 node 定义了由来源支撑、由 agent 维护的持久 wiki artifact。

[^3]:
    target: reports/source_gap_review.md
    target_version: source_snapshot_2026-05-21
    pinned_version: reports/source_gap_review.md
    citation_role: evidence_inventory
    why_cited: 该报告总结了本地 raw corpus、覆盖状态和硬性 evidence gap。
    evidence_summary: 报告记录了 origin/workflow/implementation 证据，也记录了 Reddit 与 AICritique 等受阻来源。

## References

### [R1] Source manifest
    target: data/manifests/sources.jsonl
    target_version: source_snapshot_2026-05-24
    pinned_version: data/manifests/sources.jsonl
    citation_role: source_manifest
    why_cited: 该 manifest 记录 source id、采集状态、本地路径、标签和来源类型。
    evidence_summary: 它是本地 source provenance 的入口，也记录了动态检索新增的成功与失败来源。

### [R2] Runtime 实现例子
    target: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    target_version: source_snapshot_2026-05-21
    pinned_version: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    citation_role: implementation_source
    why_cited: 支持 LLM Wiki runtime 可以暴露 raw/wiki/schema workflow、lint、gap mapping 与 MCP/CLI 接口。
    evidence_summary: 页面描述了 runtime、raw asset、wiki output、manifest、compile readiness、lint 和 gap mapping。
    source_path: data/raw/webpage/clawhub-llm-wiki-karpathy
