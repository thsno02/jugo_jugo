---
schema: justification_journal.v1
card: ../cards/collection-adapter-architecture.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：Mode A extraction from repo source bundle
来源：`data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt`
源证据：
- FILE: claude-plugin/commands/ingest-collection.md — 完整文件：五种适配器实现细节（git shallow clone + blob SHA、mediawiki iterparse、API continuation、csv field inference、wayback CDX id_ replay）
- FILE: AGENTS.md — "Bulk-ingest bounded upstream corpora... Adapters: git, mediawiki-dump, mediawiki-api, csv-messages, wayback-cdx"
- FILE: claude-plugin/commands/ingest-collection.md — 共享流程（manifest + children 二层写入、三元组去重、500 门槛确认）
- FILE: claude-plugin/commands/ingest-collection.md — 编译指导（不为每个上游页面创建一篇文章）
范围论证：集合摄入适配器架构是 llm-wiki 处理大规模外部语料的专用子系统，涉及五种适配器的自动检测、共享的二层写入模式、去重不变量和编译策略指导。现有的 parallel-multi-agent-research 卡覆盖研究流水线，但集合摄入是一个独立入口（/wiki:ingest-collection），不经过研究智能体而是直接批量写入 raw 层。这是一个完整的独立架构值得单独记录。
