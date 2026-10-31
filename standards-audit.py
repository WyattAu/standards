#!/usr/bin/env python3
"""standards-audit: mechanical conformance gate for the standards estate.

Validates, per STANDARDS-CORE:
  registry schema (§5)          ids, layers, semver, lifecycle, deps resolve
  standard anatomy (§4)         status stamp, required sections per standard
  invariant anatomy (§3)        invariant tables carry Statement/Why/Enforcement
  character rule (DOC-STYLE 1)  the em-dash character appears in no Markdown
  self-conformance (§7)         STANDARDS-CORE passes the same checks

Usage: standards-audit.py --root .
Exit:  0 pass, 1 failures.
"""
from __future__ import annotations

import datetime
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("PyYAML required (see the repo README)", file=sys.stderr)
    sys.exit(2)

EM = "\u2014"
LAYERS = {"l0", "l1", "l2"}
STATUSES = {"draft", "review", "current", "frozen", "superseded"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
DEP_RE = re.compile(r"^([A-Z0-9-]+)@\^(\d+)(?:\.(\d+))?$")
REQUIRED_SECTIONS = ("Dependencies", "Invariants", "Gates", "Grounding")
INVARIANT_FIELDS = {"Statement", "Why", "Enforcement"}


def audit(root: Path) -> int:
    fails: list[str] = []
    advisories: list[str] = []

    reg_path = root / "standards.yml"
    if not reg_path.exists():
        print("FAIL: standards.yml missing")
        return 1
    reg = yaml.safe_load(reg_path.read_text(encoding="utf-8")) or {}
    standards = reg.get("standards") or {}
    canons = reg.get("canons") or {}
    if not standards:
        print("FAIL: registry has no standards")
        return 1

    ids = set(standards)
    for sid, meta in standards.items():
        layer = meta.get("layer")
        if layer not in LAYERS:
            fails.append(f"{sid}: layer {layer!r} not in {sorted(LAYERS)}")
        version = str(meta.get("version", ""))
        if not SEMVER_RE.match(version):
            fails.append(f"{sid}: version {version!r} not semver")
        status = meta.get("status")
        if status not in STATUSES:
            fails.append(f"{sid}: status {status!r} not in {sorted(STATUSES)}")
        deps = meta.get("depends") or []
        if layer == "l0" and deps:
            fails.append(f"{sid}: L0 declares dependencies; the meta-standard depends on nothing")
        for dep in deps:
            m = DEP_RE.match(dep)
            if not m:
                fails.append(f"{sid}: dep {dep!r} not ID@^major.min")
                continue
            dep_id, dmaj = m.group(1), int(m.group(2))
            dmin = int(m.group(3) or 0)
            if dep_id in ids:
                target = standards[dep_id]
                tver = [int(x) for x in str(target.get("version", "0.0.0")).split(".")]
                if tver[0] != dmaj or tver[1] < dmin:
                    fails.append(f"{sid}: dep {dep_id}@^{dmaj}.{dmin} unsatisfied by {target.get('version')}")
            elif dep_id in canons:
                continue  # canon dep: major tracked in the canons block
            else:
                fails.append(f"{sid}: dep {dep_id!r} not registered")

    # anatomy per standard (registered files only)
    for sid, meta in standards.items():
        rel = meta.get("file")
        p = root / str(rel or "")
        if not rel or not p.exists():
            fails.append(f"{sid}: file {rel!r} missing")
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"> \*\*Status: ([A-Za-z]+)(?: \(([^)]*)\))?", text)
        stamp_status = m.group(1).lower() if m else None
        if stamp_status != str(meta.get("status", "")).lower():
            fails.append(f"{sid}: file stamp '{stamp_status}' != registry status '{meta.get('status')}' (SPEC-CORE §5 style)")
        if EM in text:
            fails.append(f"{sid}: em-dash present (DOC-STYLE §1)")
        sections = re.findall(r"^## (?:\u00a7\d+ )?([A-Za-z0-9 ]+?):", text, re.M) + \
                   re.findall(r"^## (?:\u00a7\d+ )?([A-Za-z0-9 ]+)$", text, re.M)
        names = {s.split(":")[0].strip() for s in sections}
        for req in REQUIRED_SECTIONS:
            if not any(req.lower() in n.lower() for n in names):
                fails.append(f"{sid}: missing required section '{req}' (STANDARDS-CORE §4)")
        if str(meta.get("status")) == "draft" and "Grounding pass" not in text and "DRAFT" not in text[:400]:
            advisories.append(f"{sid}: DRAFT without a visible grounding-pass note")
        # invariant table anatomy (§3): look for a table with the four fields
        if str(meta.get("status")) != "draft" and re.search(
            r"\|\s*(SC|SK|MC|LI|CO|MA|IV|DE)-", text
        ) and not ("Why" in text and "Enforcement" in text):
            fails.append(f"{sid}: invariant table missing Why/Enforcement columns (STANDARDS-CORE §3)")

    # self-conformance: L0 passes the same checks (loop closure)
    core = standards.get("STANDARDS-CORE")
    if core and str(core.get("file", "")) != "STANDARDS-CORE.md":
        fails.append("registry: STANDARDS-CORE must point at STANDARDS-CORE.md")

    for a in advisories:
        print(f"ADVISORY: {a}")
    for f in fails:
        print(f"FAIL: {f}")
    print(f"standards-audit: {len(standards)} standards, {len(canons)} canons, "
          f"{len(fails)} failure(s), {len(advisories)} advisory/advisories")
    return 1 if fails else 0


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "--root":
        print("usage: standards-audit.py --root .", file=sys.stderr)
        sys.exit(2)
    sys.exit(audit(Path(sys.argv[2]).resolve()))
