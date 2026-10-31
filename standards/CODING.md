# CODING: coding standard

> **Status: CURRENT (v0.1.0, 2026-10-31)**

**Layer:** L2 · **Depends:** STANDARDS-CORE@^0.1, ENGINEERING@^1 · **Date:** 2026-10-31

## Scope

Language-level coding rules for estate repositories. The lint and CI
configuration is the primary standard; this document records only the
rules that lints cannot express, per language, and cites the gate that
enforces each.

## Dependencies

Inherits ENGINEERING (gate matrix tiers, scripts canonical) and SPEC
(DOC-STYLE register; REQ doc-comment anchors).

## Invariants

| Id | Statement | Why | Enforcement |
|---|---|---|---|
| CO-1 | Rust: `clippy -D warnings` (pedantic at tier A); `unwrap_used`, `indexing_used`, `panic` denied at tier A | panics on hostile input are the estate's top defect class | rust-kit.yml quality matrix |
| CO-2 | Rust: `std`-bound surface is feature-gated (`std` feature, default on); `alloc` uses `hashbrown`; no 64-bit-only atomics without a critical-section fallback | no_std claims must hold on thumbv7em; the 2026-09 audit fixed nine crates the hard way | embedded gate (`embedded: true`) |
| CO-3 | Parsers of untrusted input are total: typed errors, never panic; every decoder gets a fuzz target | half-open probe storms and truncated inputs are the norm on the wire | fuzz job (tier A) + THREAT-MODEL template |
| CO-4 | Public items carry REQ doc-comment tags; every REQ maps to at least one named test (SPEC-CORE §4) | traceability from law to code | REQ cross-check (advisory, blocking 2027-01) |
| CO-5 | Error handling composes estate crates (errcode, app-error, http-error); ad-hoc string errors do not cross crate boundaries | error taxonomy is part of the wire contract | review + clippy groupings |
| CO-6 | Performance claims in doc comments carry the measurement (criterion commit), never adjectives | DOC-STYLE register applies to code comments | doc-style gate |
| CO-7 | Python: ruff + strict typing on `scripts/` that CI mirrors (estate-audit, spec-audit, standards-audit) | the scripts are the contract; an untyped script is an untested contract | kit workflow (python-kit.yml) |
| CO-8 | Generated or vendored files are excluded from review scope via the repo's declared excludes (`.doclint-exclude`, cargo-deny bans), never by silence | silent exclusions are how drift hides | doc-lint + cargo-deny configs |

## Gates

The engineering gate matrix (rust-kit.yml, python-kit.yml, node-ci.yml
per language) is the enforcement surface; this document adds nothing that
a gate cannot fail on.

## Grounding

`engineering-standards` README gate matrix + 2026-09 no_std audit results;
`wire-kit` SPEC (totality + fuzzing); `spec-standards` SPEC-CORE §4;
`homebite-scraper` ops scripts.
