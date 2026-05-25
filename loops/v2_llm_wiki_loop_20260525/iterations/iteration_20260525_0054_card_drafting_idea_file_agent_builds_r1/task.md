# 第二轮候选 3 知识卡草稿修订任务

- `task_id`: `task_20260525_0055_card_drafting_candidate_3_revision`
- `iteration_id`: `iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1`
- `role`: `card_drafting_worker`
- `main_language`: 中文

## 目标

根据 audit revise 报告，对第二轮候选 3 草稿卡和 provenance 做最小修订，使 statement 中的归属语完全由允许的来源证据字段支撑。只修订同一张草稿卡和 provenance，不写新主题页，不采纳。

## 修订要求

- 将草稿卡 statement 中的 “Karpathy 的发布帖” 改为 “这条发布帖” 或 “该来源帖文”。
- 如 provenance 中存在同类未被 `$.tweet.text` 直接证明的归属语，也做同样收窄。
- 不扩大来源证据；不要新增作者元数据、帖子作者字段或其它 JSON 字段来支撑 “Karpathy”。
- 保持事实核心不变：该帖把 `idea file` 表述为在 LLM agents 时代分享想法而非具体代码或应用，使接收者的 agent 能按需求定制和构建。

## 允许输入

- 当前任务包。
- `previous_draft_card_path`: `llm_wiki/loop/iterations/iteration_20260525_0052_card_drafting_idea_file_agent_builds/artifacts/draft_card.md`
- `previous_provenance_path`: `llm_wiki/loop/iterations/iteration_20260525_0052_card_drafting_idea_file_agent_builds/artifacts/provenance.md`
- `audit_report_path`: `llm_wiki/loop/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/artifacts/audit_report.md`
- `fact_candidate_path`: `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md` 仅限 candidate 3。
- `source_evidence_path`: `data/raw/webpage/karpathy-x-launch-post/raw.json`
- `source_evidence_json_pointer`: `$.tweet.text`

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- 旧审计报告。
- 已采纳 KB 卡片或 provenance；不得用 KB 内容补充事实支撑。
- `source_evidence_path` 中 `source_evidence_json_pointer` 之外的字段，不可作为补充事实证据。
- `fact_candidate_path` 中 candidate 3 之外的候选，不可作为补充事实证据。
- 枢纽页、聚类页或主题覆盖文档。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/artifacts/draft_card.md`
- `llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1/artifacts/provenance.md`

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

## 成功门禁

- 只生成一张修订版草稿卡。
- 修订点能对应 audit report 的 `required_changes`。
- `statement` 不再包含未由 `$.tweet.text` 直接证明的 “Karpathy 的发布帖” 归属语。
- 未扩大来源证据、未新增复杂元数据、未生成 hub/cluster/topic coverage。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 不读取作者元数据就无法修订。
- 需要改动事实核心而非归属语。
- 需要额外来源才能支撑事实。
