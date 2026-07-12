# 公开交互档案隐私审计（Privacy Audit）

## 审计结论

当前公开档案可以进入 Git publish。结论只适用于 `docs/claude_interaction_replay/` 中经过处理的 Markdown、registry、JSONL events 和 HTML，不适用于本机原始 Codex / Claude Code session 文件。Claude Code agent-effort 会话的原始工具输出曾包含高风险配置字面量；这些输出未进入公开事件，只有经审阅的人类输入和摘要被保留。

## 审计范围

- 10 个 Codex 与 9 个 Claude Code 顶层 session 的全集审计。
- 14 个纳入会话：9 个 Codex、5 个 Claude Code；其余会话均有明确排除理由。
- 324 条确认的人类用户输入或直接命令动作。
- 与每条输入相邻的用户可见助手输出窗口。

## 处理结果

- 283 条用户输入可原样发布。
- 41 条输入使用明确占位符脱敏。
- 绝对路径替换为 `<workspace>`、`<local-cli>` 等语义占位符。
- 私人 ChatGPT / Claude 会话链接替换为 `[私人会话链接]`。
- provider 邮箱、设备性质和其他可关联身份的字面量被移除。
- 公开 session、event 和 message identifier 改为语义化 alias 或 ordinal。
- 原始 locator 仅存在于 `registry/local-source-locators.json`；该文件被 `.gitignore` 排除。
- 公开的 `registry/session-audit.json` 只使用语义 alias，不包含本机 UUID 或绝对路径。

## 明确排除

- 原始 `~/.codex/**` 和 `~/.claude/**` JSONL。
- system / developer / AGENTS / environment context。
- tool result、命令输出、token usage、订阅或额度信息。
- compaction summary、platform event、encrypted 或隐藏推理。
- sub-agent task packet 中伪装成 `role=user` 的代理输入。
- 第三方网页、论文和仓库的全文副本。

## 保留内容

用户自己的项目判断、改变主意、纠偏、写作偏好、agent 编排观点和公开来源链接属于 recall 所需内容，保留在档案中。时间精确到分钟，便于恢复版本顺序；它可能暴露工作节奏，但不包含账号或组织身份。

## 可复核性

每条事件仍保存 `source_record_sha256`。在拥有本机原始 session 的环境中，可以重新计算 source record hash 完成精确对账，而无需在公开 repo 中保存原始 UUID 或绝对路径。

运行以下命令可重新执行 schema、覆盖率、分片哈希、用户文本哈希和敏感模式检查：

```bash
python docs/claude_interaction_replay/tools/validate_archive.py
```
