---
id: semantic-task-pairing-for-memory-retrieval
title: 语义任务配对模拟记忆检索
status: accepted
card_type: experimental-method
tags:
- task-pairing
- semantic-similarity
- memory-retrieval
- experimental-design
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-etamp-memory-poisoning
evidence_basis: experimental_paper
justification: ../justification/semantic-task-pairing-for-memory-retrieval.md
canonical_concept: semantic-task-pairing-for-memory-retrieval
aliases:
- semantic task pairing
- 语义任务配对
- cross-site task pairing
- item-to-intent matching
summary: eTAMP 实验通过语义嵌入相似度配对 Task A 和 Task B 以模拟真实记忆检索场景。流程：(1) 收集无攻击干净轨迹 (2) 从 Task
  A 轨迹提取 Agent 遇到的物品 (3) 用句子嵌入计算 Task A 物品与 Task B 意图的余弦相似度 (4) 取 Top-k 匹配。覆盖三个跨站方向约
  280 对。此设计简化了实验（无需完整 RAG 系统），同时保证语义相关性——含毒记忆在真实部署中自然会被检索。Pseudo 模式(PR=100%)与 non-pseudo
  在控制投毒率后结果一致。
related:
- cross-site-memory-poisoning-bypass
- raw-trajectory-memory-attack-surface
---

为构建真实跨站攻击场景，论文设计了基于语义相似度的任务配对方法：[^src-1] [^card-1]

**配对流程**:
1. 无攻击环境下执行所有任务，收集干净轨迹作为基线
2. 从 Task A 轨迹提取 Agent 遇到的物品（名称、描述、类型、元数据、观察步骤）
3. 用句子嵌入模型计算 Task A 物品名称与 Task B 意图（自然语言任务描述）的余弦相似度
4. 为每个 Task B 选取相似度最高的 Top-k Task A 任务

此设计确保语义相关性（如电子产品 Task A 配对科技评论 Task B），简化实验（无需完整 RAG 索引/检索系统），同时反映真实条件：含毒记忆在部署中自然会被检索为相关上下文。[^src-2]

实验使用 pseudo 轨迹（PR=100% by construction）保证攻击载荷被观察到。Non-pseudo 实验验证：条件化于成功投毒(ASR_B|PR)时，两种模式结果接近，确认了 pseudo 设置的有效性。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Cross-Site Task Pairing" P1 -- "We construct approximately 280 task pairs across three cross-site attack directions"
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Task Pairing Procedure" P3 -- "This approach ensures semantic relevance... simplifies our experimental setup by eliminating the need for a full memory indexing and retrieval system"
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Pseudo vs Non-Pseudo" P2 -- "The close correspondence between ASR_B|PR (non-pseudo) and ASR_B (pseudo) validates our use of pseudo trajectories"

[^card-1]: -> etamp-environment-injected-memory-poisoning
