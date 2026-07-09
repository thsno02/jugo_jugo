---
id: content-truncation-protection
title: 内容截断保护机制
status: accepted
card_type: mechanism
tags:
- llm-wiki
- error-handling
- max-tokens
- retry
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- obsidian-community-plugin
evidence_basis: documentation
justification: ../justification/content-truncation-protection.md
canonical_concept: content-truncation-protection
aliases:
- truncation protection
- 截断保护
- max_tokens detection
- stop_reason retry
summary: 内容截断保护：设置 8000 max_tokens 上限，自动检测 stop_reason，若因截断停止则以 2 倍 tokens 重试。跨所有 LLM 提供商统一实现。配合迭代批量提取消除长文档的 max_tokens 瓶颈。
related:
- parallel-page-generation
---

该插件实现内容截断保护机制，防止 LLM 输出因 token 限制而被截断：[^src-1]

- 设置 8000 max_tokens 上限
- 自动检测 stop_reason
- 若因截断（而非自然停止）而终止，则以 2 倍 tokens 重试
- 跨所有 LLM 提供商统一实现

此外，迭代批量提取（Iterative Batch Extraction）采用自适应批次大小，消除长文档的 max_tokens 瓶颈。[^src-2]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Content Truncation Protection — 8000 max_tokens with automatic stop_reason detection and retry at 2× tokens across all providers"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Iterative Batch Extraction — Adaptive batch sizing eliminates max_tokens bottleneck for long documents"
