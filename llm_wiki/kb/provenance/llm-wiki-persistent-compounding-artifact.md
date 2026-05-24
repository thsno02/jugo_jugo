# 出处论证：持久复合 wiki

- card: `llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md`
- status: accepted

## 事实来源

这张卡来自 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:13`，并用 `fact_candidates.md` 中的候选 4 字段核对事实边界。

## 支撑关系

来源第 13 行直接把 wiki 称为持久且会复合增长的产物，并继续说明三类已经保留下来的内容：交叉引用、已标记矛盾、综合结果。该行还说明 wiki 会随着新增来源和新增问题继续变丰富，因此能够支撑“持续变丰富的持久复合产物”这一表述。

## 来源明说部分

来源明说：

- wiki 是持久、复合增长的产物。
- 交叉引用已经存在。
- 矛盾已经被标记。
- 综合内容已经反映已读材料。
- wiki 会随新增来源和提问继续变丰富。

## 整理表述部分

卡片中的“保留既有交叉引用、已标记矛盾和综合内容”是对来源中“already there / already been flagged / already reflects”三组表达的中文整理。卡片中的“持续复合增长”是对来源中“persistent, compounding artifact”和“keeps getting richer”的合并表述。

## 成立范围

该事实只在该来源对 LLM Wiki 产物性质的描述范围内成立。它不主张所有 wiki、所有 RAG 替代方案或所有 LLM 知识库都具有同样性质。

## 采纳说明

该卡已通过审计，审计结论为 `audit_result: pass`。采纳时只将卡片状态从 `draft` 改为 `accepted`，并保留单一来源范围限定。
