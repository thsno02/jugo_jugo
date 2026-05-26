---
schema: comparison_provenance.v3
draft_card: ../cards/locomo-event-summarization-five-error-types.md
draft_provenance: ../provenance/locomo-event-summarization-five-error-types.md
similarity_result: ../similarity/locomo-event-summarization-five-error-types.json
existing_cards:
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.1053
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.0526
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0526
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- 候选 #1 `llm-wiki-pattern-file`：共享 `llm`、`模式`。draft 标题里"失败模式"撞 v2 "模式文件"。机械撞分。
- 候选 #2 `llm-wiki-human-llm-role-division`：共享 `llm`。极弱撞分。
- 候选 #3 `llm-wiki-persistent-wiki-alternative-mode`：共享 `模式`。极弱撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-pattern-file`：仅记录 Karpathy gist 把 "LLM Wiki" 定位成一种 pattern idea file 的元事实。和 LoCoMo 错误分类无关。
- 候选 #2、#3：v2 中关于 wiki 模式的其它小事实卡，与"事件摘要错误五类"完全不相关。
- draft 来源是 `arxiv-locomo` §6.2 + Appendix D.1 (行 493 / 行 754–774)，论点是 LoCoMo 把 LLM 事件摘要错误分成 5 类 (missing info / hallucination / dialog-cue / speaker-attribution / saliency)，每类带 GPT-3.5-turbo 真实例子并配以修复方向。v2 KB 完全无 LoCoMo 或评测错误分类卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无错误分类或 evaluation taxonomy 系列卡。
- 不是 `provenance_delta`：候选都是 wiki pattern / role / mode 概念卡，与 LoCoMo 错误分类无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有五类完整定义、tab:summary_errors 表对应例子、与 long-context 现象互证、边界标注（GPT-3.5 specific / saliency 主观性）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 tab:summary_errors 5 行例子的英文原文是否逐字对齐。

## 5. 备注

- 与同源 `locomo-three-task-evaluation-framework`、`locomo-long-context-adversarial-collapse` 构成 LoCoMo 三联视图（评测框架 + 长上下文崩塌 + 错误分类）。
- 候选 #1 是本批 LOW 中"模式"撞分的常见 v2 卡。
