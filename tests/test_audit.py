from datetime import date

import yaml

from product_discovery_harness.audit import audit_repository
from product_discovery_harness.cli import main
from product_discovery_harness.seeding import seed_target


def test_audit_preserves_same_day_history_and_refreshes_current_snapshot(tmp_path):
    """AC-001 and AC-002: history is immutable while current state is replaceable."""
    seed_target(tmp_path, "brownfield")
    (tmp_path / "booking_page.py").write_text("def index(): pass\n")

    first = audit_repository(tmp_path, today=date(2026, 7, 29))
    (tmp_path / "billing_service.py").write_text("def charge(): pass\n")
    second = audit_repository(tmp_path, today=date(2026, 7, 29))

    assert first.historical_report_path.name == "2026-07-29-001-repository-audit.md"
    assert second.historical_report_path.name == "2026-07-29-002-repository-audit.md"
    assert first.historical_report_path.exists() and second.historical_report_path.exists()
    assert "billing service" not in first.historical_report_path.read_text()
    assert "billing service" in second.historical_report_path.read_text()
    inventory = yaml.safe_load(second.feature_inventory_path.read_text())
    assert len(inventory["features"]) == 2
    index = second.index_path.read_text()
    assert "2026-07-29-002-repository-audit" in index
    assert "2026-07-29-001-repository-audit" in index


def test_audit_cli_reports_current_and_historical_evidence(tmp_path, capsys):
    """AC-003: CLI output and the audit index expose the newest report."""
    seed_target(tmp_path, "brownfield")
    (tmp_path / "settings_route.py").write_text("def route(): pass\n")

    assert main(["audit", str(tmp_path)]) == 0
    output = capsys.readouterr().out
    assert "Current feature inventory:" in output
    assert "Historical audit report:" in output
    assert "Recommended next focus: $product-review-current-state" in output
    assert list((tmp_path / "docs/product-discovery/audits").glob("*-repository-audit.md"))
