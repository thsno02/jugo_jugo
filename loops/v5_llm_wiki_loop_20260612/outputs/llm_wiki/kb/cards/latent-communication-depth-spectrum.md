---
id: latent-communication-depth-spectrum
title: 潜通信深度谱系
status: accepted
card_type: framework
tags:
- latent-communication
- depth-spectrum
- inter-agent
- information-density
- latentmas
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- complete-tech-live-frontier
evidence_basis: practitioner_report
justification: ../justification/latent-communication-depth-spectrum.md
canonical_concept: latent-communication-depth-spectrum
aliases:
- depth spectrum
- 深度谱系
- communication-depth spectrum
- 通信深度分类
- 10-level depth spectrum
summary: '潜通信深度谱系 (latent-communication-depth-spectrum): 替代智能体间自然语言管道为连续通道，按每位置信息承载量组织为 10 级——浅端自然语言 ~15 bits/position，深端完整隐藏状态序列 ~40K bits/position。中间包括 embeddings、deltas、structured representations、vision-channel、KV-cache
  selection、KV exchange、activation communication 等。LatentMAS 实现 471x 理论压缩（相对文本），零训练。涉及 12 篇论文。前沿方向：在不迫使架构紧耦合的前提下达到高信息密度。'
related:
- token-bottleneck-triple-loss
- latent-reasoning-continuous-thought
---

潜通信（Thread 2: Latent Communication）是 BTTB wiki 追踪的第二条主线，关注智能体间的连续通道。[^src-1]

核心框架为 10-level depth spectrum，按每位置信息承载量排列通信方式：[^src-2]
- 浅端：自然语言，~15 bits/position
- 深端：完整隐藏状态序列，~40K bits/position
- 中间层次：embeddings → deltas → structured representations → vision-channel methods → KV-cache selection → KV exchange → activation communication → full hidden-state + latent

关键结果：LatentMAS 实现 471x 理论压缩（相对文本），零训练。[^src-3]

涉及 12 篇论文：CIPHER、AC、KVComm、C2C、Interlat、SDE、ThoughtComm、Vision Wormhole、LatentMAS 等。[^src-4]

据材料描述，当前前沿方向在于"弯曲 depth-spectrum 曲线"—— 在不迫使通道两端智能体紧密架构耦合的情况下达到高信息密度。[^src-5]

[^card-1]: 参见 [token-bottleneck-triple-loss] 了解驱动此研究方向的核心问题

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Thread 2: Latent Communication" P11 -- "Thread 2: Latent Communication — inter-agent continuous channels"
[^src-2]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Thread 2: Latent Communication" P12 -- "a 10-level depth spectrum ordered by how much information each level carries per position — from natural language at the shallow end (~15 bits/position) to full hidden-state sequences at the deep end (~40K bits/position)."
[^src-3]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Thread 2: Latent Communication" P12 -- "LatentMAS achieves 471× theoretical compression over text with zero training."
[^src-4]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Thread 2: Latent Communication" P12 -- "Twelve papers in this thread — CIPHER, AC, KVComm, C2C, Interlat, SDE, ThoughtComm, Vision Wormhole, LatentMAS, others."
[^src-5]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "The frontier" P13 -- "The frontier...is bending the depth-spectrum curve — reaching high information density without forcing tight architectural coupling between the agents on either end of the channel."
