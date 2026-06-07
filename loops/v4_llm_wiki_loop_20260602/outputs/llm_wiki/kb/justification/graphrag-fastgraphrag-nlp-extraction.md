---
schema: justification_journal.v1
card: ../cards/graphrag-fastgraphrag-nlp-extraction.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：从 repo-microsoft-graphrag material_bundle.txt 提取实现细节
来源：`data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt`
源证据：
- docs/index/methods.md — FastGraphRAG 方法描述（NLP 替代 LLM 的具体步骤）
- docs/index/methods.md — "graph extraction to constitute roughly 75% of indexing cost"
- docs/config/yaml.md — extract_graph_nlp 配置参数（extractor_type, model_name 等）
- docs/index/methods.md — chunk size 50-100 tokens 建议
范围论证：FastGraphRAG 是 GraphRAG 开源项目独有的实现创新（论文中不存在），代表了 LLM-vs-NLP 混合索引策略的工程权衡，是独立的原子知识单元。
