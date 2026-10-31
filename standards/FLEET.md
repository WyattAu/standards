# FLEET: fleet infrastructure standard

> **Status: CURRENT (v0.1.0, 2026-10-31)**

**Layer:** L2 · **Depends:** STANDARDS-CORE@^0.2, ENGINEERING@^1 · **Date:** 2026-10-31

## Scope

The estate's machine fleet: configuration-as-code (chezmoi source-of-truth
management), host provisioning (Ansible layering), credential handling,
and the drift/smoke gates that keep rendered state honest. Application
secrets' *values* are out of scope (they live in a secret store; the
pattern for referencing them is in scope).

## Dependencies

Inherits ENGINEERING (scripts canonical: the fleet's `sys-*` scripts are
the contract, Ansible and chezmoi mirror them) and SPEC (DOC-STYLE
register applies to fleet documentation).

## Invariants

| Id | Statement | Why | Enforcement |
|---|---|---|---|
| FL-1 | The chezmoi source tree is the only edited state; rendered files are never edited directly | rendered edits are overwritten on the next apply and hide from the diff | review + fleet rules (always-in-context) |
| FL-2 | The validation ladder is mandatory before full application: dry-run, then targeted checks, then apply | a full apply is the fleet's deploy; ladders catch breakage at the cheapest step | fleet rules + `fleet-admin` skill procedure |
| FL-3 | The dev tree can flap (invisible windows on the backing filesystem): after any write, verify existence; when the tree is visible, commit and push immediately | files written during an invisible window vanish without error | verify-after-write procedure (fleet rules) |
| FL-4 | Secrets are never in the managed tree: keys live in a keys directory with owner-only permissions, read at process spawn; the pattern is the estate-keys skill | a dotfiles repo is one accidental push from public; 0600 + spawn-time reads keep values out of history | estate-keys skill + gitleaks |
| FL-5 | Drift is detected mechanically and routinely: rendered-vs-source, packages-vs-host_vars, running-vs-declared services, and the MCP surface | configuration that is not compared is not configuration, it is folklore | `fleet-drift` skill (the gate) |
| FL-6 | Smoke health is gated hourly: services, kernel, locale, SSH, theme, Docker | silent service death is the fleet's equivalent of a red main | `sys-check` schedule |
| FL-7 | Host state layers strictly: common → os → distro → host; a package or setting lives in the most general layer that can hold it | layer discipline is what makes host addition a data change, not a project | ansible host_vars structure + review |
| FL-8 | Secret scanning runs from native binaries via shell, on every dotfiles change | keys leak through history; the scanner is cheap and the leak is expensive | gitleaks/trivy pre-commit + CI |

## Gates

`fleet-drift` skill (FL-5, the primary drift detector), `sys-check`
schedule (FL-6), gitleaks/trivy (FL-4, FL-8), `save` workflow (FL-3's
commit-and-push leg), ansible `--check` inside the validation ladder
(FL-2).

## Grounding

The fleet dotfiles README (hosts, layer table, `sys-*` command reference),
fleet rules (always-in-context: source-only editing, validation ladder,
flap hazard, keys pattern, hourly gate), `fleet-drift`, `fleet-admin`,
`estate-keys` skills, and the Ansible opencode role (installed-skill
provisioning). Estate-internal; paths and hostnames deliberately absent
from this public document (STANDARDS-CORE §8 scrub discipline).
