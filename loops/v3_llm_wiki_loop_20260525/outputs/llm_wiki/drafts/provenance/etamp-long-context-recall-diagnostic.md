---
schema: draft_card_provenance.v3
draft_card: ../cards/etamp-long-context-recall-diagnostic.md
material_id: arxiv-etamp-memory-poisoning
digest_id: digest_arxiv-etamp-memory-poisoning
source_paths:
  - data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-26T15:20:00+08:00
edited_entity: llm
---

## 源证据

### §F 方法（第 909–918 行）

> "For each Task A trajectory, we construct a recall test by: (1) Extracting the full agent trajectory from task A including the malicious instructions and append the initial observation from task B (2) Prompting the model to find and extract the hidden instruction pattern (3) Comparing the extracted URL against the expected attack URL. We use Authority Framing rather than Baseline Injection or Frustration Exploitation because this configuration exhibits good variation in attack success rates across models, making it informative for studying the relationship between recall ability and attack susceptibility."

### Table tab:long_context_recall（第 972–981 行）

```
GPT-OSS-120B    282  19   6.7%  6.7%
GPT-5-mini      280  119  42.5% 42.5%
GPT-5.2         282  282  100.0% 100.0%
Qwen2.5-VL-72B  283  280  98.9%  98.9%
Qwen3-VL-32B    282  282  100.0% 100.0%
```

### Interpretation 段（第 988–996 行）

> "GPT-OSS-120B (6.7% recall): The extremely low recall rate indicates a severe needle-in-haystack failure. This model's apparent immunity to the attack is largely due to its inability to process and retrieve information from long contexts, rather than robust safety alignment. GPT-5-mini (42.5% recall): Moderate recall suggests partial context processing limitations ... GPT-5.2, Qwen2.5-VL-72B, Qwen3-VL-32B (≥98.9% recall): Near-perfect recall demonstrates these models can reliably locate hidden instructions in long contexts. For these models, any observed attack resistance can be more confidently attributed to safety alignment rather than context processing limitations."

### 关键判断（第 996 行）

> "This diagnostic is critical for interpreting Attack Success Rate (ASR_B) results: a low ASR_B combined with low recall suggests the defense is incidental (context limitations), while low ASR_B with high recall suggests intentional resistance (safety alignment). Note that we tested only one long-context recall test prompt configuration, and the low recall rates for GPT-OSS-120B and GPT-5-mini may be partly due to these models producing empty responses. In such cases, we retried the prompt up to two additional times, but non-empty responses were not guaranteed."

## 卡片范围是否成立

本卡聚焦"Recall vs Refusal 诊断"作为独立的方法学规则。现有 ETAMP 卡片只在 `etamp-capability-vs-security` 卡的 Footnotes 简单引用了 "Qwen rebustness is not due to recall limitations"（Table tab:long_context_recall）的一句话，**未把诊断方法本身、其逻辑、低 ASR + 低 recall 的判断规则展开**。

所有数字、推理、操作含义都直接源自 §F。"OSS 模型升级一代可能破防"是合理引申——论文只说"may be partly due to empty responses"，本卡把它扩展为"未来模型能力提升后这种 fragile defense 会失效"的预警，与论文 conclusion "more capable models are not more secure" 论证同向。

## 发表门控结果

本轮未运行。

## 备注

- 与 `etamp-capability-vs-security` 卡片互补：那张卡讲"capability 高不代表 secure"，本卡讲"如何鉴别 secure 是不是真的"。在 wiki 内做 cross-reference。
- 这条诊断方法可外推到其它 prompt injection 类研究——任何用"长上下文里藏恶意指令"的攻击都该跑 recall 诊断。
