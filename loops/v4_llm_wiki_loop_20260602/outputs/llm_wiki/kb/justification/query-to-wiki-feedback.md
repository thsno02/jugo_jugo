---
card_id: query-to-wiki-feedback
decision: accepted
confidence: high
---

## 提取理由

源材料明确列出三个相关特性：Query-to-Wiki Feedback（对话保存 + 实体提取 + 语义去重）和 Duplicate Save Prevention（哈希追踪防止重复评估）。这构成了一个完整的反馈回路机制——将 Wiki 从单向知识流（源 -> Wiki）扩展为双向知识流（源 -> Wiki <-> 查询对话）。这是现有卡未覆盖的独立知识点。

## 与已有卡的区分

- `obsidian-karpathy-wiki-plugin`: 该卡概览性提及六大命令中的 Query，但未展开对话回写机制
- `full-context-anti-rag`: 该卡论证查询时用全上下文而非 RAG，本卡关注查询结果如何反哺 Wiki
- `alias-cross-language-dedup`: 该卡论述去重机制，本卡将其作为保存前去重的依赖引用

## 原子性判断

该卡聚焦单一洞察：查询对话可以反向写入 Wiki 形成闭环知识增长，包含提取 + 去重 + 幂等三个保障机制。
