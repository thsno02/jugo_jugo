---
schema: draft_card_provenance.v3
draft_card: ../cards/morishige-kb-compile-mem0-overlay.md
material_id: developersio-jp-pattern
digest_id: digest_developersio-jp-pattern
source_paths:
  - data/raw/webpage/developersio-jp-pattern/text.txt
created_time: 2026-05-26T12:05:00+08:00
edited_time: 2026-05-26T12:05:00+08:00
edited_entity: llm
---

## 源证据

- 既有 Mem0 + pgvector 设施（L91）：*"Mem0 による fact 抽出やベクター DB へのドキュメント蓄積、古くなった知識を整理する監査コマンドなど。"*
- 既有不足（L91）：*"人間が読める形で構造化されたドキュメント としては十分に整備できていませんでした。"*
- 增量做法（L93）：*"既存のメモリ基盤の上に wiki 層を載せる形で /kb-compile というカスタムコマンドを作り、いま試しているところです。"*
- 目录结构（L97）。
- 三层映射（L99）。
- 命令选项（L101）：项目级 / 全量 / lint。
- `_index.md` 30 项目（L105、L107）。
- RAG vs wiki 互补判断（L83）。
- "hacky" 自评（L66、L109、L121）。
- 未完成项（L109）：*"手動でコマンドを叩かないと更新されない、プロジェクト横断のトピック記事にはまだ手をつけていない、Lint の自動実行も仕組み化できていない。"*

## 卡片范围是否成立

- 这是少见的"已有 Mem0 之上叠 wiki"的公开实践记录，对正在评估"要不要为 Karpathy 模式重建"的工程师特别有指导意义；适合作为 example_pattern 卡。
- 直接来自源材料：目录结构、命令选项、三层映射、未完成项、RAG vs wiki 互补判断。
- 引申：把"手动唤起 > 自动隐式"作为可复用判断——是对源材料"hacky"自评和未完成项的工程性总结，未越界。

## 发表门控结果

本轮未运行。

## 备注

- 本卡是该来源的"实操"卡，与同批的"三层架构"和"三操作"卡共同把概念 → 操作 → 落地三层覆盖完整。
- v2 无对应卡。后续 comparison 阶段如出现"Mem0"或"CLAUDE.md daily workflow" v2 卡，应交叉链接。
