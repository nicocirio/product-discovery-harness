"""Validate and render explicit product-record reconciliation context."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any

import yaml

from .paths import discovery_root, root

RELATIONS = {"duplicates", "overlaps", "depends_on", "conflicts_with", "extends", "supersedes", "split_from"}
RELATION_STATUSES = {"proposed", "confirmed"}
ALIGNMENT_STATUSES = {"unreviewed", "aligned", "needs_review"}


@dataclass(frozen=True)
class ReconciliationReport:
    path: Path
    record_count: int
    proposed_count: int
    needs_review_count: int
    changed: bool


def _load_yaml(path: Path, key: str) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text()) or {}
    value = data.get(key, [])
    if not isinstance(value, list):
        raise ValueError(f"{path.name}.{key} must be a list")
    return [item for item in value if isinstance(item, dict)]


def load_records(repo: str | Path) -> list[dict[str, Any]]:
    base = root(repo)
    records = _load_yaml(base / "docs/product-discovery/opportunities/index.yml", "opportunities")
    records += _load_yaml(base / "docs/product-discovery/features/index.yml", "features")
    return sorted(records, key=lambda record: str(record.get("id", "")))


def known_ids(repo: str | Path, records: list[dict[str, Any]] | None = None) -> set[str]:
    base = root(repo)
    known = {str(record.get("id")) for record in (records or load_records(base)) if record.get("id")}
    current = _load_yaml(base / "docs/product-discovery/current-state/feature-inventory.yml", "features")
    known.update(str(record.get("id")) for record in current if record.get("id"))
    decision_log = base / "docs/product-discovery/decisions/decision-log.md"
    if decision_log.exists():
        known.update(re.findall(r"\bDEC-\d{3,}\b", decision_log.read_text()))
    return known


def validate_relationships(records: list[dict[str, Any]], all_known_ids: set[str]) -> list[str]:
    """Return actionable integrity errors without changing canonical records."""
    errors: list[str] = []
    durable_ids = {str(record.get("id")) for record in records if record.get("id")}
    for record in records:
        identifier = str(record.get("id", "<unknown>"))
        alignment = record.get("alignment_status")
        if alignment is not None and alignment not in ALIGNMENT_STATUSES:
            errors.append(f"{identifier}: alignment_status must be one of {sorted(ALIGNMENT_STATUSES)}")
        seen: set[tuple[str, str]] = set()
        related = record.get("related_records", [])
        if related is None:
            related = []
        if not isinstance(related, list):
            errors.append(f"{identifier}: related_records must be a list")
            continue
        for relation in related:
            if not isinstance(relation, dict):
                errors.append(f"{identifier}: related_records entries must be mappings")
                continue
            target = relation.get("id")
            kind = relation.get("relation")
            if target not in durable_ids:
                errors.append(f"{identifier}: related record does not exist: {target}")
            if target == identifier:
                errors.append(f"{identifier}: record cannot relate to itself")
            if kind not in RELATIONS:
                errors.append(f"{identifier}: invalid relation: {kind}")
            if relation.get("status") not in RELATION_STATUSES:
                errors.append(f"{identifier}: relation status must be proposed or confirmed")
            if not isinstance(relation.get("rationale"), str) or not relation["rationale"].strip():
                errors.append(f"{identifier}: relation rationale is required")
            pair = (str(target), str(kind))
            if pair in seen:
                errors.append(f"{identifier}: duplicate relation to {target}: {kind}")
            seen.add(pair)
        for field, prefix in (("decision_refs", "DEC-"), ("current_capability_refs", "CURRENT-")):
            refs = record.get(field, [])
            if refs is None:
                continue
            if not isinstance(refs, list):
                errors.append(f"{identifier}: {field} must be a list")
                continue
            for ref in refs:
                if not isinstance(ref, str) or not ref.startswith(prefix) or ref not in all_known_ids:
                    errors.append(f"{identifier}: invalid {field} reference: {ref}")
    return errors


def _report_content(records: list[dict[str, Any]], record_id: str | None) -> tuple[str, int, int]:
    selected = [record for record in records if record_id is None or record.get("id") == record_id]
    if record_id is not None and not selected:
        raise ValueError(f"unknown durable record: {record_id}")
    proposed: list[str] = []
    review: list[str] = []
    confirmed: list[str] = []
    for record in selected:
        identifier = str(record.get("id")); title = str(record.get("title") or identifier)
        if record.get("alignment_status", "unreviewed") in {"unreviewed", "needs_review"}:
            review.append(f"- `{identifier}` — {title}: alignment is `{record.get('alignment_status', 'unreviewed')}`")
        for relation in record.get("related_records", []) or []:
            line = f"- `{identifier}` {relation.get('relation')} `{relation.get('id')}` ({relation.get('rationale')})"
            (proposed if relation.get("status") == "proposed" else confirmed).append(line)
    lines = [
        "<!-- product-discovery-harness:generated-reconciliation -->",
        f"# {'Reconciliation: ' + record_id if record_id else 'Product consistency report'}",
        "",
        "This is a derived report. Index records, decisions, current-state evidence, and sessions remain canonical.",
        "",
        "## Requires a human decision",
        "",
        *(proposed or ["No proposed relationships."]),
        "",
        "## Alignment to review",
        "",
        *(review or ["No records currently flagged for alignment review."]),
        "",
        "## Confirmed relationships",
        "",
        *(confirmed or ["No confirmed relationships."]),
        "",
        "## Facilitation prompt",
        "",
        "For one item above, decide whether to merge, extend, split, supersede, keep distinct, defer, or reject. Record the rationale only after explicit owner confirmation.",
    ]
    return "\n".join(lines) + "\n", len(proposed), len(review)


def generate_reconciliation_report(repo: str | Path, record_id: str | None = None) -> ReconciliationReport:
    base = root(repo)
    records = load_records(base)
    errors = validate_relationships(records, known_ids(base, records))
    if errors:
        raise ValueError("; ".join(errors))
    content, proposed_count, review_count = _report_content(records, record_id)
    relative_output = Path("reconciliations") / f"{record_id}.md" if record_id else Path("CONSISTENCY_REPORT.md")
    output = discovery_root(base) / relative_output
    output.parent.mkdir(parents=True, exist_ok=True)
    changed = not output.exists() or output.read_text() != content
    if changed:
        temporary = output.with_suffix(".tmp")
        temporary.write_text(content)
        temporary.replace(output)
    return ReconciliationReport(output, len(records) if record_id is None else 1, proposed_count, review_count, changed)
