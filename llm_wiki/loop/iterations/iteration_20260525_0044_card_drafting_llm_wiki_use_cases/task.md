# 任务包模板：知识卡草稿

- `task_id`: `task_20260525_0045_card_drafting_candidate_6`
- `iteration_id`: `iteration_20260525_0044_card_drafting_llm_wiki_use_cases`
- `role`: `card_drafting_worker`
- `main_language`: 中文

## 目标

把一个事实候选写成一张 zet 风格原子事实知识卡，并写一份整理后的出处论证。

## 选定候选

- `candidate_id`: `候选 6`
- `candidate_statement`: 该来源列举 LLM Wiki 可用于个人记录、长期研究、读书陪伴 wiki、业务团队内部 wiki，以及竞争分析、尽调、旅行规划、课程笔记和兴趣深挖等场景。
- `candidate_fact_type`: `known_fact`
- `candidate_scope`: 仅限该来源列举的可能应用场景。
- `candidate_source_evidence`: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:17-23`

选择理由：候选 6 是来源列举的应用场景清单。它只能被收窄为“该来源列举了一组可能适用场景”这一清单型原子事实，不得扩写成场景报告、用例体系、hub、cluster 或 topic coverage。本次选择基于来源证据集中、候选可被收窄为一个来源列举事实，以及完成当前候选集的价值；不基于主题覆盖、hub、cluster 或补齐叙事结构。

只处理 `候选 6`。`fact_candidates.md` 只可用于核对 `候选 6` 的字段，不得把其它候选写成知识卡或混入本卡。不得读取已采纳 KB 卡片来补充事实。

## 允许输入

- 当前任务包。
- `fact_candidate_path`: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
- `source_evidence_path`: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- `source_evidence_lines`: `17-23`

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- 旧审计报告。
- 其它主题页或枢纽页。
- 已采纳 KB 卡片或 provenance；不得用 KB 内容补充事实支撑。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/artifacts/draft_card.md`
- `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/artifacts/provenance.md`

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
