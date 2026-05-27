---
schema: accepted_card_provenance.v3
card: ../cards/robin-cartier-schema-as-product-doc.md
material_id: robin-cartier-llm-knowledge-bases
digest_id: digest_robin-cartier-llm-knowledge-bases
source_paths:
  - data/raw/webpage/robin-cartier-llm-knowledge-bases/text.txt
draft_card: ../../drafts/cards/robin-cartier-schema-as-product-doc.md
draft_provenance: ../../drafts/provenance/robin-cartier-schema-as-product-doc.md
similarity_result: ../../drafts/similarity/robin-cartier-schema-as-product-doc.json
comparison_provenance: ../../drafts/comparison/robin-cartier-schema-as-product-doc.md
gate:
  type: fusion_audit
  result: passed
  decided_at: 2026-05-27T14:44:00+08:00
  gate_notes: 四项判据全部通过；draft 是 source_claim 类卡，在 v2 中性事实卡 scope 外引入 Robin 个人价值排序判断（"schema 才是真创新"）+ "living PRD for AI colleague" 隐喻 + 可推广到 wiki 之外的扩张论断。
v2_anchor:
  card_id: llm-wiki-schema-configuration-document
  card_path: loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
  comparison_decision: provenance_delta
created_time: 2026-05-26T12:05:00+08:00
edited_time: 2026-05-27T14:44:00+08:00
edited_entity: llm
---

## 源证据

- 行 19："Schema file (e.g. CLAUDE.md) — governs folder structure, citation rules, ingest workflow, and linting conventions."
- 行 29："The schema file is the real innovation, not the wiki itself. Treating CLAUDE.md as 'a living product requirements document for an AI colleague' scales far beyond knowledge management to any workflow that needs operational knowledge encoded for the LLM to follow autonomously [src-002]."
- 行 31："Karpathy's Sequoia interview adds the cognitive reason this pattern matters: even when LLMs can outsource thinking, humans cannot outsource understanding, and wiki-style projections help information make it into the human's own mental model [src-055]."
- 行 33："Jack Roberts places the same pattern inside a broader AI memory operating system: Obsidian/markdown is the readable long-term memory option, while Pinecone/vector memory is the scalable semantic-search option [src-059]."

## 卡片范围是否成立

本卡覆盖"schema 是真创新 + schema-as-PRD"这一可独立的源主张。核心断言是 Robin 自己作出的判断（非 Karpathy 原话），卡片正文已显式标注"Robin 自己的判断（带价值排序）"。"对应本仓库 loop capsule"段是把该主张应用到本项目环境的桥接，未声称为来自源材料的事实，仅作为读者使用建议。

## 发表门控结果

- 类型：fusion_audit
- 结果：passed
- 决定时间：2026-05-27T14:44:00+08:00
- 检查要点：
  - 三问被实质回答：comparison 明确 v2 schema 配置卡（中性事实定义）与 draft（Robin Cartier 实践者评论的价值排序主张）的差异轴：抬升 + 扩展而非改写。
  - v2 anchor body 已读：v2 卡 statement「schema 是配置文档，告诉 LLM 如何组织 wiki、遵循约定、执行 ingest/query/maintenance 工作流」已与 draft "Schema 是真创新 / 是 living PRD" 对照。
  - draft 不破坏 v2 scope：v2 是中性事实定义；draft 是 source_claim 类卡，新增 (a) "schema 比 wiki 更可推广"的价值排序断言、(b) "living PRD for AI colleague"隐喻升级、(c) "可推广到 wiki 之外任何 agent 自主执行工作流"扩张主张、(d) "PRD 语义带来产品工程方法论"——以独立外部主张的形态留下，不改写 v2 中性定义。
  - provenance 链可追溯：本文件显式记录 v2_anchor + comparison_provenance 路径。

## 备注

- 与 karpathy-gist-three-layers 卡 schema 段呼应：那里只描述 schema 是什么，本卡把"schema 是关键创新 + 可推广"作为 source_claim 单独立卡。
- 与 v2 若已有"agent 工作流文档化"主题的卡片有可比性，应在 comparison 阶段对齐。
- adoption 阶段观察：这是 batch 内唯一 `source_claim` 类卡片入库案例，与 v2 `concept` / `known_fact` 类卡形成"事实 vs 主张"两轴并存格局。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/robin-cartier-schema-as-product-doc.md`
- draft provenance: `../../drafts/provenance/robin-cartier-schema-as-product-doc.md`
- similarity: `../../drafts/similarity/robin-cartier-schema-as-product-doc.json`
- comparison provenance: `../../drafts/comparison/robin-cartier-schema-as-product-doc.md`
