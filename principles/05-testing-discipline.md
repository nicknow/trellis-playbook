# Testing discipline

The correctness gate ([`04-quality-gates.md`](04-quality-gates.md)) only produces trustworthy
signal if the tests behind it are written and structured with discipline. This principle is about
that discipline, independent of any specific test framework.

## Test-first, in practice

1. Read the slice's acceptance criteria and enumerate the cases: the happy path; edge cases
   (boundaries, empty/missing input, duplicates or collisions, unusual but valid input); and
   failure modes (invalid input, missing dependencies, permission failures, malformed or
   adversarial input).
2. Write the failing tests for those cases — one assertion per meaningful behavior, named for the
   *behavior* it proves, not for the implementation detail that happens to satisfy it today.
3. Run them and **confirm they actually fail**. A test that passes before any implementation
   exists is either redundant or isn't exercising the behavior it claims to — either way, it's not
   yet a real test.
4. Implement the minimum needed to make them pass. Resist adding behavior beyond what the
   criteria call for — that belongs in its own, separately-tested slice.
5. Run the full gate suite. Then hand off to independent validation (see
   [`02-roles-and-team-model.md`](02-roles-and-team-model.md#validator)), which writes and runs
   its own tests derived from the acceptance criteria — not the implementer's tests re-run, and
   not a read-through of the implementer's test file — and adds edge cases and regression
   coverage the implementer may not have thought of.

## Emulate reality; don't fake it

Prefer testing against a real (if local, sandboxed, or in-memory) instance of whatever a
component depends on, over a hand-written stand-in that only approximates its behavior. A
database dependency should run real schema/migrations against a real local or embedded instance
of that database, not a mock that quietly diverges from the real schema over time. A mock is
appropriate only for the parts of a dependency that genuinely cannot be run locally — a paid
external API, a piece of hardware, a third-party identity provider — and even then, the mock
should be built to fail loudly if the real interface it's standing in for changes shape.

The reasoning: a suite that's all green against mocks proves the code satisfies the *mocks'*
assumptions, which is a different and weaker claim than proving it satisfies the *real system's*
behavior. Mocked-vs-real divergence is a classic source of "tests passed, production broke."

## Coverage is a floor, not a target

See [`04-quality-gates.md`](04-quality-gates.md#coverage). Concentrate testing effort on
logic-heavy, low-external-dependency code — the parts of a system where a bug is a pure reasoning
error, not an environment quirk — since that's both the highest-value code to cover thoroughly
and the cheapest to test well.

## Things that cannot be automated

Some behavior is real but structurally hard to exercise in an automated test: a live third-party
integration with no usable sandbox, a physical/hardware interaction, a production-only
configuration, a manual approval flow. Don't pretend these are tested by writing a hollow test
that doesn't actually exercise the real risk. Instead:

- Name the seam explicitly as untestable-by-automation, and why.
- Maintain a manual verification checklist (in permanent project knowledge, not scratch) that
  whoever operates the real system runs through — see
  [`02-roles-and-team-model.md`](02-roles-and-team-model.md#deployer--operator).
- Where possible, still unit-test the *logic* around the untestable seam (e.g., mock only the
  literal external call, and assert the surrounding code constructs the right request and handles
  the right range of responses) even though the seam itself isn't covered end to end.

A project with an honest, maintained manual checklist for its untestable seams is in a stronger
position than one with a green test suite that silently doesn't cover them.

## The non-negotiables

- No slice closes with a failing or skipped test, or a lowered coverage bar, to save time.
- No test is deleted or disabled to make a gate pass without first understanding why it failed.
- Validation is independent: whoever verifies a slice against the specification is not verifying
  their own implementation of it in the same pass, and does so with tests it wrote itself against
  the specification — not tests borrowed, read, or adapted from the implementer's own suite. "The
  implementer's tests pass" is evidence about the implementer's tests; it is not validation.
