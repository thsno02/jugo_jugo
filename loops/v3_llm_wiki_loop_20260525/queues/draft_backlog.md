# Draft Backlog

截至 2026-05-26，v3 已产出 **171** 张 draft 卡片（每张配对 draft provenance 与 title-similarity top 3 工件），全部待 comparison_provenance 与 publication_gate / fusion_audit 处理。

## 表头说明

- `draft_card` / `draft_provenance` / `similarity_result`：相对 `loops/v3_llm_wiki_loop_20260525/` 的路径。
- `top1_v2_match`：title-jaccard top1 候选（v2 `cards.md` 索引）。
- `top1_score`：Jaccard 分数。
- `decision`：本轮全部为 `pending`，等待 comparison_provenance。
- `audit_status`：`not_required_yet`（comparison_provenance 阶段才决定）。
- `adoption_status`：`not_adopted`（本轮不进入公共 KB）。

## 卡片清单

| draft_card_id | top1 v2 match | score | source_id |
| --- | --- | --- | --- |
| `agents-md-as-schema-layer` | `llm-wiki-schema-configuration-document` | 0.250 | `complete-tech-live-frontier` |
| `aillm-wiki-four-defining-properties` | `llm-wiki-pattern-file` | 0.231 | `aillm-wiki-directory` |
| `aillm-wiki-schema-as-bottleneck` | `llm-wiki-schema-configuration-document` | 0.333 | `aillm-wiki-directory` |
| `alce-citation-recall-precision-nli` | `idea-file-abstract-vague` | 0.059 | `arxiv-alce` |
| `alce-eli5-claim-recall-design` | `idea-file-abstract-vague` | 0.053 | `arxiv-alce` |
| `alce-prompting-strategies` | `idea-file-abstract-vague` | 0.091 | `arxiv-alce` |
| `alce-retriever-and-context-utilization-gap` | `llm-wiki-query-answer-writeback` | 0.111 | `arxiv-alce` |
| `alce-three-dimension-citation-metric` | `idea-file-abstract-vague` | 0.000 | `arxiv-alce` |
| `anthemcreation-llm-wiki-setup-cost-envelope` | `llm-wiki-three-layer-architecture` | 0.231 | `anthemcreation-fr-guide` |
| `anthemcreation-llm-wiki-three-layer-architecture` | `llm-wiki-three-layer-architecture` | 0.286 | `anthemcreation-fr-guide` |
| `anthemcreation-llm-wiki-vs-rag-multi-hop` | `llm-wiki-three-layer-architecture` | 0.214 | `anthemcreation-fr-guide` |
| `ares-cross-domain-generalization-limits` | `llm-wiki-query-answer-writeback` | 0.056 | `arxiv-ares` |
| `ares-gpt4-vs-human-annotation-tradeoff` | `idea-file-abstract-vague` | 0.056 | `arxiv-ares` |
| `ares-mock-rag-system-evaluation-design` | `idea-file-abstract-vague` | 0.067 | `arxiv-ares` |
| `ares-ppi-confidence-bound` | `idea-file-abstract-vague` | 0.062 | `arxiv-ares` |
| `ares-synthetic-data-pipeline` | `llm-wiki-persistent-wiki-alternative-mode` | 0.067 | `arxiv-ares` |
| `ares-three-judge-rag-evaluation` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.067 | `arxiv-ares` |
| `audit-by-suspension-against-entrenchment` | `idea-file-abstract-vague` | 0.050 | `arxiv-memory-as-metabolism` |
| `auto-index-replaces-rag-at-small-scale` | `llm-wiki-persistent-wiki-alternative-mode` | 0.182 | `karpathy-x-launch-post` |
| `beyond-the-token-bottleneck-llm-wiki-case-study` | `llm-wiki-pattern-file` | 0.188 | `complete-tech-live-frontier` |
| `cognition-human-approved-skill-md` | `idea-file-abstract-vague` | 0.056 | `cognitionus-llm-wiki-guide` |
| `cognition-skill-loop-evidence-to-teaching` | `idea-file-abstract-vague` | 0.077 | `cognitionus-llm-wiki-guide` |
| `docs-as-code-five-pillars` | `idea-file-abstract-vague` | 0.083 | `writethedocs-docs-as-code` |
| `docs-as-code-merge-block-incentive` | `llm-wiki-schema-configuration-document` | 0.158 | `writethedocs-docs-as-code` |
| `enterprise-llm-wiki-drift-detection-loop` | `llm-wiki-three-layer-architecture` | 0.200 | `falconer-enterprise-guide` |
| `enterprise-llm-wiki-four-properties` | `llm-wiki-health-checks` | 0.133 | `falconer-enterprise-guide` |
| `enterprise-llm-wiki-tool-native-ingestion` | `llm-wiki-health-checks` | 0.143 | `falconer-enterprise-guide` |
| `etamp-attack-payload-structure` | `idea-file-abstract-vague` | 0.067 | `arxiv-etamp-memory-poisoning` |
| `etamp-capability-vs-security` | `idea-file-abstract-vague` | 0.000 | `arxiv-etamp-memory-poisoning` |
| `etamp-chaos-monkey-agent-robustness` | `idea-file-abstract-vague` | 0.000 | `arxiv-etamp-memory-poisoning` |
| `etamp-direction-asymmetry-and-stealth` | `idea-file-abstract-vague` | 0.062 | `arxiv-etamp-memory-poisoning` |
| `etamp-environment-injected-memory-poisoning` | `idea-file-abstract-vague` | 0.056 | `arxiv-etamp-memory-poisoning` |
| `etamp-frustration-exploitation` | `idea-file-abstract-vague` | 0.059 | `arxiv-etamp-memory-poisoning` |
| `etamp-long-context-recall-diagnostic` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.056 | `arxiv-etamp-memory-poisoning` |
| `etamp-pseudo-trajectory-methodology` | `idea-file-abstract-vague` | 0.000 | `arxiv-etamp-memory-poisoning` |
| `file-outputs-back-as-compounding-loop` | `llm-wiki-persistent-compounding-artifact` | 0.091 | `karpathy-x-launch-post` |
| `gragpoison-additive-vs-edit-attack` | `idea-file-abstract-vague` | 0.071 | `arxiv-graph-poisoning` |
| `graphrag-adaptive-benchmark-via-personas` | `llm-wiki-wiki-layer-generated-markdown-directory` | 0.056 | `arxiv-graphrag` |
| `graphrag-context-window-8k-optimal` | `idea-file-abstract-vague` | 0.000 | `arxiv-graphrag` |
| `graphrag-global-sensemaking-pipeline` | `idea-file-abstract-vague` | 0.067 | `arxiv-graphrag` |
| `graphrag-leiden-community-hierarchy` | `idea-file-abstract-vague` | 0.083 | `arxiv-graphrag` |
| `graphrag-manipulation-only-attack-surface` | `idea-file-abstract-vague` | 0.111 | `arxiv-graph-poisoning` |
| `graphrag-pipeline-formalism` | `llm-wiki-three-layer-architecture` | 0.154 | `arxiv-graph-poisoning` |
| `graphrag-root-community-token-efficiency` | `idea-file-abstract-vague` | 0.000 | `arxiv-graphrag` |
| `graphrag-self-reflection-gleaning` | `idea-file-abstract-vague` | 0.067 | `arxiv-graphrag` |
| `graphrag-text-defense-blind-spot` | `idea-file-abstract-vague` | 0.000 | `arxiv-graph-poisoning` |
| `hn-llm-wiki-is-just-rag-debate` | `llm-wiki-three-layer-architecture` | 0.214 | `hacker-news-original-thread` |
| `hn-source-granularity-changes-synthesis-quality` | `llm-wiki-schema-configuration-document` | 0.286 | `hacker-news-original-thread` |
| `hn-writing-as-thinking-vs-llm-wiki` | `llm-wiki-human-llm-role-division` | 0.067 | `hacker-news-original-thread` |
| `idea-file-as-agent-era-artifact` | `idea-file-abstract-vague` | 0.300 | `karpathy-x-launch-post` |
| `karpathy-gist-bookkeeping-burden` | `llm-wiki-wiki-layer-generated-markdown-directory` | 0.182 | `karpathy-gist-llm-wiki` |
| `karpathy-gist-memex-connection` | `llm-wiki-schema-configuration-document` | 0.200 | `karpathy-gist-llm-wiki` |
| `karpathy-gist-three-layers` | `llm-wiki-three-layer-architecture` | 0.250 | `karpathy-gist-llm-wiki` |
| `karpathy-llm-kb-three-layer-arch` | `llm-wiki-three-layer-architecture` | 0.500 | `developersio-jp-pattern` |
| `karpathy-llm-kb-three-operations` | `llm-wiki-query-answer-writeback` | 0.133 | `developersio-jp-pattern` |
| `karpathy-llm-wiki-obsidian-plugin-overview` | `llm-wiki-three-layer-architecture` | 0.333 | `obsidian-community-plugin` |
| `karpathy-llm-wiki-source-executable-analogy` | `llm-wiki-health-checks` | 0.167 | `anthemcreation-en-guide` |
| `karpathy-llm-wiki-three-layers` | `llm-wiki-three-layer-architecture` | 0.308 | `marvin-hn-persistent-knowledge` |
| `karpathy-llm-wiki-vs-rag` | `llm-wiki-schema-configuration-document` | 0.222 | `marvin-hn-persistent-knowledge` |
| `karpathy-wiki-aliases-and-dedup` | `idea-file-abstract-vague` | 0.062 | `obsidian-community-plugin` |
| `karpathy-wiki-extraction-granularity` | `idea-file-abstract-vague` | 0.053 | `obsidian-community-plugin` |
| `karpathy-wiki-full-context-vs-rag` | `llm-wiki-three-layer-architecture` | 0.111 | `obsidian-community-plugin` |
| `knowledge-compounding-dynamic-roi` | `idea-file-abstract-vague` | 0.056 | `arxiv-knowledge-compounding` |
| `knowledge-compounding-three-mechanisms` | `llm-wiki-ingest-example-flow` | 0.067 | `arxiv-knowledge-compounding` |
| `knowledge-compounding-tokens-as-capital` | `llm-wiki-human-llm-role-division` | 0.077 | `arxiv-knowledge-compounding` |
| `kunal-llm-c-rag-misinterpretation` | `llm-wiki-three-layer-architecture` | 0.143 | `kunal-local-knowledge-base` |
| `kunal-local-setup-walls` | `llm-wiki-schema-configuration-document` | 0.118 | `kunal-local-knowledge-base` |
| `langgraph-store-namespace-key-json-model` | `llm-wiki-schema-configuration-document` | 0.133 | `langchain-long-term-memory-docs` |
| `langgraph-tool-runtime-store-access` | `idea-file-abstract-vague` | 0.000 | `langchain-long-term-memory-docs` |
| `lightmem-complexity-formula` | `idea-file-abstract-vague` | 0.062 | `arxiv-lightmem` |
| `lightmem-light2-topic-aware-stm` | `idea-file-abstract-vague` | 0.071 | `arxiv-lightmem` |
| `lightmem-precompress-and-topic-segmentation` | `idea-file-abstract-vague` | 0.059 | `arxiv-lightmem` |
| `lightmem-sleep-time-offline-parallel-update` | `idea-file-abstract-vague` | 0.062 | `arxiv-lightmem` |
| `lightmem-three-stage-atkinson-shiffrin` | `llm-wiki-three-layer-architecture` | 0.267 | `arxiv-lightmem` |
| `llm-knowledge-base-five-stage-workflow` | `llm-wiki-human-llm-role-division` | 0.200 | `karpathy-x-launch-post` |
| `llm-wiki-contradictions-are-assets` | `llm-wiki-three-layer-architecture` | 0.188 | `openaitoolshub-six-months` |
| `llm-wiki-ingest-vs-query-workflow` | `llm-wiki-health-checks` | 0.143 | `anthemcreation-en-guide` |
| `llm-wiki-karpathy-lint-grounding-trail` | `llm-wiki-persistent-compounding-artifact` | 0.083 | `clawhub-llm-wiki-karpathy` |
| `llm-wiki-karpathy-multimodal-representation-path` | `llm-wiki-ingest-example-flow` | 0.100 | `clawhub-llm-wiki-karpathy` |
| `llm-wiki-karpathy-runtime-vs-agent-split` | `llm-wiki-three-layer-architecture` | 0.300 | `clawhub-llm-wiki-karpathy` |
| `llm-wiki-mcp-design-boundary-mechanics-not-content` | `llm-wiki-schema-configuration-document` | 0.250 | `pypi-llm-wiki-mcp` |
| `llm-wiki-mcp-four-tools` | `llm-wiki-three-layer-architecture` | 0.200 | `pypi-llm-wiki-mcp` |
| `llm-wiki-mcp-skills-vs-tools-workflow` | `llm-wiki-three-layer-architecture` | 0.214 | `pypi-llm-wiki-mcp` |
| `llm-wiki-rohit-v2-improvements` | `idea-file-abstract-vague` | 0.056 | `openaitoolshub-six-months` |
| `llm-wiki-schema-is-most-important` | `llm-wiki-schema-configuration-document` | 0.333 | `openaitoolshub-six-months` |
| `llm-wiki-tldr-load-bearing` | `idea-file-abstract-vague` | 0.000 | `openaitoolshub-six-months` |
| `locomo-event-summarization-five-error-types` | `llm-wiki-pattern-file` | 0.105 | `arxiv-locomo` |
| `locomo-long-context-adversarial-collapse` | `llm-wiki-schema-configuration-document` | 0.136 | `arxiv-locomo` |
| `locomo-observation-rag-beats-summary-rag` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.050 | `arxiv-locomo` |
| `locomo-persona-event-graph-pipeline` | `idea-file-abstract-vague` | 0.067 | `arxiv-locomo` |
| `locomo-three-task-evaluation-framework` | `idea-file-abstract-vague` | 0.000 | `arxiv-locomo` |
| `locomo-very-long-term-dialogue-dataset` | `idea-file-abstract-vague` | 0.059 | `arxiv-locomo` |
| `longmemeval-benchmark-construction-pipeline` | `idea-file-abstract-vague` | 0.071 | `arxiv-longmemeval` |
| `longmemeval-chain-of-note-and-json-reading` | `idea-file-abstract-vague` | 0.000 | `arxiv-longmemeval` |
| `longmemeval-commercial-system-failure-modes` | `idea-file-abstract-vague` | 0.059 | `arxiv-longmemeval` |
| `longmemeval-five-core-memory-abilities` | `llm-wiki-schema-configuration-document` | 0.111 | `arxiv-longmemeval` |
| `longmemeval-key-expansion-with-facts` | `idea-file-abstract-vague` | 0.000 | `arxiv-longmemeval` |
| `longmemeval-three-stage-memory-framework` | `idea-file-abstract-vague` | 0.000 | `arxiv-longmemeval` |
| `longmemeval-time-aware-query-expansion` | `idea-file-abstract-vague` | 0.053 | `arxiv-longmemeval` |
| `mem0-answer-generation-prompt-design` | `idea-file-abstract-vague` | 0.059 | `arxiv-mem0` |
| `mem0-baseline-failure-modes` | `idea-file-abstract-vague` | 0.062 | `arxiv-mem0` |
| `mem0-extract-update-pipeline` | `idea-file-abstract-vague` | 0.053 | `arxiv-mem0` |
| `mem0-graph-memory-variant` | `idea-file-abstract-vague` | 0.000 | `arxiv-mem0` |
| `mem0-locomo-benchmark-evaluation` | `idea-file-abstract-vague` | 0.067 | `arxiv-mem0` |
| `mem0-rag-chunk-size-ablation` | `idea-file-abstract-vague` | 0.059 | `arxiv-mem0` |
| `mem0-tool-call-add-update-delete-noop` | `llm-wiki-three-layer-architecture` | 0.118 | `arxiv-mem0` |
| `memgpt-dmr-task-evaluation` | `idea-file-abstract-vague` | 0.062 | `arxiv-memgpt` |
| `memgpt-docqa-pagination-failure-mode` | `llm-wiki-schema-configuration-document` | 0.087 | `arxiv-memgpt` |
| `memgpt-function-chaining-heartbeat` | `idea-file-abstract-vague` | 0.059 | `arxiv-memgpt` |
| `memgpt-main-vs-external-context` | `llm-wiki-wiki-layer-generated-markdown-directory` | 0.087 | `arxiv-memgpt` |
| `memgpt-nested-kv-multi-hop` | `idea-file-abstract-vague` | 0.000 | `arxiv-memgpt` |
| `memgpt-queue-eviction-policy` | `idea-file-abstract-vague` | 0.000 | `arxiv-memgpt` |
| `memgpt-virtual-context-os-analogy` | `llm-wiki-three-layer-architecture` | 0.100 | `arxiv-memgpt` |
| `memory-as-metabolism-architectural-separability` | `llm-wiki-three-layer-architecture` | 0.125 | `arxiv-memory-as-metabolism` |
| `memory-as-metabolism-conflict-routing-matrix` | `idea-file-abstract-vague` | 0.000 | `arxiv-memory-as-metabolism` |
| `memory-as-metabolism-contextualize-depth-fitted` | `idea-file-abstract-vague` | 0.000 | `arxiv-memory-as-metabolism` |
| `memory-as-metabolism-five-operations` | `llm-wiki-three-layer-architecture` | 0.143 | `arxiv-memory-as-metabolism` |
| `memory-as-metabolism-mirror-vs-compensate` | `idea-file-abstract-vague` | 0.100 | `arxiv-memory-as-metabolism` |
| `memory-gravity-load-bearing-protection` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.053 | `arxiv-memory-as-metabolism` |
| `microsoft-agent-governance-eight-packages` | `idea-file-abstract-vague` | 0.000 | `microsoft-agent-governance-toolkit-docs` |
| `microsoft-agent-governance-standards-alignment` | `idea-file-abstract-vague` | 0.000 | `microsoft-agent-governance-toolkit-docs` |
| `minority-pressure-promotion` | `idea-file-abstract-vague` | 0.056 | `arxiv-memory-as-metabolism` |
| `morishige-kb-compile-mem0-overlay` | `llm-wiki-three-layer-architecture` | 0.200 | `developersio-jp-pattern` |
| `my-llm-wiki-supported-source-types` | `llm-wiki-schema-configuration-document` | 0.167 | `pypi-my-llm-wiki` |
| `my-llm-wiki-three-layer-implementation` | `llm-wiki-three-layer-architecture` | 0.308 | `pypi-my-llm-wiki` |
| `nist-ai-rmf-gai-profile` | `llm-wiki-schema-configuration-document` | 0.118 | `nist-gai-profile` |
| `nvk-llm-wiki-audit-and-librarian` | `llm-wiki-three-layer-architecture` | 0.200 | `llm-wiki-net` |
| `nvk-llm-wiki-hub-and-topic-wikis` | `llm-wiki-three-layer-architecture` | 0.214 | `llm-wiki-net` |
| `nvk-llm-wiki-parallel-multi-agent-research` | `llm-wiki-three-layer-architecture` | 0.167 | `llm-wiki-net` |
| `obsidian-as-ide-llm-as-programmer` | `llm-wiki-schema-configuration-document` | 0.308 | `marvin-hn-persistent-knowledge` |
| `owasp-agentic-top10-2026-positioning` | `idea-file-abstract-vague` | 0.083 | `owasp-agentic-top10-2026` |
| `owasp-agentic-vs-llm-top10-2025` | `llm-wiki-human-llm-role-division` | 0.077 | `owasp-agentic-top10-2026` |
| `owasp-genai-landscape-2026q2` | `idea-file-abstract-vague` | 0.000 | `owasp-llm-top10-2025` |
| `owasp-llm-top10-community-genealogy` | `llm-wiki-human-llm-role-division` | 0.059 | `owasp-llm-top10-2025` |
| `poisonedrag-baselines-isolate-two-conditions` | `idea-file-abstract-vague` | 0.083 | `arxiv-poisonedrag` |
| `poisonedrag-existing-defenses-insufficient` | `idea-file-abstract-vague` | 0.000 | `arxiv-poisonedrag` |
| `poisonedrag-knowledge-database-attack-surface` | `llm-wiki-schema-configuration-document` | 0.133 | `arxiv-poisonedrag` |
| `poisonedrag-retrieval-generation-two-conditions` | `llm-wiki-wiki-layer-generated-markdown-directory` | 0.067 | `arxiv-poisonedrag` |
| `poisonedrag-survives-advanced-rag-and-agents` | `llm-wiki-human-llm-role-division` | 0.067 | `arxiv-poisonedrag` |
| `rag-chunk-level-faithfulness` | `idea-file-abstract-vague` | 0.100 | `arxiv-ragchecker` |
| `ragas-answer-relevance-metric` | `llm-wiki-human-llm-role-division` | 0.062 | `arxiv-ragas` |
| `ragas-context-relevance-metric` | `llm-wiki-human-llm-role-division` | 0.071 | `arxiv-ragas` |
| `ragas-faithfulness-metric` | `llm-wiki-human-llm-role-division` | 0.059 | `arxiv-ragas` |
| `ragas-reference-free-rag-evaluation` | `idea-file-abstract-vague` | 0.059 | `arxiv-ragas` |
| `ragas-wikieval-dataset` | `idea-file-abstract-vague` | 0.056 | `arxiv-ragas` |
| `ragchecker-claim-entailment-decomposition` | `idea-file-abstract-vague` | 0.067 | `arxiv-ragchecker` |
| `ragchecker-generator-trilemma` | `idea-file-abstract-vague` | 0.077 | `arxiv-ragchecker` |
| `ragchecker-retriever-claim-vs-chunk-precision` | `idea-file-abstract-vague` | 0.000 | `arxiv-ragchecker` |
| `ragchecker-tuning-knobs-saturate` | `idea-file-abstract-vague` | 0.083 | `arxiv-ragchecker` |
| `retrieval-not-enough-for-stale-kb` | `llm-wiki-query-answer-writeback` | 0.056 | `falconer-enterprise-guide` |
| `robin-cartier-scale-ceiling` | `llm-wiki-three-layer-architecture` | 0.150 | `robin-cartier-llm-knowledge-bases` |
| `robin-cartier-schema-as-product-doc` | `llm-wiki-schema-configuration-document` | 0.222 | `robin-cartier-llm-knowledge-bases` |
| `tkpa-graph-guided-targeted-poisoning` | `idea-file-abstract-vague` | 0.067 | `arxiv-graph-poisoning` |
| `ukpa-coreference-disruption` | `idea-file-abstract-vague` | 0.067 | `arxiv-graph-poisoning` |
| `ukpa-edit-distance-stealth-tradeoff` | `idea-file-abstract-vague` | 0.053 | `arxiv-graph-poisoning` |
| `wicer-blind-compilation-catastrophic-loss` | `llm-wiki-persistent-compounding-artifact` | 0.071 | `arxiv-wicer` |
| `wicer-cegar-compile-evaluate-refine` | `llm-wiki-persistent-compounding-artifact` | 0.100 | `arxiv-wicer` |
| `wicer-fc-rag-document-count-crossover` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.111 | `arxiv-wicer` |
| `wicer-hardware-architecture-deployment` | `idea-file-abstract-vague` | 0.000 | `arxiv-wicer` |
| `wicer-llm-judge-human-validation` | `llm-wiki-three-layer-architecture` | 0.111 | `arxiv-wicer` |
| `wicer-recovery-distribution-exceeds-fc-raw` | `raw-sources-readonly-source-of-truth` | 0.059 | `arxiv-wicer` |
| `wicer-targeted-vs-random-pinning-ablation` | `raw-sources-readonly-source-of-truth` | 0.067 | `arxiv-wicer` |
| `wikibase-conceptual-not-serialization` | `raw-sources-readonly-source-of-truth` | 0.067 | `wikibase-data-model` |
| `wikibase-item-property-snak-statement` | `idea-file-abstract-vague` | 0.077 | `wikibase-data-model` |
| `wikibase-statement-rank-and-references` | `idea-file-abstract-vague` | 0.083 | `wikibase-data-model` |
| `wikibase-three-snak-types` | `idea-file-abstract-vague` | 0.000 | `wikibase-data-model` |
| `wikibase-timevalue-uncertain-dates` | `idea-file-abstract-vague` | 0.071 | `wikibase-data-model` |
| `zep-bi-temporal-edges` | `raw-sources-readonly-source-of-truth` | 0.050 | `arxiv-zep` |
| `zep-dmr-benchmark-critique` | `idea-file-abstract-vague` | 0.050 | `arxiv-zep` |
| `zep-graphiti-three-tier-graph` | `llm-wiki-three-layer-architecture` | 0.059 | `arxiv-zep` |
| `zep-hybrid-search-rerank` | `idea-file-abstract-vague` | 0.056 | `arxiv-zep` |

## 全局观察

- 最高 top1 = **0.500**（`karpathy-llm-kb-three-layer-arch` ↔ v2 `llm-wiki-three-layer-architecture`）——极强的 merge_candidate 信号。
- top1 ≥ 0.30 的卡片共 9 张，全部需要在 comparison_provenance 阶段判定 `merge_candidate` / `provenance_delta` / `duplicate_skip`。
- top1 ∈ [0.15, 0.30) 的卡片共 30 张，可能为 `new_card` 但与 v2 既有卡片在主题上邻近。
- top1 < 0.05 的卡片共 25 张，候选很可能不相关，倾向 `new_card`。

## 默认条目 schema（保留）

- `draft_card`:
- `draft_provenance`:
- `similarity_result`:
- `comparison_provenance`:
- `decision`:
- `audit_status`:
- `adoption_status`: