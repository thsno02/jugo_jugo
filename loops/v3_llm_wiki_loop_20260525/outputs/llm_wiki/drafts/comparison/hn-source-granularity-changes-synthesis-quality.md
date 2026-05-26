---
schema: comparison_provenance.v3
draft_card: ../cards/hn-source-granularity-changes-synthesis-quality.md
draft_provenance: ../provenance/hn-source-granularity-changes-synthesis-quality.md
similarity_result: ../similarity/hn-source-granularity-changes-synthesis-quality.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.2857
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2308
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1429
---

## 1. draft 与候选为什么看起来相关

三张 v2 候选 jaccard 进入 top 3 完全是 token 误中：

- 共享 token 集仅有 `llm / wiki / 是 / 的`——都是 LLM Wiki 主题板块内任何中文标题都会带的常见词。
- v2 候选都属于 `llm-wiki-*` 命名前缀的 Karpathy gist 概念卡，标题里必然含 `LLM Wiki`，与本 draft 标题中的 `LLM Wiki` 重叠。
- 实际语义不重叠：v2 三张候选讲的是 schema 配置文档定义 / 三层架构定义 / health checks 清理用途，**没有一张涉及"源文件粒度对合成质量的影响"**或任何实证 / 数值评测。

## 2. draft 与候选在哪里不同

- **事实类型不同**：v2 三张都是 `known_fact`（直接引用 Karpathy 原文），本 draft 是 `example_pattern`，承担"HN 用户 vbarsoum 的一次个人实验的具体数字 + 操作规则"。
- **来源不同**：v2 候选来源是 Karpathy gist / launch-post tweet；本 draft 来源是 HN 原帖第 521–523 行 `vbarsoum` 的一条评论。
- **覆盖维度全新**：210 concept pages / 4,597 cross-references / 19.2 avg links per page / 跨 11 个源文件的合成 / 12M tokens / 10–15 min / "It's not compression — it's synthesis" —— 这些数字与论断在 v2 任何卡片都不出现。
- **可操作产物不同**：本 draft 提出"源文件粒度是第一超参 + 评测应该看合成数 / 跨文件引用 / 矛盾识别数"——是 actionable 评测规则，v2 三张候选都没有任何评测维度。

不是 v2 卡片的扩展，也不是同视角不同源，是**全新事实卡**。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 候选都没有"源粒度对合成质量影响"的内容，无可合并对象。
- 不是 `provenance_delta`：没有 v2 卡片需要被补强（v2 健康检查 / schema / 三层架构卡都不讨论 ingest 阶段的粒度选择）。
- 不是 `duplicate_skip`：draft 内容在 v2 完全未覆盖。
- 不是 `revise_before_gate`：draft 已显式标注"单个用户报告而非受控实验 / 样本是商业书籍 / 数字未公开复核 / 仓库地址给出"等边界，证据链 + 风险陈述完整。

正确决定是 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：走 publication_gate；接受后建议在 v2 拓扑里挂到"LLM Wiki 实证 / 评测"类目下；与未来若出现的"合成质量评估指标"卡片建立 related。

## 5. 备注

- top 1 `llm-wiki-schema-configuration-document` 与本 draft 主题完全无关，是 jaccard 上限被中文低 IDF token 推高的典型例子；不要因为分数 0.2857 就误判为有重叠。
- 这张卡是当前 batch 唯一带量化数据的 HN 卡，单独保留有评测价值。
