# How MCP Works

MCP stands for Model Context Protocol. It's an open standard Anthropic created so AI models can talk to external tools in a consistent way. You don't need to understand the protocol to use it — the SDK handles everything. But the mental model helps.

---

## The pieces

**The host** — Claude Code. It manages the conversation and decides when to call tools.

**The server** — your Python (or Node.js) program. It advertises what tools it has and runs them when called.

**The transport** — how they talk to each other. For local servers, this is stdio (standard input/output). The host starts your server as a subprocess and they communicate over stdin/stdout.

```
Claude Code (host)
     |
     | stdio
     v
your server.py (MCP server)
     |
     | whatever you want
     v
your database / API / files / anything
```

---

## What a tool looks like

A tool has three things:

1. **A name** — `search_notes`, `get_open_tickets`, `query_database`
2. **A description** — plain English that Claude reads to decide if this tool is relevant
3. **A function** — Python code that runs when the tool is called

The description is the most important part. Claude uses it to match your question to the right tool. Write it like you're explaining the tool to a person: "Search my personal notes by keyword. Returns matching note titles and content."

---

## The lifecycle

1. You start Claude Code in your project
2. Claude Code reads `.mcp.json` and starts your server as a subprocess
3. Your server advertises its tools (a JSON list of names + descriptions)
4. During your session, Claude decides which tools are relevant and calls them
5. Your server runs the function and returns the result
6. Claude uses the result to answer you

Your server stays running the whole session. It only stops when you exit Claude Code.

---

## What you don't need to worry about

- JSON-RPC (the wire format MCP uses) — the SDK handles it
- Starting/stopping the server — Claude Code handles it
- Parsing tool arguments — the SDK handles it

You write functions. The SDK turns them into tools. That's the whole job.

---

## Local vs. remote servers

This section covers **local servers** — they run on your machine and are only available in your Claude Code sessions. This is the right place to start.

Remote MCP servers run on a URL and can be shared across machines or users. That's a more advanced topic covered in the [official MCP documentation](https://modelcontextprotocol.io).
