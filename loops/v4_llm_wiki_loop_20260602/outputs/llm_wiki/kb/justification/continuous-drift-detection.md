---
schema: justification_journal.v1
card: ../cards/continuous-drift-detection.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/falconer-enterprise-guide/text.txt`
源证据：
- "Stay current: health checks need to run automatically" 段 — "At the personal scale, that works well: one person sees the lint output and acts on it."
- "What an enterprise LLM wiki has to do differently" 段 — "The health check changes from on-demand to continuous."
- 同段 — "It runs as a background loop, surfacing flagged content on a schedule the team can act on (weekly review rather than quarterly audit)"
- 同段 — "the system needs to detect the contradiction, draft an update, and route it to the document owner for review"
范围论证：此卡提取文章关于企业级健康检查从个人按需模式向自动持续模式演化的机制。现有 lint-operation 卡描述的是个人 LLM Wiki 的巡检操作（用户触发、检查项列表），本卡补充企业规模下的实现变化：自动化触发、后台循环、所有权路由。两者是同一功能在不同规模下的不同实现。
