---
id: rag-knowledge-corruption-attack
title: RAG 知识腐蚀攻击
status: accepted
card_type: concept
tags: [rag, security, poisoning, knowledge-corruption, adversarial, llm-attack]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
justification: ../justification/rag-knowledge-corruption-attack.md
canonical_concept: rag-knowledge-corruption-attack
aliases: [知识腐蚀攻击, knowledge corruption attack, PoisonedRAG, RAG投毒攻击]
summary: >-
  rag-knowledge-corruption-attack（知识腐蚀攻击 / knowledge corruption attack / PoisonedRAG）攻击者向 RAG 知识库注入少量恶意文本（每个目标问题 5 条），即可在百万级文本库中以约 90% 成功率使 LLM 生成攻击者指定答案，跨 8 种 LLM 和多种检索器有效，计算成本极低。
related:
  - rag-knowledge-database-attack-surface
  - rag-retrieval-generation-dual-condition
  - poisonedrag-text-decomposition
  - rag-poisoning-defense-insufficiency
---

PoisonedRAG 是首个针对 RAG 系统的知识腐蚀攻击（knowledge corruption attack）。攻击者选择任意目标问题 Q 和目标答案 R，通过向知识库注入少量恶意文本，使 RAG 系统中的 LLM 对 Q 生成 R 而非正确答案 [^src-1]。

**攻击效果**：在默认设定下（每个目标问题注入 5 条恶意文本，检索 k=5），PoisonedRAG 在三个基准数据集上实现了约 90% 以上的攻击成功率（ASR）：NQ 数据集 97%、HotpotQA 99%、MS-MARCO 91%（黑盒设定，PaLM 2 作为 LLM）。知识库规模为 268 万至 884 万条文本 [^src-2]。在真实场景评估中（Wikipedia 全量 2100 万条文本），攻击成功率同样维持在 91-100% [^src-3]。

**跨模型泛化**：攻击对 8 种 LLM（PaLM 2, GPT-4, GPT-3.5, LLaMA-2-7B/13B, Vicuna-7B/13B/33B）均有效，且跨 3 种检索器（Contriever, Contriever-ms, ANCE）保持高 ASR [^src-4]。

**计算效率**：黑盒攻击中生成每条恶意文本平均仅需约 2 次 LLM 查询，运行时间不到 1 秒；白盒攻击中优化每条恶意文本约需 26 秒 [^src-5]。

**与 Prompt Injection 的区别**：PoisonedRAG 使用恶意*知识*（看似正常的事实性文本）而非指令来误导 LLM，因此更隐蔽且不易被指令检测器识别 [^src-6]。

**威胁场景**包括传播虚假信息、商业偏见引导（如推荐特定品牌）、金融/健康领域误导信息 [^src-7]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "abstract.tex" -- "an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer for an attacker-chosen target question"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "evaluation.tex" -- "PoisonedRAG could achieve 97% (on NQ), 99% (on HotpotQA), and 91% (on MS-MARCO) ASRs"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "evaluation.tex" -- "PoisonedRAG is still effective in a real-world scenario, where the knowledge database consists of 21,015,324 texts from Dec. 20, 2018 Wikipedia dump."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "evaluation.tex" -- "PoisonedRAG could achieve high ASRs on 3 datasets under 8 different LLMs"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "evaluation.tex" -- "on average, PoisonedRAG only needs to make around 2 queries to the GPT-4 to craft each malicious text... it takes far less than 1 second"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "background.tex" -- "the key difference between prompt injection attacks and PoisonedRAG (in the black-box setting) is that prompt injection attacks utilize instructions while PoisonedRAG crafts malicious knowledge."
[^src-7]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "introduction.tex" -- "an attacker could mislead the LLM to generate misinformation... commercial biased answers... and financial disinformation"
