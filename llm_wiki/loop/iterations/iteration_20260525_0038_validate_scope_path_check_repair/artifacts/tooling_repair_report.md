# tooling repair report

## 修复对象

- `llm_wiki/loop/tools/validate_scope.py`

## 失败证据

候选 1 audit task 中的 `fact_candidate_path` 指向不存在的 `llm_wiki/loop/iterations/iteration_20260525_0001_source_mining_karpathy_gist/artifacts/fact_candidates.md`，但派发前 `validate_scope.py` 仍返回 `scope_validation: pass`。worker 的 `read_log.md` 记录了该路径读取失败。

## 修改内容

- 增加 `## 允许输入` section 解析。
- 对允许输入区中的本地路径 code span 做存在性检查。
- 对 `raw.txt:1-5` 这类行号后缀做路径归一化。
- 跳过 `target_card_path` 和 `target_provenance_path`，因为 adoption 任务会把它们作为存在性和覆盖冲突检查目标，路径可能在采纳前不存在。
- 不检查 `## 允许写入` 区路径，避免把输出路径误判为缺失输入。

## 验证结果

```text
$ python3 -m py_compile llm_wiki/loop/tools/validate_scope.py
py_compile_ok

$ python3 llm_wiki/loop/tools/validate_scope.py llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/task.md
scope_validation: fail
missing_input_path: fact_candidate_path: llm_wiki/loop/iterations/iteration_20260525_0001_source_mining_karpathy_gist/artifacts/fact_candidates.md -> /Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/llm_wiki/loop/iterations/iteration_20260525_0001_source_mining_karpathy_gist/artifacts/fact_candidates.md

$ python3 llm_wiki/loop/tools/validate_scope.py llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/task.md
scope_validation: pass

$ python3 llm_wiki/loop/tools/validate_scope.py llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/task.md
scope_validation: pass
```

## 剩余风险

该检查只覆盖任务包允许输入区中可识别的本地路径 code span；如果未来任务包用非 code span 或自然语言描述必需输入，工具仍可能无法发现路径错误。当前选择保持最小修复，不扩大任务模板 schema。
