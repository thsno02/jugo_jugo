---
id: observation-based-rag-dialogue
title: Observation-based RAG 对话检索策略
status: accepted
card_type: finding
tags:
- RAG
- observation
- retrieval-unit
- dialogue-memory
- signal-to-noise
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-locomo
evidence_basis: experimental_paper
justification: ../justification/observation-based-rag-dialogue.md
canonical_concept: observation-based-rag-dialogue
aliases:
- observation-based RAG
- observation retrieval unit
- 基于观察的RAG策略
- assertion-based retrieval
summary: observation-based-rag-dialogue 基于 observation 的 RAG 检索策略在长期对话 QA 中表现最优。将对话转化为 speaker-level assertions（observations）作为检索单元，top-5 overall F1=41.4，显著优于 dialog-based (35.8@top-25) 和 summary-based
  (32.5@top-5)。在 temporal reasoning 上优势尤大（41.9 vs 26.2 vs 31.0）。检索更多 observations 反而性能下降，表明降低 signal-to-noise ratio 关键。使用 DRAGON 作为检索器。
related:
- reflect-and-respond-agent
- locomo-evaluation-framework
- locomo-temporal-reasoning-difficulty
---

在 LoCoMo 的 QA 任务中，以 observation（关于 speaker 的断言性陈述）作为 RAG 检索单元表现最优，优于直接检索对话段落和 session summary。[^src-1]

三种检索粒度对比（GPT-3.5-turbo-16K + DRAGON 检索器）：
- **Observation top-5**: overall F1 = 41.4，temporal = 41.9，adversarial = 44.7
- **Dialog top-25**: overall F1 = 35.8，temporal = 26.2，adversarial = 23.4
- **Summary top-5**: overall F1 = 32.5，temporal = 31.0，adversarial = 38.3 [^src-2]

关键发现：增加检索 observation 数量（top-5 → top-50）时性能反而从 41.4 下降到 37.8，表明在检索上下文中降低 signal-to-noise ratio 对模型准确利用信息至关重要。[^src-3]

Summary-based RAG 虽有最高 recall accuracy（top-10 达 90.7%），但因摘要压缩丢失细节，QA 性能不佳。[^src-4] [^card-1]

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "QA Results" -- "RAG is effective when conversations are stored as observations. There is a noticeable 5% improvement with gpt-3.5-turbo when the input is top 5 relevant observations instead of pure conversation logs"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table qa_rag_results" -- "Observation top-5: Overall 41.4; Dialog top-25: Overall 35.8; Summary top-5: Overall 32.5"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "QA Results" -- "This improvement falters with an increase in the number of retrieved observations, suggesting that it is important to reduce the signal-to-noise (SNR) ratio in retrieved contexts"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table qa_rag_results" -- "Summary top-10: Recall Overall 90.7% ... using session summaries as context does not significantly improve the performance despite high recall accuracies"

[^card-1]: 与 [reflect-and-respond-agent] 关联——observation 是该 agent 架构产生的记忆产物
