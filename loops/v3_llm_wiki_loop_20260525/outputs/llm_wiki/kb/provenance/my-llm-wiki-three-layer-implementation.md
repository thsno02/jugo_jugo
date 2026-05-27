---
schema: accepted_card_provenance.v3
card: ../cards/my-llm-wiki-three-layer-implementation.md
material_id: pypi-my-llm-wiki
digest_id: digest_pypi-my-llm-wiki
source_paths:
  - data/raw/pypi/pypi-my-llm-wiki/text.txt
draft_card: ../../drafts/cards/my-llm-wiki-three-layer-implementation.md
draft_provenance: ../../drafts/provenance/my-llm-wiki-three-layer-implementation.md
similarity_result: ../../drafts/similarity/my-llm-wiki-three-layer-implementation.json
comparison_provenance: ../../drafts/comparison/my-llm-wiki-three-layer-implementation.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:06:00+08:00
  gate_notes: 6/6 项通过；CLI 命令与 SHA256 缓存有 PyPI 页 verbatim 源。
created_time: 2026-05-26T14:45:00+08:00
edited_time: 2026-05-27T15:06:00+08:00
edited_entity: llm
---

## 源证据

- 第 27-32 行：包元数据（my-llm-wiki 0.9.0，Apr 28 2026）。
- 第 34 行：包描述 "Turn any folder into a queryable knowledge graph. Inspired by Andrej Karpathy's LLM Wiki concept."
- 第 56 行（License: MIT）/ 第 59 行（Author: phuc-nt）/ 第 63 行（Python ≥3.10）。
- 第 100 行：Karpathy 三层概念 + "compile once, query forever" 完整原文。
- 第 102-104 行：安装与命令实例、SHA256 缓存、写回命令。
- 第 108-115 行：支持文件类型列表 + 各扩展的依赖说明（Docling, vision OCR via /wiki .）。

## 卡片范围是否成立

- 三层映射、SHA256 缓存、`llm-wiki note` 子命令、Obsidian vault 输出全部直接引自 PyPI 页面正文。
- "compile once, query forever"是 PyPI 页面引述的 Karpathy 原话。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:06:00+08:00
- 检查要点：
  - 三层落地 + 设计点 + 边界 3 节。
  - 知识密度足；非标题复述。
  - 源支撑：PyPI 页正文行号 verbatim 引用。
  - References + Footnotes 双在；Footnotes 2 条 verbatim。
  - frontmatter 完整；related 含 6 张邻接卡。

## 备注

- 与 anthemcreation-en-guide 的 Karpathy LLM wiki 卡可能在概念域上有重叠（同样讲三层架构）；本卡聚焦"具体工具实现"，与之互补。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/my-llm-wiki-three-layer-implementation.md`
- draft provenance: `../../drafts/provenance/my-llm-wiki-three-layer-implementation.md`
- similarity: `../../drafts/similarity/my-llm-wiki-three-layer-implementation.json`
- comparison provenance: `../../drafts/comparison/my-llm-wiki-three-layer-implementation.md`
