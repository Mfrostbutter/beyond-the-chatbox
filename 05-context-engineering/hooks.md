# Hooks — Automating Claude's Behavior

Hooks are shell commands that run automatically at specific moments during a Claude Code session. They let you attach behavior to events without asking Claude to do it every time.

---

## Why hooks matter

Without hooks, you have to remember to ask Claude to "show what changed" or "run the tests" after every task. With hooks, that happens automatically.

Hooks are configured once in `settings.json` and run every session. They're the difference between a Claude Code setup that requires manual oversight and one that runs itself.

---

## The four hook events

| Event | When it fires | Common use |
|---|---|---|
| `Stop` | Claude finishes a turn | Show changed files, git status, run tests |
| `Notification` | Claude needs your attention | Desktop alert, sound, Slack message |
| `PreToolUse` | Before Claude uses a tool | Block dangerous commands, log intent |
| `PostToolUse` | After Claude uses a tool | Log what happened, trigger follow-ups |

For most projects, `Stop` and `Notification` are enough to start.

---

## How to add hooks

Open `.claude/settings.json` in your project and add a `hooks` key:

```json
{
  "permissions": {
    "allow": ["Bash(git *)"]
  },
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Claude finished. Changed files:' && git diff --name-only HEAD 2>/dev/null"
          }
        ]
      }
    ]
  }
}
```

The `matcher` field filters by tool name for `PreToolUse`/`PostToolUse`. Leave it empty to match everything.

---

## Recipes

### Show changed files when Claude stops

```json
"Stop": [
  {
    "matcher": "",
    "hooks": [
      {
        "type": "command",
        "command": "git diff --name-only HEAD 2>/dev/null"
      }
    ]
  }
]
```

### Desktop notification (macOS)

```json
"Notification": [
  {
    "matcher": "",
    "hooks": [
      {
        "type": "command",
        "command": "osascript -e 'display notification \"Claude needs your input\" with title \"Claude Code\"'"
      }
    ]
  }
]
```

### Desktop notification (Windows)

```json
"Notification": [
  {
    "matcher": "",
    "hooks": [
      {
        "type": "command",
        "command": "powershell -Command \"[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); [System.Windows.Forms.MessageBox]::Show('Claude needs your input', 'Claude Code')\""
      }
    ]
  }
]
```

### Block a specific bash pattern (PreToolUse)

```json
"PreToolUse": [
  {
    "matcher": "Bash",
    "hooks": [
      {
        "type": "command",
        "command": "if echo \"$CLAUDE_TOOL_INPUT\" | grep -q 'rm -rf'; then echo 'Blocked: rm -rf is not allowed'; exit 2; fi"
      }
    ]
  }
]
```

Exit code `2` blocks the tool call and surfaces the message to Claude. Exit code `0` lets it proceed.

---

## Hook output

Hook output (stdout/stderr) appears in your terminal. Claude Code does not see it unless you capture it and write it to a file that Claude reads. This is intentional: hooks are for you, not the AI.

---

## The template's hooks

The `07-repo-template/.claude/settings.json` includes two starter hooks:

- **Stop:** prints a divider and lists changed files via `git diff --name-only`
- **Notification:** prints a message when Claude is waiting

Replace the echo commands with platform-appropriate notification commands once you know what environment you're on.

---

## What to do next

1. Copy the template `settings.json` and add the hooks above
2. Start a Claude Code session and watch the Stop hook fire when Claude finishes
3. Experiment with PreToolUse to block anything you'd never want Claude to run automatically
