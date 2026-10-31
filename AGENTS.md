# AGENTS.md: standards contract

This repo is L0: the meta-standard plus the domain standards. The universal
canons (engineering-standards, spec-standards) are L1 and live elsewhere;
this repo governs what a standard is, not how code is built.

## Non-negotiables

1. STANDARDS-CORE.md is normative: changes require an ADR here and a
   header version bump plus CHANGELOG entry.
2. Every registered standard passes `standards-audit.py` (mechanical
   self-conformance); a red audit is a release blocker with no waivers.
3. Domain standards tighten; they never loosen L1 invariants. Overrides
   need an ADR in the governing canon.
4. The em-dash character appears in no Markdown file (DOC-STYLE, inherited
   from spec-standards; the gate greps it).
5. Declined standards are recorded: an ADR naming the domain and the
   reason counts as the standard's tombstone.

## Where the truth lives

| Concern | File |
|---|---|
| Meta-standard (what a standard is) | `STANDARDS-CORE.md` |
| Domain standards | `standards/` |
| Dependency contract | `standards.yml` |
| Mechanical conformance | `standards-audit.py` |
| Decisions | `docs/adr/` |
