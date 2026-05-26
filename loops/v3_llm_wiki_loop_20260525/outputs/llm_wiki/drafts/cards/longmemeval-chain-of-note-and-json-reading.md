---
id: longmemeval-chain-of-note-and-json-reading
title: Chain-of-Note + JSON 结构化 prompt 即使在 oracle 检索下也能涨 10 分
status: draft
card_type: operational_rule
tags: [#reading-strategy, #chain-of-note, #structured-prompt]
created_time: 2026-05-26T14:35:00+08:00
edited_time: 2026-05-26T14:35:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
provenance_card: ../provenance/longmemeval-chain-of-note-and-json-reading.md
aliases: [CoN, structured prompt, reading strategy]
related: [longmemeval-three-stage-memory-framework]
---

## 规则

LongMemEval §5.4 把 reading 阶段独立做消融，发现两个朴素技巧合用就能逼近上限：

1. **结构化 JSON 格式**——把检索到的 memory items 渲染成 JSON 数组（每条 item 一个 dict），让 reader 显式识别"这是供我读的数据"。来自 Yin et al. 2023 "structured prompt 提供 4.2 Rouge-L 提升"的延伸。
2. **Chain-of-Note (CoN)**——指示 LLM 先 traverse 每个 memory item 抽出与问题相关的 evidence note，再在 note 上做推理给答案，把"长上下文阅读"拆成"复制证据 + 简短推理"两步。

合用后，即便在 **oracle retrieval**（只把真实证据 session 给模型）下，CoN+JSON 也比朴素读法高 **最多 10 个绝对分**。

## 重要观察

- **CoN 与 JSON 单独都不够稳**：没有 CoN 时，JSON 不一定优于自然语言；有 CoN 时，JSON 才稳定增益。这说明 CoN 把"读"拆成两步后，结构化输入才能被显式利用。
- **CoN 增益对 reader 越弱反而越显著**——论文 appendix 显示 Llama 3.1 8B Instruct 在 oracle 上从 0.710 → 0.710（CoN 持平），但在 LongMemEval-S 真实检索上是 0.420 → 仍然有大量增益空间；GPT-4o 也从 0.870 → 0.924 oracle、0.606 → 0.640 LongMemEval-S。
- **Reading 是被忽视的环节**：error analysis 显示 reader LLM 错的 case 中 40-50% 是 "retrieval 是对的，但 generation 错了"。优化 retrieval 不会自动解决。

## 边界

- CoN 要求 reader 能"先抽证据再答"——若上下文已经接近 reader 最大长度，CoN 的中间笔记会占用宝贵 token，反而不利。论文用 800 token 上限的 greedy 生成。
- JSON 格式增益建立在 reader 已经被良好 instruction-tuned；老模型对 JSON 容器的鲁棒性差。

## References

- §5.4 reading 实验：`data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` 第 1517-1521 行，及第 1526-1533 行图 `fig:main-fig-reading-design`。
- CoN prompt 与 baseline prompt：第 1700-1714 行（reading-prompt 完整文本）。
- "Reader 错占 40-50%"error analysis：第 1768 行。

## Footnotes

- CoN+JSON 的 10 分增益："even with perfect retrieval, a suboptimal reading strategy results in up to a 10-point absolute performance drop compared to the best approach for GPT-4o. Notably, when CoN is not applied, JSON format does not consistently outperform the natural language format. However, with CoN, JSON format consistently benefits reader LLMs of various capabilities."（第 1521 行）
- CoN prompt 实例："Answer the question step by step: first extract all the relevant information, and then reason over the information to get the answer."（第 1702 行）
- Error 分布："a substantial proportion of errors corresponds to correct retrieval yet wrong generation (15\%$\sim$19\% of all instances, and 40\%$\sim$50\% among the error instances)."（第 1768 行）
