---
id: causality-ordered-repair
title: 因果序批量修复
status: accepted
card_type: mechanism
tags: [llm-wiki, maintenance, repair, dependency-ordering, batch-processing]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
justification: ../justification/causality-ordered-repair.md
canonical_concept: causality-ordered-repair
aliases: [因果序修复, Smart Fix All, 依赖感知修复, causality-ordered fix, 批量修复顺序]
summary: >-
  causality-ordered-repair（因果序修复 / Smart Fix All / 依赖感知修复）
  是 LLM Wiki 插件的批量修复执行策略：按因果依赖排序六步修复
  （污染页 -> 别名 -> 去重 -> 死链 -> 孤立页 -> 空页），后续步骤依赖前序步骤的输出，
  一键执行避免人工判断修复顺序
related: [alias-cross-language-dedup, contradiction-state-machine, lint-operation]
---

Karpathy LLM Wiki 插件的 **Smart Fix All** 功能实现了一种**因果序（causality-ordered）批量修复**策略，将六类修复操作按严格的依赖顺序串联执行[^src-1]：

1. **Fix polluted pages** -- 修复文件名中包含路径前缀的污染页（如 `concepts/concepts布局优化.md`）
2. **Complete aliases** -- 为缺失别名的页面批量生成翻译、缩写和替代名称
3. **Merge duplicates** -- 基于别名匹配合并重复页面
4. **Fix dead links** -- 修复指向不存在页面的死链
5. **Link orphans** -- 为没有入站链接的孤立页面建立连接
6. **Expand empty pages** -- 填充内容为空的页面

**因果依赖关系**是该设计的核心洞察：去重（第 3 步）依赖别名（第 2 步）的输出——没有完整别名就无法发现跨语言重复[^src-2]；死链修复（第 4 步）必须在去重（第 3 步）之后进行——合并操作会改变页面路径，可能产生新的死链也可能解决旧死链；孤立页链接（第 5 步）需要在死链修复后的稳定链接图上执行[^src-3]。

这是**修复操作不可交换**的工程认知——如果先修复死链再合并重复页，合并操作可能重新引入死链，导致修复失效。将这种依赖知识编码进执行顺序，用户无需理解修复间的因果关系即可安全执行全量修复。

该策略是巡检操作[^card-1]的执行侧补充——巡检负责检测问题，Smart Fix All 负责按正确顺序解决问题。别名系统[^card-2]作为去重的前置依赖在此顺序中得到体现。

## Footnotes

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L214-215 -- "Smart Fix All — Runs fixes in causality order (v1.9.0+): Fix polluted pages → Complete aliases → Merge duplicates → Fix dead links → Link orphans → Expand empty pages"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L65-66 -- "Missing aliases: Pages without aliases (all pre-v1.7.11 pages). Click 'Complete Aliases' — the LLM generates translations, acronyms, and alternate names in bulk. This is critical for duplicate detection."
[^src-3]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L89-90 -- "Smart Fix All — Causality-ordered batch fix: duplicates merged → dead links resolved → orphans linked → empty pages expanded"
[^card-1]: [巡检操作](lint-operation.md) -- 本卡描述修复操作的因果序执行策略，该卡描述检测阶段发现哪些问题需要修复
[^card-2]: [别名系统与跨语言去重](alias-cross-language-dedup.md) -- 本卡将别名完成作为去重的前置步骤纳入因果序，该卡详述别名系统与两层语义去重的机制本身
