# Justification: obsidian-wiki-agent-agnostic-skill-framework

## 为什么产出此卡
"代理无关"是该框架区别于特定工具插件的核心设计决策，材料在多处强调这一特性（Header、Agent Compatibility 整章、Project Structure 中的 symlink 结构）。

## Evidence basis 判定
选择 `code_implementation`：README 描述的 symlink 机制、setup.sh 行为和目录结构均为实际代码实现。

## 原子性
本卡聚焦于 agent-agnostic 这一设计决策及其通过 skill 文件 + symlink 的实现方式，不涉及具体的知识处理流程。
