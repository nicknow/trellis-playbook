# Roles and team model

Rigor comes from separating *functions*, not from headcount. The same person, or the same AI
agent across different sessions, can play every role below on a small project — what matters is
that each function is performed deliberately and its output is visible, not that a different
individual performs each one. What breaks rigor is collapsing functions that need independence
from each other into a single, un-separated pass — most importantly, implementing and
independently verifying in the same breath, and building a thing and deciding it should exist in
the same breath.

## The nine functions

### Orchestrator / lead

Coordinates the others, holds the overall plan, enforces that gates are actually run rather than
assumed, and is the point of contact with the stakeholder function for review and approval. Does
not do architecture, implementation, or verification work itself — it delegates and integrates.
On a solo project this is simply the discipline of *following the workflow* rather than skipping
straight to code.

### Stakeholder

Owns the product/business intent: holds (or names who holds) the spec, prioritizes the backlog and
roadmap, and is the default authority for anything ambiguous, irreversible, or consequential that
the rest of the team escalates (see
[`00-philosophy.md`](00-philosophy.md#human-judgment-on-anything-ambiguous-irreversible-or-consequential)).
Gives the go/no-go at each human-review checkpoint in
[`03-workflow-lifecycle.md`](03-workflow-lifecycle.md). Does not write architecture, code, or
tests, and does not resolve technical trade-offs unilaterally — those come back from the architect
as options with a recommendation.

This is almost always a real, accountable human, even on an otherwise fully autonomous build: it's
the function that answers "should this exist at all," and that question doesn't get delegated to
the same system being asked to build the thing. A **stakeholder agent** may stand in for
well-precedented, low-stakes questions the real stakeholder has already answered a version of
(e.g., "does this fit our stated scope" for an obvious case) — but anything genuinely ambiguous,
irreversible, or consequential routes to the human stakeholder; an agent proxy never becomes the
final word on those, only a filter that reduces how often the human is interrupted for the easy
cases.

### Planner

Turns a specification or a feature request into a sequence of small, independently testable
slices (see [`00-philosophy.md`](00-philosophy.md#small-vertical-slices)), each with explicit
acceptance criteria, a dependency order, a risk register, and an open-questions log for anything
ambiguous. Weighs performance and cost when ordering and scoping slices — a slice with a known
performance or spend risk is sequenced and flagged, not discovered late (see
[`00-philosophy.md`](00-philosophy.md#performance-and-cost-are-considered-continuously)). Does not
write implementation code. Its output is a living plan that the rest of the process executes
against — durable project knowledge, not scratch.

### Architect

Owns the cross-cutting decisions a plan alone doesn't resolve: module/component boundaries,
interface and data contracts, the concrete test strategy, performance/cost trade-offs, and any
decision that would be expensive to reverse later. Records each such decision (see
[`07-documentation-and-decisions.md`](07-documentation-and-decisions.md)). Stays faithful to the
plan and the spec; escalates conflicts rather than resolving them by unilateral judgment call.
Owns revising a prior decision, too: any earlier ADR can be superseded, but the architect function
is the one that must evaluate what the change means for the *whole* project, not just whichever
slice surfaced the need to revisit it — see
[`07-documentation-and-decisions.md`](07-documentation-and-decisions.md#revising-a-decision).

### Designer

Owns user-facing design decisions where the project has a user-facing surface: visual and
interaction design, the design system, and accessibility standards — including the cost/benefit
trade-off of what it directs be implemented (an accessibility or design ask that costs far more
than an alternative delivering most of the same value is the designer's call to weigh explicitly,
not something silently deferred to whoever implements it). Participates alongside the architect
during Phase 2 and whenever a slice has user-facing surface: reviews that slice's acceptance
criteria for design/accessibility implications before implementation starts, and checks the built
result against the project's design and accessibility standards before the slice closes. Records
design-system and accessibility decisions the same way the architect records technical ones.

**Not every project has this function.** A library, a CLI with no UI, or a backend service with no
human-facing surface has nothing for a designer to own — say so explicitly during setup rather than
leaving an unfilled role or forcing accessibility review onto a function that doesn't own it (see
[`04-quality-gates.md`](04-quality-gates.md#accessibility-and-design)).

### Implementer

Builds one slice at a time, test-first: writes the failing tests the acceptance criteria imply,
then the minimum code to pass them (see
[`05-testing-discipline.md`](05-testing-discipline.md)). Updates the permanent-knowledge tiers
affected by the slice as part of finishing it, not afterward. Stays inside the assigned slice's
scope.

### Validator

Independent verification against the *specification*, not against the implementer's
interpretation of it, and not against the implementer's own tests. The validator writes and runs
its **own** tests, derived directly from the slice's acceptance criteria — it does not read the
implementer's test file to decide what to test, and does not treat "the implementer's tests pass"
as evidence of anything. It adds edge-case and regression tests the implementer may not have
thought of, confirms the full gate suite is green, and — for anything that genuinely can't be
automatically tested — extends the manual verification checklist rather than pretending coverage
exists (see [`05-testing-discipline.md`](05-testing-discipline.md#things-that-cannot-be-automated)).
The independence here is the load-bearing part: a person or agent should not validate their own
implementation work in the same slice, and validating "from the implementer's tests" is not
independent validation, regardless of who runs it.

### Reviewer

A read-only check of quality, standards adherence, whether documentation and durable knowledge
were actually promoted, whether scratch and secrets stayed out of what's being committed, and
whether any boundary (see [`08-security-and-boundaries.md`](08-security-and-boundaries.md)) was
respected. Where a designer function exists for the project, the reviewer also confirms the
design/accessibility check happened for any user-facing slice, rather than re-doing that judgment
itself. Returns a verdict — approve, or specific changes requested — and does not edit code
itself. Like the validator, this function loses its value if merged into the same pass that did
the implementing.

### Deployer / operator

The only function with access to real, live, external systems — production infrastructure, real
credentials, real user data — and it is kept structurally separate from every function above (see
[`08-security-and-boundaries.md`](08-security-and-boundaries.md)). It provisions, deploys or
releases, runs post-release verification against the project's own observability/rollback
approach (a project-specific decision made during setup — see
[`08-security-and-boundaries.md`](08-security-and-boundaries.md#operational-readiness-is-a-project-specific-decision)),
and handles production incidents. It does not implement application changes; issues it finds go
back through the normal slice process.

## Handoffs

Each function's output becomes the next function's input, and that handoff happens through a
permanent-knowledge tier, never through one function reading another's scratch (see
[`01-knowledge-architecture.md`](01-knowledge-architecture.md)). Stakeholder's spec and
priorities, planner's slice plan, architect's contracts and decisions, designer's design/
accessibility standards, implementer's code plus tests, validator's pass/fail with evidence,
reviewer's verdict — each is a committed artifact before the next function starts relying on it.

## Scaling the model

**Solo developer, no AI, or one AI assistant with no subagents:** every function still happens,
in sequence, inside one person's or one session's work — but as *distinct, deliberate passes*.
The discipline is: finish planning before architecting, finish architecting before implementing,
and — critically — after implementing a slice, deliberately switch into a validator mindset
(reread the acceptance criteria cold, write a fresh set of tests against them without re-reading
the implementer's tests, try to break it) before calling it done, rather than declaring victory
the moment the code runs once. Writing down each function's output as you go (even briefly) is
what makes this work; skipping the write-down is what makes solo work drift into "vibes-based
done." The stakeholder function is the one exception worth naming explicitly even at solo scale:
it's usually still a distinct real human (the person who wants the thing built) even when every
other function is one AI session — collapsing "what should exist" into the same pass as "how do we
build it" is how scope drifts silently. The designer function, by contrast, is the one most likely
to have nothing to do on a small or UI-less solo project — skip it and say so, rather than forcing
it into an unrelated pass.

**Small team or a coordinated multi-agent setup:** functions map onto distinct people, or
distinct agent sessions/subagents with distinct scoped instructions and, where the tooling
supports it, distinct permissions (see
[`09-ai-harness-agnosticism.md`](09-ai-harness-agnosticism.md)). The orchestrator delegates
explicitly rather than doing the work itself. Independent slices with no dependency between them
can be implemented in parallel, each in its own isolated workspace (a separate devcontainer
instance, a separate git worktree) on its own branch — parallelism is about isolating the
*workspaces*, not about relaxing the per-slice loop or its gates; only the merge order needs
coordinating by the orchestrator. See
[`06-source-control-and-release.md`](06-source-control-and-release.md#parallel-work).

**Larger team:** functions may further split (e.g., separate architects per subsystem, a
dedicated security reviewer alongside the general reviewer, a design system owner distinct from a
per-feature designer) but the nine functions above remain the floor — splitting further is fine,
merging validator/reviewer back into implementer is not.

## The one non-negotiable boundary

Regardless of team size: **whoever built a piece of work does not solely decide it's correct,
whoever built or operates the system is not the same unsupervised actor who can reach production,
and whoever builds the system does not unilaterally decide what gets built.** The first is the
validator/reviewer separation; the second is the deployer/operator separation; the third is the
stakeholder separation. All three exist because self-assessment, self-authorization, and
self-assigned scope are structurally unreliable, not because any individual (human or agent) is
untrusted.
