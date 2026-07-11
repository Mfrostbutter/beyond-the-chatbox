# Custom Slash Commands

You've seen built-in slash commands like `/clear` and `/cost`. You can also make your own. A custom command is just a saved prompt you can trigger by name, so you stop retyping the same instructions.

If you find yourself pasting the same multi-line request into Claude Code over and over, that's a command waiting to be made.

---

## How it works

A custom command is a markdown file in `.claude/commands/`. The filename becomes the command name, and the file's contents become the prompt.

```
your-project/
├── CLAUDE.md
└── .claude/
    └── commands/
        └── review.md      ← creates the /review command
```

Type `/review` in Claude Code and it runs whatever is written in `review.md`, as if you'd typed it yourself.

---

## A first command

Create `.claude/commands/review.md`:

```markdown
Review my uncommitted changes before I commit.

1. Run `git diff` to see what changed.
2. Check for: leftover debug code, hardcoded secrets, anything that
   contradicts the rules in CLAUDE.md.
3. Give me a short list: blocking issues first, then minor suggestions.
4. Do not change any files. This is a review, not a rewrite.
```

Now `/review` gives you a consistent pre-commit check every time, without retyping the instructions.

---

## Passing in details with `$ARGUMENTS`

Commands can take input. Anything you type after the command name replaces `$ARGUMENTS` in the file.

Create `.claude/commands/explain.md`:

```markdown
Explain how $ARGUMENTS works in this project. Read the relevant files
first, then explain it in plain language for someone new to the codebase.
Keep it short. Point to the specific files involved.
```

Then type:

```
/explain the email sending flow
```

Claude reads `the email sending flow` in place of `$ARGUMENTS` and runs the prompt.

---

## Good commands to start with

- **`/review`** — the pre-commit check above.
- **`/explain`** — plain-language walkthrough of any part of your project.
- **`/standup`** — "summarize what changed in git over the last day and turn it into three bullet points for a standup update."
- **`/tidy`** — "look for TODO comments and dead code in the files I changed and list them. Don't fix anything, just report."

---

## Commands vs agents vs hooks

These three features overlap, so here's when to reach for each:

| Feature | What it is | Triggered by |
|---|---|---|
| **Custom command** | A saved prompt you invoke on demand | You typing `/name` |
| **Agent** (`.claude/agents/`) | A specialized helper with its own instructions and tools | You asking, or Claude delegating to it |
| **Hook** (`settings.json`) | A shell command that fires automatically on an event | An event (Stop, Notification, etc.), no typing |

Rule of thumb: **command** when you want to trigger a repeatable prompt yourself, **agent** when you want a focused specialist for a category of work, **hook** when you want something to happen every time without remembering to ask.

---

## Next

See the agents in [`07-repo-template/.claude/agents/`](../07-repo-template/.claude/agents/) for the next step up, and [Hooks](./hooks.md) for automation that runs on its own.
