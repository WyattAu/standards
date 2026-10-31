# INVARIANTS: invariant standard

> **Status: CURRENT (v0.1.0, 2026-10-31)**

**Layer:** L2 · **Depends:** STANDARDS-CORE@^0.1, ENGINEERING@^1, SPEC@^1 · **Date:** 2026-10-31

## Scope

Invariants wherever they live: standards tables (STANDARDS-CORE §3),
runtime assertions in code, type-level and proof-level guarantees, and
repo-level truth-table commitments. This standard defines the lifecycle
shared by all of them: how an invariant is proposed, promoted, enforced,
tightened, and retired.

## Dependencies

Inherits ENGINEERING (11f formal verification, gate matrix) and SPEC
(SC-3 enforcement citations, SC-5 lifecycle).

## Invariants

| Id | Statement | Why | Enforcement |
|---|---|---|---|
| IV-1 | An invariant exists only with all four fields: id, testable statement, motivating failure mode, enforcement point | the fieldless kind are slogans; the estate runs on the four-field kind | standards-audit anatomy check; review |
| IV-2 | Promotion is evidence-gated: a runtime invariant becomes law through a failing case, an ADR, or a proof; never through agreement alone | agreement rots; a named failure mode does not | ADR + gate history |
| IV-3 | Runtime invariants on hostile paths are enforced by types first (total parsers, typed errors), assertions second, tests third | types hold for all inputs; tests sample them | clippy denials + fuzz targets (CODING CO-3) |
| IV-4 | Proof-level invariants are machine-checked with the axiom discipline: `#print axioms` per theorem, any undocumented `sorry` fails | documented behavior that is proven outranks documented behavior that is described | Lean build audit (MATH MA-3) |
| IV-5 | Tightening is always allowed; loosening is a major version event with an ADR naming the incidents that motivated the relaxation | silent loosening is how estates rot | STANDARDS-CORE §2 rule 2, semver |
| IV-6 | Every invariant's enforcement point is named and machine-checkable: a gate, a test name, a theorem name, or an ADR | unenforceable invariants are draft material (SC-3 at the invariant layer) | standards-audit + spec gates |
| IV-7 | Retired invariants keep their record: the ADR or superseding version names what replaced them and why | invariant graveyards prevent re-litigation | git history + ADR dir |

## Gates

Standards-audit anatomy check (IV-1, IV-6); Lean audits (IV-4); clippy and
fuzz legs (IV-3); semver-checks (IV-5). No new script required: this
standard binds existing gates to a shared lifecycle.

## Grounding

OMNI-CORE invariant table (the four-field pattern in production),
SPEC-CORE §3, streamformer AGENTS non-negotiables (floor rule, sorry-free),
accounting-spec Theorem 4.1 (a theorem whose violation shipped a bug:
ledger-pg 0.2.0's double-flip), graphify CI (tests asserting exact
contract strings: enforcement can even live in test fixtures).
