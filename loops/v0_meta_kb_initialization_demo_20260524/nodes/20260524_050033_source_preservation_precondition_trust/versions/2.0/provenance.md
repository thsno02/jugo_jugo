# Provenance / 溯源记录

node_id:: 20260524_050033_source_preservation_precondition_trust
version:: 2.0

## 为什么存在这个版本

这个 candidate 只用于测试 major-change impact propagation。它故意改变 adopted 1.0 node 的 support contract：source preservation 必要但不充分，还需要 provenance。

## 使用的输入

### 已有 data

- nodes/20260524_050033_source_preservation_precondition_trust/versions/1.0/card.md
- nodes/20260524_050034_provenance_as_core_knowledge_asset/versions/1.0/card.md
- nodes/20260524_050035_citation_driven_impact_propagation/versions/1.0/card.md

### 动态检索

无。这是 impact test 使用的 simulated major candidate。

### prior KB nodes

- 20260524_050034_provenance_as_core_knowledge_asset
- 20260524_050035_citation_driven_impact_propagation
- 20260524_050031_llm_wiki_working_definition

### 过程 artifacts

- .llmwiki/runs/run_20260524_050634_major_impact_simulation/run_plan.md
- .llmwiki/runs/run_20260524_050634_major_impact_simulation/audit_report.md

## 生产理由

该 candidate 不会 adopted。它是一个受控测试 artifact，用来验证 `change.md` 与 `generated/citation_graph.yaml` 是否能共同生成 `generated/impact_queue.yaml`。

## Citation 理由

Candidate 引用 provenance 和 impact-rule nodes，用于说明这个 semantic change 为什么是 major，以及为什么需要 downstream review。

## Synthesis 决策

Candidate 把 trust contract 从单一前提收窄为两个部分：source preservation + provenance。

## Audit trail

audit_result:: held_for_impact_review
audit_report:: .llmwiki/runs/run_20260524_050634_major_impact_simulation/audit_report.md

## Adoption 理由

此 candidate 有意不 adopted。impact review 完成之前，它不得进入 `kb/`。

## 限制与不确定性

这是 simulated major change，不应被当成已采纳 correction。

## 修订触发条件

- impact queue 为空，说明 citation propagation 失败。
- downstream review 表明这个 candidate 实际不改变 support contract。
- demo 不再需要 simulation artifact。
