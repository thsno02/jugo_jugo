---
id: deterministic-gap-mapping
title: 确定性知识缺口映射与提升
status: accepted
card_type: mechanism
tags:
- gap-mapping
- knowledge-growth
- promotion
- wiki
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- clawhub-llm-wiki-karpathy
evidence_basis: documentation
justification: ../justification/deterministic-gap-mapping.md
canonical_concept: deterministic-gap-mapping
aliases:
- kb_map_gaps
- kb_promote_gap
- gap mapping
- gap promotion
- 知识缺口映射
summary: deterministic-gap-mapping 确定性知识缺口映射通过 kb_map_gaps 发现 wiki 中的知识空白， kb_promote_gap
  将缺口提升为正式 derived note（concept/entity/synthesis）， 覆盖 ingest 层之上的 durable knowledge
  growth。
related:
- lint-as-quality-driver
- kb-lint-deterministic-validation
- knowledge-compilation-paradigm
---

## 确定性知识缺口映射与提升

llm-wiki-karpathy 提供确定性的知识增长机制 [^src-1]：

- **`kb_map_gaps`**: 扫描当前 wiki 状态，识别知识缺口（接受 `--limit` 参数控制返回数量）
- **`kb_promote_gap`**: 将识别出的缺口提升为正式的 derived note（如 `--note-id synthesis-retrieval-vs-memory`）

这两个命令覆盖 ingest 层之上的 "durable knowledge growth"——即在源材料摄入完成后，持续发现并填补 wiki 的知识空白 [^src-2]。

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" P27 -- "deterministic gap mapping and promotion through kb_map_gaps and kb_promote_gap"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Runtime Philosophy" P119 -- "kb_map_gaps and kb_promote_gap still cover durable knowledge growth on top of that ingest layer"
[^card-2]: [[runtime-agent-responsibility-boundary]] — gap mapping 由 runtime 确定性执行，gap 填充由 agent 完成
