# User Insights Index

**Project**：jugo_jugo_llm_wiki

**Canonical Workspace**：/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/user-insights

**Coverage**：mixed

本文件是 session capture 的简短索引，不是 dream-mode aggregation。当前记录包含早期 LLM Wiki loop 0-1 设计会话，以及 Claude 中执行 v3 production/adoption 期间的用户纠偏、设计洞察和阶段结果。

| Date | Session | Current Understanding | Status | Detail |
| --- | --- | --- | --- | --- |
| 2026-05-25 | LLM Wiki Loop 0-1 设计会话 | 用户目标是用 skills + loop 自治生成 LLM Wiki KB；当前阶段重点是 bottom-up 生长经过 provenance 做实的 atomic card，main-agent 应作为控制面而不是具体生产者。 | captured, not aggregated | [session_log](sessions/session_20260525_llm_wiki_loop_bootstrap/session_log.md) |
| 2026-05-27 | Claude v3 执行会话 | v3 已从 draft/interlink 阶段推进到 adoption complete / candidate_ready；用户在 Claude 中明确了中文主语言、全文读取、批量处理全部材料、interlink 前置，以及 related 应从 footnotes/citation graph 派生而不是单独手工维护。 | captured, not aggregated | [session_log](sessions/session_20260527_claude_v3_execution/session_log.md) |

## Coverage And Scope

- `coverage: mixed`：2026-05-25 记录基于可见原始用户输入与 compact handoff；2026-05-27 Claude v3 记录基于本地 Claude JSONL session files 和 memory files。
- `scope: project`：记录主要服务于当前 LLM Wiki KB loop 的设计、运行和后续审计。
- `sensitivity: normal`：未记录凭证、客户数据或需要脱敏的私密内容。
- `doc_folder_sync: manual_update_completed`：相关洞察已同步到 `docs/llm_wiki_practice_reframe/` 的 notes、outline 和 final doc。
