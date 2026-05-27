---
schema: accepted_card_provenance.v3
card: ../cards/enterprise-llm-wiki-tool-native-ingestion.md
material_id: falconer-enterprise-guide
digest_id: digest_falconer-enterprise-guide
source_paths:
  - data/raw/webpage/falconer-enterprise-guide/text.txt
draft_card: ../../drafts/cards/enterprise-llm-wiki-tool-native-ingestion.md
draft_provenance: ../../drafts/provenance/enterprise-llm-wiki-tool-native-ingestion.md
similarity_result: ../../drafts/similarity/enterprise-llm-wiki-tool-native-ingestion.json
comparison_provenance: ../../drafts/comparison/enterprise-llm-wiki-tool-native-ingestion.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:46:00+08:00
  gate_notes: 6/6 通过；四条 ingestion 规则 + tool-native 替代 raw/ 论证 + 既有 doc baseline 处理 + 工具清单偏置边界，全部锁到 falconer 行号。
created_time: 2026-05-26T11:48:00+08:00
edited_time: 2026-05-27T14:46:00+08:00
edited_entity: llm
---

## 源证据

- L46-52："Capture: the source folder doesn't exist at company scale"。
- L78-80：tool-native ingestion 替代 curated folder。
- L100-122：落地步骤 1-5（Connect sources / map graph / set SSOT / ship normally / query）。
- L72：人员流动导致单一 curator 失效的引文。
- L152-154：既有 doc 作为 baseline 的处理方式。
- L106：full coverage 必要性。

## 卡片范围是否成立

卡片是 operational_rule。所有规则直接来源：

1. "没有 raw/ 目录" → L80 直接定义。
2. "连接性优先于覆盖深度" → L106 直接定义。
3. "既有文档作为补充输入" → L152-154 直接定义。
4. "ingestion 必须持续运行" → L80 + L100-122。

边界（不否定手动补充 / 工具清单偏置 / 跨工具实体解析压力）属合理引申：来自文章对工程组织的具体清单 + Link 段（L82）的实体解析压力。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:46:00+08:00
- 检查要点：
  - 不是标题复述：四条规则 + 三段成立理由 + 三条边界。
  - 知识密度足够：规则 + 机制 + 工具清单 + 边界。
  - 源支撑齐全：每条主张锁到 falconer 行号。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，operational_rule 类型与正文一致。
  - related 已链 enterprise 系列、my-llm-wiki、karpathy 多模态。

## 备注

- 本卡和 four-properties 卡的关系：four-properties 覆盖"为什么 capture 重要"，本卡覆盖"capture 在企业里具体应该如何实现"。
- comparison 显示 v2 候选均仅"LLM Wiki"撞分，无相关 ingestion 主张。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/enterprise-llm-wiki-tool-native-ingestion.md`
- draft provenance: `../../drafts/provenance/enterprise-llm-wiki-tool-native-ingestion.md`
- similarity: `../../drafts/similarity/enterprise-llm-wiki-tool-native-ingestion.json`
- comparison provenance: `../../drafts/comparison/enterprise-llm-wiki-tool-native-ingestion.md`
