# ADR-0001: One monorepo for L0 + L2 standards

**Status:** Accepted
**Date:** 2026-10-31

## Context

The standards estate needs a home. Options: repo per standard, sections
inside the two existing canons, or one standards monorepo.

## Decision

One repository (`standards`): STANDARDS-CORE.md (L0 meta-standard) plus
domain standards under `standards/` (L2), the registry (standards.yml),
and the auditor (standards-audit.py). OMNI-CORE invariant 3 applies:
monorepo-first; repo = unit of consistency. The universal canons
(engineering-standards, spec-standards) remain separate repos: they
predate this one, have their own CI toolchains, and are L1, not L2.

Escape hatch: a domain standard splits into its own repo when it needs a
toolchain the monorepo does not carry. Splitting requires an ADR here and
a registry update; the registry is the dependency contract, so consumers
do not change.

## Consequences

- Positive: one audit, one CI, one loop for all L2 standards; cross-standard
  dependency changes land atomically.
- Negative: the canons are governed by a document living in a sibling repo
  (mitigated: L1 conformance is declared by ADR in each canon).
- Risks: monorepo bloat; the escape hatch is the release valve.
