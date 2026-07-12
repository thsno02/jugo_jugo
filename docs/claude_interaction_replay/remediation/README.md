# GitHub Comments 可读性整改

本目录记录 GitHub Issues 从逐事件模板（event-shaped comments）迁移为阶段叙事（episode-shaped comments）的过程。

## 为什么整改

首轮发布把 archive schema 直接渲染成 comment：一条 event 对应一条 comment，并重复展示「事件性质」「当时状态」「关键判断」等字段。它保证了机器覆盖，却破坏了人类 recall 所需的因果连续性。

整改后采用两层结构：

- 主阅读区讲清触发、误解、检查、纠正、动作、结果和遗留问题。
- 全部用户原始输入保存在 `<details>` 折叠区。
- event ID 保存在隐藏 marker；一个 episode comment 可以承载多个连续 event。

## 首轮试点

- 范围：GitHub Issues `#12`、`#17`、`#20`、`#44`、`#54`、`#59`。
- 事件：64 个，顺序和原话均保持不变。
- Comments：64 条逐事件模板重组为 24 条阶段叙事，删除 40 条碎片。
- 迁移策略：保留每个 episode 第一条旧 comment 的 ID 与 URL，原地更新正文，再删除被吸收的 comments。
- 质量检查：自动验证原话、event 顺序、唯一覆盖与远端正文；两轮无 archive 上下文盲读后通过。
- 状态检查：根据 episode 结尾重新判断 open/closed；`#17` 因完整 KB 与长期自治未完成而补充 reopen comment，其余五个试点状态与当前结论一致。

## 全量整改

- 剩余范围：45 个 Issue、260 个 event。
- Comments：260 条逐事件模板重组为 122 条阶段叙事，删除 138 条碎片。
- 全库结果：324 个 event 分布在 146 条 episode comments；146/146 均包含完整原话折叠区。
- 状态结果：57 个正式节点中 41 closed、16 open；8 个错误关闭的问题先补 reopen 说明再改状态。
- 版本结果：`#6` 至 `#11` 各增加两条 origin / delta 叙事；ChangeLog 作为完成的历史交接关闭，开放子问题保持独立状态。
- 盲读结果：v0-v2、v3、v4-v5 与版本层分别接受无 archive 上下文审查；所有首轮阻断项返修后通过。
- 远端核验：324 个 event ID 与 GitHub comment ID 逐项一致，旧字段模板残留为 0。

## 文件

- `pilot-v0-v1.json`、`pilot-v2-v3.json`、`pilot-v4-v5.json`：GitHub Markdown episode 正文与 event 分组。
- `full-*.json`：试点以外 260 个 event 的 episode 正文、状态判断与 reopen 说明。
- `version-changelogs.json`：v0-v5 的版本起点、相对变化、失败与交接叙事。
- `pilot-publication-map.json`：迁移后的 comment ID、URL 与删除记录。
- `full-publication-map.json`：全量迁移后的 comment、state transition 与删除记录。
- `version-publication-map.json`：六个 ChangeLog 的正文、comment 与状态映射。
- `backups/pilot-before-*.json`：迁移前的完整 GitHub API comment 快照。
- `backups/versions-before-*.json`：版本 tracker 更新前的 Issue 与 comment 快照。
- `../tools/remediate_github_comments.py`：默认 dry-run、显式 `--apply` 的备份与迁移工具。
- `../tools/publish_version_changelogs.py`：版本叙事的幂等发布、备份和状态同步工具。
