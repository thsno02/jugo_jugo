---
schema: justification_journal.v1
card: ../cards/credibility-scoring-pipeline.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：Mode A extraction from repo source bundle
来源：`data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt`
源证据：
- FILE: claude-plugin/commands/research.md — "Phase 2b: Credibility Review" 完整章节：五维评分表、四级分类（High/Medium/Low/Reject）、处理流程（score → deduplicate → rank → select → report）
- FILE: claude-plugin/commands/research.md — "This prevents the 'fox guarding the henhouse' problem where agents self-rate their own source quality."
- FILE: claude-plugin/commands/research.md — retardmax 模式中可信度评分的变化
范围论证：可信度评分管道虽然是并行研究流水线的子阶段（Phase 2b），但其评分公式、分级体系和去重逻辑构成一个自含的原子机制。现有的 parallel-multi-agent-research 卡仅在一个脚注中提到"credibility pass deduplicates before ingestion"，未展开具体的五维评分和四级分类实现。将其独立成卡避免已有卡膨胀，并可被其他评分相关卡片交叉引用。
