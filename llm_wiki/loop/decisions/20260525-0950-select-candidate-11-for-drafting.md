# 选择第二轮候选 11 进入 drafting

- `timestamp`: `2026-05-25T09:50:39+08:00`
- `source_iteration`: `iteration_20260525_0051_source_mining_karpathy_x_launch`
- `selected_candidate`: `候选 11`
- `next_iteration`: `iteration_20260525_0063_card_drafting_wiki_qa_scale`
- `next_task_id`: `task_20260525_0064_card_drafting_candidate_11`
- `decision`: `ready_for_card_drafting`

## 选择理由

选择候选 11，因为它由本地 `raw.json` 中的 `$.tweet.quote.text` 直接支撑，事实边界清楚：被引用推文描述，当某个近期研究 wiki 达到约 100 篇文章、约 400K words 的小规模时，可以让 LLM agent 针对该 wiki 回答复杂问题并继续研究。

该候选与已采纳卡片不重复：既有 `llm-wiki-query-answer-writeback` 记录普通 query 操作和好答案回写，`llm-wiki-health-checks` 记录 linting/health checks；候选 11 记录的是被引用推文中一个具体研究 wiki 的规模与 Q&A/research 用法。该选择不基于主题覆盖、hub、cluster 或叙事补齐。

## 边界记录

本轮来源证据只使用 `data/raw/webpage/karpathy-x-launch-post/raw.json` 的 `$.tweet.quote.text`。drafting task 要求使用“被引用推文”或“该 quote text”表述，不使用未列字段补充作者身份、发布时间或外部背景。

## 生命周期记录

本轮仍是单张卡 drafting。候选 8-12 都来自同一个 `$.tweet.quote.text` 字段，但该本地 JSON 字段体量小，且每个候选的产物链路都需要独立留痕；当前继续使用 one-shot worker。若后续出现重复读取大来源或跨候选共享大量 source parsing 的失败证据，再评估 alive sub-agent。
