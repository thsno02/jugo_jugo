# V3 Scaffold Reliability Audit

Audit time: 2026-05-25T21:03:26+08:00

## Verdict

The v3 scaffold is directionally reliable and follows the optimization plan: material becomes draft cards first; similarity is lightweight title-based top 3; comparison provenance records the three decision questions; fusion and provenance-delta paths require audit; card quality is defined as knowledge-bearing rather than title restatement.

The scaffold needed hardening before handing to Claude Code: phase-specific read boundaries, a self-contained no-context handoff, explicit local skill/dependency initialization because Claude Code does not inherit Codex skills, and runtime clarification because Claude Code standard subagents do not support native nested Agent spawning. A process-level workaround has been verified: a subagent can use Bash to invoke `claude --permission-mode auto -p "..." --output-format text` as an independent inner session. These constraints are recorded in `CLAUDE_CODE_HANDOFF.md`, `CONTEXT_BOUNDARY.md`, `SKILLS_AND_DEPENDENCIES.md`, and `SUBAGENT_RUNTIME_CONSTRAINTS.md`.

## Checked Against Plan

- `material => draft card`: present in `DRAFT_FIRST_PIPELINE_V3.md` and `RUNBOOK.md`.
- Draft cards must have information value: present in `CARD_CONTRACT_V3.md`.
- Similarity mechanism: present as Jieba + Jaccard set similarity + top 3 in `SIMILARITY_MECHANISM_V3.md`.
- Similarity is candidate retrieval, not audit: present in `SIMILARITY_MECHANISM_V3.md`.
- Comparison provenance three questions: present in `PROVENANCE_CONTRACT_V3.md`.
- Fusion/provenance delta requires audit: present in `PROVENANCE_CONTRACT_V3.md` and `DRAFT_FIRST_PIPELINE_V3.md`.
- Provenance delta links back to target accepted card provenance: present in `PROVENANCE_CONTRACT_V3.md`.
- Brain mailbox / queue coordination: present in `BRAIN_MAILBOX_PROTOCOL.md`.
- Local skill/dependency initialization for Claude Code: present in `SKILLS_AND_DEPENDENCIES.md`.
- Subagent hierarchy constraint and process-level nested workaround: present in `SUBAGENT_RUNTIME_CONSTRAINTS.md`.
- Root stable `llm_wiki` remains absent: preserved; v3 output stays inside the loop capsule.

## Context-Contamination Risks

- A no-context agent might read v2 history and copy v2's process problems.
- A production worker might read accepted cards too early and optimize for fusion instead of draft creation.
- A similarity worker might inspect card bodies, turning a lightweight mechanism into a hidden audit.

Mitigation:

- `CONTEXT_BOUNDARY.md` defines phase-specific read allowlists.
- `loop_manifest.json` now mirrors these allowlists.
- `CLAUDE_CODE_HANDOFF.md` gives a single entry point for Claude Code.
- `SKILLS_AND_DEPENDENCIES.md` removes hidden dependency on Codex skills.
- `SUBAGENT_RUNTIME_CONSTRAINTS.md` prevents accidental reliance on native nested Claude Code subagents while documenting the verified `claude -p` process-level pattern.

## Remaining Limitations

- There is no automatic filesystem enforcement. The boundary is a written contract, not an OS sandbox.
- The similarity script is not implemented yet.
- No first material batch has been queued.
- No v3 card has passed through the full draft -> similarity -> provenance -> audit/adoption path yet.
- Process-level nested Claude calls are independent sessions and can drift if their prompts omit v3 boundaries; v3 uses `--permission-mode auto` to avoid headless permission blocking while retaining automatic action-level safety classification.
