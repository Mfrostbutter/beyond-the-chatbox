# Staying in Control (and Managing Cost)

Claude Code can read your files, run commands, and change things. That power is the point, but it also means you want a few guardrails so nothing happens that you didn't intend, and so you don't burn money or context by accident.

This page covers the four controls that matter most for beginners: plan mode, permissions, context management, and cost.

---

## 1. Plan mode — look before it leaps

For anything bigger than a one-line change, have Claude Code lay out a plan and wait for your approval before it touches files.

Press **Shift+Tab** to cycle the mode indicator at the bottom of the screen until it says **plan mode**. In plan mode, Claude investigates and proposes a plan but does not edit files or run commands until you approve it.

This is the single best habit for staying in control. You review the plan, say "go" (or "no, do it this way instead"), and only then does work happen.

You can also just ask, in any mode:

> Before making changes, show me your plan and wait for my OK.

---

## 2. Permissions — what runs without asking

By default, Claude Code asks before running a command or editing a file. You approve each one. That's the safest mode and the right place to start.

As you get comfortable, you'll get tired of approving the same safe commands over and over. You can pre-approve them in `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(git status)",
      "Bash(git log*)",
      "Bash(git diff*)",
      "Bash(ls*)"
    ]
  }
}
```

Anything in `allow` runs without a prompt. Everything else still asks.

**The rule of thumb:** only pre-approve commands that are read-only or easy to undo. Listing files, reading git history, and checking a diff are safe. Pushing to GitHub, deleting files, or running arbitrary code are not — leave those asking every time. The template in `07-repo-template/.claude/settings.json` ships with a deliberately conservative list for exactly this reason.

**One thing to avoid as a beginner:** the `--dangerously-skip-permissions` flag turns off all approvals and lets Claude run anything without asking. It has its place for experienced users in throwaway environments. It is not where you start. The name is a warning, not a dare.

---

## 3. Context management — keep the window clean

Everything in your conversation, every file read, and every command output shares one context window (see the [glossary](../01-foundations/glossary.md)). When it fills up, responses get slower and the AI starts losing track of earlier detail.

Two commands keep it healthy:

- **`/clear`** — wipe the conversation and start fresh. Use this between unrelated tasks. Finished fixing a bug and now writing docs? Clear first. Your CLAUDE.md reloads automatically, so you don't lose project context, just the chat history.
- **`/compact`** — summarize the conversation so far to reclaim space while keeping the gist. Use this mid-task when you're deep in something and don't want to start over.

The habit: **one task, one conversation.** Clear when you switch.

---

## 4. Cost — know what you're spending

- **`/cost`** shows token usage for the current session. Check it now and then to build intuition for what things cost.
- If you're on a **Claude Pro or Max subscription**, you're paying a flat monthly fee. There's no per-session bill to watch, just usage limits that reset.
- If you're using an **API key**, you pay per token. Set a spending limit in the [Anthropic Console](https://console.anthropic.com) under Billing so a runaway session can't surprise you. Using `/clear` between tasks also keeps costs down, because a smaller context means fewer tokens per message.

---

## The short version

- **Shift+Tab into plan mode** for anything non-trivial. Approve the plan before work starts.
- **Only pre-approve safe, reversible commands.** Leave push, delete, and arbitrary code asking.
- **`/clear` between tasks**, `/compact` mid-task.
- **`/cost` to stay aware**, and set a Console spending limit if you're on an API key.

---

## Next

Back to the [section index](./README.md), or continue to [06 — Extended Knowledge](../06-extended-knowledge/).
