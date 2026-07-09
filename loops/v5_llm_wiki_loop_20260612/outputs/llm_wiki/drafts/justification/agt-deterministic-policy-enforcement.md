# Justification: agt-deterministic-policy-enforcement

## 为什么产出此卡
Policy Engine 是 AGT 最核心的能力，也是 README 开篇即强调的核心价值主张。确定性 allow/deny + fail-closed + sub-millisecond 构成一个原子概念：运行时确定性治理。红队测试对比数据（26.67% vs 0.00%）是其核心论据。

## Evidence basis 判定
选择 `code_implementation`：有 PyPI 包（agent-os-kernel）、独立 spec (AGENT-OS-POLICY-ENGINE-1.0)、68 conformance tests、完整 Python 代码示例。

## Hedge 说明
无显式 hedge——所有性能数据和设计声明均为材料直接陈述。0.00% violation rate 引用了 docs/BENCHMARKS.md。
