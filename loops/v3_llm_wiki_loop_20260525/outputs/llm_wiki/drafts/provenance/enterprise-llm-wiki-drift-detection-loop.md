---
schema: draft_card_provenance.v3
draft_card: ../cards/enterprise-llm-wiki-drift-detection-loop.md
material_id: falconer-enterprise-guide
digest_id: digest_falconer-enterprise-guide
source_paths:
  - data/raw/webpage/falconer-enterprise-guide/text.txt
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-26T11:50:00+08:00
edited_entity: llm
---

## 源证据

- L68-74："Stay current" 段，企业级 health check 失败模式。
- L82-86：连续 drift detection + 按 owner 路由更新草稿。
- L112-118：SSOT 指定 + Step 4 ship normally 副产品式图谱增长。
- L120-122 + L150：AI agent 作为消费者通过 Claude MCP 查询同一图谱。
- L74：Anthropic 把 context 定义为 agent 最稀缺资源。

## 卡片范围是否成立

卡片范围聚焦"drift detection 必须连续 + 必须路由 + 必须有 SSOT 锚点"。每条机制都来自原文：

- "草稿而非告警" → L84 直接说明 "draft an update, and route it to the document owner"。
- "system property"形式登记 SSOT → L116 "the system monitors it from that point forward and treats conflicting sources as supplementary context"。
- "agent 是消费者而不只是工具" → L122。

操作含义里的 "review cadence 应该匹配组织变更率" 是合理引申，源材料举的例子是"weekly review rather than quarterly audit"。

边界（自动起草 ≠ 自动 merge / SSOT 治理动作 / 实体解析上限）是明确限定：原文未给具体治理模型，本卡明确指出这是局限。

## 发表门控结果

本轮未运行。

## 备注

- 与 four-properties 卡有交集（都涉及 stay current）。本卡专注 stay-current 的机制实现，four-properties 卡只点到这条属性的必要性。
