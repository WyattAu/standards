TIER ?= l0

.PHONY: help audit lint ci
help:
	@echo "audit - standards-audit.py over this repo (registry + self-conformance)"
	@echo "lint  - markdownlint (optional; SKIP when absent)"
	@echo "ci    - audit + lint"

audit:
	@python3 standards-audit.py --root .
	@python3 scripts/voice-lint.py --strict .

lint:
	@if command -v markdownlint >/dev/null 2>&1; then markdownlint "**/*.md" --config .markdownlint.json; \
	else echo "SKIP: markdownlint not installed"; fi

ci: audit lint
