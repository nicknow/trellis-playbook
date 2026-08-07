# Changelog

A dated log of changes to the standard itself — not to any project that adopts it. This is what
an adopting project reads when re-syncing: everything dated after the project's own "last synced"
date (see [`ADOPTING.md`](ADOPTING.md)) is new to them.

Entries are dated `YYYY-MM-DD` and written for someone deciding whether a change affects their
project, not for someone reading the diff. State what changed, why, and who needs to act on it.

## 2026-08-07 — Named "Trellis"

The standard is now named **Trellis**, ahead of its first publish. Previously it referred to
itself only generically ("this standard," "the Playbook"). No content changed — this is a naming
pass only, so that the project has a stable proper noun to reference from adopting repositories.
It's commonly referred to as "Trellis" or "the Trellis playbook"; "playbook" remains fine as a
lowercase, generic descriptor of what it is, not as the project's name.

- `README.md` title and opening line now name Trellis explicitly.
- `ADOPTING.md`'s sync-marker snippet (step 6 of bootstrapping) now links to `Trellis` instead of
  `the Playbook`.
- Every `templates/*.template` file that referenced "the Playbook" as this project's proper name
  now says "Trellis" instead.

**Action for adopting projects:** if your `AGENTS.md` (or equivalent) sync-marker line reads
"this project follows the Playbook," update it to "this project follows Trellis" on your next
re-sync. No process or reasoning changed, so this can be folded into any other re-sync pass rather
than done urgently on its own.

## 2026-08-07 — Stakeholder/designer roles, explicit-parameter discipline, and clarified scope

Driven by an outsider's read of the standard ahead of a real kickoff: several places assumed an
implicit "the human" without naming who that was, left open parameters (coverage numbers, branching
strategy, review cadence) that could silently survive as unfilled brackets, and under-specified how
independent validation, accessibility, performance/cost, and parallel work were actually supposed
to work. This entry resolves those without adding anything this standard previously said it
wouldn't do (dependency/license management and templated observability/rollback mechanics remain
explicitly out of scope — see `README.md`).

- **Two new functions, nine total** (`principles/02`): **stakeholder** (owns the spec, backlog
  priority, and is the default authority for ambiguous/irreversible/consequential decisions —
  gives the role that "stop for human review" was implicitly deferring to a name) and **designer**
  (owns UX, the design system, and accessibility standards where a project has a user-facing
  surface, including the cost/benefit call on design asks — not applicable to projects with none).
  New templates: `templates/roles/stakeholder.md.template`, `templates/roles/designer.md.template`.
  Every other role template, `team-brief.md.template`, `AGENTS.md.template`, and the workflow
  templates were updated to reference them.
- **Independent validation is stricter, explicitly.** The validator writes and runs its own tests
  derived from the acceptance criteria; it must not read, borrow, or rely on the implementer's test
  file, and "the implementer's tests pass" is not validation evidence. Previously implied by
  "independent," now stated outright in `principles/02`, `principles/05`, and the validator/
  test-standards/testing-loop templates.
- **Every open parameter now requires an explicit answer or an explicit, recorded opt-out** — new
  tenet in `principles/00`. Applies to (and is now called out by name in) the coverage threshold
  (`principles/04`), branching/release strategy (`principles/06`), human-review cadence
  (`principles/03`), and whether the designer/performance/accessibility categories apply at all.
  A project can still decide "no coverage number" or "no designer function" — it just has to say
  so, not leave a bracket unfilled.
- **Performance and cost** are now a named, continuous concern (new tenet in `principles/00`, new
  gate category in `principles/04`, touched in every phase of `principles/03` and in the planner/
  architect role templates) rather than unaddressed.
- **Accessibility and design** is now a named gate category (`principles/04`), owned by the new
  designer function rather than left to whichever role happened to touch the UI.
- **Branching strategy is reframed as a project choice**, not a mandate: `principles/06` now
  states the underlying invariant ("release is a deliberate act, not a merge side effect") and
  gives two example shapes — the two-branch integration/release split, and trunk-based with
  feature flags — rather than prescribing the former.
- **Parallel slice work is now designed, not just asserted**: `principles/06` adds a "Parallel
  work" section (isolated workspaces — devcontainer instances or git worktrees — per slice, merged
  to a feature branch, orchestrator sequences merge order), referenced from `principles/02`'s
  scaling guidance and the implementer/planner/team-brief templates.
- **Revising an architecture decision is now explicit**: `principles/07` adds "Revising a
  decision" — any ADR can be superseded, the architect function owns it, and must assess the
  change's impact on the whole project, not just the slice that prompted it. Referenced from
  `principles/02` (architect) and `principles/03` (brownfield).
- **Observability, incident response, and rollback strategy** are explicitly named as
  project-/technology-specific decisions made during setup, not templated by this standard —
  new note in `principles/08`, and an explicit question in `templates/starter-prompt.md.template`
  Part 1. This is a clarification of existing scope, not new prescription.
- **Dependency and license management** are now explicitly named in `README.md`'s "what this
  standard doesn't do" list — always out of scope, now stated rather than merely absent.
- **New glossary** (`principles/10-glossary.md`): short, deliberately non-prescriptive definitions
  for slice, gate, function/role, tier, ADR, boundary, human review checkpoint, greenfield/
  brownfield, Definition of Done, and open parameter.
- **`templates/starter-prompt.md.template` rewritten**: leads with "this is a playbook, not
  directions — open questions are expected," and Part 1 now has the agent walk a fixed checklist
  of this standard's open parameters (stakeholder identity, designer applicability, branching
  strategy, coverage number/opt-out, performance/cost, operational readiness, parallel work) and
  either resolve each from the brief or raise it explicitly, instead of leaving them to be
  inferred later. `README.md` states the same framing up front.
- Explicitly **not** added, on review: worked/filled-in examples of the templates (this standard
  ships principles and fill-in-the-blank templates only, deliberately — see `README.md`);
  dependency/license management tooling; templated observability/rollback mechanics.

**Action for adopting projects:** re-run `ADOPTING.md` → "Re-syncing an existing project." At
minimum: name who plays the stakeholder function; decide whether a designer function applies and,
if so, who plays it; confirm your coverage threshold and branching strategy are recorded as
explicit decisions rather than template defaults; confirm your validator role isn't reading the
implementer's tests. Projects with no user-facing surface should record "designer: not
applicable" explicitly rather than silently omitting the role.

## 2026-08-04 — Initial extraction

The standard was distilled from a single project's real development process — one that carried
it from an empty repository through active brownfield maintenance without the process breaking
down. Everything specific to that project's language, cloud provider, or AI harness was
generalized away or removed; what's left is the reasoning and structure that made the process
work, independent of any of those choices.

Established in this initial version:

- The three-tier knowledge architecture (`principles/01`): permanent project knowledge, permanent
  process knowledge, disposable scratch.
- The seven-function role model (`principles/02`): orchestrator, planner, architect, implementer,
  validator, reviewer, deployer/operator — and how it compresses for small teams.
- The phased lifecycle and per-slice loop (`principles/03`), reused for both initial build and
  ongoing maintenance.
- Technology-agnostic quality-gate categories (`principles/04`) and testing discipline
  (`principles/05`).
- Branching/release model (`principles/06`), documentation-and-decisions discipline
  (`principles/07`), and the security/boundary rules separating build from operate
  (`principles/08`).
- Harness-agnosticism guidance (`principles/09`) and a full set of copyable templates under
  `templates/`.
- The starter-prompt kickoff template (`templates/starter-prompt.md.template`): a fill-in prompt
  that has an agent turn a project's own brief into a scoping/requirements document and a
  recommended approach, get it approved, then run the bootstrap procedure in `ADOPTING.md`.
- The scaffolding-prompt template (`templates/scaffolding-prompt.md.template`): a narrow,
  self-verifying prompt for standing up (or retrofitting) just the three-tier knowledge
  architecture and entry-point file, safe to run on a repository that already has code and
  history — it preserves existing content and verifies no existing behavior changed. `Phase 0`
  in `principles/03` and the bootstrap procedure in `ADOPTING.md` now call out this
  non-destructive, retrofit-safe case explicitly.

**Action for adopting projects:** none — this is the baseline. Projects bootstrapping from
scratch should treat this date as their initial "last synced" date (see `ADOPTING.md`).
