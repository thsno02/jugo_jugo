---
id: lint-as-quality-driver
title: Lint 操作：周期性健康检查与知识获取驱动
status: accepted
card_type: operation_pattern
tags:
- llm-wiki
- lint
- quality-assurance
- wiki-maintenance
- knowledge-gap
created_time: 2026-06-12 15:04:00+08:00
edited_time: 2026-06-12 15:04:00+08:00
edited_entity: llm
source_ids:
- karpathy-gist-llm-wiki
evidence_basis: practitioner_report
justification: ../justification/lint-as-quality-driver.md
canonical_concept: lint-as-quality-driver
aliases:
- wiki lint
- wiki health check
- 知识库健康检查
- wiki quality maintenance
summary: lint-as-quality-driver 是 LLM Wiki 的维护操作：周期性检查 contradictions、stale claims、orphan
  pages、missing pages、missing cross-references、data gaps，同时驱动新问题和新 source 的发现
related:
- persistent-compounding-artifact
- ingest-operation
- kb-lint-deterministic-validation
- llm-kb-lint-operation
- llm-wiki-linting
- contradiction-as-asset
- deterministic-gap-mapping
- lint-protocol-mandatory
---

Lint 是 LLM Wiki 的周期性健康检查操作，确保 wiki 在增长过程中保持质量。[^src-1]

具体检查项目包括：页面间矛盾 (contradictions)、被新 source 取代的过时声明 (stale claims)、无入链的孤立页面 (orphan pages)、被提及但缺少独立页面的重要概念 (missing pages)、缺失的交叉引用 (missing cross-references)、可通过网络搜索填补的数据空白 (data gaps)。[^src-2]

Lint 不仅是修复性的，还是驱动性的：LLM"is good at suggesting new questions to investigate and new sources to look for"。这使 lint 操作成为知识获取的发现引擎，而非仅仅的质量闸门。[^src-3] [^card-1]

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations" P4 -- "Periodically, ask the LLM to health-check the wiki."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations" P4 -- "Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations" P4 -- "The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows."
[^card-1]: [persistent-compounding-artifact](persistent-compounding-artifact.md) -- lint 维护使 wiki 能够作为复合制品持续积累而不腐化
