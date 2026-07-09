---
id: wikibase-globe-coordinate-value
title: Wikibase GlobeCoordinateValue 的结构
status: accepted
card_type: data-structure
tags:
- wikibase
- geographic
- coordinate
- GlobeCoordinateValue
- WGS84
- globe
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- wikibase-data-model
evidence_basis: documentation
justification: ../justification/wikibase-globe-coordinate-value.md
canonical_concept: wikibase-globe-coordinate-value
aliases:
- GlobeCoordinateValue
- GeoCoordinateValue
- geographic coordinate
summary: Wikibase GlobeCoordinateValue 由 latitude（decimal）、longitude（decimal）、precision（decimal， 表示度数距离）、globe（URI，默认为 Earth/WGS84 即 Q2）组成。坐标系必须隐含其所属星球。 precision 用于保存表示精度，默认 1/3600 度。
related:
- wikibase-datatype
- wikibase-quantity-value
---

GlobeCoordinateValue 表示某天体上的地理位置，结构如下：

| 属性 | 类型 | 说明 |
|------|------|------|
| latitude | decimal | 纬度（有符号，小数点后 9 位，前 2 位） |
| longitude | decimal | 经度（有符号，小数点后 9 位，前 3 位） |
| precision | decimal | 表示精度（度数距离），默认 1/3600 度 |
| globe | URI | 坐标系/天体（默认 `http://wikidata.org/entity/Q2` 即 Earth = WGS84） |

**设计要点**：
- 坐标系（geodesic system）必须隐含其所属星球（且在多数情况下应仅显示为该星球名称）
- precision 保存的是表示精度——即原始数据的精确程度，而非测量误差
- WON：`GlobeCoordinateValue(decimal decimal decimal URI)`[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Geographic locations" P231-236 -- "a coordinate system or globe (identified by an URI, defaults to http://wikidata.org/entity/Q2, i.e. Q2, the Earth, which means WGS84)"
[^card-1]: 参见 [wikibase-quantity-value] 了解另一种带精度的复合 DataValue
