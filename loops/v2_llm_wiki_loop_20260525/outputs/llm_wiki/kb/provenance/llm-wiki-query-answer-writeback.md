# Query 操作回写好答案：出处论证

关联知识卡：`llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md`

## 事实来源

这张草稿卡来自 `候选 12`，事实证据限定为 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:39-40`。`fact_candidates.md` 只用于核对候选字段，没有为卡片加入其它候选内容。

## 支撑关系

指定来源行位于 Operations 的 Query 小节。该小节直接描述了 query 操作：用户向 wiki 提问，LLM 搜索相关页面、阅读页面，并综合生成带引用答案。同一处还提出，好答案可以被归档回 wiki，成为新页面，使探索结果留在知识库中。

## 来源明说

来源明说的部分包括：查询是 against the wiki；LLM 会搜索 relevant pages、读取它们，并 synthesizes an answer with citations；好的答案可以 filed back into the wiki as new pages。

## 整理表述

卡片把来源中的连续描述整理为一个原子事实：该来源描述了一套 query 流程，并附带一个答案回写主张。“有价值的问答结果”是对来源中 good answers、comparison、analysis、connection 等例子的概括，不额外加入来源之外的系统能力。

## 成立范围

该事实只在“该来源如何描述 query 操作流程”这个范围内成立。它不证明某个实现已经具备这些能力，也不证明所有 LLM wiki 或 RAG 系统都采用这种流程。

## 采纳状态

该卡已通过 `llm_wiki/loop/iterations/iteration_20260525_0031_card_audit_query_workflow/artifacts/audit_report.md` 审计，结论为 `audit_result: pass`；采纳后知识卡状态改为 `accepted`，来源限定不变。
