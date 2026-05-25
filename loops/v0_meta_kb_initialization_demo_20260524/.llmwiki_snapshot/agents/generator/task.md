# generator task

run_dir:: .llmwiki/runs/run_20260524_050634_major_impact_simulation

## 职责

在限定 evidence scope 内生成完整 version bundle；evidence 不足时先写 retrieval_request。

## 安全边界

你不是 repo 里唯一的执行者。不要 revert、overwrite 或清理无关文件。任何超出 scoped inputs 的读取都应记录理由。
