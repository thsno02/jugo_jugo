---
schema: comparison_provenance.v3
draft_card: ../cards/memory-as-metabolism-five-operations.md
draft_provenance: ../provenance/memory-as-metabolism-five-operations.md
similarity_result: ../similarity/memory-as-metabolism-five-operations.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1429
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0714
  - card_id: llm-wiki-query-answer-writeback
    card_path: llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md
    score: 0.0667
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 仅共享 `架构`、`的` 两个通用词（draft 标题里的"五操作架构"匹配 v2 "三层架构"）。top 2 共享 `的`、top 3 共享 `操作`。这种 token 重叠是机械的——draft 标题里 `TRIAGE / CONTEXTUALIZE / DECAY / CONSOLIDATE / AUDIT` 这些核心术语完全没有出现在任何候选标题里。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-three-layer-architecture`：Karpathy gist 提的"raw sources / wiki / schema"三个**静态层级**。draft 描述的是 Miteski 2026 论文的**五个治理操作**（治理算子，按运行节奏区分流式/批量/慢周期），论点对象是 sleep-function 架构与 vitality 公式，与"层级"无关。
- 候选 #2 `idea-file-abstract-vague`：仅描述 idea file 的抽象性立场。和 memory governance / consolidation 完全无关。
- 候选 #3 `llm-wiki-query-answer-writeback`：Karpathy gist 中 query 操作回写好答案这一事实，是"读操作的副产品写回"；和 draft 的 CONSOLIDATE / AUDIT 算子无关。
- draft 的来源是 arxiv 论文 `arxiv-memory-as-metabolism`（§5.0 / §5.5 / §5.8 / §7.5 conformance），完全在 v2 KB 未触及的领域：companion 记忆的批量/慢周期治理机制、vitality 公式、self-sealing 反例。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 memory governance 系列卡。
- 不是 `provenance_delta`：v2 候选无可被反向加挂的论点轴。
- 不是 `duplicate_skip`：无任何覆盖。
- 不是 `revise_before_gate`：draft 已有结构化的 5 操作 + vitality 公式 + 边界 + 引用页码（§5.0 表、§5.1 引文、§5.8 AUDIT 伪代码、§7.5 MUST/MUST NOT），门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；门控时可考虑五操作合卡是否在 v3 schema 下过长，必要时按"raw buffer 阶段 / DECAY+vitality / CONSOLIDATE 四 phase / AUDIT 慢周期"拆开。

## 5. 备注

- jaccard 在 v2 仅 15 张卡的窗口下，任何带"架构"或"操作"两字的中文 draft 都会被低分撞上"LLM Wiki 三层架构"或"Query 操作回写好答案"。本卡是典型的"v2 同名词撞分但内容无关"。
- draft 自身 provenance 提到"与 v2 现有 llm-knowledge-base-five-stage-workflow 有概念上的重叠"——但该 v2 卡未在本次 top 3，无法判断；从层级（interaction 层 vs retention 层）上看，互不冲突。
