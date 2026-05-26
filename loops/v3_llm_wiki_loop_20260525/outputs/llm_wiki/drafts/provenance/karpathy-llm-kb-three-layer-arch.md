---
schema: draft_card_provenance.v3
draft_card: ../cards/karpathy-llm-kb-three-layer-arch.md
material_id: developersio-jp-pattern
digest_id: digest_developersio-jp-pattern
source_paths:
  - data/raw/webpage/developersio-jp-pattern/text.txt
created_time: 2026-05-26T11:55:00+08:00
edited_time: 2026-05-26T11:55:00+08:00
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

本轮未运行。

## 备注

- 与 v2 `llm-knowledge-base-five-stage-workflow` 互补：五阶段是过程视角（ingest / IDE / Q&A / output / linting），本卡是结构视角（raw / schema / wiki）。两张可以在 related 中互链。
- 与 `aillm-wiki-four-defining-properties` 共同覆盖 Karpathy 模式的两侧叙事——技术结构 vs 用户属性。
