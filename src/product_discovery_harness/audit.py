"""Static, scope-aware brownfield archaeology with durable run history."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml

from .paths import discovery_root, root


EXTENSIONS = {".py", ".js", ".ts", ".tsx", ".ex", ".rb", ".go", ".java", ".html", ".css"}


@dataclass(frozen=True)
class AuditReport:
    findings: list[dict]
    feature_inventory_path: Path
    repository_map_path: Path
    historical_report_path: Path
    index_path: Path


def _next_report_path(audits: Path, today: date) -> Path:
    sequence = 1
    while True:
        path = audits / f"{today.isoformat()}-{sequence:03d}-repository-audit.md"
        if not path.exists():
            return path
        sequence += 1


def _render_report(findings: list[dict], scope: dict, today: date) -> str:
    lines = [
        f"# Repository audit — {today.isoformat()}", "",
        "This is provisional, static repository evidence. It does not confirm product intent or modify application code.", "",
        "## Scope", f"- Include: `{', '.join(scope.get('include', ['.']))}`", f"- Exclude: `{', '.join(scope.get('exclude', []))}`", "",
        "## Current snapshot", "- [Feature inventory](../current-state/feature-inventory.yml)", "- [Repository map](../current-state/repository-map.md)", "",
        "## Findings", "", "| ID | Title | Classification | Evidence | Confidence |", "| --- | --- | --- | --- | --- |",
    ]
    for finding in findings:
        evidence = finding["evidence"]["modules"][0]
        lines.append(f"| {finding['id']} | {finding['title']} | {finding['classification']} | `{evidence}` | {finding['confidence']} |")
    if not findings:
        lines.append("| — | No scoped source files found | — | — | — |")
    return "\n".join(lines) + "\n"


def _write_index(audits: Path) -> Path:
    reports = sorted(audits.glob("*-repository-audit.md"), reverse=True)
    lines = ["# Repository audit history", "", "Historical static-audit evidence. The current snapshot is in [`../current-state/`](../current-state/).", ""]
    if reports:
        lines.extend(["## Reports", ""])
        lines.extend(f"- [{path.stem}](./{path.name})" for path in reports)
    else:
        lines.append("No audit reports have been recorded yet.")
    path = audits / "README.md"
    path.write_text("\n".join(lines) + "\n")
    return path


def audit_repository(repo: str | Path, today: date | None = None) -> AuditReport:
    """Refresh the current snapshot and preserve an immutable historical report."""
    base = root(repo)
    cfg = yaml.safe_load((base / "product-harness.yml").read_text()) or {}
    scope = cfg.get("repository_scope", {})
    excluded = set(scope.get("exclude", []))
    findings: list[dict] = []
    for path in base.rglob("*"):
        if not path.is_file() or path.suffix not in EXTENSIONS or set(path.relative_to(base).parts).intersection(excluded):
            continue
        kind = "user_feature" if any(item in path.name.lower() for item in ("page", "screen", "route", "view")) else "internal_capability"
        findings.append({"id": f"CURRENT-{len(findings) + 1:03d}", "title": path.stem.replace("_", " "), "classification": kind, "source": "observed", "status": "exploring", "confidence": "medium", "evidence": {"modules": [str(path.relative_to(base))], "runtime_verified": False}})

    discovery = discovery_root(base)
    current_state = discovery / "current-state"
    current_state.mkdir(parents=True, exist_ok=True)
    feature_inventory_path = current_state / "feature-inventory.yml"
    repository_map_path = current_state / "repository-map.md"
    feature_inventory_path.write_text(yaml.safe_dump({"features": findings}, sort_keys=False))
    repository_map_path.write_text("# Repository map\n\n" + "\n".join(f"- `{finding['evidence']['modules'][0]}`" for finding in findings) + "\n")

    audits = discovery / "audits"
    audits.mkdir(parents=True, exist_ok=True)
    run_date = today or date.today()
    historical_report_path = _next_report_path(audits, run_date)
    historical_report_path.write_text(_render_report(findings, scope, run_date))
    index_path = _write_index(audits)
    return AuditReport(findings, feature_inventory_path, repository_map_path, historical_report_path, index_path)
