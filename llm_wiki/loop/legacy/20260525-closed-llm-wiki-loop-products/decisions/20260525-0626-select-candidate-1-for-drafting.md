# 选择候选 1 进入知识卡草稿

- `decision_time`: `2026-05-25T06:26:57+08:00`
- `controller`: `main-agent`
- `decision`: `select_candidate_for_card_drafting`
- `candidate_id`: `候选 1`
- `iteration`: `iteration_20260525_0036_card_drafting_llm_wiki_pattern_file`
- `task`: `task_20260525_0037_card_drafting_candidate_1`
- `worker_role`: `card_drafting_worker`
- `dispatch_policy`: `fork_context:false`

## 判断

从第一轮 source mining 的剩余候选中选择候选 1 进入 drafting。候选 1 的证据集中在 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:1-5`，事实边界是该来源如何描述 “LLM Wiki” 模式与该文件用途。

## 选择理由

- 本地来源可读，证据范围短且集中在开头。
- 候选陈述有清晰的文档定位边界，适合写成一张原子事实知识卡。
- 与已采纳的架构层、流程、产物性质和 RAG 对比事实不重复。
- 本次选择不基于主题覆盖、hub、cluster 或补齐叙事结构。

## 任务边界

drafting worker 只允许读取当前任务包、第一轮 `fact_candidates.md` 和 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:1-5`。不得读取父聊天上下文、旧审计报告、未列出来源、已采纳 KB 卡片或 provenance。

## 生命周期判断

本轮 drafting 是单候选、短证据范围任务。当前还没有重复大规模来源 I/O 的证据，因此继续使用一次性 worker；完成后主控 agent 关闭该 sub-agent。
