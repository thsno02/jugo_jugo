# Justification: agt-privilege-ring-sandboxing

## 为什么产出此卡
执行沙箱是 AGT 的第三大核心能力，有独立 spec (AGENT-HYPERVISOR-EXECUTION-CONTROL-1.0) 和 80 conformance tests。四特权环 + saga + kill switch 构成独立原子概念。同时材料显式声明了安全边界限制（middleware 层非 OS kernel），这一 honest limitation 是知识卡的重要组成。

## Evidence basis 判定
选择 `code_implementation`：有 agent-runtime、agent-hypervisor 独立包和 80 conformance tests。

## Hedge 说明
"据材料推测" 用于 trust score 与 kill switch 联动的推断——材料分别描述了两者但未显式说明触发关系。
