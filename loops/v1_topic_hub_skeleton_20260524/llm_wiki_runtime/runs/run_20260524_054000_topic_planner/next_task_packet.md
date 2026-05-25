# Evidence Handoff Only: llm_wiki_origin_and_canon

status: superseded_by_frontier_gate  
do_not_execute_directly: true  
superseded_by: `.llmwiki/control/orchestration_gates.yaml`  

This file was produced before `KB_INIT_KNOWLEDGE_MINING_PROTOCOL.md` was integrated into the active orchestration contract. It is useful as an evidence handoff, but it must not be used to start card generation until Source Mining Loop artifacts exist and `.llmwiki/control/knowledge_frontier.yaml` marks the candidate as `ready_to_build`.

Original packet content follows for reference.

# Original Generator Task Packet: llm_wiki_origin_and_canon

task_id: generate_llm_wiki_origin_and_canon_v0_1_0  
role: Generator worker  
target_node: `llm_wiki_origin_and_canon`  
target_topic: LLM Wiki  
expected_status: candidate_pending_audit  
main_language: zh-CN  

## 工作边界

你不是唯一执行者，不要 revert 任何现有变更，不要改动无关文件。你的任务是基于本地证据生成第一个 object-level topic node。这里的 object-level topic 是 **LLM Wiki**，不是 KB 生产机制、不是 planner/control layer，也不是上一轮 meta demo。

## 目标

生成 `llm_wiki_origin_and_canon` 的第一版 candidate node。这个 node 要回答：

- LLM Wiki / LLM Knowledge Bases 这个模式在本地语料中如何被 canonicalized？
- Karpathy 的 gist 和 X quote 中，哪些内容构成原始主张？
- 传播时间线和早期讨论语境是什么？
- HN 早期讨论中出现了哪些支持、质疑和边界问题？
- 当前证据能支持哪些事实，哪些只是解释，哪些仍是缺口？

## 允许输入

只允许读取 `evidence_scope.yaml` 中列出的 input scope。默认 primary raw inputs：

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`

允许的 secondary/navigation inputs：

- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `data/manifests/coverage_records.jsonl`
- `data/manifests/acquired_sources_index.md`
- `data/manifests/source_digests_index.md`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`
- `.llmwiki/control/topic_plan.md`
- `.llmwiki/control/topic_node_backlog.yaml`

可选 secondary raw inputs 仅在需要校验二级传播语境时读取：

- `data/raw/webpage/hacker-news-lens-thread/text.txt`
- `data/raw/webpage/marvin-hn-persistent-knowledge/text.txt`

如需读取其他文件，必须先在 node 的 provenance/audit 中记录 path、reason、use，并说明为什么 planner scope 不足。

## 禁止事项

- 不要做 web retrieval，不要尝试绕过公司网络限制。
- 不要把 `loop_plan_init_kb.md`、`.llmwiki/control/*` 或 KB 初始化机制当作 node 内容主题。
- 不要把 secondary explainers 的说法写成 Karpathy 原始主张。
- 不要为了显得完整而引入未读 source、未列 source、聊天记忆或模型常识。
- 不要强断言“LLM Wiki 优于 RAG”“已经被验证适合企业”“可以长期无漂移维护”等证据尚不足的结论。
- 不要 adopt 到 `kb/`，除非后续 auditor 明确通过 adoption gate。

## 必须产出的 version bundle

按仓库当前 node bundle 约定生成 candidate。若现有脚本要求固定文件名，至少产出：

- `nodes/llm_wiki_origin_and_canon/card.md`
- `nodes/llm_wiki_origin_and_canon/provenance.md`
- `nodes/llm_wiki_origin_and_canon/change.md`

每个文件必须标记：

- `node_id: llm_wiki_origin_and_canon`
- `version: 0.1.0`
- `status: candidate_pending_audit`
- `main_language: zh-CN`
- `topic: llm_wiki`

如本仓库已有 versioned directory 约定，可以使用等价的 `nodes/llm_wiki_origin_and_canon/v0.1.0/*`，但必须保证 validator/auditor 能定位同一 bundle。

## `card.md` 内容要求

`card.md` 应是可读的中文知识节点，不是执行日志。建议结构：

1. `# LLM Wiki 的起源与 canonical sources`
2. `## 核心结论`
3. `## 原始材料`
4. `## 时间线`
5. `## 原始主张`
6. `## 早期讨论中的分歧`
7. `## 当前证据边界`
8. `## 下一跳节点`

必须包含的事实/判断类型：

- observed fact: Karpathy gist 是 idea file，用于让 agent 按需构建个人 LLM wiki。
- observed fact: X launch/mirror 保存了 viral post、quoted original post、时间戳和社交传播指标。
- observed fact: HN thread 保存了 296 points、95 comments、链接到 gist/X mirror 的早期讨论。
- interpretation: canonical pattern 包括 raw sources、LLM-generated wiki、schema/instructions、ingest/query/lint、index/log、Obsidian-as-IDE 等元素。
- discourse note: 早期争议包括 “just RAG”、model collapse/stale claims、N*N contradiction scaling、long-context 是否会替代、human-in-the-loop 价值。
- limitation: pre-Karpathy lineage、Reddit reception、enterprise article 等仍不完整，不应在本 node 中补写。

## Citation / Provenance 要求

- 每个 substantive paragraph 至少有一个 citation marker，指向 source id 或 raw path。
- 引用 Karpathy 原始主张时优先引用 `karpathy-gist-llm-wiki` 或 `karpathy-x-launch-post`。
- 引用 HN 讨论时使用 `hacker-news-original-thread`，并区分 HN commenters 的观点与 node 作者的 synthesis。
- 引用 coverage/claim 状态时使用 claim ids 和 coverage records，不要把 manifest 当作内容原文。
- 避免长段英文原文复制；中文 paraphrase 为主。
- 在 `provenance.md` 中列出所有 read inputs、used inputs、claim ids、source ids、known gaps。

建议绑定的 claim ids：

- `claim_000001_origin_and_canon_original_karpathy_statement_exact_text`
- `claim_000002_origin_and_canon_original_date`
- `claim_000003_origin_and_canon_original_context`
- `claim_000004_origin_and_canon_examples_and_intended_workflow`
- `claim_000005_origin_and_canon_stated_or_implied_non_goals`
- `claim_000006_origin_and_canon_immediate_discussion_context`
- `claim_000007_origin_and_canon_early_forks_or_implementations`
- `claim_000008_origin_and_canon_minimal_example`

## Audit Gates

生成后必须自检并在 `change.md` 或独立 audit section 中记录结果：

- object_topic_gate: node 是否只讨论 LLM Wiki topic，而不是 KB 生产机制。
- evidence_scope_gate: 是否只使用 planner 允许输入，额外读取是否有记录。
- primary_source_gate: 核心起源事实是否至少由 Karpathy gist/X mirror/HN 原帖之一支持。
- citation_gate: 每个关键事实是否有 source id/path/claim id。
- distinction_gate: 是否区分 observed fact、interpretation、early discourse、gap。
- overclaim_gate: 是否避免超出证据的 empirical/enterprise/adoption 强结论。
- language_gate: 人类可读内容是否中文为主。
- retrieval_gate: 是否没有进行 web retrieval；如需要 retrieval，是否只写 request。

只有全部 gate 通过，才允许把 bundle 标为 `candidate_ready_for_independent_audit`。adoption 必须由后续 auditor 或 main agent 决定。

## 完成回报格式

最终回复应简短包含：

- `LOOP_DONE` 或 `LOOP_BLOCKED`
- 写入文件列表
- 使用的 primary source ids
- 未解决 evidence gaps
- audit gate 结果摘要
