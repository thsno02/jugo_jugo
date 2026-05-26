---
schema: comparison_provenance.v3
draft_card: ../cards/enterprise-llm-wiki-four-properties.md
draft_provenance: ../provenance/enterprise-llm-wiki-four-properties.md
similarity_result: ../similarity/enterprise-llm-wiki-four-properties.json
existing_cards:
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1333
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.1333
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.1333
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选的 jaccard 完全相同（0.1333），共享 token 仅 `llm`、`wiki`。draft 标题包含 `capture / link / compound / stay current / 企业级 / 四性` 等区分性 token，但都没有进入候选共享集。换言之：候选只是因为标题里有 "LLM Wiki" 而被机械召回。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-health-checks`：仅记录 LLM 在 wiki 上做 health checks（Linting）这一事实。属"维护手段之一"的最小事实，无法覆盖 draft 中"必要属性框架"。
- 候选 #2 `llm-wiki-listed-use-cases`：use case 列表（personal / research / business 等），不是分析框架。
- 候选 #3 `llm-wiki-pattern-file`：把 "LLM Wiki" 定义成 pattern idea file 的元事实卡。
- draft 来源是 Falconer 企业指南，提出"capture / link / compound / stay current"四属性作为分析任何企业 KB 是否会复利的**判别框架**，并量化"stay current 缺位"的成本（Stack Overflow 2024 调研 60%/68%/73% 数字）。这是 v2 KB 中未涉及的企业落地分析框架。

## 3. 下一步的核心依据

(1) (2) 表明 top 3 候选都是来自 Karpathy 个人 gist 视角的零散小事实卡，没有"分析框架"层级的卡片，更没有企业版讨论。

- 不是 `merge_candidate`：无可合并对象。
- 不是 `provenance_delta`：候选都是单点事实卡，不会被本 draft 的论点反向加挂。
- 不是 `duplicate_skip`：无覆盖。
- 不是 `revise_before_gate`：draft 已有四属性逐项说明、个人/企业断点解释、Stack Overflow 数据引用、边界与反例；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；可与同批次 `enterprise-llm-wiki-tool-native-ingestion` 一并审，二者共享 source（Falconer 指南）与论点轴，互为 related。

## 5. 备注

- 与 `enterprise-llm-wiki-tool-native-ingestion` 互补：一个是"概念框架（为什么这四性都要满足）"，另一个是"capture 实现细则（tool-native ingestion）"。两张都应判 new_card。
- top 3 三张同分（0.1333）也是 v2 池子小 + 高频主题词撞分的典型表现。
