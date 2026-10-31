# ADR-0003: Two declared SKILL frontmatter dialects (SKILL v0.1.1)

**Status:** Accepted
**Date:** 2026-10-31

## Context

The first fleet conformance pass (14 installed skills, 2026-10-31) found
every skill using an OpenCode-flavored frontmatter dialect
(`compatibility`, `metadata` with audience/workflow/slash fields), while
SK-1 as written demanded the skillkit distribution dialect
(`allowed-tools`, `license`). Forcing one dialect would break either the
packaging toolchain or the whole live fleet.

## Decision

SK-1 splits into core fields (required everywhere: `name` lowercase-hyphen,
`description` under 1024) plus two declared dialects: distribution
(adds `allowed-tools`, `license`; validated by skillkit) and opencode
(adds `compatibility`, `metadata`). Dialects are declared in the standard,
never accidental. The fleet conformance pass also swept every skill clean
of the em-dash character and fixed two name-format violations.

## Consequences

- Positive: the live fleet is conformant without churn; packaged skills
  keep the stricter distribution dialect; the standard describes reality.
- Negative: two dialects to keep declared; a third dialect requires an
  ADR here.
