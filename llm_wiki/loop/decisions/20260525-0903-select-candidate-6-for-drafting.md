# 选择第二轮候选 6 进入 drafting

- `timestamp`: `2026-05-25T09:03:27+08:00`
- `source_iteration`: `iteration_20260525_0051_source_mining_karpathy_x_launch`
- `selected_candidate`: `候选 6`
- `next_iteration`: `iteration_20260525_0057_card_drafting_idea_file_abstract_vague`
- `next_task_id`: `task_20260525_0058_card_drafting_candidate_6`
- `decision`: `ready_for_card_drafting`

## 选择理由

选择候选 6，因为它直接来自 `data/raw/webpage/karpathy-x-launch-post/raw.json` 的 `$.tweet.text`，事实边界清楚：这条发布帖说明该 `idea file` 有意保持一定抽象和模糊，因为可发展方向很多，并提到人们可以调整该想法或在 Discussion 中贡献自己的版本。

该候选与已采纳的 `idea-file-share-the-idea` 不重复：已采纳卡记录的是 `idea file` 的分享逻辑，本候选记录的是这条发布帖对 idea file 抽象程度和参与方式的说明。该选择不基于主题覆盖、hub、cluster 或叙事补齐。

## 边界记录

由于本轮允许的来源证据只使用 `$.tweet.text`，drafting task 明确要求避免未由该字段直接支撑的作者归属语；知识卡可使用“这条发布帖”或“该来源帖文”表述。

## 生命周期记录

本轮任务仍是单张卡 drafting，来源字段小且边界清楚，不需要 alive sub-agent 常驻。若后续连续处理 `$.tweet.quote.text` 中多个长段落并出现重复大 I/O，再重新评估 alive worker。
