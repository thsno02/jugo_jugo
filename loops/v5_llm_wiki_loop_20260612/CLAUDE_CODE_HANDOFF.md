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

## v4 KB 作为参考

v4 最终产出 328 张活跃卡片。v5 可以查看 v4 卡片了解"好的输出长什么样"，但 **不得** 在自己的 KB 中引用或复制 v4 内容。v5 的 related/footnote 只指向 v5 自己的卡片。

## v5 执行模型

- **Extraction**：可并行（parallel, wave-based 分批），提速。
- **Governance**：MUST 逐卡顺序执行（sequential per-card global grep）。无集群分组。
- **Sub-agent 递归**：Agent tool 被 harness strip；若需嵌套用 `claude -p` via Bash。

## v5 三项管线改进

### 1. source_router.py（逐类型 boundary-read dispatch）

替代扁平 fallback 的 `source_text_path()` 逻辑。按源类型分流读取路径：
- arxiv: agent_source_bundle.txt
- webpage: markdown.md > text.txt
- github_repo: material_bundle.txt > repo/README.md
- reddit/hacker_news/pypi/gist_raw: text.txt

质量门控：< 500 字节或含 blocked/captcha/403 -> `scrape_status: failed`，不传入 extraction。

### 2. Reframing skill：保留 hedging + evidence_basis 字段

v4 审计发现 62% 卡片零认识论限定词。修正：
- 保留 reader 回答中的认识论标记（'suggests' -> '据材料推测'）
- frontmatter 新增 `evidence_basis` 字段：experimental_paper | theoretical_paper | practitioner_report | community_discussion | documentation | code_implementation

### 3. Sequential governance（无集群）

```
对每张新 draft 卡 C：
  1. grep 全量 KB（canonical_concept + aliases + key_terms）命中候选集 S
  2. 对 S 中每张候选卡 Read 全文
  3. judge：duplicate / overlap_merge / distinct_link / unrelated
  4. 执行：merge -> fusion card / link -> 双向 related + footnote / unrelated -> skip
```

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
