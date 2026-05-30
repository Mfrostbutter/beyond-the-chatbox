# 04 — IDE Setup

This section gets you from zero to working with Claude on your real files and projects.

**Time required:** 15-45 minutes depending on which path you choose.

---

## Choose your path

### Desktop Path — no terminal required

Use this if you're not comfortable with a terminal, or just want the fastest path to something useful.

**What you need:** A Claude Pro or Claude Max account ($20–100/month). That's it.

**Steps:**
1. [Claude Desktop Connectors](./claude-desktop-connectors.md) — install Claude Desktop, add the Filesystem and GitHub connectors
2. [Bootstrap Prompt](./bootstrap-prompt.md) — paste this into a Claude Desktop conversation to scaffold your project

**What you'll have:** Claude can read and write files in your project folder. You describe what you want and Claude builds it.

---

### CLI Path — more control, more power

Use this if you're comfortable in a terminal or want Claude to run commands, manage git, and work autonomously on larger tasks.

**What you need:** A Claude API key (~$5-20/month) or Claude Max subscription. Node.js installed.

**Steps:**
1. [Claude Code Install](./claude-code-install.md) — install Node.js and Claude Code, get an API key
2. [VS Code Setup](./vscode-setup.md) — install VS Code and the Claude Code extension
3. [Bootstrap Prompt](./bootstrap-prompt.md) — paste this into a Claude Code session to scaffold your project

**What you'll have:** Claude running in your terminal with full filesystem and command access. The most capable setup.

---

## Not sure which to pick?

Start with Desktop. You can always add Claude Code later — the projects and CLAUDE.md files you create work in both environments.

---

## After setup

Once either path is working, move to [05 — Context Engineering](../05-context-engineering/) to understand how to structure your project so Claude always has the right context.
