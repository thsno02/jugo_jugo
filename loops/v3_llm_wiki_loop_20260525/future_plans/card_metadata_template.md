---
status: future_plan
stage: reference_template
created: 2026-06-02
loop_id: v3_llm_wiki_loop_20260525
topic: card_metadata_template
note: 卡片完整格式参考模板。展示所有字段、规则、body 结构和 typed footnote 用法。
---

# Card Metadata Template（参考模板）

> 本文件是**参考/示例**，展示一张完整卡片的格式和每个字段的规则。实际卡片不需要注释。

---

## 完整卡片示例

```markdown
---
# ── 身份 ──
id: example-concept-slug                    # stable ASCII slug, kebab-case
                                            # 规则: 一旦创建不改；全 loop 唯一
title: 示例概念的中文短标题                     # 中文；简短的概念名，不是完整句子
                                            # 规则: 不是 claim 伪装成标题

# ── 状态 ──
status: accepted                            # draft | accepted | superseded
                                            # draft: extract 刚产出
                                            # accepted: ingest 后进入 active view
                                            # superseded: governance 判定合并，移入 archive
                                            # 注意: 不存在 tentative/stable 区分

# ── 分类（自由描述，非 taxonomy）──
card_type: mechanism                        # 自由描述词，agent 自选
                                            # 常见值: concept / mechanism / distinction /
                                            #   operational_rule / source_claim / example_pattern
                                            # 规则: 不是受控分类网格；不设互斥 taxonomy
tags: [llm, decoding, agent]                # 自由 hashtag，可选
                                            # 规则: 不是受控词表；结构靠 link 涌现

# ── 时间 ──
created_time: 2026-06-02T14:30:00+08:00     # 首次创建时间，ISO8601+08:00
edited_time: 2026-06-02T14:30:00+08:00      # 最近实质性编辑时间
edited_entity: llm                          # llm | human | llm+human

# ── 来源 ──
source_ids: [karpathy-gist-llm-wiki]        # 本卡使用的 material id 列表
                                            # 可从 [^src-N] footnotes 自动派生
                                            # 卡级别的来源标记

# ── justification journal ──
justification: ../justification/example-concept-slug.md
                                            # 指向 per-card 的 justification journal
                                            # append-only 日志，记录卡的完整生命周期
                                            # 替代原来的一次性 provenance

# ── grep-friendly metadata（核心召回锚点）──
canonical_concept: example-concept           # grep 锚点，kebab-case 英文
                                            # 规则: 每卡一个归一化概念 id
                                            # 建卡时先 grep 现有 KB 的 canonical_concept：
                                            #   命中 -> 复用；无 -> 新铸
                                            # 让概念集自收敛，KB 本身是 tag registry
aliases: [示例概念, example concept, EC]     # 该概念的真实表层变体
                                            # 含中英文、缩写、符号形式
                                            # 规则: 列实际会被搜的表层串，不臆造
summary: >-                                 # 一行稠密 grep 靶子
  example-concept 是一种用于 X 场景的 Y 机制，
  通过 Z 方法实现 W 效果（示例概念/EC）
                                            # 规则: 刻意包含 canonical + 关键 aliases + 核心论断
                                            # 定位: 不是给人看的摘要，是为 grep 优化的稠密一行
                                            # 与 title 区分: title=概念名, summary=claim+召回信号

# ── 关系（自动派生）──
related: [sibling-card-id, another-card-id] # AUTO-DERIVED，脚本从 [^card-N] + [^dist-N] 派生
                                            # 规则: 不手动维护；改 body footnotes 后重跑脚本
                                            # 只含同 loop KB 卡 id

# ── governance fields（仅在适用时出现，默认模板不含）──
# superseded_by: hub-card-id               # 仅 governance 添加
                                            # 仅在 status=superseded 时存在
                                            # 指向合并后的 hub 卡
---

正文从这里开始。这是知识陈述体——自足、密集、有据。

正文应该让读者理解：这个概念/机制/区分是什么、怎么运作、边界在哪、
有什么源证据支撑。不要复述标题，不要注入源之外的通用背景[^src-1]。

具体来说，example-concept 的核心机制是通过 Z 方法处理输入数据，
与 sibling-concept 共享基础定义但聚焦不同方面[^card-1]。
值得注意的是，本概念与 related-concept 的区分在于作用范围：
本卡聚焦微观层面的机制，而 related-concept 聚焦宏观层面的策略[^dist-1]。

更多技术细节可参考原始实现文档[^url-1]。

## Footnotes

[^src-1]: `data/raw/paper/example-paper/text.txt` -- 行 42-50 -- "原文引用片段，支撑上文 claim"
[^src-2]: `data/raw/webpage/example-blog/text.txt` -- S3.2 -- "另一段源引用"
[^card-1]: [sibling-concept](sibling-concept.md) -- 本卡与该卡共享 X 概念的基础定义
[^dist-1]: [related-concept](related-concept.md) -- 本卡聚焦微观机制，该卡聚焦宏观策略
[^url-1]: <https://example.com/implementation-docs> -- 原始实现文档
```

---

## 字段规则速查

### 自动 vs 手动

| 字段 | 谁维护 | 何时 |
|---|---|---|
| `id` | extract reframing 创建 | 创建时，不改 |
| `title` | extract reframing 创建 | 可 governance 时微调 |
| `status` | 脚本 (ingest/governance) | ingest: draft->accepted; governance: accepted->superseded |
| `card_type` / `tags` | extract agent 自选 | 自由描述，不受控 |
| `created_time` | extract reframing | 创建时，不改 |
| `edited_time` | 任何实质编辑时更新 | governance/evolution 时 |
| `source_ids` | extract reframing / 脚本可从 `[^src-N]` 派生 | 创建时 |
| `justification` | extract reframing 创建路径 | 创建时，不改 |
| `canonical_concept` | extract reframing（grep 复用/新铸） | 创建时；governance 可归一化 |
| `aliases` | extract reframing | 创建时；governance 可补充 |
| `summary` | extract reframing | 创建时；governance 可微调 |
| `related` | **脚本自动派生** | body footnotes 变化后重跑 `derive_metadata_from_footnotes.py` |
| `superseded_by` | **governance 添加** | 仅在 merge 时，不在默认模板中 |

### Typed Footnote 类型速查

| marker | target | 谁产出 | 进入 `related:`? |
|---|---|---|---|
| `[^src-N]` | raw material 位置+引用 | extract reframing | NO（进 `source_ids:`） |
| `[^card-N]` | 同 loop KB 卡 | extract fusion / governance | YES |
| `[^dist-N]` | 同 loop KB 卡（区分标注） | governance link-as-distinction | YES |
| `[^url-N]` | 外部 URL | extract / governance | NO |

### 不在默认模板中的字段

以下字段仅在特定条件下由 governance 添加，**不出现在 extract 产出的卡中**：

- `superseded_by: <id>` -- 仅 status=superseded 时
- ~~`card_class`~~ -- Mode B deferred，当前不使用
- ~~`derived_from`~~ -- Mode B deferred，当前不使用
