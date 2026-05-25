# Provenance / 溯源记录

node_id:: 20260524_050318_enterprise_scale_requires_governed_context_layer
version:: 1.0

## 为什么存在这个版本

这个版本把动态检索测试从单纯 log event 转化为 adopted KB node。它记录检索到的来源能支持什么、失败来源为什么不能作为 evidence，以及综合结论的边界。

## 使用的输入

### 已有 data

- reports/source_gap_review.md
- .llmwiki/runs/run_20260524_050031_kb_initialization_bootstrap/retrieval_request.md
- .llmwiki/control/retrieval_log.yaml
- nodes/20260524_050031_llm_wiki_working_definition/versions/1.0/card.md
- nodes/20260524_050036_dynamic_retrieval_as_controlled_fallback/versions/1.0/card.md
- nodes/20260524_050033_source_preservation_precondition_trust/versions/1.0/card.md

### 动态检索

- 失败但已保存：data/raw/webpage/aicritique-enterprise-knowledge-dynamic-20260524/
- 使用为 evidence：data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt

### prior KB nodes

- 20260524_050031_llm_wiki_working_definition
- 20260524_050036_dynamic_retrieval_as_controlled_fallback
- 20260524_050033_source_preservation_precondition_trust

### 过程 artifacts

- .llmwiki/runs/run_20260524_050318_dynamic_retrieval_enterprise_scale/run_plan.md
- .llmwiki/runs/run_20260524_050318_dynamic_retrieval_enterprise_scale/data_scope.md
- .llmwiki/runs/run_20260524_050318_dynamic_retrieval_enterprise_scale/audit_report.md

## 生产理由

本 node 不把动态来源中的产品叙事整体采纳为事实，只采纳一个更窄的 process claim：enterprise-scale use 会引入 governance、access-control、freshness 和 concurrency 要求，不能靠放大 personal markdown wiki 自动解决。

## Citation 理由

动态来源用 footnote 支持核心 claim；已有 KB nodes 用来连接 definition、retrieval discipline 和 source-preservation background。

## Synthesis 决策

AICritique 抓取结果是公司网络拦截页，保存但拒绝作为 evidence。Atlan 来源可用于 enterprise framing，但其 vendor-authored 性质在限制中明确记录。

## Audit trail

audit_result:: passed
audit_report:: .llmwiki/runs/run_20260524_050318_dynamic_retrieval_enterprise_scale/audit_report.md

## Adoption 理由

1.0 被 adopted，因为 dynamic source 已保存到 `data/raw/`，manifest 记录了来源，card 有 required citation sections，provenance 区分了 retrieved evidence、失败尝试和 synthesis。

## 限制与不确定性

Atlan 是 vendor-authored source，适合支持 enterprise framing，不适合当作独立 empirical validation 或产品优越性证据。

## 修订触发条件

- 后续个人设备重新 retrieve 到更独立的 enterprise source。
- semantic citation audit 发现 Atlan source 被过度使用。
- 新 evidence 反驳 scale/governance framing。
- dynamic retrieval policy 改变。
