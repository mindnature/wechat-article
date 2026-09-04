#!/usr/bin/env python3
"""Detect obvious paragraph fragmentation in WeChat article prose."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

HEADING_RE = re.compile(r"^(?:#{1,6}\s*)?(?:0?\d{1,2}|[一二三四五六七八九十]+)[｜|、.．]\s*")
LIST_RE = re.compile(r"^(?:[-*•]\s+|\d+[.)、]\s+)")
SENTENCE_END_RE = re.compile(r"[。！？!?；;]")
MARKUP_RE = re.compile(r"[`*_>#\[\](){}]")

MICRO_CHARS = 20
MAX_MICRO_PARAGRAPHS = 2
MAX_CONSECUTIVE_MICRO = 1
MAX_CONSECUTIVE_SINGLE_SENTENCE = 2
MAX_SINGLE_SENTENCE_RATIO = 0.40


def load_state(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("ArticleState root must be an object")
    return data


def clean_text(text: str) -> str:
    text = MARKUP_RE.sub("", text)
    return re.sub(r"\s+", "", text).strip()


def split_paragraphs(text: str) -> list[str]:
    if not text:
        return []
    blocks = re.split(r"\n\s*\n+", text.strip())
    out: list[str] = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) <= 1:
            if lines:
                out.append(lines[0])
            continue
        # Preserve explicit line breaks as paragraph boundaries. Headings and list items
        # are later excluded from prose-rhythm statistics.
        out.extend(lines)
    return out


def is_exempt(paragraph: str) -> bool:
    p = paragraph.strip()
    return bool(HEADING_RE.match(p) or LIST_RE.match(p))


def sentence_count(paragraph: str) -> int:
    count = len(SENTENCE_END_RE.findall(paragraph))
    if count == 0 and clean_text(paragraph):
        return 1
    return count


def max_run(flags: list[bool]) -> int:
    best = cur = 0
    for flag in flags:
        if flag:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


def analyze(state: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    paragraphs: list[str] = []
    for section in state.get("writing", {}).get("sections", []) or []:
        paragraphs.extend(split_paragraphs(str(section.get("text", ""))))

    prose = [p for p in paragraphs if not is_exempt(p) and clean_text(p)]
    lengths = [len(clean_text(p)) for p in prose]
    single_flags = [sentence_count(p) <= 1 for p in prose]
    micro_flags = [length <= MICRO_CHARS for length in lengths]

    total = len(prose)
    single_count = sum(single_flags)
    micro_count = sum(micro_flags)
    single_ratio = (single_count / total) if total else 0.0
    max_single_run = max_run(single_flags)
    max_micro_run = max_run(micro_flags)

    metrics = {
        "prose_paragraphs": total,
        "single_sentence_paragraphs": single_count,
        "single_sentence_ratio": round(single_ratio, 3),
        "micro_paragraphs": micro_count,
        "max_consecutive_single_sentence": max_single_run,
        "max_consecutive_micro": max_micro_run,
        "micro_char_threshold": MICRO_CHARS,
    }

    errors: list[str] = []
    if total >= 4 and single_ratio > MAX_SINGLE_SENTENCE_RATIO:
        errors.append(
            f"single-sentence paragraph ratio {single_ratio:.2f} exceeds {MAX_SINGLE_SENTENCE_RATIO:.2f}"
        )
    if max_single_run > MAX_CONSECUTIVE_SINGLE_SENTENCE:
        errors.append(
            f"{max_single_run} consecutive single-sentence paragraphs; max allowed is {MAX_CONSECUTIVE_SINGLE_SENTENCE}"
        )
    if micro_count > MAX_MICRO_PARAGRAPHS:
        errors.append(
            f"{micro_count} micro paragraphs (<= {MICRO_CHARS} chars); max allowed is {MAX_MICRO_PARAGRAPHS}"
        )
    if max_micro_run > MAX_CONSECUTIVE_MICRO:
        errors.append(
            f"{max_micro_run} consecutive micro paragraphs; short emphasis paragraphs must not stack"
        )

    return metrics, errors


def validate(path: Path) -> tuple[dict[str, Any], list[str]]:
    state = load_state(path)
    mode = state.get("production", {}).get("mode")
    stage = state.get("workflow", {}).get("stage")
    if mode == "flash" or stage in {"signal", "topic", "research", "author", "architecture"}:
        return {}, []
    return analyze(state)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_readability.py <article-state.yaml>")
        return 2
    metrics, errors = validate(Path(sys.argv[1]).resolve())
    if metrics:
        print("Paragraph rhythm metrics:")
        for key, value in metrics.items():
            print(f"- {key}: {value}")
    if errors:
        print(f"FAIL: {len(errors)} readability error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: paragraph rhythm is acceptable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
