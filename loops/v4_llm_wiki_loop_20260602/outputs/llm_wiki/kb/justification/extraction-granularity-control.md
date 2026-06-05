---
schema: justification_journal.v1
card: ../cards/extraction-granularity-control.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/obsidian-community-plugin/text.txt`
源证据：
- L240-249 — "Five options control how deeply the LLM extracts entities from sources: Fine (~100 items)... Standard (~50 items)... Coarse (~10 items)... Minimal (~5 items)... Custom (1-300 items)"
- L250 — "Recommendation: Use Minimal or Coarse for large folders to save time and API costs. Use Fine selectively on key documents that warrant deep analysis."
- L420-421 — "Choose 'Minimal', 'Coarse', or 'Standard' Extraction Granularity to reduce page count and save API costs."
范围论证：提取粒度是 Karpathy 原始 gist 未讨论的新概念；该插件将其参数化为五级控制，揭示了摄入操作中分析深度与成本的直接权衡，值得独立成卡
