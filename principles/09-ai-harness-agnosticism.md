# AI harness agnosticism

Every principle above is stated without naming a tool, on purpose: the reasoning holds whether a
project is worked on by hand, by a single AI assistant, or by a coordinated multi-agent system —
and which specific product provides that system will keep changing over the project's lifetime.
This section is the only place in `principles/` that talks about harness mechanics, and it does
so at the level of *concepts to map*, not a list of current products to depend on.

## The concepts that need a home in whatever harness you use

| Concept | What it needs from the harness |
| --- | --- |
| Entry-point routing | Something a fresh session reads first that points to the permanent-knowledge tiers (see [`01-knowledge-architecture.md`](01-knowledge-architecture.md)). Most current harnesses look for a conventionally-named root file automatically. |
| Role definitions | A way to give a session a distinct, scoped brief — instructions, and ideally a restricted toolset — matching one function from [`02-roles-and-team-model.md`](02-roles-and-team-model.md). |
| Delegation | A way for one session (the orchestrator) to hand a bounded task to another session (a role) and receive its result back, without the two sharing full context. |
| Permission scoping | A way to grant or deny specific tools/actions per role — most importantly, denying the build-time roles any tool that reaches real production systems (see [`08-security-and-boundaries.md`](08-security-and-boundaries.md)). |
| Human approval gates | A way to pause and require explicit human sign-off before a specific action, not just before a whole session. |
| Disposable scratch | A workspace a role can write to freely that isn't itself treated as authoritative or depended on by other roles. |

If a harness (or a human-only process) can't express one of these mechanically, the concept still
applies — it just has to be enforced by convention and discipline instead of tooling. A solo
developer with a single chat-based AI assistant and no subagent support still separates
"implementing" from "validating" as distinct, deliberate passes, and still keeps that scratch out
of anything considered authoritative; the harness just isn't doing the separating for them.

## Adapter notes (illustrative, expected to go stale)

These are examples of how the concepts above have mapped onto specific tools at the time this was
written — useful as a starting point, not as something to trust without checking current
documentation for whatever harness is actually in use (see
[`00-philosophy.md`](00-philosophy.md#evidence-over-assumption)).

- **A CLI-based coding agent with subagent/delegation support:** role definitions as separate
  prompt files or configured subagent types; a primary/orchestrator session delegates to them via
  a task-delegation tool; permission scoping via a settings/permissions file that allow- or
  deny-lists tools per agent; project-level conventions and standing instructions in a root
  markdown file the harness loads automatically.
- **An agent framework with an explicit team/config file:** the team of roles, their prompts, and
  their tool permissions declared together in one configuration file alongside the repository;
  agent definitions as separate files the config references.
- **An IDE-integrated assistant with project-level rule files:** role separation achieved by
  switching which rule file or mode is active for a given pass (planning vs. implementing vs.
  reviewing), since many IDE-integrated tools have weaker built-in delegation than CLI agents.
- **No AI at all, or a chat-only assistant with no project-file awareness:** every mechanical
  concept above becomes a human discipline instead — a checklist followed by hand, roles played
  as deliberate mental-mode switches, scratch kept in an obviously-temporary location by
  convention. This standard was written to hold up completely in this mode; the mechanical
  versions are conveniences, not requirements.

## What to do when the harness changes

Re-derive the mapping, don't port configuration blindly. When a project adopts a new or updated
harness, re-read this file and [`02-roles-and-team-model.md`](02-roles-and-team-model.md), then
re-express the same roles, boundaries, and gates in the new harness's actual mechanisms — a
migration is an opportunity to notice if the mapping had drifted from the underlying intent, not
just a file-format conversion exercise.
