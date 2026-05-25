# 选择第二轮候选 12 进入 drafting

- `timestamp`: `2026-05-25T09:26:26+08:00`
- `source_iteration`: `iteration_20260525_0051_source_mining_karpathy_x_launch`
- `selected_candidate`: `候选 12`
- `next_iteration`: `iteration_20260525_0060_card_drafting_wiki_health_checks`
- `next_task_id`: `task_20260525_0061_card_drafting_candidate_12`
- `decision`: `ready_for_card_drafting`

## 选择理由

选择候选 12，因为它由本地 `raw.json` 中的 `$.tweet.quote.text` 直接支撑，事实边界清楚：被引用推文描述让 LLM 对 wiki 做 `health checks`，例如发现不一致数据、补全缺失数据、寻找新文章候选的有趣连接，以逐步提升数据完整性。

该候选与已采纳卡片不重复：既有 `llm-wiki-ingest-example-flow` 记录摄取流程，`llm-wiki-query-answer-writeback` 记录问答和好答案回写，候选 12 记录的是对 wiki 的检查和清理方式。该选择不基于主题覆盖、hub、cluster 或叙事补齐。

## 边界记录

本轮来源证据只使用 `data/raw/webpage/karpathy-x-launch-post/raw.json` 的 `$.tweet.quote.text`。drafting task 要求使用“被引用推文”或“该 quote text”表述，不使用未列字段补充作者身份、发布时间或外部背景。

## 生命周期记录

本轮仍是单张卡 drafting。虽然候选 8-12 都来自同一个 `$.tweet.quote.text` 字段，但该本地 JSON 字段体量小，且每个候选的写作与审计边界需要独立留痕；当前继续使用 one-shot worker。若后续出现重复读取大来源或跨候选共享大量 source parsing 的失败证据，再评估 alive sub-agent。
