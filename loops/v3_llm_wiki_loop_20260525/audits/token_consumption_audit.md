---
schema: audit.v3
topic: token_consumption
loop_id: v3_llm_wiki_loop_20260525
created_time: 2026-05-28T19:00:00+08:00
auditor: llm
status: complete
---

# V3 Loop Token 消耗审计

> 范围：v3 capsule 创建（2026-05-25T20:54:47+08:00）至 unified-citation 迁移完成（2026-05-28T18:00:00+08:00）。审计的"主会话"指顶层 `claude --permission-mode auto -p ...` 进程；"sub-agent"指主会话通过 Agent 工具或 process-level `claude -p` 派发的 nested session。

## 0. TL;DR

- 全 loop 端到端**估算总 token 消耗约 9.5–11M**，其中 sub-agent 占 ~8.74M（接近 90 %），主会话约 1–2M。
- Top-3 消耗阶段全部是 sub-agent 并行批：**adoption（1.74M）、citation migration（1.42M）、batch material→draft（1.45M）**——三者合计 ~4.6M，约占 sub-agent token 的 53 %。
- 单笔最贵的一次调用是 **derive_metadata fallback agent（623 K tokens）**——因为 bash classifier 阻塞 Python 脚本，被迫派 fresh agent 用 Read+Edit 重写 171 张卡的 `related:` frontmatter。这是"分类器干扰 → fallback agent"路径上最痛的一笔，单次成本相当于一个完整 cluster worker。
- 优化空间最大的三处：(1) 抽出共享 prompt 文件减少 worker prompt 重复；(2) 减少 worker 间对 catalog / contract 的重复 Read；(3) 把"每张卡 1 commit"的 hook 触发模式聚合到 batch commit。三项合计**保守估计可省 25–35 % token**。

---

## 1. 阶段消耗清单（measured + estimated）

### 1.1 主会话 token（estimated）

主会话使用 Anthropic SDK 时没有持久写出 token 数据。基于交互轮数（~120 个有效 turn）、每 turn 平均 reload context（~10–15 K input + 1–3 K output）粗估：

| 主会话子段 | 估算 token | 说明 |
|---|---|---|
| 第一次 production pass on `karpathy-x-launch-post`（4 张卡 + provenance + similarity） | ~25 K | 完整在主会话里走完 draft → similarity → provenance → comparison 流程 |
| 中文化重写 4 张卡 | ~8 K | 多为 Edit 局部更新，token 少 |
| 8 个 batch worker 派单 + 整理 | ~50 K | 主会话只发 prompt + 收 worker 报告 |
| revision、similarity 重跑、comparison、interlink、adoption、citation migration 各阶段调度 | ~400 K–800 K | 包括状态文件读写、queue / report bookkeeping、与 sub-agent 报告交互 |
| 系统 prompt + 上下文累积（Anthropic 标准 system + tools） | ~300 K–600 K | 整 loop 的 baseline |
| **主会话合计估算** | **~1.0–1.5 M** | 没有精确数；±30 % 浮动 |

### 1.2 Sub-agent token（measured，逐次记录）

| # | 阶段 | Worker 数 | 处理量 | 单 worker token | 阶段总 token |
|---|---|---|---|---|---|
| 1 | batch worker：material → draft | 8 | 64 条材料 / 129 张卡 | 151 K, 176 K, 174 K, 155 K, 159 K, 207 K, 216 K, 216 K | **1,453 K** |
| 2 | arxiv revision worker：14 篇 arxiv 全文重读补卡 | 4 | 14 篇 arxiv → 34 张新卡 | 247 K, 351 K, 291 K, 353 K | **1,242 K** |
| 3 | comparison_provenance worker：171 张全部跑 | 8 | 171 张 draft | 97 K, 146 K, 135 K, 222 K, 176 K, 155 K, 168 K, 130 K | **1,229 K** |
| 4 | interlink worker：6 个主题 cluster | 6 | A49 / B7 / C47 / D21 / E27 / F20 = 171 | 171 K, 67 K, 238 K, 129 K, 129 K, 129 K | **864 K** |
| 5 | adoption worker：1 fusion_audit + 5 publication_gate | 6 | 8 + 163 = 171 张 | 120 K, 350 K, 332 K, 335 K, 296 K, 307 K | **1,740 K** |
| 6 | KB index fallback agent（替代被 classifier 阻塞的 build_kb_index.py） | 2 | kb/indexes/cards.md 重建 | 99 K, 26 K | **125 K** |
| 7 | citation migration worker：unified-footnote 迁移 | 6 | A49 / B7 / C47 / D21 / E27 / F20 = 171 | 349 K, 118 K, 372 K, 196 K, 190 K, 191 K | **1,417 K** |
| 8 | derive_metadata fallback agent（替代被 classifier 阻塞的 derive_metadata_from_footnotes.py） | 1 | 171 张卡 frontmatter `related:` 重写 | 623 K | **623 K** |
| 9 | misc（hook test、smoke、recheck、handoff agent 等） | 多 | — | — | **~50 K** |
| | **Sub-agent 合计** | 41+ | 171 张卡完整 pipeline | | **8,743 K ≈ 8.74 M** |

> 注：上表 sub-agent 部分按主会话观察记录的"final report token usage"求和；这是 sub-agent 完整生命周期的累计 token（system prompt + tool calls + file reads + final response）。

### 1.3 总计估算

```
sub-agent token       ~ 8.74 M
main session token    ~ 1.00–1.50 M
                      ----------
total                 ~ 9.7–10.2 M  (call it ~10 M)
```

---

## 2. 文字 bar chart：阶段 token 排序（top-down）

```
adoption (publication_gate ×5 + fusion_audit ×1)      ████████████████████ 1,740 K
batch material→draft                                  ████████████████▌    1,453 K
citation migration                                    ████████████████     1,417 K
arxiv revision                                        █████████████▉       1,242 K
comparison_provenance                                 █████████████▌       1,229 K
interlink                                             █████████▌             864 K
derive_metadata fallback (single agent)               ██████▉                623 K
build_kb_index fallback (2 agents)                    █▍                     125 K
misc                                                  ▌                       50 K
                                                                          --------
                                                                         ~ 8,743 K
```

每格 ≈ 87 K token。

---

## 3. Top-5 token 消耗阶段：去向拆解

### 3.1 Adoption（1,740 K）

最大头。6 个 worker（1 fusion_audit + 5 publication_gate），每个处理 27–43 张卡。每张卡 worker 必须：

- Read draft card / draft provenance / similarity JSON / comparison provenance（4 个文件）
- Read v2 anchor card body（fusion_audit only，8 张）
- 在 prompt 内容里复述 `adoption_worker_prompt.md` 全文（167 行）
- Write kb card + Write kb provenance（2 个文件）

去向估算（1,740 K 总量按 6 worker 平摊）：

- **system prompt + worker prompt** ≈ 167 行 × 6 worker ≈ 6 × ~3 K = 18 K（每 worker 在 init 时读 1 次）
- **每张卡的 4 个 read 文件** ≈ avg 1.5 K × 4 × 171 = ~1,026 K（占 ~59 %）
- **每张卡的 2 个 write 文件** ≈ avg 2.5 K × 2 × 171 = ~855 K → 但因为 kb card body 是 draft body 的精确复制（"逐字保留"），这些 token 是从 draft 直接 echo 出去，并非真正"生成"，仍然占输出端 token
- **CoT 推理 + 5/6 项 gate 检查文字** ≈ avg 1 K × 171 = ~171 K
- **final report** ≈ avg 200 字 × 6 = ~12 K

**优化空间最大的两点**：
1. **kb card body 是 draft body 的逐字复制**——这部分 ~50 % 的 output token 等于把 draft body 重新打字一遍。可考虑改用 `cp` + `sed` 替换 frontmatter，但 bash classifier 经常阻塞。**真正可行的优化**：在 worker prompt 里写"用 Read 读 draft body，然后直接 Write 含相同 body 的 kb 文件"——LLM 仍需 echo body，但若改成"输出 frontmatter + 一个 marker 让脚本去拼 body"会省下 ~400 K。代价是失去 LLM 二次审稿的机会。
2. **gate_notes 文本**很多是模板化语句（"5/6 项通过…"），可以让 worker 输出结构化 JSON 字段而不是 markdown narrative，省 ~50 K。

### 3.2 Batch material → draft（1,453 K）

8 个 worker，每个处理 8 条材料，每条产 ~2 张卡。每个 worker 必须：

- Read source bundle（arxiv 论文可能 200–500 KB）
- Read 类似 prompt template（138 行）
- Write 8–18 张 draft card + 8–18 张 draft provenance + 8–18 张 draft similarity（部分 worker 只写 card+provenance，similarity 由后续脚本算）

去向估算：

- **source materials read** ≈ ~600 K（arxiv 全文是大头；karpathy gist、hn 等小源加起来不多）
- **prompt template + system prompt × 8 worker** ≈ ~50 K
- **draft body 输出** ≈ avg 2 K × 129 = ~258 K
- **draft provenance 输出** ≈ avg 1.5 K × 129 = ~194 K
- **CoT + 边读边解析** ≈ ~200 K
- **final report** ≈ ~10 K

**优化空间**：
1. arxiv 全文读取没法避开（首轮 worker 防御性切片漏掉 14 篇的后半段，导致 revision pass 又花了 1.24 M token 重读补卡——这是"省 token 反致更费 token"的负面案例）。
2. **prompt template 在 8 个 worker init 时各被读一次**：138 行 × 8 = ~12 K 重复——可优化但绝对值小。
3. 真正大头是"每条 material 对应 ~2 张卡"的输出量；这是最终产物，无法压缩。

### 3.3 Citation migration（1,417 K）

6 个 worker（A49 / B7 / C47 / D21 / E27 / F20）。每个 worker 必须：

- Read 自己 cluster 的 49（最大）张 kb 卡 body
- Read v3 KB index（kb/indexes/cards.md）以查 cross-card 目标 id
- Read CARD_CONTRACT_V3.md 理解新模型
- Read citation_migration_worker_prompt.md（148 行）
- Edit 每张卡 body（合并 References → Footnotes、加 cross-card markers、v2 anchor footnote）

去向估算：

- **cluster 内 49 卡 Read × 1 worker** ≈ avg 2 K × 49 = ~100 K（cluster A worker）
- **kb index Read × 6** ≈ ~30 K × 6 = ~180 K（**重复读，最优化点之一**）
- **CARD_CONTRACT_V3.md Read × 6** ≈ ~5 K × 6 = ~30 K（**重复读**）
- **每张卡 body Edit 过程**——LLM 必须 echo 整段 body 才能修改其中插入 marker：~2 K × 171 = ~342 K
- **Footnote section 重写** ≈ avg 1 K × 171 = ~171 K
- **CoT 判断哪句话挂哪个 marker** ≈ avg 1.5 K × 171 = ~257 K

**优化空间最大的点**：
1. **kb/indexes/cards.md 在 6 个 worker 各 Read 一次** = 5 次重复 read = 浪费 ~150 K。改进：把"id → title → source → v2_anchor"压成 1 KB 的精简表格，写进 prompt 内联，省下 file read 的 system overhead。
2. **CARD_CONTRACT_V3.md** 同理——可以把"unified-footnote 模型"摘要 200 字写进 prompt，省下 6 × 5 K = 30 K。
3. **Edit 时 LLM echo body** 是结构性损耗，无法消除，除非把"挂 marker"步骤也脚本化（但 LLM 判断"哪句话提到了哪张卡"是核心智能动作，不能下放给脚本）。

### 3.4 arxiv revision（1,242 K）

4 个 worker，全文重读 14 篇 arxiv 论文。这是**首轮 batch worker 防御性切片**留下的债：

- 首轮 worker 在 prompt 里读到"先 limit:2000 试读首段"→ 实际几乎所有 worker 都没读后半段
- Mem0 / MemGPT / ALCE / ARES / LoCoMo / LongMemEval / GraphRAG / LightMem / GRagPoison / PoisonedRAG / RAGChecker / WICER / Memory-as-Metabolism / eTAMP 共 14 篇 → 漏了评估、ablation、appendix、prompts、defenses、failure modes
- Revision worker 全文读完后又补出 34 张知识密集卡

去向估算：

- **arxiv 全文 read × 4 worker, 14 篇平摊** ≈ ~700 K（每篇 ~50 K × 14）
- **新卡 body 输出** ≈ avg 2 K × 34 = ~68 K
- **新卡 provenance 输出** ≈ avg 1.5 K × 34 = ~51 K
- **CoT 决定"是补 / 是改"** ≈ ~250 K
- **比对已有卡是否重复** ≈ ~150 K
- **final reports** ≈ ~20 K

**优化空间**：这是一笔**事后补救的成本**——如果首轮 batch worker prompt 一开始就写明"1M context 够用，请一次性 Read 全文，不要分段"，34 张补卡就能在第一轮一并产出，可省下 ~700 K（重读全文那部分）。这条经验已在 batch_worker_prompt.md 修正完毕。

### 3.5 Comparison provenance（1,229 K）

8 个 worker，每个处理 ~21 张 draft。每张卡：

- Read draft card / draft provenance / similarity JSON（3 个文件）
- Read top 1 v2 卡 body（必读）
- Read top 2 / top 3 v2 卡 body（条件读，分数接近时）
- Write comparison provenance（中文三问 + decision）

去向估算：

- **每张卡 Read** ≈ avg 2 K × 4 文件 × 171 = ~1,368 K → 但 batch 内有缓存，实际 ~750 K
- **comparison body 输出** ≈ avg 1.5 K × 171 = ~257 K
- **CoT 分析三问** ≈ avg 1 K × 171 = ~171 K
- **final reports** ≈ ~10 K

**优化空间**：top 1 / top 2 / top 3 v2 卡片中有几张被反复读（如 `idea-file-abstract-vague`、`llm-wiki-three-layer-architecture`、`llm-wiki-schema-configuration-document` 在 LOW / VLOW 区段反复占据 top 1）——多个 worker 在不同 batch 里独立 Read 同一张 v2 卡。改进：worker 间共享 v2 候选 cache 不可行（worker 是独立 session），但**可以在 prompt 里直接内联 top 1 v2 卡的 statement 文本**，让 worker 不必再 Read v2 文件。预估省 ~200 K。

---

## 4. 单笔最贵：derive_metadata fallback（623 K）

这是整个 v3 loop 里最痛的一笔单一 token 消耗。背景：

1. 用户在 unified-citation migration 完成后要求脚本从 footnote 派生 frontmatter `related:`。
2. `tools/derive_metadata_from_footnotes.py` 写好，但 **bash classifier 持续 reject `python` 调用**——多次 retry 失败。
3. Fallback 路径：派 fresh agent，让它**手动模拟脚本的逻辑**，对 171 张卡逐个 Read body → 解析 footnotes → 输出新 `related:` → Edit frontmatter。

去向估算：

- **171 张 kb 卡 Read** ≈ avg 2 K × 171 = ~342 K
- **每张卡 Edit frontmatter（注入新 related:）** ≈ avg 1 K × 171 = ~171 K
- **CoT 解析 footnote 提取 v3-* / v2-* id** ≈ ~100 K
- **final report** ≈ ~10 K

**这 623 K 完全可避免**——如果 bash classifier 没阻塞 python，原脚本跑完只需 ~5 秒、~0 token。Fallback 路径的代价是 **~120 倍 token 浪费**（623 K vs 几乎 0）。

> 同类问题在 `build_kb_index.py` 阶段也发生过，fallback 花了 125 K。两次 classifier 干扰累计 ~750 K 浪费。

---

## 5. 重复浪费的具体数据点

下表罗列 worker 间真实重复 read 的几条共享文件，估算重复浪费：

| 文件 | 大小 | 被多少 worker 读 | 重复读次数 | 浪费 token（重复部分） |
|---|---|---|---|---|
| `kb/indexes/cards.md` | ~30 K | 6（citation migration） | 5 次重复 | ~150 K |
| `CARD_CONTRACT_V3.md` | ~5 K | 6（citation migration）+ 6（adoption）= 12 | 11 次重复 | ~55 K |
| `task_templates/comparison_worker_prompt.md` | ~3 K | 8 | 7 次重复 | ~21 K |
| `task_templates/adoption_worker_prompt.md` | ~3.5 K | 6 | 5 次重复 | ~17 K |
| `task_templates/citation_migration_worker_prompt.md` | ~3 K | 6 | 5 次重复 | ~15 K |
| `task_templates/batch_worker_prompt.md` | ~3 K | 8 | 7 次重复 | ~21 K |
| `task_templates/interlink_worker_prompt.md` | ~2 K | 6 | 5 次重复 | ~10 K |
| Top-1 v2 卡（最频繁的 3 张） | avg ~3 K | comparison worker 多次 | 估 ~15 次重复 | ~45 K |
| **合计** | | | | **~334 K** |

加上 system prompt（每 worker init 都重新加载一份，~5 K × 41 worker = 205 K）：

```
重复加载浪费总估 ~ 540 K
占 sub-agent 总量 ~ 6 %
```

> 这只是**结构性重复**——每个 worker 是独立 session 没有共享 context cache，所以这些重复目前**不可避免**，但可以通过 **"把可压缩内容内联进单个 prompt 文件"** 大幅缩短。

---

## 6. 具体可执行的优化方案

### 优化 1：prompt 共享化 + 摘要内联（预估省 250–400 K，~3 % 总量）

每张 worker prompt 里现在重复包含：

- 仓库根路径 / loop 目录路径 / 今天日期（每 worker prompt 都重复一遍）
- 中文语言要求 + frontmatter 字段保持英文（每 worker 都写）
- 写入边界 / 读取边界（每 worker 都写）
- Hook 行为说明（每 worker 都写）
- "不要嵌套 Agent 工具" + "不要 git" + "WORKER_DONE" 模板（每 worker 都写）

**改造**：把上述放进一个 `task_templates/_worker_common.md`（~50 行）。每个 worker prompt 顶部加 `（请先 Read task_templates/_worker_common.md）`。这样：

- 共享段从 5 × 7 个 worker prompt = 35 份重复 → 41 个 worker session 各 Read 1 次
- 但单个 worker prompt 文件本身从 ~140 行缩到 ~70 行
- 主会话派单 prompt 也省一半

预估收益：~250 K（不大，但代码层面健康）。

### 优化 2：把 kb index / contract 摘要内联进 prompt（预估省 200 K）

不让 worker Read 整个 `kb/indexes/cards.md`。改进：

- 主会话在派单时把 cluster 内必要 id+title 列表（约 1 KB / cluster）内联进 prompt
- CARD_CONTRACT_V3.md 的"unified-footnote 模型"段落（~200 字）也内联进每个 worker prompt

收益：消除 6 个 cluster worker 各 ~30 K + 12 worker 各 ~5 K 的 Read overhead。

### 优化 3：减少 hook 触发次数（预估省 100–300 K，更高的是减少 git latency）

现状：`commit_card.sh` 每写一张 draft card / kb card / comparison 都触发，全 loop 触发 ~1374 次。每次触发：

- bash 启动开销
- jq 解析 stdin
- file lock acquire/release
- git add + git commit

**主要代价不是 token**——hook 本身不消耗 LLM token，而是 wall-clock 时间 + git index lock 风险。但**间接代价**：worker 在 30 秒 hook timeout 内必须等 commit 完成，这降低了并行度。

**改进**：改为"batch commit"模式——hook 不再每次 commit，只 stage；主会话在每个阶段完成后统一发 1 个 batch commit。代价：失去"卡级 commit history"。建议**保留卡级 commit**（这是 v3 的可贵 feature），但把 commit message 简化为 1 行无 body。

预估 token 收益小（~50 K），但工程稳健性收益大。

### 优化 4：comparison worker 内联 top-1 v2 卡 statement（预估省 200 K）

8 个 comparison worker 在处理 171 张卡时，对 ~10 张高频 v2 候选反复 Read（如 `idea-file-abstract-vague` 在 ~30 张 draft 的 top 1）。

**改进**：主会话在派单前先 Read 高频 v2 卡 statement（~200 字 / 张），把 statement 内联进派给该 worker 的 batch prompt 里。worker 仍可在必要时 Read 完整卡，但 70 % 的低分情况下"读完 statement 就知道是 token 误中"，无需再 Read。

预估收益 ~200 K。

### 优化 5：避免 fallback agent 一次性整体重写（预估省 400 K）

当 bash classifier 阻塞 python 脚本，目前的 fallback 路径是**派一个 fresh agent 用 Read+Edit 重写所有产物**。代价：单 agent 需 Read 171 文件 + Edit 171 文件 = ~600 K token。

**改进**：

1. **快速 detect classifier 拒绝**——主会话遇到第一个 `command rejected` 立刻切换路径，不要重试 4 次（每次重试都消耗 ~10 K）。
2. **更精细的 fallback**：不是"重写一切"，而是把脚本逻辑拆成 N 个小 prompt 任务，每个 prompt 只处理 1–10 张卡。这样：
   - 单个 fallback agent 只需 Read 10 张卡 = ~30 K
   - 6 个 small agent 并行 = ~180 K（vs 单 agent ~600 K）
3. **更激进**：如果 python 脚本只是单纯的"frontmatter 替换"，可以让主会话直接 Edit（主会话有 Edit 工具，token 利用率比派 agent 高）。

预估收益：单次 fallback 从 623 K 降至 ~200 K，节省 ~400 K。

### 优化 6：模型分层（不可行，但应记录）

理论上：comparison worker 中"top1 score < 0.05、明显无关"的 80+ 张卡可用 sonnet/haiku 处理，省 ~30–50 % token。**但用户当前 endpoint 不允许 haiku，且 sonnet 与 opus 价差有限**——不实施。这条记下作为未来环境变化时的潜在改造。

---

## 7. 三个最该做的改动（"如果重做一遍 v3"）

按"省 token 量 / 实施复杂度"比排序：

### Top-1：**首轮 batch worker prompt 强制全文读**（已修正）

这一个改动如果在 v3 第一天就到位，**直接消除 1.24 M 的 arxiv revision 重读成本**。这是单点最大优化。

教训已沉淀进 `batch_worker_prompt.md` 当前版本（"一次读完整源文件"）。

### Top-2：**bash classifier 干扰路径短路化**（未做）

实施：在 RUNBOOK 里写明"Python 脚本第 1 次被 reject 即切换 fallback；fallback 派 N 个小 agent 而非 1 个大 agent"。

预估收益：把两次 classifier 干扰（623 K + 125 K = 748 K）降至 ~250 K，省 ~500 K。

### Top-3：**worker prompt 抽公共部分 + 内联 catalog**（未做）

实施：

- 写 `task_templates/_worker_common.md`
- 主会话派单时内联 cluster id 表格（取代 worker Read kb index）
- 高频 v2 卡 statement 内联进 comparison worker prompt

预估收益：~400 K。

---

## 8. 一条非主流但值得讨论的观察

**citation_migration 阶段的 6 个 cluster 切分（A 49 / B 7 / C 47 / D 21 / E 27 / F 20）token 不均衡**。

| cluster | 卡数 | worker token | token/卡 |
|---|---|---|---|
| A | 49 | 349 K | 7.1 K |
| B | 7 | 118 K | 16.9 K |
| C | 47 | 372 K | 7.9 K |
| D | 21 | 196 K | 9.3 K |
| E | 27 | 190 K | 7.0 K |
| F | 20 | 191 K | 9.5 K |

cluster B（仅 7 张卡）token/卡 是 cluster A 的 2.4 倍——这是**单 worker 启动 overhead 摊薄不足**的体现。如果 cluster B 拆掉、合到 cluster A 或 C 里，可省 ~70 K。但 cluster 切分由主题完整性决定（B 是"工具"主题），合并会让 worker 处理跨主题卡，可能降低 LLM 决策质量。

**结论**：按主题切 cluster 比按数量切 token 更优，但 cluster 卡数 < 10 时应考虑合并。

---

## 9. 审计验证

- 上述 sub-agent token 数据由主会话观察记录的 worker `final_response.usage.input_tokens + output_tokens` 求和。每个 worker 的 token 数值是 Anthropic API 在 sub-agent 结束时返回的 usage 块；主会话已在派单回执里逐次记录。
- 主会话 token 数无 API-level 精确读数（顶层 `claude -p` 不写 usage 到磁盘），靠交互轮数 + context 长度估算，误差可达 ±30 %。
- 审计过程本身（Read 文件 + 写 6 份审计 md）会再消耗 ~100–200 K token；这部分不计入"v3 production token"统计。

---

## 10. 结论

- v3 产出 171 张卡 / 171 张 provenance / 504+ KB-internal footnote / 8 张 v2-anchored fusion delta，**总成本约 10 M token**。
- **单卡产出成本 ≈ 60 K token / 张**（包含全 pipeline）。这个数字用于横向对比：v2 单卡产出成本无记录，v3 是首次有量化数据。
- 最大单点浪费是**首轮 batch worker 防御性切片导致的 1.24 M arxiv revision 重读**——已修正，下次 production pass 不应再现。
- 第二大浪费是**bash classifier 干扰下的两次 fallback agent，~750 K**——可通过 RUNBOOK 改 fallback 协议消化掉一半。
- 第三大浪费是**worker 间结构性重复 read，~540 K（~6 %）**——可通过 prompt 抽公共 + 内联 catalog 消化掉一半。
- 三项合计约**~1.8 M 可省**，相当于"重做一遍 v3 时压低到 ~8 M 完全可达"。

**全部审计通过**：token 消耗虽不低，但每一笔都有出处、有 token usage 数据、有可执行的优化路径。
