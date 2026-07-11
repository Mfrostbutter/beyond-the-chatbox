# Writing Your CLAUDE.md

Use this guide to create your own CLAUDE.md from scratch. Fill in the sections below, following the prompts.

---

## The fast way: let Claude Code draft it

If you already have Claude Code set up (section 04) and an existing project folder, don't start from a blank page. Open Claude Code in the project and run:

```
/init
```

Claude Code scans your files and writes a first-draft `CLAUDE.md` for you — mission, structure, and any conventions it can infer. It's rarely perfect, but it turns "stare at an empty file" into "edit a solid draft."

Then use the rest of this guide to sharpen it: tighten the mission, add your real non-negotiables, and fix the folder descriptions. **`/init` gets you 70% there; the sections below get you the last 30%, which is the part that actually changes how the AI behaves.**

Brand new project with no files yet? Skip `/init` and fill in the template by hand, starting with Step 1.

---

## Step 1: Mission

Write one sentence. What is this project? What does it produce or manage?

```
## Mission
[One sentence describing what this project is and what it does.]
```

Examples:
- "A set of Python scripts that process weekly sales data and email reports to the team."
- "Documentation and runbooks for managing our office network infrastructure."
- "A personal system for capturing what I learn on the job and making it searchable."

**Rule:** If you can't describe it in one sentence, you don't have a clear enough project definition yet. Clarify that first.

---

## Step 2: Non-Negotiables

List 3-7 rules. These are things the AI must always or never do. Think about:

- Security rules (never hardcode credentials)
- File management rules (archive vs delete)
- Code quality rules (syntax-check before deploying)
- Documentation rules (update docs when X changes)
- Scope rules (don't modify production without testing)

```
## Non-Negotiables
- [Rule 1]
- [Rule 2]
- [Rule 3]
```

**Starter rules you can customize:**
```
- Never hardcode API keys or credentials — use .env files
- Archive instead of delete — retired files go to Archive/, not the trash
- Always test with sample data before touching real data
- Update docs/ when making significant changes
- Make git commits with clear messages: what changed and why
```

---

## Step 3: Directory Structure

List each folder with a one-line description. The AI uses this to know where things belong.

```
## Directory Structure
- `src/` — [what goes here]
- `docs/` — [what goes here]
- `knowledge/` — extended knowledge: decisions, learnings, contacts
- `Archive/` — retired files (never delete, move here)
```

**Standard starter structure** (matches the template in `07-repo-template/`):
```
## Directory Structure
- `src/` — main code and scripts
- `prototypes/` — experiments (nothing in src/ imports from here)
- `docs/` — architecture notes and runbooks
- `knowledge/` — extended knowledge: decisions, learnings, contacts
- `Archive/` — retired files (move here, never delete)
```

---

## Step 4: Load-on-Demand References

Point to detailed docs. Don't paste the docs in. Keep CLAUDE.md short.

```
## References
- [Topic]: `path/to/doc.md`
- [Topic]: `path/to/other-doc.md`
```

Examples:
```
## References
- Data schema: `docs/data-schema.md`
- Deployment steps: `docs/deploy.md`
- Vendor contacts: `knowledge/contacts/vendors.md`
```

Skip this section if your project is simple and doesn't have separate docs yet. Add it as your project grows.

---

## Putting it together

Here's the full template. Fill in the placeholders:

```markdown
# [your-project-name] — Claude Code Context

Last updated: [today's date]

## Mission
[One sentence describing what this project is and what it does.]

## Non-Negotiables
- Never hardcode API keys or credentials — use .env files
- Archive instead of delete — retired files go to Archive/, not the trash
- [Add your rules here]

## Directory Structure
- `src/` — [what goes here]
- `docs/` — [what goes here]
- `knowledge/` — extended knowledge: decisions, learnings, contacts
- `Archive/` — retired files

## References
- [Add links to detailed docs here, or delete this section if not needed]
```

---

## Tips

**Keep it short.** A CLAUDE.md that's too long doesn't get read carefully. Aim for under 50 lines. Point to docs, don't inline them.

**Be specific about rules.** "Be careful" is not a rule. "Syntax-check Python with `python3 -m py_compile` before running on production files" is a rule.

**Update it.** Every time you learn something the AI keeps getting wrong, add a rule. CLAUDE.md is a living document.

**Ask Claude Code to write it.** Paste the bootstrap prompt from `04-ide-setup/bootstrap-prompt.md` and let Claude Code draft the CLAUDE.md based on your description. Then edit it.

---

## Common mistakes

**Too much prose.** Don't write paragraphs explaining your background and philosophy. Write structured lists.

**Putting secrets in it.** Never. CLAUDE.md goes in Git. Git goes on GitHub. Secrets go in `.env` files that are in `.gitignore`.

**Making it a README.** README is for humans on GitHub. CLAUDE.md is for the AI in your terminal. Different audiences, different content.

**Never updating it.** CLAUDE.md should evolve as your project grows. When you add a new folder or learn a new rule, update it immediately.
