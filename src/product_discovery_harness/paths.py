"""Path helpers that keep writes inside a selected target repository."""
from __future__ import annotations
from pathlib import Path

DISCOVERY = Path("docs/product-discovery")

def root(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()

def discovery_root(path: str | Path) -> Path:
    return root(path) / DISCOVERY

def package_root() -> Path:
    return Path(__file__).resolve().parents[2]

def assets_root() -> Path:
    return package_root().parents[0]
