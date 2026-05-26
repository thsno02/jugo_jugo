---
schema: comparison_provenance.v3
draft_card: ../cards/knowledge-compounding-three-mechanisms.md
draft_provenance: ../provenance/knowledge-compounding-three-mechanisms.md
similarity_result: ../similarity/knowledge-compounding-three-mechanisms.json
existing_cards:
  - card_id: llm-wiki-ingest-example-flow
    card_path: llm_wiki/kb/cards/llm-wiki-ingest-example-flow.md
    score: 0.0667
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0625
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 给出的 token 共享面非常窄。Top 1 `llm-wiki-ingest-example-flow` 唯一共享 token 是 `ingest`——draft 标题里出现"INGEST 摊销"，恰好与 v2 卡里 Karpathy gist 描述的"ingest 操作"用了同一个词。Top 2 / Top 3 的共享 token 仅是中文虚词 `的`，属于 jieba 切分的副产品，不构成主题邻近。两者都未到 0.07，远低于经验性"需要 careful 判断"的 0.30 阈值。

## 2. draft 与候选在哪里不同

draft 来自 Wen 与 Ku（2026）的一篇 arxiv 论文，把"知识复利"形式化为三条独立微观机制：(i) one-time INGEST amortized over N retrievals、(ii) auto-feedback of high-value answers into synthesis pages、(iii) write-back of external search results into entity pages，并附 ~200 行 C# reference implementation。讨论对象是**经济学意义上的成本摊销模型**、可消融的工程机制，以及 wiki 可寻址性失效时复利失效的边界。

Top 1 `llm-wiki-ingest-example-flow` 只是把 Karpathy gist 的 Operations / Ingest 小节复述为"读取来源 → 讨论 → 写摘要页 → 更新 index → 写 log"的示例流程。它既不讨论 N 次检索的成本摊销，也没有 (ii)(iii) 这两条机制。Top 2 / Top 3 完全是另外的主题（idea file 的抽象性、三层架构整体定义），与"复利机制"无任何论点轴重叠。

draft 的 provenance 注明 (ii) 机制与 v2 卡 `file-outputs-back-as-compounding-loop` 主题相关——但这张 v2 卡并未进入 top 3，说明 jaccard token 共享在该方向并未生效。

## 3. 下一步的核心依据

(1) 表明 top 1 共享只在 `ingest` 一词；(2) 表明 draft 的核心论点（三机制 / 成本公式 / C# 参考实现）在 v2 中无对应。这既不是同主题不同视角（v2 没有任何"复利成本"的论点），也不是"扩展 v2 卡"——它是一篇外部论文对 Karpathy paradigm 提出的新形式化。draft 本身已经写得很完整（机制、操作含义、边界齐备），不需要 revise_before_gate。结论是 `new_card`。

不选 `provenance_delta`：draft 没有对任何 v2 卡 body 补充新证据，三机制是平行结构，不是 v2 任一卡的增量。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进 publication_gate；若 v2 后续接纳 `file-outputs-back-as-compounding-loop` 这张卡，可在那一轮将本 draft 作为 (ii) 机制的扩展互相 cite。

## 5. 备注

`ingest` 在 v2 与 draft 中是同名异指：v2 指 Karpathy gist 的示例操作，draft 指论文形式化的"一次性写入 → N 次检索摊销"机制。命名相近但论点轴不同。
