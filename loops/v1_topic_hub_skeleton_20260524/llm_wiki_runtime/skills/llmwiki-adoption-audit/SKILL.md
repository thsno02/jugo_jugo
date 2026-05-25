---
name: llmwiki-adoption-audit
description: Decide whether an LLM Wiki KB node version can be adopted. Use after bundle generation and citation/provenance audit to check schema, epistemic scope, provenance, change notes, and major-version impact requirements.
---

# LLM Wiki Adoption Audit

## Purpose

Use this skill as the final gate before rendering a version into `kb/`.

## Inputs

- `versions/<version>/node.yaml`
- `versions/<version>/card.md`
- `versions/<version>/provenance.md`
- `versions/<version>/change.md`
- Source mining artifacts.
- Retrieval logs, if any.
- Citation audit report.

## Adoption Checks

- All four version bundle files exist.
- Metadata schema and paths are valid.
- Card has parseable Footnotes and References.
- Card passes the footnote layout gate: `## References` appears before the final `## Footnotes`, and `## Footnotes` is the last top-level section.
- Audit is read-only for adopted/generated state: do not write root `node.yaml`, render `kb/`, or run generated-mutating view scripts during citation/adoption audit unless the task packet explicitly grants adoption/view authority.
- Provenance has required sections and separates existing data from dynamic retrieval.
- Change file explains genesis or semantic delta.
- Card does not present synthesis as ground truth.
- Evidence gaps are visible.
- First version and minor version can adopt after audit pass.
- Major version requires impact analysis before adoption.

## Comparison And Adjacent-System Checks

For comparison, boundary, risk, governance, evaluation, or adjacent-system nodes, adoption audit must also confirm:

- The card states the comparison axis and does not turn a bounded contrast into a broad taxonomy.
- Adjacent-system facts are supported by direct primary or technical sources, not only prior KB anchors or secondary framing.
- The card avoids unsupported absence, superiority, strawman, and equivalence claims.
- Known overlaps and complementarity are preserved where sources allow them.
- Out-of-scope systems, enterprise/scale/adoption/benchmark limits, and retrieval-deferred items are explicit.

## Output

Write an adoption decision with one status:

- `adopt`
- `repair_before_adoption`
- `needs_retrieval`
- `needs_impact_analysis`
- `reject_or_defer`

If an audit worker accidentally mutates `kb/` or `generated/`, the audit may still recommend adoption only if the version bundle itself passes, but the delivery must label the mutation as audit overreach and adoption/view must refresh all generated outputs inside its own legal scope before using them as authoritative state.

## Skill Evolution Notes

Patch this skill when adoption happens without traceable evidence, major updates bypass impact review, or repair instructions are too vague to execute.
