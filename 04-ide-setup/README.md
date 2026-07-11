# 04 — IDE Setup

This section gets you from zero to working with Claude on your real files and projects.

There are **two ways to do everything in this guide**, and this is where you pick one:

- **Claude Desktop** — a regular desktop app, no terminal. You click, you chat, Claude works with your files through a connector.
- **Claude Code** — Claude in your terminal (or inside VS Code). More power and automation, at the cost of a command line.

Both use the same core idea (context engineering) and the same [bootstrap prompt](./bootstrap-prompt.md). They differ in setup, and in a few features later on (hooks, custom commands, and how you add MCP servers). Wherever the two diverge, the rest of this guide calls it out with a **Claude Desktop** / **Claude Code** note. **Pick your track here and carry it through the guide.**

**Time required:** 15-45 minutes depending on which path you choose.

Not sure? Start with **Claude Desktop**. Everything you build (CLAUDE.md, your knowledge folder, your project) works in both, so you can add Claude Code later without redoing anything.

---

## Track A — Claude Desktop (no terminal)

Use this if you're not comfortable with a command line, or just want the fastest path to something useful.

**What you need:** A Claude Pro or Max plan ($20-100/month). No Node.js, no terminal.

**Steps, in order:**
1. Install Claude Desktop from https://claude.ai/download and sign in.
2. [Set up the Filesystem and GitHub connectors](./claude-desktop-connectors.md) — this is how Desktop reads and writes your files.
3. [Run the bootstrap prompt](./bootstrap-prompt.md) in a new conversation to scaffold your first project.

**What you'll have:** Claude reading and writing files in your project folder from a chat window. You describe what you want; Claude builds it.

---

## Track B — Claude Code (terminal / VS Code)

Use this if you're comfortable in a terminal, or want Claude to run commands, manage git, and work autonomously on larger tasks.

**What you need:** A Claude Pro or Max plan (the same account works for both tracks), or an Anthropic API key. Plus Node.js.

**Steps, in order:**
1. [Install Node.js and Claude Code, then sign in](./claude-code-install.md).
2. [Set up VS Code and the Claude Code extension](./vscode-setup.md) — optional but recommended.
3. [Run the bootstrap prompt](./bootstrap-prompt.md) in a new Claude Code session to scaffold your first project.

**What you'll have:** Claude running in your terminal with full filesystem and command access. The most capable setup, and the one that unlocks hooks, custom commands, and agents later.

---

## What differs between the two tracks

You don't need to memorize this now. It's here so you know what to expect as you move through the guide.

| Feature | Claude Desktop | Claude Code |
|---|---|---|
| Reads your files | Via the Filesystem connector | Built in |
| Reads `CLAUDE.md` automatically | No — you point it there (via a Project or by asking) | Yes, every session |
| Persistent project context | Projects (instructions + uploaded knowledge) | `CLAUDE.md` + `knowledge/` folder |
| Runs terminal commands / git | No | Yes |
| Hooks (section 05) | Not available | Yes |
| Custom slash commands (section 05) | Not available | Yes |
| Add an MCP server (section 09) | Connectors / Extensions directory, or `claude_desktop_config.json` | `claude mcp add` or `.mcp.json` |

The features Desktop lacks all have a "closest equivalent" noted where they come up. A Desktop user is never stranded.

---

## After setup

Once your track is working, move to [05 — Context Engineering](../05-context-engineering/) to understand how to structure your project so Claude always has the right context.
