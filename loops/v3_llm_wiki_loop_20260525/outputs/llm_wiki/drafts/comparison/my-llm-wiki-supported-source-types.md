---
schema: comparison_provenance.v3
draft_card: ../cards/my-llm-wiki-supported-source-types.md
draft_provenance: ../provenance/my-llm-wiki-supported-source-types.md
similarity_result: ../similarity/my-llm-wiki-supported-source-types.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1667
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1176
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.1176
decision: new_card
audit_required: false
created_time: 2026-05-26T12:20:00+08:00
edited_time: 2026-05-26T12:20:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top1 `schema-configuration-document` jaccard 0.1667，共享 `llm`/`wiki`/`文档`——`文档` 来自 draft 标题"办公文档"，与 v2 标题"配置文档"撞词，但语义截然不同。top2/top3 只共享 `llm`/`wiki`。draft 的核心术语 `Tree-sitter`、`Docling`、`OCR`、`代码`、`图像`、`视觉` 在三张候选中都没出现。属典型功能词撞分。

## 2. draft 与候选在哪里不同

- **来源不同**：本 draft 取自 `pypi-my-llm-wiki`（一个具体的 0.9.0 PyPI 包）；v2 三张候选全部出自 karpathy gist / x post 家族。
- **抽象层不同**：
  - top1 `schema-configuration-document` 谈 karpathy 抽象 schema 层角色（配置文档约束 LLM 行为）；本 draft 是某 PyPI 包对"哪些文件类型可被 ingest"的具体实现声明（19 语言代码走 Tree-sitter AST、Docling 处理 office、vision OCR via Claude Code agent mode）。两者完全不在同一抽象层。
  - top2 `health-checks`、top3 `listed-use-cases` 与文件类型 ingest 无直接关联。
- 本 draft 的关键 fact——"代码不是字符串切片而是 AST 提取（class/function/extends/implements/call graph）"、"图像 OCR 走 Claude Code agent mode 而非自带"、"Docling 是默认 office 引擎"——在 v2 KB 没有任何卡覆盖。
- draft 类型 `source_claim`，从 PyPI 页面 108-115 行逐条复述，边界严格（不外推到非 my-llm-wiki 实现）。

## 3. 下一步的核心依据

(1) 三张候选都不覆盖 my-llm-wiki 的 ingest 管道实现；(2) draft 来源（pypi-my-llm-wiki）在 v2 KB 完全缺席；(3) source_claim 类卡天然以 source 为分卡单位，draft 描述的是 v2 没有的来源。结论是 `new_card`。

不是 `provenance_delta`：本 draft 不是给 v2 schema-configuration-document 补一段证据——它是另一个工具（my-llm-wiki）的实现声明，与 v2 karpathy 抽象 schema 层无直接对应。不是 `merge_candidate`：v2 没有任何 my-llm-wiki 工具卡或 ingest 管道卡可合并。不是 `revise_before_gate`：每条管道都引到 PyPI 页面行号、optional extras 也有行号支撑。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 sources 索引加入 `pypi-my-llm-wiki`；与同源兄弟卡 `my-llm-wiki-three-layer-implementation`（如已存在）建立 related 互链作"架构 → 源类型"链路。

## 5. 备注

- "图像 OCR 必须依赖 Claude Code"是该工具的硬依赖警告，未来下游引用本卡时应同步保留这条边界。
- Tree-sitter 19 语言清单与 Docling 默认引擎选择反映 2026-04 Python 生态状态；如未来某 release 取消该依赖，应触发 v3 audit 而非本卡 revise。
