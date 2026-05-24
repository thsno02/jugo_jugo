# 自治 Loop 策略：LLM Wiki Topic KB

created_at:: 2026-05-24T05:30:00+08:00
active_topic:: llm_wiki
main_language:: zh-CN

## 目的

在人类离开电脑时，agent 可以继续围绕 LLM Wiki topic KB 做有限自治推进，但必须以 `data/` 中已保存 evidence 为主，不再漂移回 KB 生产机制这个 meta topic。

## 可自治执行

- 按 `.llmwiki/control/orchestration_gates.yaml` 检查阶段迁移。
- 从 `.llmwiki/control/knowledge_frontier.yaml` 选择 `ready_to_build` candidate。
- 读取 `data/raw/`、`data/manifests/` 和 reports 中的本地证据。
- 先执行 source mining，再更新 frontier。
- 生成 0-1 topic node bundle。
- 运行 validators、build view、parse citations、status。
- 写 run_plan、data_scope、audit_report、skill_eval。
- 如果 evidence gap 明确，写 retrieval_request。

## 必须停止或记录 blocker

- 想要绕过公司网络限制。
- 没有本地 evidence 却要 adopted topic claim。
- 把生产协议内容当成 LLM Wiki topic 内容。
- 跳过 source mining / knowledge frontier / generation-entry gate 直接写 card。
- 大规模 web retrieval 没有 request/preservation plan。
- 破坏 demo-0 archive 或用户已有未提交文件。

## 公司网络检索限制

当前是在公司电脑中运行，网页检索可能被拦截。只做有限普通检索；失败就保存 blocked/intercepted response，写入 retrieval log，未来在个人设备重新 retrieve。

## 决策规则

每个暂停点只选择一个 next action：

1. 如果 active nodes 为空，先 source-mine `origin_and_canon` batch。
2. 如果 validators 失败，先 repair instrumentation。
3. 如果 evidence 足够，把 frontier candidate 标为 `ready_to_build`。
4. 如果 evidence 不足，写 retrieval_request，不直接搜索扩展。
5. 如果生成了 major candidate，再运行 impact analysis。
6. 如果 backlog 形成 5+ adopted topic nodes，写 topic KB demo report。
