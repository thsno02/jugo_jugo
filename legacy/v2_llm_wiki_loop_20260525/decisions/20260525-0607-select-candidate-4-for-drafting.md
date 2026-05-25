# 选择候选 4 进入知识卡草稿

- `decision_time`: `2026-05-25T06:07:01+08:00`
- `controller`: `main-agent`
- `decision`: `select_candidate_for_card_drafting`
- `candidate_id`: `候选 4`
- `iteration`: `iteration_20260525_0033_card_drafting_persistent_composite_wiki`
- `task`: `task_20260525_0034_card_drafting_candidate_4`
- `worker_role`: `card_drafting_worker`
- `dispatch_policy`: `fork_context:false`

## 判断

从第一轮 source mining 的剩余候选中选择候选 4 进入 drafting。候选 4 的证据集中在 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:13`，事实边界是该来源把 wiki 描述为会保留链接、矛盾标记和综合内容并持续变丰富的持久复合产物。

## 选择理由

- 本地来源可读，证据范围短且集中。
- 候选陈述有清晰的产物性质边界，适合写成一张原子事实知识卡。
- 与已采纳的 `持久 wiki 替代模式` 相邻但不重复：已采纳卡强调替代 RAG 的持久 wiki 模式，本候选强调持久复合产物保留的内容类型。
- 本次选择不基于主题覆盖、hub、cluster 或补齐叙事结构。

## 任务边界

drafting worker 只允许读取当前任务包、第一轮 `fact_candidates.md` 和 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:13`。不得读取父聊天上下文、旧审计报告、未列出来源、已采纳 KB 卡片或 provenance。

## 生命周期判断

本轮 drafting 是单候选、短证据范围任务。当前还没有重复大规模来源 I/O 的证据，因此继续使用一次性 worker；完成后主控 agent 关闭该 sub-agent。
