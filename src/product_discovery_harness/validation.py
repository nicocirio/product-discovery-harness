"""Target contract validation with actionable local diagnostics."""
from __future__ import annotations
from pathlib import Path
import yaml
from .paths import root, discovery_root
from .records import validate_record
from .ids import validate_id
from .reconciliation import known_ids, validate_relationships
from .schema_validation import validate_schema

REQUIRED=["product-harness.yml","docs/README.md","docs/PRODUCT_SENSE.md","docs/EXPERIENCE_SENSE.md","docs/product-specs","docs/product-discovery/STATUS.md","docs/product-discovery/open-questions.md","docs/product-discovery/assumptions.yml","docs/product-discovery/current-state/feature-inventory.yml","docs/product-discovery/opportunities/index.yml","docs/product-discovery/features/index.yml","docs/product-discovery/decisions/decision-log.md","docs/product-discovery/roadmap/releases.md"]
SCHEMA_DOCUMENTS = {
    "product-harness.yml": "product-harness.schema.json",
    "docs/product-discovery/assumptions.yml": "assumptions.schema.json",
    "docs/product-discovery/current-state/feature-inventory.yml": "feature-inventory.schema.json",
    "docs/product-discovery/opportunities/index.yml": "opportunity-index.schema.json",
    "docs/product-discovery/features/index.yml": "feature-index.schema.json",
}
def validate_target(repo: str | Path) -> list[str]:
    base=root(repo); errors=[]
    for rel in REQUIRED:
        if not (base/rel).exists(): errors.append(f"missing required path: {rel}")
    cfg=base/"product-harness.yml"
    if not cfg.exists(): return errors
    try: data=yaml.safe_load(cfg.read_text()) or {}
    except yaml.YAMLError as exc: return errors+[f"product-harness.yml: invalid YAML: {exc}"]
    errors.extend(f"product-harness.yml: {error}" for error in validate_schema(SCHEMA_DOCUMENTS["product-harness.yml"], data))
    for rel in (
        "docs/product-discovery/assumptions.yml",
        "docs/product-discovery/current-state/feature-inventory.yml",
    ):
        path = base / rel
        if not path.exists():
            continue
        try:
            document = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue
        errors.extend(f"{rel}: {error}" for error in validate_schema(SCHEMA_DOCUMENTS[rel], document))
    if data.get("version") != 1: errors.append("product-harness.yml.version must be 1")
    if data.get("mode") not in {"greenfield","brownfield","pending"}: errors.append("product-harness.yml.mode must be greenfield, brownfield, or pending")
    if data.get("legacy_stance") not in {"foundation","reference","migration","salvage","ignore"}: errors.append("product-harness.yml.legacy_stance is invalid")
    engineering = ((data.get("integration") or {}).get("engineering_harness") or {})
    for key in ("enabled", "export_enabled"):
        if key in engineering and not isinstance(engineering[key], bool):
            errors.append(f"product-harness.yml.integration.engineering_harness.{key} must be boolean")
    if engineering.get("export_mode", "manual") != "manual":
        errors.append("product-harness.yml.integration.engineering_harness.export_mode must be manual")
    seen=set(); opp_ids=set()
    for rel, key in [("docs/product-discovery/opportunities/index.yml","opportunities"),("docs/product-discovery/features/index.yml","features")]:
        path=base/rel
        if not path.exists(): continue
        try:
            document=yaml.safe_load(path.read_text()) or {}
            items=document.get(key, []) if isinstance(document, dict) else []
            items=items if isinstance(items, list) else []
        except yaml.YAMLError as exc: errors.append(f"{rel}: invalid YAML: {exc}"); continue
        errors.extend(f"{rel}: {error}" for error in validate_schema(SCHEMA_DOCUMENTS[rel], document))
        for record in items:
            if not isinstance(record, dict):
                continue
            rid=record.get("id", "")
            if not validate_id(rid): errors.append(f"{rel}: invalid ID: {rid}")
            if rid in seen: errors.append(f"duplicate active ID: {rid}")
            seen.add(rid); errors += [f"{rid}: {e}" for e in validate_record(record)]
            path_value = record.get("path")
            if path_value is not None:
                if not isinstance(path_value, str) or Path(path_value).is_absolute() or ".." in Path(path_value).parts:
                    errors.append(f"{rid}: path must be target-relative")
            for date_field in ("created_at", "last_updated_at", "last_reviewed_at", "review_after"):
                value = record.get(date_field)
                if value is not None:
                    try:
                        from datetime import date
                        date.fromisoformat(str(value))
                    except ValueError:
                        errors.append(f"{rid}: {date_field} must use YYYY-MM-DD")
            if key == "opportunities": opp_ids.add(rid)
            if key == "features":
                for oid in record.get("opportunity_ids", []):
                    if oid not in opp_ids: errors.append(f"{rid}: nonexistent opportunity reference: {oid}")
    records: list[dict] = []
    for rel, key in [("docs/product-discovery/opportunities/index.yml", "opportunities"), ("docs/product-discovery/features/index.yml", "features")]:
        path = base / rel
        if path.exists():
            try:
                document = yaml.safe_load(path.read_text()) or {}
                items = document.get(key, []) if isinstance(document, dict) else []
                if isinstance(items, list):
                    records.extend(item for item in items if isinstance(item, dict))
            except yaml.YAMLError: pass
    errors.extend(validate_relationships(records, known_ids(base, records) if records else set()))
    return errors
