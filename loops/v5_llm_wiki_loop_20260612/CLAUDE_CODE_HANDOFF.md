---
loop_id: v5_llm_wiki_loop_20260612
created: 2026-06-12
status: setup
---

# v5 Handoff

v5 是 questioning-loop-based 知识卡片生产管线的第五次迭代。独立的 0->1 过程——不引用 v4 KB、不继承 v4 卡片、不依赖 v4 的 related 图。

## v4 经验文档

全部经验固化在 v4 learnings capsule 中（7 份文档），v5 必须吸收其管线修复和技能迭代成果：

| 文件 | 核心内容 |
|------|---------|
| `../v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md` | 实际管线执行记录（vs 设计偏差） |
| `../v4_llm_wiki_loop_20260602/learnings/operational_lessons.md` | 运维教训（并发、权限、数据采集陷阱） |
| `../v4_llm_wiki_loop_20260602/learnings/design_decisions.md` | 关键设计决策及理由 |
| `../v4_llm_wiki_loop_20260602/learnings/skill_iteration_log.md` | 技能迭代记录（4 个 skill 的演化路径） |
| `../v4_llm_wiki_loop_20260602/learnings/audit_methodology.md` | FSJS 审计方法论 |
| `../v4_llm_wiki_loop_20260602/learnings/next_loop_prep.md` | v5 可执行输入（待处理源、技能更新、管线工具） |
| `../v4_llm_wiki_loop_20260602/learnings/kb_health_snapshot.md` | v4 KB 健康快照（328 卡终态） |

## 原始管线规格

`../v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md`

## 关键约束

以下约束从 v4 设计决策 + MEMORY.md 反馈中确认，v5 继续生效：

1. **Loop 独立（0->1）**：不引用前序 KB、不比较 v4/v3/v2 卡片。v4 的 328 卡仅作格式参考。
2. **Zettelkasten 无 taxonomy**：card_type/tags 自由描述；结构靠 link + governance 涌现，不预设分类体系。
3. **grep-only recall**：agent 自主 grep（canonical_concept + aliases + key_terms），zh/en/同义词多轮改写。不引入 embedding/jieba/向量。
4. **Best-effort governance zen**：目标是降熵，不是完备性。make problems simpler, not solved。
5. **中文输出，英文 key**：卡片/justification/报告主体中文；schema key/path/code/id 英文。
6. **无 cluster count target**：governance clustering 启发式驱动（topic/alias overlap），永远不设数量目标。
7. **无 Co-Authored-By trailer**：git commit 禁止 Co-Authored-By 行。
8. **model:opus for Agent calls**：所有 Agent() 调用必须传 model: "opus"（endpoint 不支持 Haiku）。
9. **bypassPermissions for loop runs**：启动命令 `claude --permission-mode bypassPermissions`。
10. **Full source reads（1M context）**：Read 全文，不要 limit:2000 防御性分页。
11. **Typed footnote 四前缀**：`[^src-N]`（raw 源）、`[^card-N]`（兄弟卡）、`[^dist-N]`（distinction）、`[^url-N]`（外链）。
12. **Justification journal**：per-card append-only 决策日记，6 event types，<=20 lines/entry。
13. **exhaust = agent-judged**：不设体量目标，材料被问尽即止。
14. **Sub-agent 无递归**：Agent tool 被 harness strip；若需嵌套调用用 `claude -p` via Bash。
15. **负载均衡**：parallel() 分配前按 token/文件数估算，单 agent 不超过平均值 2x，否则拆分。

## v4 KB 作为参考

v4 最终产出 328 张活跃卡片。v5 可以查看 v4 卡片了解"好的输出长什么样"，但 **不得** 在自己的 KB 中引用或复制 v4 内容。v5 的 related/footnote 只指向 v5 自己的卡片。

## v5 执行模型

- **Extraction**：可并行（parallel, wave-based 分批），提速。
- **Governance**：MUST 逐卡顺序执行（sequential per-card global grep）。无集群分组。
- **Sub-agent 递归**：Agent tool 被 harness strip；若需嵌套用 `claude -p` via Bash。

## v5 四项管线改进

### 1. source_router.py（逐类型 boundary-read dispatch）

替代扁平 fallback 的 `source_text_path()` 逻辑。按源类型分流读取路径：
- arxiv: agent_source_bundle.txt
- webpage: markdown.md > text.txt
- github_repo: material_bundle.txt（repo2doc 产出）> repo/README.md
- reddit/hacker_news/pypi/gist_raw: text.txt

质量门控：< 500 字节或含 blocked/captcha/403 -> `scrape_status: failed`，不传入 extraction。

**返回值格式**：仓库根相对路径（如 `data/raw/webpage/llm-wiki-net/markdown.md`）。此路径直接用作 `[^src-N]` footnote 的 material_path——指向 reader 实际阅读的文件（对 webpage 为 trafilatura 的 markdown.md 而非 raw.html）。

**PDF 通用规则**：对 PDF 源运行 pdftotext/pymupdf 生成 .txt companion；若提取失败标记 `text_extractable: false`，cards 降低 epistemic_confidence。

**Sub-bundle 协议**（适用于 microsoft-agent-governance-toolkit 等大 repo）：
- repo2doc 产出多文件命名为 `material_bundle_{sub-slug}.txt`（如 `material_bundle_docs.txt`、`material_bundle_python-sdk.txt`）
- 保持单一 source_id，每个 sub-bundle 作为独立 extraction pass
- footnote 路径包含 sub-bundle 文件名以消歧：`data/raw/github_repo/repo-microsoft-agent-governance-toolkit/material_bundle_docs.txt -- S2.1 -- "quote"`
- 若存在多个 `material_bundle_*.txt`，source_router 返回列表，coordinator 为每个 bundle 调度独立 extraction pass

### 2. Reframing skill：保留 hedging + evidence_basis 字段

v4 审计发现 62% 卡片零认识论限定词。修正：
- 保留 reader 回答中的认识论标记（'suggests' -> '据材料推测'）
- frontmatter 新增 `evidence_basis` 字段（8 项枚举）：
  - `experimental_paper`：有实验/评测章节的论文
  - `theoretical_paper`：纯形式化推导的论文
  - `survey_synthesis`：文献综述 / meta-analysis
  - `practitioner_report`：个人博客/gist 实践报告
  - `community_discussion`：社区讨论（reddit/HN）
  - `documentation`：技术文档站
  - `code_implementation`：代码库/SDK
  - `normative_standard`：行业标准（OWASP/NIST 等）
- 映射判断标准：
  - arxiv -> experimental_paper（有实验）| theoretical_paper（纯推导）| survey_synthesis（综述）
  - webpage -> documentation（技术文档站）| practitioner_report（个人博客）| normative_standard（行业标准）
  - github_repo -> code_implementation
  - reddit/hacker_news -> community_discussion
  - pypi -> documentation

### 3. Sequential governance（无集群）

```
对每张新 draft 卡 C：
  1. grep 全量 KB（canonical_concept + aliases + key_terms）命中候选集 S
  2. 对 S 中每张候选卡 Read 全文
  3. judge：duplicate / overlap_merge / distinct_link / unrelated
  4. 执行：merge -> fusion card / link -> 双向 related + footnote / unrelated -> skip
```

#### Judge 四分类操作定义

- **duplicate**：两卡 canonical_concept 等价 AND 核心论断集合重叠 > 80%（一卡知识几乎完全被另一卡覆盖）。操作：保留信息更丰富的一张，另一张 supersede + archive。
- **overlap_merge**：两卡共享核心子论题 AND 各自携带对方不包含的独特知识。合并后卡信息量 > max(A, B)。操作：新建 fusion card 综合双方，原卡均 supersede。
- **distinct_link**：两卡共享概念名/别名但论断角度不同（如一张讲机制、一张讲局限）。独立阅读各自成立。操作：双向 `[^card-N]` 或 `[^dist-N]` footnote + related 派生。
- **unrelated**：grep 命中为纯术语巧合，两卡知识域无交集。操作：skip。

**边界自检**：「如果只保留一张卡，读者是否会失去另一张卡独有的知识？」YES -> distinct_link; NO + 论断高度重叠 -> duplicate; NO + 各有独特知识需综合 -> overlap_merge。

**Anti-merge bias**（防止重蹈 v4 cluster damage）：When in doubt between overlap_merge and distinct_link, choose distinct_link。过度 merge 破坏原子性且不可逆；遗漏一个 link 在下轮 governance 可修复。

#### Merge body fusion protocol

1. **选主卡**：两卡中 footnote 数更多 / body 更长者为 primary，另一张为 secondary。
2. **融合方式**：primary body 不变，secondary 独有知识点追加到 primary body 末尾（Footnotes 之前），用 `[^src-N]` 标注来源。
3. **footnote 重编号**：secondary 的 footnote 从 primary 最大编号+1 开始递增。
4. **jj 规则**：新 hub 卡继承 primary jj + append governance merge 事件；secondary 卡 jj append deprecation 事件。
5. **governance 阶段允许 LLM 改写 body**（区别于 ingest 阶段的禁止）。

#### 顺序效应补偿：backward-补链 pass

Sequential governance 有顺序偏差：早期处理的卡在治理时 KB 尚小，link 机会少。修正方案：

- **Pass 1 (forward)**：逐卡 grep KB -> 写 forward links（C -> 已有卡）。
- **Pass 2 (backward-补链)**：governance 完成后，对所有孤儿卡 + 前 1/3 处理的卡执行反向 scan——用晚期卡的 canonical/aliases 反向 grep 早期卡，补建 backlink。

Phase 3 的「孤儿检测 gate」升级为「孤儿补链 pass」——不仅检测，且对每张孤儿卡执行反向全局 grep。

#### 治理遍历顺序

确定性排序规则：`sorted(cards, key=lambda c: (c.source_id, c.created_time))`。理由：
- 同源卡相邻处理使 intra-source dedup 更容易被发现
- 字母序保证确定性和可复现性

#### 同义词改写策略（2 轮）

- **Round 1**：同语言同义词（中文概念的其他中文说法 + 英文概念的缩写/全称）
- **Round 2**：跨语言翻译（中->英 or 英->中）
- 接受 false negative 残留，由 backward-补链 pass 兜底

### 4. YAML lint gate（frontmatter 格式验证）

每次 derive-related / frontmatter 修改后自动运行，检查：
- related 字段无双格式（行内 `[]` 与缩进 `- ` 互斥）
- 所有 frontmatter key 可被标准 YAML 解析器正确读取
- slug 引用在 index 中存在（无悬空引用）

## 目录结构

```
v5_llm_wiki_loop_20260612/
├── CLAUDE_CODE_HANDOFF.md    # 本文件（一页 handoff）
├── LOOP_START_PROMPT.md      # 新 session 启动 prompt
├── task.md                   # 任务清单（按 Phase 推进）
├── loop_state.json           # loop 状态
├── status.json               # loop status
├── queue.jsonl               # work queue
├── skills/
│   ├── questioning/          # questioner SOP
│   ├── reader/               # reader 应答契约
│   ├── reframing/            # Q&A -> card reframing
│   └── reviewer/             # quit-audit rubric
├── tools/                    # 脚本（source_router.py 等）
├── outputs/llm_wiki/
│   ├── drafts/{cards,justification}  # Stage 2 output
│   └── kb/{cards,archive,justification,indexes}  # Stage 3+4
└── run/                      # per-material run-record
```
