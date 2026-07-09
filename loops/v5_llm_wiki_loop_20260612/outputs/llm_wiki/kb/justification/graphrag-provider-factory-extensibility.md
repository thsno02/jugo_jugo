# Justification: graphrag-provider-factory-extensibility

## 提取依据
材料 docs/index/architecture.md 列举了 7 个子系统的 factory 模式及对应源码链接；docs/config/models.md 详述了 LiteLLM 集成、Proxy API 方案和 Model Protocol 注入机制。

## 原子性判断
"可扩展架构"是一个统一的设计决策（factory pattern + provider injection），7 个子系统是同一 pattern 的平行应用实例，整体构成一个原子 idea。

## Evidence basis
code_implementation -- 材料直接引用了各 factory 的源码文件路径，描述的是已实现的注册与注入机制。
