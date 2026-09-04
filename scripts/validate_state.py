#!/usr/bin/env python3
"""Validate WeChat ArticleState v0.6 structure, depth gates, evidence lineage and blind-review independence."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
SCHEMA_PATH = SCHEMA_DIR / "article-state.schema.json"

STAGE_ORDER = {
    "signal": 0,
    "topic": 1,
    "research": 2,
    "author": 3,
    "architecture": 4,
    "writing": 5,
    "blind_review": 6,
    "visual": 7,
    "qa": 8,
    "publishing": 9,
    "published": 10,
    "reviewed": 11,
}

GENERIC_DECISION_PHRASES = ("多关注", "多学习", "提高认知", "持续关注", "保持关注")


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError("ArticleState root must be an object")
    return data


def validate_schema(state: dict[str, Any]) -> list[str]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    resolver = RefResolver(base_uri=SCHEMA_DIR.as_uri() + "/", referrer=schema)
    validator = Draft202012Validator(schema, resolver=resolver)
    errors = []
    for err in sorted(validator.iter_errors(state), key=lambda e: list(e.absolute_path)):
        path = ".".join(str(p) for p in err.absolute_path) or "<root>"
        errors.append(f"schema:{path}: {err.message}")
    return errors


def unique_ids(items: list[dict[str, Any]], key: str, label: str) -> tuple[set[str], list[str]]:
    seen: set[str] = set()
    errors: list[str] = []
    for item in items:
        value = item.get(key)
        if not value:
            continue
        if value in seen:
            errors.append(f"duplicate {label}: {value}")
        seen.add(value)
    return seen, errors


def validate_cross_refs(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    research = state.get("research", {})
    claims = research.get("claims", []) or []
    calculations = research.get("calculations", []) or []
    sources = research.get("source_registry", []) or []
    uncertainty = research.get("uncertainty_nodes", []) or []
    writing = state.get("writing", {})
    sections = writing.get("sections", []) or []
    visual = state.get("visual", {})
    assets = visual.get("inline_images", []) or []

    source_ids, e = unique_ids(sources, "source_id", "source_id")
    errors.extend(e)
    claim_ids, e = unique_ids(claims, "claim_id", "claim_id")
    errors.extend(e)
    calc_ids, e = unique_ids(calculations, "calc_id", "calc_id")
    errors.extend(e)
    uncertainty_ids, e = unique_ids(uncertainty, "node_id", "uncertainty node_id")
    errors.extend(e)
    _, e = unique_ids(sections, "section_id", "writing section_id")
    errors.extend(e)
    _, e = unique_ids(assets, "asset_id", "visual asset_id")
    errors.extend(e)

    for claim in claims:
        for sid in claim.get("source_ids", []) or []:
            if sid not in source_ids:
                errors.append(f"claim {claim.get('claim_id')} references missing source {sid}")

    for section in sections:
        wid = section.get("section_id", "?")
        for cid in section.get("claim_ids", []) or []:
            if cid not in claim_ids:
                errors.append(f"writing section {wid} references missing claim {cid}")
        for kid in section.get("calc_ids", []) or []:
            if kid not in calc_ids:
                errors.append(f"writing section {wid} references missing calculation {kid}")

    for usage in state.get("author", {}).get("uncertainty_usage", []) or []:
        uid = usage.get("node_id")
        if uid and uid not in uncertainty_ids:
            errors.append(f"author uncertainty_usage references missing uncertainty node {uid}")

    return errors


def validate_workflow(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    workflow = state.get("workflow", {})
    stage = workflow.get("stage")
    gate = workflow.get("gate")
    qa = state.get("qa", {})
    visual = state.get("visual", {})
    publishing = state.get("publishing", {})

    if gate == "blocked" and not workflow.get("blocked_by"):
        errors.append("workflow.gate=blocked requires blocked_by")
    if gate in {"blocked", "rework"} and not workflow.get("return_to"):
        errors.append(f"workflow.gate={gate} requires return_to")

    if qa.get("status") == "A":
        if not visual.get("assets_ready"):
            errors.append("qa.status=A requires visual.assets_ready=true")
        if qa.get("blocking_issues"):
            errors.append("qa.status=A requires no blocking_issues")
        if gate != "ready":
            errors.append("qa.status=A requires workflow.gate=ready")
        if state.get("writing", {}).get("anti_template_pass", {}).get("status") != "pass":
            errors.append("qa.status=A requires writing.anti_template_pass.status=pass")

    if stage in {"publishing", "published", "reviewed"}:
        if qa.get("status") != "A":
            errors.append(f"workflow.stage={stage} requires qa.status=A")
        if publishing.get("plan_status") not in {"planned", "ready"}:
            errors.append(f"workflow.stage={stage} requires publishing.plan_status planned/ready")

    if stage in {"published", "reviewed"}:
        publication = state.get("publication", {})
        if not publication.get("published_at"):
            errors.append(f"workflow.stage={stage} requires publication.published_at")

    return errors


def validate_tension(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mode = state.get("production", {}).get("mode")
    stage = state.get("workflow", {}).get("stage")
    if mode == "flash" or stage not in STAGE_ORDER or STAGE_ORDER[stage] < STAGE_ORDER["research"]:
        return errors

    tension = state.get("topic", {}).get("tension_test", {}) or {}
    if tension.get("status") != "pass":
        errors.append("standard/deep research requires topic.tension_test.status=pass")
    if not (tension.get("contradiction", "").strip() or tension.get("unresolved_question", "").strip()):
        errors.append("tension test requires contradiction or unresolved_question")
    decision = tension.get("decision_change", "").strip()
    if not decision:
        errors.append("tension test requires concrete decision_change")
    if any(p in decision for p in GENERIC_DECISION_PHRASES):
        errors.append("tension decision_change is too generic")
    if not (tension.get("exclusive_material_path", "").strip() or tension.get("strong_judgment_candidate", "").strip()):
        errors.append("standard/deep tension requires exclusive material path or strong judgment candidate")
    return errors


def validate_originality(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mode = state.get("production", {}).get("mode")
    stage = state.get("workflow", {}).get("stage")
    if stage not in STAGE_ORDER or STAGE_ORDER[stage] < STAGE_ORDER["writing"]:
        return errors

    assets = state.get("research", {}).get("originality_gate", {}).get("assets", []) or []
    a_count = sum(1 for a in assets if a.get("level") == "A")
    b_count = sum(1 for a in assets if a.get("level") == "B")

    if mode == "standard" and not (a_count >= 1 or b_count >= 2):
        errors.append("standard mode requires >=1 A originality asset or >=2 B assets before writing")
    if mode == "deep" and not (a_count >= 1 and b_count >= 1):
        errors.append("deep mode requires >=1 A and >=1 B originality assets before writing")
    return errors


def validate_author_depth(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mode = state.get("production", {}).get("mode")
    stage = state.get("workflow", {}).get("stage")
    if mode == "flash" or stage not in STAGE_ORDER or STAGE_ORDER[stage] < STAGE_ORDER["architecture"]:
        return errors

    author = state.get("author", {})
    candidates = author.get("pov_candidates", []) or []
    if len(candidates) != 3:
        errors.append("standard/deep AuthorLens requires exactly 3 POV candidates")

    pov_ids = {c.get("pov_id") for c in candidates if c.get("pov_id")}
    selected = author.get("selected_pov_id")
    if not selected or selected not in pov_ids:
        errors.append("author.selected_pov_id must reference one POV candidate")
    rejected = set(author.get("rejected_pov_ids", []) or [])
    if len(rejected) < 2:
        errors.append("AuthorLens must explicitly reject at least two POV candidates")

    for c in candidates:
        pid = c.get("pov_id", "?")
        if not str(c.get("banality_self_critique", "")).strip():
            errors.append(f"POV {pid} missing banality_self_critique")
        if not str(c.get("decision_change", "")).strip():
            errors.append(f"POV {pid} missing decision_change")

    entry = author.get("entry_point", {}) or {}
    decision = str(entry.get("decision_change", "")).strip()
    if not decision:
        errors.append("author.entry_point requires decision_change")
    if any(p in decision for p in GENERIC_DECISION_PHRASES):
        errors.append("author.entry_point decision_change is too generic")

    stats = author.get("selection_stats", {}) or {}
    retained = int(stats.get("retained_units", 0) or 0)
    discarded = int(stats.get("discarded_units", 0) or 0)
    if retained <= 0:
        errors.append("author.selection_stats.retained_units must be > 0")
    if discarded < retained:
        errors.append("standard/deep material graveyard requires discarded_units >= retained_units")
    if not author.get("material_graveyard"):
        errors.append("author.material_graveyard must be non-empty")

    humanity = author.get("humanity_test", {}) or {}
    if humanity.get("generic_ai_risk") == "high":
        errors.append("author humanity test: generic_ai_risk is high")
    if humanity.get("template_risk") == "high":
        errors.append("author humanity test: template_risk is high")
    if humanity.get("author_specificity") == "low":
        errors.append("author humanity test: author_specificity is low")

    return errors


def validate_writing_generation(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mode = state.get("production", {}).get("mode")
    stage = state.get("workflow", {}).get("stage")
    if mode == "flash" or stage not in STAGE_ORDER or STAGE_ORDER[stage] < STAGE_ORDER["blind_review"]:
        return errors

    trace = state.get("writing", {}).get("generation_trace", {}) or {}
    if trace.get("strategy") not in {"isolated_segments", "single_context_fallback"}:
        errors.append("standard/deep writing requires segment generation strategy")
    if int(trace.get("segment_count", 0) or 0) < 2:
        errors.append("standard/deep writing requires at least 2 generated segments")
    if trace.get("reorder_pass") is not True:
        errors.append("standard/deep writing requires reorder/delete pass")

    packet = state.get("writing", {}).get("blind_review_packet", {}) or {}
    if packet.get("ready") is not True or packet.get("body_only") is not True:
        errors.append("blind review packet must be ready and body_only")
    return errors


def validate_blind_review(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mode = state.get("production", {}).get("mode")
    stage = state.get("workflow", {}).get("stage")
    if mode == "flash" or stage not in STAGE_ORDER or STAGE_ORDER[stage] < STAGE_ORDER["visual"]:
        return errors

    review = state.get("blind_review", {}) or {}
    if review.get("status") != "pass":
        errors.append("standard/deep visual stage requires blind_review.status=pass")
    if review.get("evaluator_independence") not in {"fresh_session", "different_model"}:
        errors.append("blind review must use fresh_session or different_model")
    if review.get("ai_likeness") == "high":
        errors.append("blind review ai_likeness=high cannot pass")
    high_findings = [f for f in review.get("findings", []) or [] if f.get("severity") == "high"]
    if high_findings:
        errors.append("blind review has unresolved high-severity findings")
    return errors


def validate_calculations(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for calc in state.get("research", {}).get("calculations", []) or []:
        kid = calc.get("calc_id", "?")
        for field in ("assumptions", "formula", "inputs", "result", "verification"):
            if field not in calc or calc.get(field) in (None, ""):
                errors.append(f"calculation {kid} missing {field}")
    return errors


def validate(path: Path) -> list[str]:
    state = load_yaml(path)
    errors: list[str] = []
    errors.extend(validate_schema(state))
    errors.extend(validate_cross_refs(state))
    errors.extend(validate_workflow(state))
    errors.extend(validate_tension(state))
    errors.extend(validate_originality(state))
    errors.extend(validate_author_depth(state))
    errors.extend(validate_writing_generation(state))
    errors.extend(validate_blind_review(state))
    errors.extend(validate_calculations(state))
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_state.py <article-state.yaml>")
        return 2
    path = Path(sys.argv[1]).resolve()
    errors = validate(path)
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for err in errors:
            print(f"- {err}")
        return 1
    print("PASS: ArticleState is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
