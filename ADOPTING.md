# Adopting Trellis

Two procedures: bootstrapping a project that has never used this standard, and re-syncing a
project that has, after the standard itself has changed. Both apply whether the work is being
done by a human, a single AI agent, or a coordinated team of them — and bootstrapping applies
equally to a brand-new empty repository and to an existing project with its own code and history
that simply never adopted this standard before. In the latter case, every step below is additive:
preserve whatever already exists and don't change any existing behavior; see the scaffolding
prompt in step 3.

## Bootstrapping a new project

**No scoping or requirements document yet?** Start with
[`templates/starter-prompt.md.template`](templates/starter-prompt.md.template) instead of step 1
below — it's a kickoff prompt that has an agent read the project's own brief, produce a scoping
document and a recommended technical approach, get that approved by a human, and *then* run
through steps 1–7 below as its second half. If a scoping document already exists, start directly
at step 1.

1. **Read `principles/` in order (00 through 09).** Do not skip to `templates/` first — the
   templates only make sense in light of the reasoning, and copying them without understanding
   *why* a section exists is how they silently rot.
2. **Make the decisions the standard deliberately leaves open**, and record each as an explicit
   answer or an explicit, recorded opt-out — never a placeholder (see
   [`principles/00`](principles/00-philosophy.md#every-open-parameter-gets-an-explicit-answer)):
   language/runtime, test framework, style/lint tooling, CI system, source-control host, branching
   and release strategy, which AI harness(es) will be used, the coverage threshold (or the
   decision not to use one), the human-review cadence, whether the designer function applies to
   this project, and how far performance/cost and observability/rollback are being addressed at
   this stage. Record these as the project's first Architecture Decision Records (see
   [`principles/07`](principles/07-documentation-and-decisions.md)).
3. **Stand up the knowledge architecture** ([`principles/01`](principles/01-knowledge-architecture.md))
   in the project's repository: permanent project knowledge, permanent process knowledge, and a
   disposable scratch area, plus a small `AGENTS.md` entry point. Run
   [`templates/scaffolding-prompt.md.template`](templates/scaffolding-prompt.md.template) for
   this — it's a narrow, self-verifying pass that creates the tiers and the entry point, updates
   ignore rules around scratch, and confirms nothing pre-existing was deleted or altered. It's
   safe to run on a repository that already has code and its own conventions: preserve what's
   there and merge deliberately rather than overwrite. Once it's done, fill in
   [`templates/team-brief.md.template`](templates/team-brief.md.template) with this project's
   real specifics — delete anything that doesn't apply; do not leave placeholder text in a
   committed file.
4. **Instantiate the role prompts** you need from `templates/roles/` ([`principles/02`](principles/02-roles-and-team-model.md)
   explains which roles are load-bearing at your team size — a solo developer with one AI
   assistant still needs the *checklist*, even if one session plays several functions in
   sequence). Two of the nine are worth deciding deliberately rather than defaulting: who plays
   **stakeholder** (almost always a named human, even on an otherwise autonomous build), and
   whether **designer** applies at all — skip it explicitly, rather than silently, for a project
   with no user-facing surface.
5. **Instantiate the standards and workflows** from `templates/standards/` and
   `templates/workflows/`, translating every gate category in
   [`principles/04`](principles/04-quality-gates.md) into your actual toolchain's commands.
6. **Record the sync marker.** In the project's `AGENTS.md` (or wherever its process entry point
   lives), add a line stating which version of this standard it follows:

   ```markdown
   Process standard: this project follows [Trellis](<path-or-repo-url>), last synced
   vX.Y.Z.
   ```

   Use the version at the top of this standard's `CHANGELOG.md` (equivalently, its latest git
   tag) at the time you're bootstrapping — whichever version you actually read up through.
7. **Run the lifecycle from `principles/03`**, starting at its Phase 0 (scaffolding), before any
   feature work begins.

Everything copied from `templates/` is a **starting point, not a dependency**. Once instantiated
into a project, those files belong entirely to that project; they diverge from this standard
immediately and permanently, on purpose. Re-syncing (below) never means overwriting a project's
files with fresh copies of the templates — it means deciding, entry by entry, whether a change to
the standard's *reasoning* implies a change to the project's *artifacts*.

## Re-syncing an existing project

Triggered when a human or an agent is told "the standard has been updated, bring this project's
process in line with it" — or, proactively, at whatever cadence the project chooses to check.

1. **Find the project's current sync marker** (the "last synced vX.Y.Z" line from step 6 above).
   If none exists, treat the project as never having formally adopted the standard and fall back
   to Bootstrapping, using the current state of the project's process artifacts as the starting
   point instead of the templates.
2. **Read every `CHANGELOG.md` entry versioned after the sync marker** — starting from the top of
   the file and working down until you reach the entry matching your recorded version. Each entry
   names what changed in the standard and why. Entries at or before the sync marker's version are
   already reflected (or were deliberately not adopted, which should already be recorded — see
   step 5).
3. **For each new entry, decide and record one of:**
   - **Adopt** — update the project's own artifacts (its `AGENTS.md`, standards, workflows, role
     prompts, or docs structure) to reflect the change. Reference the entry so a future re-sync
     doesn't re-litigate it.
   - **Not applicable** — the change concerns a situation this project doesn't have (e.g. a
     multi-agent coordination rule for a solo-developer project). Note briefly why, so a future
     reader doesn't wonder if it was missed.
   - **Deliberately deferred** — the change is relevant but adopting it now is disruptive or
     out of scope for the current work. Record it with a reason and revisit it explicitly later;
     don't let it silently disappear.
4. **Apply the adopted changes as normal project work**: this is not exempt from the project's own
   process. If the project's workflow requires tests, review, or a human gate for
   architecture-level or process-level changes, this goes through the same gate.
5. **Update the sync marker** to the version of the last `CHANGELOG.md` entry you actually
   processed (equivalently, the latest git tag at the time) once every new entry has been triaged.
6. **Record the re-sync itself** wherever the project keeps a durable log of process decisions
   (an ADR, a dated note in its process docs) — what was adopted, what wasn't, and why. This is
   what makes the *next* re-sync fast: it only has to read entries after this one.

### A note on drift

A project that never re-syncs doesn't become "wrong" — the standard it adopted at bootstrap time
remains a coherent, internally consistent process. What it loses is the benefit of whatever was
learned since. Re-syncing is a deliberate, occasional act of catching up, not a continuous
subscription — there is no expectation that every project tracks every change immediately.
