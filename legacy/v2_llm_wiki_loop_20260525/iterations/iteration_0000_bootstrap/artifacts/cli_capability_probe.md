# CLI capability probe

## `codex --version`

```text
exit_code=0
codex-cli 0.132.0
```

## `codex features list`

```text
exit_code=0
apply_patch_freeform                    removed            false
apply_patch_streaming_events            under development  false
apps                                    stable             true
apps_mcp_path_override                  under development  false
artifact                                under development  false
auth_elicitation                        under development  false
browser_use                             stable             true
browser_use_external                    stable             true
child_agents_md                         under development  false
chronicle                               under development  false
code_mode                               under development  false
code_mode_only                          under development  false
codex_git_commit                        removed            false
collaboration_modes                     removed            true
computer_use                            stable             true
default_mode_request_user_input         under development  false
elevated_windows_sandbox                removed            false
enable_fanout                           under development  false
enable_mcp_apps                         under development  false
enable_request_compression              stable             true
exec_permission_approvals               under development  false
experimental_windows_sandbox            removed            false
external_migration                      experimental       false
fast_mode                               stable             true
goals                                   experimental       true
guardian_approval                       stable             true
hooks                                   stable             true
image_detail_original                   removed            false
image_generation                        stable             true
in_app_browser                          stable             true
js_repl                                 removed            false
js_repl_tools_only                      removed            false
memories                                experimental       false
mentions_v2                             experimental       false
multi_agent                             stable             true
multi_agent_v2                          under development  false
network_proxy                           experimental       false
personality                             stable             true
plugin_hooks                            stable             true
plugin_sharing                          stable             true
plugins                                 stable             true
prevent_idle_sleep                      experimental       false
realtime_conversation                   under development  false
remote_compaction_v2                    under development  false
remote_control                          removed            false
remote_models                           removed            false
remote_plugin                           under development  false
request_permissions_tool                under development  false
request_rule                            removed            false
responses_websocket_response_processed  under development  false
responses_websockets                    removed            false
responses_websockets_v2                 removed            false
runtime_metrics                         under development  false
search_tool                             removed            false
shell_snapshot                          stable             true
shell_tool                              stable             true
shell_zsh_fork                          under development  false
skill_env_var_dependency_prompt         under development  false
skill_mcp_dependency_install            stable             true
sqlite                                  removed            true
steer                                   removed            true
terminal_resize_reflow                  experimental       true
tool_call_mcp_elicitation               stable             true
tool_search                             stable             true
tool_search_always_defer_mcp_tools      under development  false
tool_suggest                            stable             true
tui_app_server                          removed            true
unavailable_dummy_tools                 removed            false
undo                                    removed            false
unified_exec                            stable             true
use_legacy_landlock                     deprecated         false
use_linux_sandbox_bwrap                 removed            false
web_search_cached                       deprecated         false
web_search_request                      deprecated         false
workspace_dependencies                  stable             true
workspace_owner_usage_nudge             removed            false
```

## `claude --version`

```text
exit_code=0
2.1.128 (Claude Code)
```

## `claude --help`

```text
exit_code=0
Usage: claude [options] [command] [prompt]

Claude Code - starts an interactive session by default, use -p/--print for
non-interactive output

Arguments:
  prompt                                            Your prompt

Options:
  --add-dir <directories...>                        Additional directories to allow tool access to
  --agent <agent>                                   Agent for the current session. Overrides the 'agent' setting.
  --agents <json>                                   JSON object defining custom agents (e.g. '{"reviewer": {"description": "Reviews code", "prompt": "You are a code reviewer"}}')
  --allow-dangerously-skip-permissions              Enable bypassing all permission checks as an option, without it being enabled by default. Recommended only for sandboxes with no internet access.
  --allowedTools, --allowed-tools <tools...>        Comma or space-separated list of tool names to allow (e.g. "Bash(git *) Edit")
  --append-system-prompt <prompt>                   Append a system prompt to the default system prompt
  --bare                                            Minimal mode: skip hooks, LSP, plugin sync, attribution, auto-memory, background prefetches, keychain reads, and CLAUDE.md auto-discovery. Sets CLAUDE_CODE_SIMPLE=1. Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read). 3P providers (Bedrock/Vertex/Foundry) use their own credentials. Skills still resolve via /skill-name. Explicitly provide context via: --system-prompt[-file], --append-system-prompt[-file], --add-dir (CLAUDE.md dirs), --mcp-config, --settings, --agents, --plugin-dir.
  --betas <betas...>                                Beta headers to include in API requests (API key users only)
  --brief                                           Enable SendUserMessage tool for agent-to-user communication
  --chrome                                          Enable Claude in Chrome integration
  -c, --continue                                    Continue the most recent conversation in the current directory
  --dangerously-skip-permissions                    Bypass all permission checks. Recommended only for sandboxes with no internet access.
  -d, --debug [filter]                              Enable debug mode with optional category filtering (e.g., "api,hooks" or "!1p,!file")
  --debug-file <path>                               Write debug logs to a specific file path (implicitly enables debug mode)
  --disable-slash-commands                          Disable all skills
  --disallowedTools, --disallowed-tools <tools...>  Comma or space-separated list of tool names to deny (e.g. "Bash(git *) Edit")
  --effort <level>                                  Effort level for the current session (low, medium, high, xhigh, max)
  --exclude-dynamic-system-prompt-sections          Move per-machine sections (cwd, env info, memory paths, git status) from the system prompt into the first user message. Improves cross-user prompt-cache reuse. Only applies with the default system prompt (ignored with --system-prompt). (default: false)
  --fallback-model <model>                          Enable automatic fallback to specified model when default model is overloaded (only works with --print)
  --file <specs...>                                 File resources to download at startup. Format: file_id:relative_path (e.g., --file file_abc:doc.txt file_def:img.png)
  --fork-session                                    When resuming, create a new session ID instead of reusing the original (use with --resume or --continue)
  --from-pr [value]                                 Resume a session linked to a PR by PR number/URL, or open interactive picker with optional search term
  -h, --help                                        Display help for command
  --ide                                             Automatically connect to IDE on startup if exactly one valid IDE is available
  --include-hook-events                             Include all hook lifecycle events in the output stream (only works with --output-format=stream-json)
  --include-partial-messages                        Include partial message chunks as they arrive (only works with --print and --output-format=stream-json)
  --input-format <format>                           Input format (only works with --print): "text" (default), or "stream-json" (realtime streaming input) (choices: "text", "stream-json")
  --json-schema <schema>                            JSON Schema for structured output validation. Example: {"type":"object","properties":{"name":{"type":"string"}},"required":["name"]}
  --max-budget-usd <amount>                         Maximum dollar amount to spend on API calls (only works with --print)
  --mcp-config <configs...>                         Load MCP servers from JSON files or strings (space-separated)
  --mcp-debug                                       [DEPRECATED. Use --debug instead] Enable MCP debug mode (shows MCP server errors)
  --model <model>                                   Model for the current session. Provide an alias for the latest model (e.g. 'sonnet' or 'opus') or a model's full name (e.g. 'claude-sonnet-4-6').
  -n, --name <name>                                 Set a display name for this session (shown in the prompt box, /resume picker, and terminal title)
  --no-chrome                                       Disable Claude in Chrome integration
  --no-session-persistence                          Disable session persistence - sessions will not be saved to disk and cannot be resumed (only works with --print)
  --output-format <format>                          Output format (only works with --print): "text" (default), "json" (single result), or "stream-json" (realtime streaming) (choices: "text", "json", "stream-json")
  --permission-mode <mode>                          Permission mode to use for the session (choices: "acceptEdits", "auto", "bypassPermissions", "default", "dontAsk", "plan")
  --plugin-dir <path>                               Load a plugin from a directory or .zip for this session only (repeatable: --plugin-dir A --plugin-dir B.zip) (default: [])
  -p, --print                                       Print response and exit (useful for pipes). Note: The workspace trust dialog is skipped when Claude is run in non-interactive mode (via -p, or when stdout is not a TTY, e.g. piped or redirected output). Only use this in directories you trust.
  --remote-control-session-name-prefix <prefix>     Prefix for auto-generated Remote Control session names (default: hostname)
  --replay-user-messages                            Re-emit user messages from stdin back on stdout for acknowledgment (only works with --input-format=stream-json and --output-format=stream-json)
  -r, --resume [value]                              Resume a conversation by session ID, or open interactive picker with optional search term
  --session-id <uuid>                               Use a specific session ID for the conversation (must be a valid UUID)
  --setting-sources <sources>                       Comma-separated list of setting sources to load (user, project, local).
  --settings <file-or-json>                         Path to a settings JSON file or a JSON string to load additional settings from
  --strict-mcp-config                               Only use MCP servers from --mcp-config, ignoring all other MCP configurations
  --system-prompt <prompt>                          System prompt to use for the session
  --tmux                                            Create a tmux session for the worktree (requires --worktree). Uses iTerm2 native panes when available; use --tmux=classic for traditional tmux.
  --tools <tools...>                                Specify the list of available tools from the built-in set. Use "" to disable all tools, "default" to use all tools, or specify tool names (e.g. "Bash,Edit,Read").
  --verbose                                         Override verbose mode setting from config
  -v, --version                                     Output the version number
  -w, --worktree [name]                             Create a new git worktree for this session (optionally specify a name)

Commands:
  agents [options]                                  Manage background and configured agents
  auth                                              Manage authentication
  auto-mode                                         Inspect auto mode classifier configuration
  doctor                                            Check the health of your Claude Code auto-updater. Note: The workspace trust dialog is skipped and stdio servers from .mcp.json are spawned for health checks. Only use this command in directories you trust.
  install [options] [target]                        Install Claude Code native build. Use [target] to specify version (stable, latest, or specific version)
  mcp                                               Configure and manage MCP servers
  plugin|plugins                                    Manage Claude Code plugins
  project                                           Manage Claude Code project state
  setup-token                                       Set up a long-lived authentication token (requires Claude subscription)
  ultrareview [options] [target]                    Run a cloud-hosted multi-agent code review of the current branch (or a PR number / base branch) and print the findings
  update|upgrade                                    Check for updates and install if available
```
