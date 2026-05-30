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

## What's in this section

- [How MCP Works](./how-mcp-works.md) — the protocol explained without jargon
- [Your First Server](./your-first-server/) — a working Python MCP server you can run in 10 minutes

---

## What to do next

Read [How MCP Works](./how-mcp-works.md) for a mental model, then follow [Your First Server](./your-first-server/README.md) to build one.
