# Skill Eval / 偏差复盘

## 主要 failure mode

我把 production protocol 当成了 content topic，混淆了 meta layer 和 object layer。

## 具体表现

- `loop_plan_init_kb.md` 被当成主要内容来源。
- `data/` 中的 raw corpus 没有被当作 topic KB 的 primary evidence layer。
- 第一批 nodes 写成了 KB 生产机制，而不是 LLM Wiki topic。

## 修正

- demo-0 已 archive。
- active topic 改成 `llm_wiki`。
- `topic_node_backlog.yaml` 改为 origin、definition、architecture、workflow、ecosystem、evaluation、risks、comparison、scale boundaries。
- 下一轮必须从 `data/raw/`、`data/manifests/` 和 reports 生成 topic nodes。

## Skill patch

Node planning skill 需要增加一条硬规则：当 plan 文件是生产协议时，不能把协议章节自动当作 KB 内容节点；必须先确认 object-level topic，并从 topic evidence corpus 选择 nodes。
