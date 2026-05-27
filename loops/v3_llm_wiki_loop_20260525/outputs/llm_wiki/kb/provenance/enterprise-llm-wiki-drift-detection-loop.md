---
schema: accepted_card_provenance.v3
card: ../cards/enterprise-llm-wiki-drift-detection-loop.md
material_id: falconer-enterprise-guide
digest_id: digest_falconer-enterprise-guide
source_paths:
  - data/raw/webpage/falconer-enterprise-guide/text.txt
draft_card: ../../drafts/cards/enterprise-llm-wiki-drift-detection-loop.md
draft_provenance: ../../drafts/provenance/enterprise-llm-wiki-drift-detection-loop.md
similarity_result: ../../drafts/similarity/enterprise-llm-wiki-drift-detection-loop.json
comparison_provenance: ../../drafts/comparison/enterprise-llm-wiki-drift-detection-loop.md
gate:
  type: fusion_audit
  result: passed
  decided_at: 2026-05-27T14:34:00+08:00
  gate_notes: 四项判据全部通过；真实 v2 anchor 为 `llm-wiki-health-checks`（comparison 明示 top1/top2 为 token 误中，top3 health-checks 为真语义匹配）；draft 提供企业级扩展性证据，与 v2 个人 on-demand scope 形成对偶。
v2_anchor:
  card_id: llm-wiki-health-checks
  card_path: loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-health-checks.md
  comparison_decision: provenance_delta
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-27T14:34:00+08:00
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

- 类型：fusion_audit
- 结果：passed
- 决定时间：2026-05-27T14:34:00+08:00
- 检查要点：
  - 三问被实质回答：comparison 明示 top1/top2（three-layer / schema-config）为 token 误中，真候选是 top3 `llm-wiki-health-checks`；draft 把 Karpathy 个人 on-demand health check 作为对照基线，提出企业级必须升级为连续 drift detection。
  - v2 anchor body 已读：v2 health-checks 卡 scope 明确「仅限被引用推文如何描述 health checks 用途，不外推为通用最佳实践」；与 draft 的企业级扩展无冲突。
  - draft 不破坏 v2 scope：draft 全新机制（continuous drift detection / ownership routing / SSOT designations / 副产品式图谱增长 / agent 是消费者）均在 v2 紧致 scope 之外，且提供「为何个人版不可直接放大」的反例 + 「企业版需要什么改造」的扩展。
  - provenance 链可追溯：本文件显式记录 v2_anchor（health-checks）+ comparison_provenance 路径。

## 备注

- 与 four-properties 卡有交集（都涉及 stay current）。本卡专注 stay-current 的机制实现，four-properties 卡只点到这条属性的必要性。
- adoption 阶段观察：similarity top-1/2 是 token 误中（仅共享 `llm/wiki/的`），top-3 才是真语义最强候选。这是 jaccard top-k 排序与语义匹配脱节的典型样本，已在 v2_anchor 中以真实候选 health-checks 记录。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/enterprise-llm-wiki-drift-detection-loop.md`
- draft provenance: `../../drafts/provenance/enterprise-llm-wiki-drift-detection-loop.md`
- similarity: `../../drafts/similarity/enterprise-llm-wiki-drift-detection-loop.json`
- comparison provenance: `../../drafts/comparison/enterprise-llm-wiki-drift-detection-loop.md`
