# MCP: Model Context Protocol server standard

> **Status: CURRENT (v0.1.0, 2026-10-31)**

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
| MC-6 | A fleet-audit pass (`mcp-doctor`) is green before release: config parse, backend resolution, real handshakes | a server that lists tools but fails handshakes is a lie with a schema | mcp-doctor |

## Gates

`mcp-doctor` (config parse, backend resolution, MCP handshakes); per-server
smoke script piping `initialize`, `tools/list`, `tools/call` over stdio
(reference implementation: standards-dist `mcp/standards_mcp.py`, smoke
tested 2026-10-31).

## Grounding

`mcp-doctor` (fleet auditor), `standards-dist/mcp/standards_mcp.py`
(reference: read-only wrapper over the estate gates), `detonate-mcp`.
