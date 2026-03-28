---
name: solution-scrutiny
description: Scrutinize RCA root cause and solution quality for evidence, assumptions, and system-level reasoning. Use when reviewing RCA drafts or evaluating whether a proposed fix is complete and non-speculative.
---

# Solution Scrutiny

## Goal

Stress-test RCA reasoning without adding new facts.

## Checks

1. Are assumptions explicitly listed?
2. Are conclusions backed by evidence?
3. Is the cause framed at system/process level?
4. Are alternative plausible causes considered and addressed?
5. Is the proposed solution clearly linked to the identified cause?

## Constraints

- Do not introduce new factual claims, timelines, or evidence not present in the RCA under review; only stress-test what is stated.
- Do not treat missing data as confirmed; call out absence of evidence instead of filling gaps.
- Separate **what the RCA asserts** from **what the scrutiny infers** about logic quality.
- Stay proportional: flag material gaps, not stylistic preferences.

## Review Output

Deliver scrutiny as a single review using the sections below, in this order.

### Strengths

What the RCA does well: clear evidence ties, explicit assumptions, system-level framing, alternatives ruled out, solution–cause alignment, or timeline discipline. Use bullets; say "none identified" only if appropriate.

### Gaps to Resolve

Missing evidence, unstated assumptions, weak cause–solution linkage, shallow system/process framing, or unaddressed plausible alternatives. Each item should be actionable for the RCA author (what to gather, clarify, or rewrite).

### Assumptions Identified

List assumptions that the RCA implies or relies on, whether or not the author labeled them. Mark which are validated in-text vs unsupported.

### Recommended Revisions

Concrete edits: reorder or expand sections, add evidence pointers, narrow or elevate root cause language, adjust the solution to match cause, or add explicit assumption tables. Number or bullet; tie each recommendation to a **Check** or gap above where helpful.

Use this skeleton when pasting the review:

```markdown
## Strengths
- ...

## Gaps to Resolve
- ...

## Assumptions Identified
- ...

## Recommended Revisions
1. ...
```
