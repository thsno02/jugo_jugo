---
schema: draft_card_provenance.v3
draft_card: ../cards/enterprise-llm-wiki-tool-native-ingestion.md
material_id: falconer-enterprise-guide
digest_id: digest_falconer-enterprise-guide
source_paths:
  - data/raw/webpage/falconer-enterprise-guide/text.txt
created_time: 2026-05-26T11:48:00+08:00
edited_time: 2026-05-26T11:48:00+08:00
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

本轮未运行。

## 备注

- 本卡和 four-properties 卡的关系：four-properties 覆盖"为什么 capture 重要"，本卡覆盖"capture 在企业里具体应该如何实现"。
