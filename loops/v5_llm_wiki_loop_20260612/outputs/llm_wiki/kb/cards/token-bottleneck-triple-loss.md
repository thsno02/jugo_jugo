---
id: token-bottleneck-triple-loss
title: Token 瓶颈的三重损失
status: accepted
card_type: problem-framing
tags:
- llm-architecture
- token-bottleneck
- latent-reasoning
- information-loss
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- complete-tech-live-frontier
evidence_basis: practitioner_report
justification: ../justification/token-bottleneck-triple-loss.md
canonical_concept: token-bottleneck-triple-loss
aliases:
- token bottleneck
- discrete bottleneck
- token 瓶颈
summary: 'Token 瓶颈三重损失 (token-bottleneck-triple-loss): LLM 内部为连续向量但对外通过离散 token 接口。损失包括 (1) 丢弃分布不确定性——概率分布坍缩为单一采样 token；(2) 阻止假设叠加——无法在同一向量槽保持多推理分支；(3) 在流利性上浪费算力——语法 token 不承载推理内容但成本相同。'
related:
- latent-reasoning-continuous-thought
- latent-communication-depth-spectrum
---

大语言模型面临的结构性问题：内部为连续表示（每层为稠密向量），但被迫通过离散 token 瓶颈与外界交互。该瓶颈造成三重损失：[^src-1]

1. **丢弃分布不确定性** — 完整概率分布坍缩为单一采样 token
2. **阻止假设叠加** — 一个 token 一条路径，无法在同一向量槽中保持两个推理分支
3. **在流利性上浪费算力** — 为语法存在的 token 不承载推理内容但计算成本相同

BTTB wiki 追踪的 27 个源（26 篇论文 + 1 个开源项目，2022.12–2026.04）共同探索：当去除这一瓶颈时会发生什么——无论是在单一模型内部还是在协作模型之间。[^src-2]

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "The frontier we pointed it at" P4-7 -- "large language models are internally continuous (dense vectors at every layer), but they're forced to interface with the world through a discrete token bottleneck."
[^src-2]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "The frontier we pointed it at" P8 -- "The wiki tracks 27 sources (26 papers + 1 open-source project, Dec 2022 – Apr 2026) that collectively ask: what happens when you remove the bottleneck"
