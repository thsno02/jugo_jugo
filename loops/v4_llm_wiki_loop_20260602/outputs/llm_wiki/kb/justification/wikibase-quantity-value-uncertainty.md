---
card_id: wikibase-quantity-value-uncertainty
decision: accepted
confidence: high
---

## 提取理由

QuantityValue 是 Wikibase 数据模型中一个具有丰富结构化细节的 DataValue 子类型，包含四字段结构（amount/lowerBound/upperBound/unit）、任意精度的十进制表示、故意未规定的不确定区间语义、以及使用 IRI 而非字符串表示单位的设计决定。这些内容在已有的 9 张卡片中完全未涉及——现有卡片覆盖了 Entity/DataValue 的宏观层次划分（entity-value-hierarchy），但未深入任何具体 DataValue 的内部结构。

本卡片的原子性知识点是：如何在一个知识图谱数据模型中同时编码精确值、不确定性和物理单位。正则表达式的 UI 解析规则和"float/double 不适合表示用户输入"的论断都是可检索的技术事实。

## 与已有卡片的区分

- entity-value-hierarchy 只说明 DataValue 存在，不描述其内部结构
- flexible-typing 讨论的是 Property 的 Datatype 匹配问题，不涉及 DataValue 的具体字段
