---
id: my-llm-wiki-three-layer-implementation
title: my-llm-wiki 把 Karpathy 三层架构落地成 Obsidian-vault 工具
status: accepted
card_type: example_pattern
tags: [#llm-wiki, #knowledge-graph, #karpathy]
created_time: 2026-05-26T14:45:00+08:00
edited_time: 2026-05-28T14:28:00+08:00
edited_entity: llm
source_ids: [pypi-my-llm-wiki]
provenance_card: ../provenance/my-llm-wiki-three-layer-implementation.md
aliases: [my-llm-wiki, llm-wiki CLI]
related: [my-llm-wiki-supported-source-types, karpathy-llm-wiki-source-executable-analogy, karpathy-gist-three-layers, anthemcreation-llm-wiki-three-layer-architecture, karpathy-llm-wiki-obsidian-plugin-overview, wicer-cegar-compile-evaluate-refine]
---

## 这个包做了什么

`my-llm-wiki`（PyPI 0.9.0，2026-04-28，作者 phuc-nt，MIT） [^src3] 是 Karpathy 4 月发布的 "LLM Wiki" 概念的开源 CLI 实现。它复现了 Karpathy 描述的三层结构 [^src1][^v3-1]：

1. **不可变的原始文件**（raw files）——用户放进的源文件夹，工具从不修改。
2. **编译后的 wiki**（compiled wiki）——输出到 `wiki-out/vault/`，是一个**可直接用 Obsidian 打开的 vault**，含交叉引用 `[[wikilinks]]`。
3. **schema / instruction**——告诉 LLM 如何维护这个 wiki。

用法极简：`pip install my-llm-wiki` → `cd your-project && llm-wiki .` [^src2]。重跑时用 SHA256 缓存跳过未变文件，因此可以增量编译。

## 设计中值得抓住的两点

- **"编译一次，查询多次"被实现成可重跑 + 缓存的命令行**：`llm-wiki .` 不是一次性脚本，而是把 raw 文件按 hash 跳过未变的，让 wiki 像增量构建一样长成"persistent, compounding artifact"。
- **`llm-wiki note "<insight>"` 子命令是从 Claude Code 会话写回 wiki 的入口**——让"和 LLM 聊出来的洞察"也能沉淀进同一张图 [^src2]，关闭"读"与"写"之间的环。这是 Karpathy 强调的"图随每次会话生长" [^v3-2]。

## 边界

- 输出是 Obsidian vault，对其他编辑器友好但 graph view 等高级功能依赖 Obsidian。
- Image / HEIC 等结构化抽取依赖"vision OCR via Claude Code agent mode (`/wiki .`)"，需要 Claude Code 运行环境，不是纯 CLI [^v3-3]。
- Docling、leiden、office 等多文档类型支持都是 extras，需要按需 `pip install 'my-llm-wiki[docling]'`。

## Footnotes

[^src1]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` — 第 100 行 verbatim："a personal knowledge system with three layers: raw files (never modified), a compiled wiki with cross-references, and a schema that tells the LLM how to maintain it. The key insight: compile once, query forever, and let the wiki grow with every session as a 'persistent, compounding artifact' rather than re-deriving knowledge on every query."
[^src2]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` — 第 102–104 行，三层落地命令；含 verbatim："`llm-wiki note '<insight>'` writes back from your Claude Code sessions so the graph compounds over time."
[^src3]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` — 第 27–65 行，PyPI 元数据（version 0.9.0 / Apr 28 2026 / MIT / phuc-nt / Python ≥3.10）。
[^v3-1]: [karpathy-gist-three-layers](karpathy-gist-three-layers.md) — Karpathy gist 的 raw / wiki / schema 三层形式化，是 my-llm-wiki 复现的设计原型。
[^v3-2]: [file-outputs-back-as-compounding-loop](file-outputs-back-as-compounding-loop.md) — "查询输出回写进 wiki 形成复利循环" 正是 `llm-wiki note` 子命令实现的工作流。
[^v3-3]: [my-llm-wiki-supported-source-types](my-llm-wiki-supported-source-types.md) — 三条源抽取管道（含图像通过 Claude Code agent mode `/wiki .` 完成 OCR）在该卡有完整描述。
