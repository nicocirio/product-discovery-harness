"""Contract checks for natural, guided product-skill protocols."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = tuple(sorted((ROOT / "skills").glob("*/SKILL.md")))


def read_skill(skill_name: str) -> str:
    return (ROOT / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")


def test_every_installed_skill_ends_with_one_recommended_next_focus() -> None:
    # AC-001: every installed product skill has a uniform routing contract.
    assert len(SKILL_FILES) == 19

    for skill_file in SKILL_FILES:
        content = skill_file.read_text(encoding="utf-8")
        assert "## Output Contract" in content
        assert content.count("Recommended next focus:") == 1, skill_file


def test_entry_skills_do_not_require_workflow_expertise_or_automatic_decisions() -> None:
    # AC-003: talk and resume are safe, no-expertise entry points.
    talk = read_skill("talk")
    resume = read_skill("resume")

    assert "$product-bootstrap" in talk
    assert "Never imply automatic promotion, acceptance, or ID allocation." in " ".join(talk.split())
    assert "$product-bootstrap" in resume
    assert "Do not change accepted content without confirmation." in resume


def test_specialist_skills_offer_actionable_recovery_routes() -> None:
    # AC-002: missing prerequisites lead to helpful recovery, not opaque failure.
    expected_routes = {
        "audit": ("$product-bootstrap",),
        "experience_evaluate": ("$product-experience-explore", "$product-landscape"),
        "experience_explore": ("$product-landscape", "$product-opportunity-explore", "$product-talk"),
        "experience_north": ("$product-talk",),
        "feature_crystallize": ("$product-landscape", "$product-talk", "$product-experience-evaluate"),
        "focus": ("$product-landscape", "$product-talk"),
        "handoff": ("$product-landscape", "$product-feature-crystallize", "$product-talk"),
        "landscape": ("$product-bootstrap",),
        "opportunity_explore": ("$product-landscape", "$product-talk"),
        "opportunity_map": ("$product-talk", "$product-reconcile"),
        "reconcile": ("$product-landscape", "$product-talk"),
        "review": ("$product-bootstrap",),
        "review_current_state": ("$product-audit", "$product-bootstrap"),
        "slice": ("$product-landscape",),
        "synthesize": ("$product-talk", "$product-bootstrap"),
        "validate": ("$product-bootstrap",),
    }

    for skill_name, routes in expected_routes.items():
        content = read_skill(skill_name)
        assert "## Preconditions" in content, skill_name
        for route in routes:
            assert route in content, f"{skill_name}: missing {route}"


def test_readme_keeps_product_talk_as_the_normal_starting_point() -> None:
    # AC-004: public onboarding stays aligned with the skill contract.
    for readme_path in (ROOT / "README.md", ROOT / "README.es.md"):
        content = readme_path.read_text(encoding="utf-8")
        assert "$product-talk" in content
        assert "checklist" in content.lower()
