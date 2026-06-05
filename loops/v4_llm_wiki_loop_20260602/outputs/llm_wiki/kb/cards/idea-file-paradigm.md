---
id: idea-file-paradigm
title: Idea File 分发范式
status: accepted
card_type: concept
tags: [llm-agent, distribution, idea-file, open-source]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [karpathy-x-launch-post]
justification: ../justification/idea-file-paradigm.md
canonical_concept: idea-file-paradigm
aliases: [idea file, 想法文件, idea sharing paradigm, 想法分发范式]
summary: >-
  idea-file-paradigm（idea file / 想法文件 / 想法分发范式）LLM agent 时代的分发单元从代码/应用转向抽象想法文件，接收者的 agent 负责定制化构建实现
related: []
  - intentional-abstraction
  - llm-wiki-pattern
  - human-llm-role-division
---

Karpathy 在 LLM Wiki 推文的后续帖子中提出了 **idea file**（想法文件）的概念：在 LLM agent 时代，分享具体代码或应用的必要性大幅降低，取而代之的分发单元是抽象层面的"想法"[^src-1]。

其运作机制是：作者将想法以 GitHub Gist 等格式发布，接收者将该想法文件交给自己的 LLM agent，由 agent 根据个人具体需求进行定制化构建[^src-2]。这意味着同一份想法文件可以产生无数种不同的具体实现，每种实现都针对不同用户的场景做了适配。

想法文件被**刻意保持抽象和模糊**，这不是缺陷而是特性——因为一个好的想法可以向多个方向发展，过度具体化反而限制了可能性空间[^src-3]。这与传统开源的"fork 代码"模式形成对比：idea file 范式下，被 fork 的是想法本身，而非代码。

社区协作的方式也随之改变：人们可以在 Discussion 中调整想法或贡献自己的想法变体[^src-4]，形成以想法为中心的协作模式。

## Footnotes

[^src-1]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- Tweet 1 text -- "in this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the other person's agent customizes & builds it for your specific needs"
[^src-2]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- Tweet 1 text -- "So here's the idea in a gist format... You can give this to your agent and it can build you your own LLM wiki and guide you on how to use it etc."
[^src-3]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- Tweet 1 text -- "It's intentionally kept a little bit abstract/vague because there are so many directions to take this in."
[^src-4]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- Tweet 1 text -- "And ofc, people can adjust the idea or contribute their own in the Discussion which is cool."
