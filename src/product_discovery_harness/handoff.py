"""Product-owned feature specs and optional public Engineering Harness exports."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .paths import root
from .schema_validation import validate_handoff_frontmatter

REQUIRED = ["feature_id", "name", "opportunity_ids", "target_users", "problem", "desired_outcome", "selected_experience", "core_interaction_model", "scope", "non_goals", "experience_invariants", "required_states", "dependencies", "success_signals"]
SECTIONS = ["Product context", "Target users", "Problem", "Desired outcome", "Why now", "Product alignment", "Selected experience", "Core interaction model", "Key journey", "Required states", "Experience invariants", "Scope", "Non-goals", "Dependencies", "Constraints", "Success signals", "Risks", "Open technical questions", "Prototype references", "Source references", "Decisions and rejected alternatives"]
ALIASES = {"Non-goals": "non_goals", "Selected experience": "selected_experience", "Core interaction model": "core_interaction_model", "Required states": "required_states", "Experience invariants": "experience_invariants", "Success signals": "success_signals", "Target users": "target_users", "Desired outcome": "desired_outcome", "Open technical questions": "open_technical_questions", "Prototype references": "prototype_references", "Source references": "source_references", "Decisions and rejected alternatives": "decisions"}


@dataclass(frozen=True)
class HandoffReport:
    """Paths produced by a handoff without hiding ownership boundaries."""
    canonical_spec_path: Path
    engineering_export_path: Path | None


def readiness_errors(feature: dict[str, Any]) -> list[str]:
    errors = [f"missing Definition-of-Ready field: {key}" for key in REQUIRED if not feature.get(key)]
    if feature.get("status") != "accepted":
        errors.append("feature status must be accepted")
    if not feature.get("accepted_by"):
        errors.append("accepted feature requires accepted_by")
    return errors


def _slug(feature: dict[str, Any]) -> str:
    return str(feature.get("slug") or feature["name"].lower().replace(" ", "-"))


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content)
    temporary.replace(path)


def _value(feature: dict[str, Any], section: str) -> str:
    value = feature.get(ALIASES.get(section, section.lower().replace(" ", "_")), "Not specified.")
    return "\n".join(f"- {item}" for item in value) if isinstance(value, list) else str(value)


def _render(feature: dict[str, Any], frontmatter: dict[str, Any]) -> str:
    lines = ["---", yaml.safe_dump(frontmatter, sort_keys=False).strip(), "---", "", f"# {feature['name']}", ""]
    for section in SECTIONS:
        lines.extend([f"## {section}", _value(feature, section), ""])
    return "\n".join(lines)


def write_product_spec(repo: str | Path, feature: dict[str, Any], version: str = "0.1.0") -> Path:
    """Write the complete product-owned source of truth for an accepted feature."""
    errors = readiness_errors(feature)
    if errors:
        raise ValueError("; ".join(errors))
    base = root(repo)
    path = base / "docs/product-specs" / f"{_slug(feature)}.md"
    frontmatter = {
        "document_type": "product-feature-spec",
        "contract_version": 1,
        "feature_id": feature["feature_id"],
        "opportunity_ids": feature["opportunity_ids"],
        "product_harness_version": version,
        "status": "accepted",
        "ownership": "product-discovery-harness",
    }
    _atomic_write(path, _render(feature, frontmatter))
    return path


def _export_enabled(repo: str | Path) -> bool:
    config = root(repo) / "product-harness.yml"
    if not config.exists():
        return False
    data = yaml.safe_load(config.read_text()) or {}
    engineering = (data.get("integration") or {}).get("engineering_harness") or {}
    return engineering.get("export_enabled", False) is True


def _generated_export(path: Path) -> bool:
    if not path.exists():
        return True
    text = path.read_text()
    if not text.startswith("---\n"):
        return False
    try:
        frontmatter = yaml.safe_load(text.split("---", 2)[1]) or {}
    except yaml.YAMLError:
        return False
    return frontmatter.get("document_type") == "product-feature-handoff" and frontmatter.get("generated_by") == "product-discovery-harness"


def export_engineering_handoff(repo: str | Path, feature: dict[str, Any], canonical_spec: Path, epic: str | None = None, version: str = "0.1.0") -> Path:
    """Export a public compatibility document without touching other engineering files."""
    base = root(repo)
    slug = _slug(feature)
    destination = base / "docs/exec-plans/current" / epic / slug / "informal.md" if epic else base / "docs/exec-plans/current" / slug / "informal.md"
    if not _generated_export(destination):
        raise ValueError(f"refusing to overwrite non-generated engineering handoff: {destination}")
    frontmatter = {
        "document_type": "product-feature-handoff",
        "contract_version": 1,
        "feature_id": feature["feature_id"],
        "opportunity_ids": feature["opportunity_ids"],
        "product_harness_version": version,
        "status": "ready-for-analysis",
        "generated_by": "product-discovery-harness",
        "canonical_spec": str(canonical_spec.relative_to(base)),
    }
    errors = validate_handoff_frontmatter(frontmatter)
    if errors:
        raise ValueError("invalid Engineering Harness handoff frontmatter: " + "; ".join(errors))
    _atomic_write(destination, _render(feature, frontmatter))
    return destination


def create_handoff(repo: str | Path, feature: dict[str, Any], epic: str | None = None, version: str = "0.1.0", export_engineering: bool | None = None) -> HandoffReport:
    """Create the canonical spec and, only if requested, an Engineering export."""
    canonical_spec = write_product_spec(repo, feature, version)
    should_export = _export_enabled(repo) if export_engineering is None else export_engineering
    engineering_export = export_engineering_handoff(repo, feature, canonical_spec, epic, version) if should_export else None
    return HandoffReport(canonical_spec, engineering_export)
