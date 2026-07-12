# GitHub Issues 全量发布

本目录保存从公开交互档案到 `thsno02/jugo_jugo` GitHub Issues 的发布包和可逆映射。

## 发布状态

- 状态：`complete`（2026-07-12）
- 根索引：[`#5 LLM Wiki 是如何从原始资料库逐步演化到 v5 的？`](https://github.com/thsno02/jugo_jugo/issues/5)
- 正式节点：57 个（1 个根 Issue、6 个版本 ChangeLog、50 个问题 Issue）
- canonical 事件：324 个，当前分布在 146 条 episode comments；事件 ID 无缺失、无重复、无额外项
- 版本叙事：v0-v5 六个 ChangeLog 各有两条 origin / delta comments
- 可读性整改：324 条逐事件模板重组为 146 条阶段叙事，旧模板残留为 0
- 状态收口：41 个历史节点关闭；16 个待继续问题保持 open

## 不变量

- 324 个已审阅事件都必须有 canonical GitHub comment 位置。
- 用户原话使用公开档案中的脱敏 verbatim，不再二次改写。
- 助手内容只保存核心洞察、动作和效果摘要。
- Issue body 保持短；推理过程进入 comments。
- 新问题从触发它的 comment 派生，并建立 parent/sub-issue 或 cross-link。
- Mermaid 用于真实流程和分支，并附文字解释。
- 原始 session UUID、本机路径和凭据不发布。

## 文件

- `packets-*.json`：分版本发布包，由审计 worker 生成。
- `github-publication-map.json`：Issue、comment 与 archive event 的公开映射。
- `../remediation/`：阶段叙事源文件、版本叙事、迁移前备份和整改后的 comment 映射。
