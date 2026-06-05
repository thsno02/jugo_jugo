---
id: archive-lifecycle
title: 主题归档生命周期
status: accepted
card_type: mechanism
tags: [llm-wiki, archive, lifecycle, topic-management]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/archive-lifecycle.md
canonical_concept: archive-lifecycle
aliases: [归档生命周期, archive lifecycle, 主题归档, topic archive]
summary: >-
  archive-lifecycle（归档生命周期 / archive lifecycle / 主题归档 / topic archive）是 LLM Wiki
  的主题生命周期机制：整个 topic wiki 移至 topics/.archive/，保留知识但默认静默，
  大多数工具自动跳过，需显式 --include-archived 才可读写
related: []
---

LLM Wiki 的归档机制作用于**整个 topic wiki** 而非单篇文章——将不再活跃的主题 wiki 移动到 `topics/.archive/` 下[^src-1]。

归档遵循**保留但静默（preserved but quiet）**原则[^src-2]：
- 来源、文章、产出和日志全部保留，保持结构可维护性
- 大多数工具默认跳过归档内容——query、compile、research、output、maintenance 都不触及[^src-3]
- 深度查询（deep query）可能浮出归档索引的线索[^src-4]
- 显式 `--include-archived` 标记是读写归档材料的唯一入口[^src-5]

归档操作是可逆的——`/wiki:archive restore <slug>` 可将归档主题恢复为活跃状态[^src-6]。`/wiki:archive peek <query>` 可搜索归档主题的索引而不读取文章正文[^src-7]。

这一机制解决的问题是：如何让旧兴趣退出日常上下文而不丢失已积累的知识[^src-8]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Archive" L40-42 -- "Move whole topic wikis to topics/.archive/. Preserved knowledge stays structurally maintainable but out of default query, compile, research, output, and maintenance context."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Archive is quiet" L162-164 -- "Archived topics live under topics/.archive/. Most tools skip them by default"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Archive-aware tools" L415-416 -- "Query, ingest, compile, research, output, inventory, dataset, project, lessons-learned, librarian, refresh, audit, lint, init, and routing now distinguish active material from explicitly included archived context."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Archive is quiet" L164 -- "deep queries may surface index hits"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Commands" L172 -- "Archived topic wikis are skipped by default; commands that support --include-archived require that explicit flag before reading or writing archived material."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Commands" L204 -- "/wiki:archive restore <slug> Restore an archived topic wiki to active status."
[^src-7]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Commands" L206 -- "/wiki:archive peek <query> Search archived topic indexes without reading archived article bodies."
[^src-8]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L313-314 -- "Archive (topics/.archive/) is for whole topic wikis the user no longer wants in normal context. It preserves source history, articles, outputs, and logs while keeping old interests quiet by default."
