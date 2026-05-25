# Citation edges 在 major change 后驱动 impact review

这个 demo 把 citation 当作 dependency information 的来源。A footnote from node A to node B 表示 A 对某个 claim 强依赖 B；reference 表示较弱的背景依赖；plain link 默认不传播。[^1]

当 node B 出现 major version candidate，系统可以解析 citation edges，把 citing nodes 放入 impact queue，而不是手动维护 `depends_on` 字段。[^2]

这个设计是保守的：impact analysis 只创建 review tasks，不自动重写下游 nodes。这样可以把 semantic revision 和 graph computation 分开。[^3]

## Footnotes

[^1]:
    target: loop_plan_init_kb.md
    target_version: plan_snapshot_2026-05-24
    pinned_version: loop_plan_init_kb.md
    citation_role: process_contract
    why_cited: 该文件定义了本 demo 的初始化 loop、version bundle、provenance、citation、adoption 与 impact 规则。
    evidence_summary: 计划明确要求 nodes 是版本化知识对象库，kb/ 是 adopted view，citation 驱动 impact，动态检索必须受控并沉淀为 data asset。

[^2]:
    target: kb/20260524_050034_provenance_as_core_knowledge_asset.md
    target_version: 1.0
    pinned_version: nodes/20260524_050034_provenance_as_core_knowledge_asset/versions/1.0/card.md
    citation_role: claim_support
    why_cited: 解释 citations 与 provenance 为什么必须保留 support boundary。
    evidence_summary: 被引 node 把 provenance 和 citation rationale 视为可复用 audit surface。

[^3]:
    target: data/raw/arxiv/arxiv-alce/text.txt
    target_version: source_snapshot_2026-05-21
    pinned_version: data/raw/arxiv/arxiv-alce/text.txt
    citation_role: research_context
    why_cited: 支持 citation 不能只看形式存在，还需要评价 citation quality 与 verifiability。
    evidence_summary: ALCE 摘要把 citation 作为提升事实正确性和可验证性的机制，并提出自动评价 citation quality。
    source_path: data/raw/arxiv/arxiv-alce

## References

### [R1] Source preservation node
    target: kb/20260524_050033_source_preservation_precondition_trust.md
    target_version: 1.0
    pinned_version: nodes/20260524_050033_source_preservation_precondition_trust/versions/1.0/card.md
    citation_role: background_support
    why_cited: 提供 citation audit 可行所需的 source-preservation 前提。
    evidence_summary: 被引 node 说明 support 必须可追溯到 preserved source records。

### [R2] Claim manifest
    target: data/manifests/claims.jsonl
    target_version: source_snapshot_2026-05-21
    pinned_version: data/manifests/claims.jsonl
    citation_role: claim_manifest
    why_cited: 该 manifest 提供采集阶段生成的 source-linked claim records。
    evidence_summary: 记录包含 claim、coverage area、confidence 和 supporting sources，是从 raw data 进入 KB 的中间证据层。
