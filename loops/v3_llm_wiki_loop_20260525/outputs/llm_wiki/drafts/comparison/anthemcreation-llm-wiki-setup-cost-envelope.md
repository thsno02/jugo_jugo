---
schema: comparison_provenance.v3
draft_card: ../cards/anthemcreation-llm-wiki-setup-cost-envelope.md
draft_provenance: ../provenance/anthemcreation-llm-wiki-setup-cost-envelope.md
similarity_result: ../similarity/anthemcreation-llm-wiki-setup-cost-envelope.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2308
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.2
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1429
decision: new_card
audit_required: false
created_time: 2026-05-26T12:37:00+08:00
edited_time: 2026-05-26T12:37:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 `llm-wiki-three-layer-architecture` 共享 token `llm / wiki / 的`，纯属 token 误中：

- v2 卡片只断言"Karpathy gist 把架构分成三层"这一定义事实。
- 本 draft 是 Anthem Création 法语指南给出的**具体操作流程**：5 步搭建路径 + 工具替换 + 成本表（0 €/月 / 0.01–0.10 € per ingest / <10€ for 100 docs）+ 规模限制。

两者主题完全不同：v2 是架构定义，draft 是 setup + cost envelope。

top 2 / top 3 同样是 token 误中（共享词都是 LLM Wiki 板块常见词）。

## 2. draft 与候选在哪里不同

- **事实类型不同**：v2 三张都是 `known_fact`（定义/描述）；draft 是 `operational_rule`（搭建步骤 + 成本上限 + 风险）。
- **覆盖维度全新**：5 步流程（拷 gist / 建空目录 / Obsidian 打开 / 独立 sources 子目录 / 让 LLM ingest 第一篇）+ 成本表（三档配置的 € 量级）+ 规模限制（10–几百篇）+ 风险（弱 LLM 传染错误 / 无官方实现）—— 都不在 v2 任何卡片中。
- **可操作产物不同**：v2 不能直接被读作"我该怎么开始"；draft 直接给出 5 分钟搭建路径与花费上限。
- **来源不同**：v2 来源是 Karpathy 原始 gist；draft 来源是 Anthem Création 法语指南。

不是 v2 卡片的扩展，是**全新的 operational 类卡**。

## 3. 下一步的核心依据

- 不是 `merge_candidate` / `provenance_delta`：v2 没有任何 setup / cost 内容，找不到合并 / 补强对象。
- 不是 `duplicate_skip`：v2 完全未覆盖搭建路径与成本。
- 不是 `revise_before_gate`：draft 证据扎实（所有数字与限制都直接引法语原文行号）、scope 清晰、边界（弱 LLM 传染错误 / 无官方实现 / 个人量级才优）也标注。

正确决定是 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：走 publication_gate；接受后建议在 audit 阶段与同源的 `anthemcreation-llm-wiki-three-layer-architecture`（what）形成"what + how/cost"组合卡对；与未来若出现的 v2 `llm-knowledge-base-five-stage-workflow` 卡通过 related 链接区分（五阶段 = 抽象 workflow，本卡 = 5 分钟最小搭建）。

## 5. 备注

- draft 提到的 `llm-knowledge-base-five-stage-workflow` 是 v2 已有卡片但未进入本 batch top-3；audit 阶段需要交叉对齐两者的粒度差。
- 这张卡是 batch 中少数带"€ 量级数字"的卡片之一，工程参考价值高，建议优先 publish。
