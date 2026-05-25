# 任务包模板：知识卡相似门

- `task_id`:
- `iteration_id`:
- `role`: `card_similarity_gate_worker`
- `main_language`: 中文

## 目标

用 title similarity 快速列出 top 3 accepted cards，再阅读 top candidates 并回答三问，形成新卡/融合/重复/增量 provenance 决策。similarity gate 不做事实审计。

## 允许输入

- 当前任务包。
- `draft_batch_manifest_path`:
- `draft_card_paths`:
- `draft_provenance_paths`:
- `target_index_path`: `llm_wiki/kb/indexes/cards.md`
- `accepted_card_root`: `llm_wiki/kb/cards/`，只允许读取 title similarity top3 选出的卡。
- `allowed_draft_provenance_updates`:
- `draft_backlog_path`: `llm_wiki/loop/queues/draft_backlog.md`

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- top3 之外的 KB 卡片。
- 旧审计报告。
- accepted KB 卡或 accepted provenance 的写入修改。
- 枢纽页、聚类页或主题覆盖文档。

## 允许写入

- `llm_wiki/loop/iterations/<iteration_id>/loop_status.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_delivery.md`
- `llm_wiki/loop/iterations/<iteration_id>/read_log.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/similarity_top3.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/similarity_gate.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/comparison_provenance/`
- 任务包列出的 draft provenance 文件，仅允许追加 comparison provenance 链接，不允许重写事实来源。

## Similarity top3

- 对 draft title 和 index 中 accepted card title 使用 Jieba 分词。
- 用 token set 计算 Jaccard similarity。
- 排序规则：Jaccard 分数降序；分数相同则 shared-token count 降序；仍相同则保持 index 顺序。
- 每张 draft 最多返回 top 3。
- 记录 tokenizer、tokens、shared tokens、Jaccard score 和被选中的 A 卡路径。
- 只能在 top3 选出后读取这些 A 卡；不得借 comparison 继续扩展阅读其它 KB 卡。

## 三问

对每个 draft card / A 卡组合回答：

- 为什么认为 draft card 和 A 卡有共同点？
- draft card 和 A 卡的不同在哪里？
- 进行下一步操作的核心依据是什么？

## 成功门禁

- 每张草稿卡都有一个明确分类。
- 每张草稿卡都有 title similarity top3 记录，或明确说明 index 为空。
- 每个可能相似的 A 卡都有 comparison provenance。
- 每个 `merge_candidate`、`provenance_delta` 或 `duplicate_skip` 都指出对应 existing card，并回答三问。
- 对 `merge_candidate` 和 `provenance_delta` 明确标记 `audit_required: true`。
- 没有把相似门结论写成事实审计结论。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 草稿清单缺失。
- KB 索引缺失。
- `accepted_card_root` 不可读，或 index 中的 top3 路径无法对应到文件。
