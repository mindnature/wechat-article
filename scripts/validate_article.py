#!/usr/bin/env python3
"""Run structural/state validation plus paragraph readability validation."""

from __future__ import annotations

import sys
from pathlib import Path

from validate_readability import validate as validate_readability
from validate_state import validate as validate_state


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_article.py <article-state.yaml>")
        return 2

    path = Path(sys.argv[1]).resolve()
    state_errors = validate_state(path)
    metrics, readability_errors = validate_readability(path)

    errors = [*(f"state: {e}" for e in state_errors), *(f"readability: {e}" for e in readability_errors)]

    if metrics:
        print("Paragraph rhythm metrics:")
        for key, value in metrics.items():
            print(f"- {key}: {value}")

    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: ArticleState and paragraph rhythm are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
