# Justification: lightmem-sleep-time-offline-update

## 为什么产出此卡
睡眠时离线并行更新是 LightMem 最具创新性的设计之一——它是将认知科学"睡眠整合"映射到工程系统的完整机制。包含软更新 + 更新队列 + 并行化三个子要素，但它们紧密耦合为单一决策（解耦更新与推理），因此保持为一张卡。

## 材料锚定
- Section "Light3" 给出形式化定义
- Case Study 给出软/硬更新对比
- Table tree_update 给出串行 vs 并行延迟对比（5x/8x）

## Hedge 说明
"可能将...误判" -- 论文用 "might incorrectly interpret" 表述，保留了不确定性。
