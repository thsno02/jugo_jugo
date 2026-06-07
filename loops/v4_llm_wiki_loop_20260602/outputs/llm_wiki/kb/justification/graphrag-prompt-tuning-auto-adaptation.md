---
schema: justification_journal.v1
card: ../cards/graphrag-prompt-tuning-auto-adaptation.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：从 repo-microsoft-graphrag material_bundle.txt 提取实现细节
来源：`data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt`
源证据：
- docs/prompt_tuning/auto_prompt_tuning.md — auto-tune 算法流程、文档选择方法（random/top/all/auto）、命令行参数
- docs/prompt_tuning/overview.md — prompt tuning 概览（default/auto/manual 三层）
- docs/prompt_tuning/manual_prompt_tuning.md — token 替换机制（{input_text}, {entity_types} 等）
范围论证：提示词调优是 GraphRAG 实现中最重要的实践建议（README 和文档反复强调 "strongly recommend"），涉及具体的文档选择策略和 LLM 推断流程，论文中仅简要提及，此卡填补实现细节空白。
