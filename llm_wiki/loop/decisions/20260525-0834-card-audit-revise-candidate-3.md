# 第二轮候选 3 审计要求修订

- `timestamp`: `2026-05-25T08:34:50+08:00`
- `iteration_id`: `iteration_20260525_0053_card_audit_idea_file_agent_builds`
- `task_id`: `task_20260525_0054_card_audit_candidate_3`
- `sub_agent`: `019e5c8b-3deb-7063-9c6a-fccc19a2fc46`
- `decision`: `revise_required`

## 审计结论

`card_audit_worker` 返回 `audit_result: revise`。审计认为核心事实可由 `data/raw/webpage/karpathy-x-launch-post/raw.json` 的 `$.tweet.text` 支撑，卡片保持原子事实边界，未漂移到 hub、cluster 或 topic coverage。

## 需要修订的点

草稿卡 statement 使用了“Karpathy 的发布帖”这一归属语，但本轮 audit 任务允许的来源证据字段只有 `$.tweet.text`，该字段本身不直接证明发帖者身份。审计建议将该表述改为“这条发布帖”或“该来源帖文”，除非另行允许使用作者元数据字段。

## 判断

这是一个可由同一 drafting worker 最小修订解决的来源支撑边界问题，不是事实候选失败、来源不足、上下文泄漏或 schema 问题。主控 agent 不直接改知识卡正文；下一步创建 revision drafting 任务包。

## 生命周期记录

本轮 `card_audit_worker` 是 one-shot worker，完成后已关闭。审计只涉及一张草稿卡和一个来源字段，不需要 alive sub-agent 常驻。

## 下一步

创建 `card_drafting_worker` revision 任务：只修订候选 3 草稿卡和 provenance 中超出允许证据字段的归属语，优先改为“这条发布帖”或“该来源帖文”，不得扩大来源证据、不得引入作者元数据、不得改成主题页。
