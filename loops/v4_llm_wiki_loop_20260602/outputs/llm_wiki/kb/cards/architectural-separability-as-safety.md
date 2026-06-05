---
id: architectural-separability-as-safety
title: 架构可分离性作为安全承诺
status: accepted
card_type: distinction
tags: [companion-memory, separability, safety, base-model, correction-channel, weight-externalization]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/architectural-separability-as-safety.md
canonical_concept: architectural-separability-as-safety
aliases: [架构可分离性安全, architectural separability as safety, 权重外部化安全承诺, wiki-weight separation, 基模型纠正通道]
summary: >-
  architectural-separability-as-safety（架构可分离性安全 / wiki-weight separation / 基模型纠正通道）伴侣记忆框架的安全设计承诺：wiki 必须保持在基模型权重之外，因为可分离性在结构上必要——使基模型演进作为外部纠正通道对抗用户耦合认知固化；将 wiki 折叠进权重则永久关闭此通道
related: [companion-knowledge-system, wiki-as-git-repo, weight-internalization-aspiration, three-correction-channels]
---

架构可分离性是伴侣记忆框架的一项设计承诺而非实现细节：wiki 必须保持在基模型权重之外[^src-1]。

**安全理由**：Lewis et al. (2020) 和 Atlas 等工作已在操作便利性的基础上论证了外部化（更新无需重训练、溯源审计）。本论文增加的是一个**伴侣特定的安全理据**——可分离性在结构上必要，使基模型演进作为外部纠正通道，特别针对用户耦合认知固化发挥作用[^src-2]。

**机制**：运行伴侣系统五年的用户从模型改进的事实先验和对齐训练中**免费获益**，因为更换基模型是配置变更而非 wiki 操作。将 wiki 折叠进权重，此通道永久关闭[^src-3]。

**三个诚实限制**[^src-4]：
1. Wiki 仍然锚定解释——高引力的错误条目仍然偏置输出
2. 基模型更新不总是纠正——实验室出于多种原因更新，包括可能使特定用户变差的原因
3. 用户不控制更新何时发生

**存储表示含义**：纯文本作为权威内容存储（而非仅嵌入）使跨模型交换的可审计性成为可能——模型交换强制重新嵌入，期间语义可以以用户事后无法检查的方式漂移。纯文本层是被保留的，嵌入层是派生制品[^src-5]。

**与现有外部化教义的区别**：不是更广泛的"保持知识外部化"论点的重述，而是一个更窄更具体的安全论据——可分离性保留的是特别针对用户耦合认知固化的基模型演进纠正通道[^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Abstract" -- "the wiki stays outside the base model weights. This is deliberate."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 8.3" -- "separability is not merely operationally convenient... but structurally necessary for base-model evolution to function as an external correction channel specifically against user-coupled epistemic entrenchment."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 8.3" -- "a user running a companion system for five years benefits from the model's improved factual priors and alignment training precisely because swapping the base model is a configuration change, not a wiki operation. Fold the wiki into weights and this channel closes permanently."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 8.3" -- "Three honest limits: the wiki still anchors interpretation... base model updates are not always corrections... the user does not control when updates happen."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 6" -- "Plain text as primary representation makes that survival auditable in a way embeddings-only storage does not"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 8.3" -- "That rationale is narrower than 'keep knowledge external.'"
