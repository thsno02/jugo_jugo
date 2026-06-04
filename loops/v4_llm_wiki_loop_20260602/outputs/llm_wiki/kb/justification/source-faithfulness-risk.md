---
schema: justification_journal.v1
card: ../cards/source-faithfulness-risk.md
created_time: 2026-06-04T22:45:00+08:00
---

## creation | 2026-06-04T22:45:00+08:00

生成方式：Mode A questioning loop, round 2-3 (Phase 3 — evaluative)
问题：wiki 经多轮迭代后如何防止偏离来源？有无内建验证机制？
来源：`data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`

源证据：
- "Architecture > Raw sources" — "These are immutable... This is your source of truth."
- "Operations > Lint" — "stale claims that newer sources have superseded"
- "The core idea" 第4段 — "I browse the results in real time"

范围论证：本卡聚焦知识漂移风险和不可变锚点机制。
lint 操作的完整检查项已有独立卡（lint-operation）。
