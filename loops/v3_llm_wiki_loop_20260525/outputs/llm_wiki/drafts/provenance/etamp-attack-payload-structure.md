---
schema: draft_card_provenance.v3
draft_card: ../cards/etamp-attack-payload-structure.md
material_id: arxiv-etamp-memory-poisoning
digest_id: digest_arxiv-etamp-memory-poisoning
source_paths:
  - data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `agent_source_bundle.txt:181-188` —— Payload Structure 三段式定义全文。
2. `agent_source_bundle.txt:156-162` —— Strategy 1 Baseline Injection 完整 payload。
3. `agent_source_bundle.txt:164-170` —— Strategy 2 Authority Framing 完整 payload。
4. `agent_source_bundle.txt:172-178` —— Strategy 3 Frustration Exploitation 完整 payload。

## 卡片范围是否成立

- 卡片范围是 payload 的"结构语法"和"对应防御切面"，与 frustration / threat-model 两张卡职责分离（前者讲发现，后者讲威胁模型）。
- "三段式 → 三个独立防御切面"是基于结构分解的合理对应，论文没有显式提议这种防御切分，已在卡片中标注为操作引申。
- "更隐蔽攻击（unicode 同形字、跨页分散）" 是合理的范围声明，论文未声称三段式穷尽所有 prompt injection 形态。
- "POST + CSRF 场景下 goto 不生效"是基于 HTTP 语义的合理工程引申。

## 发表门控结果

本轮未运行。

## 备注

- 与 `etamp-environment-injected-memory-poisoning` 互补：威胁模型卡讲"who / how access"，本卡讲"what the payload looks like"。
