<table>
<tr>
<td width="33%">
  <img src="assets/trellis-icon.png" alt="Trellis" width="100%">
</td>
<td width="67%">

# Trellis

Trellis is a technology-agnostic, harness-agnostic standard for how a software project is
planned, architected, built, tested, reviewed, released, and maintained — by any mix of humans
and AI agents. It is written to be **read once by whoever is setting up a project's process**,
then translated into that project's own concrete, project-specific artifacts. It is not a
library, a framework, or something a project depends on at runtime.

</td>
</tr>
</table>

This standard was distilled from a real project's development process, after that process
carried the project all the way from a blank repository through active brownfield maintenance
without the rigor breaking down. It has been stripped of everything specific to that project —
no language, no cloud provider, no AI harness is assumed anywhere in `principles/`. Wherever a
concrete instantiation is useful, it's illustrated with a placeholder or a range of real-world
examples, never a single canonical stack.

## A playbook, not a set of directions

This is guidance for building a robust process, not a script that decides your project's answers
for you. Adopting it means answering a set of open questions this standard deliberately leaves
open — a coverage number, a branching strategy, a review cadence, whether a design/accessibility
function even applies to what you're building — and recording those answers explicitly (see
[`00-philosophy.md`](principles/00-philosophy.md#every-open-parameter-gets-an-explicit-answer)).
Hitting an open question during setup is not a sign the standard is incomplete; it's the standard
working as intended. The pitch is closer to: tell us what you're building, your tech stack, and
your release strategy, and this gives you back a robust, checkable process — not "do it this
exact way." [`templates/starter-prompt.md.template`](templates/starter-prompt.md.template) is
built around asking exactly these questions up front.

## Who this is for

- A **new project**, greenfield: read this before writing the first line of code, and use it to
  produce your own `AGENTS.md`, standards, workflows, and role definitions.
- An **existing project**, brownfield: read this when told the standard has changed, to bring
  your process artifacts back in sync. See [`ADOPTING.md`](ADOPTING.md).
- A **human, a solo developer with an AI assistant, or a multi-agent team**: the role model and
  workflow scale down as well as up — see
  [`principles/02-roles-and-team-model.md`](principles/02-roles-and-team-model.md).
- Any **AI coding harness** — this file makes no assumption about which one. See
  [`principles/09-ai-harness-agnosticism.md`](principles/09-ai-harness-agnosticism.md) for how to
  map the concepts here onto whatever tool you're actually using today.

## How this folder is organized

| Path                | Answers                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------- |
| [`principles/`](principles/) | **Why and what.** The standard itself — durable, project-agnostic reasoning and rules. Read these in numeric order the first time through. |
| [`templates/`](templates/)   | **How, as a starting point.** Copyable, fill-in-the-blank files an adopting project instantiates into its own repository and then edits until they stop being generic. |
| [`ADOPTING.md`](ADOPTING.md) | The step-by-step procedure: bootstrapping a new project from this standard, and re-syncing an existing one after the standard changes. |
| [`CHANGELOG.md`](CHANGELOG.md) | A dated log of what changed in the standard itself and why — the thing you diff against when re-syncing. |

## The principles, at a glance

1. [**Philosophy**](principles/00-philosophy.md) — the tenets everything else follows from: care
   over speed, evidence over assumption, small vertical slices, test-first, docs travel with
   behavior, human judgment on anything ambiguous or irreversible.
2. [**Knowledge architecture**](principles/01-knowledge-architecture.md) — the three-tier split
   of durable project knowledge, durable process knowledge, and disposable scratch, and why
   mixing them causes decay.
3. [**Roles and team model**](principles/02-roles-and-team-model.md) — the nine functions a
   rigorous process separates (even when one person or one agent plays several) — including the
   stakeholder, who decides what gets built, and the designer, who owns UX/accessibility where
   the project has a user-facing surface — and the boundaries between them.
4. [**Workflow lifecycle**](principles/03-workflow-lifecycle.md) — the phases of standing up a
   new project, the per-slice loop that both initial build and ongoing maintenance run on, and
   when the standard itself needs re-syncing.
5. [**Quality gates**](principles/04-quality-gates.md) — the categories of automated check every
   project needs, technology-agnostic, and how to instantiate them concretely.
6. [**Testing discipline**](principles/05-testing-discipline.md) — test-first in practice, what
   "don't fake reality" means, and how to handle the parts of a system that genuinely can't be
   automated.
7. [**Source control and release**](principles/06-source-control-and-release.md) — branching,
   commit hygiene, and the deliberate human gate between "integrated" and "released."
8. [**Documentation and decisions**](principles/07-documentation-and-decisions.md) — why docs
   travel with the behavior they describe, and how decisions get recorded so they survive the
   people who made them.
9. [**Security and boundaries**](principles/08-security-and-boundaries.md) — least privilege,
   secrets, and why the people or agents who build a system should not be the same ones who can
   touch its production instance, unsupervised.
10. [**AI harness agnosticism**](principles/09-ai-harness-agnosticism.md) — translating roles,
    permission boundaries, and delegation into whatever tool you're actually running.
11. [**Glossary**](principles/10-glossary.md) — short definitions of the terms used throughout,
    in one place.

## What this standard deliberately does not do

- It does not name a programming language, framework, cloud provider, or AI product. Every
  principle is phrased so it holds for a Python data pipeline, a Rust CLI, a mobile app, an
  embedded firmware project, or a static site — built by one person or by ten agents.
- It does not pretend one team size fits all. Every role-and-process principle says explicitly
  how it compresses for a solo developer and expands for a larger team.
- It does not manage dependencies, licenses, or third-party compliance — that's your toolchain's
  job, not a process standard's.
- It does not prescribe observability, incident response, or rollback mechanics — those are too
  project- and technology-specific to template usefully; it requires that a project decide them
  explicitly during setup instead of by default neglect (see
  [`08-security-and-boundaries.md`](principles/08-security-and-boundaries.md#operational-readiness-is-a-project-specific-decision)).
- It does not ship worked examples of its own templates filled in — see "What this folder is
  organized" above: `principles/` is the reasoning, `templates/` is the fill-in-the-blank
  starting point, and an adopting project's own instantiation is the example.
- It does not freeze in time. It is expected to change as practice improves; see
  [`CHANGELOG.md`](CHANGELOG.md) and [`ADOPTING.md`](ADOPTING.md) for how adopting projects stay
  current without being surprised by a change.

## Where to start

- Setting up a new project? Start with [`ADOPTING.md`](ADOPTING.md) → "Bootstrapping a new
  project." If there's no scoping/requirements document yet, start one step earlier with
  [`templates/starter-prompt.md.template`](templates/starter-prompt.md.template) — the kickoff
  prompt that has an agent produce that document and a recommended approach before setup begins.
- Have an existing codebase with its own history but no formal process yet? Bootstrapping
  applies to you too — see [`ADOPTING.md`](ADOPTING.md) → "Bootstrapping a new project" and run
  [`templates/scaffolding-prompt.md.template`](templates/scaffolding-prompt.md.template), which
  is written to be safe and non-destructive on a non-empty repository.
- Told to re-sync an existing project against an updated standard? Start with
  [`ADOPTING.md`](ADOPTING.md) → "Re-syncing an existing project."
- Just want to understand the reasoning? Read `principles/` in order, starting with
  [`00-philosophy.md`](principles/00-philosophy.md).
