---
schema: comparison_provenance.v3
draft_card: ../cards/ares-cross-domain-generalization-limits.md
draft_provenance: ../provenance/ares-cross-domain-generalization-limits.md
similarity_result: ../similarity/ares-cross-domain-generalization-limits.json
existing_cards:
  - card_id: llm-wiki-query-answer-writeback
    card_path: llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md
    score: 0.0556
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity JSON 显示 top 1 的 0.0556 来自单一 token `query`：draft 标题里写 "query/document 类型可变"，候选 "Query 操作回写好答案" 标题里也有 "Query"。top 2/3 分数 0.0。完全是字面 token 同名。

## 2. draft 与候选在哪里不同

- draft 论述 ARES fine-tuned LLM judge 的**跨域迁移边界**：用 Kendall's τ 度量在 KILT/SuperGLUE 6 个迁移对上可保持 ≥0.78，但在 XGLUE 多语 (τ=0.33)、CodeSearchNet 文→代码 (τ=0.28)、T-Rex 抽取 (τ=0.38) 三类剧烈漂移上会塌；并讨论 PPI 对 raw accuracy 损失的缓冲作用。来源 `arxiv-ares`。
- top 1 `llm-wiki-query-answer-writeback` 讲 Karpathy LLM Wiki 的 query 操作：LLM 搜 wiki、读页面、综合带引用答案，并把"好答案归档回 wiki"。来源 `karpathy-gist`。
- 两者都谈"query"，但 ARES 中 query 是 RAG 测试的输入；Wiki 中 query 是用户对 wiki 的提问。论点轴（评估泛化界 vs 操作流程）、机制（fine-tune judge + PPI vs LLM-on-wiki-search）、来源完全不同。

## 3. 下一步的核心依据

(1) 与 (2) 表明 jaccard 仅由共享 token `query` 触发，无主题交集。判 `new_card`：直接走 publication_gate。draft 含完整跨域表数字、机制解释（PPI 缓冲）、三类失败模式与未来工作边界，已具备发表门控所需信息。不是 `provenance_delta` —— Karpathy 的 query 卡 scope 严格限定在该来源对 query 操作的描述，不需要 ARES 评估证据。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

`query` 在两个语境里都很常见，是中英混合标题的常见低分误中触发词。
