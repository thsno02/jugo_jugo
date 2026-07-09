---
schema: claude_code_evidence_map.v1
publish_status: sanitized
---

# Evidence Map

| Claim | Published Evidence | Evidence Role |
| --- | --- | --- |
| Claude Code loop 必须可冷启动 | `loops/v3_llm_wiki_loop_20260525/CLAUDE_CODE_HANDOFF.md` | execution contract |
| v3 从 demo 转向 batch production | `loops/v3_llm_wiki_loop_20260525/reports/loop_report.md` | state transition |
| v4 固化审计和治理方法 | `loops/v4_llm_wiki_loop_20260602/learnings/audit_methodology.md` | methodology |
| v5 使用显式 source routing | `loops/v5_llm_wiki_loop_20260612/tools/source_router.py` | mechanism |
| v5 使用 script-based governance | `loops/v5_llm_wiki_loop_20260612/tools/batch_link.py` and `loops/v5_llm_wiki_loop_20260612/tools/backward_backlink.py` | mechanism |
| v5 产出 477 active cards | `loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md` | outcome |
| v5 审计采用 FSJS | `loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_audit_methodology.md` | audit method |
| v5 存在信息密度退化 | `loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md` | failure analysis |
| 交互内容只发布摘要 | `user-insights/index.md` and `docs/process_provenance.md` | redaction policy |

## Local-Only Evidence

本地 Claude/Codex raw session 只用于人工或 agent 复核，不作为公开证据提交。公开证据以 repo 内文件和过程化 commit 为准。
