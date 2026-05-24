# 用户洞察记录（临时 fallback）

本目录是在正式 `user-insights` skill 路径被确认前创建的临时 fallback。

现在 canonical 记录目标已经更正为仓库顶层：

```text
user-insights/
```

本目录只保留为 bootstrap 历史痕迹，后续增量记录由专用 `user-insights` sidecar 写入顶层目录。

记录原则：

- 中文为主。
- 不把用户表达改写成过度抽象的管理口号。
- 区分“用户明确要求”和“从对话中推断出的偏好”。
- 记录对系统设计有持续影响的内容。
