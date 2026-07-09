# Justification: hub-topic-wiki-isolation

## 抽卡理由
Hub/Topic 隔离架构是 llm-wiki 的核心结构决策，直接影响所有命令的路径解析、并发安全、Obsidian 集成。理解该架构是理解 wiki 操作语义的前提。

## 证据强度
- README Architecture 段明确声明目录结构
- wiki-structure.md 完整定义布局
- hub-resolution.md 定义路径解析协议
- 所有 command spec 重复相同的 wiki resolution 步骤
- evidence_basis: code_implementation

## 原子性检验
单一核心 idea：hub 是纯注册中心 + topic wiki 是内容隔离单元。与"编译器隐喻"（定义角色）和"派生索引"（定义并发）分开成卡。
