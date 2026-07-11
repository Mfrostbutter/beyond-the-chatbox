# Installing Claude Code

Claude Code is Anthropic's official CLI and IDE extension for working with Claude in your projects. It runs in your terminal and can be embedded in VS Code.

---

## Step 1: Install Node.js

Claude Code requires Node.js 18 or higher.

**Check if you already have it:**
```bash
node --version
```
If you see `v18.0.0` or higher, skip to Step 2.

**Install Node.js:**
1. Go to https://nodejs.org
2. Download the LTS (Long Term Support) version
3. Run the installer — accept all defaults
4. Open a new terminal and run `node --version` to confirm

---

## Step 2: Install Claude Code

Open your terminal (Terminal on Mac/Linux, PowerShell or Command Prompt on Windows) and run:

```bash
npm install -g @anthropic-ai/claude-code
```

The `-g` flag installs it globally so you can run it from any directory.

**Verify the install:**
```bash
claude --version
```

---

## Step 3: Choose how you'll pay for it

You have two options. Most people should use the subscription.

**Option A — Claude subscription (recommended).** Claude Code is included with **Claude Pro** ($20/month) and **Claude Max** (from $100/month). If you set up Claude Pro back in section 00, you already have access. No API key needed — you'll log in with your Claude.ai account in the next step.

**Option B — Anthropic API key (pay as you go).** Bills per use through the Console instead of a flat monthly fee. Useful if you don't have a subscription or expect very light usage.

1. Go to https://console.anthropic.com
2. Sign in or create an account
3. Click "API Keys" in the left sidebar
4. Click "Create Key" and name it (e.g., "claude-code-personal")
5. Copy the key — it starts with `sk-ant-...`

> Keep this key private. Treat it like a password. Don't paste it into chat windows or commit it to GitHub.

---

## Step 4: Sign in

Run Claude Code for the first time:

```bash
claude
```

It will ask how you want to log in:

- **Subscription (Option A):** choose the Claude.ai login. Your browser opens, you approve, and you're in. No key to copy or store.
- **API key (Option B):** paste the `sk-ant-...` key when prompted.

Once you're signed in, you'll see the Claude Code prompt. Type `/help` to see available commands, or just start typing to have a conversation.

---

## Step 5: Test it

Navigate to a folder you want to work in:

```bash
cd ~/Documents/my-project
claude
```

Type: `What files are in this directory?`

Claude Code will list them. If it works, you're set.

---

## Common issues

**"command not found: claude"**
Close your terminal and open a new one. If still not working, the npm global bin directory may not be on your PATH. Run `npm bin -g` to find the path and add it to your shell config.

**API key not accepted**
Double-check that you copied the full key (starting with `sk-ant-`). API keys are long — make sure nothing got cut off.

**Permission errors on Mac/Linux**
If npm install fails with permission errors, try:
```bash
sudo npm install -g @anthropic-ai/claude-code
```
Or use nvm (Node Version Manager) which avoids permission issues entirely.

---

## Next: VS Code Setup

Continue to [vscode-setup.md](./vscode-setup.md) to integrate Claude Code with VS Code.
