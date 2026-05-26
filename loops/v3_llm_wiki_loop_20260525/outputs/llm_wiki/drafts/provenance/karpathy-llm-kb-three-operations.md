---
schema: draft_card_provenance.v3
draft_card: ../cards/karpathy-llm-kb-three-operations.md
material_id: developersio-jp-pattern
digest_id: digest_developersio-jp-pattern
source_paths:
  - data/raw/webpage/developersio-jp-pattern/text.txt
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 源证据

- 三操作定义（L54–62）：Ingest 是 "integration"、Query 含 "filing back"、Lint 是 health check。
- 关键日语原句：
  - L58：*"Ingest（取り込み） は、新しいソースを処理して wiki に統合する操作です。... 単なるインデックス化ではなく「統合」であることがポイントで、既存の知識と矛盾があればそれも解消されます。"*
  - L60：*"回答を新たなページとして wiki に「filing back」する ことで、自分の探索や質問がそのまま知識として蓄積されます。"*
  - L62：*"Lint（健全性チェック） は、wiki 全体に対するヘルスチェックです。"* + 引用 Karpathy 原句。
- Karpathy 自评（L66）：*"intentionally kept a little bit abstract/vague because there are so many directions to take this in"*。
- Karpathy 引用 Memex（L68）：*"Vannevar Bush が 1945 年に提唱した Memex（ドキュメント間の連想トレイルを辿る装置）を思い出します。"*
- 森茂 `/kb-compile --lint` 状态（L101、L109）。

## 卡片范围是否成立

- 三操作是 Karpathy 设计的"操作语义"层，独立成卡能配合三层架构卡形成"结构 + 行为"完整描述。
- 直接来自源材料：三操作定义、filing back 句、Lint 描述。
- 引申：把 Query 的 filing back 命名为"反直觉部分"、把三操作与 RAG 检索做对照——属于解读，但与森茂正文里的"RAG とどう違うのか"段一致，未越界。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 `llm-knowledge-base-five-stage-workflow` 高度互补但不重复：五阶段是"ingest / IDE / Q&A / output / linting"五分法，本卡是 Karpathy gist 里更原始的"ingest / query / lint"三操作；可在 related 中互链。
- 与同批 `karpathy-llm-kb-three-layer-arch` 共同覆盖该来源；后续可考虑再切一张关于森茂"既有 Mem0 之上加 wiki 层"的实操卡。
