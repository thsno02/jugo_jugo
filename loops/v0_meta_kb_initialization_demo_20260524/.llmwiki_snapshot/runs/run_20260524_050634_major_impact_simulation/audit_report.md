# Audit Report / 审计报告

audit_result:: held_for_impact_review

## 检查项

- Candidate bundle 位于 `versions/2.0/`。
- Root node metadata 仍指向 adopted 1.0。
- Candidate `change.md` 标记 `change_scale:: major`。
- Candidate `change.md` 标记 `propagation_required:: true`。
- Adoption 被有意 hold。

## 预期结果

`scripts/kb_compute_impact.py` 应把引用 changed node 的下游 nodes 写入 `generated/impact_queue.yaml`。
