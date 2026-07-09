---
id: memgpt-premature-stopping
title: MemGPT 提前停止搜索的失败模式
status: draft
card_type: failure-mode
tags: [memgpt, premature-stopping, pagination, search-persistence, limitation]
created_time: 2026-06-12T10:21:00+08:00
edited_time: 2026-06-12T10:21:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-premature-stopping.md
canonical_concept: premature-stopping-failure
aliases: [提前停止搜索, premature stopping, early termination, search persistence failure]
summary: >-
  MemGPT premature-stopping-failure 的主要失败模式是 LLM 在应该继续翻页/查找时提前停止：Document QA 中未耗尽 retriever 数据库即放弃，Nested KV 中未完成所有嵌套层即返回——系统性能上界由 LLM 搜索持久性决定。
related: [memgpt-document-qa-pagination, memgpt-nested-kv-retrieval, memgpt-context-window-vs-agency-tradeoff]
---

论文在多个实验中观察到 MemGPT 的共同失败模式——premature stopping（提前停止搜索）：

**Document QA**："we observe that MemGPT will often stop paging through retriever results before exhausting the retriever database"——理论上 MemGPT 可以通过不断翻页找到 gold document（只要它存在于 embedding 数据库中），但实践中 LLM 经常在几页结果后就放弃搜索。[^src-1]

**Nested KV**：MemGPT+GPT-4 Turbo 和 GPT-3.5 在 2+ nesting levels 开始失败，原因是 "failing to perform enough lookups"——LLM 没有完成所需的全部嵌套查找就返回了中间结果。[^src-2]

**根因分析**：LLM 缺乏对"完成条件"的可靠判断——何时已经找到最终答案、何时还需要继续搜索。这是概率性 agent 与确定性算法的根本区别：确定性搜索总会遍历到终止条件，LLM 可能基于某种启发式"觉得够了"就停止。

这一失败模式揭示了 MemGPT 架构的核心 tradeoff：系统赋予 LLM 自主权（决定何时检索、何时停止），但自主权也意味着可能做出次优决策。论文中通过在 prompt 中强调"DO NOT STOP SEARCHING UNTIL YOU VERIFY"来缓解（见 KV task instructions），但效果因模型而异。[^src-2]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Multi-document QA -- "we observe that MemGPT will often stop paging through retriever results before exhausting the retriever database"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Nested KV + Appendix KV Instructions -- "still begin to drop off in performance at 2 nesting levels as a result of failing to perform enough lookups... DO NOT STOP SEARCHING UNTIL YOU VERIFY THAT THE VALUE IS NOT A KEY"
[^card-1]: -> memgpt-document-qa-pagination -- 本卡聚焦提前停止的失败模式分析，该卡描述 Document QA 中迭代检索的结构性优势
[^card-2]: -> memgpt-context-window-vs-agency-tradeoff -- 本卡描述提前停止的表象，该卡分析导致提前停止的更深层 tradeoff（上下文大小 vs 主动性）
