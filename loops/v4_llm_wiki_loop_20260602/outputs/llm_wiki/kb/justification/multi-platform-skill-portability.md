---
schema: justification_journal.v1
card: ../cards/multi-platform-skill-portability.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/llm-wiki-net/text.txt`
源证据：
- L440-442 — "Five install modes... The behavioral logic lives in a single wiki-manager skill shared across runtimes — Codex, OpenCode, and Pi trees symlink into the Claude source of truth so there is no fork. Drift is caught by self-healing sync tests."
- L92-96 — "Pi's 1K system prompt leaves room for the full wiki skill on 32K context local models."
范围论证：多平台技能可移植性描述了 LLM Wiki 如何在不分叉代码的情况下支持五种运行时——这是一个独立的分发/架构机制，不同于零运行时依赖（描述技术约束）或主题隔离（描述数据组织）。
