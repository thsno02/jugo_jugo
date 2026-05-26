---
schema: draft_card_provenance.v3
draft_card: ../cards/karpathy-gist-three-layers.md
material_id: karpathy-gist-llm-wiki
digest_id: digest_karpathy-gist-llm-wiki
source_paths:
  - data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-26T11:45:00+08:00
edited_entity: llm
---

## 源证据

- 行 27 "## Architecture"：开始三层架构正式段。
- 行 29："Raw sources — your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them. This is your source of truth."
- 行 31："The wiki — a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely."
- 行 33："The schema — a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file"
- 行 15："You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it."
- 行 75："This document is intentionally abstract. It describes the idea, not a specific implementation."

## 卡片范围是否成立

本卡只聚焦"三层架构 + 所有权分离"，独立于已有的 launch-post 五阶段工作流卡。Gist 的"Architecture"段比 launch-post 推文更系统、更显式地给出三层定义，因此存在新增价值。所有主张直接来自 Architecture 段；"raw 不可变意味 wiki 可重建"是把 raw immutable 与 LLM 拥有 wiki 这两条原文结合的合理推论。

## 发表门控结果

本轮未运行。

## 备注

- 与 v3 已有 idea-file-as-agent-era-artifact / llm-knowledge-base-five-stage-workflow / auto-index-replaces-rag-at-small-scale / file-outputs-back-as-compounding-loop（均来自 launch-post）主题相邻：本卡作为 gist 视角补充。Comparison 阶段需评估"是否合并为统一 LLM Wiki 架构卡"。
