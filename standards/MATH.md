# MATH: mathematical and formal standard

> **Status: CURRENT (v0.1.0, 2026-10-31)**

**Layer:** L2 · **Depends:** STANDARDS-CORE@^0.1, SPEC@^1 · **Date:** 2026-10-31

## Scope

How mathematics appears in estate artifacts: notation in specs, the
decision to formalize, proof discipline, numerics rules, and test-vector
grounding. Documentation mechanics (status stamps, REQ anchors) are
inherited from SPEC.

## Dependencies

Inherits SPEC (SC-3 enforcement citations, SC-5 lifecycle, SC-6 oracle
rule, DOC-STYLE register).

## Invariants

| Id | Statement | Why | Enforcement |
|---|---|---|---|
| MA-1 | Money is integer minor units; no floats anywhere in an arithmetic path that carries value | float rounding on value is the defect class Odoo's `float_utils.py` documents; integer addition eliminates it | accounting-spec §1 (the axiom the ledger estate is built on) |
| MA-2 | Hardware-visible division is floor division everywhere: Python `//`, Lean `Int.fdiv`, RTL `>>>`; truncating division in a numeric path is a bug even when a test passes | hardware ARSHIFT is floor; one truncating division silently desyncs reference and RTL | streamformer conformance gate (golden vectors, bit-exact) |
| MA-3 | A proof is `sorry`-free, or every `sorry` carries a documented reason it is acceptable and what closes it | an undocumented sorry is an unproven claim wearing a proof's clothes | Lean build audit (`#print axioms` / sorry grep; accounting-spec discipline) |
| MA-4 | Proofs use the weakest sufficient toolchain: `omega` for linear integer arithmetic, mathlib only when a theorem demands it | heavy dependencies rot; linear arithmetic is decidable cheaply | accounting-spec precedent (Lean 4 core only) |
| MA-5 | Golden vectors are committed, generation is deterministic, and regeneration diffs clean | a vector set nobody can regenerate is a snapshot, not a contract | spec-standards SC-6 + streamformer `make golden` |
| MA-6 | Specs containing mathematics carry a notation table before any formula: symbol, meaning, domain | notation drift between spec and proof is the spec-level analogue of a type error | spec review (SPEC-CORE §4 grounding pass) |
| MA-7 | Numeric claims carry bounds with their provenance: which lemma, which vector set, which measurement | a bound without provenance is a wish (SPEC-CORE SC-3 at the math layer) | proof audit + review |

## Gates

The Lean build audit (sorry grep + axiom printout) in proof-carrying
repos; golden-vector regeneration diff check; the spec gates at tier S
(oracle lines). These are per-repo scripts today; the estate-wide
formal-verification job is the engineering gate matrix's formal leg.

## Grounding

`accounting-spec` (integer minor units, posting algebra, omega-only Lean,
documented sorries), streamformer (floor-ARSHIFT rule, golden vectors,
bit-exact conformance), `OmniLean-template`, engineering-standards
OMNI-CORE 11f (formal verification).
