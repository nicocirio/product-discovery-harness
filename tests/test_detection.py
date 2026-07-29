from product_discovery_harness.detection import detect_mode

def test_detection(tmp_path):
    assert detect_mode(tmp_path).mode == "greenfield"
    (tmp_path / "package.json").write_text("{}")
    assert detect_mode(tmp_path).mode == "pending"
    (tmp_path / "src").mkdir(); (tmp_path / "src" / "main.py").write_text("x=1")
    (tmp_path / "tests").mkdir(); (tmp_path / "tests" / "test_app.py").write_text("x=1")
    (tmp_path / "app.py").write_text("x=1")
    assert detect_mode(tmp_path).mode == "brownfield"
    assert detect_mode(tmp_path, "greenfield").mode == "greenfield"
