# WyattAu Standards

The L0 meta-standard (STANDARDS-CORE) and the L2 domain standards for the
WyattAu estate, with a mechanical conformance gate. Layering mirrors the
estate's own crate layers (engineering-standards `docs/layers.md`):

| Layer | What | Where |
|---|---|---|
| L0 | what a standard is | this repo, `STANDARDS-CORE.md` |
| L1 | universal canons | [engineering-standards](https://github.com/WyattAu/engineering-standards), [spec-standards](https://github.com/WyattAu/spec-standards) |
| L2 | domain standards | this repo, `standards/` |
| L3 | repo truth tables, kit specs, REQUIREMENTS | each repo |

## Gate

```sh
python3 standards-audit.py --root .
```

Validates: registry schema, dependency resolution, required anatomy per
standard, lifecycle stamps, semver, the character rule. CI runs it on
every push; the audit is the standard's own enforcement (a standard that
fails its own gate is a release blocker).
