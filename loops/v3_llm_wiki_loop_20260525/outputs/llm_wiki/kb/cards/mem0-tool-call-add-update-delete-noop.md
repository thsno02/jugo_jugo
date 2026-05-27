---
id: mem0-tool-call-add-update-delete-noop
title: Mem0 的 ADD/UPDATE/DELETE/NOOP：让 LLM 自己决定记忆该怎么改
status: accepted
card_type: mechanism
tags: [#memory, #mem0, #tool-call, #update-operations]
created_time: 2026-05-26T11:35:00+08:00
edited_time: 2026-05-27T12:01:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
provenance_card: ../provenance/mem0-tool-call-add-update-delete-noop.md
aliases: [Mem0 update operations, ClassifyOperation, tool-call routing]
related: [mem0-extract-update-pipeline, mem0-graph-memory-variant, mem0-answer-generation-prompt-design, memory-as-metabolism-five-operations, lightmem-sleep-time-offline-parallel-update, zep-bi-temporal-edges]
---

## 把 update 决策当成语义任务

Mem0 的 update 阶段不引入独立分类器，而是通过 LLM function calling（论文称为 "tool call"）让模型在四种操作之间做选择。对每个抽取出来的候选事实 $\omega_i$ + 它的 top-$s$（实验 $s=10$）语义相似记忆：

| 操作 | 触发条件（Algorithm 1 中的 ClassifyOperation） | 副作用 |
| --- | --- | --- |
| **ADD** | $\omega_i$ 与 $M$ 语义不相似 → 新信息 | 生成新 ID，加入 $M$，操作类型记为 "ADD" |
| **UPDATE** | $\omega_i$ 增益（Augments）已有记忆 $m_i$ | 若 $\omega_i$ 的 InformationContent 更大，替换 $m_i$，保留原 ID，操作类型记为 "UPDATE" |
| **DELETE** | $\omega_i$ 与 $m_i$ 矛盾（Contradicts） | 从 $M$ 中移除 $m_i$ |
| **NOOP** | 事实已存在或与现有记忆无关 | 无变化 |

## ClassifyOperation 的判断顺序

伪代码（appendix Algorithm 1）按以下优先级走：

1. 先判 $f$ 是否与 $M$ **语义不相似** → 若是，ADD（新信息）；
2. 否则判**矛盾** → 若是，DELETE（让位给新信息，因为对话向前推进时旧事实可能失效）；
3. 否则判**增益** → 若是，UPDATE（把已有事实变得更丰富，但只在 InformationContent 增加时才写入）；
4. 否则 NOOP。

注意 UPDATE 是**有信息量门槛的**：仅当新事实的信息内容大于旧的才替换——避免"为新而新"的语义抖动。

## 与传统 CRUD 的差别

- 没有时间戳级的硬版本：DELETE 不保留旧条目，论文也没引入 archive 状态——这与 `arxiv-memory-as-metabolism` 中"never hard-delete, terminal states are archived/expired"的 governance 立场对比鲜明。
- 没有 minority retention：与新事实矛盾的旧条目**直接删除**，不进入隔离 cluster 等待 buffer 压力翻盘。
- ADD/UPDATE/DELETE 选择**完全由 LLM 推理**而非规则——好处是无需手工标签数据训练分类器；代价是 LLM 推理稳定性与提示设计成为性能下限。

## 系统副作用

- 写完之后向量库重建对应嵌入；
- 操作类型（"ADD"/"UPDATE"）作为元数据写回，供下次 ClassifyOperation 参考；
- 论文未公布 NOOP 比率，因此"语义抖动率"在论文中不可直接量化。

## 使用边界

- 这是面向**两个对话方之间消息对**的设计（user-assistant 或 user-user）；对多 agent 群聊或文档批处理，需要重新设计消息分组与 update 触发条件。
- DELETE 操作的"contradicts"判断由 LLM 单步给出，**没有 audit/反事实压力测试通道**——这与 v3 memory-as-metabolism 的 AUDIT-by-suspension 设计是不同立场：mem0 选择直觉判断 + 后续操作可纠正，而非显式 audit cycle。

## References

- Algorithm 1（`sections/appendix.tex` 第 911–966 行）：UpdateMemory 与 ClassifyOperation 伪代码。
- §3.1（`sections/proposed_work.tex` 第 1155 行）：四操作语义与"不用独立分类器"的设计选择。
- 来源：`data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt`。

## Footnotes

[^1]: ClassifyOperation 伪代码（第 950–964 行 verbatim 块）：
    ```
    Function ClassifyOperation(f, M):
        If not SemanticallySimilar(f, M):  Return ADD
        ElseIf Contradicts(f, M):          Return DELETE
        ElseIf Augments(f, M):             Return UPDATE
        Else:                              Return NOOP
    ```

[^2]: UPDATE 的 InformationContent 门槛（第 931–933 行）："If InformationContent(f) > InformationContent(m_i): M ← (M \ {m_i}) ∪ {(id_i, f, 'UPDATE')}  // Replace with richer information"

[^3]: 不用独立分类器的设计原文（第 1155 行）："Rather than using a separate classifier, we leverage the LLM's reasoning capabilities to directly select the appropriate operation based on the semantic relationship between the candidate fact and existing memories."
