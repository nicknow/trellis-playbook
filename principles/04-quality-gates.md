# Quality gates

A gate is an automated check that must pass before a slice is considered closed. This standard
fixes the *categories* every project needs; each project chooses its own concrete tools and
commands to satisfy them. A project's `templates/standards/` instantiation should list the actual
commands next to each category below, so "run the gates" is one unambiguous action, not a
judgment call made fresh each time.

## The categories

### Correctness (automated tests)

The suite exercising the behavior described by acceptance criteria: unit, integration, and
end-to-end as appropriate to the system. This is the gate [`05-testing-discipline.md`](05-testing-discipline.md)
is entirely about. No failing or skipped test at the gate, ever — a skipped test is a silent gap,
not a passed check.

### Static correctness (types / static analysis)

Whatever the language and toolchain offer for catching a class of bug before runtime: a type
checker, a static analyzer, a linter's correctness rules (as opposed to its style rules). If the
language has no such tooling, this category is genuinely empty for that project — don't invent
busywork to fill it, but don't skip checking whether it's actually empty.

### Style and consistency

Formatting and stylistic-lint rules, automatically enforced rather than debated in review.
The point of automating this category specifically is to remove it from human review time
entirely — a reviewer should never be commenting on formatting a formatter could have fixed.

### Security

Whatever is proportionate to the project: secret-scanning, dependency vulnerability checks,
static security analysis. A project handling sensitive data or exposed to the public internet
needs more here than an internal CLI tool; see
[`08-security-and-boundaries.md`](08-security-and-boundaries.md) for the boundary rules this
category doesn't cover (those are process rules, not automated checks).

### Coverage

A minimum bar on how much of the behavior is actually exercised by the correctness gate, agreed
during the architecture phase as **either a specific number or an explicit, recorded decision not
to use one** — never left as a placeholder, a "TBD," or a vague aspiration (see
[`00-philosophy.md`](00-philosophy.md#every-open-parameter-gets-an-explicit-answer)). "We're not
using a coverage percentage because X" is a legitimate answer for a project that's decided the
number doesn't earn its keep; an unset threshold is not. Where a number is used, revisit it if
it's clearly wrong (too loose to mean anything, or so strict it incentivizes hollow tests).
Coverage percentage is a floor to notice regressions, not a target to be gamed — a slice with 100%
coverage and untested edge cases has not met this standard's testing discipline, whatever the
number says.

### Performance and cost

Whatever is proportionate to the project: latency/throughput budgets, load or stress testing,
resource ceilings, third-party spend limits. A public API or anything with real usage volume
needs more here than an internal batch script; see
[`00-philosophy.md`](00-philosophy.md#performance-and-cost-are-considered-continuously). If a
project has no meaningful performance or cost concern, say so explicitly — as with static
correctness above, an empty category is a decision, not an oversight.

### Accessibility and design

For any project with a user-facing surface: adherence to the project's design system and
accessibility standard, owned by the designer function (see
[`02-roles-and-team-model.md`](02-roles-and-team-model.md#designer)). Not applicable to a project
with no user-facing surface — a library, a headless service, an internal CLI — in which case say
so explicitly and skip it, rather than leaving it unaddressed or forcing it onto a role that
doesn't own it.

### Build / packaging

Whatever "build" means for the project — compiling, bundling, packaging, producing a deployable
artifact — succeeds cleanly. For projects with a size or resource constraint (a bundle-size limit,
a memory budget), that constraint is itself a gate, not a documented aspiration.

## The rule

Every gate runs, and is green, before a slice is reported as done — not "before merge" as a
separate later step, and not selectively based on how confident the implementer feels. Running
gates only sometimes is equivalent to not having them, because it means "the gates are green" is
no longer a fact anyone can trust without re-checking.

## Instantiating this for a project

A project's own standards documentation (see
[`templates/standards/`](../templates/standards/)) should, for each category above, name: the
concrete tool, the exact command, and the pass/fail bar. If a category is legitimately not
applicable to a project (e.g., no meaningful "build" step for an interpreted script with no
packaging), say so explicitly rather than leaving it silently unaddressed — a missing gate should
read as a decision, not an oversight.
