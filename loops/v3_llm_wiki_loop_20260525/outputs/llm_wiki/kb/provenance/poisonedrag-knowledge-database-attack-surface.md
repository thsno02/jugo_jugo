---
schema: accepted_card_provenance.v3
card: ../cards/poisonedrag-knowledge-database-attack-surface.md
material_id: arxiv-poisonedrag
digest_id: digest_arxiv-poisonedrag
source_paths:
  - data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt
draft_card: ../../drafts/cards/poisonedrag-knowledge-database-attack-surface.md
draft_provenance: ../../drafts/provenance/poisonedrag-knowledge-database-attack-surface.md
similarity_result: ../../drafts/similarity/poisonedrag-knowledge-database-attack-surface.json
comparison_provenance: ../../drafts/comparison/poisonedrag-knowledge-database-attack-surface.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:30:00+08:00
  gate_notes: 6/6 项通过；攻击面四特征与数字均出自论文 verbatim。
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-27T15:30:00+08:00
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

这张卡的角色是 "concept" —— 把 RAG 知识库这个攻击面从单纯的内容质量问题抽象出来，并用 PoisonedRAG 的四组数字把它定量化。所有数字直接来自论文。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:30:00+08:00
- 检查要点：
  - 四特征 + 操作启示 + 原话锚 节构清晰。
  - 知识密度高；非标题复述。
  - 源支撑：6 段 verbatim + 行号。
  - References + Footnotes 双在；Footnotes 2 条 verbatim。
  - frontmatter 完整；related 含 8 张邻接卡。

## 备注

与 `poisonedrag-retrieval-generation-two-conditions` 互补：前者是机制，本卡是威胁面。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/poisonedrag-knowledge-database-attack-surface.md`
- draft provenance: `../../drafts/provenance/poisonedrag-knowledge-database-attack-surface.md`
- similarity: `../../drafts/similarity/poisonedrag-knowledge-database-attack-surface.json`
- comparison provenance: `../../drafts/comparison/poisonedrag-knowledge-database-attack-surface.md`
