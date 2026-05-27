---
schema: accepted_card_provenance.v3
card: ../cards/karpathy-llm-kb-three-operations.md
material_id: developersio-jp-pattern
digest_id: digest_developersio-jp-pattern
source_paths:
  - data/raw/webpage/developersio-jp-pattern/text.txt
draft_card: ../../drafts/cards/karpathy-llm-kb-three-operations.md
draft_provenance: ../../drafts/provenance/karpathy-llm-kb-three-operations.md
similarity_result: ../../drafts/similarity/karpathy-llm-kb-three-operations.json
comparison_provenance: ../../drafts/comparison/karpathy-llm-kb-three-operations.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:15:00+08:00
  gate_notes: 6/6 项通过：三操作定义 + 不可替代性 + 操作含义 + 边界，证据锚 developersio L54-66 / L101 / L109。
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-27T10:15:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:15:00+08:00
- 检查要点：
  - 非标题复述：以三操作 + 各自不可替代性 + 操作含义 + 边界与误读四段实质展开。
  - 知识密度：Ingest=integration / Query+filing back 反直觉 / Lint 可持续性。
  - 源支撑：日文二次源 L58 / L60 / L62 / L66 / L101 / L109。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 6 个 v3 draft id。

## 备注

- 与 v2 `llm-knowledge-base-five-stage-workflow` 高度互补但不重复：五阶段是"ingest / IDE / Q&A / output / linting"五分法，本卡是 Karpathy gist 里更原始的"ingest / query / lint"三操作。
- 与同批 `karpathy-llm-kb-three-layer-arch` 共同覆盖该来源；后续可考虑再切一张关于森茂"既有 Mem0 之上加 wiki 层"的实操卡。
- Adoption 阶段观察：与 v2 `llm-wiki-query-answer-writeback` 有真主题重叠但本卡是三操作合卡，不可降级为 provenance_delta；门控阶段可顺手把 developersio 源作为 v2 原子卡的额外引证候选（属 audit 工作面）。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/karpathy-llm-kb-three-operations.md`
- draft provenance: `../../drafts/provenance/karpathy-llm-kb-three-operations.md`
- similarity: `../../drafts/similarity/karpathy-llm-kb-three-operations.json`
- comparison provenance: `../../drafts/comparison/karpathy-llm-kb-three-operations.md`
