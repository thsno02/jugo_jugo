# Justification: llm-wiki-kit-mcp-tool-surface

## 为什么产出此卡

8 个 MCP 工具构成该项目的外部接口面，是 agent 实际可调用的能力集合。这是一个独立的 API surface 知识单元，与架构设计和问题定义正交。

## evidence_basis 选择: code_implementation

README 中的工具表直接对应代码实现的 MCP tool handlers，且提供了可执行的 serve 命令和配置示例。

## 卡片边界

本卡聚焦"agent 能做什么"（工具清单、连接配置方式、搜索能力）。不涉及内部 wiki 结构（见 wiki-architecture 卡）或宏观设计理念（见 persistent-agent-memory 卡）。

## 材料覆盖度

覆盖 README 的 Available Tools 表、Quickstart 中的 agent 配置部分、What Makes This Different 中的 FTS5 条目。
