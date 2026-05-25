# LLM Wiki Topic KB Plan / 主题 KB 计划

generated_at:: 2026-05-24T05:30:00+08:00
main_language:: zh-CN

## 纠偏结论

当前 active KB 主题已从“KB 生产机制”切换为“LLM Wiki topic”。上一轮 meta KB 已存档到：

- `archive/demo_0_meta_kb_initialization_20260524/`

## 为什么必须使用 data folder

`data/` 不是背景资料，而是 topic KB 的 primary evidence layer。真正的 LLM Wiki KB 应该从这些已保存来源生成：

- raw sources：`data/raw/`
- source manifests：`data/manifests/sources.jsonl`
- digests：`data/manifests/source_digests.jsonl`
- claims：`data/manifests/claims.jsonl`
- claim-source links：`data/manifests/claim_source_links.jsonl`
- coverage records：`data/manifests/coverage_records.jsonl`
- source/evidence reports：`reports/source_gap_review.md`、`reports/evidence_matrix.md`

`loop_plan_init_kb.md` 只应作为生产协议，不应作为内容主题。

## 第一批 node backlog

见 `.llmwiki/control/topic_node_backlog.yaml`。第一批应从 `llm_wiki_origin_and_canon` 开始，而不是从 `current_kb_initialization_loop` 开始。

## 下一步建议

生成第一个真正 topic node：

`llm_wiki_origin_and_canon`

建议 evidence scope：

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `reports/source_gap_review.md`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
