---
schema: draft_card_provenance.v3
draft_card: ../cards/poisonedrag-knowledge-database-attack-surface.md
material_id: arxiv-poisonedrag
digest_id: digest_arxiv-poisonedrag
source_paths:
  - data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-26T11:30:00+08:00
edited_entity: llm
---

## 源证据

- 威胁模型与攻击面声明（`introduction.tex` 第 1707 行）：
  > "knowledge databases of RAG systems introduce a new and practical attack surface ... maliciously editing Wikipedia pages ... post fake news or host malicious websites ... an insider can inject malicious texts into an enterprise private knowledge database."。
- 5 条/268 万比例与 97% ASR（同文件第 1724–1726 行）：
  > "PoisonedRAG could achieve a 97% ASR by injecting 5 malicious texts for each target question into a knowledge database (with 2,681,468 clean texts) in the black-box setting."。
- 攻击者不知 LLM 参数但需选 retriever 设定（`preliminary.tex` 第 2027 行）：
  > "we consider that the attacker cannot access texts in a knowledge database, and cannot access the parameters nor query the LLM. Depending on whether the attacker knows the retriever, we consider two settings: black-box setting and white-box setting."。
- 跨多模型/多 retriever 稳定（`appendix.tex` Table `tab:ablation-llm-tmp-results` 第 263–286 行 + `tab:retriever-model` 第 559–574 行）：
  > "PaLM 2 0.97 / GPT-3.5 0.92 / GPT-4 0.98 / LLaMa-2-7B 0.95 / Vicuna-7B 0.92 ... Contriever / Contriever-ms / ANCE 均 0.88–0.99"。
- Wikipedia 可编辑性数字（`preliminary.tex` 第 2033 行）：
  > "A recent study showed that it is possible to maliciously edit 6.5% (conservative analysis) of Wikipedia documents."。
- 非目标问题附带影响（`relatedwork.tex` 第 2076–2077 行）：
  > "the fractions of non-target questions influenced by malicious texts are 0.3% and 0.9% in black-box and white-box settings, respectively. Additionally, the fractions of non-target answers ... is 0% and 0.4%."。

## 卡片范围是否成立

这张卡的角色是 "concept" —— 把 RAG 知识库这个攻击面从单纯的内容质量问题抽象出来，并用 PoisonedRAG 的四组数字把它定量化。所有数字（268 万 clean / 5 条恶意 / 97% / 6.5% Wikipedia / 0.3–0.9% 附带）都直接来自论文，没有引入二次估计。最后一句"换 LLM 不安全 / 看不见广谱症状"是把"跨 LLM ASR 稳定 + 非目标问题附带很低"两个实验结果做直接的工程语言重述，没有越界。

## 发表门控结果

本轮未运行。

## 备注

与 `poisonedrag-retrieval-generation-two-conditions` 互补：前者是机制，本卡是威胁面；与未来可能的 `poisonedrag-defenses-insufficient` 卡形成三连。预计 `new_card`。
