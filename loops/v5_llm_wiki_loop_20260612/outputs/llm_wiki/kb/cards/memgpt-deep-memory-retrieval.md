---
id: memgpt-deep-memory-retrieval
title: MemGPT 深度记忆检索任务
status: accepted
card_type: experimental-result
tags:
- benchmark
- conversational-agent
- memory-retrieval
- consistency
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memgpt
evidence_basis: experimental_paper
justification: ../justification/memgpt-deep-memory-retrieval.md
canonical_concept: memgpt-deep-memory-retrieval
aliases:
- deep memory retrieval
- DMR
- DMR task
- 深度记忆检索
summary: MemGPT memgpt-deep-memory-retrieval 深度记忆检索 DMR 是基于Multi-Session Chat(MSC)数据集 设计的对话一致性评测任务。用户向agent提出明确引用先前对话内容的问题, 期望窄范围答案。 MemGPT+GPT-4 Turbo达93.4%准确率(ROUGE-L 0.827), 远超固定上下文基线的35.3%(0.359)。 基线使用有损摘要,
  MemGPT通过分页搜索访问完整对话历史。该结果表明层级内存管理 显著提升长期对话的记忆一致性。
related:
- memgpt-virtual-context-management
- memgpt-self-directed-memory
- zep-dmr-benchmark-results
- memgpt-conversation-opener-engagement
- memgpt-nested-kv-retrieval
---
深度记忆检索 (Deep Memory Retrieval, DMR) 是 MemGPT 论文提出的新评测任务，旨在测试对话 agent 的一致性 (consistency)。[^src-1]

**任务设计**: 基于 Multi-Session Chat (MSC) 数据集，使用独立 LLM 生成问答对。问题明确引用先前对话内容（跨 session 1-5），且具有非常窄的期望答案范围。评测使用 ROUGE-L recall 和 LLM judge 两种方式。[^src-1]

**关键对比**:
- 基线方法可看到过去五次对话的有损摘要（模拟递归摘要过程）
- MemGPT 能访问完整对话历史，但必须通过分页搜索查询将其带入主上下文 [^src-2]

**实验结果** (Table 1): [^src-3]
| 方法 | 准确率 | ROUGE-L (R) |
|------|--------|-------------|
| GPT-3.5 Turbo | 38.7% | 0.394 |
| + MemGPT | 66.9% | 0.629 |
| GPT-4 | 32.1% | 0.296 |
| + MemGPT | 92.5% | 0.814 |
| GPT-4 Turbo | 35.3% | 0.359 |
| + **MemGPT** | **93.4%** | **0.827** |

MemGPT 明确提升了底层 LLM 的性能：从 MemGPT 切换到对应 LLM 基线时，准确率和 ROUGE 分数均显著下降。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "We introduce a new 'deep memory retrieval' (DMR) task based on the MSC dataset designed to test the consistency of a conversational agent"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "The baselines are able to see a lossy summarization of the past five conversations to mimic an extended recursive summarization procedure, while MemGPT instead has access to the full conversation history but must access it via paginated search queries to recall memory"
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "tables/deep_memory_retrieval_table_singlecol.tex" -- "GPT-4 Turbo & 35.3% & 0.359 ... + MemGPT & 93.4% & 0.827"
[^card-1]: [memgpt-virtual-context-management] DMR 任务验证了虚拟上下文管理在长期对话中的有效性
