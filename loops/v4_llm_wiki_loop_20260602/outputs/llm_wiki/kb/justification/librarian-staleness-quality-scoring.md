---
schema: justification_journal.v1
card: ../cards/librarian-staleness-quality-scoring.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：Mode A extraction from repo source bundle
来源：`data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt`
源证据：
- FILE: claude-plugin/commands/librarian.md — 完整的 Scan Protocol（4 阶段 + Tier 1/Tier 2 升级逻辑 + checkpoint 崩溃恢复）
- FILE: AGENTS.md — "Staleness scoring (0-100): four dimensions at 25 points each" + "Quality scoring (0-100): four dimensions at 25 points each"
- FILE: AGENTS.md — "Librarian... Content-level wiki maintenance: staleness detection, quality scoring, factual verification, semantic coherence, deduplication"
范围论证：Librarian 的陈旧度/质量评分系统和两级扫描架构是完整的独立机制。已有的 parallel-multi-agent-research 卡覆盖研究流水线，thesis-driven-research 覆盖论点模式，但无卡覆盖 wiki 的维护/质量保障层面。continuous-drift-detection 卡是通用概念，本卡是其在 llm-wiki 中的具体实现实例。
