# Workflow lifecycle

Two modes share one underlying loop: standing up a project for the first time (greenfield), and
extending or fixing one that already exists (brownfield, the steady state every project reaches
eventually). Greenfield runs a few phases once, in order, before the loop starts; brownfield runs
the same loop directly, scoped to one change at a time.

A spec-first, big-picture pass followed by many small incremental slices is the expected shape of
a project's *entire* lifetime, not a one-time exception to "small vertical slices": Phases 0–2
below establish enough shared understanding to decompose safely, and everything after that —
whether it's slice 3 of the initial build or a feature added a year later — runs the same
per-slice loop. Brownfield work gets its own lightweight version of Phases 1–2, proportional to
the change, not a rerun of the original ceremony (see *Brownfield* below).

Every "stop for human review" checkpoint below is, by default, a stop for the **stakeholder**
function (see [`02-roles-and-team-model.md`](02-roles-and-team-model.md#stakeholder)) — a project
may route a given checkpoint to a different human, but should record that choice rather than leave
it ambiguous who "the human" actually is.

## Greenfield: standing up a project

### Phase 0 — Scaffolding

Establish the knowledge architecture ([`01-knowledge-architecture.md`](01-knowledge-architecture.md)),
the entry-point file, the toolchain, and the reproducible environment (a clean checkout must be
able to install, build, test, and run locally with no undocumented manual steps). Nothing about
the target system's features is decided here — only how the project will be worked on. This is
also where this standard's open parameters get resolved to an explicit value or an explicit,
recorded opt-out — review cadence, branching/release strategy, coverage threshold, whether the
designer function applies, and how (if at all) performance/cost budgets and observability/rollback
are being handled — see
[`00-philosophy.md`](00-philosophy.md#every-open-parameter-gets-an-explicit-answer) and
[`templates/starter-prompt.md.template`](../templates/starter-prompt.md.template). On a project
that already has code or history, this phase is strictly additive: preserve whatever already
exists, merge deliberately rather than overwrite, and verify that no existing, observable
behavior of the system changed as a result — scaffolding that quietly alters behavior has
overrun its scope. **Stop for human review** before proceeding; this is the cheapest point in the
whole project to catch a structural mistake.

### Phase 1 — Plan

The planner function decomposes the specification into slices with acceptance criteria, a
dependency order, a risk register, and an open-questions log (see
[`02-roles-and-team-model.md`](02-roles-and-team-model.md#planner)). **Stop for human review.**

### Phase 2 — Architect

The architect function resolves the cross-cutting decisions the plan doesn't: contracts, data
model, the concrete test strategy, performance/cost trade-offs, and any decision expensive to
reverse later, each recorded (see
[`07-documentation-and-decisions.md`](07-documentation-and-decisions.md)). Where the project has a
designer function, it resolves design-system and accessibility decisions alongside the architect
in this same phase. **Stop for human review.**

### Phase 3…N — Implement, one slice at a time

Run the per-slice loop below until the plan is exhausted. Do not start the next slice until the
current one closes — except for independent slices being run in parallel, each in its own
isolated workspace (see
[`02-roles-and-team-model.md`](02-roles-and-team-model.md#scaling-the-model) and
[`06-source-control-and-release.md`](06-source-control-and-release.md#parallel-work)), where "the
current one" means each parallel slice individually, not the whole batch.

### Final phase — Validate and prepare release

An end-to-end pass against the specification's behaviors as a whole (not slice by slice), the
project's Definition of Done checklist completed, any manual/operational verification checklist
finished, and a summary of the work produced for the stakeholder. See
[`06-source-control-and-release.md`](06-source-control-and-release.md) for what happens next.

## The per-slice loop (used by every phase, and forever after)

This is the loop a slice runs through regardless of whether it's part of the initial build or a
brownfield change made a year later. It is deliberately the same loop so that "adding a feature"
and "building the first feature" are not, structurally, different processes.

1. **Restate** the slice's acceptance criteria (happy path, edge cases, failure modes) from the
   plan or the change request, including any performance/cost or design/accessibility
   implications relevant to this slice. If they're not explicit yet, that's the first thing to
   fix — an implementer should never be inferring acceptance criteria from the request title.
2. **Write failing tests** covering those criteria, before any implementation code.
3. **Implement** the minimum needed to make them pass.
4. **Run every quality gate** (see [`04-quality-gates.md`](04-quality-gates.md)) — all green,
   nothing skipped, no reduced coverage accepted "for now."
5. **Validate** independently against the specification, with tests the validator wrote itself
   (see [`02-roles-and-team-model.md`](02-roles-and-team-model.md#validator)).
6. **Review** for quality, standards, documentation, knowledge promotion, and boundaries (see
   [`02-roles-and-team-model.md`](02-roles-and-team-model.md#reviewer)).
7. **Commit** on a branch, with the durable-knowledge promotion done and scratch cleaned (see
   [`06-source-control-and-release.md`](06-source-control-and-release.md)).
8. **Report** the outcome; pause for stakeholder/human review at the cadence decided during Phase
   0 (every slice, every few, or at milestones — smaller/higher-risk projects should default to
   more frequent checkpoints). That cadence is a setup-time decision, not one renegotiated slice
   by slice: once it's recorded, execution proceeds against it without needing a fresh human
   decision each time a slice closes.

A slice does not close with a failing or skipped test, a lowered coverage bar, or a "changes
requested" review left unaddressed, regardless of schedule pressure.

## Brownfield: the steady state

Once a project has shipped once, essentially all further work — a new feature, an enhancement, a
bug fix, a refactor — is a slice (or a small number of slices) run through the loop above,
preceded by however much of Phases 1–2 the change actually needs:

- **A small, well-scoped change** may only need the loop itself: acceptance criteria are already
  clear enough to restate directly.
- **A change with real design ambiguity or cross-cutting impact** needs a lightweight planning
  and/or architecture pass first — proportional to the size of the ambiguity, not a full re-run
  of Phases 1–2's original ceremony. If it requires revisiting a standing architectural decision,
  the architect function creates a new ADR that supersedes the old one and explicitly records what
  the change means for the project as a whole, not only for the slice that prompted it (see
  [`07-documentation-and-decisions.md`](07-documentation-and-decisions.md#revising-a-decision)).
- **A bug fix** runs the same loop with the acceptance criterion being "the reported failure no
  longer reproduces, and a regression test proves it won't silently recur."

What does not change between greenfield and brownfield: test-first, every gate green, independent
validation and review, documentation travels with the change, and decisions get recorded. A
brownfield project that quietly drops these because "it's just a small fix" is how rigor erodes.

## When the standard itself changes

This lifecycle is itself governed by this standard, which can change (see the root
[`CHANGELOG.md`](../CHANGELOG.md)). A project doesn't need to react to every change immediately —
but should periodically run the re-sync procedure in [`ADOPTING.md`](../ADOPTING.md), and always
run it when explicitly told the standard has been updated.
