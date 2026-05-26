---
schema: comparison_provenance.v3
draft_card: ../cards/memgpt-docqa-pagination-failure-mode.md
draft_provenance: ../provenance/memgpt-docqa-pagination-failure-mode.md
similarity_result: ../similarity/memgpt-docqa-pagination-failure-mode.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.087
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0476
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0476
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 计算结果显示三张候选与 draft 的 jaccard 分数都低于 0.09，shared_tokens 仅为「是」「的」「模式」这种通用汉字虚词或泛义名词。Top 1 `llm-wiki-schema-configuration-document` 的 0.087 完全由「是」「的」贡献；top 3 的「模式」与 draft 标题里的「失败模式」、候选的「持久 wiki 替代模式」在词形上重合但语义不同。这是典型的 jaccard 误中。

## 2. draft 与候选在哪里不同

draft 写的是 MemGPT 在 NaturalQuestions-Open / DocQA 任务上的实测失败模式：retriever-reader 设置、pgvector + HNSW、agent 自决何时停止翻页、GPT-3.5 vs GPT-4 函数调用差异、以及由此引出的 satisficing 与 agent control 问题。来源是 `arxiv-memgpt`。

三张 v2 候选完全来自 Karpathy 的 `llm-wiki` gist / 推文：
- top 1 描述 `schema` 作为 wiki 配置文档；
- top 2 描述 `idea file` 在表述上有意保持抽象；
- top 3 描述 LLM 持久 wiki 与一次性 RAG 的对比。

论点轴、机制、来源类型、覆盖维度都不重叠：v2 候选是「wiki 模式 / idea file 概念」层，draft 是「agent 在 retrieval pagination 上的具体失败实验」层。draft provenance 也明确指出现有 5 张 MemGPT 卡均未覆盖 DocQA / NaturalQuestions 任务或 pagination 失败模式。

## 3. 下一步的核心依据

(1) 表明 jaccard 是误中；(2) 表明语义、来源、问题域都不重叠。因此应当判 `new_card`，而非 `merge_candidate` / `provenance_delta`（v2 卡的 scope 严格限定在 Karpathy gist 文本范围内，无法把 MemGPT DocQA 证据反向链入）也不是 `revise_before_gate`（draft 已有完整源证据与 prompt 全文佐证）。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- 三张 v2 候选属于「高频通用 token」误命中类型，下次可考虑在 tokenizer 阶段过滤掉「是 / 的 / 模式」等单字虚词。
- draft provenance 已声明这是 MemGPT 论文里唯一一处承认自家结构性短板的段落，价值较高，建议优先 gate。
