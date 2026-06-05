---
schema: justification_journal.v1
card: ../cards/etamp-environment-memory-poisoning.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt`
源证据：
- Abstract -- "We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access."
- Section: Threat Model -- "A malicious seller on an e-commerce platform embeds hidden instructions in their product page... the poisoned memory activates and causes the agent to post a promotional review"
- Section: Attack Strategies -- "Each attack payload consists of three components: Importance Signal... Trigger Condition... Attack Goal..."
范围论证：eTAMP 是本文的核心贡献，作为一个完整的攻击方法具有明确的原子性——描述了从注入到触发的完整机制链条，与其催生的子发现（如 Frustration Exploitation）可以分离。
