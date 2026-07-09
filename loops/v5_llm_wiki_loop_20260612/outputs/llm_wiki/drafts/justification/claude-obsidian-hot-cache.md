# Justification: claude-obsidian-hot-cache

## 为何建卡
hot cache 是 claude-obsidian 区别于其他 Obsidian AI 插件的核心差异化机制之一（对比表中独有 "Session memory"），且有独立的实现细节（hooks 驱动、约 500 words、跨项目优先读取），值得原子化记录。

## 与主卡关系
从 claude-obsidian-knowledge-engine 拆出，因 hot cache 是独立可引用的机制概念。

## evidence_basis 选择
code_implementation：hooks.json 和 hot.md 均为仓库中的实际文件。
