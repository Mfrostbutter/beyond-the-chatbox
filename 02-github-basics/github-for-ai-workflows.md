# GitHub for AI Workflows

GitHub isn't just for code. For teams using AI tools, it becomes the hub for everything — agent definitions, CLAUDE.md files, prompt libraries, knowledge bases, and automation scripts.

---

## What AI teams store in GitHub

**CLAUDE.md files**
The context documents that tell Claude Code about your project. Version-controlled means you can see exactly when you added a rule, why you changed it, and what the project context looked like six months ago.

**Agent definitions**
The `.claude/agents/` files that define what specialized agents can do. These are text files — they belong in Git just like code does.

**Knowledge base entries**
The `knowledge/` folder documents. As you capture decisions, learnings, and contacts, commit them. This creates a searchable, version-controlled institutional memory.

**Prompt libraries**
Reusable prompts that work well for specific tasks. Store them in `resources/prompt-library.md` or similar, commit them, share them with your team.

**n8n workflow exports**
n8n can export workflows as JSON. Commit those exports so you can restore workflows, review changes, and share them with teammates.

---

## GitHub features worth knowing

### Issues
The GitHub issue tracker. Use it to capture bugs, feature requests, and tasks. When Claude Code references an issue number in a commit message (`fix #42 broken link`), GitHub automatically links the commit to the issue.

**AI use:** You can ask Claude Code to create issues, reference them in commits, and close them when work is done.

### GitHub Actions
Automated workflows that run when something happens in your repo — a push, a PR, a schedule. You can use Actions to:
- Run tests automatically when code is pushed
- Deploy a site when you merge to main
- Trigger an n8n workflow when an issue is created
- Summarize a PR with Claude when it's opened

Not required for beginners, but worth knowing they exist.

### GitHub Copilot
Microsoft's AI coding assistant, built into VS Code and JetBrains IDEs. Powered by OpenAI models. Suggests code as you type (autocomplete) and can chat in a sidebar.

**Claude Code vs. Copilot:** Copilot is better for autocomplete while typing. Claude Code is better for larger tasks — refactoring, creating files, understanding the whole codebase, and multi-step work.

### GitHub Discussions
Like a forum attached to your repo. Good for longer-form questions, ideas, and knowledge sharing with collaborators.

---

## The AI-assisted PR review workflow

When Claude Code opens a PR, a common workflow looks like this:

```mermaid
sequenceDiagram
    participant You
    participant Claude as Claude Code
    participant GH as GitHub
    Claude->>Claude: make changes, commit to a branch
    Claude->>GH: push branch & open PR
    You->>GH: review the diff
    opt ask for a second opinion
        You->>Claude: "review this PR, list any issues"
        Claude-->>You: feedback on the diff
    end
    alt looks good
        You->>GH: approve & merge
        GH->>GH: delete branch, changes land in main
    else needs work
        You->>Claude: request revisions
    end
```

1. Claude Code makes changes and commits them to a branch
2. Claude Code (or you) pushes the branch and opens a PR on GitHub
3. You review the diff — what changed, why, does it look right?
4. Optional: ask Claude "review this PR and list any issues" — it reads the diff and gives feedback
5. Approve and merge, or ask for revisions
6. The branch gets deleted, changes land in main

This keeps humans in the loop for every significant change, even when AI is doing the work.

---

## GitHub vs. local Git

| Local Git | GitHub |
|---|---|
| Lives on your machine | Lives in the cloud |
| No account needed | Requires an account |
| No collaboration features | PRs, issues, discussions |
| Private by default | Public or private repos |
| Command-line or GUI | Web UI + command-line |

Think of local Git as your working copy and GitHub as the backup + collaboration layer.

---

## Setting up your first GitHub repo

1. Create an account at github.com
2. Click "New repository"
3. Name it, choose public or private, check "Add a README"
4. Copy the clone URL
5. In your terminal: `git clone <url>`
6. Open the folder in VS Code

That's it. You have a version-controlled project connected to GitHub.
