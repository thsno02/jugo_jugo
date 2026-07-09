# Justification: locomo-temporal-reasoning-difficulty

## 抽取理由
论文在 Introduction 和 Results 中多次强调时间推理和开放域知识是"most challenging scenarios"，并提供了 Human-model 73% 差距的定量证据。该发现对理解 LLM 在对话场景下的能力边界具有普遍意义，且与 TRAM 等独立基准的结论互相验证。

## 原子性检验
该卡聚焦于"时间推理和开放域知识是最难类型"这一诊断性发现，不与 human-LLM 整体差距卡（关注全局差距）重叠——本卡强调的是类型间差异和原因分析。

## 来源锚定
- Table qa_results + Table qa_rag_results 提供各类型对比数据
- Section 6.1 QA Results 段落"time reasoning and open-domain knowledge questions are the most challenging scenarios"
