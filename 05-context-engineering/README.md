# 05 — Context Engineering

This is the core skill. Everything else in this repo supports it.

**Prompt engineering** is the art of asking AI good questions.
**Context engineering** is the art of structuring your work so the AI always has the right information — without you having to ask.

The difference: prompt engineering requires effort every session. Context engineering is a one-time investment that compounds.

---

## The problem with web chat AI

When you use Claude.ai or ChatGPT without any setup:
- The AI knows nothing about your project
- You re-explain context every conversation
- Nothing is remembered between sessions
- The AI makes decisions without knowing your rules, preferences, or constraints

This is like hiring a contractor who shows up to every job with no memory of previous visits.

---

## The context engineering solution

A well-structured project with a CLAUDE.md file means:
- Claude Code reads your project context before every session
- Your rules are enforced automatically
- The AI knows your folder structure, naming conventions, and constraints
- You spend time on work, not re-explaining

This is like having a contractor who reads the job file before every visit.

---

## What's in this section

- [What is CLAUDE.md](./what-is-claude-md.md) — The core pattern explained with examples
- [Writing Your CLAUDE.md](./writing-your-claude-md.md) — Step-by-step guide with fill-in-the-blank structure
- [Repo Structure Patterns](./repo-structure-patterns.md) — How to organize files so the AI always knows where things are
- [Prompting in the IDE](./prompting-in-ide.md) — Effective prompting patterns once you're in Claude Code
- [Staying in Control](./staying-in-control.md) — Plan mode, permissions, context management, and cost
- [Custom Slash Commands](./custom-commands.md) — Turn a prompt you keep retyping into a `/command` *(Claude Code only)*
- [Hooks](./hooks.md) — Shell commands that run automatically at key moments *(Claude Code only)*

> **On the two tracks (from [section 04](../04-ide-setup/)):** CLAUDE.md and the knowledge folder work in both Claude Desktop and Claude Code. Hooks and custom commands are Claude Code only, and each of those pages opens with the Desktop equivalent. The core skill in this section applies no matter which track you chose.

---

## The big ideas

### 1. CLAUDE.md is a control plane, not prose
Don't write paragraphs. Write structured metadata. The AI reads this like a database, not a letter.

### 2. Load-on-demand references
CLAUDE.md should point to detailed docs, not contain them. "Deployment guide: `docs/deploy.md`" is better than pasting the whole guide in.

### 3. Your folder structure communicates intent
`prototypes/` means "experimental, not production." `docs/` means "reference material." The names matter — the AI uses them to understand what kind of work belongs where.

### 4. The knowledge folder is your extended knowledge base
A `knowledge/` folder full of markdown files is context that persists. When you capture a decision in `knowledge/decisions/`, it's there the next time the AI needs it — without you having to remember to mention it.

---

## What to do next

Read [what-is-claude-md.md](./what-is-claude-md.md) first, then work through the others in order.
