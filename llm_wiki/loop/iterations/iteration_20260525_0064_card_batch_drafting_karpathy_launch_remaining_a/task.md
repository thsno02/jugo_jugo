# 任务包：批量知识卡草稿

- `task_id`: `task_20260525_0066_card_batch_drafting_karpathy_launch_remaining_a`
- `iteration_id`: `iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a`
- `role`: `card_batch_drafting_worker`
- `main_language`: 中文

## 目标

把 `karpathy-x-launch-post` 的 6 个剩余高价值事实候选批量写成 atomic draft cards。每个候选最多一张卡；每张卡必须有 provenance。本轮只做 draft，不做相似门、审计、融合或采纳。

## 选定候选

- `候选 2`: 发布帖说被引用前帖传播很广，并想用 `idea file` 分享略有改进的版本。
- `候选 4`: 发布帖把 `idea file` 指向 GitHub Gist，card 标题为 `llm-wiki`。
- `候选 5`: 发布帖说读者可以把 gist 给自己的 agent，让 agent 构建个人 LLM wiki 并指导使用。
- `候选 8`: quote text 描述 raw/ 目录与 LLM 增量编译 Markdown wiki 的流程。
- `候选 9`: quote text 描述 wiki 包含 raw 数据摘要、backlinks、concepts 文章和链接。
- `候选 10`: quote text 描述 Obsidian IDE frontend，以及 wiki 由 LLM 写作和维护。

不处理 `候选 1` 和 `候选 7`，因为它们主要是元数据候选，首批先处理更有知识卡价值的流程/用法候选。不处理 `候选 3`、`候选 6`、`候选 11`、`候选 12`，因为它们已经 drafting 或 adoption。

## 允许输入

- 当前任务包。
- `fact_candidate_path`: `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md`
- `allowed_candidates`: `候选 2`, `候选 4`, `候选 5`, `候选 8`, `候选 9`, `候选 10`
- `source_evidence_path`: `data/raw/webpage/karpathy-x-launch-post/raw.json`
- `source_evidence_pointers`: `$.tweet.text`, `$.tweet.card.url`, `$.tweet.card.title`, `$.tweet.card.domain`, `$.tweet.quote.text`

## 候选读取边界

- 读取 `fact_candidates.md` 时，只读取本任务列出的 6 个候选块。
- 不把带上下文的关键词检索结果当作候选证据。
- 如果工具输出暴露未授权候选字段，必须丢弃该结果，改用精确候选块读取，并在 `read_log.md` 记录边界噪声。
- 不读取已采纳 KB 卡片来判断重复或融合；相似门会在后续任务中处理。

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- 已采纳 KB 卡片或 provenance。
- 旧审计报告。
- `fact_candidate_path` 中未列入 `allowed_candidates` 的候选，不可作为本轮事实支撑。
- `source_evidence_path` 中未列入 `source_evidence_pointers` 的字段，不可作为本轮事实支撑。
- 枢纽页、聚类页或主题覆盖文档。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a/artifacts/draft_cards/`
- `llm_wiki/loop/iterations/iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a/artifacts/provenance/`
- `llm_wiki/loop/iterations/iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a/artifacts/batch_manifest.md`

## 知识卡要求

- 每张卡只表达一个主要事实。
- 标题短，正文可读，不像中间状态。
- 可以有简短解释，但不能扩写成主题页。
- `References` 必须放在 `Footnotes` 前。
- `Footnotes` 必须是最后一个 section。
- 每张卡必须包含 `statement`、`fact_type`、`support`、`scope`、`status: draft`。

## 出处论证要求

每份 provenance 说明：

- 事实从哪里来。
- 来源为什么能支撑它。
- 哪部分是来源明说的。
- 哪部分是整理后的表述。
- 成立范围是什么。
- 当前为什么只能是 `draft`。

## 命名要求

- 草稿卡文件名使用 `candidate-<number>-<short-slug>.md`。
- provenance 文件名与草稿卡 slug 对齐。
- `batch_manifest.md` 必须列出每个候选的 `candidate_id`、`result`、`draft_card_path`、`provenance_path`、`source_pointer`、`notes`。

## 成功门禁

- `artifacts/batch_manifest.md` 存在，并列出 6 个候选的结果。
- 每张 drafted 卡都有对应 provenance。
- 所有 drafted 卡都是 `status: draft`。
- 没有新增复杂元数据。
- 没有生成 hub、cluster 或 coverage 文档。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 候选列表与来源证据无法对应。
- 来源证据不足。
- 需要未列出的来源才能支撑事实。
