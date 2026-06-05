---
card_id: comparison-detection-blind-spot-under-entrenchment
decision: accepted
confidence: high
---

## 出卡理由

此对比卡捕捉持续偏移检测（continuous-drift-detection）与用户耦合漂移固化（entrenchment-under-user-coupled-drift）之间的结构性张力。这一张力本身是一个值得独立记录的原子概念：

1. **非显然性**：一致性检测是知识库健康检查的标准手段，其在范式固化场景下的结构性失灵不是直觉上显然的
2. **实践含义**：如果运维团队仅依赖一致性检查来保障知识库质量，可能获得虚假安全感
3. **设计指导**：揭示了需要超越一致性检查的治理机制（如少数压力提升、审计压力测试）

## 来源支撑

- falconer-enterprise-guide 描述了持续偏移检测的机制和假设
- arxiv-memory-as-metabolism 描述了固化如何产生虚假内部一致性

## 与现有卡的关系

此卡是 continuous-drift-detection 与 entrenchment-under-user-coupled-drift 两卡的 [^dist-1] 张力关系的展开论述。
