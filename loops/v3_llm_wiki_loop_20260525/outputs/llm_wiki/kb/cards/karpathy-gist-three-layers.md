---
id: karpathy-gist-three-layers
title: Karpathy gist 把 LLM Wiki 形式化成"raw / wiki / schema"三层，每层的所有权严格分离
status: accepted
card_type: distinction
tags: [#llm-wiki, #karpathy, #architecture, #schema]
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-28T10:20:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
provenance_card: ../provenance/karpathy-gist-three-layers.md
aliases: [LLM Wiki 三层架构, raw/wiki/schema separation, CLAUDE.md as schema]
related: [karpathy-gist-bookkeeping-burden, karpathy-gist-memex-connection, karpathy-llm-wiki-three-layers, karpathy-llm-kb-three-layer-arch, anthemcreation-llm-wiki-three-layer-architecture, robin-cartier-schema-as-product-doc, llm-wiki-schema-is-most-important]
---

Karpathy 在 2026 年 gist 里把"LLM Wiki"模式形式化成**三层结构 + 严格的所有权分离**[^v2-1]，这是它和"普通 RAG 上的笔记库"最关键的区别：

1. **Raw sources** — 你自己收集的源文档（文章、论文、图像、数据文件）。**immutable**。"LLM reads from them but never modifies them. This is your source of truth."[^src1]
2. **The wiki** — LLM 生成的 markdown 目录（摘要、实体页、概念页、对比页、总览、综合页）。**"The LLM owns this layer entirely."** 创建页面、随新源更新、维护交叉引用、保持一致性都是 LLM 的活；人类只读。[^src2]
3. **The schema** — 一份指挥 LLM 的文档（例如 Claude Code 的 `CLAUDE.md`，Codex 的 `AGENTS.md`）。**这是关键的配置文件**[^v3-1]——它告诉 LLM wiki 怎么组织、约定是什么、ingest/query/lint 时跟哪些工作流。"You and the LLM co-evolve this over time as you figure out what works for your domain."[^src3]

所有权分离的工程含义：
- 任何修改 raw 的动作都是错误——它破坏了"the source of truth"的不可变假设；
- 人写 wiki 也是错误（或至少不应主流化）——"You never (or rarely) write the wiki yourself"[^src4]。原因：人写的页面无法被 LLM 在下一次 ingest 时自动维护，会破坏交叉引用一致性；
- schema 是**人 + LLM 共同演进**的——它不是死的配置，而是"实验 → 改 schema → 更好的下次 ingest"的反馈环节。

为什么这种分层比"一个文件夹塞 markdown"更有结构：
- 它把"信息源 (raw) / 派生工件 (wiki) / 工作流契约 (schema)"分开，等价于软件项目中的"数据 / 编译产物 / 构建脚本"分离；
- 一旦 raw 是不可变的，wiki 任何时候都可以"重新 ingest 全部 raw 重生成"——这意味着 wiki 是**可重建的派生产物**，类似 build artifact，而不是源真相；
- schema 类比"代码"——它定义所有工作流，并且对所有未来会话稳定；这是为什么"schema-as-product-document"[^v3-2]的工程实践会出现。

边界：
- gist 自己强调"这文档故意是抽象的"——具体的目录结构、页面格式、工具选择都依赖具体领域，应由用户与 LLM 协作实例化；
- 三层不是强制的——可以根据规模简化，例如不需要单独的 schema 文件、不需要图像处理；
- 人始终可以编辑 wiki（git 仓库特性带来），但**默认不编辑**是为了让 LLM 维护成本接近零；如果人编辑频繁，所有权又混乱了。

## References

Karpathy 2026 LLM Wiki gist 的 "Architecture" 段落明确给出三层定义。

- 源路径：`data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`（行 27–33 "Architecture" 段的 raw/wiki/schema 三段定义；行 15 "You never (or rarely) write the wiki yourself"；行 75 "intentionally abstract"边界声明）。

## Footnotes

- Raw 不可变原文（行 29）："Raw sources — your curated collection of source documents. ... These are immutable — the LLM reads from them but never modifies them. This is your source of truth."
- Wiki 由 LLM 持有原文（行 31）："The wiki — a directory of LLM-generated markdown files. ... The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it."
- Schema 是关键配置（行 33）："The schema — a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured ... This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot."
- 不写 wiki 原文（行 15）："You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions."
