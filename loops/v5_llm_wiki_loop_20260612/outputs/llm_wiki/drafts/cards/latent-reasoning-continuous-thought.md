---
id: latent-reasoning-continuous-thought
title: 潜空间推理（单模型连续思维）
status: draft
card_type: research-thread
tags: [latent-reasoning, continuous-thought, coconut, hidden-state, bfs]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
evidence_basis: practitioner_report
justification: ../justification/latent-reasoning-continuous-thought.md
canonical_concept: latent-reasoning-continuous-thought
aliases: [latent reasoning, 潜空间推理, intra-agent continuous thought, 连续思维]
summary: >-
  潜空间推理 (latent-reasoning-continuous-thought): 将隐藏状态作为输入 embedding 反馈而非解码为 token，模型在连续向量空间中无声推理并以叠加态保持多推理路径。代表工作 Coconut (Hao et al., ICLR 2025) 在规划任务通过涌现 BFS 达 97.0%，vs chain-of-thought 77.5%。其他方法包括 Pause Tokens、iCoT、SoftCoT、Thinking States、Superposition Theory。
related: [token-bottleneck-triple-loss, latent-communication-depth-spectrum]
---

潜空间推理（Thread 1: Latent Reasoning）是 BTTB wiki 追踪的两条主线之一，关注单模型内部的连续思维。[^src-1]

核心机制：将隐藏状态作为输入 embedding 反馈（而非解码为 token），使模型在连续向量空间中无声推理，并以叠加态保持多条推理路径。[^src-2]

关键结果：Hao et al. 的 Coconut (ICLR 2025) 在规划任务上通过涌现的广度优先搜索 (BFS) 达到 97.0%，而 chain-of-thought 在相同任务上为 77.5%。[^src-3]

该线程还包括：Pause Tokens、iCoT、SoftCoT、Thinking States、Superposition Theory paper。[^src-4]

[^card-1]: 参见 [token-bottleneck-triple-loss] 了解该研究方向试图解决的核心问题

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Thread 1: Latent Reasoning" P9 -- "Thread 1: Latent Reasoning — intra-agent continuous thought"
[^src-2]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Thread 1: Latent Reasoning" P10 -- "Feed hidden states back as input embeddings instead of decoding to tokens. The model reasons silently in continuous vector space, holding multiple reasoning paths in superposition."
[^src-3]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Thread 1: Latent Reasoning" P10 -- "Hao et al.'s Coconut (ICLR 2025): 97.0% on planning tasks via emergent BFS, vs. 77.5% for chain-of-thought on the same tasks."
[^src-4]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Thread 1: Latent Reasoning" P10 -- "Pause Tokens, iCoT, SoftCoT, Thinking States, and the Superposition Theory paper round out this thread."
