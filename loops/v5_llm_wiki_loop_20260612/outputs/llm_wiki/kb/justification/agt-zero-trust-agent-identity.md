# Justification: agt-zero-trust-agent-identity

## 为什么产出此卡
身份与信任是 AGT 独立于策略引擎的第二大核心能力，有独立 spec (AGENTMESH-IDENTITY-TRUST-1.0) 和 135 conformance tests。Trust ceiling propagation 和量子安全 credentials 是该系统的独特设计决策。

## Evidence basis 判定
选择 `code_implementation`：有独立 PyPI 包 agentmesh-platform，135 conformance tests，属已实现代码。

## Hedge 说明
"似乎" 用于 ML-DSA-65 引入目的的推断——材料标注 "quantum-safe" 但未显式说明动机。
