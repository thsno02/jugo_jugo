# Source preservation 需要 provenance 才能支撑 KB 信任

这个 candidate 修改了 1.0 的 support contract：保存 source files 对 KB trust 是必要条件，但单独保存 source files 还不充分。后续 auditor 还需要 provenance 来解释 source 为什么被使用、synthesis 如何产生、哪些材料被拒绝，以及什么时候应该修订 node。[^1]

因为这个变化把 node 从“source preservation 是前提”改成“source preservation 加 provenance 才构成 support contract”，所有引用 1.0 framing 的下游 nodes 都需要 review，才能决定这个 candidate 是否可 adopted。[^2]

## Footnotes

[^1]:
    target: kb/20260524_050034_provenance_as_core_knowledge_asset.md
    target_version: 1.0
    pinned_version: nodes/20260524_050034_provenance_as_core_knowledge_asset/versions/1.0/card.md
    citation_role: claim_support
    why_cited: 支持 provenance 是可复用知识对象的一部分，而不是附录。
    evidence_summary: 被引 node 说明 provenance 记录 inputs、synthesis、citation rationale、audit、adoption、limits 和 revision triggers。

[^2]:
    target: kb/20260524_050035_citation_driven_impact_propagation.md
    target_version: 1.0
    pinned_version: nodes/20260524_050035_citation_driven_impact_propagation/versions/1.0/card.md
    citation_role: impact_rule
    why_cited: 解释为什么 major support-contract change 应该创建 impact review tasks，而不是自动重写下游 nodes。
    evidence_summary: 被引 node 说明 citation edges 在 major changes 后驱动 impact review。

## References

### [R1] 工作定义
    target: kb/20260524_050031_llm_wiki_working_definition.md
    target_version: 1.0
    pinned_version: nodes/20260524_050031_llm_wiki_working_definition/versions/1.0/card.md
    citation_role: background_definition
    why_cited: 提供本 candidate 所修订的 source-backed maintained-wiki 语境。
    evidence_summary: 被引 node 定义 preserved raw sources、maintained wiki artifacts 和 control rules。
