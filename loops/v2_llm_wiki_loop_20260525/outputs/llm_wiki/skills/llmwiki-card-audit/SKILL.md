---
name: llmwiki-card-audit
description: 审计一张原子事实知识卡及其出处论证，检查事实粒度、证据支持、适用范围、事实类型、中文可读性和引用/脚注布局；用于对草稿知识卡给出通过、修订、拒绝或暂缓结论。
---

# LLM Wiki 知识卡审计

## 目标

审计草稿知识卡是否可以进入 `accepted` 状态。审计执行者只读知识卡、出处论证和指定来源；除本次运行目录内的审计产物外，不修改知识卡、不刷新索引、不写全局生成物。

## 检查项

- 事实陈述是否只有一个主要事实。
- 事实类型是 `known_fact` 还是 `accepted_fact`，是否合理。
- 证据是否直接支撑事实陈述。
- 适用范围是否足够清楚。
- 出处论证是否是可读文档，而不是流水日志。
- 知识卡是否像 zet 风格原子卡，而不是主题报告。
- 知识卡主语言是否为中文。
- 引用区（`References`）是否在脚注区（`Footnotes`）前。
- 脚注区（`Footnotes`）是否是最后一个一级章节。

## 决策

只允许四种决策：

- `pass`：可以进入采纳。
- `revise`：事实可成立，但写法、适用范围、证据或脚注布局需要修。
- `reject`：证据不足或事实陈述不成立。
- `defer`：需要未来补充检索或外部来源。

## 输出

写 `audit.md`：

```yaml
decision: pass | revise | reject | defer
reasons:
  - <中文说明>
required_changes:
  - <若 revise，列出最小修改>
evidence_checked:
  - path: <path>
unexpected_writes: []
```

同时写 `loop_status.md` 与 `loop_delivery.md`。

## 禁止事项

- 不直接改知识卡。
- 不直接改出处论证。
- 不执行采纳。
- 不运行会写全局状态的脚本。
- 不把旧主题/枢纽标准用于原子事实知识卡。
