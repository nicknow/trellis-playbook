# Philosophy

Everything else in this standard is an application of a small number of tenets. When a situation
this standard doesn't explicitly cover comes up, resolve it by asking which choice these tenets
would favor — don't invent a new principle from scratch.

## Care and precision over speed

It is always acceptable to go slower to be correct. A rigorous process is not the fast path for
any single task — it is the fast path in aggregate, because it removes the slow, expensive
failure mode of shipping confidently wrong work and discovering it later, often far from the
change that caused it. Batching unrelated changes, skipping a gate "just this once," or marking
something done with a known gap are all speed bought against a larger, later cost. Don't buy it.

This does not mean gold-plating or excess ceremony on trivial work. It means the *size* of an
increment of work should shrink until it can be done carefully at the speed available, rather
than the care shrinking to fit an arbitrary deadline.

## Evidence over assumption

Anyone's memory of how a language, library, platform, or tool behaves is a snapshot from whenever
they last learned it — and fast-moving dependencies (cloud platform behavior, library APIs,
security guidance, pricing/limits) drift out from under that snapshot constantly. Before relying
on a fact that could have changed, verify it against a current, authoritative source and record
where the verification came from, especially in a decision record (see
[`07-documentation-and-decisions.md`](07-documentation-and-decisions.md)). This applies equally to
a human relying on memory and an AI agent relying on training data — neither is exempt.

## Small vertical slices

Break work into thin increments, each of which delivers one coherent, independently testable
behavior end to end, rather than one horizontal layer of many behaviors at once. A slice that
touches every layer but does one thing is easier to specify, test, review, and — if wrong — throw
away, than a horizontal layer that does many things but isn't usable until its siblings exist.
Prefer many small slices to few large ones, even when the large one feels more "efficient" to plan.

## Test-first

For every slice of behavior, the test that proves it exists *before* the code that implements it,
and is derived from the acceptance criteria — not written afterward to match whatever the
implementation happened to do. This is what keeps "done" meaning "verified" rather than "written."
A slice is not finished with a failing, skipped, or missing test, regardless of time pressure.

## Documentation travels with behavior

A doc that describes behavior is updated in the same unit of work that changes the behavior, not
"soon after." Documentation written after the fact, from memory, in a separate pass, is
documentation that silently drifts — because nothing forces it to stay attached to the change
that invalidated it. See [`07-documentation-and-decisions.md`](07-documentation-and-decisions.md).

## Human judgment on anything ambiguous, irreversible, or consequential

Autonomy is appropriate for well-specified, reversible, low-consequence work. It is not
appropriate for resolving genuine ambiguity in what should be built, for anything that touches
production systems or real external state, for security-relevant decisions, or for anything
user-visible that wasn't explicitly asked for. In those situations: stop, lay out the options and
a recommendation, and wait — don't guess silently and hope it was right. The **stakeholder**
function (see [`02-roles-and-team-model.md`](02-roles-and-team-model.md#stakeholder)) is who this
judgment defers to by default. See [`08-security-and-boundaries.md`](08-security-and-boundaries.md)
for how this becomes concrete role boundaries, not just a sentiment.

## Every open parameter gets an explicit answer

This standard deliberately leaves many parameters to the adopting project: a coverage threshold,
a branching/release strategy, how often to pause for human review, whether a category like
performance or accessibility applies, what "done" means for an operational seam this standard
doesn't template. None of those may be left as a placeholder, an unfilled bracket, or a silent
assumption. Each gets either a specific, recorded value, or an explicit, recorded decision not to
have one and why. "We don't use a coverage percentage because our test suite is small enough to
read in full" is a valid answer; a `[coverage threshold]` bracket surviving into a committed file
is not. This is what makes a template this standard's *starting point* rather than its
*directions* — see the root [`README.md`](../README.md) and
[`ADOPTING.md`](../ADOPTING.md) for where these questions get asked and resolved.

## Performance and cost are considered continuously

Latency, throughput, resource usage, and spend are not a phase bolted on before release — they're
a question asked at every stage: the planner weighs them when ordering slices, the architect
weighs them when choosing a design and records the trade-off, the implementer and validator check
them where they're load-bearing, and a release doesn't go out on a system whose cost or
performance profile nobody has looked at. How rigorously depends entirely on the project — a
batch script's "performance" question might be a single sentence in an ADR; a public API's might
be a load-test gate — but every project answers it deliberately, at every phase, rather than by
default neglect. See [`04-quality-gates.md`](04-quality-gates.md#performance-and-cost).

## Knowledge has a home, and scratch is not it

Anything a future contributor — human or agent, and regardless of whether they have any memory of
this session — would benefit from knowing belongs in a durable, committed location. Anything only
useful for getting through the current task belongs in disposable scratch, and should not be
depended on by anyone else. Conflating the two is how projects end up with either bloated,
untrustworthy permanent docs, or durable knowledge that only exists in a deleted temp file. See
[`01-knowledge-architecture.md`](01-knowledge-architecture.md).

## Scope discipline

New ideas, however good, are captured — in an open-questions log, a roadmap, a backlog — not
implemented silently inside unrelated work. A slice that quietly grows to cover "one more useful
thing" stops being reviewable as the thing it was supposed to be. Deciding whether a captured idea
is worth doing, and when, is the stakeholder function's call
(see [`02-roles-and-team-model.md`](02-roles-and-team-model.md#stakeholder)), not something the
build team resolves for itself.
