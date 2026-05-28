---
id: karpathy-llm-kb-three-operations
title: Karpathy "LLM KB" 的三个操作：Ingest / Query / Lint，与 Query 的 "filing back"
status: accepted
card_type: mechanism
tags: [#llm-wiki, #karpathy, #operations, #knowledge-system]
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-28T11:13:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
provenance_card: ../provenance/karpathy-llm-kb-three-operations.md
aliases: ["LLM KB ingest query lint", "filing back"]
related: [karpathy-llm-kb-three-layer-arch, llm-knowledge-base-five-stage-workflow, llm-wiki-ingest-vs-query-workflow, file-outputs-back-as-compounding-loop, llm-wiki-karpathy-lint-grounding-trail, morishige-kb-compile-mem0-overlay]
---

森茂洋根据 Karpathy 的 gist 总结，Wiki 之上有三类操作：

- **Ingest（取り込み）**：处理新源并把它"统合"到 wiki。要点是这不是单纯的 indexing，而是 *integration*——LLM 读文档、写摘要、更新相关实体页、改写 `index.md`，并且**主动消解新旧知识的矛盾**[^src1]。
- **Query（質問）**：对 wiki 提问、得到回答。Karpathy 的关键设计是**把回答作为新页面 "filing back" 到 wiki**[^src2][^v3-1]——也就是说自己的每一次探索都直接变成持久知识，wiki 越用越富。
- **Lint（健全性チェック）**：对整个 wiki 做健康检查——发现矛盾、过时主张、孤页、断链，并提出修复建议[^v3-2]。Karpathy 原话被森茂引用："LLM は人間が退屈に感じる保守タスク——相互参照、一貫性チェック、統合の更新——を放棄しない"[^src3]。

三个操作各自的不可替代性：

1. Ingest 不是 RAG 检索：RAG 把"检索"推迟到查询时；Ingest 把"理解 + 编排"提前到入库时。这是 LLM Wiki 与传统 RAG 在系统形态上的最大分野——一个是**事前编译**，一个是**事后检索**。
2. **Query 的 filing back 是这套模式最反直觉的部分**。它意味着 query 不只是消费操作，而是写操作。一个"知识库"如果不把对话产物吸纳回去，就退化成 Wikipedia 浏览器；filing back 让 wiki 成为复利系统。
3. Lint 是模式可持续的关键。Karpathy 自己也强调这部分被低估——没有 Lint，ingest 越多越乱；做了 Lint，wiki 越大越值得查。

操作含义：

- 三个操作并不是任何"知识管理工具"都具备：Notion、Obsidian 默认只是 IDE；要变成 LLM KB 必须**显式实现** Ingest / Query / Lint 三个动作，通常以 slash command 或 cron 任务的形式。
- Query 的 filing back 工程上要注意"防止 wiki 被无意义的对话产物淹没"。可以用 schema 限定哪些 Query 配 filing、哪些只是即时回答。
- Lint 不必每次实时跑——Karpathy 的实践是周期性 health check（在五阶段卡里描述更细），森茂也说自己的 `/kb-compile --lint` 还未做到自动化。

边界与误读：

- Karpathy 自评 "intentionally kept a little bit abstract/vague because there are so many directions to take this in"[^src4]，三操作并非穷举；未来很可能扩展出"diff / publish / sync"等操作。
- "Ingest 解决矛盾"在小规模下可行，到一定规模 LLM 自身可能成为不一致来源；引用时不宜把这句当成保证。
- "Lint 让 LLM 处理人觉得无聊的事"是设计哲学，不是工程保证——Lint 本身需要被 audit。

## Footnotes

[^src1]: `data/raw/webpage/developersio-jp-pattern/text.txt` L58 — "Ingest（取り込み） は、新しいソースを処理して wiki に統合する操作です ... 単なるインデックス化ではなく「統合」であることがポイントで、既存の知識と矛盾があればそれも解消されます。"
[^src2]: 同文件 L60 — "回答を新たなページとして wiki に「filing back」する ことで、自分の探索や質問がそのまま知識として蓄積されます。"
[^src3]: 同文件 L62 — "LLM は人間が退屈に感じる保守タスク——相互参照、一貫性チェック、統合の更新——を放棄しない"
[^src4]: 同文件 L66 — "intentionally kept a little bit abstract/vague because there are so many directions to take this in"
[^v3-1]: [file-outputs-back-as-compounding-loop](file-outputs-back-as-compounding-loop.md) — "Query filing back" 的复利展开。
[^v3-2]: [llm-wiki-karpathy-lint-grounding-trail](llm-wiki-karpathy-lint-grounding-trail.md) — Lint 强制 grounding trail 的展开。
