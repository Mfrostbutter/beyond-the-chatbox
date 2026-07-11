# 00 — Prerequisites

Before you dive in, get these four things installed and set up. This is a one-time investment — once done, you won't need to revisit it.

**Time required:** 30-60 minutes depending on your internet speed.

---

## 1. Claude Pro ($20/month)

Claude Pro is Anthropic's subscription plan. It gives you access to Claude's most capable models and — critically — **Claude Code**, the AI coding assistant this repo is built around.

**Why you need it:** Claude Code requires either a Claude Pro subscription or a pay-as-you-go API key. Pro is the simpler path — no usage tracking, no surprise bills.

**How to set it up:**
1. Go to https://claude.ai
2. Sign in or create a free account
3. Click "Upgrade to Pro" in the sidebar
4. Enter payment info — $20/month, cancel anytime

**Pro vs. API key:**
- **Claude Pro** — $20/month flat, unlimited Claude.ai chat, includes Claude Code access. Best for most people.
- **API key** — Pay per token used. Cheaper if you use it lightly, can get expensive with heavy Claude Code use. Get one at https://console.anthropic.com.

If you're unsure, start with Pro.

---

## 2. Git

Git is the version control system that tracks changes to your files. It's required for everything in sections 02 and beyond.

**Check if you already have it:**

Open a terminal (PowerShell on Windows, Terminal on Mac) and run:
```
git --version
```
If you see a version number, you're done. Skip to step 3.

**Install Git:**

**Windows:**
1. Go to https://git-scm.com/download/win
2. Download and run the installer
3. Accept all defaults — the default options are fine
4. Open a new PowerShell window and run `git --version` to confirm

**Mac:**
1. Run `git --version` in Terminal — if Git isn't installed, macOS will prompt you to install Xcode Command Line Tools
2. Click Install and follow the prompts
3. Or install via Homebrew: `brew install git`

**Linux:**
```bash
sudo apt install git        # Ubuntu/Debian
sudo dnf install git        # Fedora
```

**After installing:**

Set your name and email (Git attaches these to every commit you make):
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## 3. VS Code

Visual Studio Code is a free code editor from Microsoft. It's the primary editor used in this repo and has excellent Claude Code integration.

**Download:** https://code.visualstudio.com

1. Go to the URL above
2. Click the download button for your operating system
3. Run the installer — accept all defaults
4. Open VS Code

**During install on Windows:** Check the box "Add to PATH" if prompted. This lets you open VS Code from the terminal with `code .`.

**Verify the install:**

Open a terminal and run:
```
code --version
```
You should see a version number.

**Extensions to install now** (open VS Code, press `Ctrl+Shift+X` or `Cmd+Shift+X`, search for each):

| Extension | Why |
|---|---|
| Claude Code | Official Anthropic extension — integrates Claude Code into the VS Code sidebar |
| GitLens | Shows git history inline — useful when reviewing AI-made changes |
| Markdown Preview Enhanced | Better rendering for CLAUDE.md and knowledge base files |

---

## 4. Docker Desktop

Docker lets you run software in isolated containers — no installation mess, no dependency conflicts. It's used in this repo for running n8n locally (section 08) and any other tools that come packaged as containers.

**Download:** https://www.docker.com/products/docker-desktop

1. Go to the URL above
2. Download for your operating system
3. Run the installer
4. Start Docker Desktop — it runs in your system tray/menu bar

**Verify the install:**

Open a terminal and run:
```
docker --version
docker run hello-world
```
The second command downloads and runs a test container. If it prints "Hello from Docker!" — you're set.

**Windows note:** Docker Desktop on Windows requires either WSL 2 (Windows Subsystem for Linux) or Hyper-V. The installer will guide you through enabling WSL 2 if needed. Follow the prompts — it's a one-time setup.

**Why Docker and not a cloud service?**
Running tools like n8n locally via Docker is free and private. No account, no subscription, your data stays on your machine. When you're ready to share with your team, you can move to a hosted option.

---

## Optional: OpenAI API account

An OpenAI API account gives you access to OpenAI's GPT models. Not required for this repo — everything here uses Claude — but useful if you want to compare models, use OpenAI in n8n workflows, or work with tools that default to it.

**Set it up:**
1. Go to https://platform.openai.com
2. Sign up and verify your email
3. Add a payment method under Billing
4. Go to API Keys and create a key
5. Store it somewhere safe — you'll add it to `.env` files, never paste it in chat

**Pricing:** Pay-as-you-go, priced per token (typically a few dollars per million input tokens, depending on the model). Typical workflow usage is cents per run. No subscription required. Check current rates at https://openai.com/api/pricing.

**When you'd use it:** n8n has native OpenAI nodes. Some community tools and templates default to OpenAI. Having the key means you can run those without modification.

---

## Also recommended: a GitHub account

GitHub is where you'll host your repos, share work, and collaborate. It's free.

1. Go to https://github.com
2. Click "Sign up"
3. Choose a username and verify your email

Once you have an account, install the GitHub CLI for managing repos from the terminal:

**Windows:** https://cli.github.com — download and run the installer

**Mac:**
```
brew install gh
```

**Authenticate:**
```
gh auth login
```
Follow the prompts to connect to your GitHub account.

---

## Checklist

Before moving to section 01, confirm:

- [ ] Claude Pro subscription active at claude.ai (or API key from console.anthropic.com)
- [ ] `git --version` returns a version number
- [ ] VS Code opens and the Claude Code extension is installed
- [ ] `docker --version` returns a version number and `docker run hello-world` works
- [ ] GitHub account created and `gh auth login` completed

Once all five are checked, you're ready. Start at [01 — Foundations](../01-foundations/).
