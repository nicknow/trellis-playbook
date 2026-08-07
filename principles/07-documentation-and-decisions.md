# Documentation and decisions

## Docs travel with behavior

If a change alters something described in permanent project knowledge — an interface, a data
model, an operational procedure, a documented behavior — the doc is updated in the same unit of
work, not scheduled for later. "Later" is where documentation debt comes from: it competes with
whatever the next priority is and reliably loses, and the change that invalidated the doc is no
longer fresh in anyone's context by the time someone gets to it.

Write for a reader who has never seen the project before, human or agent. Prefer explaining *why*
a thing is the way it is over restating *what* it is — the "what" is often visible in the code or
config directly; the "why" is the part that disappears if it isn't written down.

## Decisions get recorded

Any decision that would be expensive or risky to silently reverse later — a technology choice, an
architectural boundary, a security-relevant trade-off, anything resolved by picking one option
among several plausible ones — gets written down as a short, permanent, timestamped record, close
to the code it affects. A common form is the **Architecture Decision Record (ADR)**: one file per
decision, capturing context (what prompted it, what was considered), the decision itself (with
citations if it rests on external facts — see
[`00-philosophy.md`](00-philosophy.md#evidence-over-assumption)), and consequences (what it
enables or forecloses). See
[`templates/adr-template.md`](../templates/adr-template.md).

The point of an ADR is not ceremony — it's making the *next* decision cheaper, by letting whoever
reconsiders a choice later see what was actually known and weighed at the time, instead of
re-deriving it from scratch or guessing at the original reasoning from the code alone.

## Revising a decision

Any ADR can be superseded — a decision made under one set of constraints can turn out to be wrong,
or the constraints can change. The architect function (see
[`02-roles-and-team-model.md`](02-roles-and-team-model.md#architect)) owns this, and it is a
first-class, expected event, not something the standard treats as exceptional.

What makes a revision different from just editing the old file: write a **new** ADR that names the
one it supersedes (and update the old one's status — see `templates/adr-template.md`), and before
adopting it, evaluate what the change means for the **whole project**, not only for the slice or
symptom that prompted revisiting it. A decision that looked local when it was first made (a data
shape, a caching model, a module boundary) is frequently load-bearing for other parts of the
system by the time it's revisited — the architect's job in a revision is specifically to find and
record that blast radius, not just to bless the new answer. If the revision does turn out to be
genuinely local, say that explicitly too, so a future reader doesn't have to re-derive it.

## An index, not a pile

Permanent project documentation should be discoverable through a short index describing what each
section answers (architecture, interfaces, operations, decisions, and whatever else the project
needs) — see [`templates/docs-index-README.md.template`](../templates/docs-index-README.md.template).
A pile of undated, unindexed files is functionally close to no documentation at all, because
nothing tells a reader where to start or what's current.

## Traceability, lightly

Where a project labels units of work (slice numbers, ticket IDs, milestone names), it's worth
letting decision records, commit messages, and plan documents reference those labels — it turns
"why is this the way it is" into a short lookup instead of an investigation. This is a convenience,
not a requirement; don't invent a labeling scheme a project doesn't otherwise need.
