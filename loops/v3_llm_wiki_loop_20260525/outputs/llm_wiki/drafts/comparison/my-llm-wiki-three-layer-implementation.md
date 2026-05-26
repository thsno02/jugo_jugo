---
schema: comparison_provenance.v3
draft_card: ../cards/my-llm-wiki-three-layer-implementation.md
draft_provenance: ../provenance/my-llm-wiki-three-layer-implementation.md
similarity_result: ../similarity/my-llm-wiki-three-layer-implementation.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.3077
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1333
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.1333
decision: new_card
audit_required: false
created_time: 2026-05-26T12:18:00+08:00
edited_time: 2026-05-26T12:18:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- **top 1 `llm-wiki-three-layer-architecture` (0.308)**：共享 `llm / wiki / 三层 / 架构`。draft 明确说 `my-llm-wiki` 这个 PyPI 包"复现了 Karpathy 描述的三层结构"——这正是 v2 top1 statement 所讲的同一三层。所以是真主题相关。
- **top 2 `llm-wiki-health-checks` (0.133)**：仅共享 `llm / wiki`。draft 完全没提 health checks 或 Linting；token 共享只来自高频词。低分误中。
- **top 3 `llm-wiki-listed-use-cases` (0.133)**：仅共享 `llm / wiki`。draft 没列举使用场景；只是 `my-llm-wiki` 自身在做"通用文件夹 → 知识图"。低分误中。

## 2. draft 与候选在哪里不同

- **卡片类型完全不同**：v2 top1 是 known_fact（Karpathy 把架构分为三层）；draft 是 example_pattern（一个 PyPI 工具 `my-llm-wiki` v0.9.0 如何把这个三层落到 Obsidian vault）。
- **scope 完全不同**：v2 top1 只声明三层这件事；draft 描述具体工具的：
  - 命令 `pip install my-llm-wiki` / `llm-wiki .` / `llm-wiki note "<insight>"`；
  - SHA256 缓存增量编译机制；
  - "compile once, query forever"（这是 PyPI 页面引述 Karpathy 的原话，逐字引用）；
  - 输出目录 `wiki-out/vault/`；
  - 文件类型覆盖（代码 19 语言、PDF / DOCX via Docling、HEIC/PNG/JPG via vision OCR）；
  - 包元数据（作者 phuc-nt、MIT、Python ≥3.10、Apr 28 2026）。
- **来源不同且不交叉**：v2 top1 来自 Karpathy gist；draft 来自 PyPI 页面 `data/raw/pypi/pypi-my-llm-wiki/text.txt`，两份证据完全独立。
- draft 与 v2 top1 不是"同一卡的两个版本"，是"概念 vs 该概念的具体工程实例"的关系。

## 3. 下一步的核心依据

- (1)(2) 表明：token 共享高分来自 `三层 / 架构` 这两个通用 token，但 draft 是产品实例卡，v2 top1 是概念事实卡，scope 与卡片类型都不重叠。
- 选 `new_card`：
  - draft 不为 v2 top1 的"作者把架构分为三层"这一事实提供新证据 / 新边界 / 新数值——它陈述的是某 PyPI 包的实现细节；
  - v2 top1 的 statement 不需要因 draft 改写或回链，其 scope 已声明"仅限该来源提出的架构分层"，不应纳入第三方实现细节。
- 不选 `provenance_delta`：draft 内容主要是工具本身的实现信息，不是对 v2 概念的证据补强。
- 不选 `merge_candidate`：实例卡与概念卡合并会破坏 v2 top1 的事实卡紧致性。
- 不选 `revise_before_gate`：draft 引用、版本号、边界（Image / HEIC 抽取需 Claude Code agent mode；Docling 等是 extras）都已显式标注。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议 draft `related` 追加 `llm-wiki-three-layer-architecture`，方便从 v2 概念卡导航到该实现实例。

## 5. 备注

- draft 与 batch 中其他 Karpathy 三层架构实现卡（如 `karpathy-llm-wiki-obsidian-plugin-overview`）共同构成"实现示例集"，可以在 publication_gate 阶段考虑做一张综合索引卡。
- draft 引述的 "compile once, query forever" 是 PyPI 页面对 Karpathy 的二次概括（不是 Karpathy 原话），draft 已正确地标为"PyPI 页面引述"，未误用为 Karpathy 直接引语。
