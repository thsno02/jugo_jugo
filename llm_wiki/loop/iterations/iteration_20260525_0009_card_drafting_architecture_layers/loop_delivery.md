# loop_delivery

LOOP_DONE

- task_id: task_20260525_0010_card_drafting_candidate_7
- candidate_id: 候选 7
- outputs:
  - `artifacts/draft_card.md`
  - `artifacts/provenance.md`
- result: 已生成一张 `status: draft` 的原子事实知识卡，并完成出处论证。
- validation:
  - 只处理候选 7。
  - 知识卡包含 `statement`、`fact_type`、`support`、`scope`、`status: draft`。
  - `References` 位于 `Footnotes` 前，且 `Footnotes` 是最后一个 section。
