---
schema: draft_card_provenance.v3
draft_card: ../cards/enterprise-llm-wiki-four-properties.md
material_id: falconer-enterprise-guide
digest_id: digest_falconer-enterprise-guide
source_paths:
  - data/raw/webpage/falconer-enterprise-guide/text.txt
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-26T11:45:00+08:00
edited_entity: llm
---

## 源证据

- L18-30："Key takeaways" 段总览四属性。
- L42-74：分别展开 Capture / Link / Compound / Stay current 的失败模式。
- L86-98：个人版与企业版四属性的对照表。
- L66：Stack Overflow 2024 调研数据（60% / 68% / 73%）。
- L82：实体解析跨工具的具体例子（payments service 三个名字）。
- L128-130："Why retrieval tools don't solve this" 段印证 retrieval 不解决 stay-current。

## 卡片范围是否成立

卡片范围是"四属性框架本身"，所有主张直接源自文本：

- 四属性定义 → 原文 takeaways + 后续四节标题。
- 个人 → 企业的断点（stay-current 最难）→ 直接来自 L68-74 一节。
- "必要而非充分集合"是合理引申：文本没有用这个术语，但反复强调"没有这四条之一就塌"——L26 的 "But the maintenance model has to change" 与 L130 的 "smarter search over bad context just produces wrong answers faster" 共同支撑这一同义概括。
- "实现路径不混入"——卡片不复述 Falconer 产品宣传文案（L102-138），只在 References 引用结构。

## 发表门控结果

本轮未运行。

## 备注

- v2 卡片可能已有 "llm-knowledge-base-five-stage-workflow" 等总览卡，本卡的独立价值在于把"四属性"作为分析企业 KB 的判别框架，与五阶段工作流是不同切面。
