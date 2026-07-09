---
id: llm-wiki-librarian-quality-scoring
title: Librarian 陈旧度与质量评分
status: draft
card_type: mechanism
tags: [llm-wiki, librarian, quality-scoring, staleness, two-tier-scan]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-librarian-quality-scoring.md
canonical_concept: librarian-quality-scoring
aliases: [librarian, staleness scoring, quality assessment, 图书管理员评分]
summary: >-
  librarian-quality-scoring 机制：为每篇文章评分陈旧度 staleness 和质量 quality，两层扫描（快速元数据检查 + 对标记文章深度内容读取），支持检查点恢复 checkpoint recovery，输出机器可读 JSON 加人类可读报告
related: [llm-wiki-audit-trust-verification, llm-wiki-compilation-process]
---

llm-wiki 的 librarian 功能对每篇文章进行陈旧度（staleness）和质量（quality）评分，采用两层扫描策略：首先快速元数据检查，然后对标记的文章执行深度内容读取。[^src-1]

该功能支持检查点恢复（checkpoint recovery），产出机器可读 JSON 和人类可读报告两种格式。可通过 --article <path> 对单篇文章执行。[^src-2]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Librarian" P35 -- "Score every article for staleness and quality. Two-tier scan: fast metadata check, then deep content read for flagged articles."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Librarian" P35 -- "Checkpoint recovery. Machine-readable JSON + human-readable report."
