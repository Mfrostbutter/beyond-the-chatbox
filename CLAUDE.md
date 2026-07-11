# context-engineering-blueprint — Claude Code Context

Last updated: 2026-07-11.

## Mission

Educational repo for people transitioning from web-based AI chat tools to IDE-based AI workflows. Teaches context engineering, GitHub basics, and automation fundamentals.

## Non-Negotiables

- **Beginner-first.** No jargon without a glossary entry. No assumed technical knowledge.
- **No infra complexity.** No LXCs, no Qdrant, no MCP servers, no self-hosted databases in examples.
- **No brand content.** This repo has no association with Agenius AI Labs, BWIT, RIOS, or Cantique. Keep it generic and universal.
- **Real links only.** All YouTube and whitepaper links must be real and verified. No made-up URLs.
- **Archive, never delete.** Retired content goes to `Archive/`, not the trash.

## Directory Structure

- `00-prerequisites/` - One-time setup: Claude Pro, Git, VS Code, Docker Desktop
- `01-foundations/` - AI concepts, YouTube channels, whitepapers, glossary
- `02-github-basics/` - Git fundamentals, GitHub for AI workflows, resources
- `03-ai-tools-landscape/` - Web chat vs IDE comparison, tool overview
- `04-ide-setup/` - Claude Code install, VS Code setup, bootstrap prompts
- `05-context-engineering/` - CLAUDE.md pattern, repo structure, prompting in IDE
- `06-extended-knowledge/` - Knowledge folder setup, Obsidian integration
- `07-repo-template/` - Drop-in template: copy, fill in, go
- `08-automation-platforms/` - n8n, Make, Zapier beginner workflows
- `09-mcp-servers/` - How MCP works, build your first server
- `docs/` - Images used by the guides
- `resources/` - Prompt library, communities

## Key Files

- `07-repo-template/BOOTSTRAP.md` — Paste into Claude Code to scaffold a new project
- `07-repo-template/CLAUDE.md` — Annotated template with fill-in-the-blank sections
- `07-repo-template/.claude/agents/` — Four ready-to-use agents + create-your-own prompt
- `07-repo-template/.claude/commands/` — Starter custom slash command (`/review`)
- `04-ide-setup/bootstrap-prompt.md` — First-session prompt for brand new Claude Code users
- `04-ide-setup/claude-desktop-connectors.md` — No-terminal path: enable the Filesystem connector
- `05-context-engineering/staying-in-control.md` — Plan mode, permissions, context, cost
- `05-context-engineering/custom-commands.md` — Author your own slash commands
- `.github/workflows/link-check.yml` — CI enforcing the real-links-only rule
