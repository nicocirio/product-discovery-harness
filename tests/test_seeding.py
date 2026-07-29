from product_discovery_harness.seeding import seed_target
from product_discovery_harness.validation import validate_target

def test_seed_is_safe_and_valid(tmp_path):
    """AC-002: a normal seeded target stays valid under schema-backed validation."""
    report=seed_target(tmp_path, "greenfield")
    assert report.mode == "greenfield" and not validate_target(tmp_path)
    sense=tmp_path / "docs/PRODUCT_SENSE.md"; sense.write_text("# My product\n\nOwner words\n")
    assert "docs/PRODUCT_SENSE.md" in seed_target(tmp_path).preserved
    assert "Owner words" in sense.read_text()
    assert (tmp_path / "docs/README.md").exists()
    assert not (tmp_path / "docs/exec-plans/current").exists()
