---
schema: comparison_provenance.v3
draft_card: ../cards/auto-index-replaces-rag-at-small-scale.md
draft_provenance: ../provenance/auto-index-replaces-rag-at-small-scale.md
similarity_result: ../similarity/auto-index-replaces-rag-at-small-scale.json
existing_cards:
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.1818
  - card_id: llm-wiki-wiki-layer-generated-markdown-directory
    card_path: llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md
    score: 0.1429
  - card_id: llm-wiki-persistent-compounding-artifact
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md
    score: 0.0909
decision: new_card
audit_required: false
created_time: 2026-05-26T12:14:00+08:00
edited_time: 2026-05-26T12:14:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top1 `llm-wiki-persistent-wiki-alternative-mode` 与 draft 共享 `wiki`、`替代` 两个 token——这是真主题邻近：两者都谈"LLM Wiki 作为 RAG 替代"的同一议题。top2 共享 `wiki`、`维护`（"自维护索引" vs "LLM 生成和维护"），也是主题邻近。top3 只共享 `wiki`，邻近性弱。整体属于"同主题不同切片"。

## 2. draft 与候选在哪里不同

- **来源不同**：本 draft 取自 `karpathy-x-launch-post` 推文 Q&A 章节；v2 top1 取自 `karpathy-gist-llm-wiki` 行 11–13。两者同属 karpathy 但是不同载体、不同段落。
- **论点轴不同**：
  - v2 top1（"持久 wiki 替代模式"）谈**整合 / 持久化**机制：wiki 位于用户与原始来源之间，新增 source 时 LLM 读取并整合进既有 wiki。论点轴是"如何写"。
  - 本 draft 谈**检索 / 问答** 机制：在 ~100 篇 / ~400K 词规模下，索引 + 摘要替代向量 RAG；并给出阈值（"索引塞不进 context"或"系统性漏读"时再上 RAG）。论点轴是"如何读"。
- v2 top2（"Wiki 层由 LLM 生成和维护"）谈写者归属（LLM 负责生成）；本 draft 借同一作者群体描述检索方法，与"谁来写"无关。
- v2 top3（"持久复合 wiki"）谈"知识积累/复利"价值；本 draft 谈具体规模区间下的检索机制选择。

特别注意：本 draft 显式锁定规模锚（"~100 articles, ~400K words"）和触发上 RAG 的两个条件（context 装不下、系统性漏读），这是 v2 三张候选都没有的可量化操作边界。

## 3. 下一步的核心依据

(1) 三张候选都属"LLM Wiki 是 RAG 替代"的主题家族，但都在写/整合或概念定位上谈，没有任何一张给出检索机制 + 规模阈值；(2) 本 draft 提供 v2 完全没有的 Q&A 阶段 operational_rule，并带"何时该切换到 RAG"的可执行触发条件；(3) draft 来源是 v2 KB 之外的另一个 karpathy 载体（推文 Q&A），不能被并入 v2 任一卡。结论是 `new_card`。

不是 `provenance_delta`：尽管与 v2 top1 同主题（RAG 替代），本 draft 不是给 v2 top1 补一行证据——它是一个独立的 operational rule（检索机制 + 阈值），从论点轴到 fact_type 都不同。v2 top1 的 statement 是"模式存在"（known_fact），本 draft 是"在某规模下用索引而不是向量"（operational_rule）。两者并列、互相 cross-link 是正确做法，合并会损失抽象层。

不是 `merge_candidate`：v2 没有任何 operational_rule 类卡可合并；也不应把"模式存在"的 known_fact 与"具体规模下的操作选择"的 operational_rule 合在一张卡里。

不是 `revise_before_gate`：draft 已锁定规模、阈值、边界声明（"不是说 RAG 整体不必要"），证据完整。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 v2 `llm-wiki-persistent-wiki-alternative-mode` 做 related 双向 cross-link（"模式存在" ↔ "在 ~100 篇规模下的具体操作"）；与同批 `llm-knowledge-base-five-stage-workflow` 互链作"Q&A 阶段细节"链路。

## 5. 备注

- v2 top1 的 statement 偏抽象，本 draft 可视为该模式在 Q&A 阶段的可量化补充。如果未来 v2 卡愿意接受 cross-link，可在 v2 卡 provenance 加一行"v3 draft `auto-index-replaces-rag-at-small-scale` 提供 ~100 articles / ~400K words 规模锚"。但这属于 v2 reflection 范畴，不作为 provenance_delta 触发。
- "系统性漏读"作为切到 RAG 的触发条件是 draft 的合理引申，原文未直说；如审稿严格可保留为操作建议。
