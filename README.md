# Design Low-Friction Products

An agent skill for designing and auditing product interfaces, forms, workflows, dashboards, and AI-assisted operations around a simple acceptance unit: can the user move from the expected entry point to a reliable outcome with low learning cost?

Status: public standalone skill. The first release is validated as a minimal, English-language runtime package with Chinese human documentation.

## What it protects

- Short, complete task paths instead of feature accumulation.
- Recently used and frequently used choices without unstable or unsafe ranking.
- Context-aware defaults and prefill without overwriting manual input.
- One authoritative mutation path with multiple useful UI entry points.
- Risk-based automation, confirmation, recovery, and permission handling.
- Focused evidence that distinguishes automated checks, usability review, and real-user acceptance.

The skill treats repeated work as a product capability. It explicitly separates candidate eligibility, current-value preservation, ordering, recommendation, prefill, and submission so that a convenience signal cannot silently become a business decision.

## Install

Copy the distributable skill directory into a supported user skill location:

```bash
mkdir -p ~/.agents/skills
cp -R skills/design-low-friction-products ~/.agents/skills/
```

Codex normally detects skill changes automatically. If the skill does not appear, restart Codex.

## Use

Invoke it explicitly:

```text
$design-low-friction-products audit this order-entry workflow and reduce repeated input without hiding risk
```

Codex can also invoke it implicitly when a task materially changes a user-visible flow, form behavior, defaults, option ordering, workflow automation, recovery, or supported-device interaction.

## Repository layout

```text
skills/design-low-friction-products/  Distributable runtime package
evals/trigger-cases.json              Positive and negative trigger cases
scripts/validate.py                   Dependency-free repository validation
README.zh-CN.md                       Human-readable Chinese introduction
```

The runtime package is English-only to keep one canonical behavior specification. The Chinese README is documentation, not a second executable skill.

## Validate

```bash
python3 scripts/validate.py
```

The validator checks required files, frontmatter, package naming, UI metadata, relative Markdown links, HTTPS-only public references, English-only runtime files, known private-path and credential patterns, and evaluation-case coverage.

## Public evidence policy

This public package contains generalized design patterns and public references only. It intentionally excludes private project names, local file paths, customer context, internal work records, and unverifiable production claims.

## License

MIT. See [LICENSE](LICENSE).

## Further distribution

A standalone skill is the first release target. Package it as a Codex/ChatGPT plugin only after the standalone version has stable trigger behavior and public feedback.

## Standards

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Agent Skills specification](https://agentskills.io/specification)
