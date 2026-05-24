# 选择候选 6 进入 drafting

- `timestamp`: `2026-05-25T07:27:13+08:00`
- `decision`: `select_candidate_for_card_drafting`
- `candidate_id`: `候选 6`
- `next_iteration_id`: `iteration_20260525_0044_card_drafting_llm_wiki_use_cases`
- `next_task_id`: `task_20260525_0045_card_drafting_candidate_6`

## 选择理由

候选 6 是第一轮 source mining 中最后一个未进入 drafting 的候选。它的形态是应用场景清单，原子性弱于前几张卡；但可以收窄为一条可审计的清单型原子事实：该来源列举了一组 LLM Wiki 可能适用的场景。任务包必须禁止把每个场景扩展成主题说明或覆盖报告。

本次选择基于来源证据集中、候选可被收窄为一个来源列举事实，以及完成当前候选集的价值；不基于主题覆盖、hub、cluster、topic 平衡或补齐叙事结构。

## 与已采纳卡片的关系

已采纳卡片覆盖了 LLM Wiki 的模式定位、RAG 对比、持久 wiki 模式、复合产物性质、人机分工、架构层、raw sources、wiki 层、schema、ingest 和 query。候选 6 只记录该来源列举的使用场景，不应扩写为用例体系，也不应作为 hub。

## 生命周期判断

继续使用 one-shot `card_drafting_worker`。候选 6 的来源证据只有 `raw.txt:17-23`，不构成使用 alive worker 常驻以节省大规模 I/O 的证据。
