# 任务包模板：知识卡草稿

- `task_id`: `task_20260525_0034_card_drafting_candidate_4`
- `iteration_id`: `iteration_20260525_0033_card_drafting_persistent_composite_wiki`
- `role`: `card_drafting_worker`
- `main_language`: 中文

## 目标

把一个事实候选写成一张 zet 风格原子事实知识卡，并写一份整理后的出处论证。

## 选定候选

- `candidate_id`: `候选 4`
- `candidate_statement`: 在该来源中，wiki 被定位为会随新增来源和提问持续变丰富的持久复合产物，其中交叉引用、矛盾标记和综合内容会被保留下来。
- `candidate_fact_type`: `known_fact`
- `candidate_scope`: 仅限该来源对 LLM Wiki 产物性质的描述。
- `candidate_source_evidence`: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:13`

选择理由：候选 4 的证据集中在单行，事实边界是 wiki 产物会保留链接、矛盾标记和综合内容并持续变丰富；它与已采纳的“持久 wiki 替代模式”相邻但不重复，后者强调替代 RAG 的持久 wiki 模式，本候选强调持久复合产物的保留内容类型。本次选择基于本地可读性、来源质量、事实候选清晰度和当前 loop 价值，不基于主题覆盖、hub、cluster 或补齐叙事结构。

只处理 `候选 4`。`fact_candidates.md` 只可用于核对 `候选 4` 的字段，不得把其它候选写成知识卡或混入本卡。不得读取已采纳 KB 卡片来补充事实。

## 允许输入

- 当前任务包。
- `fact_candidate_path`: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
- `source_evidence_path`: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- `source_evidence_lines`: `13`

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- 旧审计报告。
- 其它主题页或枢纽页。
- 已采纳 KB 卡片或 provenance；不得用 KB 内容补充事实支撑。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/artifacts/draft_card.md`
- `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/artifacts/provenance.md`

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
