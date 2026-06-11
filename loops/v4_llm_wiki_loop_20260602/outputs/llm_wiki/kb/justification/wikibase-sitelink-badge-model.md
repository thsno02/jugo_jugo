---
card_id: wikibase-sitelink-badge-model
decision: accepted
confidence: high
---

## 提取理由

Sitelink 是 Wikibase 连接 Item 与外部 wiki 页面的核心机制，包含三个重要设计特征：一对一约束（每个 wiki 至多一条链接）、Badge 附加（以 Item 表示的页面标记如"特色条目"）、以及"Item 代表事物而非页面"的语义区分。这些内容在已有卡片中仅被间接提及（entity-value-hierarchy 提到 Item 代表维基页面的主题），但从未作为独立机制被系统描述。

本卡片的原子性知识点是：Wikidata 如何通过 Sitelink 实现跨语言互联，以及"每个 Item 完整表示一个事物"的数据归属原则如何服务于跨语言数据整合。

## 与已有卡片的区分

- entity-value-hierarchy 提到 Item 是维基页面主题的代表，但不涉及 Sitelink 的具体约束
- entity-description 讨论 label/description/aliases 的词汇信息，不涉及 Sitelink
