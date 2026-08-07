# Knowledge architecture

A project built or maintained across many separate working sessions — separate human sittings,
separate AI agent sessions, or both — cannot rely on anything surviving in a participant's head
between sessions. The only knowledge that persists is what got committed. That constraint is why
knowledge is deliberately split into three places, by how long it stays true and who needs it —
and the split matters whether or not any AI is involved at all; it is just more visible once
sessions stop sharing memory.

## The three tiers

### Permanent project knowledge

Answers: **how does the system work, and how do I build, run, test, and operate it?**

Architecture, interface/data contracts, operational runbooks, and the record of every
significant decision. Written for a reader — human or agent — who has never seen the project
before, and expected to stay accurate: a change that alters described behavior updates this
tier in the same unit of work (see
[`00-philosophy.md`](00-philosophy.md#documentation-travels-with-behavior)).

This is the tier a user of the finished system, a new contributor, or an operator needs. It says
nothing about *how the team works* — only about the system itself.

### Permanent process knowledge

Answers: **how should anyone — human or agent — work on this project?**

Reusable role definitions, coding/test/commit standards, and repeatable workflows/procedures.
This tier is allowed to *reference* the permanent project knowledge (e.g., "coding standards
follow the toolchain decisions recorded in the decision log") but must never duplicate its
content — a fact stated in two permanent places will eventually be true in only one of them.

This is the tier this standard itself lives at, one level removed: this standard is process
knowledge *about how to build a project's own process knowledge*.

### Disposable scratch

Answers: **nothing durable.** Working notes, drafts, and in-progress reasoning that only matter
while a specific task is being solved. Not committed as authoritative (a repository may choose to
track it for auditability, but never treat it as a dependency), and safe to delete once the task
closes.

If more than one role or session works on a project concurrently, each gets its own scratch
location, and — critically — **no role's work depends on the contents of another role's
scratch.** If one participant's output is needed by another, it has already been promoted to a
permanent tier; it is never read out of someone else's disposable notes.

## The governing rule

> If a future contributor — human or agent, with or without any memory of this session — will
> benefit from a piece of information, commit it to a permanent tier.
> If the information is only useful for getting through the current task, it stays in disposable
> scratch.

In practice: a decision, a discovered constraint, or a convention is written into its permanent
home *during* the work that discovered it, not reconstructed later from notes. Promotion is not
a cleanup step performed at the end — it's how the permanent tiers get built in the first place.

## Anti-patterns

- **Stranding durable knowledge in scratch.** If it's only findable by digging through a
  disposable working file, it is invisible to the next contributor and might as well not exist.
- **Duplicating permanent project knowledge into permanent process knowledge, or vice versa.**
  Two authoritative copies of the same fact is a guarantee that one goes stale.
- **Copying scratch into a permanent tier wholesale.** Scratch is written for the person who
  wrote it, mid-task; a permanent doc is written for a stranger. Promoting knowledge means
  rewriting it for the new audience, not pasting the working notes in unedited.
- **Letting one participant's work depend on another's scratch.** This silently recreates shared
  memory between sessions that were supposed to be independent, and breaks the moment the scratch
  is cleaned up.

## The entry point

A project maintains one short, stable entry-point file at its root (conventionally named
`AGENTS.md`, though any consistently-used name works) that does none of the above work itself —
it only routes a new contributor to the permanent tiers, in the order they should be read. It
stays small deliberately: detailed knowledge belongs in the tiers it points to, never in the
entry point itself. See [`templates/AGENTS.md.template`](../templates/AGENTS.md.template).
