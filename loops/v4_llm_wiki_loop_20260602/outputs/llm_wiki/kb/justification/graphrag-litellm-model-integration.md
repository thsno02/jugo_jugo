---
schema: justification_journal.v1
card: ../cards/graphrag-litellm-model-integration.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：从 repo-microsoft-graphrag material_bundle.txt 提取实现细节
来源：`data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt`
源证据：
- docs/config/models.md — LiteLLM 集成说明、100+ models 支持、structured output 约束
- docs/config/models.md — o-series 推理模型适配（max_tokens -> prompted approach, logit_bias 移除）
- docs/config/yaml.md — retry/rate_limit/metrics 配置详情
- docs/config/models.md — proxy API 方案与 JSON 格式问题警告
范围论证：LiteLLM 集成策略与 o-series 适配是 GraphRAG 实现中模型层的核心决策，影响用户的模型选择和成本优化。与工厂模式卡描述的自定义模型注入形成互补（LiteLLM 是内置默认，自定义 Protocol 是高级扩展）。
