---
card_id: llm-wiki-vault-three-layer-shape
decision: accept
---

## 为什么接受

1. **原子性**——本卡聚焦于 vault 的三层目录结构（raw/wiki/.llm-kb），这是一个独立的架构模式，不同于已有卡片覆盖的摄入路径（representation-first-ingest）或职责分工（runtime-agent-boundary）。
2. **信息密度**——源材料中 Default Vault Shape 部分提供了完整的目录树和每个子目录的用途，属于结构化数据，适合独立成卡。
3. **无重复**——现有三张卡均未详细描述目录结构。representation-first-ingest 提到 `.llm-kb/representations/` 但仅作为摄入流程的一步，未覆盖完整目录树和 wiki 子目录分区。
4. **可链接性**——该结构是理解其他操作（lint 检查孤立页面、gap mapping 产出归入哪个子目录）的前提知识。
