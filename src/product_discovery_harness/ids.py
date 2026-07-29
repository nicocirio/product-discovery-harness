"""Monotonic local IDs backed by a durable registry."""
from __future__ import annotations
import re
from pathlib import Path
import yaml
from .paths import discovery_root

PREFIXES = {"CURRENT", "OPP", "FEATURE", "DEC", "ASSUMPTION", "QUESTION"}
PATTERN = re.compile(r"^(CURRENT|OPP|FEATURE|DEC|ASSUMPTION|QUESTION)-(\d{3,})$")

def validate_id(value: str) -> bool:
    return bool(PATTERN.fullmatch(value))

def allocate_id(repo: str | Path, prefix: str) -> str:
    if prefix not in PREFIXES: raise ValueError(f"unsupported ID prefix: {prefix}")
    path = discovery_root(repo) / ".id-registry.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    data = yaml.safe_load(path.read_text()) if path.exists() else {}
    data = data or {}
    next_number = int(data.get(prefix, 0)) + 1
    data[prefix] = next_number
    temp = path.with_suffix(".tmp")
    temp.write_text(yaml.safe_dump(data, sort_keys=True))
    temp.replace(path)
    return f"{prefix}-{next_number:03d}"
