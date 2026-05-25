---
name: llmwiki-citation-audit
description: Audit LLM Wiki KB card citations for parseability, source support, pinned paths, citation roles, and overclaim risk. Use after card generation and before adoption.
---

# LLM Wiki Citation Audit

## Purpose

Use this skill to decide whether a card's citations actually support the claims they are attached to.

## Checks

- `## Footnotes` and `## References` exist.
- Every citation block has all required fields.
- `target` and `pinned_version` resolve.
- `why_cited` is specific.
- `evidence_summary` matches the source.
- Citation role fits the use: claim support, background definition, discourse context, implementation evidence, limitation, or provenance anchor.
- Source-backed claims do not rely only on manifests unless the claim is about manifest status.
- Audit stays read-only for KB/view state: do not run or trigger view-building/generated-mutating scripts such as `kb_parse_citations.py`, backlink refresh, impact refresh, or status refresh unless the task packet explicitly grants adoption/view authority.

## Overclaim Review

For each key paragraph, ask:

- Is this observed fact, interpretation, discourse note, or gap?
- Does the citation support that exact epistemic status?
- Is a secondary source being treated as primary?
- Would a future reader know what to inspect?

## Output

Write findings to the run's `audit_report.md` or `citation_audit.md` with pass/fail per gate and concrete repair instructions.

If generated outputs were mutated accidentally, disclose the exact files in the audit delivery and require the adoption/view worker to refresh generated state before it is considered authoritative.

## Skill Evolution Notes

Patch this skill when unsupported claims pass audit, citation blocks parse but remain semantically weak, or auditors miss source/category confusion.
