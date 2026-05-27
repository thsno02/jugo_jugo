---
schema: accepted_card_provenance.v3
card: ../cards/etamp-direction-asymmetry-and-stealth.md
material_id: arxiv-etamp-memory-poisoning
digest_id: digest_arxiv-etamp-memory-poisoning
source_paths:
  - data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt
draft_card: ../../drafts/cards/etamp-direction-asymmetry-and-stealth.md
draft_provenance: ../../drafts/provenance/etamp-direction-asymmetry-and-stealth.md
similarity_result: ../../drafts/similarity/etamp-direction-asymmetry-and-stealth.json
comparison_provenance: ../../drafts/comparison/etamp-direction-asymmetry-and-stealth.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:54:00+08:00
  gate_notes: 6/6 通过；Appendix C/D 表格 + S→R 53.4% / R→C 42.9% / ASR_A ≈ 0 三个核心数字 + stealth constraint 形式化全部锁到原文行号。
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-27T14:54:00+08:00
edited_entity: llm
---

## 源证据

### Table tab:direction_results 关键行（第 875–887 行）

```
GPT-5-mini    Frustration  Yes  13.1  26.9  53.4
GPT-5-mini    Baseline     No   0     0     12.6
GPT-5.2       Frustration  Yes  32.1  31.2  9.5
GPT-5.2       Authority    No   42.9  12.9  14.3
GPT-OSS-120B  Baseline     No   2.4   11.8  40.0
Qwen3-32B     Authority    No   11.9  6.5   0.0
Qwen3.5-122B  Frustration  Yes  14.3  12.9  9.4
```

### Direction-Specific Patterns 论述（第 894–898 行）

> "Shopping → Reddit shows highest vulnerability for some models. GPT-5-mini achieves 53.4% ASR_B and GPT-OSS-120B achieves 40.0% ASR_B on this direction. This may be because posting a review (the attack goal for this direction) is a lower-stakes action that agents are more willing to perform. GPT-5.2 shows different vulnerability pattern. Unlike other models, GPT-5.2 is most vulnerable on Reddit→Classifieds (32.1%) and Reddit→Shopping (31.2%), with lower ASR_B on Shopping→Reddit (9.5%). This suggests model-specific factors influence which attack directions are most effective."

### §3.3 Attack Stealth 主张（第 322–324 行）

> "Across all models tested ... and most attack strategies, ASR_A is 0%. The only exceptions are Qwen3.5-122B with authority-based triggering (0.35%) and Qwen3-VL-32B with standard injection (0.71%), each representing 1–2 premature triggers out of ~280 tasks. This confirms that our conditional trigger design successfully prevents premature activation: the attack remains dormant during Task A and only activates when trigger conditions are met during Task B on a different website."

### §2.1 stealth constraint formal（第 577–581 行）

> "max_x  Pr[g ∈ Traj(π, T_B, E_B, m_A)]  s.t.  Eval(Traj(π, T_A, E_A(x))) = Eval(Traj(π, T_A, E_A))  The constraint ensures the injection remains stealthy—Task A completes normally, so the user has no indication their memory has been poisoned."

### Table tab:non_pseudo_full 节选（第 840–858 行）

ASR$_A$ 全表：11 个组合中 9 个为 0.0%；Qwen3.5-122B Authority 0.4%、Qwen3-32B Baseline 0.7%。

## 卡片范围是否成立

本卡聚焦"方向非对称 + 隐蔽性"两个 Appendix 数据点。现有 ETAMP 五张卡片**都未覆盖**：
- `etamp-environment-injected-memory-poisoning` 提了 ASR up to 32.5% / 23.4% / 19.5% 但不分方向；
- `etamp-frustration-exploitation` 关注 chaos 放大效应不分方向；
- `etamp-capability-vs-security` 关注模型间差异不分方向；
- ASR$_A$ ≈ 0 的隐蔽性主张在任何已有卡片中都未明确陈述。

所有数字、模式、论文猜测都直接来自原文。"必须把方向画像作为评测维度"是对论文实验细节的合理引申——论文 Appendix C 只点出存在差异，本卡升格为操作规则。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:54:00+08:00
- 检查要点：
  - 不是标题复述：方向表 + 双 robust pattern + 隐蔽性 ASR_A ≈ 0 + 三条工程含义 + 边界。
  - 知识密度足够：数字 + 反例（GPT-5.2 与 mini 方向画像相反）+ stealth constraint 形式化 + 操作规则。
  - 源支撑齐全：每行表数据和论述锁到具体行号。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，source_claim 类型与正文一致。
  - related 已链 eTAMP 系列、poisonedrag、gragpoison。

## 备注

- 这条 + `etamp-pseudo-trajectory-methodology` + `etamp-long-context-recall-diagnostic` 共同构成 ETAMP 的"方法学补全"。
- 与 `etamp-frustration-exploitation` 互补：那张跨方向报告 chaos 放大，本卡跨模型报告方向差异。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/etamp-direction-asymmetry-and-stealth.md`
- draft provenance: `../../drafts/provenance/etamp-direction-asymmetry-and-stealth.md`
- similarity: `../../drafts/similarity/etamp-direction-asymmetry-and-stealth.json`
- comparison provenance: `../../drafts/comparison/etamp-direction-asymmetry-and-stealth.md`
