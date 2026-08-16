# Public Design Rationale

This reference explains the reusable reasoning behind the skill. It contains generalized patterns and public sources only. It is not a substitute for current-product evidence or real-user research.

## 1. Repeated work should become easier

Systems often know the current object, a configured default, a last confirmed choice, or a related prior record. Reuse that context when the field contract and risk allow it, but keep the source inspectable and preserve manual edits.

Useful pattern:

- filter eligible options by tenant, permission, status, validity, and domain rules;
- keep the current value and explicit user intent first;
- use scoped, decayed confirmed-use signals to improve discovery;
- retain search and a stable fallback so adaptive ordering cannot hide the complete option set.

Public basis:

- [Apple Human Interface Guidelines: Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data)
- [Apple Human Interface Guidelines: Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning)
- [GOV.UK Design System: Select](https://design-system.service.gov.uk/components/select/)
- [W3C WCAG 2.2: Redundant Entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html)

## 2. Ordering, recommendation, prefill, and submission are different controls

A ranking signal should help discovery. A recommendation adds an explanation. Prefill writes a reversible starting value. Submission creates a formal effect. Treating these as one default mechanism can convert convenience into an unintended decision.

Generalized example:

- a recently confirmed shipping location may rank near the top;
- a location related to the current order may be recommended with a reason;
- a field-specific rule may prefill a safe default into an untouched field;
- the order still requires confirmation appropriate to its consequences.

## 3. Progressive disclosure should reduce, not relocate, complexity

Keep common work visible and move genuinely rare or advanced capability behind a clear entry. Do not hide required actions or split fields that users must compare together. Two levels are a useful target rather than a universal hard limit.

Public basis:

- [Nielsen Norman Group: Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)
- [Apple Human Interface Guidelines: Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls)
- [GOV.UK Service Manual: Structuring forms](https://www.gov.uk/service-manual/design/form-structure)

## 4. One authoritative mutation path does not require one UI entry

Users may need a contextual quick action in a list, a complete editor in a detail view, and a task-specific action on a workbench. These can remain consistent when they invoke the same domain command, validation, permission, audit, idempotency, and recovery behavior.

Use deep links when context or risk makes inline editing inappropriate. Use contextual actions when they materially reduce navigation without creating a second business implementation.

## 5. Automation should preserve control and recovery

Automate deterministic, low-risk, reversible work. Use suggestions or prefill when uncertainty remains. Preview and confirm consequential writes. Preserve human judgment for regulation, exceptions, final acceptance, and conclusions the system cannot verify.

Public basis:

- [Microsoft Research: Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/)
- [Google PAIR Guidebook: Feedback and Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/)
- [Google PAIR Guidebook: Mental Models](https://pair.withgoogle.com/guidebook-v2/chapter/mental-models/)

## 6. Lower friction needs a protection metric

Fewer fields or steps can be harmful if the system creates wrong defaults, overwrites manual input, repeats writes, or exposes cross-scope history. Pair an effort metric with a protection metric.

Examples:

- effort: required fields, manual decisions, navigation steps, task time, or interruption points;
- protection: corrected defaults, overwritten manual values, duplicate writes, permission failures, or cross-scope exposure.

Without telemetry, use a scripted task and report the observed result. Do not invent improvement percentages.

## 7. Accessibility and recovery are functional behavior

The expected task must remain discoverable and operable through the supported device and input contract. Clear labels, focus behavior, target size, permission states, error explanations, and recovery paths belong to functional acceptance rather than optional polish.

Public basis:

- [W3C WCAG 2.2: Consistent Identification](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html)
- [Apple Human Interface Guidelines: Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion)
