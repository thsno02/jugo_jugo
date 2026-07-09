# Justification: kv-cache-quantization-tradeoff

## 提取依据
Appendix C (KV Cache Quantization Ablation) 和 Appendix D (Multi-Domain Results) 中的 Q4 vs Q8 对比数据。

## 原子性判断
量化权衡是独立的实验发现，适用范围超出 WiCER 本身（对任何 KV cache 部署有参考价值）。

## Evidence basis
experimental_paper -- Policygenius 和 RepLiQA 双数据集的量化消融。
