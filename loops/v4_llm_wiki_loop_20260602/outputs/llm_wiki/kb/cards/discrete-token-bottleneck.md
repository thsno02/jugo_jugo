---
id: discrete-token-bottleneck
title: 离散 token 瓶颈的三重代价
status: accepted
card_type: concept
tags: [latent-reasoning, architecture-limitation, token-interface, information-loss]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
justification: ../justification/discrete-token-bottleneck.md
canonical_concept: discrete-token-bottleneck
aliases: [离散token瓶颈, token bottleneck, 令牌瓶颈, discrete interface cost]
summary: >-
  discrete-token-bottleneck（离散token瓶颈 / token bottleneck / 令牌瓶颈 / discrete interface cost）
  描述 LLM 内部连续（dense vectors）但被迫通过离散 token 接口与外界交互的结构性问题，
  造成三重代价：丢弃分布不确定性、阻止假设叠加态、在流畅性上浪费算力
related: [latent-reasoning-continuous-thought, communication-depth-spectrum]
---

大型语言模型在每一层内部都是连续的（dense vectors），但被强制通过离散 token 瓶颈与外界交互[^src-1]。这一结构性问题带来三重代价：

1. **丢弃分布不确定性**——完整的概率分布被压缩为单个采样 token，分布中的信息损失不可逆[^src-2]。

2. **阻止假设叠加态**——一个 token 意味着一条路径；无法在同一个向量位置保持两条推理分支的叠加[^src-3]。

3. **在流畅性上浪费算力**——为语法存在的 token 不携带任何推理内容，但消耗与推理 token 相同的计算成本[^src-4]。

这三重代价定义了潜空间推理（latent reasoning）和潜通信（latent communication）两条研究线索的共同出发点：前者通过在连续向量空间中「无声推理」绕过瓶颈[^card-1]，后者通过用连续通道替代自然语言管道绕过瓶颈[^card-2]。

## Footnotes

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第4行 -- "large language models are internally continuous (dense vectors at every layer), but they're forced to interface with the world through a discrete token bottleneck."
[^src-2]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第5行 -- "Discards distributional uncertainty — a full probability distribution collapses to one sampled token."
[^src-3]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第6行 -- "Prevents superposition of hypotheses — one token, one path; you can't hold two reasoning branches in the same vector slot."
[^src-4]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- 第7行 -- "Wastes compute on fluency — tokens that exist for grammar carry no reasoning content but cost just as much."
[^card-1]: [潜空间推理与连续思维](latent-reasoning-continuous-thought.md) -- 通过在连续向量空间推理绕过 token 瓶颈
[^card-2]: [通信深度谱](communication-depth-spectrum.md) -- 通过连续通道替代自然语言管道绕过 token 瓶颈
