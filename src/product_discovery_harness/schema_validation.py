"""Local JSON Schema validation for durable target contracts."""
from __future__ import annotations

from functools import lru_cache
import json
from typing import Any

from jsonschema import Draft202012Validator, SchemaError

from .paths import package_root


@lru_cache(maxsize=None)
def load_schema(name: str) -> dict[str, Any]:
    """Load a checked-in schema without resolving any remote resource."""
    path = package_root() / "schemas" / name
    return json.loads(path.read_text())


def validate_schema(name: str, instance: Any) -> list[str]:
    """Return stable, concise violations for an instance of a named schema."""
    try:
        schema = load_schema(name)
        Draft202012Validator.check_schema(schema)
        errors = Draft202012Validator(schema).iter_errors(instance)
    except (OSError, json.JSONDecodeError, SchemaError) as exc:
        return [f"cannot load schema {name}: {exc}"]

    result: list[str] = []
    for error in sorted(errors, key=lambda item: (tuple(map(str, item.absolute_path)), item.message)):
        location = ".".join(str(part) for part in error.absolute_path) or "root"
        result.append(f"{location}: {error.message}")
    return result


def validate_handoff_frontmatter(frontmatter: dict[str, Any]) -> list[str]:
    """Validate the explicitly versioned Engineering Harness export contract."""
    return validate_schema("handoff-frontmatter.schema.json", frontmatter)
