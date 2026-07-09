# Justification: graphrag-query-modes

## 提取依据
材料 docs/query/overview.md、global_search.md、local_search.md、drift_search.md 分别详细描述了四种查询模式的方法论、数据流和配置参数。

## 原子性判断
本卡将四种查询模式作为一个概念集整合，因为它们共同构成 GraphRAG 的查询层。标题中虽有"四种"但核心概念仍是"GraphRAG 的查询模式体系"这一原子 idea，各模式间是平行枚举关系而非因果/连词关系。

## Evidence basis
code_implementation -- 材料来自实际代码仓库的文档，描述的查询类均有对应 Python 实现。
