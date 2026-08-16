---
name: design-low-friction-products
description: Apply a low-friction product design workflow when a task materially changes a user-visible task path, information architecture, form or default behavior, option ordering, workflow automation or confirmation, system states or recovery, or interaction on supported devices. Use for planning, implementation, review, or product specifications involving human-centered design, low learning cost, progressive disclosure, recently used choices, smart defaults, prefill, reduced repeated entry, or avoiding feature pile. Do not trigger for purely internal refactors, backend-only changes, documentation of unchanged behavior, or isolated visual polish when user behavior and acceptance criteria do not change.
---

# Design Low-Friction Products

Optimize for reliable task completion. Treat feature count, page count, and technical completeness as constraints, not as success by themselves.

## Establish the task contract

Before designing, changing, or reviewing a product, derive these facts from the current product, documentation, code, and user feedback:

- who uses it, in what context, on which supported devices, and with which permissions;
- the outcome the user needs, not merely the control named in the request;
- the expected entry point and what should happen after completion;
- the frequency, risk, reversibility, and resource cost of the main path;
- existing authoritative data, business defaults, confirmed-use history, and mutation paths;
- the smallest observable friction or failing task path.

If missing facts would materially change the product direction, present a small number of choices and ask. Do not replace discoverable context with a broad questionnaire.

## Design the shortest complete path

Describe the flow in one readable sequence:

Expected entry -> recognize current state -> primary work -> necessary confirmation -> completion feedback -> next step or recovery

Apply these constraints:

- Put entry points where users reasonably expect them. A working feature hidden in a deep page is not complete.
- Emphasize a primary action only when the current state has one. When several actions are equally valid, group them by task, object, or risk.
- Let home, workbench, and detail surfaces show relevant status, blockers, next actions, and deep links. Allow high-frequency, low-risk contextual actions.
- Keep one authoritative command, validation, permission, and audit path for each business mutation. Multiple expected UI entry points may call the same command when semantics, confirmation, idempotency, and recovery remain consistent.
- Preserve the current object, selection, filters, scroll position, and unfinished progress when users return or continue.
- Name actions and states in user and business language rather than exposing internal pipelines, models, tables, or technical stages.
- Separate exploration, preview, and formal submission. After completion, state what happened and what did not happen.

## Make repeated work progressively easier

Treat recently used choices, safe prefill, remembered context, and reuse of confirmed data as normal business-system capabilities rather than optional polish.

### Separate ordering, recommendation, and prefill

- Ordering helps users find an option faster; it does not decide for them.
- Recommendation highlights a candidate and explains why; it does not silently write a value.
- Prefill writes only into fields that are empty or still automatic when the source is trusted and the risk is controlled. Let the user edit or clear it.
- Automatic submission is only for deterministic, low-risk, reversible actions that require no new business judgment.

Do not turn a recent-use signal into an automatic financial, legal, identity, permission, or other formal business fact.

### Separate eligibility, preservation, ordering, recommendation, prefill, and submission

Do not use one universal default cascade to decide all six behaviors. Define each field separately:

1. **Candidate eligibility**: Filter by tenant or organization, user permission, status, validity period, and domain rules first. Enforce scope and permission when reading, aggregating, caching, persisting, and displaying history. Never read cross-scope history and rely on the UI to hide it later.
2. **Value preservation**: Keep existing and manually entered values unless the user explicitly clears them or accepts a replacement.
3. **Automatic prefill**: Use only an authoritative object relationship, an explicitly auto-applicable default, a same-scope recently confirmed value allowed by the field contract, or a unique valid candidate that is low risk. Present other cases as recommendations instead of writing them automatically.
4. **Display ordering**: Order eligible candidates only. A useful fallback is current value or strong current-object relationship -> explicit pin or favorite -> field-specific contextual relevance or recommended default -> last explicit confirmation in the same scope -> decayed recent or frequent confirmed use -> administrator order -> stable name or code. Domain rules may reorder these signals when the result stays explainable, testable, and stable.
5. **Recommendation**: Highlight a candidate and explain the reason without silently writing it. A high rank is not automatically a recommendation, and a recommendation is not automatically a prefill.
6. **Submission**: Ordering, pins, recommendations, and prefill never equal submission. Choose confirmation based on the consequence of the formal action.

Treat a pin or favorite as a discoverability preference by default. Let it participate in prefill only after an explicit “set as default” action.

Learn from real use only. An active user selection or explicit acceptance may strongly update the last-confirmed signal. An untouched prefill may contribute at most a weak frequency signal. Page views, expansion, hover, system exposure, and automatic submission must not train user preference. Apply decay or caps so old habits do not dominate indefinitely or hide new and complete option sets.

Produce the same order for the same inputs and freeze ordering while a selection surface is open. Keep long lists searchable and keep all eligible options reachable. Add “current,” “recent,” or “frequent” groups only when they provide observable value, and provide a way to clear or reset history.

### Reuse context and prior data safely

- Prefill related fields from the current customer, contract, project, organization, last confirmed record, or trusted historical snapshot when the field contract allows it.
- Make the source inspectable, such as “from current contract” or “from latest confirmed order.” Show high-risk, non-obvious, or possibly stale sources inline.
- Fill only blank or still-automatic fields. Never silently overwrite a manual edit.
- When an upstream object changes, recalculate affected fields only. Ask or warn before replacing a manual value.
- Distinguish copying from referencing. Keep a relationship when the value should follow its source; create a snapshot when the business fact must remain frozen.
- Be conservative with dates, amounts, tax rates, legal entities, identities, permissions, and missing historical facts. Leave unknown values empty or request confirmation rather than guessing.
- On shared devices, do not store identifiable customer, project, or personal recency history in unprotected local storage by default. Prefer account-scoped server preferences or disable sensitive local memory.
- Define each memory key's scope, source, retention period, reset path, and behavior after sign-out, account changes, or permission changes.

## Control complexity without removing capability

- Keep frequent, task-critical work on the primary surface and place rare or advanced capability behind one clearly labeled secondary layer.
- Treat two disclosure levels as a target, not a hard gate. When a third level is justified by role, frequency, or risk, verify discoverability and the return path instead of merging unrelated capabilities.
- Keep fields that must be decided together visible together. Do not split interdependent comparisons into artificial one-question pages.
- Require a service-delivery reason for every field. Reuse known facts and safe defaults instead of asking twice.
- Prefer recognizable options, examples, and current values over recall, transcription, and format guessing.
- Support the common case first. Keep expert shortcuts available without letting them dominate the new-user path.
- Before adding visible capability, name the observable friction, expected entry, frequency, and relationship to existing actions. Merge, replace, or defer rather than adding another parallel button.

## Choose the automation level

Use the lowest-friction level that remains safe for the action:

1. **Automatic**: deterministic, low risk, reversible, no new business judgment, and clear feedback.
2. **Suggestion or prefill**: reduces input but retains uncertainty; allow edit, rejection, reset, and retry.
3. **Preview then confirm**: external writes, publication, batch impact, cost, finance, permission, identity, migration, or difficult reversal.
4. **Human judgment**: regulation, final acceptance, exception handling, or high-risk conclusions that cannot be verified.

Preserve the source, inputs, impact, uncertainty, audit trail, and recovery path. Never describe an AI-generated result as business acceptance or a technical test as human approval.

## Design applicable states

Cover states that actually exist in the feature's asynchronous, write, permission, and cache model. Do not manufacture states to satisfy a checklist. Cover the normal state and applicable loading or processing, empty, success or partial success, failure, blocked or disabled, insufficient-permission, and stale-data states.

For each applicable state, explain:

- what happened;
- what the user can do now;
- whether a write or cost already occurred;
- how to retry, correct, undo, take over, or get help.

Do not leave dead buttons, unexplained disabled controls, silent failures, or visible actions that permissions make unusable. Hide irrelevant capability or provide a stable explanation and alternative at the place where users reasonably expect it.

## Deliver and verify

Implement the smallest complete main path before adding states and protections required by the current risk. Read only the relevant sections of [the checklists](references/checklists.md). Use the full checklist only for a new main flow, cross-scope memory, consequential automation, or broad responsive change.

Do not load [the public design rationale](references/design-rationale.md) by default. Read it when a rule is disputed, when a public basis is needed, or when a generalized precedent would clarify the decision. A precedent shows that a pattern can work; it is not acceptance evidence for the current product.

Perform focused verification:

- complete one real main task from the expected entry point;
- verify that a new user can find and understand the next action;
- verify contextual ordering, recent and frequent signals, source-backed defaults, and stable fallback order;
- verify that asynchronous prefill, upstream changes, or refresh do not overwrite a manual edit;
- verify that user, organization, role, device, and permission changes do not leak remembered context;
- check applicable permission, disabled, failure, recovery, and duplicate-submission behavior;
- check the devices, dimensions, and input methods declared by the task contract. On unsupported devices, require no data damage or irreversible action and explain the limitation without expanding the delivery scope;
- measure overlap, overflow, and fixed regions rather than relying on a single screenshot;
- report automated evidence, manual usability review, and real-user acceptance separately.

When a change claims to reduce friction, select at least one effort metric and one protection metric, and provide a baseline and result when practical:

- effort: required fields or manual decisions, navigation steps, completion time, or primary interruption points;
- protection: manual values overwritten, wrong defaults corrected, duplicate writes, or unauthorized cross-scope exposure.

For adaptive ordering, verify a stable no-history fallback, identical ordering for identical inputs, no movement while open, and reachability of every eligible option. Without telemetry, use scripted task checks. Do not invent improvement rates or require an analytics platform for every small change.

## Output contract

For work that materially changes the main task path, defaults or memory, automation boundary, or authoritative mutation, cover the applicable items concisely:

1. the core task, expected entry, and evidenced friction;
2. the proposed path and primary versus secondary disclosure;
3. eligibility, memory, ordering, prefill, automation, permission, and recovery boundaries;
4. the minimum implementation and explicitly deferred work;
5. verification evidence, unverified items, and residual risk.

For a localized fix, report applicable items only. Do not repeat content to satisfy a template.

Classify severity consistently:

- **P0**: unauthorized or cross-scope disclosure, silent high-risk writes, irreversible data loss, divergent authoritative mutation paths, or no viable completion path for a released critical task.
- **P1**: an expected entry is hidden but a workaround exists; repeated entry, wrong or unstable defaults and ordering, missing state, permission, or recovery feedback; or supported-device usability materially blocks the task.
- **P2**: visual, wording, and consistency improvements that do not block completion.
