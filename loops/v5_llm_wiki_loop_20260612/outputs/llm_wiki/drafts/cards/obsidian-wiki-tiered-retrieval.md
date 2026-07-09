---
id: obsidian-wiki-tiered-retrieval
title: obsidian-wiki 分层检索策略
status: draft
card_type: implementation-mechanism
tags: [tiered-retrieval, wiki-query, index-pass, scalability]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-ar9av-obsidian-wiki]
evidence_basis: code_implementation
justification: ../justification/obsidian-wiki-tiered-retrieval.md
canonical_concept: tiered-retrieval-index-then-body
aliases: [tiered retrieval, wiki-query, index-only mode, cheap pass]
summary: >-
  obsidian-wiki 的 wiki-query 技能采用分层检索策略（tiered-retrieval-index-then-body）：
  先读取标题、tags 和 frontmatter summary 字段（cheap pass / index pass），
  仅当廉价通道无法回答时才打开页面正文。用户可说 "quick answer" 或 "just scan"
  强制 index-only 模式。使查询成本在 vault 从 20 页增长到 2000 页时保持大致平坦。
  可选集成 QMD 语义搜索实现 lex+vec 检索。
related: [obsidian-wiki-four-stage-pipeline, obsidian-wiki-compile-not-retrieve-pattern]
---

obsidian-wiki 的 `wiki-query` 技能实现了分层检索（tiered retrieval）策略[^src-1]：

**第一层（Index Pass）**：先读取 titles、tags 和 frontmatter 中的 `summary:` 字段。这是一个"廉价通道"（cheap pass），只需扫描元数据即可尝试回答查询[^src-2]。

**第二层（Body Pass）**：仅当 index pass 无法充分回答时，才打开相关页面的正文内容进行深入检索[^src-3]。

**强制 index-only 模式**：用户可说 "quick answer" 或 "just scan" 跳过 body pass，强制只使用索引[^src-4]。

**可扩展性**：该策略使查询成本在 vault 从 20 页增长到 2000 页时保持大致平坦[^src-5]。

**可选 QMD 语义搜索**：当配置了 `QMD_WIKI_COLLECTION` 时，query 先运行 lex+vec 语义 pass，再回退到 Grep；未配置时完全依赖 Grep/Glob 仍可正常工作[^src-6]。

[^card-1]: [obsidian-wiki-four-stage-pipeline] — Extract 阶段生成的 summary 字段正是 tiered retrieval 的 index pass 所依赖的数据
[^card-2]: [obsidian-wiki-compile-not-retrieve-pattern] — 分层检索是"编译式"知识消费端的效率保障

[^src-1]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "What we added on top of Karpathy's pattern" P12 -- "Tiered retrieval. wiki-query reads titles, tags, and page summaries first and only opens page bodies when the cheap pass can't answer."
[^src-2]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "What we added on top of Karpathy's pattern" P12 -- "wiki-query reads titles, tags, and page summaries first"
[^src-3]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "What we added on top of Karpathy's pattern" P12 -- "only opens page bodies when the cheap pass can't answer"
[^src-4]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "What we added on top of Karpathy's pattern" P12 -- "Say 'quick answer' or 'just scan' to force index-only mode."
[^src-5]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "What we added on top of Karpathy's pattern" P12 -- "Keeps query cost roughly flat as your vault grows from 20 pages to 2000."
[^src-6]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Optional: QMD Semantic Search" P2 -- "wiki-query runs a semantic pass (lex+vec) against your wiki collection before falling back to Grep."
