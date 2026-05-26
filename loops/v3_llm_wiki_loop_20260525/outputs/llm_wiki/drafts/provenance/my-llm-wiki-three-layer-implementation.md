---
schema: draft_card_provenance.v3
draft_card: ../cards/my-llm-wiki-three-layer-implementation.md
material_id: pypi-my-llm-wiki
digest_id: digest_pypi-my-llm-wiki
source_paths:
  - data/raw/pypi/pypi-my-llm-wiki/text.txt
created_time: 2026-05-26T14:45:00+08:00
edited_time: 2026-05-26T14:45:00+08:00
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
- "compile once, query forever"是 PyPI 页面引述的 Karpathy 原话，属于"对源材料的逐字引用"。

## 发表门控结果

本轮未运行。

## 备注

- 与 anthemcreation-en-guide 的 Karpathy LLM wiki 卡可能在概念域上有重叠（同样讲三层架构）；本卡聚焦"具体工具实现"，应可与之互补，comparison_provenance 阶段确认。
