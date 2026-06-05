---
schema: justification_journal.v1
card: ../cards/topic-isolation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt`
源证据：
- L142-144 — "Each research area is isolated. No cross-topic noise. Queries stay focused."
- L302-303 — "Topic wikis (~/wiki/topics/<name>/) are isolated research areas. Each has its own sources, articles, outputs, and Obsidian vault config."
- L172 — "query, output, and plan also accept --with <wiki> for cross-wiki context."
范围论证：主题隔离是 nvk 实现中的核心设计原则，与已有的 three-layer-architecture（描述 raw/wiki/schema 三层）互补——三层是垂直分层，主题隔离是水平分域。两者正交，各自成立。
