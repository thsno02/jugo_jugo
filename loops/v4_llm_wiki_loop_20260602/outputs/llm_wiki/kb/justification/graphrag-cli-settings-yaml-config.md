---
schema: justification_journal.v1
card: ../cards/graphrag-cli-settings-yaml-config.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：从 repo-microsoft-graphrag material_bundle.txt 提取实现细节
来源：`data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt`
源证据：
- docs/config/yaml.md — 完整 YAML 配置 section 定义（models, input, chunks, output, cache, vector_store, workflows）
- docs/config/init.md — graphrag init 命令生成 settings.yaml + .env + prompts/
- docs/get_started.md — CLI 使用 quickstart（init/index/query 命令）
- docs/config/models.md — 非对称模型配置示例
范围论证：描述 GraphRAG 的配置体系与 CLI 命令集，属于纯实现层信息。论文中未涉及配置细节，现有卡均不覆盖此内容。
