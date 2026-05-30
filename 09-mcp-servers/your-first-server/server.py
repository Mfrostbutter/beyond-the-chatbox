"""
Personal Notes MCP Server
A minimal MCP server that gives Claude the ability to save and read your notes.
"""

import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("personal-notes")

# Notes are stored in a JSON file next to this script.
NOTES_FILE = Path(__file__).parent / "notes.json"


def _load_notes() -> list[dict]:
    if not NOTES_FILE.exists():
        return []
    return json.loads(NOTES_FILE.read_text())


def _save_notes(notes: list[dict]) -> None:
    NOTES_FILE.write_text(json.dumps(notes, indent=2))


@mcp.tool()
def add_note(title: str, content: str) -> str:
    """Save a note with a title and content. Use this to capture anything
    you want Claude to be able to find later: decisions, links, reminders."""
    notes = _load_notes()
    notes.append({"title": title, "content": content})
    _save_notes(notes)
    return f"Saved note: {title}"


@mcp.tool()
def search_notes(keyword: str) -> str:
    """Search saved notes by keyword. Returns all notes whose title or
    content contains the keyword. Case-insensitive."""
    notes = _load_notes()
    if not notes:
        return "No notes saved yet."

    keyword_lower = keyword.lower()
    matches = [
        n for n in notes
        if keyword_lower in n["title"].lower() or keyword_lower in n["content"].lower()
    ]

    if not matches:
        return f"No notes found matching '{keyword}'."

    lines = []
    for note in matches:
        lines.append(f"## {note['title']}\n{note['content']}")
    return "\n\n---\n\n".join(lines)


@mcp.tool()
def list_notes() -> str:
    """List all saved note titles. Use this to see what notes exist
    before searching for a specific one."""
    notes = _load_notes()
    if not notes:
        return "No notes saved yet."
    return "\n".join(f"- {n['title']}" for n in notes)


if __name__ == "__main__":
    mcp.run()
