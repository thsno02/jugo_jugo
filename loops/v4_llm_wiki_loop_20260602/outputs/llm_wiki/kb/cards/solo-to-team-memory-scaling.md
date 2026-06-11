---
id: solo-to-team-memory-scaling
title: 个人记忆到团队记忆的渐进扩展路径
status: accepted
card_type: mechanism
tags: [agent-memory, scaling, solo-memory, team-memory, compounding, onboarding]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [cognitionus-llm-wiki-guide]
justification: ../justification/solo-to-team-memory-scaling.md
canonical_concept: solo-to-team-memory-scaling
aliases: [个人到团队记忆扩展, solo-to-team memory scaling, 记忆渐进扩展, memory compounding path]
summary: >-
  solo-to-team-memory-scaling（个人到团队记忆扩展 / solo-to-team memory scaling）Cognition 的架构路径：从单人 agent 记忆（偏好、决策、修复、安装配置）起步，当团队成员加入后，经审批的技能、决策和结果复合为团队大脑，每个 agent 均可复用；三层递进——solo（技能/决策/安装）→ team（带作者归属的共享技能）→ proof（复用收据与结果）
related: [agent-memory-lifecycle-phases, ask-first-retrieve-loop, confirm-first-skill-capture, knowledge-compounding]
---

Cognition 的产品架构设计了一条从个人到团队的**渐进扩展路径**，而非要求用户一开始就建立团队知识库[^src-1]。

**Solo 层（个人记忆）**：起步时只有一个人的 agent 记忆，保存该用户的偏好（preferences）、决策（decisions）、修复（fixes）和已安装的 agent 配置（installed agent setup），供下次会话使用[^src-2]。Solo 层的数据类型被明确标注为三类：skills、decisions、installs[^src-3]。

**Team 层（团队共享）**：当队友加入后，经审批的工作流成为带作者归属的共享技能（shared skills with authors）[^src-4]。团队成员通过同一 group code 加入，即刻开始共享记忆[^src-5]。团队层增加了审批门控——只有被认为值得复用的工作流才进入共享空间，并保留作者信息[^src-6]。

**Proof 层（复用证明）**：系统追踪复用收据（reuse receipts）和结果（outcomes），为技能的实际价值提供可验证证据[^src-7]。

该三层递进模型的核心设计意图是**复合效应**（compounding）：个人决策和技能在团队层面被复用后产生价值倍增，而复用证明又为技能的持续维护提供数据支撑[^src-8]。这与 Wen & Ku 的知识复利理论在结论上趋同——两者都主张持久化知识层的价值随使用次数和时间递增——但本卡描述的是产品架构层面的渐进部署策略，而非经济学建模[^card-1]。

材料未详述 solo 层与 team 层的数据隔离机制（哪些个人记忆可升级为团队技能、哪些始终保持私有），也未说明 group code 的权限粒度（是否支持只读/只写分离）。

## Footnotes

[^card-1]: [知识复利效应](knowledge-compounding.md) -- 本卡描述产品架构层面的渐进扩展路径，该卡从经济学角度建模知识复利的 H(t) 凹饱和曲线，两者从不同视角论证了持久化知识的累积价值

[^src-1]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- product demo section -- "Start with one personal memory for your agent. When teammates join, approved skills, decisions, and outcomes compound into a team brain every agent can reuse."
[^src-2]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- "For individuals" section -- "Personal Cognition keeps your preferences, decisions, fixes, and installed agent setup in reach for the next session."
[^src-3]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- solo section -- "skills, decisions, installs"
[^src-4]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- team section -- "shared skills with authors"
[^src-5]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- "Group-code setup" section -- "One teammate creates the group. Everyone else joins with the same code and starts sharing memory."
[^src-6]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- "For organizations" section -- "Teams approve the workflows worth reusing, keep author attribution, and let every agent ask the brain before guessing."
[^src-7]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- proof section -- "reuse receipts and outcomes"
[^src-8]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- product demo section -- "approved skills, decisions, and outcomes compound into a team brain every agent can reuse"
