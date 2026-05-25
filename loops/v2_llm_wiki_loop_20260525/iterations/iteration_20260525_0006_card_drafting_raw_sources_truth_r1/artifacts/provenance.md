# 出处论证：Raw sources 是只读事实来源

## 事实从哪里来

本卡事实来自任务指定候选 `候选 8`，并以 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:27-30` 作为唯一来源证据。`fact_candidates.md` 只用于核对候选字段，没有引入其它候选内容。

## 来源为什么能支撑它

指定来源行直接定义 `Raw sources` 层，并把它放在“三层”架构说明下。该段把 `Raw sources` 说成用户策展的来源文档集合，并列举文章、论文、图片和数据文件作为例子；同一段还说明这些来源不可变，LLM 读取它们但不修改它们，并把它们称为 `source of truth`。

## 来源明说的部分

来源明说了四点：`Raw sources` 是用户策展的来源文档集合；集合中可以包含文章、论文、图片和数据文件；这些材料是不可变的；LLM 从中读取但不修改它们。来源还明说这是 `source of truth`。

## 整理后的表述

草稿卡中的“事实来源”是对 `source of truth` 的中文整理；“在该来源的架构中”是根据来源先说 “There are three layers” 后定义 `Raw sources` 而作出的范围化表述。卡片没有把该说法扩展为通用 LLM wiki 规范。

## 成立范围

该事实只在该来源对 `Raw sources` 层的规定内成立。它不说明其它系统、其它 LLM wiki 实现或更广泛知识管理方法中的 `Raw sources` 必须如此设计。

## 当前为什么只能是 draft

本轮任务是 drafting worker，只能生成草稿而不能采纳知识卡。并且当前论证只使用任务指定的一段来源证据，足以支撑草稿事实，但未经过主控 agent 的采纳流程，因此状态保持为 `draft`。
