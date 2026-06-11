# V5 Loop Start Prompt

> 复制下方 prompt 到新的 Claude Code session 中启动。
> 启动命令：`claude --permission-mode bypassPermissions`

---

你是 v5 llm_wiki loop 的执行者。这是 questioning-loop-based 知识卡片生产管线的第五次独立迭代。

## 你的第一步

1. 读 `loops/v5_llm_wiki_loop_20260612/CLAUDE_CODE_HANDOFF.md`（一页 handoff，了解全貌）
2. 读 `loops/v5_llm_wiki_loop_20260612/task.md`（v5 任务清单，按 Phase 推进）
3. 读 `loops/v4_llm_wiki_loop_20260602/learnings/next_loop_prep.md`（v5 可执行输入——源清单、技能更新、管线工具）
4. 读 `loops/v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md`（完整管线规格）

## 当前阶段

Phase 0 — Setup。具体：

1. 读 v4 learnings 全部 7 份文档，理解管线实际执行 vs 设计偏差
2. 实现 `tools/source_router.py`——按源类型 dispatch 读取路径，质量门控（< 500B = failed）
3. 从 v4 复制 skills 并更新 reframing（hedge 保留规则 + evidence_basis 字段）
4. 验证运行环境（bypassPermissions + model:opus + trafilatura 可用）

完成后进入 Phase 1（Build/Update Skills）。

## 管线

```
collect -> extract (questioning loop) -> ingest -> sequential governance
```

- **extract**: coordinator 静态协调 + questioner 提问 + reader 回答 + reviewer quit-audit
- **ingest**: 脚本（禁止 LLM body 复制）
- **governance**: sequential per-card global grep（取代 v4 的集群分组）

## 关键约束

- **loop 独立**：只用本 loop 的 cards，不比较/引用 v4/v3/v2/v1
- **Zettelkasten**：原子卡、无 taxonomy；结构靠 link + governance 涌现
- **grep-only recall**：agent 自主 grep，zh/en/同义词多轮改写。不用 embedding/jieba
- **Best-effort governance zen**：降熵不求完备，make problems simpler not solved
- **中文主语言**：卡片/justification/报告中文；schema key/path/code/id 英文
- **无 cluster count target**：启发式驱动，不是数量驱动
- **typed footnote**：`[^src-N]`（raw 源）、`[^card-N]`（兄弟卡）、`[^dist-N]`（distinction）、`[^url-N]`（外链）
- **justification journal**：per-card append-only 决策日记，6 event types，<=20 lines/entry
- **exhaust = agent-judged**：不设体量目标，材料被问尽即止
- **无 Co-Authored-By trailer**

## v5 新增/改进

1. **source_router.py**：逐类型 boundary-read dispatch（替代扁平 fallback）
2. **Reframing hedge 保留**：源说 'suggests' 卡必须保留限定词；新增 evidence_basis 字段
3. **Sequential governance**：逐卡全局 grep，无集群分组，双向 backlink 强制
4. **YAML lint gate**：每次 frontmatter 修改后自动验证格式

## 关键设计文档位置

```
loops/v3_llm_wiki_loop_20260525/future_plans/
├── pipeline_spec.md               # 完整管线规格（先读这个）
├── questioning_loop_design.md     # Mode A/B 对话设计
├── card_metadata_template.md      # 卡片格式参考
├── jj_template.md                 # Justification Journal 模板
├── fusion_and_governance.md       # governance 设计
└── next_loop_design.md            # 整体设计

loops/v4_llm_wiki_loop_20260602/learnings/
├── pipeline_actual.md             # 实际执行 vs 设计偏差
├── operational_lessons.md         # 运维教训
├── design_decisions.md            # 关键设计决策
├── skill_iteration_log.md         # 技能演化
├── audit_methodology.md           # FSJS 审计方法论
├── next_loop_prep.md              # v5 可执行输入
└── kb_health_snapshot.md          # v4 终态快照
```

## 开始工作

从 task.md 的 Phase 0 开始。先读全部 v4 learnings 理解全貌（特别是 next_loop_prep.md 的"第一天该做什么"），然后实现管线工具、更新 skills。Phase 0 完成后进入 Phase 1 测试 skills 改进效果。
