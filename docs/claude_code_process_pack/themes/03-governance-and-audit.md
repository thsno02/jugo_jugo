---
schema: claude_code_theme.v1
theme: governance_and_audit
publish_status: sanitized
---

# Governance And Audit

Claude Code 的一个重要经验是：LLM 适合生成候选知识，但治理动作必须尽量脚本化、可重复、可审计。

## Governance Actions

| Action | Purpose |
| --- | --- |
| fusion scan | 发现 duplicate / overlap_merge / distinct_link |
| anti-merge bias | 避免过度合并破坏原子性和 provenance |
| batch link | 以脚本写入 related，减少 YAML 错误 |
| orphan governance | 消除没有入站/出站关系的孤立卡 |
| backward backlink | 补全对称关系，降低 backlink asymmetry |
| YAML lint | 验证 frontmatter 可解析、related 无双格式 |

## Audit Model

v5 使用 FSJS：

```text
Filter
-> Shard
-> Judge
-> Synthesize
```

Filter 负责机械检查，Judge 负责少量语义判断，Synthesize 负责把结果变成可读审计报告。这比让一个 agent 从头到尾“感觉一下质量”更可靠。

## Publication Gate

KB publish 不是文件存在就结束。至少要回答：

- 每张 card 是否能追溯到 source；
- related 图是否有孤儿；
- backlink 是否大体对称；
- 是否存在明显 fake citation；
- 信息密度是否足以支持未来使用。
