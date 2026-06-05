---
schema: justification_journal.v1
card: ../cards/citation-partial-support-limitation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
源证据：
- sections/evaluation.tex -- "this algorithm overlooks the scenario when one citation partially supports the statement"
- sections/appendix.tex -- "it is challenging to conduct such evaluation automatically...We also explore prompting ChatGPT to conduct such a task, which yields poor results."
- sections/appendix.tex -- "ALCE has a recall of 75.6% and a precision of 66.1%...it has a relatively high false positive rate"
范围论证："部分支持"检测缺失是 NLI 引用验证机制的一个独立且明确的局限，直接影响 citation precision 的准确性。与 NLI 引用验证机制卡相区分——该卡描述机制本身，本卡描述机制的已知边界。
