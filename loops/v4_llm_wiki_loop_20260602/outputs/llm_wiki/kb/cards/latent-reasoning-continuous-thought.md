---
id: latent-reasoning-continuous-thought
title: 潜空间推理与连续思维
status: accepted
card_type: concept
tags: [latent-reasoning, continuous-thought, hidden-state-feedback, emergent-BFS]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
justification: ../justification/latent-reasoning-continuous-thought.md
canonical_concept: latent-reasoning-continuous-thought
aliases: [潜空间推理, latent reasoning, 连续思维, continuous thought, intra-agent continuous thought]
summary: >-
  latent-reasoning-continuous-thought（潜空间推理 / latent reasoning / 连续思维 / continuous thought）
  指将隐状态直接反馈为输入嵌入，使模型在连续向量空间中无声推理、保持多推理路径叠加态的技术路线；
  Coconut (ICLR 2025) 在规划任务上达到 97.0%（CoT 为 77.5%），通过涌现 BFS 实现
related: [discrete-token-bottleneck, communication-depth-spectrum]
---

潜空间推理（Latent Reasoning）是绕过离散 token 瓶颈[^card-1]的第一条研究线索——面向单 agent 内部的连续思维。核心机制是：将隐状态直接反馈为输入嵌入，而不是解码为 token[^src-1]。模型在连续向量空间中「无声推理」，可以在叠加态中保持多条推理路径[^src-2]。

**标志性结果**：Hao et al. 的 Coconut（ICLR 2025）在规划任务上达到 97.0% 准确率，对比链式思维（Chain-of-Thought）的 77.5%——差距达 19.5 个百分点[^src-3]。其成功的关键机制是**涌现广度优先搜索（emergent BFS）**：连续隐状态允许模型同时探索多条分支，而非 CoT 的逐步串行推理[^src-3]。

该线索下的其他工作包括[^src-4]：
- Pause Tokens（推理暂停标记）
- iCoT（内化链式思维）
- SoftCoT（软链式思维）
- Thinking States（思维状态）
- Superposition Theory paper（叠加态理论）

这些方法共同构成一个研究方向：让模型的推理过程不再受限于 token 的离散性和串行性，而是利用向量空间的连续性和高维性进行更高效的探索。

## Footnotes

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第9-10行 -- "Feed hidden states back as input embeddings instead of decoding to tokens."
[^src-2]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第9-10行 -- "The model reasons silently in continuous vector space, holding multiple reasoning paths in superposition."
[^src-3]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第10行 -- "Headline number from Hao et al.'s Coconut (ICLR 2025): 97.0% on planning tasks via emergent BFS, vs. 77.5% for chain-of-thought on the same tasks."
[^src-4]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第10行 -- "Pause Tokens, iCoT, SoftCoT, Thinking States, and the Superposition Theory paper round out this thread."
[^card-1]: [离散token瓶颈的三重代价](discrete-token-bottleneck.md) -- 本卡描述的技术路线正是为了绕过该卡定义的三重代价
