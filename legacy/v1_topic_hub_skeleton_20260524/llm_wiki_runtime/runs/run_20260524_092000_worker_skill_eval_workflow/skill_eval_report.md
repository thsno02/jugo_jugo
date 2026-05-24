# Skill Evaluation Report

run_id:: run_20260524_092000_worker_skill_eval_workflow
executor_role:: skill_eval_worker
candidate:: cand_004_workflow
decision:: revise_skills_then_continue

## Adopted KB Status

The adopted KB has 4 adopted nodes according to `generated/status.yaml`. The latest adopted node is `20260524_084000_llm_wiki_ingest_compile_query_lint_workflow@1.0`. Generated status reports 4 KB view cards, 51 citation edges, no major candidates, and 0 open impact items.

The adopted root metadata for the workflow node exists and points to version `1.0`. The rendered KB/status layer is usable, but full node validation is not clean because the selected version metadata still records candidate state.

## Evaluation

- Source mining and frontier update: pass. `cand_004_workflow` was made ready by worker-attributed source mining with bounded workflow evidence.
- Node planning and generation entry: pass. The generation packet named the existing frontier candidate, cited the readiness run, and targeted `nodes/<node_id>/versions/1.0/`.
- Generation: pass. The version bundle was written under the version directory and did not adopt root metadata before audit.
- Audit: pass. Citation/adoption audit returned `adopt_recommended`; no repair or retrieval was required.
- Adoption/view: partial pass with contract caveat. View/status generation passed, but node validation fails because root metadata is adopted while version metadata remains candidate.
- Controller boundary: pass. No new controller drift sample is needed.

## Skill Changes Made

Changed `.llmwiki/skills/llmwiki-view-building/SKILL.md`:

- Added an adoption/view workflow step allowing the worker to update only selected version metadata adoption fields after audit pass.
- Added hard rules forbidding an adopted root from pointing to candidate version metadata.
- Clarified that adoption/view may update version metadata fields but must not rewrite card/provenance/change/evidence content without an explicit repair task.

Changed `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`:

- Added a hard rule that the selected `versions/<version>/node.yaml` must also mark the version adopted and record audit/adoption run when root metadata points to that adopted version.

## Reason For Patch

This is a hard-contract break rather than a low-risk local observation. The official node validator fails, and the existing metadata skill already requires root and version metadata consistency. The gap was specific and testable: future adoption/view workers need clear permission to synchronize version metadata adoption fields after audit pass.

## Rollback Risk

Low. The patch narrows permissions rather than broadening content edits. It does not permit rewriting card text, provenance, change notes, source files, archived protocol text, or generated evidence. The main risk is that a future worker could over-edit version metadata; the patched view-building rule limits this to adoption metadata fields after audit pass.

## Blockers

No loop blocker. There is one required repair before treating node validation as clean: run a worker metadata repair that synchronizes `cand_004_workflow` version metadata adoption fields with the adopted root and reruns node/view validators.
