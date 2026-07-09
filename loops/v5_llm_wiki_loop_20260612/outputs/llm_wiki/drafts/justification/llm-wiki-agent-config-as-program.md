# Justification: llm-wiki-agent-config-as-program

## 抽取理由
该卡片捕获 LLM Wiki Agent 的 "config-as-program" 设计范式——通过 agent config 文件（而非 API/CLI）来编程 coding agent 行为。这是该项目的独特分发和交互模式，与传统工具的安装/使用方式有质的区别。

## 证据强度
- evidence_basis: `code_implementation` — 仓库中实际存在 CLAUDE.md / AGENTS.md / GEMINI.md 文件，README 的 Install 部分明确说明了这种使用方式
- 项目自称 "coding agent skill"，明确不是独立应用

## 边界标注
- "config-as-program" 是提取者对该模式的概括命名，材料原文使用 "The schema file tells the agent how to maintain the wiki"
- 该范式的有效性取决于各 coding agent 对 config 文件的支持程度（Claude Code 支持最完整，含 slash commands）
