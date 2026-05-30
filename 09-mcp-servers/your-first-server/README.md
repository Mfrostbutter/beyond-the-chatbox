# Your First MCP Server

This is a working MCP server that gives Claude three new tools: saving notes, listing notes, and searching notes. It's intentionally simple — the goal is to understand the pattern, then build something useful for your own workflow.

---

## What you'll build

Three tools Claude can call during your sessions:

- `add_note(title, content)` — saves a note to a local JSON file
- `list_notes()` — returns all note titles
- `search_notes(keyword)` — finds notes by keyword

Once connected, you can say "save a note: decided to use Postgres for this project" and Claude will call `add_note` automatically. Later: "what did I decide about the database?" and it will call `search_notes`.

---

## Prerequisites

Python 3.10+ and the MCP SDK:

```bash
pip install mcp
```

---

## Setup

**Step 1 — Test the server runs**

```bash
cd 09-mcp-servers/your-first-server
python server.py
```

You should see no output and no errors. The server is waiting for input from Claude Code. Press Ctrl+C to stop it.

**Step 2 — Copy the MCP config to your project root**

Copy `.mcp.json` from this folder to your project's root directory (same level as `CLAUDE.md`).

Edit the `cwd` path to match where you put the server:

```json
{
  "mcpServers": {
    "personal-notes": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolute/path/to/your-first-server"
    }
  }
}
```

Use an absolute path. Relative paths can fail depending on where Claude Code is launched from.

**Step 3 — Start Claude Code**

Open Claude Code in your project directory. It reads `.mcp.json` on startup and launches the server automatically.

**Step 4 — Verify the tools are available**

Type `/mcp` in Claude Code. You should see `personal-notes` listed with its three tools.

**Step 5 — Try it**

```
Save a note: "decided to use Postgres instead of SQLite for this project because we expect > 10k rows"
```

```
What notes do I have about the database?
```

---

## How the code works

Open `server.py`. There are three parts:

**The server declaration**
```python
mcp = FastMCP("personal-notes")
```
This names your server. The name appears in `/mcp` and in Claude Code's tool list.

**The tool decorator**
```python
@mcp.tool()
def add_note(title: str, content: str) -> str:
    """Save a note..."""
```
`@mcp.tool()` registers the function as a tool. The docstring is what Claude reads to decide whether to call it. Type annotations (`str`, `int`, etc.) tell the SDK what arguments to expect.

**The function body**
Regular Python. Read a file, call an API, query a database — anything goes here.

---

## Extending this server

To add a new tool, add a new function with `@mcp.tool()`:

```python
@mcp.tool()
def delete_note(title: str) -> str:
    """Delete a saved note by its exact title."""
    notes = _load_notes()
    original_count = len(notes)
    notes = [n for n in notes if n["title"] != title]
    if len(notes) == original_count:
        return f"No note found with title: {title}"
    _save_notes(notes)
    return f"Deleted note: {title}"
```

Restart Claude Code (or reload the MCP server) after adding tools. Changes don't hot-reload.

---

## Ideas for your own server

Once you understand the pattern, replace the notes logic with something you actually need:

- **Task list** — read/write from a local markdown file or a Todoist API
- **Database query** — run read-only SQL queries against a local Postgres or SQLite database
- **Docs search** — search a folder of markdown files with keyword or semantic matching
- **Calendar** — fetch today's events from a calendar API
- **Ticket lookup** — query Jira or Linear for open tickets in a project

The pattern is always the same: one function per tool, a clear docstring, and whatever logic you need in the body.
