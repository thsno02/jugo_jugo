---
id: karpathy-llm-kb-three-layer-arch
title: Karpathy "LLM Knowledge Base" 的三层架构：Raw / Schema / Wiki
status: accepted
card_type: concept
tags: [#llm-wiki, #karpathy, #architecture, #knowledge-system]
created_time: 2026-05-26T11:55:00+08:00
edited_time: 2026-05-27T14:40:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
provenance_card: ../provenance/karpathy-llm-kb-three-layer-arch.md
aliases: ["LLM KB 3-layer", "Raw / Schema / Wiki"]
related: [llm-knowledge-base-five-stage-workflow, aillm-wiki-four-defining-properties, karpathy-gist-three-layers, karpathy-llm-wiki-three-layers, anthemcreation-llm-wiki-three-layer-architecture, karpathy-llm-kb-three-operations, morishige-kb-compile-mem0-overlay]
---

DevelopersIO 上 Classmethod 工程师森茂洋整理的 Karpathy "LLM Knowledge Base" 概念结构，把它拆为三层，比五阶段工作流卡更接近**数据建模视角**：

- **Raw sources**：不可变的精选素材——文章、论文、仓库、图片。源语原话："記事、論文、リポジトリ、画像など、不変の精選ドキュメントです"。Web 文章通过 Obsidian Web Clipper 转 Markdown；相关图片也下载到本地以便 LLM 引用。
- **Schema**：定义 wiki 的结构与规约——分类法、命名规则、互链规则。"wiki の『設計図』"。在 Claude Code 实践里，schema 常常以分目录的 `CLAUDE.md` 形式存在。
- **Wiki**：LLM 编译出来的 markdown 文件群——raw 的 summary、概念实体页、互链 backlinks。森茂强调："人間が直接書くことはほとんどない という点"——人类几乎不直接写 wiki 层，wiki 是 LLM 的领域，人类负责 curation 与方向。

为什么这个三层划分值得记住：

- 它给"什么文件可以被人手编辑"画了清楚的边界——只有 raw 和 schema；wiki 是输出层，应当可重新编译。这避免了"人改一行 wiki 又被 LLM 覆盖"的常见迷惑。
- 它对应于现有 Claude Code / Obsidian 工作流的目录约定（如森茂的 `workspace/knowledge/` = Raw、各级 `CLAUDE.md` = Schema、`workspace/wiki/` = Wiki），不需要新工具就能落地。
- 它把 schema 与 wiki 显式分开，等于明确告诉工程师：**schema 是少量人工高密度产物，wiki 是大量自动低密度产物**，两者维护方式完全不同。

边界与误读：

- Karpathy 自己把整套设计称为 "hacky collection of scripts"，森茂也引用了这句；不要把三层结构当成完成态。
- 三层不是绝对——森茂自己的实践在 raw 和 wiki 之间另加了 Memory MCP（Mem0 + pgvector）作为"检索层"。三层是骨架，不是禁止扩展。
- "人不直接写 wiki"不是"人不可以编辑 wiki"——是"日常工作流不依赖人写 wiki"。bug 修补与紧急更正仍然合理。

## References

- 三层架构整段见 §"3 層アーキテクチャ"（`data/raw/webpage/developersio-jp-pattern/text.txt`，第 46–53 行）。
- 森茂自己的目录映射见 §"自分は Claude Code でこう組み込んでいる"（同文件 L85–99）。
- Karpathy 原贴日期与背景在 L23–28。

## Footnotes

- L48：*"Raw sources は、記事、論文、リポジトリ、画像など、不変の精選ドキュメントです。"*
- L50：*"Schema は、wiki の構造や規約を定義する設定ドキュメントです ... いわば wiki の『設計図』です。"*
- L52：*"Wiki は、LLM が生成した Markdown ファイル群です ... 重要なのは、人間が直接書くことはほとんどない という点。"*
- L97–99：森茂的目录映射 `workspace/knowledge/` → Raw、各 `CLAUDE.md` → Schema、`workspace/wiki/` → Wiki。
