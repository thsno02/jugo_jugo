# V3 citation_migration worker 指令

你是 v3 KB unified-citation 迁移 worker。本会话无上下文继承。任务是把分配给你的一组**已 adopted** 卡片改造成新合同形态：

- 砍掉 `## References` 章节
- 升级 `## Footnotes` 为唯一 citation hub
- 在 body 中给"自然提到的其他 v3 / v2 卡 / external URL"加 inline `[^id]` markers
- 8 张 v2-anchored 卡的 v2 anchor 关系也变成 body 里某句话上的 `[^v2-1]` footnote

## 仓库与路径

- 仓库根目录：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo`（先 `cd`）
- 修改对象目录：`loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/<id>.md`（**仅 kb 卡片**，drafts 不动）
- v3 KB 卡片总览索引：`loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md`（含全部 171 张卡的 id + title + source_id + v2_anchor）
- v2 KB 卡片索引：`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md`
- 合同：`loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`（先读以理解 unified footnote 模型）
- 今天日期：2026-05-28

## 语言要求

- 卡片 body / footnote 叙述以**中文**为主语言。原文引用保留源语言。
- frontmatter schema 字段名英文。

## 写入边界

- **只**修改你 cluster 内 cards 的 body（YAML frontmatter 后面的全部内容）。
- frontmatter 的 `related:` 字段**不要手动改**——稍后会用脚本从 footnotes 重新生成。其它 frontmatter 字段（id、title、source_ids、provenance_card、aliases、created_time 等）也不要改；只更新 `edited_time`。
- 不要触动 drafts/、provenance/、similarity/、comparison/、queues/、state、tools、brains、v2 等任何其它文件。

## 读取边界

允许读：
- 你 cluster 的 kb cards；
- 任何 v3 KB cards（构造 cross-card footnote 时需要查目标卡 id）；
- v3/v2 kb indexes；
- `CARD_CONTRACT_V3.md`。

不要读：v3 drafts、v3 provenance（adoption 已经发生，drafts 是历史记录）、v2 卡 body（除非要确认 8 张 v2-anchored 卡的 anchor 是否仍准确）、source_materials、queues / state / brains。

## Footnote target 域与格式

按合同四种 target：

```markdown
## Footnotes

[^src1]: `data/raw/webpage/karpathy-x-launch-post/text.txt` — JSON 指针 `$.tweet.text` — "原文引用片段"
[^v3-1]: [karpathy-gist-three-layers](karpathy-gist-three-layers.md) — 本卡的三层骨架来自这里
[^v2-1]: v2 anchor [llm-wiki-three-layer-architecture](../../../../../v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md) — 本卡是该卡的 delta
[^url1]: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
```

`[^id]` 命名建议（不强制，但同 cluster 内尽量一致）：
- `src1`、`src2` … 用于 raw source
- `v3-1`、`v3-2` … 用于 v3 KB 卡
- `v2-1` 用于 v2 KB 卡（多数卡片只有 0-1 个 v2 anchor）
- `url1` 用于 external URL

每个 `[^id]` marker 在 body 必须出现一次以上，footnote section 里必须有且仅有一条 `[^id]: ...` 展开。

## 5 步处理流程（每张卡）

### Step 1: 读卡片

读卡片 frontmatter + body 完整内容。识别：
- 现有 `## References` 章节里的每条（通常是 raw source narrative）
- 现有 `## Footnotes` 章节里的每条（通常是 inline locator）
- body 正文里是否提到其它 v3 卡的概念（如 "LoCoMo"、"Mem0"、"Karpathy 三层架构"、"PoisonedRAG" 等）

### Step 2: 把 References 合并进 Footnotes

- 每条 References entry 变成一条 `[^src1]`（或 `[^src2]` ...）footnote。
- 在 body 里找一个最相关的句子，挂上 `[^srcN]` marker（如果 References 描述的就是这张卡的总起源，挂在第一段第一处提到该 idea 的位置）。
- 现有 `## Footnotes` 条目保留，重新编号或保持原编号都可——重要的是 body marker 和 expansion 一一对应。
- 删除 `## References` 章节。

### Step 3: 加 KB-internal cross-card footnotes

扫描 body，找到自然提到其它 v3 KB 卡概念的位置，挂 `[^v3-N]` marker。例如：

- `mem0-locomo-benchmark-evaluation` 卡的 body 里如果出现 "在 LoCoMo 上评估..." → 挂 `[^v3-X]`，footnote 指向 `locomo-very-long-term-dialogue-dataset.md`
- `etamp-` 系列卡的 body 里如果出现 "类似 PoisonedRAG..." → 挂 footnote 指向相应 poisonedrag-* 卡
- `enterprise-llm-wiki-drift-detection-loop` body 里如果出现 "类似 Karpathy 的 health check..." → 指向 `llm-wiki-karpathy-lint-grounding-trail.md`

**保守原则**：只在概念真的被实质性提到时加 footnote，不要为了凑数硬加。如果 body 没自然提到某张卡，不要往里硬塞。

### Step 4: 处理 v2 anchor（仅 8 张 provenance_delta 卡）

如果你的 cluster 包含以下任意一张 v2-anchored 卡，body 里必须有一处 `[^v2-1]` footnote 指向 v2 anchor。anchor 关系来自 kb provenance 的 `v2_anchor:` 字段（不需要你读 kb provenance，直接用下表）：

| v3 卡 id | v2 anchor id |
|---|---|
| `agents-md-as-schema-layer` | `llm-wiki-schema-configuration-document` |
| `anthemcreation-llm-wiki-three-layer-architecture` | `llm-wiki-three-layer-architecture` |
| `enterprise-llm-wiki-drift-detection-loop` | `llm-wiki-health-checks` |
| `idea-file-as-agent-era-artifact` | `idea-file-abstract-vague` |
| `karpathy-gist-three-layers` | `llm-wiki-three-layer-architecture` |
| `karpathy-llm-kb-three-layer-arch` | `llm-wiki-three-layer-architecture` |
| `karpathy-llm-wiki-three-layers` | `llm-wiki-three-layer-architecture` |
| `robin-cartier-schema-as-product-doc` | `llm-wiki-schema-configuration-document` |

v2 footnote 形式：

```markdown
[^v2-1]: v2 anchor [<v2-id>](../../../../../v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/<v2-id>.md) — 本卡是该卡的 delta：<一句话说明 delta 是什么>
```

注意路径：从 `loops/v3.../outputs/llm_wiki/kb/cards/<v3-id>.md` 到 v2 同位置，**5 个 `..`**。

### Step 5: 更新 frontmatter

- `edited_time` 改为今天日期（`2026-05-28T<时间>+08:00`）
- 其余 frontmatter 字段（含 `related:`）**不要动**——`related:` 会被脚本从 footnotes 自动重新生成。

## 数量与质量原则

- KB-internal footnote 数量按"自然出现"为准——可能 0 个、1 个、5 个，都正常。
- 不要在 body 里硬加"本卡相关：A、B、C"这种总结性话——related 走 frontmatter 由脚本生成。
- body 文笔尽量保留原状——只在自然位置插入 `[^id]` marker，不要为了挂 footnote 改写句子。
- 不要新增 `## Backlinks` 章节、不要写"被引用：..."——backlinks 由 Obsidian / 索引工具自动算。

## 不能做的事

- 不要改 `related:` frontmatter（脚本会做）
- 不要改 `source_ids:` frontmatter（除非合同要求且你确定）
- 不要改其它 frontmatter 字段（id / title / source_ids / aliases / provenance_card / status / card_type / tags / created_time / edited_entity）
- 不要碰 drafts / provenance / similarity / comparison
- 不要新增 body 章节（除非是合并 References 后修改 Footnotes 内容；不能新增其它 section heading）
- 不要写 git 命令

## Hook 行为

- 已配置 hook：写 kb/cards/<id>.md 时自动 `git add` + commit 卡片 + 同名 kb provenance（如果一并改了 provenance）。commit message 形如 `v3 adopt: <id>`。
- 本次只改 kb/cards/，hook 会自动 commit 每张卡。无需自己跑 git。

## 最终报告

```
citation_migration cluster <NAME> 报告：
- 处理卡片数：<n>
- References 合并：<n>（每张卡 References 条目数总和）
- 新增 KB-internal footnote：<n>（v3 + v2 cross-card 总和）
- v2 anchor footnote：<n>（应等于本 cluster 包含的 v2-anchored 卡数量）
- 异常：<...>
WORKER_DONE
```

最后一行必须正好是 `WORKER_DONE`。
