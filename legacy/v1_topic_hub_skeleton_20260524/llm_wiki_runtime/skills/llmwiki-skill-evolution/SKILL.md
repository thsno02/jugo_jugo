---
name: llmwiki-skill-evolution
description: Evaluate and patch the reusable skills used by the LLM Wiki KB mining loop. Use after each 0-1 node build, audit failure, retrieval case, build failure, or impact run to decide whether a failure is case-local or requires a general skill update.
---

# LLM Wiki Skill Evolution

## Purpose

Use this skill after each completed run. Every 0-1 node is also a test case for the skills that produced it.

## Inputs

- Run artifacts.
- Version bundle.
- Audit report.
- Retrieval usage.
- Adoption result.
- Validation/build failures.

## Evaluation Questions

- Which failure mode appeared?
- Which skill caused it or failed to prevent it?
- Is it local to this case, repeated, high-risk, or a hard-contract break?
- Should the response be a case note, retrieval request, validator fix, or skill patch?

## Patch Rule

Patch a skill only if:

- The failure is repeated.
- The failure is high-risk.
- The failure breaks a hard contract.
- The patch is specific and testable.

Do not patch global skills for one low-risk local observation.

## Outputs

- `.llmwiki/runs/<run_id>/skill_eval.md`
- `.llmwiki/control/skill_eval_log.yaml`
- Optional targeted patch to one skill's `SKILL.md`.

## Skill Evolution Notes

This skill should be patched when skill evaluation becomes vague, unactionable, or too eager to generalize from a single case.
