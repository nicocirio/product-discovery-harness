from datetime import date
from pathlib import Path

import yaml

from product_discovery_harness.landscape import generate_landscape
from product_discovery_harness.seeding import seed_target


def _write_index(root: Path, name: str, records: list[dict]) -> None:
    path = root / "docs/product-discovery" / name / "index.yml"
    key = "opportunities" if name == "opportunities" else "features"
    path.write_text(yaml.safe_dump({key: records}, sort_keys=False))


def test_landscape_only_links_existing_documents_and_marks_stale(tmp_path):
    seed_target(tmp_path, "greenfield")
    brief = tmp_path / "docs/product-discovery/opportunities/OPP-001/brief.md"
    brief.parent.mkdir(parents=True)
    brief.write_text("# Existing brief\n")
    _write_index(tmp_path, "opportunities", [{
        "id": "OPP-001", "title": "Clarify attention", "source": "user_reported",
        "status": "exploring", "path": "docs/product-discovery/opportunities/OPP-001/brief.md",
        "created_at": "2026-01-01", "last_updated_at": "2026-01-02", "last_reviewed_at": "2026-06-01",
    }, {
        "id": "OPP-002", "title": "Missing context", "source": "proposed",
        "status": "deferred", "path": "docs/product-discovery/opportunities/OPP-002/brief.md",
        "last_reviewed_at": "2026-07-28",
    }])
    report = generate_landscape(tmp_path, stale_after_days=30, today=date(2026, 7, 29))
    text = report.path.read_text()
    assert "[brief.md](opportunities/OPP-001/brief.md)" in text
    assert "Missing document: `docs/product-discovery/opportunities/OPP-002/brief.md`" in text
    assert "Exploring — Review needed" in text
    assert report.stale_count == 1 and report.missing_document_count == 1
    before = text
    assert not generate_landscape(tmp_path, 30, date(2026, 7, 29)).changed
    assert report.path.read_text() == before


def test_landscape_never_changes_record_status(tmp_path):
    seed_target(tmp_path, "greenfield")
    record = {"id": "FEATURE-001", "title": "A deferred feature", "source": "proposed", "status": "deferred", "path": "docs/product-discovery/features/FEATURE-001/feature.md"}
    _write_index(tmp_path, "features", [record])
    generate_landscape(tmp_path, today=date(2026, 7, 29))
    stored = yaml.safe_load((tmp_path / "docs/product-discovery/features/index.yml").read_text())["features"][0]
    assert stored["status"] == "deferred" and "last_reviewed_at" not in stored
