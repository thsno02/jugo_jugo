# loop_delivery

LOOP_DONE

- task_id: task_20260525_0019_card_drafting_candidate_9
- candidate_id: 候选 9
- result: 已生成一张 `status: draft` 的原子事实知识卡和一份出处论证。
- outputs:
  - `artifacts/draft_card.md`
  - `artifacts/provenance.md`
  - `loop_status.md`
  - `read_log.md`
- checks:
  - 只处理候选 9。
  - 只使用指定候选文件核对字段，并只使用 `raw.txt:31-32` 作为事实证据。
  - 知识卡包含 `statement`、`fact_type`、`support`、`scope`、`status: draft`。
  - 知识卡中 `References` 位于 `Footnotes` 之前，且 `Footnotes` 为最后一个 section。
