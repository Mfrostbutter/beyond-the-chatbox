# Agents

> **Claude Code only.** Agents (like the rest of the `.claude/` folder: `commands/`, `settings.json`, and hooks) are read by Claude Code, not Claude Desktop. If you're on the **Claude Desktop** track, you can ignore this folder. It does no harm sitting in your project, and the parts that *do* work in both environments (`CLAUDE.md` and the `knowledge/` folder) are unaffected. The Desktop equivalent of an agent is a Project with focused instructions.

This folder contains agent definitions for Claude Code. Each agent is a specialized assistant scoped to a specific task.

## How agents work

An agent is triggered by a description pattern. When you tell Claude Code to do something that matches an agent's trigger description, it uses that agent's tools and workflow instead of the default behavior.

You can also explicitly invoke an agent by naming it.

## Agents in this template

| Agent | File | What it does |
|---|---|---|
| Researcher | `researcher.md` | Research a topic and produce a structured brief |
| Doc Writer | `doc-writer.md` | Turn notes or bullet points into a clean markdown doc |
| Code Reviewer | `code-reviewer.md` | Review changed files for quality and issues |
| Meeting Prep | `meeting-prep.md` | Produce a meeting brief from context files |

## Adding your own agents

Use the `create-your-own.md` prompt to have Claude Code walk you through building a custom agent.

## Agent file structure

Every agent file has this structure:

```markdown
---
name: agent-name
description: [trigger patterns that activate this agent]
tools: [list of tools the agent can use]
model: sonnet  # or haiku for faster/cheaper, opus for complex tasks
---

## What this agent does
[brief description]

## Workflow
1. [step one]
2. [step two]
...

## Never
- [things this agent should not do]
```
