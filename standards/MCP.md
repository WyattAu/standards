# MCP: Model Context Protocol server standard

> **Status: CURRENT (v0.2.0, 2026-10-31)**

**Layer:** L2 · **Depends:** STANDARDS-CORE@^0.1, ENGINEERING@^1 · **Date:** 2026-10-31

## Scope

MCP servers built in the estate: protocol shape, tool design, security
posture, and validation. Does not govern MCP client configuration beyond
the config snippet a server must ship.

## Dependencies

Inherits ENGINEERING (scripts canonical, least privilege, release
attestation) and OMNI-CORE 11i (agent-facing interfaces).

## Invariants

| Id | Statement | Why | Enforcement |
|---|---|---|---|
| MC-1 | A server wraps canonical estate scripts or services; it never reimplements estate logic | two implementations of one rule is the drift SC-9 exists to kill | review + mcp-doctor probe |
| MC-2 | Servers are read-only by default; a mutation tool requires an ADR in the server's repo and per-call confirmation design | a mutating tool in every agent session is a standing footgun | review |
| MC-3 | Every tool declares a complete `inputSchema` (types, enum, required) | schema-less tools push validation onto the model | mcp-doctor |
| MC-4 | The server runs with no secrets and no write scope; config snippets shipped in the repo state the exact command | least privilege; fleets are auditable | mcp-doctor (fleet audit) |
| MC-5 | Stdio transport first; zero-dependency implementations preferred where the surface is small | deployment surface is the cost model; stdio needs no daemon | review |
| MC-6 | A fleet-audit pass (`mcp-fleet-doctor`) is green before release: config parse, backend resolution, real handshakes | a server that lists tools but fails handshakes is a lie with a schema | mcp-fleet-doctor |
| MC-7 | Dependency trees are pinned (lockfiles committed; no floating ranges); install scripts are declared and justified | 78% of surveyed servers ship unpinned deps; unreviewed upstream releases are the npm/PyPI attack pattern | lockfile check in CI (Canopii 2026: 8,735 of 11,141 servers unpinned) |
| MC-8 | Tool paths contain no `eval`, shell-execution, or unsafe-deserialization sinks; if the server's purpose requires execution, it is sandboxed and the sandbox is declared in the README | researchers confirmed 232 servers with reachable dangerous sinks; 687 unauthenticated shell-exec tools found internet-facing | static scan (dangerous-sink patterns) + review |
| MC-9 | Auth declared in the manifest is tested: the tool list must not be served to anonymous callers | 1 in 3 manifest-auth servers served full tool lists anonymously (741 tools on the top 20) | handshake probe with and without credentials (mcp-fleet-doctor --deep) |
| MC-10 | Remote endpoints are pinned trust-on-first-use: host and tool-definition digest recorded at install; any later change is a breaking event requiring re-consent | 4.2% of multi-version servers silently redirected endpoints (rug-pull shape); silent drift triples high-severity odds | PROVENANCE-style pin + drift diff (build.sh --diff pattern) |
| MC-11 | Tool definitions are versioned; a tool-changing release emits a machine-readable diff | registries do not version tool definitions, so behavioral change is undetectable by construction (the drift research's central structural finding) | diff emission in the release procedure |
| MC-12 | Sandboxing posture is declared: unsandboxed servers say so, name their privilege level, and list every filesystem/network reach | 81% ship unsandboxed with full host access by default | README declaration + review |

## Gates

`mcp-doctor` (config parse, backend resolution, MCP handshakes); per-server
smoke script piping `initialize`, `tools/list`, `tools/call` over stdio
(reference implementation: standards-dist `mcp/standards_mcp.py`, smoke
tested 2026-10-31).

## Grounding

`mcp-fleet-doctor` (OpenCode fleet auditor; renamed from mcp-doctor,
ADR-0001 there, collision with an unrelated scanner),
`standards-dist/mcp/standards_mcp.py` (reference: read-only wrapper over
the estate gates), `detonate-mcp`. Research grounding for MC-7..MC-12:
"Exposed by Design" (arXiv 2608.00150: 91.8% unauthenticated, 687 unauthed
shell tools), "Same Name, Different Server" (arXiv 2609.14119: silent
drift, 4.2% endpoint redirection, pinning recommendations), Canopii
"State of MCP Security 2026" (11,524 servers scored, 184 rug pulls, 78%
unpinned deps), DSN 2026 registry study (67,057 servers, 833 vulnerable).
