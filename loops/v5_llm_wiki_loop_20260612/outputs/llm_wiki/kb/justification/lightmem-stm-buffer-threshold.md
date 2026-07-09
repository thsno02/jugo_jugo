# Justification: lightmem-stm-buffer-threshold

## 为什么产出此卡
STM buffer threshold 是 LightMem 效率提升的核心杠杆参数，其非单调准确率影响是论文重要发现。与架构卡分离保持原子性。

## 材料锚定
- Section "Light2" 给出机制描述
- "Analysis of the STM Threshold's Impact" 给出定量分析
- Table lightmem_comparison 给出完整参数扫描数据

## Hedge 说明
"据论文推测" 用于解释 th 与 r 交互效应的原因——论文用 "This suggests" 表述。
