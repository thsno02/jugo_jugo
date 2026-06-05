---
schema: justification_journal.v1
card: ../cards/agent-memory-persistent-attack-surface.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt`
源证据：
- Abstract -- "Memory makes LLM-based web agents personalized, powerful, yet exploitable. By storing past interactions to personalize future tasks, agents inadvertently create a persistent attack surface that spans websites and sessions."
- Section: Threat Model -- "The attack may be repeatedly triggered on any relevant future tasks."
- Appendix: Attack Characteristics -- "Temporal Separation... Cross-Site Execution... Semantic Relevance... Persistent Threat..."
范围论证：与 eTAMP 攻击方法本身分离，本卡聚焦于"agent 记忆作为攻击面"这一概念层面的认识——记忆的个性化价值与安全风险的内在耦合，以及其跨会话/跨站的持久性特征。这是一个独立于具体攻击方法的安全概念。
