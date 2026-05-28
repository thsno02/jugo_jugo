---
id: anthemcreation-llm-wiki-three-layer-architecture
title: Karpathy 的 LLM wiki 是三层结构：原始源 / LLM 编译产物 / agents.md
status: accepted
card_type: concept
tags: [#llm-wiki, #karpathy, #agents-md, #obsidian]
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-28T10:05:00+08:00
edited_entity: llm
source_ids: [anthemcreation-fr-guide]
provenance_card: ../provenance/anthemcreation-llm-wiki-three-layer-architecture.md
aliases: [LLM wiki Karpathy, sources brutes / wiki / agents.md, three-layer LLM wiki]
related: [karpathy-gist-three-layers, karpathy-llm-wiki-three-layers, karpathy-llm-kb-three-layer-arch, anthemcreation-llm-wiki-setup-cost-envelope, anthemcreation-llm-wiki-vs-rag-multi-hop, my-llm-wiki-three-layer-implementation, agents-md-as-schema-layer]
---

Karpathy 2026 年 4 月发布的 LLM wiki 蓝图（GitHub Gist）[^v3-1]被这家法国机构（Anthem Création）总结成一段紧凑的工程描述[^v2-1]：整个系统由三层构成，三层之间的"写"与"读"权限被严格分离。把这三层记牢，可以避免大多数 LLM wiki 初学者把"原始 PDF 也丢进 wiki 文件夹"或"让用户和 LLM 同时写一个文件"这两类常见错误。

三层（原文 enumerate）：

1. **Sources brutes immuables**（不可变原始源）—— 论文、PDF、抓取下来的网页等；**永不修改**，存放在独立子目录（教程里建议 `/sources/`）。
2. **Wiki gérée par LLM**（LLM 管理的 wiki）—— 一组互相链接的 markdown 文件，由 LLM 自动创建和更新；包含实体页（entity pages）、主题摘要（résumés de sujets）、跨源对比（comparaisons）与综述（synthèses）。
3. **Fichier d'instructions**（指令文件）—— 典型文件名为 `agents.md`[^v3-2]，定义"如何命名页面、何时新建实体 vs 更新已有页面、如何形式化矛盾"等规则——它是把 wiki 长期保持一致的主要杠杆。

权限边界：原文一句话写得很硬——「Les sources brutes restent immuables. Le LLM écrit dans la wiki, l'utilisateur lit la wiki. La séparation des rôles est stricte.」[^src1] 即：

- 原始源：人/抓取脚本写入，LLM 只读；
- Wiki：LLM 写入，人只读；
- agents.md：人写入，LLM 读并执行。

这种"写者唯一"的设计直接借用了 Karpathy 提出的编译类比[^v3-3]——原始源是 *源代码*，wiki 是 *编译产物*：「les sources brutes sont comme du code source, et la wiki LLM est l'exécutable compilé. Vous ne re-compilez pas à chaque fois que vous lancez un programme.」[^src2] 你不会每次运行就重新编译一遍，所以也不该在每次查询时重抓原文。

Ingestion 时 LLM 在第二层做的具体动作（原文列举）：

- 为不存在的概念**新建实体页**（举例：为 Phi-2 建一页，记下 2.7B 参数、1.4T token 训练）；
- **更新**已有页面；
- 在源之间**标注并合成矛盾**（contradictions entre sources）；
- 自动建立**双向 backlinks**。

读侧：查询直接打到 wiki，而不是回到原始源。这是这套系统能做 **multi-hop 推理** 的物理基础[^v3-4]——知识已经被预先合成、链接、消歧。

操作含义：

- `agents.md` 不是可选 README，是规约文件；它的质量直接决定 wiki 长期一致性，文中明示「La qualité de votre agents.md détermine directement la fiabilité de la base.」[^src3]
- 原始源和 wiki 必须在文件层物理分离，否则 LLM 重写 wiki 时可能误改原文；
- 编辑器选用 Obsidian / VS Code + Markdown Preview / Logseq 都行，关键约束是文件保持**flat markdown**，便于 LLM 读写。

## Footnotes

[^src1]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` 第 104 行 — "Les sources brutes restent immuables. Le LLM écrit dans la wiki, l'utilisateur lit la wiki. La séparation des rôles est stricte."
[^src2]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` 第 76 行（编译类比）— "Il décrit l'analogie suivante : les sources brutes sont comme du code source, et la wiki LLM est l'exécutable compilé. Vous ne re-compilez pas à chaque fois que vous lancez un programme. La wiki reste canonique, vivante, et s'améliore à chaque nouvelle source ingérée."
[^src3]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` 第 162 行 — "La qualité de votre agents.md détermine directement la fiabilité de la base."
[^v3-1]: [karpathy-gist-three-layers](karpathy-gist-three-layers.md) — Anthem Création 的总结直接来自 Karpathy gist 三层蓝图。
[^v3-2]: [agents-md-as-schema-layer](agents-md-as-schema-layer.md) — `agents.md` 作为 schema 层的角色在此卡有更细节的展开。
[^v3-3]: [karpathy-llm-wiki-source-executable-analogy](karpathy-llm-wiki-source-executable-analogy.md) — 编译类比来自 Karpathy 自己的同一段表述。
[^v3-4]: [anthemcreation-llm-wiki-vs-rag-multi-hop](anthemcreation-llm-wiki-vs-rag-multi-hop.md) — multi-hop 推理优势在此卡作为独立 distinction 展开。
[^v2-1]: v2 anchor [llm-wiki-three-layer-architecture](../../../../../v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md) — 本卡是该卡的 delta：从 Anthem Création 法语视角再次确认三层结构，并补全"写者唯一"权限边界与 ingestion 实操列表。
