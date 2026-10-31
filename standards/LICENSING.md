# LICENSING: licensing standard

> **Status: CURRENT (v0.1.0, 2026-10-31)**

**Layer:** L2 · **Depends:** STANDARDS-CORE@^0.1, ENGINEERING@^1 · **Date:** 2026-10-31

## Scope

Which license a WyattAu repo carries, how third-party and vendored content
is licensed, and how the gates verify it. Does not pick licenses for
business-specific repos (those are the owner's call, recorded here as the
proprietary class).

## Dependencies

Inherits ENGINEERING (cargo-deny license gate, SBOM, REUSE conventions).

## Invariants

| Id | Statement | Why | Enforcement |
|---|---|---|---|
| LI-1 | Published estate crates carry `MIT OR Apache-2.0` (dual), with both license files present at the repo root | the ecosystem default: permissive, patent-tolerant, cargo-toolchain-native | `cargo-deny` licenses gate; repo tree check |
| LI-2 | Toolchain and template repos carry `Apache-2.0` | matches the toolchain ecosystem the repos compose (skillkit, cargo tooling) | repo tree check |
| LI-3 | Forks keep upstream licensing intact and unchanged | a fork that relabels upstream code is a compliance incident, not a fork | repo tree check |
| LI-4 | Private and business repos carry no open-source LICENSE file and are marked `personal` in the estate registry | an OSS license on proprietary business logic is a giveaway | estate-audit status |
| LI-5 | Vendored content keeps its upstream license with a provenance header naming source repo, rev, and path | attribution travels with the bytes (SPEC-CORE SC-8 pattern) | provenance header check on vendored dirs |
| LI-6 | A dependency adding a strong-copyleft license fails CI | license drift is silent otherwise | cargo-deny (licenses) + GitHub dependency review (OMNI-CORE 11h) |

## Gates

`cargo-deny` (licenses + bans), dependency review on PRs (11h), estate
status audit (LI-4), vendored provenance headers (spot check, SC-8).

## Grounding

`cuesheet-core`, `policy-kit` (dual MIT/Apache at root), `skillkit`
(Apache-2.0), `continuwuity`/`latex2e` (forks, upstream licenses),
`PatentSafePermissiveLicense` (owner's patent-grant preference),
`engineering-standards` `LICENSES/` + `REUSE.toml` + cargo-deny config.
