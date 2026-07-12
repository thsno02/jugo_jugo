#!/usr/bin/env python3
"""Validate the interaction archive's contracts, coverage, integrity, and privacy gate."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import jsonschema


BASE = Path(__file__).resolve().parents[1]
REPO_ROOT = BASE.parents[1]
SCHEMA_DIR = BASE / "schema"
SENSITIVE_PATTERNS = {
    "absolute_user_path": re.compile(r"/Users/[^\s\"']+"),
    "private_conversation_url": re.compile(
        r"https?://(?:chatgpt\.com/(?:c|share)/|claude\.ai/chat/)[^\s\"']+",
        re.IGNORECASE,
    ),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "secret_like": re.compile(
        r"(?i)(api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*[^\s,}]{8,}"
    ),
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_schema(data_path: Path, schema_name: str) -> dict:
    data = load_json(data_path)
    schema = load_json(SCHEMA_DIR / schema_name)
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))
    if errors:
        details = "\n".join(f"  {list(error.path)}: {error.message}" for error in errors)
        raise ValueError(f"Schema validation failed for {data_path}:\n{details}")
    return data


def visible_event_text(event: dict) -> str:
    assistant = event["assistant"]
    return "\n".join(
        [
            event["user"]["verbatim"],
            assistant["summary"] or "",
            *assistant["core_insights"],
            *assistant["actions"],
            *assistant["observed_effects"],
        ]
    )


def iter_artifact_refs(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "artifact_refs":
                yield from item
            else:
                yield from iter_artifact_refs(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_artifact_refs(item)


def main() -> int:
    manifest = validate_schema(BASE / "archive.json", "archive-manifest.schema.json")
    versions = validate_schema(
        BASE / manifest["versions_file"], "version-registry.schema.json"
    )
    sources = validate_schema(
        BASE / manifest["source_registry_file"], "source-registry.schema.json"
    )
    validate_schema(BASE / manifest["source_map_file"], "source-map.schema.json")
    session_audit = validate_schema(
        BASE / manifest["session_audit_file"], "session-audit.schema.json"
    )
    module_registry = validate_schema(
        BASE / manifest["module_registry_file"], "module-registry.schema.json"
    )
    query_timeline = validate_schema(
        BASE / manifest["query_timeline_file"], "query-timeline.schema.json"
    )

    version_ids = {version["version_id"] for version in versions["versions"]}
    source_ids = {source["source_id"] for source in sources["sources"]}
    event_schema = load_json(SCHEMA_DIR / "interaction-event.schema.json")
    event_validator = jsonschema.Draft202012Validator(
        event_schema, format_checker=jsonschema.FormatChecker()
    )

    all_events: list[dict] = []
    event_ids: set[str] = set()
    sequences: dict[str, list[int]] = defaultdict(list)
    privacy_findings: list[str] = []

    for shard in manifest["event_shards"]:
        shard_path = BASE / shard["file"]
        raw = shard_path.read_bytes()
        digest = "sha256:" + hashlib.sha256(raw).hexdigest()
        if shard.get("sha256") and shard["sha256"] != digest:
            raise ValueError(f"Shard hash mismatch: {shard_path}")

        events = [
            json.loads(line)
            for line in raw.decode("utf-8").splitlines()
            if line.strip()
        ]
        if len(events) != shard["record_count"]:
            raise ValueError(
                f"Shard count mismatch: {shard_path} has {len(events)}, "
                f"manifest says {shard['record_count']}"
            )

        for line_number, event in enumerate(events, 1):
            errors = list(event_validator.iter_errors(event))
            if errors:
                raise ValueError(
                    f"Event schema failed: {shard_path}:{line_number}: "
                    f"{errors[0].message}"
                )
            if event["event_id"] in event_ids:
                raise ValueError(f"Duplicate event id: {event['event_id']}")
            event_ids.add(event["event_id"])

            if not set(event["version_ids"]) <= version_ids:
                raise ValueError(f"Unknown version in {event['event_id']}")
            relation_versions = [
                item["version_id"] for item in event["version_relations"]
            ]
            if relation_versions != event["version_ids"]:
                raise ValueError(
                    f"Version relation mismatch in {event['event_id']}: "
                    f"{relation_versions} != {event['version_ids']}"
                )
            if event["provenance"]["source_id"] not in source_ids:
                raise ValueError(f"Unknown source in {event['event_id']}")
            if event["classification"] != {
                "source_record_class": "human_user_message",
                "authorship": "human",
                "human_input_eligible": True,
            } and not (
                event["classification"]["source_record_class"] == "human_user_message"
                and event["classification"]["authorship"] == "human"
                and event["classification"]["human_input_eligible"] is True
            ):
                raise ValueError(f"Non-human record entered event stream: {event['event_id']}")

            expected_user_hash = "sha256:" + hashlib.sha256(
                event["user"]["verbatim"].encode("utf-8")
            ).hexdigest()
            if event["user"]["sha256"] != expected_user_hash:
                raise ValueError(f"User text hash mismatch: {event['event_id']}")

            if event["privacy"]["publication"] != "withheld":
                for name, pattern in SENSITIVE_PATTERNS.items():
                    if pattern.search(visible_event_text(event)):
                        privacy_findings.append(f"{event['event_id']}: {name}")

            sequences[event["session"]["session_id"]].append(event["sequence"])
            all_events.append(event)

    for session_id, values in sequences.items():
        if values != sorted(values) or len(values) != len(set(values)):
            raise ValueError(f"Non-monotonic or duplicate sequence in {session_id}")

    if privacy_findings:
        raise ValueError("Privacy scan failed:\n  " + "\n  ".join(privacy_findings))

    coverage = manifest["coverage"]
    if coverage["human_user_inputs_archived"] != len(all_events):
        raise ValueError(
            "Coverage mismatch: manifest archived count is "
            f"{coverage['human_user_inputs_archived']}, actual is {len(all_events)}"
        )
    if (
        coverage["human_user_inputs_expected"] is not None
        and coverage["human_user_inputs_expected"] < len(all_events)
    ):
        raise ValueError("Expected human input denominator is smaller than the archive")
    for item in coverage["by_version"]:
        actual = sum(item["version_id"] in event["version_ids"] for event in all_events)
        if actual != item["archived"]:
            raise ValueError(
                f"Version coverage mismatch for {item['version_id']}: "
                f"manifest {item['archived']}, actual {actual}"
            )
        if item["complete"] and item["expected"] != item["archived"]:
            raise ValueError(f"Complete version has an incomplete denominator: {item['version_id']}")
    for item in coverage["by_session"]:
        actual = sum(
            event["provenance"]["source_id"] == item["source_id"]
            for event in all_events
        )
        if actual != item["archived"]:
            raise ValueError(
                f"Session coverage mismatch for {item['source_id']}: "
                f"manifest {item['archived']}, actual {actual}"
            )
    for item in coverage["by_provider"]:
        actual = sum(event["provider"] == item["provider"] for event in all_events)
        if actual != item["archived"]:
            raise ValueError(
                f"Provider coverage mismatch for {item['provider']}: "
                f"manifest {item['archived']}, actual {actual}"
            )
    for item in coverage["complete_windows"]:
        if item["complete"] and item["expected"] != item["archived"]:
            raise ValueError(f"Complete window is missing records: {item['window_id']}")

    audit_sessions = session_audit["sessions"]
    audit_aliases = [item["session_alias"] for item in audit_sessions]
    if len(audit_aliases) != len(set(audit_aliases)):
        raise ValueError("Duplicate session alias in session audit")
    for provider in ("codex", "claude_code"):
        actual = sum(item["provider"] == provider for item in audit_sessions)
        expected = session_audit["discovery"][provider]["top_level_count"]
        if actual != expected:
            raise ValueError(
                f"Session universe mismatch for {provider}: audit has {actual}, "
                f"discovery says {expected}"
            )
    for item in audit_sessions:
        actual = sum(
            event["provenance"]["source_id"] == item["session_alias"]
            for event in all_events
        )
        if actual != item["archived_event_count"]:
            raise ValueError(
                f"Session audit count mismatch for {item['session_alias']}: "
                f"audit {item['archived_event_count']}, actual {actual}"
            )
        if item["inclusion_status"] == "included":
            if item["session_alias"] not in source_ids or not item["event_shard"]:
                raise ValueError(f"Included session lacks source/shard: {item['session_alias']}")
            observed = item["semantic_input_count"] + item["command_action_count"]
            if observed != item["archived_event_count"]:
                raise ValueError(f"Included session denominator mismatch: {item['session_alias']}")
        elif item["archived_event_count"] != 0 or item["event_shard"] is not None:
            raise ValueError(f"Excluded session leaked into public events: {item['session_alias']}")
    if coverage["complete"] and sum(
        item["archived_event_count"] for item in audit_sessions
    ) != len(all_events):
        raise ValueError("Complete coverage is not reconciled to the session audit")

    for version in versions["versions"]:
        if not (BASE / version["content_ref"]).exists():
            raise ValueError(f"Missing version content: {version['content_ref']}")
        if not set(version["source_ids"]) <= source_ids:
            raise ValueError(f"Unknown source in version {version['version_id']}")
    for view in manifest["generated_views"]:
        if not (BASE / view["file"]).exists():
            raise ValueError(f"Missing generated view: {view['file']}")

    module_ids = {item["module_id"] for item in module_registry["modules"]}
    if len(module_ids) != len(module_registry["modules"]):
        raise ValueError("Duplicate module id in module registry")
    modules = []
    for item in module_registry["modules"]:
        module_path = BASE / item["data_file"]
        module = validate_schema(module_path, "module-recall.schema.json")
        modules.append(module)
        if module["module_id"] != item["module_id"] or module["status"] != item["status"]:
            raise ValueError(f"Module registry mismatch: {item['module_id']}")
        if not (BASE / item["content_file"]).exists():
            raise ValueError(f"Missing module content: {item['content_file']}")
        if not set(module["version_ids"]) <= version_ids:
            raise ValueError(f"Unknown version in module {module['module_id']}")

    control_ids = {
        control["control_id"] for module in modules for control in module["controls"]
    }
    control_count = sum(len(module["controls"]) for module in modules)
    if len(control_ids) != control_count:
        raise ValueError("Duplicate audit control id across modules")
    for module in modules:
        stage_ids = [stage["stage_id"] for stage in module["stages"]]
        if len(stage_ids) != len(set(stage_ids)):
            raise ValueError(f"Duplicate stage id in module {module['module_id']}")
        sequences = [stage["sequence"] for stage in module["stages"]]
        if sequences != sorted(sequences) or len(sequences) != len(set(sequences)):
            raise ValueError(f"Invalid stage order in module {module['module_id']}")
        for point in (
            module["design_context"]["observations"]
            + module["design_context"]["assumptions"]
        ):
            if not set(point["event_ids"]) <= event_ids:
                raise ValueError(
                    f"Unknown event in module design context: {module['module_id']}"
                )
        for stage in module["stages"]:
            if not set(stage["audit_control_ids"]) <= control_ids:
                raise ValueError(f"Unknown audit control in stage {stage['stage_id']}")
            for point in (
                stage["rationale"]["observations"]
                + stage["rationale"]["assumptions"]
            ):
                if not set(point["event_ids"]) <= event_ids:
                    raise ValueError(
                        f"Unknown event in stage rationale: {stage['stage_id']}"
                    )
            for evidence in stage["evidence"]:
                if evidence["event_id"] not in event_ids:
                    raise ValueError(f"Unknown event in module evidence: {evidence['event_id']}")
            for evolution in stage["evolution"]:
                if evolution["version_id"] not in module["version_ids"]:
                    raise ValueError(f"Evolution version outside module scope: {stage['stage_id']}")
                if not set(evolution["event_ids"]) <= event_ids:
                    raise ValueError(f"Unknown event in module evolution: {stage['stage_id']}")
        for control in module["controls"]:
            for evidence in control["evidence"]:
                if evidence["event_id"] not in event_ids:
                    raise ValueError(f"Unknown event in audit control: {control['control_id']}")
            for evolution in control["evolution"]:
                if evolution["version_id"] not in module["version_ids"]:
                    raise ValueError(f"Control evolution outside module scope: {control['control_id']}")
                if not set(evolution["event_ids"]) <= event_ids:
                    raise ValueError(f"Unknown event in control evolution: {control['control_id']}")
        for edge in module["edges"]:
            if edge["from"] not in stage_ids or edge["to"] not in stage_ids:
                raise ValueError(f"Unknown stage in module edge: {module['module_id']}")
        for ref in iter_artifact_refs(module):
            if ref.startswith("git:"):
                continue
            if not (REPO_ROOT / ref).exists():
                raise ValueError(f"Missing module artifact: {ref}")
        if module["status"] == "complete":
            if set(module["version_ids"]) != version_ids:
                raise ValueError(f"Complete module lacks version coverage: {module['module_id']}")
            for stage in module["stages"]:
                evolution_versions = {item["version_id"] for item in stage["evolution"]}
                if evolution_versions != version_ids:
                    raise ValueError(f"Complete stage lacks version evolution: {stage['stage_id']}")
            for control in module["controls"]:
                evolution_versions = {item["version_id"] for item in control["evolution"]}
                if evolution_versions != version_ids:
                    raise ValueError(f"Complete control lacks version evolution: {control['control_id']}")

    timeline_versions = set()
    timeline_ids = set()
    for timeline in query_timeline["timelines"]:
        if timeline["timeline_id"] in timeline_ids:
            raise ValueError(f"Duplicate timeline id: {timeline['timeline_id']}")
        timeline_ids.add(timeline["timeline_id"])
        timeline_versions.add(timeline["version_id"])
        annotations = {item["event_id"]: item for item in timeline["annotations"]}
        if len(annotations) != len(timeline["annotations"]):
            raise ValueError(f"Duplicate timeline annotation: {timeline['timeline_id']}")
        for event_id, annotation in annotations.items():
            if event_id not in event_ids:
                raise ValueError(f"Unknown timeline event: {event_id}")
            event = next(event for event in all_events if event["event_id"] == event_id)
            if timeline["version_id"] not in event["version_ids"]:
                raise ValueError(f"Timeline event has wrong version: {event_id}")
            if not set(annotation["module_ids"]) <= module_ids:
                raise ValueError(f"Unknown module in timeline annotation: {event_id}")
        for edge in timeline["causal_edges"]:
            if edge["from_event_id"] not in annotations or edge["to_event_id"] not in annotations:
                raise ValueError(f"Timeline edge endpoint is not annotated: {timeline['timeline_id']}")
            from_event = next(event for event in all_events if event["event_id"] == edge["from_event_id"])
            to_event = next(event for event in all_events if event["event_id"] == edge["to_event_id"])
            if str(from_event["times"]["source_recorded_at"] or "") > str(to_event["times"]["source_recorded_at"] or ""):
                raise ValueError(f"Reverse-time causal edge: {timeline['timeline_id']}")
        for ref in iter_artifact_refs(timeline):
            if ref.startswith("git:"):
                continue
            if not (REPO_ROOT / ref).exists():
                raise ValueError(f"Missing timeline artifact: {ref}")
    if query_timeline["coverage"]["annotated_versions"] != len(timeline_versions):
        raise ValueError("Timeline annotated version count mismatch")
    if query_timeline["status"] == "complete" and (
        timeline_versions != version_ids or not query_timeline["coverage"]["complete"]
    ):
        raise ValueError("Complete timeline lacks full version coverage")

    reviewed = sum(
        event["privacy"]["review_status"] == "reviewed" for event in all_events
    )
    redacted = sum(
        event["privacy"]["publication"] == "redacted" for event in all_events
    )
    print(
        f"PASS: {len(all_events)} events, {len(event_ids)} unique ids, "
        f"{reviewed} privacy-reviewed, {redacted} redacted, "
        f"{len(version_ids)} versions, {len(modules)} modules, "
        f"{len(query_timeline['timelines'])} annotated timelines"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
