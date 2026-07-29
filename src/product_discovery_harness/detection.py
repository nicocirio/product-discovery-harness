"""Conservative repository mode detection."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

APPLICATION_DIRS = {"src", "app", "apps", "lib", "server", "client", "web"}
MANIFESTS = {"package.json", "mix.exs", "pyproject.toml", "Cargo.toml", "go.mod", "Gemfile"}
ENTRYPOINTS = {"manage.py", "main.py", "main.ts", "main.js", "router.ex", "routes.rb"}
IGNORED = {".git", "node_modules", "deps", "dist", "build", "vendor", ".venv", "__pycache__"}

@dataclass(frozen=True)
class Detection:
    mode: str
    status: str
    evidence: list[str]

def detect_mode(repo: str | Path, explicit_mode: str = "auto") -> Detection:
    if explicit_mode not in {"auto", "greenfield", "brownfield"}:
        raise ValueError("mode must be auto, greenfield, or brownfield")
    if explicit_mode != "auto":
        return Detection(explicit_mode, "confirmed", ["explicit mode selection"])
    root = Path(repo)
    names = {p.name for p in root.iterdir() if p.name not in IGNORED} if root.exists() else set()
    dirs = {p.name for p in root.iterdir() if p.is_dir() and p.name not in IGNORED} if root.exists() else set()
    files = [p for p in root.rglob("*") if p.is_file() and not set(p.parts).intersection(IGNORED)] if root.exists() else []
    evidence: list[str] = []
    if names.intersection(MANIFESTS): evidence.append("framework manifest detected")
    if dirs.intersection(APPLICATION_DIRS): evidence.append("application source directory detected")
    if any(p.name in ENTRYPOINTS for p in files): evidence.append("application entrypoint detected")
    if any("test" in p.name.lower() for p in files): evidence.append("application test files detected")
    source_files = [p for p in files if p.suffix in {".py", ".js", ".ts", ".tsx", ".ex", ".rb", ".go", ".java"}]
    if len(source_files) >= 3 and len(evidence) >= 2:
        return Detection("brownfield", "suggested", evidence)
    if not names:
        return Detection("greenfield", "suggested", ["repository is empty"])
    if not evidence:
        return Detection("greenfield", "suggested", ["no substantive application signals detected"])
    return Detection("pending", "pending", evidence + ["signals are insufficient to classify a mature product"])
