---
id: memgpt-dmr-task-evaluation
title: MemGPT 的 Deep Memory Retrieval 任务：把"记得住"做成可量化的 consistency 指标
status: accepted
card_type: source_claim
tags: [#memgpt, #benchmark, #DMR, #MSC, #LLM-judge, #ROUGE-L]
created_time: 2026-05-26T15:25:00+08:00
edited_time: 2026-05-28T11:12:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
provenance_card: ../provenance/memgpt-dmr-task-evaluation.md
aliases: [DMR task, deep memory retrieval, MSC session 6, MemGPT consistency benchmark]
related: [memgpt-virtual-context-os-analogy, memgpt-main-vs-external-context, memgpt-docqa-pagination-failure-mode, zep-dmr-benchmark-critique, mem0-locomo-benchmark-evaluation]
---

## 任务设计

DMR (Deep Memory Retrieval) 是 MemGPT 论文为了量化**对话 agent 的一致性 (consistency)** 而新造的任务[^src1]，建立在 Multi-Session Chat (MSC) dataset 之上：

- MSC 原本 5 个 session × 每 session 大约一打消息；
- 作者**自造 session 6**，里面只有一对 Q–A：用户提一个**明确回指前 5 个 session 中某细节**的问题，gold answer 范围非常狭窄；
- 问答对由独立 LLM 用 self-instruct 流程合成，prompt 显式要求"问题必须**不能仅靠 persona summary** 回答，必须用到旧 chat log"，并给出"surfing/Taco Bell" 反例对训练 LLM 区分好/坏问题；
- 评测时 agent 看不到 session 6 之前的对话原文（必须靠内存机制 retrieval），最后输出和 gold answer 比对。

## 双指标：ROUGE-L recall + LLM-judge

- **ROUGE-L recall (R)**：选 recall 而不是 F1 / precision，理由是"生成回答普遍比 gold 长很多"——precision 会被冗长惩罚；
- **LLM-as-Judge**：GPT-4 当裁判，被给定 question + gold + generated，输出 CORRECT/WRONG。论文借用并形式化了 prompt（"shell necklace" hawaii 示例），并显式列出 CORRECT 的可接受变体（"got a ton of stuff... that surfboard, the mug, the necklace, those coasters too.." 也算对）；
- 这条评估范式后来被 Mem0 复用并改写（见 mem0 论文 appendix），是 MSC-style memory 评估的事实标准。

## 主结果（论文 Table）

| Model | Accuracy ↑ | ROUGE-L (R) ↑ |
| --- | --- | --- |
| GPT-3.5 Turbo (baseline) | 38.7% | 0.394 |
| + MemGPT | 66.9% | 0.629 |
| GPT-4 (baseline) | 32.1% | 0.296 |
| + MemGPT | 92.5% | 0.814 |
| GPT-4 Turbo (baseline) | 35.3% | 0.359 |
| **+ MemGPT** | **93.4%** | **0.827** |

读法：

- baseline 都拿到一份"前 5 个 session 的 lossy recursive summary"作为上下文——这是 baseline 能拿到的最强 fixed-context 信号；
- MemGPT 看不到 summary，但可以**通过 conversation_search 函数翻 recall storage 的完整历史**；
- **GPT-4 baseline 反而 比 GPT-3.5 baseline 差**（32.1 vs 38.7）——论文未深入分析，但提示 lossy summary + 长 prompt 在更强模型上不一定有正向收益；
- 一旦套上 MemGPT，GPT-4 跳到 92.5%，GPT-4 Turbo 跳到 93.4%；ROUGE-L recall 也跟着翻倍。

## 为什么这一条比"看 J 分"更有信息量

- DMR 是**强 lossy-summary baseline**：不是给 baseline 一段截断对话，而是给它"代表全部 5 个 session"的精炼摘要——所以差距严格反映**主动 retrieval vs 被动摘要**的差异，不是上下文长度差异。
- DMR 的 gold answer 故意"narrow"，避免 ROUGE 蒙混过关；
- 论文承认 ROUGE/accuracy 上的"+MemGPT"差距如此之大，部分是因为 baseline 必须依赖 summary 的覆盖率上限——这件事意味着**只要 lossy 压缩在 ingestion 阶段就把细节丢了，下游再聪明也救不回来**。

## 边界与误用

- DMR 只测 single-turn 反问，不测多轮深度推理；
- baseline 的 lossy summary 是 MemGPT 作者自己产的，未必是其他系统能给 baseline 的最佳上下文；
- 92.5% 不等于 "MemGPT 永远不会忘"——它只表明在 narrow gold 的窄题上，retrieval 路径几乎都命中；
- LLM-judge 用 GPT-4 评分会引入 self-preference 偏差；论文用 ROUGE-L recall 做 sanity 但没给 IRR。

## References

- §experiments DMR 任务与表（`sections/experiments.tex` 第 1375–1389 行，table 在 `tables/deep_memory_retrieval_table_singlecol.tex` 第 1793–1832 行）。
- LLM judge prompt 完整文本（`sections/appendix.tex` 第 1231–1255 行）。
- self-instruct 生成 DMR 数据集（`sections/appendix.tex` 第 1257–1294 行）。
- 来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`。

## Footnotes

[^1]: 任务设计原文（experiments.tex 第 1370–1376 行）："Each multi-session chat in MSC has five total sessions, and each session consists of a roughly a dozen messages. As part of our consistency experiments, we created a new session (session 6) that contains a single question-answer response pair between the same two personas. ... we generated the DMR question-answer (QA) pairs using a separate LLM that was instructed to write a question from one user to another that could only be answered correctly using knowledge gained from the past sessions."

[^2]: ROUGE-L recall 选型理由（experiments.tex 第 1379–1380 行）："In practice, we notice that the generated responses (from both MemGPT and the baselines) were generally more verbose than the gold responses. We use the ROUGE-L recall (R) metric to account for the verbosity of the generated agent replies compared to the relatively short gold answer labels."

[^3]: GPT-4 + MemGPT 92.5%（tables/deep_memory_retrieval_table_singlecol.tex 第 1819–1827 行）："GPT-4 & 32.1\% & 0.296 / + MemGPT & 92.5\% & 0.814 / GPT-4 Turbo & 35.3\% & 0.359 / + MemGPT & 93.4\% & 0.827"

[^4]: baseline 拿 lossy summary 作为上下文（experiments.tex 第 1388 行）："The baselines are able to see a lossy summarization of the past five conversations to mimic an extended recursive summarization procedure, while MemGPT instead has access to the full conversation history but must access it via paginated search queries to recall memory."
