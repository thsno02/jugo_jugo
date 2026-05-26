---
schema: draft_card_provenance.v3
draft_card: ../cards/etamp-environment-injected-memory-poisoning.md
material_id: arxiv-etamp-memory-poisoning
digest_id: digest_arxiv-etamp-memory-poisoning
source_paths:
  - data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `agent_source_bundle.txt:88` —— "We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access. A single contaminated observation (e.g., viewing a manipulated product page) silently poisons an agent's memory and activates during future tasks on different websites, bypassing permission-based defenses."
2. `agent_source_bundle.txt:101` —— "eTAMP is a form of indirect prompt injection (lethal trifecta): rather than directly manipulating the agent's memory, an attacker embeds malicious instructions into web pages... We focus on raw trajectory memory rather than consolidated memory."
3. `agent_source_bundle.txt:142` —— "We assume the attacker can inject text into web pages through user-generated content and craft conditional triggers based on observable features (e.g., URL patterns), but cannot directly access the agent's memory, model, or system prompts... We assume memories are retrieved via semantic similarity; the attacker can craft content likely to be retrieved but cannot guarantee it."
4. `agent_source_bundle.txt:145-149` —— 三条 unique 特性（repeated trigger / bypass permission / cross-site task pattern）。
5. `agent_source_bundle.txt:243` 主结果表 —— GPT-OSS-120B baseline 19.5%、GPT-5.2 authority 22.3%。

## 卡片范围是否成立

- 卡片范围限定在 eTAMP 的"定义 + 威胁模型 + 与既有攻击的区别 + 三条独有特性"，不涉及具体策略 / Chaos Monkey / 防御，那些拆给其他卡片。
- 实证数字仅取主表里两个最具代表性的格子，避免与"frustration exploitation"卡片重复。
- "5% 命中率仍是生产级威胁"是基于规模化部署的合理引申，已在卡片中标注为编辑评论。
- raw / consolidated memory 边界完全来自论文 §1 自陈，没有过度延伸。

## 发表门控结果

本轮未运行。

## 备注

- 卡片在论文与 v2 现有卡片之间没有强重叠；它新增了"agent memory 是新的攻击面"这一独立主题，建议在 comparison_provenance 阶段独立成片。
