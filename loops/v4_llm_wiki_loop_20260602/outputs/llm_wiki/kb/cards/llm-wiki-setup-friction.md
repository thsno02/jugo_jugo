---
id: llm-wiki-setup-friction
title: LLM Wiki 搭建摩擦
status: accepted
card_type: source_claim
tags: [llm-wiki, setup, friction, practitioner-report, llm-c]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [kunal-local-knowledge-base]
justification: ../justification/llm-wiki-setup-friction.md
canonical_concept: llm-wiki-setup-friction
aliases: [搭建摩擦, setup friction, 三个搭建障碍, setup walls]
summary: >-
  llm-wiki-setup-friction（搭建摩擦 / setup friction / 三个搭建障碍）是 llm.c 搭建时的三面墙：macOS Clang 不支持 OpenMP 需改用 GCC、wiki 功能要求单一大文本文件需预处理多文件笔记、CPU 推理 30+ 秒/查询而 GPU 仅需数秒
related: [llm-wiki-pattern]
---

作者在搭建 Karpathy 的 llm.c LLM wiki 时遇到了三个具体障碍，"花了整个周六"[^src-1]：

**障碍一：macOS 编译。** macOS 默认的 Clang 编译器不支持 OpenMP（llm.c 的并行化所需），这是 Hacker News 讨论中"最常见的抱怨"。修复方法是通过 Homebrew 安装 GCC（`brew install gcc`），但错误信息本身不会指向这个解决方案。在 Linux 上使用较新版 GCC 则编译顺畅[^src-2]。

**障碍二：数据准备。** wiki 功能期望输入一个**单一的大文本文件**。作者的笔记分散在三个工具中的 400 个 markdown 文件里，因此需要编写预处理脚本并添加文档边界标记。"可黑客化"的哲学在此有两面性——没有内建的文档加载器意味着"又多花了一小时"[^src-3]。

**障碍三：硬件现实。** CPU 推理可行但缓慢——在 M2 MacBook Pro 上即使是中等规模索引，每次查询也需 30+ 秒。使用 CUDA GPU 则可降至数秒。硬件始终是本地 AI 工作的首要瓶颈[^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L94 -- "In practice, I hit three walls that cost me an entire Saturday."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L97 -- "the default Clang compiler doesn't support OpenMP, which llm.c needs for parallelism. This is the single most common complaint in the Hacker News threads... The fix is installing GCC via Homebrew"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L99 -- "The wiki feature expects a single large text file. My notes lived in 400 markdown files across three tools... there's no built-in document loader, which means you build your own, which means another hour gone."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L101 -- "Running inference on CPU is possible but slow. I'm talking 30+ seconds per query on an M2 MacBook Pro... With a CUDA-capable GPU, queries drop to a few seconds."
