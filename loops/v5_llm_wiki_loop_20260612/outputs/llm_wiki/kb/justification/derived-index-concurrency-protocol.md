# Justification: derived-index-concurrency-protocol

## 抽卡理由
派生索引协议是 llm-wiki 实现多会话无锁并发的关键机制。它将索引从"权威数据"降级为"派生缓存"，通过过期检测 + 内联重建实现最终一致性。这是一个独立的、可复用的系统设计模式。

## 证据强度
- indexing.md 完整定义协议
- SKILL.md Concurrency 段明确声明无锁安全
- 所有 command spec 中"Index Freshness Check"段重复检查逻辑
- evidence_basis: code_implementation

## 原子性检验
单一核心 idea：索引是派生缓存 + 过期检测 + 收敛一致的并发安全保证。
