# Task

Run citation/adoption audit for `cand_007_evaluation_evidence`.

Scope:
- Read required orchestration, citation audit, adoption audit, source mining, planning, generation, and candidate bundle files.
- Run the official card validator with `/opt/homebrew/bin/python3`.
- Assess citation target integrity, source/evidence traceability, footnote layout, provenance/change readiness, and adoption risk.
- Do not modify candidate bundle, root node, kb, generated, frontier, skill files, or mutating index/view/status/citation/backlink outputs.

Allowed write path:
- `.llmwiki/runs/run_20260524_135000_worker_audit_evaluation_evidence/`

Decision options:
- `adopt_recommended`
- `repair_before_adoption`
- `needs_retrieval`
- `reject_or_defer`

