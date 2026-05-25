LOOP_DONE

完成内容：

- 生成一张 `status: draft` 的原子事实知识卡：`artifacts/draft_card.md`
- 生成整理后的出处论证：`artifacts/provenance.md`
- 补齐状态文件和读取记录：`loop_status.md`、`read_log.md`

门禁检查：

- 只处理 `候选 3`。
- 只使用任务指定候选块与 `$.tweet.text` 来源字段。
- 知识卡包含 `statement`、`fact_type`、`support`、`scope`、`status: draft`。
- `References` 位于 `Footnotes` 前，且 `Footnotes` 是最后一个 section。
- 未读取已采纳 KB、旧审计报告、相邻候选或未列出的来源。
