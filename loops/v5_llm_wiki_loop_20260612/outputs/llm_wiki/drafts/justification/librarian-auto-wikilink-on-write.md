# Justification: librarian-auto-wikilink-on-write

## 为什么值得建卡

自动 wikilink 是 Librarian 独有的写入时增强机制，也是 LLM Wiki 中"写入即织网"理念的具体实现。它确保知识图谱随写入自动增长而非需要手动维护。

## evidence_basis 选择: code_implementation

README 明确描述了 library_write 工具的自动链接行为、跳过规则、规范文件名策略，这是已实现功能的文档。

## 原子性检验

本卡聚焦于自动 wikilink 的触发条件、扫描逻辑、安全跳过规则。不涉及图遍历或社区检测（各有独立卡）。
