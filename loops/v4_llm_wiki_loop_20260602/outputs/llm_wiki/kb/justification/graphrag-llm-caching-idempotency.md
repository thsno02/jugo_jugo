---
schema: justification_journal.v1
card: ../cards/graphrag-llm-caching-idempotency.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：从 repo-microsoft-graphrag material_bundle.txt 提取实现细节
来源：`data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt`
源证据：
- docs/index/architecture.md — LLM Caching 段落："a common setback when working with LLM APIs is various errors due to network latency, throttling"
- docs/index/architecture.md — "allows our indexer to be more resilient to network issues, to act idempotently"
- docs/config/yaml.md — cache 配置（type: json|memory|none, storage 后端）
范围论证：LLM 缓存幂等机制是 GraphRAG 实现中应对大规模索引任务的关键工程决策，论文未涉及此实现细节。作为独立的容错模式，与管线阶段卡和配置卡互补。
