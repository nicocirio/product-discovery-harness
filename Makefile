.PHONY: test validate

test:
	python3 -m pytest

validate:
	PYTHONPATH=src python3 -m pytest tests/test_seeding.py tests/test_validation.py
