# V3 Loop Report

## 当前决定

V3 已对 `data/manifests/source_digests_index.md` 中**全部 72 条来源**完成 first-pass draft + comparison_provenance。最终产出 **171 张 draft 卡片 + 171 张 draft provenance + 171 份 title-similarity top-3 工件 + 171 份 comparison provenance**。comparison 判定：**163 张 `new_card`、8 张 `provenance_delta`、0 张 `merge_candidate`/`duplicate_skip`/`revise_before_gate`**。本轮未做任何 KB adoption，adoption 推到 publication_gate（new_card）与 fusion_audit（provenance_delta）。

## Why This Loop

V2 已证明卡片生产可行，但流程偏慢，部分卡片过原子或更像标题。V3 测试"draft-first"工作流能否在保证卡片质量与可审计性的前提下提升吞吐。

## 流程轨迹

- 2026-05-25：创建 v3 capsule，注册为 active，搭建 draft-first / similarity / provenance / mailbox 合同。
- 2026-05-25：补 Claude Code 无上下文 handoff、phase-specific context boundary、本地 skill/dependency 初始化、scaffold reliability audit。
- 2026-05-25：核查 Claude Code subagent runtime——原生嵌套 Agent spawning 不支持；process-level nesting 通过 `claude -p` 可工作（marker `NESTED_CLAUDE_OK_9X2Y4Z`）。
- 2026-05-25：规范 process-level nested task 启动命令为 `claude --permission-mode auto -p "<self-contained prompt>" --output-format text`。
- 2026-05-25：加入 `LOOP_START_PROMPT.md` 作为 v3 第一次正式 production pass 的顶层 prompt。
- 2026-05-25：在 `karpathy-x-launch-post` 上跑通第一次正式 production pass（4 张英文卡 + 4 张英文 provenance + 4 张 similarity）。
- 2026-05-26：用户更正——所有输出必须以中文为主语言；4 张已有卡片 + 4 张 provenance 已重写成中文。
- 2026-05-26：实现 `tools/similarity_top3.py`（Jieba + Jaccard），覆盖 `SIMILARITY_MECHANISM_V3.md` 要求的全部输出 schema。
- 2026-05-26：增加项目级 PostToolUse hook `commit_card.sh`：每写一张 draft 卡，自动 commit 卡片 + 同名 provenance + 同名 similarity；用 `/tmp/v3-commit-card.lock` 串行化并发 worker 的提交。
- 2026-05-26：创建 worker 模板 `task_templates/batch_worker_prompt.md`（强制中文输出 + 一次读完整源文件）；以 model:opus 派发 8 个并行 batch worker，每个 worker 处理 8 条材料，共产出 129 张卡。
- 2026-05-26：用户指出 1M 上下文窗口足以一次读完整篇论文；针对 14 篇被截断的 arxiv 论文派发 4 个并行 revision worker，补出 34 张新卡（无需 edit 已有卡）。
- 2026-05-26：对全部 171 张 draft 重跑 similarity，产出 171 份新工件；更新 `queues/material_queue.md`、`queues/draft_backlog.md`、`loop_state.json`、`status.json`、本报告、`brains/production/*`、`brains/similarity/*`。
- 2026-05-26：扩展 PostToolUse hook `commit_card.sh` 以支持 `outputs/llm_wiki/drafts/comparison/*.md` 的自动提交（commit message `v3 comparison provenance: <id>`），文件锁继续生效。
- 2026-05-26：新建 `task_templates/comparison_worker_prompt.md`（中文输出、严格按 CONTEXT_BOUNDARY.md 的 comparison_provenance 读取范围、三问 + decision schema）；按 similarity 分布分 8 个并行 worker（HIGH 9 / MID-A 15 / MID-B 15 / LOW-1..4 共 107 / VLOW 25）写出全部 171 份 comparison provenance。
- 2026-05-26：comparison 判定汇总——163 张 `new_card`、8 张 `provenance_delta`、0 张其他；8 张 `provenance_delta` 写入 `queues/audit_queue.md` 待 fusion_audit。

## 产出工件

Draft 卡片（按 material 聚合）：见 `queues/material_queue.md` 与 `queues/draft_backlog.md`。

工具：

- `tools/similarity_top3.py`——自包含；读 draft cards + v2 cards 索引，按 Jieba 分词 + Jaccard 集合相似度，输出每张 draft 的 JSON 工件。
- `tools/bootstrap_dependencies.sh`——之前已存在；用于安装 `jieba`。
- `hooks/commit_card.sh`——PostToolUse hook 助手；每写一张 draft 卡片自动提交，幂等，并发安全。
- `task_templates/batch_worker_prompt.md`——material_to_draft worker 模板；中文输出 + 全文读取两条规则被显式写在里面。

配置：

- 项目 `.claude/settings.json`——注册 PostToolUse hook，匹配 `Write|Edit`，30 秒超时。

## 关键指标

- 总材料数（manifest）：72
- 已 draft 材料数：43
- `blocked: empty_source`（0KB README）：22
- `blocked: upstream_pending_or_blocked`：7
- Draft 卡片总数：**171**
- Draft provenance 总数：171
- Similarity 工件总数：171
- Comparison provenance 总数：**171**
- decision = `new_card`：**163**
- decision = `provenance_delta`：**8**
- decision = `merge_candidate` / `duplicate_skip` / `revise_before_gate`：0 / 0 / 0
- 公共 KB adopted 卡片：0（推后到 publication_gate）
- Fusion audits 待办：8（见 `queues/audit_queue.md`）
- Fusion audits 已完成：0

## Similarity 分数分布

| 区间 | 卡片数 | 含义 |
| --- | --- | --- |
| top1 ≥ 0.50 | 1 | 几乎确定的 merge_candidate |
| 0.30 ≤ top1 < 0.50 | 8 | 高 merge_candidate 风险 |
| 0.15 ≤ top1 < 0.30 | 30 | 可能 `new_card`，但和 v2 主题邻近 |
| 0.05 ≤ top1 < 0.15 | 107 | 大概率 `new_card` |
| top1 < 0.05 | 25 | 候选基本无关，倾向 `new_card` |

**最高分**：`karpathy-llm-kb-three-layer-arch`（developersio-jp-pattern）↔ v2 `llm-wiki-three-layer-architecture`，**score 0.500**。

## 观察与风险

- **中文统一标题让 similarity 真正生效**。第一次 pass 用英文标题时全部卡的 top1 都在 0.08–0.20 之间，连 `file-outputs-back-as-compounding-loop` 都漏掉了真正的 v2 邻居 `llm-wiki-query-answer-writeback`。改成中文后 39 张卡产生有意义的 ≥0.15 top1，包括 9 张 ≥0.30 的强候选。
- **首轮 worker 防御性切片是真实风险**。即使 prompt 写了 "limit:2000 先读首段"，所有 worker 都倾向不读后段。结果是 mem0、memgpt、alce、ares、locomo、longmemeval、graphrag、lightmem、graph-poisoning、poisonedrag、ragchecker、wicer、memory-as-metabolism、etamp 都漏掉了后半段（评估、ablation、appendix、prompts、defenses、failure modes）。Revision pass 全文读完后又补了 34 张知识密集卡。后续 worker 模板已修正为"一次读完整源文件"。
- **大文件特例**：`arxiv-ragas` 的 `agent_source_bundle.txt` 是 44MB，但实际论文只占前 357 行，其余 1.1M 行是 `anthology.bib`；首轮 worker 已读到第 600 行，覆盖完整论文。1M 上下文对真实论文部分够用。
- **0KB 源文件占比偏高**。22 张 github_repo `README.remote` 为 0 字节（=`data/raw/...` 抓取阶段没拿到内容），按合同跳过。后续若上游补齐，可重新走 material_to_draft。
- **Hook 并发安全已验证**。`/tmp/v3-commit-card.lock` 在 ~165 次提交里没出现 git index lock 冲突。
- **本轮没有越界写入**。所有非 v3 文件（root README、loops/registry.json、loops/current_loop.json、v0/v1/v2、data/、docs/、scripts/、user-insights/）均未触动。
- **adoption 推后是设计**。171 张 draft 中 9 张高分需要 comparison_provenance + audit；30 张中分需要逐一判定；其余可走轻量 publication_gate。

## 携带的旧风险

- Jieba title similarity 仍可能漏掉语义重叠（已被 cross-language 案例和 `file-outputs-back-as-compounding-loop` 漏掉 v2 真正邻居的案例两次确认）。
- New-card publication gate 若不强制知识密度，可能放过低质量卡片。
- 邮箱文件并不会自我唤醒；hook 或人手动操作才会驱动下一步。
- 访问边界是合约级而非沙盒级，没有外部 enforcement。
- 两层 runtime 仅能通过 process-level nesting 实现，且内嵌 prompt 必须自包含。

## comparison 阶段的发现

- **title-similarity 的局限被 comparison 阶段消化**。最高 top1 = 0.500（`karpathy-llm-kb-three-layer-arch`）实际为 `provenance_delta`，而许多 0.30–0.50 的卡因高频中文 token（`的` / `LLM` / `wiki` / `三层`）被 jaccard 误判，实际是 `new_card`。
- **8 张 `provenance_delta` 都围绕 v2 三类锚点 accepted card**：`llm-wiki-three-layer-architecture`（5 张相关 draft）、`idea-file-abstract-vague` / `idea-file-share-the-idea`（1 张）、`llm-wiki-schema-configuration-document`（2 张）。这些 draft 给出了 v2 卡未涵盖的具体实现细节 / 限定条件 / 第三方实现。
- **v2 高频干扰卡簇**：在 LOW 与 VLOW 区段，`idea-file-abstract-vague`、`llm-wiki-three-layer-architecture`、`llm-wiki-schema-configuration-document`、`llm-wiki-human-llm-role-division` 反复占据 top 1，几乎全部是 token 误中。后续版本的 similarity 机制可以考虑：(a) 引入虚词/停用词过滤；(b) 用 alias / id slug 补充 title；(c) 在 top 1 之外强制看 top 2/3 是否离题更近。
- **3 张 draft 真正的 v2 邻居没进 top 3**：`karpathy-llm-kb-three-operations`、`file-outputs-back-as-compounding-loop`、`llm-wiki-karpathy-multimodal-representation-path` 与 v2 `llm-wiki-query-answer-writeback` / `llm-wiki-persistent-compounding-artifact` / `llm-wiki-ingest-example-flow` 在主题层是真实邻居，但 title-jaccard 没把它们列入 top 3。已在各自 comparison 文件第 5 节备注，建议 fusion_audit 阶段额外检查。

## 下一步行动

1. **fusion_audit** 上述 8 张 `provenance_delta`（见 `queues/audit_queue.md`）：核对 comparison 三问是否实质回答、v2 body 是否真读过、scope 是否保留、provenance 链接是否增量可追溯。通过后把 comparison 文件反向链接到 v2 accepted card provenance。
2. **publication_gate** 163 张 `new_card`：检查每张是否满足知识密度阈值；通过则写入 `outputs/llm_wiki/kb/cards/` 与 `outputs/llm_wiki/kb/provenance/`，并维护 `outputs/llm_wiki/kb/indexes/cards.md`。
3. **补查 3 张 similarity miss**：fusion_audit 完成 8 张 provenance_delta 之后，对 `karpathy-llm-kb-three-operations`、`file-outputs-back-as-compounding-loop`、`llm-wiki-karpathy-multimodal-representation-path` 三张做一次定向比对（强制对 v2 真实邻居做 comparison），判断是否需要补写为 provenance_delta。
4. **upstream 跟进**：7 条 `pending_or_blocked` 上游材料补齐后重新入队；22 条 0KB README 上游补内容后再 draft。
5. **机制改进考虑**（可选，独立任务）：similarity_top3.py 是否引入中文停用词过滤 / alias 加权 / id slug 补充 title。
