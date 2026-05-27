---
schema: accepted_card_provenance.v3
card: ../cards/my-llm-wiki-supported-source-types.md
material_id: pypi-my-llm-wiki
digest_id: digest_pypi-my-llm-wiki
source_paths:
  - data/raw/pypi/pypi-my-llm-wiki/text.txt
draft_card: ../../drafts/cards/my-llm-wiki-supported-source-types.md
draft_provenance: ../../drafts/provenance/my-llm-wiki-supported-source-types.md
similarity_result: ../../drafts/similarity/my-llm-wiki-supported-source-types.json
comparison_provenance: ../../drafts/comparison/my-llm-wiki-supported-source-types.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:04:00+08:00
  gate_notes: 6/6 项通过；三管道描述与 PyPI 页 verbatim 对应。
created_time: 2026-05-26T14:50:00+08:00
edited_time: 2026-05-27T15:04:00+08:00
edited_entity: llm
---

## 源证据

- 第 108-115 行：代码 / Markdown / 办公文档 / 图像四类的完整描述。
- 第 65 行：`Provides-Extra: pdf , leiden , office , docling , all , dev` 说明这些都是 optional extras。
- 第 100-104 行：再次确认 Karpathy 三层 + `llm-wiki .` 命令。

## 卡片范围是否成立

- 三条管道、Tree-sitter / Docling / vision OCR 的工具引用、EPUB zipfile 拆包、Bold-as-heading fallback、HEIC/PNG/JPG hub-node 模式，都是 PyPI 页面的逐条复述。
- "图像 OCR 必须依赖 Claude Code"是页面原文 "vision OCR via Claude Code agent mode (/wiki .)" 的直接含义，不是引申。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:04:00+08:00
- 检查要点：
  - 三管道分述 + 值得抓住的 3 点。
  - 知识密度足；非标题复述。
  - 源支撑：第 108–115 行 verbatim + Provides-Extra。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含 5 张邻接卡。

## 备注

- 与 my-llm-wiki-three-layer-implementation 卡互补：三层卡谈架构，本卡谈源类型；不应合并。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/my-llm-wiki-supported-source-types.md`
- draft provenance: `../../drafts/provenance/my-llm-wiki-supported-source-types.md`
- similarity: `../../drafts/similarity/my-llm-wiki-supported-source-types.json`
- comparison provenance: `../../drafts/comparison/my-llm-wiki-supported-source-types.md`
