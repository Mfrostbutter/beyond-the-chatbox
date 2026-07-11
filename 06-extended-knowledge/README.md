# 06 — Extended Knowledge

Extended knowledge is a system for capturing what you learn so you don't have to carry it all in your head. For AI-assisted work, it has an additional benefit: the AI can read it.

When your extended knowledge lives in a `knowledge/` folder in your project, Claude Code has access to your decisions, learnings, and context. You stop repeating yourself. The AI stops making mistakes based on things you've already figured out.

---

## What's in this section

- [Knowledge Folder Setup](./knowledge-folder-setup.md) — How to structure a knowledge/ folder Claude Code reads
- [Obsidian Integration](./obsidian-integration.md) — Using an Obsidian vault as your knowledge base
- [What to Capture](./what-to-capture.md) — What's actually worth writing down

---

## The core idea

You learn something hard — why a vendor's API has a specific quirk, which approach you tried and failed, who to call when the system breaks. That knowledge usually lives in your head, in a chat message, or nowhere.

When it lives in a markdown file in `knowledge/`, it's:
- **Persistent** — survives sessions, days, weeks
- **Searchable** — grep, GitHub search, Obsidian search
- **AI-readable** — Claude Code pulls it in as context automatically
- **Shareable** — commit it, your teammates have it too

---

## What the AI does with it

When CLAUDE.md contains:
```markdown
## References
- Decisions: `knowledge/decisions/`
- Learnings: `knowledge/learnings/`
```

**Claude Code** reads those directories before working. When you say "check if we've dealt with this before," it searches the knowledge folder. When you ask "why did we make this architectural decision," it reads `knowledge/decisions/`.

**Claude Desktop** works the same way once it can see the folder. With the [Filesystem connector](../04-ide-setup/claude-desktop-connectors.md), tell it to "check `knowledge/learnings/` before answering," or point at the folder in your Project instructions so it does this by default. The folder is identical; only the "read it" step is manual on Desktop, exactly like CLAUDE.md itself.

---

## Getting started

Start small. Create one file today:

```
knowledge/
└── learnings/
    └── first-entry.md
```

Write one thing you learned this week. That's it. The habit builds from there.
