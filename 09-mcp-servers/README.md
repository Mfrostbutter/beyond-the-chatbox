# 09 — MCP Servers

MCP (Model Context Protocol) is how you give Claude new tools.

By default, Claude Code can read files, run shell commands, and search your codebase. MCP lets you extend that with anything you can write a function for: query a database, search your notes app, call an API, read a Slack channel. Any Python or Node function can become a tool Claude uses in conversation.

---

## How it works

An MCP server is a small program that runs alongside Claude Code. It exposes a list of tools with names and descriptions. When Claude decides a tool is relevant, it calls the server, gets the result, and uses it to answer you.

```
You: "What did I decide about the database schema last week?"
Claude: [calls your notes MCP server] → finds the relevant note → answers
```

The server runs locally. Your data never leaves your machine unless you explicitly write a server that sends it somewhere.

---

## When to build an MCP server

Build one when you find yourself repeatedly giving Claude the same context that lives somewhere else:

- "Here's my task list from Notion: ..."
- "Here's the current database schema: ..."
- "Here are the open tickets from Jira: ..."

If you're pasting that context into every session, an MCP server can pull it in automatically.

Don't build one for things Claude Code already does well: reading your local files, running commands, editing code. Those are built-in tools. MCP fills the gaps.

---

## Start by using one, not building one

Before you write any code, know this: you rarely have to. There's a large ecosystem of ready-made MCP servers for common tools (GitHub, Slack, Postgres, Google Drive, Notion, and many more). How you add one depends on your track from [section 04](../04-ide-setup/).

**Claude Code (terminal).** Adding a server is a single command:

```bash
claude mcp add --help
```

For example, to add a filesystem server that lets Claude work with a specific folder:

```bash
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /path/to/folder
```

Then type `/mcp` inside Claude Code to confirm it's connected and see its tools.

**Claude Desktop.** You've already done this once. The Filesystem connector you set up in [section 04](../04-ide-setup/claude-desktop-connectors.md) *is* an MCP server. To add more, open **Settings > Connectors** (or the `+` menu in a chat) and browse the directory. Many popular servers install with one click as **Extensions**. Custom or local servers (like the one you'll build next) are added by editing a config file instead, covered in the build guide below.

Either way, browse what exists before assuming you need to build.

**Build your own only when nothing off the shelf fits** — usually because the data lives in your own files, your own database, or an internal tool. That's what the rest of this section walks through.

---

## What's in this section

- [How MCP Works](./how-mcp-works.md) — the protocol explained without jargon
- [Your First Server](./your-first-server/) — a working Python MCP server you can run in 10 minutes

---

## What to do next

Read [How MCP Works](./how-mcp-works.md) for a mental model. Try adding a prebuilt server with `claude mcp add` above. Then, when you have a need nothing off the shelf covers, follow [Your First Server](./your-first-server/README.md) to build one.
