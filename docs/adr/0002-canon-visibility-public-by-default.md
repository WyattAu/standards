# ADR-0002: Standards canons are public by default

**Status:** Accepted
**Date:** 2026-10-31

## Context

STANDARDS-CORE v0.2.0 adds the visibility invariant (§8): canon repos are
public by default; private standards need an ADR naming the secrecy
interest. Rationale: standards that cannot be read cannot be followed,
and every private canon adds a scrub tax to each projection (domain
standards name estate internals today; the scrub discipline already
exists and works, but it is a recurring cost).

## Decision

`standards` is public, carries Apache-2.0 (toolchain class, LICENSING
LI-2), and states the default in STANDARDS-CORE §8. Estate internals that
must not leak stay in named private repos and are cited as
estate-internal precedent, per the scrub discipline.

## Consequences

- Positive: projections (skills, MCP, future doc site) ship without
  redaction passes; external agents can consume the standards directly.
- Negative: every canon edit re-runs the scrub check (grep for private
  repo names and business context).
- Risks: leakage through accumulated small facts; mitigated by the scrub
  check landing in CI alongside the audit.
