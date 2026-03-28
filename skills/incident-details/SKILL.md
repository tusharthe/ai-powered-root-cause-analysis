---
name: incident-details
description: Collect incident information step by step for RCA drafting. Use when starting or updating an RCA, gathering what/when/impact/evidence details, or filling missing mandatory RCA sections.
---

# Incident details (RCA)

## Goal

Collect incident facts in a fixed order, keep factual sections free of unverified speculation, and produce or refresh a markdown RCA draft using the Output Format below. When information is missing, ask targeted follow-ups or mark placeholders explicitly (for example `pending`).

## Required RCA Sections

Each section is mandatory in the final output. Define "done" as follows:

- **Incident summary**: Neutral statement of what failed or degraded, which system or scope, and how it manifested. No blame or unproven causes.
- **Impact**: Who or what was affected (users, regions, tenants), duration or window, SLA or contractual notes if known, and material effects (data, revenue) only when verified.
- **Timeline**: Chronological events with time references; timezone or UTC must be explicit; note precision (exact time vs approximate).
- **Root cause**: Mechanism that allowed the incident plus contributing factors when supported by evidence. Use `pending` if not yet verified.
- **Solution**: Corrective change that restored or contains the issue, or `pending` if not decided or not yet applied.
- **Action items**: Concrete follow-ups; include owner and target date when known. Use `- [pending or known]` style bullets until filled.
- **Mitigation plan**: How recurrence will be prevented, detected earlier, or recovered faster; `pending` if not yet defined.

## Collection Workflow

1. Clarify whether this is a new RCA or an update to an existing draft; reuse or extend prior sections when updating.
2. Gather **incident summary**, then **impact**, then **timeline**; ask follow-ups until systems, boundaries, and times are specific enough to be useful.
3. Capture **evidence pointers** (log groups, queries, ticket IDs, dashboards, commit or deploy references). Do not paste secrets, tokens, or unnecessary PII.
4. Only after facts and timeline are solid, draft **root cause**, **solution**, **action items**, and **mitigation plan** from what is supported; label gaps as `pending`.
5. Emit the full document using **Output Format** and briefly list any remaining gaps or assumptions.

## Data Quality Rules

- Separate **facts** (observed, logged, ticketed) from **hypotheses**; do not present guesses as facts in summary, impact, or timeline.
- Tie root cause and solution statements to evidence when possible; say `pending` instead of inventing detail.
- Use one consistent time basis (UTC recommended); state it once if all times share it.
- Distinguish **time of detection**, **start of user-visible impact**, and **time of mitigation or fix** when they differ.
- Do not paste credentials, session tokens, or full PII; reference secure locations instead.

## Output Format

Use this structure for the RCA draft:

```markdown
## Incident summary
[facts]

## Impact
[facts]

## Timeline
[ordered events with time references]

## Root cause
[current known cause or "pending"]

## Solution
[proposed/implemented fix or "pending"]

## Action items
- [pending or known]

## Mitigation plan
[pending or known]
```
