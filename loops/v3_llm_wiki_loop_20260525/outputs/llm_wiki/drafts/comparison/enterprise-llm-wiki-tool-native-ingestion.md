---
schema: comparison_provenance.v3
draft_card: ../cards/enterprise-llm-wiki-tool-native-ingestion.md
draft_provenance: ../provenance/enterprise-llm-wiki-tool-native-ingestion.md
similarity_result: ../similarity/enterprise-llm-wiki-tool-native-ingestion.json
existing_cards:
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1429
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.1429
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.1429
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选的 jaccard 分数完全相同（0.1429），共享 token 都只是 `llm` 与 `wiki` 这两个高频通用词。draft 标题"企业级 LLM Wiki 必须 tool-native 摄取，不能依赖 raw 目录"在 token 集合上只在通用主题词上与候选相交，没有任何关于"ingestion / 企业 / 工具栈"的共享 token。这是典型的 jaccard 误中：所有以 "LLM Wiki" 起头的卡都会和这张 draft 撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-health-checks`：只描述 LLM 对 wiki 做 linting / 寻找不一致 / 寻找新文章候选；它属于 wiki 维护阶段，且仅记录 Karpathy 推文中 `Linting` 段事实。和企业 ingestion 完全不在同一论点轴。
- 候选 #2 `llm-wiki-listed-use-cases`：仅枚举 personal、research、business 等可能用例，是个 use-case 清单。draft 是一个 operational_rule（企业落地约束），论点结构不同。
- 候选 #3 `llm-wiki-pattern-file`：定义 "LLM Wiki" 是一种用 LLM 构建个人知识库的模式 idea file 的元性质描述。这是高层范畴卡，没有触及 capture/ingestion 机制。
- 而 draft 的核心来源是 Falconer 企业指南（`falconer-enterprise-guide/text.txt`）的 L46–L154，论点是"企业里没有 curator/raw 目录，必须 tool-native ingestion 从 GitHub / Slack / Linear / Granola / Google Drive 等持续摄取"。这是 v2 KB 里**未涉及的论点轴**（v2 完全是 Karpathy 个人 gist 视角，无企业落地话题）。

## 3. 下一步的核心依据

由 (1) (2) 得：top 3 与 draft 仅在"LLM Wiki"主题词上相交，但论点轴、来源类型、覆盖维度都不同。draft 引入了 v2 未触及的企业 capture/ingestion 视角，并由具体来源逐条支撑四个规则。

- 不是 `merge_candidate`：没有任何候选写到 capture / ingestion / 工具栈，无可合并对象。
- 不是 `provenance_delta`：v2 没有任何相邻卡可以反向链接这条 provenance；它是新建轴而非补强。
- 不是 `duplicate_skip`：v2 中无重叠主张。
- 不是 `revise_before_gate`：draft 已有清晰 statement、四条规则、边界与反例、显式 quotes 支撑；门控时再决定是否调整即可。
- 因此判定 `new_card`，进入 publication_gate。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate，重点核 Falconer 引文的逐字对齐与企业工具清单的偏置说明是否充分。

## 5. 备注

- jaccard 在 v2 仅 15 张卡的小池子里很容易让任何带 "LLM Wiki" 的 draft 与多张候选撞同分；本卡是该模式的典型案例。
- 与同批次 `enterprise-llm-wiki-four-properties` 互补：那张是"为什么 capture 重要"，本卡是"capture 在企业里怎么实现"。两张卡都应是 new_card。
