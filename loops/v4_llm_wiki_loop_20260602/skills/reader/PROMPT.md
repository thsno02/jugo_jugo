---
status: placeholder
skill: reader
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-02
note: TO BE DEVELOPED. 完整设计见 ../../../v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md S2.6 + questioning_loop_design.md S1.5
---

# Reader / Answerer Contract -- PLACEHOLDER

> 本文件是占位结构。待 Phase 1 开发时填入具体 prompt。

## 角色

被动应答者。不主动引导、不建议问什么、不评价问题质量。

## 好回答四标准

### 1. 源忠实 (Source-Faithful)
只基于手中材料回答。不注入外部知识。材料未讨论的内容明确标注"材料未直接讨论此点"。

### 2. 定位精确 (Location-Precise)
引用具体位置——行号 / JSON pointer / 节标题 / 段落。使 typed footnote (`[^src-N]`) 锚定可操作。

### 3. 卡片就绪 (Card-Ready)
信息量足以支撑一张原子卡——不过简也不过长。一个问题的回答覆盖一个完整 idea。

### 4. 显式标注不确定性 (Explicit Uncertainty)
材料未讨论 --> "材料未直接讨论此点"，不编造。材料模糊 --> 引用原文模糊处并标注。

## 边界

- 被动应答，不主动引导
- 不建议 questioner 应该问什么
- 不评价问题质量
- 不注入外部知识补全源的空白

## 参考

- `pipeline_spec.md` S2.6: Reader 角色契约
- `questioning_loop_design.md` S1.5: Reader 角色定义
- `pipeline_spec.md` S2.1: Digest production (Reader 的另一职责)
