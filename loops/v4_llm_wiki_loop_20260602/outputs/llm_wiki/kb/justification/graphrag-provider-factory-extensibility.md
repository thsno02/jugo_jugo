---
schema: justification_journal.v1
card: ../cards/graphrag-provider-factory-extensibility.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：从 repo-microsoft-graphrag material_bundle.txt 提取实现细节
来源：`data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt`
源证据：
- docs/index/architecture.md — 七大工厂子系统列表与描述
- docs/index/architecture.md — "All of these factories allow you to register an impl using any string name you would like, even overriding built-in ones directly"
- docs/config/models.md — Model Protocol 自定义模型注册示例代码
范围论证：工厂模式可扩展架构是 GraphRAG 作为研究平台的关键设计决策，与具体的管线步骤（六阶段卡）和配置系统（CLI 卡）形成架构-管线-配置三层互补。
