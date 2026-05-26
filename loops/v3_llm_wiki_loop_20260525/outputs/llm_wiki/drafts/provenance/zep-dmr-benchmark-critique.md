---
schema: draft_card_provenance.v3
draft_card: ../cards/zep-dmr-benchmark-critique.md
material_id: arxiv-zep
digest_id: digest_arxiv-zep
source_paths:
  - data/raw/arxiv/arxiv-zep/agent_source_bundle.txt
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-26T11:15:00+08:00
edited_entity: llm
---

## 源证据

- main.tex 行 218："The Deep Memory Retrieval evaluation, introduced by [memgpt], comprises 500 multi-session conversations, each containing 5 chat sessions with up to 12 messages per session."
- main.tex 行 220："Using gpt-4-turbo, the full-conversation baseline achieved 94.4% accuracy, slightly surpassing MemGPT's reported results, while the session summary baseline achieved 78.6%. When using gpt-4o-mini, both approaches showed improved performance: 98.0% for full-conversation and 88.0% for session summaries."
- main.tex 行 222："Zep achieved 94.8% accuracy with gpt-4-turbo and 98.2% with gpt-4o-mini ... However, these results must be contextualized: each conversation contains only 60 messages, easily fitting within current LLM context windows."
- main.tex 行 224："The evaluation relies exclusively on single-turn, fact-retrieval questions that fail to assess complex memory understanding. Many questions contain ambiguous phrasing ... Most critically, the dataset poorly represents real-world enterprise use cases for LLM agents. The high performance achieved by simple full-context approaches using modern LLMs further highlights the benchmark's inadequacy for evaluating memory systems."
- main.tex 行 226："The LongMemEval dataset addresses many of these shortcomings by presenting longer, more coherent conversations that better reflect enterprise scenarios, along with more diverse evaluation questions."
- main.tex 行 220（结尾）："We were unable to reproduce MemGPT's results using gpt-4o-mini due to insufficient methodological details in their published work."
- main.tex 行 266："we attempted to evaluate MemGPT using the LongMemEval dataset. Given that the current MemGPT framework does not support direct ingestion of existing message histories ... we were unable to achieve successful question responses using this approach."

## 卡片范围是否成立

本卡范围是"对 DMR 作为基准的批判与替代建议"这一独立 source_claim。所有五点局限直接出自原文。"含 60 条消息的对话能塞进现代 LLM 上下文"是数学事实（5 session × ≤12 messages = ≤60）。本卡不评判 MemGPT 算法本身。"评估方法学的含义"用论文自己给的对比作为引申，仍受 §4 支撑。

## 发表门控结果

本轮未运行。

## 备注

- 这张卡和"评估方法论"主题相关，未来可能与其他 benchmark 卡（如 LongMemEval 卡）做比较合并。
