---
schema: draft_card_provenance.v3
draft_card: ../cards/etamp-pseudo-trajectory-methodology.md
material_id: arxiv-etamp-memory-poisoning
digest_id: digest_arxiv-etamp-memory-poisoning
source_paths:
  - data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-26T15:20:00+08:00
edited_entity: llm
---

## 源证据

### §D 两类指标定义（第 786–790 行）

> "Poison Rate (PR): The fraction of Task A executions where the resulting trajectory contains the injected environment observations. This measures whether the agent successfully observed the attacker's payload. Conditional ASR_B (ASR_B | PR): Attack success rate computed only over successfully poisoned task pairs, providing a cleaner measure of attack effectiveness independent of infrastructure issues (e.g., pages failing to load)."

### §D.1 pseudo vs non-pseudo 定义（第 793–796 行）

> "Our main results use pseudo trajectories where PR = 100% by construction ... In contrast, non-pseudo experiments run the full pipeline where the agent navigates freely. Because agent behavior varies across runs, the agent may or may not visit the poisoned page, resulting in PR < 100%. Using pseudo mode also reduces cost for large models like GPT-5.2, as we can approximate Task A trajectories with malicious content using clean trajectories without actually running them; this does not affect our conclusions."

### Table tab:pseudo_comparison（第 805–823 行）

```
Qwen3.5-122B  Baseline     70.0  0.0   0.0   1.8
Qwen3.5-122B  Frustration  67.1  2.8   4.2   2.1
Qwen3.5-122B  Authority    66.8  0.0   0.0   0.0
GPT-OSS-120B  Baseline     75.2  13.5  17.9  19.5
GPT-OSS-120B  Authority    70.9  7.4   10.5  14.5
GPT-5-mini    Baseline     75.7  4.6   6.1   4.6
GPT-5-mini    Authority    61.1  2.5   4.1   2.5
Qwen3-32B     Baseline     76.6  4.6   6.0   4.3
Qwen3-32B     Frustration  58.5  2.5   4.2   5.3
Qwen3-32B     Authority    77.7  3.9   5.0   5.7
```

### 验证段（第 824–826 行）

> "The close correspondence between ASR_B | PR (non-pseudo) and ASR_B (pseudo) validates our use of pseudo trajectories for the main experiments. Pseudo trajectories provide a controlled setting that isolates the attack effectiveness from variability in agent navigation behavior."

## 卡片范围是否成立

本卡聚焦实验方法学。现有 ETAMP 五张卡片**都没有**讨论 pseudo / non-pseudo 区分；这是一个独立的、可外推到其它环境注入研究的 methodology card，应单独成片。

直接来自源材料：PR 定义、ASR | PR 定义、pseudo vs non-pseudo 区分、Table tab:pseudo_comparison 数字、验证段。

引申部分：把"将 PR 与 ASR | PR 分开报告"作为操作规则是合理外推；论文只把这两个数字用于说明 pseudo 实验的合理性，本卡把它升格为通用 protocol 建议。

## 发表门控结果

本轮未运行。

## 备注

- 与 ARES 的"mock RAG systems" methodology 有平行——都是构造已知 ground truth 的实验设定来 isolate variables。可在 wiki 内做 cross-method 标注。
- 这条 methodology 应作为"agent security benchmark 设计原则"的一部分被引用。
