#!/usr/bin/env python3
"""Dependency-free validation for the public skill candidate."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "design-low-friction-products"
SKILL_FILE = SKILL_DIR / "SKILL.md"

REQUIRED_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "LICENSE",
    ROOT / ".github" / "workflows" / "validate.yml",
    SKILL_FILE,
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "references" / "checklists.md",
    SKILL_DIR / "references" / "design-rationale.md",
    ROOT / "evals" / "trigger-cases.json",
)

ENGLISH_RUNTIME_FILES = (
    SKILL_FILE,
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "references" / "checklists.md",
    SKILL_DIR / "references" / "design-rationale.md",
)

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ""}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str, errors: list[str]) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    if not match:
        fail(errors, "SKILL.md has invalid YAML frontmatter boundaries")
        return {}

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator:
            fail(errors, f"unsupported frontmatter line: {line!r}")
            continue
        values[key.strip()] = value.strip().strip('"')
    return values


def validate_frontmatter(errors: list[str]) -> None:
    text = SKILL_FILE.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text, errors)
    if set(frontmatter) != {"name", "description"}:
        fail(errors, "frontmatter must contain exactly name and description")
        return

    name = frontmatter["name"]
    description = frontmatter["description"]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail(errors, f"invalid skill name: {name!r}")
    if name != SKILL_DIR.name:
        fail(errors, "skill name must match its parent directory")
    if not 1 <= len(name) <= 64:
        fail(errors, "skill name must be 1-64 characters")
    if not 1 <= len(description) <= 1024:
        fail(errors, "description must be 1-1024 characters")

    required_description_terms = (
        "low-friction",
        "user-visible task path",
        "recently used choices",
        "prefill",
        "Do not trigger",
    )
    for term in required_description_terms:
        if term not in description:
            fail(errors, f"description is missing trigger-boundary term: {term}")


def validate_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.is_file():
            fail(errors, f"missing required file: {path.relative_to(ROOT)}")


def validate_runtime_language(errors: list[str]) -> None:
    cjk = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
    for path in ENGLISH_RUNTIME_FILES:
        text = path.read_text(encoding="utf-8")
        if cjk.search(text):
            fail(errors, f"runtime file is not English-only: {path.relative_to(ROOT)}")
        if path.name == "SKILL.md" and len(text.splitlines()) >= 500:
            fail(errors, "SKILL.md must remain under 500 lines")


def validate_public_content(errors: list[str]) -> None:
    private_fragments = (
        "/" + "Users" + "/",
        "C:" + "\\" + "Users" + "\\",
        ".codex/" + "memories",
        "rollout_" + "summaries",
        "SH" + "BL",
        "Home" + "Centre",
        "Cosmo" + "graph",
        "Su" + "ki",
        "ST" + "T-ui",
    )
    secret_patterns = (
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
        re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
        re.compile(r"sk-[A-Za-z0-9]{20,}"),
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    )

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        for fragment in private_fragments:
            if fragment.lower() in text.lower():
                fail(errors, f"private or local fragment {fragment!r} found in {relative}")
        for pattern in secret_patterns:
            if pattern.search(text):
                fail(errors, f"secret-shaped content matched {pattern.pattern!r} in {relative}")


def validate_markdown_links(errors: list[str]) -> int:
    link_count = 0
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target:
                continue
            link_count += 1
            parsed = urlparse(target)
            if parsed.scheme:
                if parsed.scheme != "https":
                    fail(errors, f"non-HTTPS external link in {path.relative_to(ROOT)}: {target}")
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                fail(errors, f"broken relative link in {path.relative_to(ROOT)}: {target}")
    return link_count


def validate_openai_yaml(errors: list[str]) -> None:
    path = SKILL_DIR / "agents" / "openai.yaml"
    text = path.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s{{2}}{key}:\s+\"[^\"]+\"\s*$", text, re.MULTILINE):
            fail(errors, f"agents/openai.yaml is missing quoted {key}")
    if "$design-low-friction-products" not in text:
        fail(errors, "default_prompt must explicitly mention the skill")


def validate_evals(errors: list[str]) -> tuple[int, int, int]:
    path = ROOT / "evals" / "trigger-cases.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"invalid evaluation JSON: {exc}")
        return 0, 0, 0

    cases = data.get("cases")
    if data.get("schema_version") != 1 or data.get("skill") != SKILL_DIR.name or not isinstance(cases, list):
        fail(errors, "evaluation metadata is invalid")
        return 0, 0, 0

    identifiers: set[str] = set()
    positive = negative = 0
    coverage: set[tuple[str, str, bool]] = set()
    for case in cases:
        if not isinstance(case, dict):
            fail(errors, "every evaluation case must be an object")
            continue
        identifier = case.get("id")
        language = case.get("language")
        invocation = case.get("invocation")
        should_trigger = case.get("should_trigger")
        prompt = case.get("prompt")
        behaviors = case.get("expected_behaviors")
        if not isinstance(identifier, str) or identifier in identifiers:
            fail(errors, f"invalid or duplicate evaluation id: {identifier!r}")
            continue
        identifiers.add(identifier)
        if language not in {"en", "zh"}:
            fail(errors, f"unsupported evaluation language in {identifier}")
        if invocation not in {"explicit", "implicit"}:
            fail(errors, f"unsupported invocation type in {identifier}")
        if not isinstance(should_trigger, bool):
            fail(errors, f"should_trigger must be boolean in {identifier}")
            continue
        if not isinstance(prompt, str) or not prompt.strip():
            fail(errors, f"missing prompt in {identifier}")
        if invocation == "explicit" and "$design-low-friction-products" not in str(prompt):
            fail(errors, f"explicit case does not mention the skill in {identifier}")
        if not isinstance(behaviors, list) or not behaviors or not all(isinstance(item, str) for item in behaviors):
            fail(errors, f"expected_behaviors must be a non-empty string list in {identifier}")
        coverage.add((str(language), str(invocation), should_trigger))
        if should_trigger:
            positive += 1
        else:
            negative += 1

    required_coverage = {
        ("en", "explicit", True),
        ("zh", "explicit", True),
        ("en", "implicit", True),
        ("zh", "implicit", True),
        ("en", "implicit", False),
        ("zh", "implicit", False),
    }
    missing = required_coverage - coverage
    if missing:
        fail(errors, f"evaluation coverage is missing: {sorted(missing)}")
    if len(cases) < 10 or positive < 5 or negative < 4:
        fail(errors, "evaluation set needs at least 10 cases, 5 positive cases, and 4 negative cases")
    return len(cases), positive, negative


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    if not errors:
        validate_frontmatter(errors)
        validate_runtime_language(errors)
        validate_public_content(errors)
        link_count = validate_markdown_links(errors)
        validate_openai_yaml(errors)
        case_count, positive, negative = validate_evals(errors)
    else:
        link_count = case_count = positive = negative = 0

    if errors:
        print("VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALIDATION: PASS")
    print(f"- required files: {len(REQUIRED_FILES)}")
    print(f"- markdown links checked: {link_count}")
    print(f"- trigger cases: {case_count} ({positive} positive, {negative} negative)")
    print(f"- SKILL.md lines: {len(SKILL_FILE.read_text(encoding='utf-8').splitlines())}")
    print("- private-path and credential-pattern scan: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
