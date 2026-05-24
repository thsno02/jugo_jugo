# 选择候选 5 进入 drafting

- `timestamp`: `2026-05-25T07:04:09+08:00`
- `decision`: `select_candidate_for_card_drafting`
- `candidate_id`: `候选 5`
- `next_iteration_id`: `iteration_20260525_0041_card_drafting_human_llm_roles`
- `next_task_id`: `task_20260525_0042_card_drafting_candidate_5`

## 选择理由

候选 5 的事实边界相对清楚：它描述该来源中的人机分工，而不是扩大为 LLM Wiki 的整体方法论或主题页。候选 5 的证据分布在 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:15-16` 和 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:68-69`；前者说明用户通常不直接写 wiki，后者说明用户与 LLM agent 的分工。

本次选择基于本地可读性、来源质量、事实候选清晰度和当前 loop 价值；不基于主题覆盖、hub、cluster、topic 平衡或补齐叙事结构。

## 与已采纳卡片的关系

已采纳卡片覆盖了 raw sources、三层架构、schema、wiki 层、持久 wiki 模式、RAG 对比、ingest、query、持久复合产物和模式文件定位。候选 5 聚焦人机分工，不重复这些已采纳事实。

## 生命周期判断

继续使用 one-shot `card_drafting_worker`。候选 5 的来源证据行数较少，不构成使用 alive sub-agent 常驻以节省大规模 I/O 的证据。
