# Git Fundamentals

Git is a version control system. It tracks changes to files over time so you can see what changed, when, and why — and roll back if something breaks.

GitHub is a website that hosts Git repositories and adds collaboration features (pull requests, issues, code review, Actions).

---

## The core concepts

### Repository (repo)
The project folder, tracked by Git. It contains your files plus a hidden `.git/` folder that stores the entire history. When you "clone a repo," you're copying the project and its full history to your machine.

**Real-world analogy:** A repo is like a Google Drive folder, except it remembers every version of every file you've ever saved.

### Commit
A saved snapshot of the project at a specific point in time. Each commit has a message describing what changed ("add CLAUDE.md with project context") and a timestamp.

**Real-world analogy:** A commit is like hitting "save" in a video game — you can always come back to this exact state.

### Branch
A parallel version of the project. When you create a branch, you're working on a copy that doesn't affect the main version until you decide to merge it.

The default branch is usually called `main`. Feature branches are usually named for what they're adding (`feature/new-agent` or `fix/broken-link`).

**Real-world analogy:** A branch is like making a photocopy of a document to try edits on, before committing to the changes on the original.

### Merge
Combining the changes from one branch into another. When your feature is ready, you merge it into `main`.

Here's a branch splitting off `main`, getting its own commits, then merging back:

```mermaid
gitGraph
    commit id: "initial setup"
    commit id: "add README"
    branch feature/new-agent
    checkout feature/new-agent
    commit id: "draft agent"
    commit id: "refine agent"
    checkout main
    merge feature/new-agent id: "merge PR"
    commit id: "next change"
```

`main` keeps moving in a straight line. Your branch is a detour that rejoins it once the work is reviewed and merged.

### Pull Request (PR)
A proposal to merge your branch's changes into another branch, usually `main`. PRs let teammates review changes before they're merged. On GitHub, PRs show a diff (what changed), support comments, and require approvals.

**Why it matters for AI:** Claude Code creates commits and can open PRs. Understanding what a PR is helps you review what the AI did before merging.

### Clone
Copying a repo from GitHub (or another remote) to your local machine. Creates a local working copy with full history.

```
git clone https://github.com/username/repo-name
```

### Push / Pull
- **Push:** Send your local commits to the remote (GitHub)
- **Pull:** Download new commits from the remote to your local machine

```mermaid
flowchart LR
    subgraph local["💻 Your machine (local)"]
        L["Local repo"]
    end
    subgraph remote["☁️ GitHub (remote)"]
        G["Remote repo"]
    end
    L -->|"git push"| G
    G -->|"git pull"| L
```

`clone` is the one-time first copy from GitHub to your machine. After that, `push` and `pull` keep the two in sync.

### .gitignore
A file that tells Git which files to ignore — secrets, credentials, build artifacts, OS files. Always add `.env` files (which contain API keys) to `.gitignore`.

---

## Common Git commands

You don't need to memorize these. Claude Code can run them for you. But knowing what they do helps you understand what's happening.

```bash
# Start tracking a folder with Git
git init

# See what's changed since the last commit
git status

# Stage a file to be included in the next commit
git add filename.md

# Stage all changed files
git add .

# Create a commit with a message
git commit -m "add CLAUDE.md with project context"

# See the commit history
git log --oneline

# Create a new branch
git checkout -b feature/new-agent

# Switch to an existing branch
git checkout main

# Push your commits to GitHub
git push origin main

# Pull new changes from GitHub
git pull
```

---

## The workflow in practice

Day-to-day, working with Git looks like this:

```mermaid
flowchart LR
    A["⬇️ Pull<br/>latest changes"] --> B["🌿 Create<br/>a branch"]
    B --> C["✏️ Make<br/>changes"]
    C --> D["💾 Stage &amp;<br/>commit"]
    D --> E["⬆️ Push<br/>to GitHub"]
    E --> F["🔀 Open<br/>a PR"]
    F --> G["✅ Review<br/>&amp; merge"]
    G -.->|next task| A
```

1. **Pull** to get the latest changes from your team
2. **Create a branch** for your new work
3. **Make changes** (edit files, add new ones)
4. **Stage and commit** your changes with a clear message
5. **Push** your branch to GitHub
6. **Open a PR** to propose merging into `main`
7. Get reviewed, merge

With Claude Code in the loop, steps 3-5 often happen automatically. The AI edits files, stages them, and commits them. Your job is to review what it did and decide whether to push.

---

## What makes a good commit message

Good:
- `add researcher agent for project kickoffs`
- `fix broken YouTube link in foundations section`
- `update CLAUDE.md with automation platform notes`

Bad:
- `stuff`
- `update`
- `WIP`

A good commit message answers: "What changed, and why?" You should be able to read the git log six months from now and understand what each commit did.
