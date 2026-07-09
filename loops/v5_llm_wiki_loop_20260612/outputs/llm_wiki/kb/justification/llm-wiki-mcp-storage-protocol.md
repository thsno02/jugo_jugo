# Justification: llm-wiki-mcp-storage-protocol

## 为什么产出此卡

WikiStorage Protocol 是 llm-wiki-mcp 可扩展性的关键设计——允许替换底层存储后端。这是独立于架构概览的 API 设计层面知识，对想要集成或测试的开发者有直接参考价值。

## 原子性判断

本卡聚焦 Protocol 接口定义 + build_server 组合根模式 + 领域错误类型，构成"如何插入自定义后端"这一完整原子概念。

## Evidence basis

`documentation` — 来自 PyPI 官方项目描述中 "Python API" 章节，含代码示例。

## 源覆盖

- Python API 章节
- build_server composition root 说明
- domain errors 列表
