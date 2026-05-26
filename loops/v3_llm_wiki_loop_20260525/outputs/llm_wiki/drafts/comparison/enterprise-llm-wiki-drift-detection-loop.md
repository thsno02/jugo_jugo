---
schema: comparison_provenance.v3
draft_card: ../cards/enterprise-llm-wiki-drift-detection-loop.md
draft_provenance: ../provenance/enterprise-llm-wiki-drift-detection-loop.md
similarity_result: ../similarity/enterprise-llm-wiki-drift-detection-loop.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1765
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.125
decision: provenance_delta
audit_required: true
created_time: 2026-05-26T12:44:00+08:00
edited_time: 2026-05-26T12:44:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 / top 2 共享 token 仅 `llm / wiki / 的`，是 token 误中——v2 的"三层架构"与 schema 配置卡片完全不涉及 drift detection。

top 3 `llm-wiki-health-checks` 虽然 jaccard 最低（0.125），但**才是语义最相关的候选**：

- v2 卡片由 Karpathy launch-post tweet 抽取，statement 是"LLM 可以对 wiki 运行 health checks，用于发现不一致 / 补全缺失 / 找新文章候选连接，逐步清理 wiki"。
- 本 draft 由 Falconer 企业级指南抽取，主题是"Karpathy 个人 LLM Wiki 的 health check 是 on-demand 的，但在企业里必须改成连续后台 drift detection + 按 owner 路由 + SSOT 锚点"。

draft 明确把 Karpathy 的"个人 on-demand 健康检查"作为基线，提出"企业级必须升级为连续 drift detection 循环"——这是同一机制范畴（LLM-based wiki maintenance）的扩展性主张。

## 2. draft 与候选在哪里不同

- **来源不同**：v2 来源 Karpathy launch-post tweet `$.tweet.quote.text` Linting 段；draft 来源 Falconer 企业级指南。
- **覆盖维度全新**：v2 卡片只覆盖"health checks 做什么"（发现不一致 / 补全缺失 / 找新连接）；draft 覆盖 (a) on-demand 在企业失败的三个原因（写 runbook 的人已离开 / 不一致安静累积 / agent 把陈旧 runbook 当输入）、(b) 连续 drift detection 取代手动触发、(c) 按 ownership 路由更新草稿（不只是 alert）、(d) SSOT 指定作为 system property 显式登记、(e) "图谱增长作为副产品"的 compounding 机制、(f) AI agent 作为消费者（through Claude MCP）。
- **scope 不同**：v2 scope 仅限"被引用推文如何描述 health checks 用途"，明示不外推为通用最佳实践；draft scope 是"企业级 LLM Wiki 必须的 stay-current 机制"。
- 不是 v2 卡片的扩展，也不是同源同事实——是**同概念（LLM-based wiki maintenance），新源（企业级实践），新机制（连续 + 路由 + SSOT）**。

## 3. 下一步的核心依据

这是 `new_card` vs `provenance_delta` 的边界判断：

- 倾向 `new_card`：draft 是关于"企业级 drift detection 机制"的独立事实卡，机制具体到 SSOT / ownership routing / draft-not-alert 等，v2 health-checks 卡完全没有这些。
- 倾向 `provenance_delta`：draft 在论证开头就明确把 Karpathy on-demand health check 作为对照基线，从机制本质上是同一谱系（LLM 对 wiki 做检查与清理）。Falconer 文章是对 v2 health-checks 概念的"企业级扩展性背书 + 不可直接放大的反证"，应该反向链接进 v2 卡的 provenance。

最终选 `provenance_delta`：v2 health-checks 卡当前 scope 明确"不外推为通用最佳实践"，draft 正好提供了"为什么个人版不可直接放大到企业 + 企业版需要什么改造"的扩展性证据。这条证据写入 v2 provenance 后，能让 v2 卡的 scope 边界更有据可循（"以 Karpathy on-demand 个人版为限"vs"企业级见 Falconer 扩展"）。同时 audit 应判断是否把 draft 独立为 `enterprise-` 前缀的独立机制卡（与 v2 health-checks 形成"个人 vs 企业"对偶卡组）。

## 4. 决策

- decision: provenance_delta
- audit_required: true
- 后续动作建议：fusion_audit 把 Falconer "Stay current"段的核心论点（个人 on-demand 在企业失败的三原因 + 连续 drift detection + ownership routing + SSOT）作为 v2 `llm-wiki-health-checks` 卡 provenance 的扩展性证据补充；audit 判断是否同时保留 draft 为独立 `enterprise-` 前缀机制卡，与 v2 health-checks 互链。

## 5. 备注

- 这是 batch 中 top-3 score 最低但语义最强的"边界情况"——top 3 才是真候选，top 1/2 是误中。提醒下次评审时不能只看 top 1。
- 如果 audit 决定保留 draft 为独立卡（推荐），则在 v2 health-checks 卡 Note 段加一句"个人版以 on-demand 为主；企业级需扩展为连续 drift detection（见 `enterprise-llm-wiki-drift-detection-loop`）"，让两张卡形成显式对偶。
