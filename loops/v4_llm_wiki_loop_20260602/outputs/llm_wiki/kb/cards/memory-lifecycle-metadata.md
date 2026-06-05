---
id: memory-lifecycle-metadata
title: 记忆生命周期元数据
status: accepted
card_type: mechanism
tags: [llm-wiki, metadata, lifecycle, temporal, rohit-v2]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
justification: ../justification/memory-lifecycle-metadata.md
canonical_concept: memory-lifecycle-metadata
aliases: [记忆生命周期, Memory Lifecycle, 时效性元数据, lifecycle frontmatter, 知识新鲜度管理]
summary: >-
  memory-lifecycle-metadata（记忆生命周期 / Memory Lifecycle / 时效性元数据 / lifecycle
  frontmatter / 知识新鲜度管理）指在 wiki 页面 frontmatter 中添加 last_verified / confidence /
  superseded_by / contradicts 等字段，管理知识的时间维度；缺失时导致过时主张与新鲜主张无法区分
related: [schema-as-configuration, lint-operation, contradiction-as-asset, continuous-drift-detection]
---

记忆生命周期元数据是 Rohit v2 引入的 frontmatter 字段集，用于管理 wiki 页面的**时间维度**。具体包括[^src-1]：

- `last_verified: 2026-05-01` —— 最后验证日期
- `confidence: high|medium|low` —— 置信度等级
- `superseded_by: another-page.md` —— 标记被更新版本替代
- `contradicts: an-older-claim.md` —— 标记与其他页面的矛盾关系

Karpathy v1 **不包含任何这些字段**[^src-2]。缺失这些元数据的实际后果在三个月后显现：wiki 中出现了过时的 ChatGPT 定价声明与新鲜的声明并列的情况，两者都以同等置信度呈现，用户无法区分哪个是当前有效的[^src-3]。

生命周期字段与巡检操作形成协同：字段提供了时效性的结构化标记，巡检操作可以据此检测需要更新的页面。与矛盾保留规则（contradiction-as-asset）也有协同：`contradicts:` 字段是实现「不覆盖，标记」规则的具体 schema 机制。伴侣记忆框架的活力评分公式将类似的生命周期信号（recency/frequency/utility）形式化为多信号保留度量[^card-1]。

## Footnotes

[^card-1]: [活力评分公式](vitality-score-formula.md) -- Rohit v2 的 frontmatter 元数据是 wiki 实践中的轻量级生命周期管理，伴侣记忆框架的活力评分公式将类似信号（recency/frequency/utility/gravity）形式化为理论层面的多信号保留度量

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L54 -- "every page has last_verified: 2026-05-01, confidence: high|medium|low, and (when relevant) superseded_by: another-page.md or contradicts: an-older-claim.md"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L54 -- "v1 has none of these."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L54 -- "After three months I had pages with stale ChatGPT pricing claims sitting next to fresh ones, both confidently asserted. The lifecycle fields fixed it."
