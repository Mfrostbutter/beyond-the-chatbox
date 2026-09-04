# 02 — GitHub Basics

GitHub is where code lives. It's also where AI-assisted work lives — agents commit changes, PRs get reviewed with AI help, and your project history becomes searchable context for future work.

You don't need to become a Git expert to get value here. You need to understand the concepts well enough to not be confused when AI tools reference them.

This section covers:

- [Git Fundamentals](./git-fundamentals.md) — Repos, commits, branches, PRs — the core concepts
- [GitHub for AI Workflows](./github-for-ai-workflows.md) — How AI teams use GitHub day-to-day
- [Resources](./resources.md) — The best places to learn more

---

## Why GitHub matters for AI work

**Version control for everything, not just code.** Modern AI workflows involve CLAUDE.md files, agent definitions, knowledge base entries, and prompt libraries. All of these benefit from version history — you can see what changed, why, and roll back if needed.

**Your project history is AI context.** When Claude Code runs `git log`, it understands what changed recently and why. A well-maintained commit history is free context engineering.

**Collaboration at scale.** As you build AI workflows, you'll want to share them. GitHub makes it easy to share a repo with your team, accept improvements, and track issues.

**GitHub Actions for automation.** You can trigger AI workflows automatically when code is pushed, issues are created, or PRs are opened. This is how "AI in the development pipeline" works in practice.

---

## The mental model

Think of Git like a very detailed save history for your project:

- **Repository (repo):** The project folder, including its entire history
- **Commit:** A saved snapshot — "at this point in time, this is what everything looked like"
- **Branch:** A parallel version of the project you can work on without affecting the main version
- **Pull Request (PR):** A proposal to merge your branch's changes into the main version

That's 90% of what you need to know to get started. The rest is details.

Visually, those four concepts fit together like this:

```mermaid
flowchart TB
    subgraph Repo["📁 Repository — the whole project + its full history"]
        direction TB
        Start["💾 first commit"]
        subgraph mainlane["🌳 main · the official version"]
            direction TB
            M1["💾 commit"] --> M2["💾 latest"]
        end
        subgraph featlane["🌿 branch · your safe copy"]
            direction TB
            B1["💾 commit"] --> B2["💾 commit"]
        end
        Start -->|stays on main| M1
        Start -->|branch off| B1
        B2 -->|open PR, merge| M2
    end
```

Read it top to bottom, like a timeline. You start from a commit on `main`, **branch off** into a safe copy, **commit** your changes there, then open a **Pull Request** to merge the branch back into `main` — which becomes the new latest. While you experiment on the branch, `main` stays intact until the work is reviewed and ready.

---

## What to do next

1. Read [Git Fundamentals](./git-fundamentals.md) — takes about 10 minutes
2. Create a free GitHub account at github.com if you don't have one
3. Try GitHub Skills at skills.github.com — free, browser-based, no install required
4. Come back here after completing section 04 (IDE Setup) and try your first commit from Claude Code

Then move to [03 — AI Tools Landscape](../03-ai-tools-landscape/).
