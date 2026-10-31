# STANDARDS-CORE: what a standard is

> **Status: CURRENT (v0.1.0, 2026-10-31).** Normative and living: changes
> require an ADR in `docs/adr/`, a header version bump, and a CHANGELOG
> entry. Cited by the audit as `STANDARDS-CORE §N`.

**Oracle:** No-oracle: normative process contract; the mechanical check is
`standards-audit.py` (§7).

## §1 Scope and boundary

This document defines the identity, anatomy, dependency mechanics,
lifecycle, and governance of every standard in the WyattAu standards
estate. It does not define how code is built (L1:
[`engineering-standards`](https://github.com/WyattAu/engineering-standards),
OMNI-CORE) nor how specifications and documentation are written (L1:
[`spec-standards`](https://github.com/WyattAu/spec-standards), SPEC-CORE).

| Layer | What | Where |
|---|---|---|
| L0 | the meta-standard (this document) | `standards` repo |
| L1 | universal canons | engineering-standards, spec-standards |
| L2 | domain standards | `standards/` in this repo |
| L3 | repo-level conformance (truth tables, kit specs, REQUIREMENTS) | each repo |

## §2 Layering and inheritance

1. A standard at layer N automatically inherits every invariant of the
   standards its `depends` field names, transitively.
2. A standard may **tighten** an inherited invariant (add constraints).
   It may never **loosen** one (weaken, widen, or waive).
3. Override of an inherited invariant requires an ADR in the governing
   canon repo and a registry note.
4. Conflict order between standards: L0 > L1 > L2 > L3; within a layer,
   safety-critical > regulatory > domain > general; same priority: both
   documented, impact analyzed, ADR filed.

## §3 Invariants

Every invariant, in every standard, is a table row with exactly these
fields:

| Field | Requirement |
|---|---|
| Id | `SC-` style prefix unique to the standard, sequential |
| Statement | one normative sentence, testable |
| Why | the failure mode that motivated it, named |
| Enforcement | the gate, script, or ADR that enforces it |

An invariant without a **why** is a preference. An invariant without
**enforcement** is draft material: it becomes law when a gate lands or an
ADR adjudicates it, never before.

## §4 Standard anatomy

Every standard document contains, in order:

1. Title and status stamp (§6).
2. **Scope and boundary**: what it governs; what it explicitly does not.
3. **Dependencies**: `depends` ids with version ranges (§5); the
   tighten-only rule restated with any inherited invariants summarized.
4. **Invariants**: the §3 table.
5. **Gates**: the mechanical checks, each naming its script and what it
   verifies; local-first (running locally implies CI results).
6. **Grounding**: the estate facts the standard was authored from (repos,
   files, ADRs). A standard that cannot cite its grounding stays DRAFT.
7. **Governance**: change procedure (ADR + version bump), loop cadence.

## §5 Dependencies

1. Ids are `SC-`-style uppercase tokens registered in `standards.yml`.
2. `depends` entries are `ID@^major.min` ranges; resolved by
   `standards-audit.py`; unresolvable deps fail the gate.
3. L1 canon dependencies are declared through the `canons:` block
   (repo + expected major).
4. Breaking an invariant is a major version bump of the standard;
   dependents see it through resolution failure, the same way
   `cargo-semver-checks` fails a crate.
5. The registry (`standards.yml`) is the dependency contract of record;
   consumers depend on ids, never on file paths.

## §6 Lifecycle

`DRAFT` → `REVIEW` → `CURRENT` → `FROZEN (date)` → `SUPERSEDED by <id>`.
Declined domains get an ADR (the tombstone) instead of a DRAFT file.

1. `DRAFT`: grounding incomplete or gates pending; audit enforces the
   DRAFT stamp and the grounding section naming its sources.
2. `CURRENT`: grounding complete, gates live, audit green.
3. `FROZEN`: append-only; corrections via superseding version.
4. `SUPERSEDED`: keeps original text visible; names its successor id.

## §7 Gates

| Script | Checks |
|---|---|
| `standards-audit.py --root .` | registry schema; dependency resolution; anatomy per standard (§4 sections present); lifecycle stamps; semver; character rule; self-conformance of this document |

## §8 Projections

Standards are canon. Skills, MCP servers, and doc sites that repackage
them are projections (SPEC-CORE SC-11, OMNI-CORE 11p): they declare their
source rev, are rebuilt by CI, and a stale projection fails the canon's
gate.

## §9 Declining a standard

A domain without a gate, without repeated adjudicated disputes, and
without survey evidence is declined: an ADR names the domain and the
reason, and no DRAFT file is created. The decline is reversible by a new
ADR when the evidence arrives.

## §10 Grounding

This document is authored from the estate's own practice: the four-field
invariant pattern in production (engineering-standards OMNI-CORE invariant
table; spec-standards SPEC-CORE §2), the registry-plus-audit pattern
(estate.yml + estate-audit.py; spec-standards standards.yml + spec-audit.py),
and the projection machinery (SPEC-CORE SC-11, OMNI-CORE 11p). Both L1
canons are the first conformers; their conformance is declared by ADR in
each canon repo.
