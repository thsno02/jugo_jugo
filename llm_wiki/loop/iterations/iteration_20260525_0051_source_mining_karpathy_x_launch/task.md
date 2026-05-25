# 任务包模板：来源挖掘

- `task_id`: `task_20260525_0052_source_mining_karpathy_x_launch`
- `iteration_id`: `iteration_20260525_0051_source_mining_karpathy_x_launch`
- `role`: `source_mining_worker`
- `main_language`: 中文

## 目标

从一个指定本地来源中抽取事实候选。只抽取来源能够支撑的事实，不写知识卡，不做采纳。

选源规则：一次只选一个具体来源。选择依据是本地可读性、来源质量和是否适合产生清楚事实候选，不按主题覆盖、聚类或枢纽页规划来选源。

## 选定来源

- `source_id`: `karpathy-x-launch-post`
- `source_type`: `webpage`
- `source_url`: `https://api.fxtwitter.com/karpathy/status/2040470801506541998`
- `source_path`: `data/raw/webpage/karpathy-x-launch-post`
- `local_files`: `metadata.json`, `raw.json`, `raw.txt`, `text.txt`

选择理由：这是 Karpathy 发布语境的 API mirror，本地状态为 `ok`，目录小且结构清楚；相比评论线程或二级介绍，更适合先挖掘直接来源支持的事实候选。选择依据是本地可读性、来源质量、事实候选可能清晰度和当前 loop 价值，不基于主题覆盖、hub、cluster 或叙事补齐。

生命周期判断：本轮只处理一个约 40K 的本地来源目录，不涉及跨多来源重复读取，因此使用 one-shot `source_mining_worker`；若后续同一大型来源需要多轮反复读写，再另行记录 alive sub-agent 决策。

## 允许输入

- 当前任务包。
- `source_manifest`: `data/manifests/sources.jsonl`
- `source_path`: `data/raw/webpage/karpathy-x-launch-post`
- 必要时可读取：
  - `data/manifests/acquired_sources_index.md`
  - `data/manifests/sources.jsonl`

## 禁止输入

- 父聊天上下文。
- 旧版 `legacy/` 产物。
- 旧审计报告。
- 未在本任务包中列出的其它来源。
- `user-insights/` 不可作为事实来源。
- 其它 KB 卡片或 provenance 不可作为事实来源。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md`
- 可选：`llm_wiki/kb/candidates/karpathy-x-launch-post.md`

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
