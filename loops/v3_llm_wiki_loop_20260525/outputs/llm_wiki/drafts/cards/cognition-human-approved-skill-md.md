---
id: cognition-human-approved-skill-md
title: SKILL.md 写入闸门：人工审批作为团队级 agent 记忆的第一道安全机制
status: draft
card_type: operational_rule
tags: [#agent-memory, #governance, #human-in-the-loop, #cognition]
created_time: 2026-05-26T12:05:00+08:00
edited_time: 2026-05-26T12:05:00+08:00
edited_entity: llm
source_ids: [cognitionus-llm-wiki-guide]
provenance_card: ../provenance/cognition-human-approved-skill-md.md
aliases: [SKILL.md gate, confirm-first capture, human approval before group save]
related: [cognition-skill-loop-evidence-to-teaching, llm-wiki-schema-is-most-important, robin-cartier-schema-as-product-doc, idea-file-as-agent-era-artifact, microsoft-agent-governance-eight-packages]
---

## 规则

Cognition 把"agent 把一次成功操作沉淀为团队可用技能"的过程切成**两个不对称阶段**：

1. **草稿阶段（自动）**：Cognition 在 agent 完成任务后自动起草一份 `SKILL.md`，记录步骤、检查项、失败模式、作者归属、当前状态（如 `awaiting approval`）。
2. **保存阶段（人审）**：草稿**不直接进**团队共享库。系统等待原作者**显式的人工 yes**——页面用 "Cognition drafts skills and waits for explicit approval before saving anything to the group" 表达。

只有审批通过的 SKILL.md 才会进入团队 brain，被其他 agent 检索到。

## 为什么需要这一闸门

页面虽未展开论证，但从描述能读出 3 个设计动机：

- **避免私域数据外溢**：agent 可能在解决问题时接触到只属于个人或某次会话的敏感信息，自动写库会污染团队空间。
- **避免错误模式被复制**：某次"碰巧 work"的修复未必是正确思路；人审让原作者**对自己的判断负责**，把"成功一次"与"值得教别人"分开。
- **保留作者归属**：审批的同一动作把"作者：Alice"绑定到 SKILL，使后续团队检索时能跟随**具体作者的品味**（页面：person-specific retrieval）。

## 与 RAG/通用文档库的差别

- 通用文档库：写入是开放的，治理靠事后审计；
- Cognition 的 SKILL.md：写入是**封闭的**（默认不入库），治理靠**事前人审**——把"团队 brain"看作高信任度面，刻意拒绝"反正先存着"的累积逻辑。

## 与"自动巩固"派的张力

`arxiv-memory-as-metabolism` 描述的 CONSOLIDATE 是**调度自动**的：低 cohesion 隔离、高 cohesion 直接整合，无须人工介入。Cognition 的立场可以看成另一极端——**所有进入共享空间的条目都过人审**，把整合责任交回人。两种立场没有谁更对，但分别假设了不同信任模型：

- 自动 CONSOLIDATE 适合**单用户 companion**（用户即审者，承担自己 wiki 的所有后果）；
- 人审 SKILL.md 适合**多用户 team brain**（一条错误的共享技能可能误导整组，所以写入门槛抬高）。

## 实施约束（页面可见的）

- 草稿生成是 LLM 任务，输出固定为 SKILL.md 格式；
- 审批是单人动作（页面：作者本人，不是团队投票或 PR review）；
- group-code 协议：一个队员创建 group，其他人用同 code 加入后才能看到对方的 SKILL.md（这意味着写入边界也是显式邀请边界）。

## References

- 来源页面：`data/raw/webpage/cognitionus-llm-wiki-guide/text.txt`。
- 第 79–92 行（DRAFT SKILL 步）。
- 第 135–137 行（Confirm-first capture）。
- 第 140–141 行（Person-specific retrieval）。
- 第 143–145 行（Group-code setup）。

## Footnotes

[^1]: 起草 + 等待人审 verbatim（第 92 行）："Cognition drafts the SKILL.md and waits for a human yes before sharing it."

[^2]: Confirm-first capture verbatim（第 136 行）："Cognition drafts skills and waits for explicit approval before saving anything to the group."

[^3]: Group-code 写入边界与邀请边界绑定 verbatim（第 144 行）："One teammate creates the group. Everyone else joins with the same code and starts sharing memory."
