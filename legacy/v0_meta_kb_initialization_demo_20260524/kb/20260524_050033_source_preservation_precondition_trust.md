# Source preservation 是 KB 信任的前提

如果后续 agent 不能从 synthesized claim 回到背后的保存材料，KB 就无法被真正审计。在这个 repo 里，这意味着 source id、acquisition status、本地 raw path、readable text path、digest、claim links 和 access failure 都要和 synthesized nodes 一起保留下来。[^1]

LLM Wiki 的工作定义依赖这个分层：wiki 是 maintained layer，位于 immutable raw sources 和面向用户的 answers 之间；它不能替代 source record。[^2]

Source preservation 本身不保证 synthesis 为真。它保证 synthesis 可检查：auditor 可以判断一个 claim 是否被支持、是否过宽、是否过期、是否被反驳，或是否只是 process decision。[^3]

## Footnotes

[^1]:
    target: data/manifests/sources.jsonl
    target_version: source_snapshot_2026-05-24
    pinned_version: data/manifests/sources.jsonl
    citation_role: source_manifest
    why_cited: 该 manifest 记录 source id、采集状态、本地路径、标签和来源类型。
    evidence_summary: 它是本地 source provenance 的入口，也记录了动态检索新增的成功与失败来源。

[^2]:
    target: kb/20260524_050031_llm_wiki_working_definition.md
    target_version: 1.0
    pinned_version: nodes/20260524_050031_llm_wiki_working_definition/versions/1.0/card.md
    citation_role: background_definition
    why_cited: 定义 raw-source 与 maintained-wiki 的分工。
    evidence_summary: 被引 node 说明 preserved raw sources 和 maintained wiki artifacts 具有不同职责。

[^3]:
    target: reports/source_gap_review.md
    target_version: source_snapshot_2026-05-21
    pinned_version: reports/source_gap_review.md
    citation_role: evidence_inventory
    why_cited: 该报告总结了本地 raw corpus、覆盖状态和硬性 evidence gap。
    evidence_summary: 报告记录了 origin/workflow/implementation 证据，也记录了 Reddit 与 AICritique 等受阻来源。

## References

### [R1] 本地 claim records
    target: data/manifests/claims.jsonl
    target_version: source_snapshot_2026-05-21
    pinned_version: data/manifests/claims.jsonl
    citation_role: claim_manifest
    why_cited: 该 manifest 提供采集阶段生成的 source-linked claim records。
    evidence_summary: 记录包含 claim、coverage area、confidence 和 supporting sources，是从 raw data 进入 KB 的中间证据层。

### [R2] Runtime implementation evidence
    target: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    target_version: source_snapshot_2026-05-21
    pinned_version: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    citation_role: implementation_source
    why_cited: 支持 LLM Wiki runtime 可以暴露 raw/wiki/schema workflow、lint、gap mapping 与 MCP/CLI 接口。
    evidence_summary: 页面描述了 runtime、raw asset、wiki output、manifest、compile readiness、lint 和 gap mapping。
    source_path: data/raw/webpage/clawhub-llm-wiki-karpathy
