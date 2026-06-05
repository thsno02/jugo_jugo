---
schema: justification_journal.v1
card: ../cards/rag-evaluation-meta-evaluation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`
源证据：
- sections/experiments.tex, Meta Evaluation -- 元评估方法论完整描述
- tables/human_eval_selected.tex -- RAGChecker vs 基线的相关性对比
- tables/human_eval_full.tex -- 13 个指标的完整相关性结果
范围论证：元评估方法论不仅验证了 RAGChecker 自身的有效性，也为 RAG 评估指标的可靠性验证提供了可复用的范式——构建成对人类偏好数据集并计算与自动指标的相关性。
