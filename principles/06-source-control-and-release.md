# Source control and release

Version control history is itself a permanent-knowledge artifact — it should read as a coherent
account of how the system got to its current state, not as an unstructured stream of saves.

## Branching

- One unit of work — one slice, one bug fix — gets its own branch, forked from the project's
  integration branch.
- Small, frequent, logically coherent commits on that branch. A commit is a unit a reviewer could
  reasonably evaluate on its own; "fix stuff" spanning unrelated files is not that.
- The branch merges back into the integration branch once its gates are green and it has been
  validated and reviewed (see [`03-workflow-lifecycle.md`](03-workflow-lifecycle.md)).

## The moment code goes live is a decision, not a side effect

Whatever branching/release mechanics a project chooses, the invariant is this: the moment code
becomes "live" is a deliberate, reviewed act, never an automatic or incidental consequence of a
merge. This is the concrete form of
[`00-philosophy.md`](00-philosophy.md#human-judgment-on-anything-ambiguous-irreversible-or-consequential)
applied to releases.

An urgent fix still goes through a branch, gates, and review; what changes under urgency is
priority and turnaround time, not the process itself.

This standard does not mandate one branching strategy — it's one of the open parameters a project
resolves during setup (see
[`00-philosophy.md`](00-philosophy.md#every-open-parameter-gets-an-explicit-answer)) and records,
e.g. as an ADR. Two common, valid shapes:

- **Two branches, two meanings.** Maintain a clear distinction between **where in-flight work
  lands and gets exercised together** (an integration branch) and **what is actually released or
  deployable** (a release branch). Work merges into the integration branch continuously; the
  release branch only moves when a human deliberately promotes integration into it. Nothing
  commits or merges directly to the release branch outside that deliberate promotion.
- **Trunk-based with feature flags.** Everything merges to a single main branch continuously, but
  user-visible behavior stays behind a flag until a human deliberately flips it — the flag flip
  *is* the deliberate release act, playing the same role the release-branch promotion plays above.

Whichever shape a project picks, the deliberate-release invariant above is what's actually
required; the mechanism is a project choice, not a mandate of this standard.

## Commit hygiene

- Write commit messages that explain **why**, when the diff alone doesn't make it obvious — not a
  restatement of the diff.
- A structured commit-message convention (type/scope/summary, or whatever the project adopts) is
  strongly recommended: it makes history searchable and lets tooling (changelog generation,
  release notes) derive from it. See
  [`templates/standards/commit-conventions.md.template`](../templates/standards/commit-conventions.md.template).
- A commit that touches code does not leave the correctness gate red, static analysis failing, or
  formatting dirty — see [`04-quality-gates.md`](04-quality-gates.md).
- Never commit secrets, credentials, local environment files, or scratch working notes. Stage
  deliberately; don't rely on a blanket "add everything" and hope the ignore rules catch
  everything sensitive.
- Documentation affected by a commit is updated in that same commit (see
  [`00-philosophy.md`](00-philosophy.md#documentation-travels-with-behavior)).

## Review before merge

Every branch merging into the integration branch has been through the review function (see
[`02-roles-and-team-model.md`](02-roles-and-team-model.md#reviewer)) and has green gates,
enforced by the project's CI or equivalent automation wherever the toolchain supports it — a
human (or agent) should not need to remember to run gates manually if the tooling can require it.

## Parallel work

Independent slices — ones with no dependency on each other — may be implemented at the same time
rather than strictly sequentially. Parallelism works by isolating **workspaces**, not by relaxing
anything else: each slice still gets its own branch, its own full per-slice loop
([`03-workflow-lifecycle.md`](03-workflow-lifecycle.md#the-per-slice-loop-used-by-every-phase-and-forever-after)),
and its own gates, run in its own isolated environment (a separate devcontainer instance, a
separate git worktree) so that one slice's in-progress state can't leak into another's. When
several slices compose a single larger feature, they merge into a shared feature branch first;
that feature branch merges into the integration branch (and, on its own promotion cadence, the
release branch) once the whole feature closes. The orchestrator function is what sequences merge
order when parallel slices land close together — parallel implementation does not mean parallel,
uncoordinated merging.
