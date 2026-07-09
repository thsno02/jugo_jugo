# Justification: obsidian-wiki-compile-not-retrieve-pattern

## 为什么产出此卡
"编译式知识管理"是该项目的核心设计哲学和出发点，源于 Karpathy 的原始 gist。材料开头即定义此理念，CLAUDE.md 的 Core Principles 再次确认。这是理解该框架所有其他设计决策的基础。

## Evidence basis 判定
选择 `code_implementation`：虽然是设计哲学描述，但 README 和 CLAUDE.md 直接描述了实际运行框架的核心原则，且框架整体就是这一理念的代码实现。

## 原子性
本卡聚焦于"compile not retrieve"这一理念及 LLM-as-maintainer / Obsidian-as-viewer 的角色分工。具体的四阶段实现机制、agent-agnostic 设计等拆分为独立卡片。
