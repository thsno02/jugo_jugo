---
id: research-session-crash-recovery
title: 研究会话注册与崩溃恢复
status: accepted
card_type: mechanism
tags: [llm-wiki, session, crash-recovery, provenance, research-state]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
justification: ../justification/research-session-crash-recovery.md
canonical_concept: research-session-crash-recovery
aliases: [会话注册, session registry, 崩溃恢复, research crash recovery, session provenance]
summary: >-
  research-session-crash-recovery（会话注册 / session registry / 崩溃恢复 / research crash recovery / session provenance）
  是 llm-wiki 多轮研究和论点会话的状态持久化机制：临时注册表支持中断恢复，
  持久化事件日志和检查点支持审计追溯，两层分离确保安全清理
related: [parallel-multi-agent-research, thesis-driven-research, audit-provenance-tracing]
---

llm-wiki 的多轮研究（`--min-time`）和论点模式产生长时间运行的会话。为了在崩溃、超时或用户中断后能恢复进度，系统维护**两层状态持久化**[^src-1]：

**第一层：临时会话注册表（ephemeral）**
- 位置：`<wiki-root>/.research-session.json`（研究）或 `.thesis-session.json`（论点）[^src-2]
- 内容：session_id、topic、mode、start_time、min_time_budget、current_round、paths 数组（含 status/sources_ingested）、rounds_completed 数组（含 gaps/progress_score）、cumulative_sources/articles、status[^src-3]
- 生命周期：研究开始时创建，每轮结束后更新，正常完成时删除[^src-4]

**第二层：持久化出处制品（durable provenance）**
- `.session-events.jsonl`：仅追加事件日志，支持可重放历史[^src-5]
- `.session-checkpoint.json`：最新紧凑摘要，用于恢复简报和审计[^src-6]
- 生命周期：正常完成后保留，不删除——为 `/wiki:audit` 提供可分类的出处[^src-7]

**恢复检测逻辑**[^src-8]：
1. 命令启动时检查 `.research-session.json` 是否存在且 `status: "in_progress"`
2. 如存在 → 读取已完成轮次和缺口，询问用户："Found interrupted session (Round N, M sources so far). Continue from Round N+1, or start fresh?"
3. 如选择继续 → 跳过 Phase 1，直接从上轮缺口作为起点开始下一轮
4. 如选择重新开始 → 删除临时注册表，从零开始

**陈旧会话检测**：如果注册表存在且 `status: "in_progress"` 但 `start_time` 超过 7 天前 → 警告 "Stale research session found. Clean up or delete manually."[^src-9]

**审计集成**：当 `/wiki:audit` 检查出处时，有 `.session-events.jsonl` 的会话被分类为 `replayable`，仅有注册表残留的被分类为 `partial`，无任何会话文件的被分类为 `missing`[^src-10]。

这种两层分离设计确保：临时层可安全删除（正常完成时自动删除），持久层不受干扰地保留审计追溯能力[^card-1]。进度评分（0-100）和终止判据（连续 3 轮下降 30+ 分、分数 >=80 无高优先缺口）内嵌于注册表驱动的轮次循环中[^card-2]。

## Footnotes

[^card-1]: [审计出处追踪](audit-provenance-tracing.md) -- 会话持久层为审计提供 replayable/partial/missing 三级出处分类
[^card-2]: [并行多智能体研究机制](parallel-multi-agent-research.md) -- 会话注册表驱动的进度评分和缺口迭代是多轮并行研究的状态骨架

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "create and maintain: an ephemeral session registry for crash recovery and round-to-round state; durable provenance artifacts for replayable audit trails and resume briefings"
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "Ephemeral location: <wiki-root>/.research-session.json"
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "Schema: {session_id, topic, mode, start_time, min_time_budget, current_round, paths: [...], rounds_completed: [...], cumulative_sources, cumulative_articles, status}"
[^src-4]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "On completion -> set status to completed, append research_completed... delete only .research-session.json"
[^src-5]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/skills/wiki-manager/SKILL.md -- ".session-events.jsonl — append-only event log for replayable history"
[^src-6]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/skills/wiki-manager/SKILL.md -- ".session-checkpoint.json — latest compact summary for resume briefings and audits"
[^src-7]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "Keep .session-events.jsonl and .session-checkpoint.json as durable provenance."
[^src-8]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "Resume detection: At command start, if .research-session.json exists with status: 'in_progress': Read the file... Ask: 'Found interrupted session (Round N, M sources so far). Continue from Round N+1, or start fresh?'"
[^src-9]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/skills/wiki-manager/SKILL.md -- "If a session file exists with status: 'in_progress' and start_time > 7 days ago -> warn: 'Stale research session found.'"
[^src-10]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/audit.md -- "Classify provenance as: replayable, partial, missing"
