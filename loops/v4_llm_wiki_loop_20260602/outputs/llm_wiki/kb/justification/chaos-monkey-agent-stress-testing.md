---
schema: justification_journal.v1
card: ../cards/chaos-monkey-agent-stress-testing.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt`
源证据：
- Section: Introduction -- "Inspired by chaos engineering principles... we introduce Chaos Monkey to study whether such stress creates a 'frustration window'"
- Section: Chaos Monkey -- "Click Drop... Scroll Swap... Type Transform..."
- Table 2 -- "Chaos Monkey roughly doubles the number of steps required while reducing TSR for most models."
范围论证：Chaos Monkey 作为一种独立的 agent 测试方法论，与 Frustration Exploitation 攻击策略分离。前者是测试手段，后者是攻击策略+发现。Chaos Monkey 方法本身可应用于 agent 安全性测试的更广泛场景。
