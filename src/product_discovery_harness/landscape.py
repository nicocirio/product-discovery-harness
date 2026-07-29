"""Generate a non-canonical, review-oriented product landscape."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from .paths import discovery_root, root

INDEXES = (
    ("opportunity", "docs/product-discovery/opportunities/index.yml", "opportunities"),
    ("feature", "docs/product-discovery/features/index.yml", "features"),
)
STALE_STATUSES = {"raw", "exploring", "candidate", "accepted", "deferred"}
NEXT_ACTIONS = {
    "raw": "Clarify the idea",
    "exploring": "Continue discovery",
    "candidate": "Confirm or revise",
    "accepted": "Choose the next product step",
    "deferred": "Review when the stated trigger arrives",
    "rejected": "Closed — retain rationale",
    "superseded": "Closed — follow replacement",
}


@dataclass(frozen=True)
class LandscapeItem:
    record_type: str
    identifier: str
    title: str
    status: str
    path: str | None
    path_exists: bool
    last_reviewed_at: date | None
    review_after: date | None



@dataclass(frozen=True)
class LandscapeReport:
    path: Path
    record_count: int
    stale_count: int
    missing_document_count: int
    changed: bool


def _parse_date(value: Any, field: str, identifier: str) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, date):
        return value
    if not isinstance(value, str):
        raise ValueError(f"{identifier}.{field} must be an ISO date")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{identifier}.{field} must use YYYY-MM-DD") from exc


def _relative_path(base: Path, value: Any, identifier: str) -> tuple[str | None, bool]:
    if value in (None, ""):
        return None, False
    if not isinstance(value, str):
        raise ValueError(f"{identifier}.path must be a target-relative string")
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError(f"{identifier}.path must stay inside the target repository")
    resolved = (base / candidate).resolve()
    if base not in (resolved, *resolved.parents):
        raise ValueError(f"{identifier}.path must stay inside the target repository")
    return candidate.as_posix(), resolved.is_file()


def load_index_records(repo: str | Path) -> list[LandscapeItem]:
    """Read records from their canonical indexes without changing them."""
    base = root(repo)
    items: list[LandscapeItem] = []
    for record_type, relative_index, key in INDEXES:
        index_path = base / relative_index
        if not index_path.exists():
            continue
        data = yaml.safe_load(index_path.read_text()) or {}
        records = data.get(key, [])
        if not isinstance(records, list):
            raise ValueError(f"{relative_index}.{key} must be a list")
        for record in records:
            if not isinstance(record, dict):
                raise ValueError(f"{relative_index} contains a non-record entry")
            identifier = str(record.get("id", ""))
            title = str(record.get("title") or identifier or "Untitled record")
            path, path_exists = _relative_path(base, record.get("path"), identifier)
            items.append(
                LandscapeItem(
                    record_type=record_type,
                    identifier=identifier,
                    title=title,
                    status=str(record.get("status", "raw")),
                    path=path,
                    path_exists=path_exists,
                    last_reviewed_at=_parse_date(record.get("last_reviewed_at"), "last_reviewed_at", identifier),
                    review_after=_parse_date(record.get("review_after"), "review_after", identifier),
                )
            )
    return sorted(items, key=lambda item: (item.status in {"rejected", "superseded"}, item.identifier))


def _relative_age(reviewed: date | None, today: date) -> str:
    if reviewed is None:
        return "Never reviewed"
    days = (today - reviewed).days
    if days <= 0:
        return "Reviewed today"
    if days == 1:
        return "1 day ago"
    return f"{days} days ago"


def _status(item: LandscapeItem, stale_after_days: int, today: date) -> tuple[str, bool]:
    action = NEXT_ACTIONS.get(item.status, "Review record status")
    if item.status in {"rejected", "superseded"}:
        return f"{item.status.title()} — {action}", False
    age = None if item.last_reviewed_at is None else (today - item.last_reviewed_at).days
    stale = item.last_reviewed_at is None or (
        item.review_after is not None and item.review_after <= today
    ) or (age is not None and age >= stale_after_days and item.status in STALE_STATUSES)
    if stale:
        return f"{item.status.title()} — Review needed: {action.lower()}", True
    return f"{item.status.title()} — {action}", False


def _document_cell(item: LandscapeItem) -> str:
    if item.path is None:
        return "Missing document path"
    if not item.path_exists:
        return f"Missing document: `{item.path}`"
    path = Path(item.path)
    try:
        path = path.relative_to("docs/product-discovery")
    except ValueError:
        pass
    return f"[{path.name}]({path.as_posix()})"


def _render(items: list[LandscapeItem], stale_after_days: int, today: date) -> tuple[str, int, int]:
    rows: dict[str, list[str]] = {"Needs attention": [], "Active": [], "Parked or closed": []}
    stale_count = 0
    missing_count = 0
    for item in items:
        status, stale = _status(item, stale_after_days, today)
        stale_count += int(stale)
        missing_count += int(not item.path_exists)
        label = f"{item.identifier} — {item.title}" if item.identifier else item.title
        row = f"| {label} | {_document_cell(item)} | {status} | {_relative_age(item.last_reviewed_at, today)} |"
        group = "Needs attention" if stale or not item.path_exists else "Parked or closed" if item.status in {"deferred", "rejected", "superseded"} else "Active"
        rows[group].append(row)
    lines = [
        "<!-- product-discovery-harness:generated-landscape -->",
        "# Product landscape",
        "",
        "This is a generated orientation view. Individual index records and their detail documents remain the source of truth.",
        "",
        "## Summary",
        "",
        f"- Records: {len(items)}",
        f"- Require review: {stale_count}",
        f"- Missing detail documents: {missing_count}",
        f"- Stale review threshold: {stale_after_days} days",
    ]
    for group, group_rows in rows.items():
        lines.extend(["", f"## {group}", ""])
        if group_rows:
            lines.extend(["| Idea | Document | Status | Last reviewed |", "| --- | --- | --- | --- |", *group_rows])
        else:
            lines.append("No records in this group.")
    return "\n".join(lines) + "\n", stale_count, missing_count


def generate_landscape(repo: str | Path, stale_after_days: int = 30, today: date | None = None) -> LandscapeReport:
    """Write the derived landscape only when its content changed."""
    if stale_after_days < 1:
        raise ValueError("stale_after_days must be at least 1")
    now = today or date.today()
    items = load_index_records(repo)
    content, stale_count, missing_count = _render(items, stale_after_days, now)
    output = discovery_root(repo) / "PRODUCT_LANDSCAPE.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    changed = not output.exists() or output.read_text() != content
    if changed:
        temporary = output.with_suffix(".tmp")
        temporary.write_text(content)
        temporary.replace(output)
    return LandscapeReport(output, len(items), stale_count, missing_count, changed)
