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

Python 3.10+ and the MCP SDK. Install the SDK into a virtual environment so it doesn't collide with other Python projects:

**Mac / Linux:**
```bash
cd 09-mcp-servers/your-first-server
python3 -m venv .venv
source .venv/bin/activate
pip install mcp
```

**Windows (PowerShell):**
```powershell
cd 09-mcp-servers\your-first-server
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install mcp
```

> If `pip install mcp` succeeds but running the server later says `No module named 'mcp'`, you installed it with a different Python than the one launching the server. Activating the venv first (as above) avoids this — the most common beginner snag.

---

## Setup

**Step 1 — Test the server runs**

With the venv still activated from the Prerequisites step:

```bash
python server.py
```

You should see no output and no errors. The server is waiting for input from Claude Code. Press Ctrl+C to stop it.

**Step 2 — Write the config**

Both tracks use the **same JSON**, just in a different place. Whichever you're on, you edit two things: point `command` at the Python **inside your venv**, and set `cwd` to this folder's absolute path. Both must be absolute paths, because the tool that launches the server does not activate your venv for you, so a bare `"python"` may not find the `mcp` module.

**Mac / Linux:**
```json
{
  "mcpServers": {
    "personal-notes": {
      "command": "/absolute/path/to/beyond-the-chatbox/09-mcp-servers/your-first-server/.venv/bin/python",
      "args": ["server.py"],
      "cwd": "/absolute/path/to/beyond-the-chatbox/09-mcp-servers/your-first-server"
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "personal-notes": {
      "command": "C:\\absolute\\path\\to\\beyond-the-chatbox\\09-mcp-servers\\your-first-server\\.venv\\Scripts\\python.exe",
      "args": ["server.py"],
      "cwd": "C:\\absolute\\path\\to\\beyond-the-chatbox\\09-mcp-servers\\your-first-server"
    }
  }
}
```

Now put that JSON in the right place for your track.

**Step 3 — Connect it (pick your track)**

**Claude Code (terminal):**
1. Copy `.mcp.json` from this folder to your project's root directory (same level as `CLAUDE.md`) and paste your edited JSON into it.
2. Start Claude Code in that project directory. It reads `.mcp.json` on startup and launches the server automatically.
3. Type `/mcp` in Claude Code. You should see `personal-notes` listed with its three tools.

**Claude Desktop:**
1. Open **Settings > Developer > Edit Config**. This opens `claude_desktop_config.json` (and creates it if it doesn't exist).
2. Paste your edited JSON into that file and save. If the file already has an `mcpServers` block, add `personal-notes` inside it rather than pasting a second one.
3. **Fully quit and reopen Claude Desktop.** It launches the server on startup; changes don't take effect until you restart.
4. In a chat, open the tools/connector menu (the `+` or the slider icon). You should see `personal-notes` and its three tools.

**Step 4 — Try it**

In a new conversation (either track):

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
