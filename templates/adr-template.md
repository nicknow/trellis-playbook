<!--
  Template: a single Architecture Decision Record, plus the index-file conventions around it.
  See trellis/principles/07-documentation-and-decisions.md.

  Usage: copy the "One ADR" section below into `NNNN-short-title.md` in this project's ADR
  directory (next sequential number), fill it in, and add a row to that directory's index file
  (modeled on the "Index file" section below).
-->

## One ADR (`NNNN-short-title.md`)

```markdown
# NNNN: <title>

- Status: proposed | accepted | superseded by NNNN
- Date: <YYYY-MM-DD>

## Context

<What prompted this decision? What options were considered?>

## Decision

<What was chosen, and why. Cite sources for any external/platform fact this rests on — see
trellis/principles/00-philosophy.md#evidence-over-assumption. If this ADR supersedes an earlier
one, name it and state what changed — a new constraint, new information, or a decision that
turned out wrong — see trellis/principles/07-documentation-and-decisions.md#revising-a-decision.>

## Consequences

<Trade-offs. What this enables or forecloses. What would need to change to reverse it. If this
supersedes a prior decision, what does the change mean for the *rest* of the project — not just
whatever slice or symptom prompted revisiting it?>
```

## Index file (`[adr dir]/README.md`)

Keep a table of every ADR — number, title (linked), status — so a reader can scan the decision
history without opening every file. When a number is intentionally skipped (a decision reserved
then dropped, or scope that got folded into an amendment elsewhere), leave a note explaining the
gap rather than silently renumbering — the gap is itself part of the project's history.
