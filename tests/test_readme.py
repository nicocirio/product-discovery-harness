"""Regression checks for the public learning guides."""

from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
README_PATHS = (ROOT / "README.md", ROOT / "README.es.md")
SKILLS = (
    "product-bootstrap",
    "product-resume",
    "product-audit",
    "product-review-current-state",
    "product-talk",
    "product-focus",
    "product-synthesize",
    "product-review",
    "product-opportunity-map",
    "product-opportunity-explore",
    "product-experience-north",
    "product-experience-explore",
    "product-experience-evaluate",
    "product-feature-crystallize",
    "product-slice",
    "product-handoff",
    "product-validate",
    "product-landscape",
    "product-reconcile",
)
COMMANDS = (
    "product-harness bootstrap . --mode=auto",
    "product-harness detect .",
    "product-harness landscape .",
    "product-harness reconcile . --record OPP-001",
    "product-harness validate .",
)
GUIDED_ONBOARDING = {
    "README.md": {
        "entry": "## Start here: tell the harness what is on your mind",
        "guidance": "recommends the next useful focus",
        "depth": "## Choose the depth that fits the decision",
    },
    "README.es.md": {
        "entry": "## Empezá por acá: contale al harness qué tenés en mente",
        "guidance": "recomienda el próximo foco útil",
        "depth": "## Elegí la profundidad según la decisión",
    },
}


@pytest.mark.parametrize("readme_path", README_PATHS)
def test_learning_guides_cover_every_installed_skill_and_cli_command(readme_path: Path) -> None:
    # AC-001: valid conversational-skill and CLI examples stay distinct.
    # AC-002: every installed product skill remains discoverable in each guide.
    content = readme_path.read_text(encoding="utf-8")

    for skill in SKILLS:
        assert f"${skill}" in content
    for command in COMMANDS:
        assert command in content


@pytest.mark.parametrize("readme_path", README_PATHS)
def test_learning_guides_explain_the_optional_engineering_complement(readme_path: Path) -> None:
    # AC-003: both languages retain the same integration and diagram guidance.
    content = readme_path.read_text(encoding="utf-8")

    assert "https://github.com/Simon-Initiative/harness" in content
    assert "mermaid" in content


def test_readme_skill_links_resolve_locally() -> None:
    for skill_file in (ROOT / "skills").glob("*/SKILL.md"):
        assert skill_file.is_file()


@pytest.mark.parametrize("readme_path", README_PATHS)
def test_guides_teach_conversation_before_durable_ids(readme_path: Path) -> None:
    # AC-001: the harness guides newcomers from product-talk.
    # AC-002: an ID is created and recovered through landscape before reuse.
    # AC-003: deeper discovery is conditional, not a mandatory sequence.
    content = readme_path.read_text(encoding="utf-8")
    normalized_content = " ".join(content.split())
    expected = GUIDED_ONBOARDING[readme_path.name]

    assert expected["entry"] in content
    assert expected["guidance"] in normalized_content
    assert expected["depth"] in content
    assert content.index("Created opportunity:") < content.index("$product-landscape")
    assert content.index("$product-landscape") < content.index("$product-opportunity-explore OPP-001")


def test_skill_guidance_audit_covers_every_installed_skill() -> None:
    # AC-004: maintainers have a durable, complete assessment of skill guidance.
    # AC-005: documentation claims remain protected by automated checks.
    audit_path = (
        ROOT
        / "docs/exec-plans/archive/product-discovery-harness-v1"
        / "guided-discovery-onboarding/skill-guidance-audit.md"
    )
    content = audit_path.read_text(encoding="utf-8")

    assert "| Skill | Guidance posture | Evidence in current protocol |" in content
    for skill in SKILLS:
        assert f"`${skill}`" in content


def test_release_guides_describe_the_manual_tagging_policy() -> None:
    # AC-001: maintainers receive the ordered manual tag commands.
    # AC-002: stable/latest behavior is stated beside the release procedure.
    # AC-003: English and Spanish guides keep the same manual policy.
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    spanish = (ROOT / "README.es.md").read_text(encoding="utf-8")
    for content in (english, spanish):
        assert "git tag -a vX.Y.Z" in content
        assert "git push origin main --follow-tags" in content
        assert "`stable`" in content and "`latest`" in content
