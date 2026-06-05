---
schema: justification_journal.v1
card: ../cards/dynamic-community-detection.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-zep/agent_source_bundle.txt`
源证据：
- Section 2.3 — "we employ a label propagation algorithm rather than the Leiden algorithm. This choice was influenced by label propagation's straightforward dynamic extension"
- Section 2.3 — "this dynamic updating strategy provides a practical heuristic that significantly reduces latency and LLM inference costs"
范围论证：动态社区检测是 Graphiti 在 GraphRAG 社区检测方案上的具体改进，涉及算法选择（标签传播 vs Leiden）和动态扩展策略，是一个可独立描述的工程机制。
