# Justification: llm-wiki-mcp-etag-cas

## 为什么产出此卡

乐观并发控制（etag CAS）是 llm-wiki-mcp server 机制层的核心设计，直接影响多 agent 协作场景的正确性。与架构概览拆分为独立卡，因为并发模型本身是一个完整的原子概念。

## 原子性判断

本卡覆盖 server 的四项机制保障（etag CAS、原子写入、路径安全、日志格式），它们共同构成"server 强制的机制层"，逻辑上不可分割。

## Evidence basis

`documentation` — 来自 PyPI 官方项目描述中 "Design boundary" 章节的详细技术说明。

## 源覆盖

- Design boundary 章节全部四个要点
- CVE-2025-53109 引用
