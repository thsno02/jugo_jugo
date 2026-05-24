# Enterprise-scale LLM Wiki 需要 governed context layer

动态检索 run 保存了一个 enterprise/RAG comparison 来源，因为原有本地 corpus 中 enterprise article 被公司网络拦截，形成了 evidence gap。新来源认为，LLM Wiki 与 RAG 回答的是相关但尺度不同的知识访问问题：wiki-style approach 更适合 bounded、stable、personal-scale corpus；enterprise 场景则会引入 scale、access control、freshness 和 concurrency 问题，不能靠放大 markdown folder 自行解决。[^1]

对这个 KB 来说，可采纳的 claim 比来源中的产品叙事更窄：enterprise-scale LLM Wiki use 不应被理解为“把个人 wiki 做大一点”。它需要 governed context layer 或等价控制机制，才能让 source-backed synthesis 在多用户、多系统环境中保持可信。[^2]

这也符合本地 KB 规则：新 evidence 必须先保存为 data，并写入 provenance，才能支撑 adopted synthesis。[^3]

## Footnotes

[^1]:
    target: data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt
    target_version: source_snapshot_2026-05-24_dynamic
    pinned_version: data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt
    citation_role: dynamic_retrieval_support
    why_cited: 该动态检索来源直接讨论 enterprise 场景下 LLM Wiki 与 RAG 的 scale、governance、access control 和 freshness 问题。
    evidence_summary: 来源认为 LLM Wiki 适合 bounded personal-scale corpus，而 enterprise 使用需要治理、访问控制、freshness 与并发控制。
    source_path: data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524

[^2]:
    target: kb/20260524_050031_llm_wiki_working_definition.md
    target_version: 1.0
    pinned_version: nodes/20260524_050031_llm_wiki_working_definition/versions/1.0/card.md
    citation_role: background_definition
    why_cited: 提供 LLM Wiki 作为 source-backed maintained wiki artifact 的 adopted definition。
    evidence_summary: 被引 node 区分 preserved raw sources、maintained wiki artifacts 和 control rules。

[^3]:
    target: kb/20260524_050036_dynamic_retrieval_as_controlled_fallback.md
    target_version: 1.0
    pinned_version: nodes/20260524_050036_dynamic_retrieval_as_controlled_fallback/versions/1.0/card.md
    citation_role: process_support
    why_cited: 说明动态检索为什么必须 request、preserve、enter manifest 并写入 provenance。
    evidence_summary: 被引 node 说明 retrieval 不能作为没有 audit trail 的临时补料。

## References

### [R1] Retrieval log
    target: .llmwiki/control/retrieval_log.yaml
    target_version: retrieval_log_2026-05-24
    pinned_version: .llmwiki/control/retrieval_log.yaml
    citation_role: process_artifact
    why_cited: 记录 AICritique 失败尝试和 Atlan 成功检索。
    evidence_summary: log 显示同一个 enterprise evidence-gap request 下有一个 intercepted source 和一个 preserved ok source。

### [R2] Source preservation node
    target: kb/20260524_050033_source_preservation_precondition_trust.md
    target_version: 1.0
    pinned_version: nodes/20260524_050033_source_preservation_precondition_trust/versions/1.0/card.md
    citation_role: audit_background
    why_cited: 解释为什么 synthesized claim 必须能回到保存的本地 source material。
    evidence_summary: 被引 node 把 source preservation 视为后续 inspection 与 trust 的前提。
