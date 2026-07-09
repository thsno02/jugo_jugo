---
id: llm-wiki-audit-trust-verification
title: Audit 信任验证机制
status: draft
card_type: mechanism
tags: [llm-wiki, audit, trust, provenance, drift-detection]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-audit-trust-verification.md
canonical_concept: audit-trust-verification
aliases: [wiki audit, trust verification, provenance check, 信任审计]
summary: >-
  audit-trust-verification 机制：回答更广泛的信任问题，复用 librarian pass，跨 raw/ wiki/ output/ 追踪输出证据链，检测漂移 drift，检查出处 provenance，本地证据不足时升级为新鲜研究
related: [llm-wiki-librarian-quality-scoring, llm-wiki-immutable-raw-sources, llm-wiki-compilation-process]
---

llm-wiki 的 audit 功能回答关于输出可信度的广泛信任问题。它复用 librarian pass 的结果，跨 raw/、wiki/ 和 output/ 追踪输出的完整证据链，检测漂移（drift），检查出处（provenance）。[^src-1]

当本地存储的证据不足以回答信任问题时，audit 会升级为执行新鲜研究。[^src-2]

Audit 可以追溯一个 output 回溯经过其依赖的 wiki 状态和 raw sources，然后在存储的证据陈旧或不完整时升级为新鲜研究。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Audit" P36 -- "Answer the broader trust question. Reuse the librarian pass, trace outputs across raw/, wiki/, and output/, detect drift, inspect provenance, and do fresh research when local evidence is not enough."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Audit" P36 -- "do fresh research when local evidence is not enough"
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P208 -- "Audit walks that full artifact graph. It can trace an output back through the wiki state and raw sources it depended on, then escalate into fresh research when the stored evidence is stale or incomplete."
