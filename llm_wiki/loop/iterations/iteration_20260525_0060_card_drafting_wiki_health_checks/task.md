# 任务包模板：知识卡草稿

- `task_id`: `task_20260525_0061_card_drafting_candidate_12`
- `iteration_id`: `iteration_20260525_0060_card_drafting_wiki_health_checks`
- `role`: `card_drafting_worker`
- `main_language`: 中文

## 目标

把一个事实候选写成一张 zet 风格原子事实知识卡，并写一份整理后的出处论证。

## 选定候选

- `candidate_id`: `候选 12`
- `candidate_statement`: 被引用推文称会让 LLM 对 wiki 做 `health checks`，例如发现不一致数据、补全缺失数据、寻找新文章候选的有趣连接，以逐步提升数据完整性。
- `candidate_fact_type`: `known_fact`
- `candidate_scope`: 仅限被引用推文对 wiki 检查和清理方式的描述。
- `candidate_source_evidence`: `data/raw/webpage/karpathy-x-launch-post/raw.json`, JSON pointer `$.tweet.quote.text`

选择理由：候选 12 的证据集中在一个 JSON 字段，事实边界清楚；它记录的是被引用推文对 wiki 检查和清理方式的描述，不重复已采纳的 ingest flow、query answer writeback 或 idea file 卡。选择不基于主题覆盖、hub、cluster 或补齐叙事结构。

只处理 `候选 12`。`fact_candidates.md` 只可用于核对 `候选 12` 的字段，不得把其它候选写成知识卡或混入本卡。不得读取已采纳 KB 卡片来补充事实。

由于允许的来源证据只包括 `$.tweet.quote.text`，知识卡和 provenance 不要使用未由该字段直接支撑的作者身份、发布时间或外部背景；可使用“被引用推文”或“该 quote text”。

## 允许输入

- 当前任务包。
- `fact_candidate_path`: `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md` 仅限任务指定的单个候选块。
- `source_evidence_path`: `data/raw/webpage/karpathy-x-launch-post/raw.json`
- `source_evidence_json_pointer`: `$.tweet.quote.text`

## 候选读取边界

- 读取 `fact_candidates.md` 时，只读取当前任务指定的候选块。
- 不把带上下文的关键词检索结果当作候选证据。
- 如果工具输出暴露相邻候选字段，必须改用精确候选块读取；相邻候选内容不得进入知识卡、provenance 或审计证据，并要写入 `read_log.md`。

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- 旧审计报告。
- 其它主题页或枢纽页。
- 相邻事实候选的字段、标题或表述。
- 已采纳 KB 卡片或 provenance；不得用 KB 内容补充事实支撑。
- `source_evidence_path` 中 `source_evidence_json_pointer` 之外的字段，不可作为补充事实证据。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0060_card_drafting_wiki_health_checks/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0060_card_drafting_wiki_health_checks/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0060_card_drafting_wiki_health_checks/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0060_card_drafting_wiki_health_checks/artifacts/draft_card.md`
- `llm_wiki/loop/iterations/iteration_20260525_0060_card_drafting_wiki_health_checks/artifacts/provenance.md`

## 知识卡要求

知识卡应该是结果，不是流程日志。

必须包含极简契约：

- `statement`
- `fact_type`
- `support`
- `scope`
- `status: draft`

写作要求：

- 标题短。
- 正文只围绕一个主要事实。
- 可以有简短解释，但不能扩写成主题页。
- `References` 必须放在 `Footnotes` 前。
- `Footnotes` 必须是最后一个 section。

## 出处论证要求

出处论证说明这张卡为什么可以暂时被当作事实：

- 事实从哪里来。
- 来源为什么能支撑它。
- 哪部分是来源明说的。
- 哪部分是整理后的表述。
- 成立范围是什么。
- 当前为什么只能是 `draft`。

## 成功门禁

- 只生成一张知识卡。
- 知识卡可读，不像中间状态。
- 出处论证可读，不是流水日志。
- 没有新增复杂元数据。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 事实候选不够清楚。
- 来源证据不足。
- 需要额外来源才能支撑事实。
