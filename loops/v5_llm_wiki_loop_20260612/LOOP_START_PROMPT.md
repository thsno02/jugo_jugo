# V5 Loop Start Prompt

> 复制下方 prompt 到新的 Claude Code session 中启动。
> 启动命令：`claude --permission-mode bypassPermissions`

---

你是 v5 llm_wiki loop 的执行者。这是 questioning-loop-based 知识卡片生产管线的第五次独立迭代。

> **cwd 要求**：确认 cwd 为仓库根目录 `jugo_jugo/`（即包含 `data/`、`loops/`、`scripts/` 的目录）。如果不是，先 `cd` 到该目录。下文所有路径均基于仓库根。

## 你的第一步

1. 读 `loops/v5_llm_wiki_loop_20260612/CLAUDE_CODE_HANDOFF.md`（一页 handoff，了解全貌）
2. 读 `loops/v5_llm_wiki_loop_20260612/task.md`（v5 任务清单，按 Phase 推进）
3. 读 `loops/v4_llm_wiki_loop_20260602/learnings/next_loop_prep.md`（v5 可执行输入——源清单、技能更新、管线工具）
4. 读 `loops/v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md`（完整管线规格）

## 当前阶段

Phase 0 — Setup。具体：

1. 读 v4 learnings 全部 7 份文档，理解管线实际执行 vs 设计偏差
2. 实现 `tools/source_router.py`——按源类型 dispatch 读取路径，质量门控（< 500B = failed）
2b. 实现 `tools/repo2doc.py`——repo 目录 -> material_bundle.txt，Tier-1 前 3 个 repo 验证
2c. 实现 `tools/yaml_lint.py`——frontmatter 格式验证（YAML parser 读写 + related 双格式检测）
3. 从 v4 复制 skills 并更新 reframing（hedge 保留规则 + evidence_basis 字段）
   - v4 skills 路径：`loops/v4_llm_wiki_loop_20260602/skills/questioning/SKILL.md`、`reader/PROMPT.md`、`reframing/PROMPT.md`、`reviewer/PROMPT.md`
   - 卡片 schema 权威模板：`loops/v3_llm_wiki_loop_20260525/future_plans/card_metadata_template.md`（新增字段必须以此为基础）
4. 验证运行环境（bypassPermissions + model:opus + trafilatura 可用）

**Phase 0 完成条件**（全部满足才进入 Phase 1）：
1. source_router.py 对 `data/raw/` 中每种类型各 1 个源成功返回正确读取路径
2. repo2doc.py 对 Tier-1 前 3 个 repo 成功生成 material_bundle.txt
3. yaml_lint.py 可正常解析一张示例卡片的 frontmatter
4. skills/ 下四个 PROMPT.md/SKILL.md 文件就位且 reframing 包含 evidence_basis 和 hedge 保留规则
5. `python -c "import trafilatura"` 成功 + 对一个 webpage raw.html 成功输出 markdown
6. loop_state.json 的 phase 字段更新为 `phase1_ready`

完成后进入 Phase 1（Build/Update Skills）。

## 管线

```
collect -> extract (questioning loop) -> ingest -> sequential governance
```

- **extract**: coordinator 静态协调 + questioner 提问 + reader 回答 + reviewer quit-audit
- **ingest**: 脚本（禁止 LLM body 复制）
- **governance**: sequential per-card global grep（取代 v4 的集群分组）

## 源材料目录

根路径：`data/raw/{source_type}/{slug}/`

| source_type | 文件结构 & 读取优先级 |
|-------------|---------------------|
| arxiv | `agent_source_bundle.txt`（primary） |
| webpage | `markdown.md` > `text.txt`（trafilatura 转换优先于原始提取） |
| github_repo | `material_bundle.txt`（repo2doc 产出，待建）> `repo/README.md` |
| reddit | `text.txt` |
| hacker_news | `text.txt` |
| pypi | `text.txt` |
| gist_raw | `text.txt` |

已知死源（`scrape_status: failed`，不进入 extraction）：
- reddit: 5 个 blocked（224B）
- webpage: aicritique x2 blocked（13B）、hacker-news-lens-thread（454B 纯导航噪声）

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
- **model:opus**：所有 Agent() 调用必须传 model: "opus"（endpoint 不支持 Haiku）
- **bypassPermissions**：loop 启动命令 `claude --permission-mode bypassPermissions`
- **Full source reads**：Read 全文（1M context），不要 limit:2000 防御性分页
- **Sub-agent 无递归**：Agent tool 被 harness strip；若需嵌套调用用 `claude -p` via Bash
- **负载均衡**：parallel() 分配前按 token/文件数估算，单 agent 不超过平均值 2x，否则拆分

## v5 新增/改进

1. **source_router.py**：逐类型 boundary-read dispatch（替代扁平 fallback）
2. **Reframing hedge 保留**：源说 'suggests' 卡必须保留限定词；新增 evidence_basis 字段
3. **Sequential governance**：逐卡全局 grep，无集群分组，双向 backlink 强制 + backward-补链 pass
4. **YAML lint gate**：每次 frontmatter 修改后自动验证格式

## Extraction 编排协议

- per-material extraction 完全独立运行（无跨材料 canonical 同步）
- post-extraction fusion scan 负责去重（boundary-read = `outputs/llm_wiki/drafts/cards/*.md`）
- per-round reframe 时机：每轮问答间（非最后一步）
- SATISFIED 三条件（权威定义在 pipeline_spec.md S2.2）：(a) digest core_claims 全覆盖 (b) 无开放 chase-chain (c) 进一步提问不会产生新原子概念

## 关键设计文档位置

```
loops/v3_llm_wiki_loop_20260525/future_plans/
├── pipeline_spec.md               # 完整管线规格（先读这个）
├── questioning_loop_design.md     # Mode A/B 对话设计
├── card_metadata_template.md      # 卡片 schema 权威模板（新增字段必须以此为基础）
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
