---
name: rca-iteration-policy
description: Guides RCA drafting and review cadence—what to do and avoid, including scrutiny on partial drafts without requiring all mandatory sections first. Use when combining incident collection, solution scrutiny, and iteration; or when avoiding a finalize-all-sections gate before review.
---

# RCA iteration policy

## Goal

Keep RCAs factual and complete for publication while allowing **early scrutiny** and **iterative** improvement. This skill does not replace [rules/rca-mandatory-sections.mdc](rules/rca-mandatory-sections.mdc) or [skills/incident-details/SKILL.md](skills/incident-details/SKILL.md); it adds workflow expectations only.

## What to do

- When **producing or publishing a complete RCA**, still include all mandatory `##` sections in order and use `pending` for unknowns (see workspace rule and incident-details skill).
- Keep **Incident summary**, **Impact**, and **Timeline** grounded in verified **facts**; use **Root cause** / **Solution** with evidence or `pending`.
- Use one **consistent time basis** (UTC recommended); separate **detection**, **user-visible impact**, and **fix/mitigation** when they differ.
- Reference logs, tickets, and dashboards; **do not** paste secrets, tokens, or unnecessary PII.
- Run **solution scrutiny** when reviewing root-cause and fix quality: [skills/solution-scrutiny/SKILL.md](skills/solution-scrutiny/SKILL.md).

## What not to do

- **Do not** require every mandatory section to be complete **before** running scrutiny, peer review, or solution-quality checks. Partial drafts with explicit `pending` are valid inputs to review.
- **Do not** block iteration: refine sections after scrutiny; do not treat “all sections finalized” as a prerequisite that must come before any critique.
- **Do not** state hypotheses as facts in summary, impact, or timeline.
- **Do not** invent evidence, times, or impact to fill sections; use `pending` and list gaps instead.

## Related

- Mandatory section definitions and skeleton: [rules/rca-mandatory-sections.mdc](rules/rca-mandatory-sections.mdc)
- Step-by-step collection: [skills/incident-details/SKILL.md](skills/incident-details/SKILL.md)
- Root-cause and solution review output: [skills/solution-scrutiny/SKILL.md](skills/solution-scrutiny/SKILL.md)
