"""Concise discovery session persistence."""
from __future__ import annotations
from datetime import date
from pathlib import Path
from .paths import discovery_root

SECTIONS = ["Focus", "Context entering the session", "Discussion summary", "Ideas raised", "Assumptions identified", "Candidate decisions", "Accepted decisions", "Rejected alternatives", "Open questions", "Contradictions or tensions", "Documents updated", "Recommended next focus"]
def create_session(repo: str | Path, focus: str, summary: str = "") -> Path:
    folder=discovery_root(repo)/"sessions"; folder.mkdir(parents=True, exist_ok=True)
    stem=f"{date.today().isoformat()}-01-{focus.lower().replace(' ', '-')[:40]}"; path=folder/f"{stem}.md"; index=1
    while path.exists(): index += 1; path=folder/f"{date.today().isoformat()}-{index:02d}-{focus.lower().replace(' ', '-')[:40]}.md"
    text=f"# Session: {focus}\n\n" + "\n".join(f"## {s}\n{summary if s == 'Discussion summary' else ''}" for s in SECTIONS) + "\n"
    path.write_text(text); return path
