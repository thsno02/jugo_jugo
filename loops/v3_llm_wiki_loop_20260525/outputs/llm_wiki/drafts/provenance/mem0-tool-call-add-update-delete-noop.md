---
schema: draft_card_provenance.v3
draft_card: ../cards/mem0-tool-call-add-update-delete-noop.md
material_id: arxiv-mem0
digest_id: digest_arxiv-mem0
source_paths:
  - data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt
created_time: 2026-05-26T11:35:00+08:00
edited_time: 2026-05-26T11:35:00+08:00
edited_entity: llm
---

## 源证据

- 第 911–966 行（Algorithm 1）：
  > "Procedure UpdateMemory(F, M): For each fact f ∈ F: operation ← ClassifyOperation(f, M); If operation = ADD: id ← GenerateUniqueID(); M ← M ∪ {(id, f, 'ADD')}; ElseIf operation = UPDATE: m_i ← FindRelatedMemory(f, M); If InformationContent(f) > InformationContent(m_i): M ← (M \\ {m_i}) ∪ {(id_i, f, 'UPDATE')}; ElseIf operation = DELETE: m_i ← FindContradictedMemory(f, M); M ← M \\ {m_i}; ElseIf operation = NOOP: No operation performed."
  > "Function ClassifyOperation(f, M): If not SemanticallySimilar(f, M): Return ADD; ElseIf Contradicts(f, M): Return DELETE; ElseIf Augments(f, M): Return UPDATE; Else: Return NOOP."
- 第 1155 行：tool call 接口 + 不用独立分类器的设计原文。

## 卡片范围是否成立

- 卡片范围 = "Update 阶段的四操作语义、判断顺序、与传统 CRUD 的差别"；与 `mem0-extract-update-pipeline`（管线骨架）正交，不重复。
- 直接来自源：四操作触发条件、InformationContent 门槛、ClassifyOperation 判断顺序、不用独立分类器的设计。
- 引申点：与 memory-as-metabolism 的 "never hard-delete" 对比、与 AUDIT 反事实测试的对比，是把同 batch 中两个论文的设计立场并置——属于跨材料对比，未对 mem0 本身引入论文外主张。

## 发表门控结果

本轮未运行。

## 备注

- 与本 batch 的 `audit-by-suspension-against-entrenchment` 形成有意义的对照——可在 comparison_provenance 阶段评估是否值得在两卡之间建立"两种保留策略对照"的双向 cross-link。
- v2 卡片中无 mem0 相关条目，无重叠。
