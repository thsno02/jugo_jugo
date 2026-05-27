---
schema: accepted_card_provenance.v3
card: ../cards/lightmem-complexity-formula.md
material_id: arxiv-lightmem
digest_id: digest_arxiv-lightmem
source_paths:
  - data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt
draft_card: ../../drafts/cards/lightmem-complexity-formula.md
draft_provenance: ../../drafts/provenance/lightmem-complexity-formula.md
similarity_result: ../../drafts/similarity/lightmem-complexity-formula.json
comparison_provenance: ../../drafts/comparison/lightmem-complexity-formula.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:29:00+08:00
  gate_notes: 6/6 项通过：复杂度对照表 + 三处来源拆解 + LongMemEval 实测对照 + r/th 边界。
created_time: 2026-05-26T15:11:00+08:00
edited_time: 2026-05-27T10:29:00+08:00
edited_entity: llm
---

## 源证据

- 行 989–1014（§Complexity analysis about LightMem，包含表 `tab:complexity_comparison`）：
  - Baselines 行："Baselines & $N(L_{\text{sum-in}} + T + L_{\text{sum-out}})$ & $NM_1R_1(L_{\text{up-in}} + L_{\text{up-out}})$ & $N$ & $O(N)$"（行 1001）
  - LightMem 行："LightMem & $\frac{N r^x T}{th}(L_{\text{sum-in}} + th + L_{\text{sum-out}})$ & $\frac{N r^x T}{th} M_2 R_2 (L_{\text{up-in}} + L_{\text{up-out}})$ & $\frac{N r^x T}{th}$ & $O\Big(\frac{N r^x T}{th}\Big)$"（行 1003）
  - 三处来源叙述：行 1010–1014——`r^x T` 的预压缩、`Nr^x T/th` 的 summary 频率、`M_2 R_2 < M_1 R_1` 的 update 比例下降。

- 行 300–326（Appendix `tab:notation` 符号定义）：覆盖 `N, T, r, x, th, L_sum-in/out, M_1/M_2, R_1/R_2, L_up-in/out` 全部定义。其中：
  - "$x$: Number of compression iterations. In LightMem, the *pre-compress* module may be invoked multiple times for the same message to remove redundancy until the message is sufficiently compact. This occurs frequently in datasets such as **LongMemEval**."（行 313）

- 行 1271–1290（`tab:memory_comparison` GPT-4o-mini 分区）：A-MEM 与 LightMem(r=0.7,th=512) 的总 token / API calls / runtime 实测对照：1605.81k vs 28.25k、986.55 vs 18.43、5132s vs 284s。

- 行 596–598（§experiments online vs offline）："If considering only online test-time cost, LightMem shows an even larger efficiency advantage. For GPT, LightMem reduces total token consumption by 31.4×–105.9× and API calls by 17.1×–159.4×"——支持 LongMemEval 上的极端 token 降幅。

## 卡片范围是否成立

- 复杂度公式与三处来源拆解直接来自论文表与正文，没有引申。
- "数量级一致" 的估算（`th/(r^x T) ≈ 24×`）是基于论文给定 r=0.7、典型 T、th 做的合理算术校验，未声称是论文断言。
- "操作含义" 中的"r 越小越省，但 r≤0.4 时 ACC 掉" 引自论文实验段（行 629 "the optimal r for ACC is 0.6"）。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:29:00+08:00
- 检查要点：
  - 非标题复述：以符号清单 + 复杂度对照 + 三处来源 + 实测对照 + 操作含义 + 边界六段实质展开。
  - 知识密度：完整公式 + 57×/54×/18× 实测对照 + r/th/x 三参数操作规则。
  - 源支撑：lightmem 行 989-1014 / 300-326 / 1271-1290 / 596-598。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 5 个 v3 draft id。

## 备注

- 与 `lightmem-three-stage-atkinson-shiffrin` 卡互补：那张卡只给出"10–38× 之类"的实测数字，这张卡给出渐进公式与降本来源拆解。
- 与 `lightmem-light2-topic-aware-stm` 配合：`Nr^x T/th` 中 `th` 这个变量的语义在 Light2 卡详细说明。
- Adoption 阶段观察：v2 候选 token 共享在中文虚词上，无 LightMem / 复杂度论点交集。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/lightmem-complexity-formula.md`
- draft provenance: `../../drafts/provenance/lightmem-complexity-formula.md`
- similarity: `../../drafts/similarity/lightmem-complexity-formula.json`
- comparison provenance: `../../drafts/comparison/lightmem-complexity-formula.md`
