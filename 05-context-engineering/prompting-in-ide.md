# Prompting in the IDE

You've set up Claude Code and created a CLAUDE.md. Now you're typing instructions in the terminal. How you prompt matters — but not in the same way as in web chat.

---

## The key difference from web chat

In web chat, you need to provide all the context in your message. In Claude Code, the context is already there — in your files, your CLAUDE.md, your git history. You don't need to re-explain. You just need to give clear instructions.

This means your prompts can (and should) be shorter and more task-focused.

---

## Give tasks, not questions

**Web chat style (less effective in IDE):**
> "Can you help me understand how to add error handling to my Python script?"

**IDE style (more effective):**
> "Add error handling to src/export-processor/main.py — catch file not found errors and log them to a file instead of crashing."

In the IDE, Claude Code can read the file. You don't need to explain what's in it. Just tell it what to do.

---

## Reference files by path

Be specific about which files you're talking about.

**Vague:**
> "Update the main script to handle the new CSV format."

**Specific:**
> "Update `src/export-processor/main.py` to handle the new CSV format described in `docs/data-schema.md`."

Claude Code can read both files and make exactly the right change.

---

## Use the context you've already built

Your knowledge folder is there to be used. Reference it.

> "I'm about to change how the email sender works. Before making changes, read `knowledge/decisions/` to understand why we made the current design choices."

> "Check `knowledge/learnings/csv-encoding-issues.md` before touching any CSV processing code."

---

## Multi-step tasks

Claude Code handles multi-step tasks well. You can give it a full workflow:

> "Do the following:
> 1. Read `docs/data-schema.md` to understand the expected format
> 2. Update `src/export-processor/main.py` to validate incoming data against that schema
> 3. Add a test case in `tests/` with sample invalid data
> 4. Update `src/export-processor/README.md` with notes about the validation logic
> 5. Commit everything with the message 'feat: add schema validation to export processor'"

It will work through these steps in order and ask if it hits anything unclear.

---

## Ask for a plan first

For larger changes, ask Claude Code to describe what it's going to do before doing it:

> "Before making any changes: read the current state of `src/` and describe your plan for refactoring the export processor to support multiple input formats. I want to review the plan before you start."

This is the most reliable way to avoid surprises.

---

## Be explicit about what you don't want

If you have constraints, state them:

> "Refactor `src/export-processor/main.py` to be more readable — but don't change the function signatures, and don't add any new dependencies."

> "Update the README — don't touch any code files."

---

## Use `/` commands

> **Claude Code.** These slash commands are terminal commands. In **Claude Desktop**, the equivalents live in menus and buttons (start a **New chat** instead of `/clear`; usage shows against your plan rather than `/cost`). The prompting advice above this section applies to both tracks equally.

Claude Code has built-in slash commands:

| Command | What it does |
|---|---|
| `/help` | List available commands |
| `/clear` | Clear the conversation context (start fresh) |
| `/cost` | Show token usage for this session |
| `/compact` | Summarize the conversation to save context space |
| `/memory` | View what's in persistent memory |

---

## Reviewing what the AI did

After Claude Code makes changes:

1. Look at the diff in VS Code (`Ctrl+Shift+G` to open Source Control)
2. Read the changed files — don't just accept
3. If something looks wrong, tell it: "That's not quite right — the function should return a list, not a string"
4. Commit when you're satisfied

The goal isn't to rubber-stamp everything the AI does. It's to do the review work, not the typing work.

---

## When to break out of the IDE and use web chat

- Quick conceptual questions: "What's the difference between async and sync Python?"
- Exploring options before committing: "What are three approaches I could take to solve this problem?"
- Sensitive work where you don't want file access

You don't have to choose one tool. Use what fits the moment.
