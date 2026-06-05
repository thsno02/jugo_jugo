---
id: gap-mapping-promotion
title: 缺口映射与晋升机制
status: accepted
card_type: mechanism
tags: [llm-wiki, knowledge-growth, gap-detection, wiki-maintenance]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
justification: ../justification/gap-mapping-promotion.md
canonical_concept: gap-mapping-promotion
aliases: [缺口映射, gap mapping, 缺口晋升, gap promotion, kb_map_gaps, kb_promote_gap]
summary: >-
  gap-mapping-promotion（缺口映射 / gap mapping / 缺口晋升 / kb_map_gaps / kb_promote_gap）llm-wiki-karpathy 运行时通过确定性缺口映射识别 wiki 覆盖空白，并将缺口晋升为一等笔记，实现持久知识增长
related: [ingest-operation, lint-operation]
---

llm-wiki-karpathy 运行时提供了一对确定性操作来驱动 wiki 的持久知识增长[^src-1]：

**kb_map_gaps**——扫描当前 wiki 状态，确定性地识别知识覆盖中的空白区域。支持通过 `--limit` 参数控制返回的缺口数量[^src-2]。

**kb_promote_gap**——将一个已识别的缺口晋升为一等 wiki 笔记（如综合笔记）。晋升后，该缺口不再是缺失的知识点，而成为 wiki 中的正式页面，可被其他页面链接和引用[^src-3]。

这一机制在摄入层之上运作：摄入操作处理新资料的进入，缺口映射与晋升则关注已有知识的系统性补全[^src-4]。两者共同构成 wiki 知识增长的双引擎——摄入是外部驱动（新资料触发），缺口晋升是内部驱动（已有知识结构自身暴露的不完整性）。

## Footnotes

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "What 0.4.4 Implements" -- "deterministic gap mapping and promotion through kb_map_gaps and kb_promote_gap"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "CLI Commands" -- "llm-wiki-karpathy kb_map_gaps --vault-root /vault --limit 10"
[^src-3]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "CLI Commands" -- "llm-wiki-karpathy kb_promote_gap --vault-root /vault --note-id synthesis-retrieval-vs-memory"
[^src-4]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "Runtime Philosophy" -- "kb_map_gaps and kb_promote_gap still cover durable knowledge growth on top of that ingest layer."
