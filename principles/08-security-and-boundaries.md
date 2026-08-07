# Security and boundaries

## Build and operate are separate, structurally

Whoever writes and tests a system's code should not, in the same capacity, hold unsupervised
access to that system's real, live production environment — its real infrastructure, real
credentials, real user data. This holds regardless of whether "whoever" is a person or an AI
agent, and regardless of how much that person or agent is trusted; the point is structural, not a
statement of distrust. A build process that can also silently reach production has no reliable
boundary preventing an untested or unreviewed change from reaching real users, and no
after-the-fact way to distinguish "the build process did this" from "the operator deliberately
did this."

Concretely: assign the deployer/operator function (see
[`02-roles-and-team-model.md`](02-roles-and-team-model.md#deployer--operator)) its own identity,
its own credentials, and — wherever the tooling allows expressing it — its own explicit
permission grant, separate from whatever identity does the building and testing. Deny the build
function any credential or tool that could reach the real production system, so that "the build
team can't reach production" is a property enforced by configuration, not merely an instruction
that's trusted to be followed. Where the tooling can require a human approval on every
production-reaching action (not just a one-time grant), use it.

This generalizes past "cloud provider": the same separation applies to a production database, a
payment processor, a fleet of physical devices, a live customer-facing queue, or any other system
where a mistake is expensive, hard to reverse, or affects real third parties. If a project has no
such system (e.g., a library with no runtime infrastructure of its own), this principle has
nothing to separate — say so rather than inventing a boundary that isn't needed.

## Least privilege by default

Every role, human or agent, and every credential or tool grant, gets the minimum access that
function actually needs — not the maximum that's convenient. Widen access only when a specific,
justified need appears, and prefer narrowing it back down once that need has passed over leaving
a broad grant in place "in case it's useful again."

## Secrets

Real credentials, tokens, and keys never appear in source control, in permanent project
documentation, or in any committed configuration — only placeholders do (an example environment
file, a documented variable name). Real values exist only in the environment of whoever is
actually authorized to use them, provisioned through whatever secret-management mechanism fits
the project, and are never echoed, logged, or pasted into a chat transcript, an issue, or a
disposable scratch file that might get shared.

## Human approval for consequential actions

Anything that is irreversible, reaches a real external system, spends real money, or is otherwise
consequential in a way this standard's default autonomy doesn't cover, gets explicit human
approval before it happens — not a retroactive review after the fact. This is
[`00-philosophy.md`](00-philosophy.md#human-judgment-on-anything-ambiguous-irreversible-or-consequential)
made operational: where a harness or tool can be configured to require approval per action rather
than granting a standing permission, prefer that.

## Operational readiness is a project-specific decision

Observability (logging, metrics, alerting), incident response, and rollback strategy are real and
important, but this standard deliberately does not template them: what "monitoring" means for a
Cloudflare Worker, a mobile app, and an embedded device have almost nothing in common, and a
generic prescription here would be worse than none. Resolve them explicitly during setup instead —
[`templates/starter-prompt.md.template`](../templates/starter-prompt.md.template) asks the
question so it gets a real answer (even if that answer is "not applicable yet, revisit before
first real release") rather than silently defaulting to nothing. Once decided, the deployer/
operator function is who owns running them for real (see
[`02-roles-and-team-model.md`](02-roles-and-team-model.md#deployer--operator)).

## Scope discipline is a security property too

Work that quietly exceeds the scope of what was asked isn't just a process problem (see
[`00-philosophy.md`](00-philosophy.md#scope-discipline)) — unreviewed scope creep is exactly the
kind of change that bypasses the scrutiny the rest of this standard is built to guarantee. New
capability ideas go to a backlog or open-questions log; they don't appear unannounced inside a
slice that was scoped to something else.
