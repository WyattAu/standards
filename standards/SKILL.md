# SKILL: agent skill standard

> **Status: CURRENT (v0.1.0, 2026-10-31)**

**Layer:** L2 · **Depends:** STANDARDS-CORE@^0.1, ENGINEERING@^1, SPEC@^1 · **Date:** 2026-10-31

## Scope

Agent skills in the estate: structure, frontmatter, packaging, validation,
and projection rules. Does not govern skill *content quality* beyond the
register rules inherited from DOC-STYLE.

## Dependencies

Inherits ENGINEERING (scripts canonical, agent-facing contract 11i, SBOM
and release attestation) and SPEC (prose register, citation rule,
projection freshness SC-11).

## Invariants

| Id | Statement | Why | Enforcement |
|---|---|---|---|
| SK-1 | Frontmatter fields are exactly `name`, `description`, `allowed-tools`, `license`; `name` is lowercase-hyphen, at most 64 chars | agents route on description; a rogue field breaks the parsers | `skillkit lint` (crates: skillkit) |
| SK-2 | `description` states what the skill does and when to load it, under 1024 chars | the description is the routing key; a vague description is an unloaded skill | `skillkit lint` |
| SK-3 | Executable steps live in `scripts/`, long-form prose in `references/`; SKILL.md stays lean | progressive disclosure; a 5k-word SKILL.md burns every caller's context | `skillkit lint` + review |
| SK-4 | `allowed-tools` is minimal and honest | a skill with write access is a mutation surface; least privilege (OMNI-CORE 10) | `skillkit lint` + review |
| SK-5 | A skill that repackages canon content is a projection: it carries a PROVENANCE file with the source repo and rev, is rebuilt by the canon's CI, and a stale pin fails the canon gate | skills multiply drift surfaces; SC-11/11p | build.sh --check in the canon CI |
| SK-6 | Packaged skills record the pack hash in release notes | consumers pin an artifact, not a vibe | release procedure (skillkit pack) |

## Gates

`skillkit lint <dir>` (frontmatter + structure), `skillkit pack <dir>`
(hash), projection freshness via `build.sh --check` in standards-dist.

## Grounding

`OmniSkill-template` (canonical frontmatter + layout, "validated by
skillkit"), `skillkit` (lint/pack/verify/audit crates), `agentic-awesome-skills`
(collection), `standards-dist` (projection implementation with PROVENANCE.yml).
