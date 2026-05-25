# 任务包模板：来源挖掘

- `task_id`: `task_20260525_0003_source_mining_bootstrap`
- `iteration_id`: `iteration_20260525_0002_source_mining_karpathy_gist`
- `role`: `source_mining_worker`
- `main_language`: 中文

## 目标

从一个指定本地来源中抽取事实候选。只抽取来源能够支撑的事实，不写知识卡，不做采纳。

选源规则：一次只选一个具体来源。选择依据是本地可读性、来源质量和是否适合产生清楚事实候选，不按主题覆盖、聚类或枢纽页规划来选源。

## 选源决策

- `source_id`: `karpathy-gist-llm-wiki`
- `source_title`: `Andrej Karpathy LLM Wiki / LLM Knowledge Bases idea file`
- `source_type`: `gist_raw`
- `selection_reason`: `status: ok`；本地已获取；`gist_raw` 接近原始来源；目录中存在 `raw.txt` / `text.txt` 可供 worker 读取；适合第一轮 bottom-up 挖掘清楚事实候选；不需要网络 retrieve；不是按主题覆盖、topic 平衡、hub 或 cluster 规划选源。

## 允许输入

- 当前任务包。
- `source_manifest`: `data/manifests/acquired_sources_index.md`
- `source_path`: `data/raw/gist_raw/karpathy-gist-llm-wiki`
- 必要时可读取：
  - `data/manifests/acquired_sources_index.md`
  - `data/manifests/sources.jsonl`

## 禁止输入

- 父聊天上下文。
- 旧版 `legacy/` 产物。
- 旧审计报告。
- 未在本任务包中列出的其它来源。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
- 可选：`llm_wiki/kb/candidates/karpathy-gist-llm-wiki.md`

## 输出要求

每个事实候选至少包含：

- `statement`
- `fact_type`: `known_fact` 或 `accepted_fact`
- `support`
- `scope`
- `source_evidence`
- `draft_status`: `candidate`

## 成功门禁

- 至少产出 3 个事实候选，除非来源内容不足。
- 每个候选都能追溯到来源中的具体段落、文件或片段。
- 没有生成枢纽页、聚类或主题覆盖。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 来源文件不存在。
- 来源内容不可读。
- 来源不包含足够事实。
- 需要访问网络但公司网络限制导致失败。

阻塞时写 `LOOP_BLOCKED`，并记录证据。
