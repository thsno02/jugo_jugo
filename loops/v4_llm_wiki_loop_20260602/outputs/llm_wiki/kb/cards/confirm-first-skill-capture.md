---
id: confirm-first-skill-capture
title: 确认优先的技能捕获规则
status: accepted
card_type: operational_rule
tags: [agent-memory, human-approval, skill-sharing, team-memory, gating]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [cognitionus-llm-wiki-guide]
justification: ../justification/confirm-first-skill-capture.md
canonical_concept: confirm-first-skill-capture
aliases: [确认优先捕获, confirm-first capture, 人工审批门控, human-gated skill sharing]
summary: >-
  confirm-first-skill-capture（确认优先捕获 / confirm-first capture / 人工审批门控）Cognition 的设计规则：系统自动起草技能文档（SKILL.md），但必须等待人类明确批准后才保存到团队共享空间，防止未经审核的工作流污染团队知识库
related: [human-llm-role-division, review-involvement-spectrum]
---

Cognition 采用**确认优先**（confirm-first）模式处理团队技能共享：系统起草技能文档并等待人类的明确批准，在此之前不会将任何内容保存到团队共享空间[^src-1]。

具体流程：当 agent 完成一项工作后，Cognition 将命令、文件编辑、卡点和结果捕获为可复用工作流的证据[^src-2]，然后自动起草 SKILL.md 文件，标记状态为「awaiting approval」，标注作者，并提示人类决定是否批准该技能供团队使用[^src-3]。

该规则的设计意图是在自动化捕获与质量控制之间取得平衡：agent 负责从工作痕迹中提炼技能草稿（降低人类的文档编写负担），人类负责决定哪些工作流值得复用（保持团队知识库的信噪比）[^src-4]。

材料未讨论批准的粒度（是逐条技能还是批量审批）、拒绝后的处理流程、以及随着技能数量增长审批负担是否会成为瓶颈。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Confirm-first capture" section -- "Cognition drafts skills and waits for explicit approval before saving anything to the group."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Capture work" step -- "Commands, file edits, stuck points, and outcomes become evidence for a reusable workflow."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Save skills" step -- "Cognition drafts the SKILL.md and waits for a human yes before sharing it."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "For organizations" section -- "Teams approve the workflows worth reusing, keep author attribution, and let every agent ask the brain before guessing."
