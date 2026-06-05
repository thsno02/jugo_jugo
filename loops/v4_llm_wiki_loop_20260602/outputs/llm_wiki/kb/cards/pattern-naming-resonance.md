---
id: pattern-naming-resonance
title: 模式命名的共振效应
status: accepted
card_type: source_claim
tags: [llm-wiki, pattern-naming, community-reception, scattered-practices]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
justification: ../justification/pattern-naming-resonance.md
canonical_concept: pattern-naming-resonance
aliases: [模式命名共振, 命名结晶效应, pattern naming effect]
summary: >-
  pattern-naming-resonance（模式命名共振 / 命名结晶效应）指 Karpathy 的 LLM Knowledge Base
  帖子引发强烈共鸣的原因：许多人已在用 CLAUDE.md、Agent 规则文件、Obsidian 等做类似实践，
  该帖子为这些散发性尝试赋予了名称和结构，产生了「原来我做的就是这个」的认知结晶
related: [llm-wiki-pattern, intentional-abstraction]
---

Karpathy 的「LLM Knowledge Bases」帖子获得超过 1300 万次浏览，其引发强烈反响的根本原因在于：**许多人已经在独立地进行类似实践**，帖子为这些散发性尝试赋予了名称和结构[^src-1]。

这些既有的散发实践包括：Claude Code 的 CLAUDE.md 文件、各 AI Agent 的规则文件、在 Notion 或 Obsidian 中自行构建的知识结构。X、Reddit、Hacker News 上「让 LLM 整理知识」的话题也早已反复出现[^src-2]。

作者本人也经历了这种认知结晶：「自分もそのひとりで、『ああ、自分がやっていたのはこういうことだったのか』と輪郭がはっきりした感覚がありました」（我也是其中之一，产生了「啊，原来自己一直在做的就是这个」的轮廓清晰化感觉）[^src-3]。作者此前已有 Mem0 事实抽取、向量 DB 文档蓄积、知识审计命令等跨会话知识持久化机制，但缺少「以人类可读形式结构化文档」这一层，Karpathy 的「编译为 wiki」概念填补了这一空白[^src-4]。

这一现象表明，LLM Wiki 模式并非凭空创造，而是对已广泛存在但尚未被明确表述的实践的命名与结构化。Karpathy 帖子中的刻意抽象策略可能正是促成这种广泛共振的原因之一——足够抽象以覆盖多种既有实践[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L27 -- "このポストに反応が大きかった理由は、多くの人がすでに似たようなことを試みていたからだと思います"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L27 -- "Claude Code の CLAUDE.md、各 AI エージェント のルールファイル、あるいは Notion や Obsidian に自分なりのナレッジ構造を作っている人。X や Reddit、Hacker News でも「LLM にナレッジを整理させる」系の話題は以前から繰り返し盛り上がっていました"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L27 -- "自分もそのひとりで、「ああ、自分がやっていたのはこういうことだったのか」と輪郭がはっきりした感覚がありました"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L91-93 -- "セッション間の知識を永続化する仕組みは持っていました...ただ、それらはあくまで LLM が検索で参照するためのもので、人間が読める形で構造化されたドキュメント としては十分に整備できていませんでした"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L27 -- "Karpathy 氏のポストは、そういった散発的な試みに名前と構造を与えてくれたように感じます"
