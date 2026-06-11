---
id: communication-depth-spectrum
title: 通信深度谱 10 级框架
status: accepted
card_type: framework
tags: [latent-communication, inter-agent, information-density, depth-spectrum]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
justification: ../justification/communication-depth-spectrum.md
canonical_concept: communication-depth-spectrum
aliases: [通信深度谱, depth spectrum, 10-level spectrum, 信息密度谱, latent communication levels]
summary: >-
  communication-depth-spectrum（通信深度谱 / depth spectrum / 10-level spectrum / 信息密度谱）
  是一个 10 级框架，按每位置携带的信息量排列 agent 间通信方式：从自然语言（~15 bits/position）
  到完整隐状态序列（~40K bits/position），中间经过嵌入、增量、结构化表示、视觉通道、KV 缓存等
related: [discrete-token-bottleneck, latent-reasoning-continuous-thought]
---

通信深度谱是一个将 agent 间通信方式按**每位置携带的信息量**排列的 10 级框架[^src-1]：

- **浅端**：自然语言，约 15 bits/position[^src-2]
- **深端**：完整隐状态序列，约 40K bits/position[^src-2]

中间各级按信息密度递增排列[^src-3]：
1. 自然语言
2. 嵌入（Embeddings）
3. 增量（Deltas）
4. 结构化表示（Structured representations）
5. 视觉通道方法（Vision-channel methods）
6. KV 缓存选择（KV-cache selection）
7. KV 交换（KV exchange）
8. 激活通信（Activation communication）
9. 完整隐状态（Full hidden-state）
10. 潜序列（Latent sequences）

该框架的核心洞察：**信息密度与架构耦合度之间存在权衡**——深端方法（如完整隐状态交换）虽然信息密度极高，但要求通信双方具有紧密的架构耦合[^src-4]。当前研究前沿的目标是「弯曲」这条曲线——在不强制紧密架构耦合的前提下达到高信息密度[^src-4]。

标志性结果：LatentMAS 在零训练条件下实现了相对文本 471 倍的理论压缩率[^src-5]。

该谱涵盖 12 篇论文的方法，包括 CIPHER、AC、KVComm、C2C、Interlat、SDE、ThoughtComm、Vision Wormhole、LatentMAS 等[^src-6]。

## Footnotes

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第11-12行 -- "The wiki organizes this as a 10-level depth spectrum ordered by how much information each level carries per position"
[^src-2]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第12行 -- "from natural language at the shallow end (~15 bits/position) to full hidden-state sequences at the deep end (~40K bits/position)"
[^src-3]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第12行 -- "Embeddings, deltas, structured representations, vision-channel methods, KV-cache selection, KV exchange, activation communication, and full hidden-state plus latent come in between."
[^src-4]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第13行 -- "The frontier, as the wiki frames it, is bending the depth-spectrum curve — reaching high information density without forcing tight architectural coupling between the agents on either end of the channel."
[^src-5]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第12行 -- "LatentMAS achieves 471x theoretical compression over text with zero training."
[^src-6]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第12行 -- "Twelve papers in this thread — CIPHER, AC, KVComm, C2C, Interlat, SDE, ThoughtComm, Vision Wormhole, LatentMAS, others."
