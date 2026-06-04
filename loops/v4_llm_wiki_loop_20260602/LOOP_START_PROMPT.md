# V4 Loop Start Prompt

> 复制下方 prompt 到新的 Claude Code session 中启动。
> 启动命令：`claude --permission-mode bypassPermissions`

---

你是 v4 llm_wiki loop 的执行者。这是一个 questioning-loop-based 知识卡片生产管线。

## 你的第一步

1. 读 `loops/v4_llm_wiki_loop_20260602/CLAUDE_CODE_HANDOFF.md`（一页 handoff，了解全貌）
2. 读 `loops/v4_llm_wiki_loop_20260602/task.md`（v4 任务清单，按 Phase 推进）
3. 读 `loops/v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md`（完整管线规格——阶段定义、I/O schema、全局约束）

## 当前阶段

Phase 1 — Build Core Skills。具体：

1. 开发 questioning skill（`skills/questioning/SKILL.md`）——questioner 的 5 阶段 SOP，参考 `v3 future_plans/questioning_loop_design.md`
2. 开发 reader/answerer prompt（`skills/reader/PROMPT.md`）——被动应答契约
3. 开发 digest production prompt——reader 产出 digest 的 SOP
4. 开发 Q&A→card reframing logic——Q&A 转原子卡 + metadata + typed footnotes
5. 开发 reviewer prompt——quit-audit rubric（覆盖率 + 源忠实 + 知识密度）

开发完后，用 `data/raw/webpage/karpathy-gist-llm-wiki/` 做第一次实验（seed material）。

## 管线

```
collect → extract (questioning loop) → ingest → evolve/governance
```

- **extract**: coordinator 静态协调 + questioner（全文 + digest）提问 + reader/answerer 回答 + reviewer quit-audit
- **ingest**: 脚本（禁止 LLM body 复制）
- **evolve**: governance（dedup + canonical 归一化 + typed footnote distinction linking）

## 关键约束

- **loop 独立**：只用本 loop 的 cards，不比较/引用 v3/v2/v1
- **Zettelkasten**：原子卡、无 taxonomy（card_type/tags 自由描述）；结构靠 link + governance 涌现
- **grep-only recall**：agent 自主 grep，zh/en/同义词多轮改写查询。不用 embedding/jieba
- **永不删除**：superseded → `kb/archive/`，不 rm
- **中文主语言**：卡片/justification/报告中文；schema key/path/code/id 英文
- **typed footnote**：`[^src-N]`（raw 源）、`[^card-N]`（兄弟卡）、`[^dist-N]`（distinction）、`[^url-N]`（外链）
- **justification journal**：per-card append-only 决策日记（替代 provenance），6 event types，≤20 lines/entry
- **exhaust = agent-judged**：不设体量目标，材料被问尽即止
- **init 不特殊**：同一管线处理所有材料，KB 通过 governance + consumption 成熟
- **无 Co-Authored-By trailer**

## 关键设计文档位置

所有设计在 v3 capsule 的 future_plans/ 中：

```
loops/v3_llm_wiki_loop_20260525/future_plans/
├── pipeline_spec.md               # 完整管线规格（先读这个）
├── questioning_loop_design.md     # Mode A/B 对话设计
├── card_metadata_template.md      # 卡片格式参考
├── jj_template.md                 # Justification Journal 模板
├── fusion_and_governance.md       # governance 设计
├── next_loop_design.md            # 整体设计（不变量 + 阶段）
├── next_loop_optimization_and_landing.md  # 落地方案 + 卡点分析
└── design_interaction_log.md      # 16 条设计决策记录
```

## 开始工作

从 task.md 的 Phase 1 开始。先读设计文档理解全貌，然后逐个开发 skills。开发完后用 karpathy-gist 做第一次实验。每次实验后 review 产出的 cards，refine skills，再跑——这是 iteration cycle。skills 是文件，改文件 = 零成本迭代。
