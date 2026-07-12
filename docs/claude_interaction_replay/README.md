# LLM Wiki 构建回忆档案（Build Memory Archive）

## 目标

这套档案用于还原用户怎样通过 Codex 与 Claude Code 从 v0 到 v5 构建 LLM Wiki。它不把聊天记录当日志堆放，而是把用户输入、模型核心摘要、关键决策、实际动作、仓库产物和版本迁移连接成可复核的回忆路径：

```text
问题 → 决策 → 动作 → 产物 → 下一版触发条件
```

当前状态是 **Schema v2 + v0-v5 顶层会话全集已审计**。本机发现的 session universe 为 10 个 Codex 顶层 session 和 9 个 Claude Code 顶层 session；每个会话都已在 `registry/session-audit.json` 中标记为纳入、排除或档案构建会话，并写明理由。14 个相关会话共归档 324 条人类输入或直接命令动作。

## 数据边界

```text
content/                 人类可读的版本叙事和版本比较
events/*.jsonl           一行一条 human user input 锚定事件
registry/                版本、来源和事实证据映射
modules/                 入库/审计机制的结构化 module recall
research/                分阶段证据审计与扩展前自审记录
schema/                  可校验的数据合同
archive.json             覆盖率、隐私门禁和生成视图清单
index.html               可删除、可重建的回忆界面
demo/                    旧 v1 citation 讨论 demo，作为迁移样本保留
```

事实责任分开保存：

- Markdown 解释一个版本为什么存在，以及它相对上一版改变了什么。
- JSONL 保留按顺序排列的用户输入、助手核心摘要、动作与效果。
- Registry 保存 source id、session、版本归属、仓库路径和证据映射。
- Session audit 保存全部顶层会话的发现口径、纳入/排除决定和隐私风险。
- Query timeline 只保存关键 event annotation；全部原文仍来自 events。
- Module JSON 1.1 区分设计、执行、失败、后验与反证；模块和阶段都保存 justification、observation、assumption 状态，并引用既有 event/artifact。
- HTML 只负责展示，不是新的事实源。

## 人类输入判定

Codex 顶层 session 的候选规则：

```text
type == "event_msg" && payload.type == "user_message"
```

`response_item.role=user` 可能包含环境上下文、AGENTS、工具通知和 sub-agent task packet，不能直接计为人类输入。sub-agent 的 `role=user` 是代理任务包，只能作为动作或效果证据。

Claude Code 的 `type=user` 同样可能是 `tool_result`、slash command envelope 或 compaction summary，必须先分类作者身份。

## 原始记录位置

Codex：

```text
~/.codex/sessions/YYYY/MM/DD/rollout-<timestamp>-<session-id>.jsonl
~/.codex/archived_sessions/*.jsonl
```

Claude Code：

```text
~/.claude/projects/<project-key>/<session-id>.jsonl
~/.claude/projects/<project-key>/<session-id>/subagents/
```

原始 JSONL 永远是 `local-only`，不会随本目录公开。公开事件只使用语义化 alias；本机精确路径保存在被 `.gitignore` 排除的 `registry/local-source-locators.json`。

## 不可变规则（Invariants）

- 选定 session 或版本窗口后，所有确认的 human-authored 用户输入必须逐条进入档案。
- 重复输入、纠正、制止执行和改变主意不能去重。
- 助手输出只保存 `not_verbatim` 核心摘要，不保存隐藏推理。
- session time、文档声明时间、文件观测时间和 Git 时间分开记录。
- 首次 Git commit 不能被自动解释为想法或文件的出生时间。
- 冲突状态与指标必须并列保存，不能静默选择一个“正确”数字。
- 未通过隐私复核的事件不能进入公开 HTML。

## 版本索引

| 版本 | 核心 |
|---|---|
| v0 | filesystem-backed 机制验证；topic 错位 |
| v1 | 自顶向下的 8 个主题枢纽 |
| v2 | 自底向上的 scoped knowledge cards |
| v3 | draft-first、相似卡比较、融合与统一 citation |
| v4 | 独立 0→1 questioner/reader 循环与 FSJS |
| v5 | source router、evidence basis 和规模化图治理 |

## 本地查看

在本目录启动静态文件服务后打开本机预览地址。页面提供版本、交互时间线、机制和跨版本对比四个视图，每个 Tab 使用自己的上下文节点：版本 Tab 导航 v0-v5，交互 Tab 导航版本与交互阶段，机制 Tab 导航 flow、design 与 stages，对比 Tab 导航比较维度。机制阶段内按设计逻辑、执行合同、版本演化、证据与缺口纵向展开，并可从设计依据回跳到完整用户交互。

## 当前覆盖

- 324 条 human-authored 用户输入或直接命令动作，324 个唯一事件。
- 15 个事件分片，覆盖 14 个与 v0-v5 相关的顶层会话。
- 41 条输入经过明确脱敏；其余 283 条可原样发布。
- 10 个 Codex 与 9 个 Claude Code 顶层会话已全部完成纳入/排除审计；排除的是无语义内容、无关 general chat 或会造成递归的档案构建会话。
- v0-v5 六个版本已有版本叙事、相对变化、recall trail 和分阶段交互回放。
- v0-v5 六版 query timeline 已完整标注，默认显示 87 个关键节点，并可切换全部 324 条输入、点击回到用户原文。
- 入库机制已覆盖 8 个稳定阶段的 v0-v5 evolution；审计机制已覆盖 7 个阶段和 10 个 control evolution；15 个阶段均有带事件证据的 why、observation 与 assumption。
- 完整模块会强制校验 6/6 版本、event 引用和 artifact 路径；结构 PASS、流程合规与知识质量保持为不同 verdict。
- sub-agent 不计为人类输入；其动作和效果已进入主事件摘要，后续仍可扩展独立 agent-action index。
