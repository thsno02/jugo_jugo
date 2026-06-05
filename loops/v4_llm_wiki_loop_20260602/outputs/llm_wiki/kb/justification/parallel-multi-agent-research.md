---
schema: justification_journal.v1
card: ../cards/parallel-multi-agent-research.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/llm-wiki-net/text.txt`
源证据：
- L20-22 — "5-10 parallel agents search academic, technical, applied, news, and contrarian angles."
- L285-286 — "5 agents (8 with --deep, 10 with --retardmax) search simultaneously from different angles — 2-3 web searches each, full-content fetch, quality scoring (1-5). A credibility pass deduplicates before ingestion."
- L293-296 — "After each round, you see what's covered, what's still missing, and suggested follow-ups... Add --min-time 2h to keep researching in rounds"
- L351-356 — "--plan decomposes your research into independent paths and runs them all in parallel"
范围论证：并行多智能体研究是 nvk 实现的核心机制，涵盖智能体数量/角度/可信度去重/缺口迭代/路径分解，构成一个完整的原子概念。与已有卡片（llm-wiki-pattern 描述模式、ingest-operation 描述单次摄入）互补但不重叠。
