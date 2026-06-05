---
id: context-scaling-diminishing-returns
title: 上下文窗口扩展的递减收益问题
status: accepted
card_type: distinction
tags: [LLM, context_window, lost_in_the_middle, attention, scaling, transformer]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
justification: ../justification/context-scaling-diminishing-returns.md
canonical_concept: context-scaling-diminishing-returns
aliases: [上下文扩展递减收益, lost in the middle, 上下文窗口限制]
summary: >-
  context-scaling-diminishing-returns（上下文扩展递减收益, lost in the middle）MemGPT 论文论证直接扩展 LLM 上下文窗口面临二次方计算开销、长上下文模型存在不均匀注意力分布（中间位置信息利用差）、以及实际文档长度可能远超可行上下文规模等三重困境，为虚拟上下文管理方案提供动机
related: [virtual-context-management, memgpt-document-qa-scaling]
---

MemGPT 论文提出了直接扩展 LLM 上下文窗口面临的多重困境，作为虚拟上下文管理方案的核心动机：

**二次方计算开销**：直接扩展 transformer 的上下文长度会因自注意力机制导致计算时间和内存成本的二次增长 [^src-1]。

**长上下文利用效果不佳**：即使克服了计算挑战，近期研究表明长上下文模型在利用额外上下文方面表现不佳。Liu 等人发现长上下文模型存在不均匀的注意力分布：模型更擅长回忆上下文窗口开头或末尾的信息，而非中间位置的 token（"lost in the middle"问题）[^src-2]。

**实际文档长度远超上限**：许多真实文档分析任务涉及的文档长度远超当前最大上下文窗口。例如法律或财务文档如年报（SEC Form 10-K）可轻松超过百万 token。许多任务还需要跨多个此类长文档建立联系 [^src-3]。

这三重困境共同论证了：盲目扩展上下文并非解决固定上下文问题的可行方案，需要更灵活的内存架构如 MemGPT [^src-3]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/intro.tex -- "Directly extending the context length of transformers incurs a quadratic increase in computational time and memory cost due to the transformer architecture's self-attention mechanism"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/intro.tex -- "even if we could overcome the computational challenges of context scaling, recent research shows that long-context models struggle to utilize additional context effectively"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/experiments.tex -- "many documents easily surpass these lengths; for example, legal or financial documents such as Annual Reports (SEC Form 10-K) can easily pass the million token mark...it becomes difficult to envision blindly scaling up context as a solution...more flexible memory architectures like MemGPT are needed."
