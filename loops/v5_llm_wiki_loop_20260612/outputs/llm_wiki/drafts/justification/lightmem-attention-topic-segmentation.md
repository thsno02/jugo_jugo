# Justification: lightmem-attention-topic-segmentation

## 为什么产出此卡
主题分割是 LightMem 区别于现有记忆系统的关键创新之一，它是独立的、可复用的 chunking 策略（基于注意力矩阵局部峰值 + 相似度交叉验证）。

## 材料锚定
- Section "Topic Segmentation Submodule" 给出数学定义 B1, B2, B
- Appendix "Topic Segmentation" 给出完整实现细节（层选择、token masking、buffer 流程）
- Analysis section 给出准确率超 80% 的定量结果和消融 (-6.3%/-5.4%)

## Hedge 说明
定量结果直接引用论文数据，无 hedge 需要。
