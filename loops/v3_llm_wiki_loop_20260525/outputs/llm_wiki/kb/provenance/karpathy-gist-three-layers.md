---
schema: accepted_card_provenance.v3
card: ../cards/karpathy-gist-three-layers.md
material_id: karpathy-gist-llm-wiki
digest_id: digest_karpathy-gist-llm-wiki
source_paths:
  - data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
draft_card: ../../drafts/cards/karpathy-gist-three-layers.md
draft_provenance: ../../drafts/provenance/karpathy-gist-three-layers.md
similarity_result: ../../drafts/similarity/karpathy-gist-three-layers.json
comparison_provenance: ../../drafts/comparison/karpathy-gist-three-layers.md
gate:
  type: fusion_audit
  result: passed
  decided_at: 2026-05-27T14:38:00+08:00
  gate_notes: 四项判据全部通过；draft 同源同段但抽取粒度从 v2 三张窄事实卡整合为 distinction 卡，并提供第 15 行（never write wiki yourself）与第 75 行（intentionally abstract）新行号证据 + 所有权分离 / wiki 可重建 / schema 共同演进三论点框架。
v2_anchor:
  card_id: llm-wiki-three-layer-architecture
  card_path: loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
  comparison_decision: provenance_delta
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-27T14:38:00+08:00
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

- 类型：fusion_audit
- 结果：passed
- 决定时间：2026-05-27T14:38:00+08:00
- 检查要点：
  - 三问被实质回答：comparison 明确 v2 三张同源窄卡（三层 / schema / wiki 层）与 draft 抽取自同一 Karpathy gist Architecture 段，draft 选择整合视角而非拆分粒度。
  - v2 anchor body 已读：v2 三层架构卡 statement「该来源把 LLM Wiki 架构分成三个层次：原始来源、wiki 和 schema」已与 draft "Raw / The wiki / The schema" 三段对照。
  - draft 不破坏 v2 scope：核心三层事实与 v2 一致；draft 加 (a) 第 15 行 "You never (or rarely) write the wiki yourself" 新行号证据、(b) 第 75 行 intentionally abstract 边界、(c) 所有权分离 / wiki 可重建 / schema 共同演进三论点框架——这些都在 v2 三张窄事实卡 References 与 statement 之外。
  - provenance 链可追溯：本文件显式记录 v2_anchor + comparison_provenance 路径。

## 备注

- 与 v3 已有 idea-file-as-agent-era-artifact / llm-knowledge-base-five-stage-workflow / auto-index-replaces-rag-at-small-scale / file-outputs-back-as-compounding-loop（均来自 launch-post）主题相邻：本卡作为 gist 视角补充。Comparison 阶段需评估"是否合并为统一 LLM Wiki 架构卡"。
- adoption 阶段观察：这是 batch 中唯一"同源同段，与多张 v2 卡同时高重合"的案例；v2 拆分粒度 vs v3 整合粒度的差异已记入 comparison 备注，是未来 reflection 的素材。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/karpathy-gist-three-layers.md`
- draft provenance: `../../drafts/provenance/karpathy-gist-three-layers.md`
- similarity: `../../drafts/similarity/karpathy-gist-three-layers.json`
- comparison provenance: `../../drafts/comparison/karpathy-gist-three-layers.md`
