# Phase 4 FILTER 审计报告

审计时间: 2026-06-12
KB 路径: `loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/cards/`


## 1. 源忠实性 grep 验证

- 总卡片数: 477 (其中 46 张无 [^src-N] 脚注，不参与验证)
- 总验证脚注: 431 (每卡随机抽 1 条)
- grep-verified: 413 (95%)
- suspect: 18 (4%)

### Suspect 清单

| card_id | footnote | source_file | grep_phrase |
|---------|----------|-------------|-------------|
| agent-environment-awareness-under-stress | src-3 | `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` | High confidence examples: 'The typed search text was becomin |
| alce-citation-support-gap | src-4 | `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` | ChatGPT Vanilla (5-psg): Rec. 73.6; w/ Rerank: Rec. 84.8 |
| chaos-monkey-agent-stress-testing | src-2 | `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` | With p_click=0.4, p_scroll=1, and p_type=1, tasks remain com |
| collection-ingestion-adapter-system | src-1 | `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` | Supported: git, mediawiki-dump, mediawiki-api, csv-messages, |
| dual-link-obsidian-agent-compatibility | src-2 | `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` | The wiki is not locked into any tool |
| instruction-tuning-citation-ability | src-2 | `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` | LLaMA-13B (3-psg): Rec. 10.6 |
| knowledge-compilation-paradigm | src-3 | `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` | raw/ # 原始素材（不可变） |
| langgraph-store-search-capabilities | src-1 | `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` | items = store.search(namespace, filter={\"my-key\": \"my-val |
| llm-as-judge-position-bias | src-3 | `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` | GPT Ranking 0.54 0.40 0.52 |
| locomo-temporal-reasoning-difficulty | src-2 | `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` | Human temporal 92.6; GPT-3.5-16K 12K temporal 25.0; Observat |
| observation-based-rag-dialogue | src-2 | `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` | Observation top-5: Overall 41.4; Dialog top-25: Overall 35.8 |
| poisonedrag-nontarget-question-impact | src-1 | `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` | 0.3% and 0.9% |
| ragchecker-retriever-metrics | src-1 | `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` | we compute claim recall as the proportion of {c^(gt)_i \| c^( |
| source-id-repair-mechanism | src-2 | `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` | kb_repair_source_ids --vault-root /vault" and "--apply |
| tkpa-experimental-results | src-2 | `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` | TKPA LP 94496 48/155 0.055%/0.164% |
| tkpa-vulnerability-score | src-1 | `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` | we define a vulnerability score for each community: V_score  |
| wiki-page-generation-output | src-2 | `data/raw/webpage/obsidian-community-plugin/markdown.md` | type: entity; created: 2026-05-15; sources: [[sources/machin |
| zep-dmr-benchmark-results | src-1 | `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` | Zep achieved 94.8% accuracy with gpt-4-turbo and 98.2% with  |


## 2. 权威扁平化

- 检查卡片总数: 307 (排除 comparison 后)
- 零限定词卡片: 245 (79%)

按 evidence_basis 分:

- experimental_paper: 137/181 (75%)
- theoretical_paper: 15/17 (88%)
- practitioner_report: 90/103 (87%)
- community_discussion: 3/6 (50%)


## 3. 跨域桥梁

| Domain | 卡片数 | 对外链接数 | 平均对外链接/卡 |
|--------|--------|-----------|----------------|
| arxiv | 200 | 33 | 0.17 |
| github_repo | 76 | 89 | 1.17 |
| hacker_news | 6 | 1 | 0.17 |
| pypi | 6 | 20 | 3.33 |
| webpage | 189 | 95 | 0.50 |
