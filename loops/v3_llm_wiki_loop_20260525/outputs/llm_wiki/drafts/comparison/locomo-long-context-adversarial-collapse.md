---
schema: comparison_provenance.v3
draft_card: ../cards/locomo-long-context-adversarial-collapse.md
draft_provenance: ../provenance/locomo-long-context-adversarial-collapse.md
similarity_result: ../similarity/locomo-long-context-adversarial-collapse.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1364
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0952
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0476
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

共享 token 只有 `llm`、`是`、`的` 这些高频通用词；draft 的核心术语 `LoCoMo`、`adversarial`、`长上下文` 全部未出现在任何候选标题。这是典型的"v2 单词撞 draft 标题里的散字"现象。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-schema-configuration-document`：Karpathy gist 第 33 行对 schema 层的事实描述。和长上下文 hallucination 评测完全无关。
- 候选 #2 `llm-wiki-three-layer-architecture`：Karpathy gist 的架构三层。同样无关。
- 候选 #3 `idea-file-abstract-vague`：仅是 idea file 抽象性的事实记录。无关。
- draft 来自 `arxiv-locomo`，是一个针对 GPT-3.5-turbo-16K 等模型在 adversarial / single-hop / multi-hop 等任务上的实证 F1 表格，主张"长上下文 LLM 在 adversarial 上崩到 2.1%"这一论文结论。所属论点轴是 long-context 评测，v2 完全没有此类 benchmark 卡。

## 3. 下一步的核心依据

(1) (2) 表明 top 3 候选与 draft 没有任何论点对接面。

- 不是 `merge_candidate`：无候选承担"长上下文崩塌"主题。
- 不是 `provenance_delta`：top 3 候选都是 gist 的元事实卡，本 draft 的数字无法反向链接。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有完整 QA 表 + 论文行号 + 边界（模型版本免责）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；门控阶段建议核对 Table `tab:qa_results` 与 draft 中表数字是否逐字对齐（尤其 GPT-3.5-turbo 4K 的 Adversarial 12.8 vs 论文 intro 里引用的 13.1 这种小差异）。

## 5. 备注

- jaccard 0.1364 完全由"llm/是/的"产生，不反映任何内容关系；这是 v2 候选池仅 15 张时常见误中。
- draft 自身已经在 related 列出 `locomo-three-task-evaluation-framework`、`locomo-observation-rag-beats-summary-rag` 两张同源姊妹卡，体现"分析维度独立成卡"的合理拆分。
