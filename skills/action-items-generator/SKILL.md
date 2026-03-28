---
name: action-items-generator
description: Generate preventive, system-focused RCA remediation tasks with ownership and measurable outcomes. Use after root cause and solution are validated or when the user asks for RCA action items.
---

# Action items generator

Generate **Action items** for an RCA after root cause and solution are understood (or clearly marked `pending` with stated gaps). Align tone with [rules/rca-blameless-tone.mdc](rules/rca-blameless-tone.mdc); fit the **Action items** section in [rules/rca-mandatory-sections.mdc](rules/rca-mandatory-sections.mdc).

## Requirements Per Action Item

Each item must include:

- **Title**: Short, imperative, describes the change (system, process, or documentation)—not a person’s mistake.
- **Intent**: One line—**prevent** recurrence, **detect** earlier, or **recover** faster—tied to a specific lever from root cause or solution.
- **Owner**: Role or team (e.g. `Platform`, `SRE`, `Team-<service>`); use `TBD` only if the user has not named an owner.
- **Due**: Target date or sprint/milestone; use `TBD` when unknown.
- **Measurable outcome**: What “done” looks like (metric threshold, checklist, merged PR, runbook section exists, alert fires on X).
- **Link to cause** (optional but preferred): Which part of root cause or gap this addresses.

Avoid duplicating the immediate **Solution** hotfix unless the item extends it (e.g. harden, automate, or document the same path).

## Quality Criteria

- **System-focused**: Changes to code, config, infra, automation, alerts, runbooks, training material—not blame.
- **Actionable**: Verifiable completion; no vague “be more careful” or “review later.”
- **Scoped**: One primary outcome per item; split broad work into multiple items.
- **Prioritized**: Mark **P0/P1/P2** or order by risk reduction if the user wants prioritization.
- **Realistic**: Do not invent owners, dates, or internal tools; use `TBD` and ask one clarifying question if needed.

## Output Template

Paste using this structure (repeat the item block as needed):

```markdown
### Action item: [short title]
- **Intent**: prevent | detect | recover — [one line]
- **Owner**: [role/team or TBD]
- **Due**: [date or milestone or TBD]
- **Measurable outcome**: [how we know it is done]
- **Addresses**: [root-cause or gap reference]

## Action items

- [ ] **[short title]** — Owner: … | Due: … | Outcome: …
- [ ] **[short title]** — Owner: … | Due: … | Outcome: …
```

The `## Action items` list is the form that drops into the RCA body; the `###` blocks are optional detail the user can keep in an appendix or ticket body.

## Action items

When only the RCA section is needed, output **only** the `## Action items` block with checklist lines, each summarizing title, owner, due, and outcome in one line (or two lines per item if clarity needs it). Use `- [ ]` for open work; use `- [x]` only if the user confirmed completion.
