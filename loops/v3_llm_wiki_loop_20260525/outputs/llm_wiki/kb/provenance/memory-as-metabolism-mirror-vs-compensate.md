---
schema: accepted_card_provenance.v3
card: ../cards/memory-as-metabolism-mirror-vs-compensate.md
material_id: arxiv-memory-as-metabolism
digest_id: digest_arxiv-memory-as-metabolism
source_paths:
  - data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
draft_card: ../../drafts/cards/memory-as-metabolism-mirror-vs-compensate.md
draft_provenance: ../../drafts/provenance/memory-as-metabolism-mirror-vs-compensate.md
similarity_result: ../../drafts/similarity/memory-as-metabolism-mirror-vs-compensate.json
comparison_provenance: ../../drafts/comparison/memory-as-metabolism-mirror-vs-compensate.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:52:00+08:00
  gate_notes: 6/6 项通过；原则 + 时间规则 + 操作表三层论证完整。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:52:00+08:00
edited_entity: llm
---

## 源证据

- 第 283–305 行：
  > "A companion system mirrors its user on *operational* dimensions: the working context the user is currently reasoning within, the load-bearing structure the user depends on for coherent thought... A companion system compensates for its user on *epistemic failure* dimensions: entrenchment of demonstrably false high-gravity entries, suppression of evidence contradicting settled beliefs, convergence toward monoculture under repeated use."
- 第 322–327 行（贡献声明）：
  > "The contribution is the TRIAGE → CONSOLIDATE → AUDIT execution model as a binding: not the discovery of the tension, and not the individual operations, but the procedural rule that decides how and when each operation applies to the mirror-vs-compensate conflict in a companion wiki."
- 第 1037–1067 行：§5.0 Mapping operations 表格，逐操作标注 mirror/compensate。

## 卡片范围是否成立

- 卡片把"原则陈述（§1.2）+ 操作角色分配表（§5.0）+ 时间结构化程序规则"合并为一个 operational_rule 卡，与论文自己强调的"核心贡献是绑定规则"一致。
- 直接来自源：mirror-vs-compensate 的维度定义、五操作 mirror/compensate 标注、TRIAGE→CONSOLIDATE→AUDIT 的时间分发。
- 引申部分：把"是否真理追踪器"、"安全故事部分性"、"AUDIT 灵敏度开放问题"列在边界节，是对原文 §8.3/§9 立场的概括，未引入新主张。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:52:00+08:00
- 检查要点：
  - 核心主张-时间规则-操作角色表-边界 四段。
  - 知识密度足；非标题复述。
  - 源支撑：§1.2 / §5.0 多段 verbatim。
  - References + Footnotes 双在。
  - frontmatter 完整；related 含 6 张同系列卡。

## 备注

- v2 已有的 `idea-file-as-agent-era-artifact` 和 `llm-knowledge-base-five-stage-workflow` 关注 Karpathy 原始 wiki 思想；本卡是 governance 层 mirror-vs-compensate 程序规则，与 v2 是互补。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memory-as-metabolism-mirror-vs-compensate.md`
- draft provenance: `../../drafts/provenance/memory-as-metabolism-mirror-vs-compensate.md`
- similarity: `../../drafts/similarity/memory-as-metabolism-mirror-vs-compensate.json`
- comparison provenance: `../../drafts/comparison/memory-as-metabolism-mirror-vs-compensate.md`
