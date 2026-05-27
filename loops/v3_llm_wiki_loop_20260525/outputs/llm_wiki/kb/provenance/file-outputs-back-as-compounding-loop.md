---
schema: accepted_card_provenance.v3
card: ../cards/file-outputs-back-as-compounding-loop.md
material_id: karpathy-x-launch-post
digest_id: digest_karpathy-x-launch-post
source_paths:
  - data/raw/webpage/karpathy-x-launch-post/text.txt
draft_card: ../../drafts/cards/file-outputs-back-as-compounding-loop.md
draft_provenance: ../../drafts/provenance/file-outputs-back-as-compounding-loop.md
similarity_result: ../../drafts/similarity/file-outputs-back-as-compounding-loop.json
comparison_provenance: ../../drafts/comparison/file-outputs-back-as-compounding-loop.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:04:00+08:00
  gate_notes: 6/6 通过；Output 段 + Linting 段 verbatim + 三步落地 + 复利效果论断齐全；与 v2 `llm-wiki-persistent-compounding-artifact` 互为性质卡/操作规则分轴关系。
created_time: 2026-05-25T22:05:00+08:00
edited_time: 2026-05-27T15:04:00+08:00
edited_entity: llm
---

## 源证据

- 主要片段：`data/raw/webpage/karpathy-x-launch-post/text.txt`，JSON 指针 `$.tweet.quote.text`，"Output:" 章节：
  - "Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian."
  - "Often, I end up \"filing\" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always \"add up\" in the knowledge base."
- 边界片段：`$.tweet.quote.text`，"Linting:" 章节——health check 会发现数据不一致并补全缺失字段。用来支撑卡片中关于"没有 linting 兜底时回写会放大错误答案"的边界警告。

## 卡片范围是否成立

卡片提取了一条行为规则（把每次查询输出归档回 wiki）和作者本人主张的结构性后果（"my own explorations and queries always 'add up' in the knowledge base"）。两者都直接来自 Output 段。

卡片正文给出的三个操作步骤（把答案当候选文章；放进概念目录；允许后续查询将其作为一等公民检索）是对源材料较高抽象描述的具体落地。它们没有引入源材料未提及的机制（例如自动反向链接生成）；卡片中提到 LLM 在 ingest 和 lint 阶段补反向链接，这部分依据来自 "Data ingest:" 和 "Linting:" 章节。

边界（"没有 linting，回写会放大错误答案"）是源材料自身的逻辑后果：源材料把回写（Output 段）和健康检查（Linting 段）显式地绑定在一起；缺了健康检查，工作流就失去源材料设计的属性。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:04:00+08:00
- 检查要点：
  - 不是标题复述：行为规则 + 复利效果论断 + 三步落地 + 边界警告。
  - 知识密度足够：规则 + 机制 + 反例（无 linting 兜底）+ 落地步骤。
  - 源支撑齐全：Karpathy 原文 verbatim + JSON 指针定位。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，operational_rule 类型与正文一致。
  - related 已链 v3 draft 卡（五阶段 / idea-file / compounding 三机制 / karpathy 三操作）。

## 备注

- 标题 token 与 v2 中的 "Query 操作回写好答案" 预期会高度重合；comparison 已论证 new_card 决策（性质卡 vs 操作规则卡分轴）。
- 与 v2 `llm-wiki-persistent-compounding-artifact` 是同源段不同论点轴的关系——建议未来 audit 阶段加 cross-link。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/file-outputs-back-as-compounding-loop.md`
- draft provenance: `../../drafts/provenance/file-outputs-back-as-compounding-loop.md`
- similarity: `../../drafts/similarity/file-outputs-back-as-compounding-loop.json`
- comparison provenance: `../../drafts/comparison/file-outputs-back-as-compounding-loop.md`
