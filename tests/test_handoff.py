import pytest

from product_discovery_harness.handoff import create_handoff
from product_discovery_harness.schema_validation import validate_handoff_frontmatter
from product_discovery_harness.seeding import seed_target
from product_discovery_harness.validation import validate_target


def feature():
    return {
        "feature_id": "FEATURE-001", "name": "Attention clarity",
        "opportunity_ids": ["OPP-001"], "target_users": ["Owner"],
        "problem": "Unclear attention", "desired_outcome": "Know next action",
        "selected_experience": "Guided queue", "core_interaction_model": "Prioritized workflow",
        "scope": "One queue", "non_goals": ["Analytics"],
        "experience_invariants": ["Explain why"], "required_states": ["Empty"],
        "dependencies": ["OPP-001"], "success_signals": ["Faster action"],
        "status": "accepted", "accepted_by": "Owner",
    }


def test_handoff_creates_canonical_product_spec_without_engineering_directory(tmp_path):
    seed_target(tmp_path, "greenfield")
    assert not (tmp_path / "docs/exec-plans").exists()
    with pytest.raises(ValueError):
        create_handoff(tmp_path, {})
    report = create_handoff(tmp_path, feature(), "epic")
    assert report.canonical_spec_path.exists()
    assert report.engineering_export_path is None
    assert "document_type: product-feature-spec" in report.canonical_spec_path.read_text()
    assert not validate_target(tmp_path)


def test_explicit_export_is_linked_and_preserves_unowned_engineering_file(tmp_path):
    seed_target(tmp_path, "greenfield")
    report = create_handoff(tmp_path, feature(), "epic", export_engineering=True)
    export = report.engineering_export_path
    assert export is not None and export.exists()
    text = export.read_text()
    assert "document_type: product-feature-handoff" in text
    assert "generated_by: product-discovery-harness" in text
    assert "canonical_spec: docs/product-specs/attention-clarity.md" in text
    export.write_text("# Engineering-owned handoff\n")
    with pytest.raises(ValueError, match="refusing to overwrite"):
        create_handoff(tmp_path, feature(), "epic", export_engineering=True)
    assert export.read_text() == "# Engineering-owned handoff\n"


def test_handoff_frontmatter_schema_rejects_invalid_contract():
    """AC-003: invalid Engineering Harness handoff frontmatter is rejected."""
    errors = validate_handoff_frontmatter(
        {
            "document_type": "wrong-type",
            "contract_version": 1,
            "feature_id": "FEATURE-001",
            "opportunity_ids": ["OPP-001"],
            "product_harness_version": "0.1.0",
            "status": "ready-for-analysis",
        }
    )
    assert any("document_type" in error for error in errors)
