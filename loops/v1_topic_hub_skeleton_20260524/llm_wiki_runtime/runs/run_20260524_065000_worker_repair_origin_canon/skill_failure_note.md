# Skill Failure Note

executor_role:: repair_worker
status:: recorded
failure_type:: source_state_verification_failure

## Summary

The source-mining/planning boundary accepted and propagated a false file-state claim: X launch raw files and HN `item.json` were described as empty even though the current checkout contains non-empty local captures.

## Affected Process

- Source mining recorded the X files and HN item JSON as empty.
- Frontier update propagated the empty-file boundary into `.llmwiki/control/knowledge_frontier.yaml`.
- Node planning and repaired planning packets carried the same boundary into generator instructions.
- Candidate generation repeated the claim in `node.yaml`, `card.md`, `provenance.md`, and `change.md`.

## Root Process Failure

Workers treated an inherited or stale source-state statement as evidence without rechecking file byte size and readable content at the point where the boundary was written.

## Skill Patch Applied

Patched:

- `.llmwiki/skills/llmwiki-source-mining/SKILL.md`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`

Patch intent:

- Require byte-size and content verification before declaring a raw path empty.
- Require planners to recheck inherited file-state assumptions before writing evidence boundaries.
- Require process-boundary language when a present file is excluded for scope reasons, instead of calling it empty.

