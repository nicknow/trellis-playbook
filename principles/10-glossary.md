# Glossary

Short definitions for terms this standard uses repeatedly. Kept deliberately simple — for the full
reasoning behind any of these, follow the link to the principle that owns it.

**Slice** — the largest unit of work that can be independently tested, validated, and released:
the discretely-releasable pieces a feature breaks down into. Sizing is a judgment call, not a fixed
metric — "small" means small enough to specify, test, review, and throw away if wrong, not a line
count or a time box. See [`00-philosophy.md`](00-philosophy.md#small-vertical-slices).

**Gate** — an automated check that must pass before a slice is considered closed (tests, type
checks, lint, security scan, coverage, build). See [`04-quality-gates.md`](04-quality-gates.md).

**Function / role** — one of the nine deliberate responsibilities this standard separates
(stakeholder, orchestrator, planner, architect, designer, implementer, validator, reviewer,
deployer/operator). A function is not a headcount — one person or agent can play several, in
sequence. See [`02-roles-and-team-model.md`](02-roles-and-team-model.md).

**Tier** — one of the three places knowledge lives: permanent project knowledge (how the system
works), permanent process knowledge (how anyone works on it), and disposable scratch (nothing
durable). See [`01-knowledge-architecture.md`](01-knowledge-architecture.md).

**ADR (Architecture Decision Record)** — a short, timestamped, permanent record of a decision that
would be expensive to silently reverse: what was chosen, why, and what it forecloses. See
[`07-documentation-and-decisions.md`](07-documentation-and-decisions.md).

**Boundary** — a hard rule about who or what may take an action, enforced structurally where
possible (permissions, credentials) rather than by instruction alone — most importantly, the
build/operate separation and least-privilege access. See
[`08-security-and-boundaries.md`](08-security-and-boundaries.md).

**Human review checkpoint** — a deliberate pause in the workflow where the stakeholder function
(by default) gives explicit go/no-go before work continues. Decided once, during setup, as a
cadence — not renegotiated at each occurrence. See
[`03-workflow-lifecycle.md`](03-workflow-lifecycle.md).

**Greenfield / brownfield** — greenfield is standing a project up for the first time (Phases 0–2
run once, in order); brownfield is every bit of work after that (a feature, a fix, a refactor),
each run through the same per-slice loop with only as much re-planning as the change needs. See
[`03-workflow-lifecycle.md`](03-workflow-lifecycle.md).

**Definition of Done** — the project's own checklist of what "finished" requires for a slice and
for a phase, instantiated from [`04-quality-gates.md`](04-quality-gates.md) and this standard's
non-negotiables. See
[`templates/standards/definition-of-done.md.template`](../templates/standards/definition-of-done.md.template).

**Open parameter** — anything this standard deliberately leaves for the adopting project to decide
(a coverage number, a branching strategy, a review cadence, whether a given function or gate
category applies). Every open parameter gets an explicit, recorded answer or an explicit, recorded
opt-out — never a placeholder. See
[`00-philosophy.md`](00-philosophy.md#every-open-parameter-gets-an-explicit-answer).
