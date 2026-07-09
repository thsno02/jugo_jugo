# Justification: langgraph-store-index-config

## 为什么产出此卡
IndexConfig 是独立的配置对象，其参数（embed 函数签名、dims）构成原子知识点。

## Evidence basis 选择
官方文档 documentation。

## 原子性检查
仅覆盖 IndexConfig 的结构和传入方式，不涉及搜索行为本身。
