---
schema: draft_card_provenance.v3
draft_card: ../cards/ares-cross-domain-generalization-limits.md
material_id: arxiv-ares
digest_id: digest_arxiv-ares
source_paths:
  - data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-26T15:30:00+08:00
edited_entity: llm
---

## 源证据

### §Cross-Domain Applications 段（第 884–896 行）

> "The generalizability of the LLM judge used in ARES is critical for deploying our framework in specialized domains, particularly domains where in-domain queries, documents, and answers are difficult to gather. Therefore, we wanted to test how the LLM judges used in ARES would be affected by three domain shifts: change in query type from training to test (e.g. NQ to FEVER), change in document type from training to test (e.g. NQ to MultiRC), and change in both query and document type (e.g. NQ to ReCoRD). ... we found that the fine-tuned LLM judges used in ARES proved successful in cross-domain applications. Across all settings, we found that LLM judges in ARES had strong generalizability, even when only using 300 datapoints in our human preference validation set for PPI. Furthermore, we found that even when the LLM judge's accuracy suffered in cross-domain applications, PPI helped mitigate the loss in accuracy and still allow ARES to be successful."

### 剧烈漂移失败（第 898–904 行）

> "While LLM judges in ARES were successful in cross-domain applications for KILT and SuperGLUE, LLM judges are unable to generalize when making more drastic shifts in domain, such as: switching languages (e.g. English to Spanish, German, and other languages), switching from text to code (e.g. questions + passages to coding functions + documentation), and switching from retrieving text to extraction of entities, webpages, or citations. To test cross-lingual transfer, we used the XGLUE datasets; a LLM judge fine-tuned on NQ achieved a Kendall's tau of 0.33 over both context relevance and answer relevance scoring for XGLUE. To test text-to-code, we used CodeSearchNet; an LLM judge fine-tuned on NQ achieved a Kendall's tau of 0.28 ... To test extraction task generalizability, we used T-Rex from KILT ... achieved a Kendall's tau of 0.38 ... Each cross-domain shift requires in-domain passages and few-shot query examples for reconfiguring ARES judges."

### Table tab:cross_domain（第 80–101 行，Cross_Domain.tex）

6 个迁移对：NQ↔FEVER、NQ↔MultiRC、NQ↔ReCoRD。τ 普遍 ≥ 0.78，多数 ≥ 0.89；包括"in-domain LLM judge"对照、"average PPI range"、"accuracy on RAG evaluation sets"四列数据。

### §Limitations 中 specialized domain（第 666–671 行）

> "ARES relies on a small set of annotations in the human preference validation set (roughly 150-300 datapoints but more is better). These annotations often require an annotator familiar with the RAG system's domain application. While these annotations can be easy to generate for general-domain applications, more specialized domains, such as law, medicine, and finance, may require annotators with specialized expertise."

## 卡片范围是否成立

本卡聚焦"跨域迁移成立的边界"。现有三张 ARES 卡片：
- `ares-three-judge-rag-evaluation` 在边界一段提了"剧烈领域漂移时 τ 掉到 0.28–0.38"——但**未列出 6 个跨域迁移对的具体数字**、未把"成立 / 失败"分界线显式化为操作规则；
- `ares-synthetic-data-pipeline` 完全不涉及跨域；
- `ares-ppi-confidence-bound` 提了 PPI 在 cross-domain 下的缓冲作用，但未给出迁移表数字。

所有 6 个迁移对 τ 数字、3 个剧烈漂移 τ 数字、PPI 缓冲机制论述都直接来自原文。"操作含义"段把论文事实总结为"什么时候必须重训判官"，是合理引申——论文 §Limitations 已隐式表达。

## 发表门控结果

本轮未运行。

## 备注

- 与 `ares-three-judge-rag-evaluation` 卡片有信息重叠（后者也提了剧烈漂移的 τ 数字）——本卡是该信息的专卡展开。可能需要在 comparison_provenance 阶段决定是否把 `ares-three-judge-rag-evaluation` 卡里那段边界文字精简。
- 与 `ares-ppi-confidence-bound` 互补：那张卡讲 PPI 如何工作，本卡讲 PPI 在跨域下的缓冲极限。
