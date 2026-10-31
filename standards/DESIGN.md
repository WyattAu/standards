# DESIGN: color, a11y, typography standard

> **Status: DRAFT (v0.1.0, 2026-10-31)**

**Layer:** L2 · **Depends:** STANDARDS-CORE@^0.1 · **Date:** 2026-10-31

## Scope

Visual and interaction standards for estate UI: color tokens, contrast
floors, accessibility requirements, and typography. This document is
DRAFT: its grounding pass (below) has not run, so its invariants are
candidates, not law (STANDARDS-CORE §6).

## Dependencies

Inherits STANDARDS-CORE (anatomy, lifecycle). Intends to inherit
ENGINEERING once the grounding pass names the gates.

## Grounding pass (required before CURRENT)

Authorship must extract the real rules from, and cite:

1. `color-kit`, `theme-kit`, `theme-egui`: the existing token system, its
   naming scheme, dark/light handling, and what components are allowed to
   hardcode.
2. `a11y-kit`: the accessibility surface already built (focus handling,
   labels, semantics) and which WCAG levels its helpers can guarantee.
3. `font-conformance` and the `font-*` family: the differential harness
   that already exists for typography.
4. `pediment`, `plychart`: chart color and contrast behavior on real
   surfaces.

## Invariants

Candidates only: this document is DRAFT; rows below are not law
(STANDARDS-CORE §3 applies on promotion).

| Id | Candidate statement | Grounding needed |
|---|---|---|
| DE-1 | Components consume color only through theme tokens; hardcoded color values fail review | color-kit/token audit |
| DE-2 | Text contrast meets the WCAG AA floor for its size class, checked by a gate, not by eye | contrast measurement against theme-kit palettes |
| DE-3 | Interactive elements expose a11y-kit semantics (labels, focus, roles); a component without them fails review | a11y-kit surface audit |
| DE-4 | Typography renders through the font stack validated by `font-conformance`; new faces pass the differential harness first | font-conformance run book |
| DE-5 | Every estate web surface ships llms.txt and passes the docs gate at tier d | spec-standards adoption |

## Gates

None yet: the grounding pass names the gates (contrast check, a11y
lint, font-conformance run) that promotion to CURRENT requires.

## Grounding

Required before promotion; the four sources in the grounding pass above
are the citation set. Until then this document is DRAFT by construction,
not by omission.

## Why DRAFT

Three of five candidates name gates that do not exist yet (STANDARDS-CORE
§3: no gate or adjudicated ADR means draft material). The grounding pass
converts this document into law or files the decline.
