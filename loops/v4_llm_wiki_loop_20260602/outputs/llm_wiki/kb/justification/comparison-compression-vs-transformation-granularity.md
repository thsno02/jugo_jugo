---
card_id: comparison-compression-vs-transformation-granularity
---

## creation | 2026-06-05T15:00:00+08:00

生成方式：governance comparison pipeline
note: comparison/distinction 卡由 governance workflow 生成

## 为什么需要这张卡

LongMemEval（memory-value-granularity-tradeoff）发现事实级压缩损害 QA 性能，LoCoMo（observation-based-memory-representation）发现观察式提取提升 QA 性能。两者表面矛盾，但根源在于"细化"有两条路径——有损压缩与澄清性转化。这一区分本身是一个值得独立捕捉的原子概念，对记忆系统设计有直接指导意义。

## 证据支撑

- LongMemEval Section 5.2：事实提取因信息丢失负面影响 QA（除跨会话推理）
- LoCoMo Section 6.1/Table 3：观察 top-5 F1=41.4 vs 对话 top-5 F1=31.7

## 为什么不合并为一张卡

两张源卡分别来自不同论文、不同基准、不同实验设置，各自记录了独立的实证发现。本卡的价值在于从两者的对比中提炼出"压缩 vs 转化"这一跨实验的设计原则。
