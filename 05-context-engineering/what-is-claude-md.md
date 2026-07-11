# What is CLAUDE.md?

CLAUDE.md is a special file that Claude Code reads at the start of every session. It's like a briefing document — it tells the AI what your project is, what rules to follow, and where to find things.

Think of it as the difference between a contractor who walks onto a job site cold and one who read the job file before arriving.

---

## Where it lives

Place `CLAUDE.md` in the root of your project directory:

```
my-project/
├── CLAUDE.md          ← Claude Code reads this first
├── src/
├── docs/
└── knowledge/
```

---

## What it contains

A CLAUDE.md has four core sections:

### 1. Mission
One sentence. What is this project?

```markdown
## Mission
A knowledge management system for capturing and retrieving what I learn on the job.
```

### 2. Non-Negotiables
Your rules. What should the AI always or never do in this project?

```markdown
## Non-Negotiables
- Never hardcode credentials or API keys — use .env files only
- Archive instead of delete — retired files go to Archive/, not the trash
- Always update docs/ when making significant changes
- Keep commit messages descriptive: what changed and why
```

### 3. Directory Structure
A map of your project. What's in each folder?

```markdown
## Directory Structure
- `src/` — main scripts and code
- `docs/` — architecture notes and runbooks
- `knowledge/` — extended knowledge: decisions, learnings, contacts
- `prototypes/` — experiments (nothing in src/ imports from here)
- `Archive/` — retired files (never delete, move here)
```

### 4. Load-on-Demand References
Pointers to detailed docs. Keep CLAUDE.md short by linking out.

```markdown
## References
- Deploy guide: `docs/deploy.md`
- Knowledge folder guide: `knowledge/README.md`
- Credential locations: `docs/credentials.md` (no secrets stored here)
```

---

## What CLAUDE.md is NOT

- **Not a README.** README is for humans visiting your GitHub. CLAUDE.md is for the AI working in your project.
- **Not a prose document.** Don't write paragraphs. Write structured lists and metadata.
- **Not a place for secrets.** Never put API keys, passwords, or credentials in CLAUDE.md.
- **Not exhaustive.** Keep it short — point to detailed docs, don't paste them in.

---

## A complete example

```markdown
# my-automation-project — Claude Code Context

Last updated: 2026-05-01

## Mission
Python automation scripts for processing customer data exports and generating weekly reports.

## Non-Negotiables
- Never hardcode credentials — all config via .env files
- Syntax-check Python before deploying: python3 -m py_compile
- Archive instead of delete — retired scripts go to Archive/
- Update docs/CHANGELOG.md when scripts change behavior
- Test scripts against sample data in tests/ before touching production files

## Directory Structure
- `src/` — production scripts
- `prototypes/` — experiments (never import from src/)
- `docs/` — runbooks and notes
- `tests/` — sample data and test runs
- `knowledge/` — decisions, learnings, vendor contacts
- `Archive/` — retired code

## References
- Customer data format: `docs/data-schema.md`
- Deployment runbook: `docs/deploy.md`
- Vendor contacts: `knowledge/contacts/vendors.md`
```

---

## How each environment uses it

This is the one place the two tracks from [section 04](../04-ide-setup/) genuinely differ, so it's worth being clear.

**Claude Code (terminal).** It's automatic. When you run `claude` in your project directory, Claude Code:
1. Finds CLAUDE.md in the current directory
2. Reads it before doing anything else
3. Applies the rules throughout the session
4. Knows where to look for things without asking

You do nothing. Every session starts already briefed.

**Claude Desktop.** Desktop does *not* automatically read CLAUDE.md. It's a Claude Code convention. But you still get the same benefit with one small habit. Two ways to do it:

- **Best: use a Project.** Create a Project in Claude Desktop and, in the Project's custom instructions, add a line like: *"At the start of every conversation, use the Filesystem connector to read CLAUDE.md in the project folder and follow it."* Now every chat in that Project briefs itself, the same way Claude Code does. (You'll need the [Filesystem connector](../04-ide-setup/claude-desktop-connectors.md) set up.)
- **Quick: just ask.** At the start of a conversation, say *"Read CLAUDE.md in my project folder before we start."* Less automatic, but it works anywhere.

Either way, the file itself is identical. You write one CLAUDE.md; only *how it gets loaded* differs by environment.

The result in both: the AI behaves consistently across sessions, doesn't make decisions that violate your rules, and always knows your project structure.

---

## Next: writing your own CLAUDE.md

See [writing-your-claude-md.md](./writing-your-claude-md.md) for a fill-in-the-blank template.
