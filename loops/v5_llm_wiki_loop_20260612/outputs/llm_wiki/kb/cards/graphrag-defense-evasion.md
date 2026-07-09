---
id: graphrag-defense-evasion
title: GraphRAG 投毒攻击的防御规避
status: accepted
card_type: experimental-finding
tags:
- defense-evasion
- perplexity-filter
- llm-detector
- semantic-closeness
- graphrag
- stealthiness
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-graph-poisoning
evidence_basis: experimental_paper
justification: ../justification/graphrag-defense-evasion.md
canonical_concept: graphrag-defense-evasion
aliases:
- defense evasion
- KPA stealthiness
- 防御规避
- 攻击隐蔽性
summary: GraphRAG defense evasion 实验表明现有防御对 TKPA/UKPA 几乎无效：Perplexity Filter F1=0.07/0.04， LLM Detector F1=0.13/0.11，Semantic Closeness Checking F1=0.07。TKPA 重写由高级 LLM 生成， 风格/困惑度与正常文本无法区分；UKPA 保持句子级语义完整仅破坏跨
  chunk 共指信号，超出局部文本分析检测能力。 查询侧防御（如 query paraphrasing）亦无效因攻击目标是语料本身而非查询。defense evasion stealthiness。
related:
- targeted-knowledge-poisoning-attack
- universal-knowledge-poisoning-attack
- graphrag-knowledge-poisoning-attack-surface
- etamp-attack-stealth-mechanism
- etamp-threat-model-positioning
- graphrag-graph-construction-as-security-component
---
三种 SOTA 防御方法对 TKPA 和 UKPA 的检测效果：

| 攻击 | 防御 | Precision | Recall | F1 |
|------|------|-----------|--------|-----|
| TKPA | Perplexity Filter | 0.08 | 0.06 | 0.07 |
| TKPA | LLM Detector | 0.14 | 0.12 | 0.13 |
| UKPA | Semantic Closeness | 0.08 | 0.06 | 0.07 |
| UKPA | Perplexity Filter | 0.05 | 0.04 | 0.04 |
| UKPA | LLM Detector | 0.12 | 0.10 | 0.11 |

所有 F1 接近 0，说明这些攻击具有极高隐蔽性。[^src-1]

失败原因：TKPA 的 LLM 重写在统计和风格上与正常文本无法区分（低 PPL ratio）；UKPA 仅改变跨 chunk 共指信号，句子级语义完整不变，超出局部文本分析的检测能力。查询侧防御（如 query paraphrasing）因攻击目标是语料本身也无效。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Table 4 Defense evaluation" P746-761 -- "PF 0.08 0.06 0.07... LLMDet 0.12 0.10 0.11"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Attack Stealthiness" P731-740 -- "existing defenses are largely ineffective... the modified text is statistically and stylistically indistinguishable from clean text"

[^card-10]: [[graphrag-knowledge-poisoning-attack-surface]] 防御失效凸显该攻击面的严重性
