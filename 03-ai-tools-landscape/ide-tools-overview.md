# IDE-Based AI Tools

These tools run outside the browser — on your desktop, in a terminal, or inside your editor. They can read your files, edit code, maintain context across sessions, and connect to external services.

---

## Claude Desktop

**Made by:** Anthropic
**Runs in:** Desktop app (Windows and macOS)
**Pricing:** Claude Pro ($20/month) or Claude Max (from $100/month)
**Best for:** People who want to work with files and projects without touching a terminal

**What makes it different:**
- **Projects** — upload your CLAUDE.md, docs, or any files; Claude reads them at the start of every conversation
- **Connectors** — give Claude access to your local filesystem, GitHub, Google Drive, and more
- **No terminal required** — everything runs through a GUI you already understand
- **Same models as the API** — Claude Sonnet, Haiku, Opus depending on your plan
- **MCP server support** — connect custom tools the same way Claude Code does

**When to use it:** When you want AI to help with your real files and projects but you're not comfortable in a terminal yet. The BOOTSTRAP prompt in this repo works in Claude Desktop just as well as in Claude Code.

---

## Claude Code

**Made by:** Anthropic
**Runs in:** Terminal (any), VS Code extension
**Pricing:** Included with Claude Pro ($20/month) and Claude Max (from $100/month). You can also pay as you go with an Anthropic API key (billed through the Console). Log in with your Claude.ai subscription or an API key.
**Best for:** This is what this repo focuses on — see section 04 for full setup

**What makes it different:**
- Full filesystem access — reads and edits any file in your project
- Runs bash commands, git commands, package installs
- Reads your `CLAUDE.md` at the start of every session — persistent project context
- Supports custom agents (`.claude/agents/` directory)
- Agentic loops — can plan and execute multi-step tasks autonomously
- No GUI — runs in your terminal, which is part of the point

**When to use it:** When you want the AI to actually do work — scaffold a project, refactor code, review files, set up a new agent, initialize a CLAUDE.md.

---

## Cursor

**Made by:** Anysphere
**Runs in:** Dedicated editor (VS Code fork)
**Pricing:** Free tier (limited), Pro $20/month
**Website:** cursor.com

**What makes it different:**
- A full VS Code fork with AI deeply integrated throughout the editor
- "Composer" mode: give it a multi-file task, it plans and executes across the whole codebase
- Tab autocomplete that predicts multi-line edits (better than Copilot for some workflows)
- Built-in Claude, GPT-4, and other model support — you choose per-task
- `.cursorrules` file for persistent project context (equivalent to CLAUDE.md for Cursor)

**When to use it:** If you want a polished all-in-one AI coding environment and don't mind switching from standard VS Code. Popular in the AI-native developer community.

---

## Cline (formerly Claude Dev)

**Made by:** Community/open source
**Runs in:** VS Code extension
**Pricing:** Free extension — pays for API calls (Claude, GPT-4, Gemini, local models)
**GitHub:** github.com/cline/cline

**What makes it different:**
- Open source VS Code extension
- Similar agentic capabilities to Claude Code (reads files, runs commands)
- Supports multiple AI providers — Claude, GPT-4, local models via Ollama
- Good for teams that want flexibility on model choice
- Active community and rapid development

**When to use it:** If you want Claude Code-style capability inside VS Code without switching to Cursor, or if you want to use local/open-source models.

---

## GitHub Copilot

**Made by:** GitHub / Microsoft
**Runs in:** VS Code, JetBrains IDEs, GitHub.com
**Pricing:** Free tier for some users; $10/month individual; $19/month Business
**Best for:** Autocomplete and inline suggestions

**What makes it different:**
- The most widely deployed AI coding tool in enterprise
- Excellent at autocomplete — suggests the next line (or next block) as you type
- Copilot Chat in VS Code: ask questions in a sidebar, get code explanations
- GitHub integration: PR summaries, issue generation, code review suggestions
- Does NOT have the same filesystem/command access as Claude Code or Cline

**When to use it:** When you want smart autocomplete while typing. Many people run Copilot alongside Claude Code — Copilot for inline suggestions, Claude Code for larger tasks.

---

## Comparison table

| Tool | Interface | File access | Runs commands | Persistent context | Needs terminal |
|---|---|---|---|---|---|
| Claude Desktop | Desktop app | Via connector | No | Projects + CLAUDE.md | No |
| Claude Code | Terminal + VS Code ext | Full (built-in) | Yes | CLAUDE.md | Yes |
| Cursor | Dedicated editor | Full | Yes | .cursorrules | No |
| Cline | VS Code extension | Full | Yes | .clinerules | No |
| GitHub Copilot | VS Code + IDEs | Limited | No | None | No |

---

## Which should you start with?

**If you're new to terminals or just want something that works immediately:** Start with Claude Desktop. Install it, set up the Filesystem connector (section 04), and paste the BOOTSTRAP prompt in a conversation. No Node.js, no command line.

**If you're comfortable in a terminal and want more control:** Use Claude Code. It runs commands, manages git, and does more autonomous work. It's the more powerful path and the one most of section 04 covers.

**If you want an all-in-one polished editor:** Try Cursor.

**If you want to stay in VS Code and use multiple models:** Try Cline.

**If your workplace already uses GitHub:** Copilot is probably already available to you. It's a good starting point even if you eventually add Claude Desktop or Claude Code.

You don't need to pick just one. Many people use Claude Desktop for day-to-day work and Claude Code for heavier engineering tasks.
