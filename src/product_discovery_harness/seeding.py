"""Safe target-contract seeding."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import shutil
import yaml
from .detection import detect_mode
from .paths import package_root, root

MARKER = "<!-- product-discovery-harness:seeded -->"
@dataclass
class SeedReport:
    mode: str; status: str; created: list[str] = field(default_factory=list); preserved: list[str] = field(default_factory=list); updated: list[str] = field(default_factory=list); evidence: list[str] = field(default_factory=list)

def template_root() -> Path: return package_root() / "templates" / "target"
def _placeholder(text: str) -> bool: return not text.strip() or MARKER in text or text.strip() in {"# Product Sense", "# Experience Sense"}
def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True); temp=path.with_suffix(path.suffix+".tmp"); temp.write_text(content); temp.replace(path)

def seed_target(target: str | Path, mode: str = "auto", include: list[str] | None = None, exclude: list[str] | None = None) -> SeedReport:
    destination=root(target); destination.mkdir(parents=True, exist_ok=True)
    detection=detect_mode(destination, mode)
    selected=detection.mode
    report=SeedReport(selected, detection.status, evidence=detection.evidence)
    for rel_dir in (Path("docs/product-specs"),):
        (destination / rel_dir).mkdir(parents=True, exist_ok=True)
    for source in template_root().rglob("*"):
        if source.is_dir(): continue
        rel=source.relative_to(template_root())
        # The two durable summaries live under docs in a target; templates keep
        # them at the target-template root for a readable distribution layout.
        target_rel = rel if rel.name == "product-harness.yml" and len(rel.parts) == 1 else Path("docs") / rel
        dest=destination/target_rel
        if dest.exists() and dest.is_dir(): report.preserved.append(str(rel)); continue
        content=source.read_text()
        if rel.name == "product-harness.yml":
            data=yaml.safe_load(content); data["mode"] = selected; data["mode_detection"]={"status": detection.status, "evidence": detection.evidence}; data["repository_scope"]["include"] = include or ["."]; data["repository_scope"]["exclude"] = exclude or data["repository_scope"]["exclude"]; content=yaml.safe_dump(data, sort_keys=False)
        if rel.name == "STATUS.md":
            phase = "repository-reconnaissance" if selected == "brownfield" else "product-purpose-exploration" if selected == "greenfield" else "mode-selection"
            content=content.replace("{{MODE}}", selected).replace("{{PHASE}}", phase)
        if not dest.exists(): _write(dest, content); report.created.append(str(target_rel))
        elif _placeholder(dest.read_text()): _write(dest, content); report.updated.append(str(target_rel))
        else: report.preserved.append(str(target_rel))
    return report
