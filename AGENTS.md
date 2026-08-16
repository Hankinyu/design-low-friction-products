# Open-Source Skill Working Agreements

## Scope

- Treat `skills/design-low-friction-products/` as the distributable runtime package.
- Keep the runtime package English-only. Human translations belong outside the package.
- Never copy local absolute paths, private project names, customer data, internal status claims, credentials, or local memory references into this repository.

## Editing

- Keep `SKILL.md` concise, imperative, and under 500 lines.
- Preserve the distinction between eligibility, value preservation, ordering, recommendation, prefill, and submission.
- Update the relevant evaluation cases when trigger scope or user-visible behavior changes.
- Do not add dependencies or scripts unless they provide repeatable validation that cannot be expressed clearly in instructions.

## Verification

- Run `python3 scripts/validate.py` after changes.
- Review `evals/trigger-cases.json` for both positive and negative English and Chinese prompts.
- Treat static checks as repository evidence only; do not describe them as real-user acceptance.

## Publication

- Do not create a remote repository, add a remote, push, publish, or submit a plugin without explicit user authorization for that exact target.
- Keep Gitea as the default destination for unrelated repositories. GitHub is only for work the user explicitly designates for open-source publication.
