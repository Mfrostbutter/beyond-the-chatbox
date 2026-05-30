# Bootstrap Prompt — Scaffold Your First Project

This prompt works in both Claude Desktop and Claude Code. Paste it into a fresh conversation (Desktop) or a new Claude Code session (CLI) to scaffold your first context-engineered project.

**Claude Desktop users:** Make sure the [Filesystem connector is set up](./claude-desktop-connectors.md) with your project folder added before running this. Claude needs file access to create the folder structure.

**Claude Code users:** Run `claude` from inside your project directory, then paste the prompt.

---

## Prompt to paste

```
I'm new to Claude Code. I want to set up a new project. Here's what I'm working on:

[REPLACE THIS: describe your project in 2-3 sentences. What are you building or managing? What's the goal?]

Please help me:

1. Explore my current working directory and tell me what's here
2. Create a CLAUDE.md file that captures:
   - What this project is (one sentence)
   - 3-5 rules I should follow (no hardcoded secrets, archive instead of delete, etc.)
   - The directory structure with a brief description of each folder
3. Create this folder structure if it doesn't exist:
   - src/ (main work goes here)
   - prototypes/ (experiments — nothing in src/ imports from here)
   - docs/ (notes and documentation)
   - knowledge/ (extended knowledge — markdown files you should read for context)
   - knowledge/decisions/ (important decisions I've made)
   - knowledge/learnings/ (hard-won lessons and gotchas)
4. Create a knowledge/decisions/project-setup.md with a brief note that this project was initialized today and what it's for
5. Make an initial git commit with the message "chore: init project with CLAUDE.md and folder structure"

Ask me any questions you need before starting.
```

---

## What to replace

Replace the `[REPLACE THIS: ...]` section with your actual project description. Examples:

- "I'm building a Python script that processes our customer CSV exports and sends summary emails."
- "I'm managing our IT documentation — runbooks, network diagrams, and vendor contacts."
- "I'm setting up a personal knowledge management system for capturing what I learn on the job."

---

## What Claude Code will do

After you paste this prompt (with your project description filled in), Claude Code will:

1. List what's currently in your directory
2. Write a CLAUDE.md tailored to your project
3. Create the folder structure
4. Write an initial knowledge entry
5. Make the first git commit

You'll have a context-engineered project in about 2 minutes.

---

## After the bootstrap

Once your project is set up:

1. Read the CLAUDE.md Claude Code created — edit anything that's wrong or missing
2. Add something to `knowledge/learnings/` — even just one thing you learned today
3. Continue with [05 — Context Engineering](../05-context-engineering/) to understand the patterns behind what Claude Code just built

---

## Tips

- If Claude Code asks clarifying questions, answer them — the more context you give, the better the CLAUDE.md
- If you don't like something in the generated CLAUDE.md, just tell Claude Code what to change
- You can re-run this process as many times as you want on new projects
- The `knowledge/` folder is yours to fill — start capturing things immediately
