# Low-Friction Product Checklists

Read only the sections relevant to the current task. Do not add features merely to satisfy a checkbox.

## Task and proposal gate

- [ ] State the user outcome in one sentence without naming a page or control.
- [ ] Identify the expected entry, completion signal, and next step after completion.
- [ ] Separate frequent primary work, infrequent maintenance, and administrator work.
- [ ] Record authoritative data, confirmed-use evidence, and the authoritative mutation path.
- [ ] Identify risk, reversibility, cost, permission, and required human judgment.
- [ ] State what the system already knows and what it must ask.
- [ ] Define the smallest complete path and explicitly name what is out of scope.

## Information architecture gate

- [ ] Emphasize a primary action only when the current state genuinely has one; group equally valid actions by task, object, or risk.
- [ ] Keep frequent work discoverable without hiding it under “More” or a deep detail page.
- [ ] Give advanced capability one clear secondary entry with an informative label.
- [ ] Route the same business action through one authoritative command, validation, permission, and audit path; allow multiple contextual UI entry points when useful.
- [ ] Layer browse, create, import, review, and administration by task frequency.
- [ ] Use familiar business language consistently across surfaces.
- [ ] Preserve the object, filters, scroll position, or unfinished progress on return.

## Recent use, ordering, and defaults gate

- [ ] Define candidate eligibility, current-value preservation, display ordering, recommendation, automatic prefill, and formal submission separately.
- [ ] Enforce permission and scope before reading, aggregating, caching, persisting, or displaying history.
- [ ] Define which events count as real use; exclude views, expansion, hover, and system exposure.
- [ ] Define scope by user, organization, role, device, project, customer, or task type as applicable.
- [ ] Treat active selection or explicit acceptance as a strong signal, untouched prefill as at most a weak signal, and system automation as no preference signal.
- [ ] Let pins or favorites affect ordering by default; require an explicit “set as default” action before they affect prefill, and never equate them with submission.
- [ ] Keep the current value and current context visible ahead of adaptive history.
- [ ] Keep stable name or code fallback ordering after recent and frequent candidates.
- [ ] Add search for long lists and stable groups only when grouping improves comprehension.
- [ ] Freeze order while a selection surface is open.
- [ ] Exclude unauthorized, inactive, expired, and cross-scope options from recommendation.
- [ ] Apply a recency window, decay, or cap so old habits do not dominate indefinitely.
- [ ] Keep new and complete option sets reachable; avoid self-reinforcing recommendation loops.
- [ ] Show a historical current value when necessary without treating it as a valid candidate for a new record.

## Prefill and state-memory gate

- [ ] Reuse known information through prefill, selection, or reference instead of requesting repeated entry.
- [ ] Make the automatic value's source inspectable, such as current contract, latest confirmed order, or organization default.
- [ ] Let users edit or clear automatic values and fill only blank or still-automatic fields.
- [ ] Protect manual edits from asynchronous responses, refresh, and upstream-object changes.
- [ ] Recalculate affected fields only when an upstream object changes, and explain consequential replacement.
- [ ] Distinguish copy from reference; snapshot business facts that must remain frozen.
- [ ] Do not guess amounts, dates, tax rates, entities, identities, permissions, or missing historical facts.
- [ ] Prevent local memory on shared devices from exposing customer, financial, or personal data.
- [ ] Restore filters, pagination, scroll position, current object, or unfinished draft only when the task benefits.
- [ ] Provide clear-history, reset-default, and show-all paths.
- [ ] Define retention and behavior after sign-out, account changes, and permission changes.

## Input and cognitive-load gate

- [ ] Require each field for delivery of the actual service.
- [ ] Keep defaults safe, visible, editable, and unable to create silent business facts.
- [ ] Organize options by decision value rather than raw frequency or internal structure.
- [ ] Show format, range, and examples at the point of input rather than requiring recall.
- [ ] Keep interdependent information available for comparison; use steps only for genuinely sequential work.
- [ ] Show a few options directly; use search or autocomplete for large sets instead of a very long dropdown.
- [ ] Keep expert shortcuts from taking over the new-user path.

## Automation and safety gate

- [ ] Consider automatically completing deterministic, low-risk, reversible steps.
- [ ] Present uncertain results as editable and rejectable suggestions, drafts, or prefill.
- [ ] Preview the target, scope, consequence, and cost of high-impact or irreversible actions.
- [ ] Match confirmation strength to action risk without creating confirmation fatigue.
- [ ] Make duplicate submission idempotent or detectable so it cannot silently create duplicate business facts.
- [ ] Preserve user input on failure and provide correction, retry, or human takeover.
- [ ] Keep automated output separate from human acceptance, publication, and approval status.

## State and permission gate

- [ ] Give clear feedback for the normal state and the loading, empty, processing, success, partial-success, and failure states that actually exist.
- [ ] Explain blocked, disabled, and insufficient-permission states with a viable next step.
- [ ] Remove dead actions and retry loops for unavailable capability.
- [ ] Report progress for long work and say whether the user may safely leave.
- [ ] Make success feedback state what was written and what remains incomplete.
- [ ] Use user language for errors and identify both the problem location and recovery path.
- [ ] Keep help and recovery entry points consistent across related surfaces.

## Focused acceptance gate

- [ ] Complete one end-to-end main task from the expected entry point.
- [ ] Review entry and next-action discoverability from a first-time user's perspective.
- [ ] When claiming lower friction, select one effort metric and one protection metric; use a scripted task when telemetry is unavailable and do not invent improvement rates.
- [ ] Test ordering with no history, one candidate, multiple candidates, confirmed history, and inactive history.
- [ ] Verify that prefill never overwrites a manual edit.
- [ ] Verify memory isolation across users, organizations, roles, devices, and permission changes.
- [ ] Verify recovery after repeated clicks, navigation, refresh, network failure, or model failure as applicable.
- [ ] Verify distinct surfaces for read-only, write, administrator, and no-permission roles.
- [ ] Verify declared target devices and dimensions; on unsupported devices prevent data damage and irreversible action and explain limitations.
- [ ] Verify keyboard focus, semantic labels, touch targets, contrast, and non-color signals for supported input methods.
- [ ] Label focused automated tests, browser checks, manual review, and real-user acceptance separately.

## Anti-feature-pile gate

Before adding visible capability, answer:

1. Which observable user friction does it solve?
2. At which existing task stage will users look for it?
3. Is it primary work, an advanced option, or administrator maintenance?
4. Which existing entry can it merge with, replace, or remove?
5. If it is secondary, will its entry remain discoverable?
6. How does it change state, permission, error, memory, and recovery behavior?
7. What evidence justifies the added interface complexity?

Defer the feature when questions 1, 2, 3, or 7 have no clear answer. Merge instead of adding a parallel entry when possible.
