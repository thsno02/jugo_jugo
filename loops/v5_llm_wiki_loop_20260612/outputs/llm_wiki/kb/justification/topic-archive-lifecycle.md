# Justification: topic-archive-lifecycle

## 抽卡理由
Topic 归档生命周期是 v0.9.0 新增的主要功能，定义了一种"静默保留"策略——不删除、不出现在默认工作流中。它影响所有命令的 archive-awareness 行为。

## 证据强度
- archive.md 完整参考文档
- commands/archive.md 命令规格
- linting.md C19 规则
- 所有 command spec 都包含 "Archive awareness" 段
- README changelog v0.9.0 为该功能的版本记录
- evidence_basis: code_implementation

## 原子性检验
单一核心 idea：整个 topic wiki 的归档生命周期（移动到 .archive/ + 上下文隐藏 + 显式恢复）。
