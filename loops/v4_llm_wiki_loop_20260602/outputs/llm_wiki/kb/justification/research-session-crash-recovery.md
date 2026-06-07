---
schema: justification_journal.v1
card: ../cards/research-session-crash-recovery.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：Mode A extraction from repo source bundle
来源：`data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt`
源证据：
- FILE: claude-plugin/commands/research.md — "Multi-Round Session State" 完整章节：两层状态、schema 定义、lifecycle（create/update/complete/interrupt）、resume 检测逻辑
- FILE: claude-plugin/skills/wiki-manager/SKILL.md — ".session-events.jsonl — append-only event log for replayable history; .session-checkpoint.json — latest compact summary"
- FILE: claude-plugin/commands/audit.md — "Classify provenance as: replayable, partial, missing"
- FILE: claude-plugin/skills/wiki-manager/SKILL.md — "If a session file exists with status: 'in_progress' and start_time > 7 days ago -> warn"
范围论证：研究会话注册与崩溃恢复机制是 llm-wiki 支持长时间运行任务的关键基础设施。现有的 parallel-multi-agent-research 卡提到 "--min-time 可持续多轮迭代"但未展开状态持久化和恢复的具体实现。两层分离设计（临时 + 持久）、审计集成（replayable/partial/missing 分类）和陈旧会话检测构成一个完整的独立机制。
