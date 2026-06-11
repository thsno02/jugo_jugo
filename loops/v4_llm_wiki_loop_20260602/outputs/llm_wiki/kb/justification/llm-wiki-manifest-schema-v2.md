---
card_id: llm-wiki-manifest-schema-v2
decision: accept
---

## 为什么接受

1. **原子性**——本卡聚焦于 manifest schema v2 的五个新增字段及其在运行时操作中的作用，是一个独立的数据模型描述。
2. **信息密度**——源材料明确列出五个字段名称，并在多个上下文中说明其作用（编译就绪、源笔记验证、安全资产检查），适合以表格形式整理。
3. **无重复**——representation-first-ingest 卡提到 compile-readiness 状态但未展开清单字段；llm-wiki-vault-three-layer-shape 提到 manifest.json 文件但未展开 schema 内容。本卡填补了「数据模型层」的空白。
4. **可链接性**——schema v2 是理解 representation-first-ingest（如何判断 ready/partial/needs_representation）和 deterministic-lint（如何检测不一致）的底层数据基础。
