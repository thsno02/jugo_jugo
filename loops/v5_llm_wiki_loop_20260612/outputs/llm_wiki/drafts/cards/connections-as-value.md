---
id: connections-as-value
title: 文档间连接与文档本身同等有价值
status: draft
card_type: epistemological_claim
tags: [llm-wiki, memex, cross-references, associative-trails, knowledge-topology]
created_time: 2026-06-12T15:07:00+08:00
edited_time: 2026-06-12T15:07:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
evidence_basis: practitioner_report
justification: ../justification/connections-as-value.md
canonical_concept: connections-as-value
aliases: [associative trails, cross-references as value, 连接即价值, Memex vision]
summary: >-
  connections-as-value 是 LLM Wiki 继承自 Memex (1945) 的认识论主张：文档间的连接（cross-references, associative trails）与文档本身同等有价值；LLM 解决了 Bush 遗留的维护问题使这一愿景首次可实现
related: [persistent-compounding-artifact, human-llm-cognitive-division]
---

LLM Wiki 在精神上继承了 Vannevar Bush 的 Memex (1945) 愿景——一个"personal, curated knowledge store with associative trails between documents"。[^src-1]

核心认识论主张：在知识系统中，"the connections between documents as valuable as the documents themselves"。这意味着 wiki 的价值不仅在于单个页面的内容质量，更在于页面间交叉引用构成的网络拓扑。[^src-2]

Bush 的愿景"was closer to this than to what the web became"——web 最终演变为公开、去中心化的形态，而非 Bush 设想的私有、主动策展、以连接为核心的形态。[^src-3]

Memex 遗留的关键未解问题是维护成本："The part he couldn't solve was who does the maintenance. The LLM handles that." LLM 使这一 1945 年的愿景首次在技术上可实现。[^src-4] [^card-1]

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" P3 -- "The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" P3 -- "the connections between documents as valuable as the documents themselves"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" P3 -- "Bush's vision was closer to this than to what the web became: private, actively curated"
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" P3 -- "The part he couldn't solve was who does the maintenance. The LLM handles that."
[^card-1]: [human-llm-cognitive-division](human-llm-cognitive-division.md) -- LLM 承担维护连接网络的工作正是解决 Memex 遗留问题的方式
