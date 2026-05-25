# Brain mailbox protocol

`status`: `experimental`

本目录是一个最小 brain-agent team control plane。它不假设 Codex 已经提供完整 agent team runtime，而是在文件系统上提供可恢复的 mailbox、route、claim、complete 和 wake 标记。

## 核心模型

```text
main-agent / ops brain
-> brainctl route / hook
-> brain inbox
-> brain agent wakes once, claims one message, writes artifacts, completes
-> brain outbox response
```

mailbox 是 durable communication；hook 或 ops brain 是 alarm clock；brain agent 是醒来处理消息后退出的 lane controller。

## Brain 目录

每个 brain 至少有：

```text
brains/<brain>/
  brain_state.json
  inbox.jsonl
  outbox.jsonl
  queue.jsonl
  wake_required.json
```

当前实验 brain：

- `audit`: 产生审计请求。
- `production`: 响应 revision / draft / production 请求。
- `similarity`: 后续负责 title similarity top3 和 comparison。
- `ops`: 后续负责 routing、lifecycle registry 和 push window。

## Message 状态

- `open`: 已创建但未完成。
- `routed`: 已投递到目标 inbox。
- `claimed`: 目标 brain 已领取。
- `resolved`: 已处理完成。
- `blocked`: 无法处理，需要上游或 human checkpoint。

## Hook 约定

repo-local 最小 hook 入口是：

```bash
python3 llm_wiki/loop/tools/brainctl.py hook --event post_tool_use
```

也可以调用 shell shim：

```bash
llm_wiki/loop/hooks/brain-mailbox-hook.sh
```

它只做轻量工作：

1. route open outbox messages to target inboxes。
2. 为有 open/routed message 的 brain 写 `wake_required.json`。
3. 在 `logs/brain_message_bus.jsonl` 里追加事件。

它不 spawn sub-agent，不读取 source material，不写 KB。

## Brain agent wake prompt

调度者唤醒某个 brain 时，提示词应包含：

```text
你是 <brain>_brain。
先读 llm_wiki/loop/brains/<brain>/brain_state.json。
再读 llm_wiki/loop/brains/<brain>/inbox.jsonl。
只处理 status 为 routed/open 且 to 为 <brain> 的消息。
处理前用 brainctl claim。
处理后写必要 artifact，并用 brainctl complete 或 block。
不要直接写其它 brain 的目录；跨 brain 只通过 outbox message。
```

## 当前限制

- 这是最小实验，不是完整 scheduler。
- `brainctl hook` 只写 wake marker；真正 spawn/resume 仍由 main-agent 或未来 ops brain 完成。
- brain 之间不直接 spawn 对方 child worker。
