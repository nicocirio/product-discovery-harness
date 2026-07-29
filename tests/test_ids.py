import pytest
from product_discovery_harness.ids import allocate_id, validate_id

def test_monotonic_ids(tmp_path):
    assert allocate_id(tmp_path,"OPP") == "OPP-001"
    assert allocate_id(tmp_path,"OPP") == "OPP-002"
    assert validate_id("FEATURE-001") and not validate_id("FEATURE-1")
    with pytest.raises(ValueError): allocate_id(tmp_path,"BAD")
