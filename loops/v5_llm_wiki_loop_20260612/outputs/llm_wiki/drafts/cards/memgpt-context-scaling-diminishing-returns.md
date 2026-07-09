---
id: memgpt-context-scaling-diminishing-returns
title: 上下文扩展的递减收益与 lost-in-the-middle 现象
status: draft
card_type: problem-statement
tags: [context-window, attention-distribution, scaling-limits, motivation]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: experimental_paper
justification: ../justification/memgpt-context-scaling-diminishing-returns.md
canonical_concept: context-scaling-diminishing-returns
aliases: [lost in the middle, context scaling limitations, 上下文扩展递减收益, 注意力分布不均]
summary: >-
  context-scaling-diminishing-returns 上下文扩展递减收益: MemGPT论文指出直接扩展transformer
  上下文长度面临二次计算成本增长(self-attention), 且即便成功扩展, 长上下文模型也难以有效利用
  额外上下文 -- Liu et al.(2023)发现注意力分布不均匀(lost in the middle),
  模型更能recall窗口首尾而非中间信息。这一双重局限性(计算代价+利用效率)
  构成MemGPT选择内存层级方案而非盲目扩展上下文的核心动机。
related: [memgpt-virtual-context-management]
---

MemGPT 论文指出直接扩展 LLM 上下文长度面临双重根本性挑战：[^src-1]

**计算代价**: 直接扩展 transformer 上下文长度会因 self-attention 机制导致计算时间和内存成本的二次增长。虽然已有多种高效架构（稀疏注意力、低秩近似等）尝试缓解，但直接扩展仍是活跃研究挑战。[^src-1]

**利用效率低下 (Lost in the Middle)**: 即便能克服计算挑战，近期研究 (Liu et al., 2023) 表明长上下文模型难以有效利用额外上下文。具体表现为注意力分布不均匀：模型更能有效 recall 上下文窗口开头和末尾的信息，而对中间位置的 tokens 表现显著下降。[^src-2]

这一双重局限性使论文得出结论：鉴于训练 SOTA LLM 所需的巨大资源以及上下文扩展的递减收益，亟需替代技术来支持长上下文 -- 这正是 MemGPT 虚拟上下文管理方案的核心动机。[^src-1]

论文还指出现实中许多文档（如 SEC Form 10-K 年报）轻易超过百万 token，盲目扩展上下文似乎难以作为固定上下文问题的解决方案。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/intro.tex" -- "Directly extending the context length of transformers incurs a quadratic increase in computational time and memory cost...even if we could overcome the computational challenges of context scaling, recent research shows that long-context models struggle to utilize additional context effectively"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "Recent research also raises doubts about the utility of simply scaling contexts, since they find uneven attention distributions in large context models (the model is more capable of recalling information at the beginning or end of its context window, vs tokens in the middle)"
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "legal or financial documents such as Annual Reports (SEC Form 10-K) can easily pass the million token mark...it becomes difficult to envision blindly scaling up context as a solution"
[^card-1]: [memgpt-virtual-context-management] 上下文扩展的局限性是选择虚拟上下文管理方案的直接动因
