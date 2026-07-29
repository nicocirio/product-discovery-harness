import yaml
from product_discovery_harness.seeding import seed_target
from product_discovery_harness.validation import validate_target

def test_invalid_config_and_reference(tmp_path):
    seed_target(tmp_path,"greenfield"); cfg=tmp_path/"product-harness.yml"; data=yaml.safe_load(cfg.read_text()); data["mode"]="bad"; cfg.write_text(yaml.safe_dump(data)); assert any("mode" in x for x in validate_target(tmp_path))

def test_invalid_engineering_export_config_is_actionable(tmp_path):
    seed_target(tmp_path, "greenfield")
    cfg = tmp_path / "product-harness.yml"
    data = yaml.safe_load(cfg.read_text())
    data["integration"]["engineering_harness"]["export_enabled"] = "yes"
    cfg.write_text(yaml.safe_dump(data))
    assert any("export_enabled" in error for error in validate_target(tmp_path))


def test_schema_violation_is_scoped_to_its_target_document(tmp_path):
    """AC-001: structural errors name the target document that violates its schema."""
    seed_target(tmp_path, "greenfield")
    index = tmp_path / "docs/product-discovery/opportunities/index.yml"
    index.write_text(yaml.safe_dump({"opportunities": "not-a-list"}))
    assert any(
        "docs/product-discovery/opportunities/index.yml" in error and "not of type 'array'" in error
        for error in validate_target(tmp_path)
    )
