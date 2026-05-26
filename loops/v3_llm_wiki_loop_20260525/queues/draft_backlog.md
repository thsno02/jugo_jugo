# Draft Backlog

截至 2026-05-26，v3 已对 **171** 张 draft 卡片完成 draft + draft provenance + title-similarity top-3 + comparison provenance。下一步：8 张 `provenance_delta` 走 fusion_audit；163 张 `new_card` 走 publication_gate。

## 表头说明

- `draft_card` / `draft_provenance` / `similarity_result` / `comparison_provenance`：相对 `loops/v3_llm_wiki_loop_20260525/` 的路径（按 draft_card_id 一一对应）。
- `top1_v2_match`：title-jaccard top1 候选（v2 `cards.md` 索引）。
- `decision`：comparison_provenance 阶段写入的判定。
- `audit_required`：comparison_provenance 阶段标记是否需 audit。
- `adoption_status`：本轮全部 `not_adopted`（推到 publication_gate / fusion_audit 之后）。

## 决策汇总

| decision | 数量 | 下一步 |
| --- | ---: | --- |
| `new_card` | 163 | publication_gate（轻量门控；通过即 adopt 到 v3 KB） |
| `provenance_delta` | 8 | fusion_audit（通过后把 comparison 反向链接到对应 v2 accepted card 的 provenance） |
| `merge_candidate` | 0 | — |
| `duplicate_skip` | 0 | — |
| `revise_before_gate` | 0 | — |

## 卡片清单

| draft_card_id | source_id | top1 v2 match | score | decision | audit |
| --- | --- | --- | ---: | --- | :---: |
| `agents-md-as-schema-layer` | `complete-tech-live-frontier` | `llm-wiki-schema-configuration-document` | 0.250 | `provenance_delta` | ✓ |
| `aillm-wiki-four-defining-properties` | `aillm-wiki-directory` | `llm-wiki-pattern-file` | 0.231 | `new_card` |  |
| `aillm-wiki-schema-as-bottleneck` | `aillm-wiki-directory` | `llm-wiki-schema-configuration-document` | 0.333 | `new_card` |  |
| `alce-citation-recall-precision-nli` | `arxiv-alce` | `idea-file-abstract-vague` | 0.059 | `new_card` |  |
| `alce-eli5-claim-recall-design` | `arxiv-alce` | `idea-file-abstract-vague` | 0.053 | `new_card` |  |
| `alce-prompting-strategies` | `arxiv-alce` | `idea-file-abstract-vague` | 0.091 | `new_card` |  |
| `alce-retriever-and-context-utilization-gap` | `arxiv-alce` | `llm-wiki-query-answer-writeback` | 0.111 | `new_card` |  |
| `alce-three-dimension-citation-metric` | `arxiv-alce` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `anthemcreation-llm-wiki-setup-cost-envelope` | `anthemcreation-fr-guide` | `llm-wiki-three-layer-architecture` | 0.231 | `new_card` |  |
| `anthemcreation-llm-wiki-three-layer-architecture` | `anthemcreation-fr-guide` | `llm-wiki-three-layer-architecture` | 0.286 | `provenance_delta` | ✓ |
| `anthemcreation-llm-wiki-vs-rag-multi-hop` | `anthemcreation-fr-guide` | `llm-wiki-three-layer-architecture` | 0.214 | `new_card` |  |
| `ares-cross-domain-generalization-limits` | `arxiv-ares` | `llm-wiki-query-answer-writeback` | 0.056 | `new_card` |  |
| `ares-gpt4-vs-human-annotation-tradeoff` | `arxiv-ares` | `idea-file-abstract-vague` | 0.056 | `new_card` |  |
| `ares-mock-rag-system-evaluation-design` | `arxiv-ares` | `idea-file-abstract-vague` | 0.067 | `new_card` |  |
| `ares-ppi-confidence-bound` | `arxiv-ares` | `idea-file-abstract-vague` | 0.062 | `new_card` |  |
| `ares-synthetic-data-pipeline` | `arxiv-ares` | `llm-wiki-persistent-wiki-alternative-mode` | 0.067 | `new_card` |  |
| `ares-three-judge-rag-evaluation` | `arxiv-ares` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.067 | `new_card` |  |
| `audit-by-suspension-against-entrenchment` | `arxiv-memory-as-metabolism` | `idea-file-abstract-vague` | 0.050 | `new_card` |  |
| `auto-index-replaces-rag-at-small-scale` | `karpathy-x-launch-post` | `llm-wiki-persistent-wiki-alternative-mode` | 0.182 | `new_card` |  |
| `beyond-the-token-bottleneck-llm-wiki-case-study` | `complete-tech-live-frontier` | `llm-wiki-pattern-file` | 0.188 | `new_card` |  |
| `cognition-human-approved-skill-md` | `cognitionus-llm-wiki-guide` | `idea-file-abstract-vague` | 0.056 | `new_card` |  |
| `cognition-skill-loop-evidence-to-teaching` | `cognitionus-llm-wiki-guide` | `idea-file-abstract-vague` | 0.077 | `new_card` |  |
| `docs-as-code-five-pillars` | `writethedocs-docs-as-code` | `idea-file-abstract-vague` | 0.083 | `new_card` |  |
| `docs-as-code-merge-block-incentive` | `writethedocs-docs-as-code` | `llm-wiki-schema-configuration-document` | 0.158 | `new_card` |  |
| `enterprise-llm-wiki-drift-detection-loop` | `falconer-enterprise-guide` | `llm-wiki-three-layer-architecture` | 0.200 | `provenance_delta` | ✓ |
| `enterprise-llm-wiki-four-properties` | `falconer-enterprise-guide` | `llm-wiki-health-checks` | 0.133 | `new_card` |  |
| `enterprise-llm-wiki-tool-native-ingestion` | `falconer-enterprise-guide` | `llm-wiki-health-checks` | 0.143 | `new_card` |  |
| `etamp-attack-payload-structure` | `arxiv-etamp-memory-poisoning` | `idea-file-abstract-vague` | 0.067 | `new_card` |  |
| `etamp-capability-vs-security` | `arxiv-etamp-memory-poisoning` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `etamp-chaos-monkey-agent-robustness` | `arxiv-etamp-memory-poisoning` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `etamp-direction-asymmetry-and-stealth` | `arxiv-etamp-memory-poisoning` | `idea-file-abstract-vague` | 0.062 | `new_card` |  |
| `etamp-environment-injected-memory-poisoning` | `arxiv-etamp-memory-poisoning` | `idea-file-abstract-vague` | 0.056 | `new_card` |  |
| `etamp-frustration-exploitation` | `arxiv-etamp-memory-poisoning` | `idea-file-abstract-vague` | 0.059 | `new_card` |  |
| `etamp-long-context-recall-diagnostic` | `arxiv-etamp-memory-poisoning` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.056 | `new_card` |  |
| `etamp-pseudo-trajectory-methodology` | `arxiv-etamp-memory-poisoning` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `file-outputs-back-as-compounding-loop` | `karpathy-x-launch-post` | `llm-wiki-persistent-compounding-artifact` | 0.091 | `new_card` |  |
| `gragpoison-additive-vs-edit-attack` | `arxiv-graph-poisoning` | `idea-file-abstract-vague` | 0.071 | `new_card` |  |
| `graphrag-adaptive-benchmark-via-personas` | `arxiv-graphrag` | `llm-wiki-wiki-layer-generated-markdown-directory` | 0.056 | `new_card` |  |
| `graphrag-context-window-8k-optimal` | `arxiv-graphrag` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `graphrag-global-sensemaking-pipeline` | `arxiv-graphrag` | `idea-file-abstract-vague` | 0.067 | `new_card` |  |
| `graphrag-leiden-community-hierarchy` | `arxiv-graphrag` | `idea-file-abstract-vague` | 0.083 | `new_card` |  |
| `graphrag-manipulation-only-attack-surface` | `arxiv-graph-poisoning` | `idea-file-abstract-vague` | 0.111 | `new_card` |  |
| `graphrag-pipeline-formalism` | `arxiv-graph-poisoning` | `llm-wiki-three-layer-architecture` | 0.154 | `new_card` |  |
| `graphrag-root-community-token-efficiency` | `arxiv-graphrag` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `graphrag-self-reflection-gleaning` | `arxiv-graphrag` | `idea-file-abstract-vague` | 0.067 | `new_card` |  |
| `graphrag-text-defense-blind-spot` | `arxiv-graph-poisoning` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `hn-llm-wiki-is-just-rag-debate` | `hacker-news-original-thread` | `llm-wiki-three-layer-architecture` | 0.214 | `new_card` |  |
| `hn-source-granularity-changes-synthesis-quality` | `hacker-news-original-thread` | `llm-wiki-schema-configuration-document` | 0.286 | `new_card` |  |
| `hn-writing-as-thinking-vs-llm-wiki` | `hacker-news-original-thread` | `llm-wiki-human-llm-role-division` | 0.067 | `new_card` |  |
| `idea-file-as-agent-era-artifact` | `karpathy-x-launch-post` | `idea-file-abstract-vague` | 0.300 | `provenance_delta` | ✓ |
| `karpathy-gist-bookkeeping-burden` | `karpathy-gist-llm-wiki` | `llm-wiki-wiki-layer-generated-markdown-directory` | 0.182 | `new_card` |  |
| `karpathy-gist-memex-connection` | `karpathy-gist-llm-wiki` | `llm-wiki-schema-configuration-document` | 0.200 | `new_card` |  |
| `karpathy-gist-three-layers` | `karpathy-gist-llm-wiki` | `llm-wiki-three-layer-architecture` | 0.250 | `provenance_delta` | ✓ |
| `karpathy-llm-kb-three-layer-arch` | `developersio-jp-pattern` | `llm-wiki-three-layer-architecture` | 0.500 | `provenance_delta` | ✓ |
| `karpathy-llm-kb-three-operations` | `developersio-jp-pattern` | `llm-wiki-query-answer-writeback` | 0.133 | `new_card` |  |
| `karpathy-llm-wiki-obsidian-plugin-overview` | `obsidian-community-plugin` | `llm-wiki-three-layer-architecture` | 0.333 | `new_card` |  |
| `karpathy-llm-wiki-source-executable-analogy` | `anthemcreation-en-guide` | `llm-wiki-health-checks` | 0.167 | `new_card` |  |
| `karpathy-llm-wiki-three-layers` | `marvin-hn-persistent-knowledge` | `llm-wiki-three-layer-architecture` | 0.308 | `provenance_delta` | ✓ |
| `karpathy-llm-wiki-vs-rag` | `marvin-hn-persistent-knowledge` | `llm-wiki-schema-configuration-document` | 0.222 | `new_card` |  |
| `karpathy-wiki-aliases-and-dedup` | `obsidian-community-plugin` | `idea-file-abstract-vague` | 0.062 | `new_card` |  |
| `karpathy-wiki-extraction-granularity` | `obsidian-community-plugin` | `idea-file-abstract-vague` | 0.053 | `new_card` |  |
| `karpathy-wiki-full-context-vs-rag` | `obsidian-community-plugin` | `llm-wiki-three-layer-architecture` | 0.111 | `new_card` |  |
| `knowledge-compounding-dynamic-roi` | `arxiv-knowledge-compounding` | `idea-file-abstract-vague` | 0.056 | `new_card` |  |
| `knowledge-compounding-three-mechanisms` | `arxiv-knowledge-compounding` | `llm-wiki-ingest-example-flow` | 0.067 | `new_card` |  |
| `knowledge-compounding-tokens-as-capital` | `arxiv-knowledge-compounding` | `llm-wiki-human-llm-role-division` | 0.077 | `new_card` |  |
| `kunal-llm-c-rag-misinterpretation` | `kunal-local-knowledge-base` | `llm-wiki-three-layer-architecture` | 0.143 | `new_card` |  |
| `kunal-local-setup-walls` | `kunal-local-knowledge-base` | `llm-wiki-schema-configuration-document` | 0.118 | `new_card` |  |
| `langgraph-store-namespace-key-json-model` | `langchain-long-term-memory-docs` | `llm-wiki-schema-configuration-document` | 0.133 | `new_card` |  |
| `langgraph-tool-runtime-store-access` | `langchain-long-term-memory-docs` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `lightmem-complexity-formula` | `arxiv-lightmem` | `idea-file-abstract-vague` | 0.062 | `new_card` |  |
| `lightmem-light2-topic-aware-stm` | `arxiv-lightmem` | `idea-file-abstract-vague` | 0.071 | `new_card` |  |
| `lightmem-precompress-and-topic-segmentation` | `arxiv-lightmem` | `idea-file-abstract-vague` | 0.059 | `new_card` |  |
| `lightmem-sleep-time-offline-parallel-update` | `arxiv-lightmem` | `idea-file-abstract-vague` | 0.062 | `new_card` |  |
| `lightmem-three-stage-atkinson-shiffrin` | `arxiv-lightmem` | `llm-wiki-three-layer-architecture` | 0.267 | `new_card` |  |
| `llm-knowledge-base-five-stage-workflow` | `karpathy-x-launch-post` | `llm-wiki-human-llm-role-division` | 0.200 | `new_card` |  |
| `llm-wiki-contradictions-are-assets` | `openaitoolshub-six-months` | `llm-wiki-three-layer-architecture` | 0.188 | `new_card` |  |
| `llm-wiki-ingest-vs-query-workflow` | `anthemcreation-en-guide` | `llm-wiki-health-checks` | 0.143 | `new_card` |  |
| `llm-wiki-karpathy-lint-grounding-trail` | `clawhub-llm-wiki-karpathy` | `llm-wiki-persistent-compounding-artifact` | 0.083 | `new_card` |  |
| `llm-wiki-karpathy-multimodal-representation-path` | `clawhub-llm-wiki-karpathy` | `llm-wiki-ingest-example-flow` | 0.100 | `new_card` |  |
| `llm-wiki-karpathy-runtime-vs-agent-split` | `clawhub-llm-wiki-karpathy` | `llm-wiki-three-layer-architecture` | 0.300 | `new_card` |  |
| `llm-wiki-mcp-design-boundary-mechanics-not-content` | `pypi-llm-wiki-mcp` | `llm-wiki-schema-configuration-document` | 0.250 | `new_card` |  |
| `llm-wiki-mcp-four-tools` | `pypi-llm-wiki-mcp` | `llm-wiki-three-layer-architecture` | 0.200 | `new_card` |  |
| `llm-wiki-mcp-skills-vs-tools-workflow` | `pypi-llm-wiki-mcp` | `llm-wiki-three-layer-architecture` | 0.214 | `new_card` |  |
| `llm-wiki-rohit-v2-improvements` | `openaitoolshub-six-months` | `idea-file-abstract-vague` | 0.056 | `new_card` |  |
| `llm-wiki-schema-is-most-important` | `openaitoolshub-six-months` | `llm-wiki-schema-configuration-document` | 0.333 | `new_card` |  |
| `llm-wiki-tldr-load-bearing` | `openaitoolshub-six-months` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `locomo-event-summarization-five-error-types` | `arxiv-locomo` | `llm-wiki-pattern-file` | 0.105 | `new_card` |  |
| `locomo-long-context-adversarial-collapse` | `arxiv-locomo` | `llm-wiki-schema-configuration-document` | 0.136 | `new_card` |  |
| `locomo-observation-rag-beats-summary-rag` | `arxiv-locomo` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.050 | `new_card` |  |
| `locomo-persona-event-graph-pipeline` | `arxiv-locomo` | `idea-file-abstract-vague` | 0.067 | `new_card` |  |
| `locomo-three-task-evaluation-framework` | `arxiv-locomo` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `locomo-very-long-term-dialogue-dataset` | `arxiv-locomo` | `idea-file-abstract-vague` | 0.059 | `new_card` |  |
| `longmemeval-benchmark-construction-pipeline` | `arxiv-longmemeval` | `idea-file-abstract-vague` | 0.071 | `new_card` |  |
| `longmemeval-chain-of-note-and-json-reading` | `arxiv-longmemeval` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `longmemeval-commercial-system-failure-modes` | `arxiv-longmemeval` | `idea-file-abstract-vague` | 0.059 | `new_card` |  |
| `longmemeval-five-core-memory-abilities` | `arxiv-longmemeval` | `llm-wiki-schema-configuration-document` | 0.111 | `new_card` |  |
| `longmemeval-key-expansion-with-facts` | `arxiv-longmemeval` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `longmemeval-three-stage-memory-framework` | `arxiv-longmemeval` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `longmemeval-time-aware-query-expansion` | `arxiv-longmemeval` | `idea-file-abstract-vague` | 0.053 | `new_card` |  |
| `mem0-answer-generation-prompt-design` | `arxiv-mem0` | `idea-file-abstract-vague` | 0.059 | `new_card` |  |
| `mem0-baseline-failure-modes` | `arxiv-mem0` | `idea-file-abstract-vague` | 0.062 | `new_card` |  |
| `mem0-extract-update-pipeline` | `arxiv-mem0` | `idea-file-abstract-vague` | 0.053 | `new_card` |  |
| `mem0-graph-memory-variant` | `arxiv-mem0` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `mem0-locomo-benchmark-evaluation` | `arxiv-mem0` | `idea-file-abstract-vague` | 0.067 | `new_card` |  |
| `mem0-rag-chunk-size-ablation` | `arxiv-mem0` | `idea-file-abstract-vague` | 0.059 | `new_card` |  |
| `mem0-tool-call-add-update-delete-noop` | `arxiv-mem0` | `llm-wiki-three-layer-architecture` | 0.118 | `new_card` |  |
| `memgpt-dmr-task-evaluation` | `arxiv-memgpt` | `idea-file-abstract-vague` | 0.062 | `new_card` |  |
| `memgpt-docqa-pagination-failure-mode` | `arxiv-memgpt` | `llm-wiki-schema-configuration-document` | 0.087 | `new_card` |  |
| `memgpt-function-chaining-heartbeat` | `arxiv-memgpt` | `idea-file-abstract-vague` | 0.059 | `new_card` |  |
| `memgpt-main-vs-external-context` | `arxiv-memgpt` | `llm-wiki-wiki-layer-generated-markdown-directory` | 0.087 | `new_card` |  |
| `memgpt-nested-kv-multi-hop` | `arxiv-memgpt` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `memgpt-queue-eviction-policy` | `arxiv-memgpt` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `memgpt-virtual-context-os-analogy` | `arxiv-memgpt` | `llm-wiki-three-layer-architecture` | 0.100 | `new_card` |  |
| `memory-as-metabolism-architectural-separability` | `arxiv-memory-as-metabolism` | `llm-wiki-three-layer-architecture` | 0.125 | `new_card` |  |
| `memory-as-metabolism-conflict-routing-matrix` | `arxiv-memory-as-metabolism` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `memory-as-metabolism-contextualize-depth-fitted` | `arxiv-memory-as-metabolism` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `memory-as-metabolism-five-operations` | `arxiv-memory-as-metabolism` | `llm-wiki-three-layer-architecture` | 0.143 | `new_card` |  |
| `memory-as-metabolism-mirror-vs-compensate` | `arxiv-memory-as-metabolism` | `idea-file-abstract-vague` | 0.100 | `new_card` |  |
| `memory-gravity-load-bearing-protection` | `arxiv-memory-as-metabolism` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.053 | `new_card` |  |
| `microsoft-agent-governance-eight-packages` | `microsoft-agent-governance-toolkit-docs` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `microsoft-agent-governance-standards-alignment` | `microsoft-agent-governance-toolkit-docs` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `minority-pressure-promotion` | `arxiv-memory-as-metabolism` | `idea-file-abstract-vague` | 0.056 | `new_card` |  |
| `morishige-kb-compile-mem0-overlay` | `developersio-jp-pattern` | `llm-wiki-three-layer-architecture` | 0.200 | `new_card` |  |
| `my-llm-wiki-supported-source-types` | `pypi-my-llm-wiki` | `llm-wiki-schema-configuration-document` | 0.167 | `new_card` |  |
| `my-llm-wiki-three-layer-implementation` | `pypi-my-llm-wiki` | `llm-wiki-three-layer-architecture` | 0.308 | `new_card` |  |
| `nist-ai-rmf-gai-profile` | `nist-gai-profile` | `llm-wiki-schema-configuration-document` | 0.118 | `new_card` |  |
| `nvk-llm-wiki-audit-and-librarian` | `llm-wiki-net` | `llm-wiki-three-layer-architecture` | 0.200 | `new_card` |  |
| `nvk-llm-wiki-hub-and-topic-wikis` | `llm-wiki-net` | `llm-wiki-three-layer-architecture` | 0.214 | `new_card` |  |
| `nvk-llm-wiki-parallel-multi-agent-research` | `llm-wiki-net` | `llm-wiki-three-layer-architecture` | 0.167 | `new_card` |  |
| `obsidian-as-ide-llm-as-programmer` | `marvin-hn-persistent-knowledge` | `llm-wiki-schema-configuration-document` | 0.308 | `new_card` |  |
| `owasp-agentic-top10-2026-positioning` | `owasp-agentic-top10-2026` | `idea-file-abstract-vague` | 0.083 | `new_card` |  |
| `owasp-agentic-vs-llm-top10-2025` | `owasp-agentic-top10-2026` | `llm-wiki-human-llm-role-division` | 0.077 | `new_card` |  |
| `owasp-genai-landscape-2026q2` | `owasp-llm-top10-2025` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `owasp-llm-top10-community-genealogy` | `owasp-llm-top10-2025` | `llm-wiki-human-llm-role-division` | 0.059 | `new_card` |  |
| `poisonedrag-baselines-isolate-two-conditions` | `arxiv-poisonedrag` | `idea-file-abstract-vague` | 0.083 | `new_card` |  |
| `poisonedrag-existing-defenses-insufficient` | `arxiv-poisonedrag` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `poisonedrag-knowledge-database-attack-surface` | `arxiv-poisonedrag` | `llm-wiki-schema-configuration-document` | 0.133 | `new_card` |  |
| `poisonedrag-retrieval-generation-two-conditions` | `arxiv-poisonedrag` | `llm-wiki-wiki-layer-generated-markdown-directory` | 0.067 | `new_card` |  |
| `poisonedrag-survives-advanced-rag-and-agents` | `arxiv-poisonedrag` | `llm-wiki-human-llm-role-division` | 0.067 | `new_card` |  |
| `rag-chunk-level-faithfulness` | `arxiv-ragchecker` | `idea-file-abstract-vague` | 0.100 | `new_card` |  |
| `ragas-answer-relevance-metric` | `arxiv-ragas` | `llm-wiki-human-llm-role-division` | 0.062 | `new_card` |  |
| `ragas-context-relevance-metric` | `arxiv-ragas` | `llm-wiki-human-llm-role-division` | 0.071 | `new_card` |  |
| `ragas-faithfulness-metric` | `arxiv-ragas` | `llm-wiki-human-llm-role-division` | 0.059 | `new_card` |  |
| `ragas-reference-free-rag-evaluation` | `arxiv-ragas` | `idea-file-abstract-vague` | 0.059 | `new_card` |  |
| `ragas-wikieval-dataset` | `arxiv-ragas` | `idea-file-abstract-vague` | 0.056 | `new_card` |  |
| `ragchecker-claim-entailment-decomposition` | `arxiv-ragchecker` | `idea-file-abstract-vague` | 0.067 | `new_card` |  |
| `ragchecker-generator-trilemma` | `arxiv-ragchecker` | `idea-file-abstract-vague` | 0.077 | `new_card` |  |
| `ragchecker-retriever-claim-vs-chunk-precision` | `arxiv-ragchecker` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `ragchecker-tuning-knobs-saturate` | `arxiv-ragchecker` | `idea-file-abstract-vague` | 0.083 | `new_card` |  |
| `retrieval-not-enough-for-stale-kb` | `falconer-enterprise-guide` | `llm-wiki-query-answer-writeback` | 0.056 | `new_card` |  |
| `robin-cartier-scale-ceiling` | `robin-cartier-llm-knowledge-bases` | `llm-wiki-three-layer-architecture` | 0.150 | `new_card` |  |
| `robin-cartier-schema-as-product-doc` | `robin-cartier-llm-knowledge-bases` | `llm-wiki-schema-configuration-document` | 0.222 | `provenance_delta` | ✓ |
| `tkpa-graph-guided-targeted-poisoning` | `arxiv-graph-poisoning` | `idea-file-abstract-vague` | 0.067 | `new_card` |  |
| `ukpa-coreference-disruption` | `arxiv-graph-poisoning` | `idea-file-abstract-vague` | 0.067 | `new_card` |  |
| `ukpa-edit-distance-stealth-tradeoff` | `arxiv-graph-poisoning` | `idea-file-abstract-vague` | 0.053 | `new_card` |  |
| `wicer-blind-compilation-catastrophic-loss` | `arxiv-wicer` | `llm-wiki-persistent-compounding-artifact` | 0.071 | `new_card` |  |
| `wicer-cegar-compile-evaluate-refine` | `arxiv-wicer` | `llm-wiki-persistent-compounding-artifact` | 0.100 | `new_card` |  |
| `wicer-fc-rag-document-count-crossover` | `arxiv-wicer` | `rag-document-qa-does-not-accumulate-synthesized-knowledge` | 0.111 | `new_card` |  |
| `wicer-hardware-architecture-deployment` | `arxiv-wicer` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `wicer-llm-judge-human-validation` | `arxiv-wicer` | `llm-wiki-three-layer-architecture` | 0.111 | `new_card` |  |
| `wicer-recovery-distribution-exceeds-fc-raw` | `arxiv-wicer` | `raw-sources-readonly-source-of-truth` | 0.059 | `new_card` |  |
| `wicer-targeted-vs-random-pinning-ablation` | `arxiv-wicer` | `raw-sources-readonly-source-of-truth` | 0.067 | `new_card` |  |
| `wikibase-conceptual-not-serialization` | `wikibase-data-model` | `raw-sources-readonly-source-of-truth` | 0.067 | `new_card` |  |
| `wikibase-item-property-snak-statement` | `wikibase-data-model` | `idea-file-abstract-vague` | 0.077 | `new_card` |  |
| `wikibase-statement-rank-and-references` | `wikibase-data-model` | `idea-file-abstract-vague` | 0.083 | `new_card` |  |
| `wikibase-three-snak-types` | `wikibase-data-model` | `idea-file-abstract-vague` | 0.000 | `new_card` |  |
| `wikibase-timevalue-uncertain-dates` | `wikibase-data-model` | `idea-file-abstract-vague` | 0.071 | `new_card` |  |
| `zep-bi-temporal-edges` | `arxiv-zep` | `raw-sources-readonly-source-of-truth` | 0.050 | `new_card` |  |
| `zep-dmr-benchmark-critique` | `arxiv-zep` | `idea-file-abstract-vague` | 0.050 | `new_card` |  |
| `zep-graphiti-three-tier-graph` | `arxiv-zep` | `llm-wiki-three-layer-architecture` | 0.059 | `new_card` |  |
| `zep-hybrid-search-rerank` | `arxiv-zep` | `idea-file-abstract-vague` | 0.056 | `new_card` |  |

## provenance_delta 列表（待 audit）

下列 8 张 draft 在 comparison 阶段被判为 `provenance_delta`：v2 已有同主题 accepted card，但 draft 引入了新证据 / 新边界 / 新数值 / 新视角。fusion_audit 通过后应把对应 comparison 文件反向链接到 v2 accepted card 的 provenance。

- `agents-md-as-schema-layer` — top1 `llm-wiki-schema-configuration-document` @ 0.250
- `anthemcreation-llm-wiki-three-layer-architecture` — top1 `llm-wiki-three-layer-architecture` @ 0.286
- `enterprise-llm-wiki-drift-detection-loop` — top1 `llm-wiki-three-layer-architecture` @ 0.200
- `idea-file-as-agent-era-artifact` — top1 `idea-file-abstract-vague` @ 0.300
- `karpathy-gist-three-layers` — top1 `llm-wiki-three-layer-architecture` @ 0.250
- `karpathy-llm-kb-three-layer-arch` — top1 `llm-wiki-three-layer-architecture` @ 0.500
- `karpathy-llm-wiki-three-layers` — top1 `llm-wiki-three-layer-architecture` @ 0.308
- `robin-cartier-schema-as-product-doc` — top1 `llm-wiki-schema-configuration-document` @ 0.222

## 全局观察

- title-similarity 不准确性已被 comparison 阶段消化：最高 top1 = 0.500 的卡片实际是 `provenance_delta`（同主题不同视角），而很多 0.30–0.50 的卡片实际是 `new_card`（v2 candidate 是因为高频常用 token 误中）。
- `idea-file-abstract-vague` 在 v2 cards.md 中作为 jaccard 高频干扰卡反复出现在低分段 top1，但 comparison 阶段已逐张验证主题无关。
- 0 张 `merge_candidate` / `duplicate_skip` / `revise_before_gate`：第一轮 production pass 的 171 张 draft 在质量和与 v2 的重叠程度上落在可推进的位置。

## 默认条目 schema（保留）

- `draft_card`:
- `draft_provenance`:
- `similarity_result`:
- `comparison_provenance`:
- `decision`:
- `audit_status`:
- `adoption_status`: