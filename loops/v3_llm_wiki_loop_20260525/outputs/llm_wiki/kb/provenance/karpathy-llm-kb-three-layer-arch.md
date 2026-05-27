---
schema: accepted_card_provenance.v3
card: ../cards/karpathy-llm-kb-three-layer-arch.md
material_id: developersio-jp-pattern
digest_id: digest_developersio-jp-pattern
source_paths:
  - data/raw/webpage/developersio-jp-pattern/text.txt
draft_card: ../../drafts/cards/karpathy-llm-kb-three-layer-arch.md
draft_provenance: ../../drafts/provenance/karpathy-llm-kb-three-layer-arch.md
similarity_result: ../../drafts/similarity/karpathy-llm-kb-three-layer-arch.json
comparison_provenance: ../../drafts/comparison/karpathy-llm-kb-three-layer-arch.md
gate:
  type: fusion_audit
  result: passed
  decided_at: 2026-05-27T14:40:00+08:00
  gate_notes: 四项判据全部通过；draft 作为 DevelopersIO/森茂洋日文工程化解读，在 v2 三层架构卡 scope 外补充二次独立来源 + workspace 目录映射 + "schema 是高密度 / wiki 是低密度产物"工程含义 + Memory MCP 可扩展第四层与 hacky 自评等边界。
v2_anchor:
  card_id: llm-wiki-three-layer-architecture
  card_path: loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
  comparison_decision: provenance_delta
created_time: 2026-05-26T11:55:00+08:00
edited_time: 2026-05-27T14:40:00+08:00
edited_entity: llm
---

## 源证据

- 三层架构定义（L46–53）：Raw / Schema / Wiki 各自定义与人/LLM 分工。
- 关键原句（日语原文）：
  - L48：*"Raw sources は、記事、論文、リポジトリ、画像など、不変の精選ドキュメントです。"*
  - L50：*"Schema は、wiki の構造や規約を定義する設定ドキュメントです ... いわば wiki の『設計図』です。"*
  - L52：*"Wiki は、LLM が生成した Markdown ファイル群です ... 重要なのは、人間が直接書くことはほとんどない という点。"*
- Karpathy 原贴背景（L23–28）：*"2026 年 4 月 3 日、AI 研究者で「バイブコーディング（vibe coding）」の名付け親としても知られる Andrej Karpathy 氏が X のポスト で「LLM Knowledge Bases」と題した投稿をしました。"*
- 森茂目录映射（L97–99）：`workspace/knowledge/` / `CLAUDE.md` / `workspace/wiki/`。
- "hacky collection of scripts" 引用（L66、L121）。

## 卡片范围是否成立

- 三层架构是 Karpathy 概念在工程师视角下的二次抽象，独立成卡能为后续"工作流卡 / 三操作卡"提供共享底座。
- 直接来自源材料：三层定义、目录映射、Karpathy 自评。
- 引申主张已显式标注：人/工具分工的含义（如"wiki 是输出层"、"schema 是少量高密度产物"）属于对源材料的整理性解读，不是新主张。

## 发表门控结果

- 类型：fusion_audit
- 结果：passed
- 决定时间：2026-05-27T14:40:00+08:00
- 检查要点：
  - 三问被实质回答：comparison 明确 v2 三层架构卡（Karpathy gist 一手）与 draft（DevelopersIO 日文二次解读）共享三层事实，jaccard 0.500 是 batch 中最高。
  - v2 anchor body 已读：v2 卡 statement 与 draft 三层翻译对照，名称（Raw / Schema / Wiki）完全照搬。
  - draft 不破坏 v2 scope：核心三层划分与 v2 一致；draft 新加 (a) DevelopersIO 二次独立来源、(b) 森茂 workspace/knowledge / CLAUDE.md / workspace/wiki 目录映射、(c) "schema 是少量高密度、wiki 是大量低密度产物"工程含义、(d) "hacky collection of scripts" 自评与 Memory MCP 可扩展第四层等边界——均在 v2 紧致 scope 外。
  - provenance 链可追溯：本文件显式记录 v2_anchor + comparison_provenance 路径。

## 备注

- 与 v2 `llm-knowledge-base-five-stage-workflow` 互补：五阶段是过程视角（ingest / IDE / Q&A / output / linting），本卡是结构视角（raw / schema / wiki）。两张可以在 related 中互链。
- 与 `aillm-wiki-four-defining-properties` 共同覆盖 Karpathy 模式的两侧叙事——技术结构 vs 用户属性。
- adoption 阶段观察：draft 是 batch 内最高 jaccard 的"同事实新来源"案例，并存的工程价值在于把"概念事实"与"落地映射"分开承载。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/karpathy-llm-kb-three-layer-arch.md`
- draft provenance: `../../drafts/provenance/karpathy-llm-kb-three-layer-arch.md`
- similarity: `../../drafts/similarity/karpathy-llm-kb-three-layer-arch.json`
- comparison provenance: `../../drafts/comparison/karpathy-llm-kb-three-layer-arch.md`
