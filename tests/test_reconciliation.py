from pathlib import Path

import yaml

from product_discovery_harness.reconciliation import generate_reconciliation_report
from product_discovery_harness.seeding import seed_target
from product_discovery_harness.validation import validate_target


def _record(identifier: str, **extra):
    return {"id": identifier, "title": identifier, "source": "proposed", "status": "candidate", **extra}


def _write(root: Path, name: str, key: str, records: list[dict]):
    (root / f"docs/product-discovery/{name}/index.yml").write_text(yaml.safe_dump({key: records}, sort_keys=False))


def test_reconciliation_report_is_derived_and_preserves_records(tmp_path):
    seed_target(tmp_path, "greenfield")
    opportunity = _record("OPP-001", related_records=[{
        "id": "FEATURE-001", "relation": "overlaps", "rationale": "Same desired outcome", "status": "proposed",
    }], alignment_status="needs_review")
    feature = _record("FEATURE-001")
    _write(tmp_path, "opportunities", "opportunities", [opportunity])
    _write(tmp_path, "features", "features", [feature])
    before = (tmp_path / "docs/product-discovery/opportunities/index.yml").read_text()
    report = generate_reconciliation_report(tmp_path, "OPP-001")
    text = report.path.read_text()
    assert "`OPP-001` overlaps `FEATURE-001`" in text
    assert report.proposed_count == 1 and report.needs_review_count == 1
    assert (tmp_path / "docs/product-discovery/opportunities/index.yml").read_text() == before


def test_invalid_relationships_fail_target_validation(tmp_path):
    seed_target(tmp_path, "greenfield")
    bad = _record("OPP-001", related_records=[{
        "id": "OPP-001", "relation": "unknown", "rationale": "", "status": "confirmed",
    }], decision_refs=["DEC-999"])
    _write(tmp_path, "opportunities", "opportunities", [bad])
    errors = validate_target(tmp_path)
    assert any("cannot relate to itself" in error for error in errors)
    assert any("invalid relation" in error for error in errors)
    assert any("invalid decision_refs" in error for error in errors)
