from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "projects"

ID_RE = re.compile(r"^(TECH|DEMO|PROD|RES|PLAY)-\d{3,}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

ALLOWED_TYPES = {
    "technical-lab",
    "business-demo",
    "product",
    "research",
    "playground",
}

TYPE_TO_PREFIX = {
    "technical-lab": "TECH",
    "business-demo": "DEMO",
    "product": "PROD",
    "research": "RES",
    "playground": "PLAY",
}

ALLOWED_STATUS = {"idea", "planning", "building", "qa", "published", "archived"}
ALLOWED_VISIBILITY = {"public", "private"}

REQUIRED_FIELDS = {
    "schema_version",
    "id",
    "name",
    "slug",
    "type",
    "domain",
    "areas",
    "status",
    "visibility",
    "purpose",
    "stack",
    "featured",
    "repository",
    "live_demo",
}


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def validate_project(path: Path, errors: list[str]) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, path, f"cannot parse YAML: {exc}")
        return {}

    if not isinstance(data, dict):
        fail(errors, path, "top-level YAML value must be a mapping")
        return {}

    missing = sorted(REQUIRED_FIELDS - data.keys())
    if missing:
        fail(errors, path, f"missing required fields: {', '.join(missing)}")

    project_id = data.get("id")
    project_type = data.get("type")
    slug = data.get("slug")

    if data.get("schema_version") != 1:
        fail(errors, path, "schema_version must be 1")

    if not isinstance(project_id, str) or not ID_RE.fullmatch(project_id):
        fail(errors, path, f"invalid id: {project_id!r}")

    if project_type not in ALLOWED_TYPES:
        fail(errors, path, f"invalid type: {project_type!r}")
    elif isinstance(project_id, str) and project_id.split("-", 1)[0] != TYPE_TO_PREFIX[project_type]:
        fail(errors, path, f"id prefix does not match type {project_type!r}")

    if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
        fail(errors, path, f"invalid slug: {slug!r}; expected lowercase kebab-case")

    if data.get("status") not in ALLOWED_STATUS:
        fail(errors, path, f"invalid status: {data.get('status')!r}")

    if data.get("visibility") not in ALLOWED_VISIBILITY:
        fail(errors, path, f"invalid visibility: {data.get('visibility')!r}")

    for field in ("areas", "purpose", "stack"):
        value = data.get(field)
        if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value):
            fail(errors, path, f"{field} must be a non-empty list of strings")

    if not isinstance(data.get("featured"), bool):
        fail(errors, path, "featured must be true or false")

    repository = data.get("repository")
    if not isinstance(repository, str) or not repository.startswith("https://github.com/"):
        fail(errors, path, "repository must be a GitHub HTTPS URL")

    live_demo = data.get("live_demo")
    if live_demo is not None and (not isinstance(live_demo, str) or not live_demo.startswith(("http://", "https://"))):
        fail(errors, path, "live_demo must be null or an HTTP(S) URL")

    if isinstance(project_id, str) and path.stem != project_id:
        fail(errors, path, f"filename must match id ({project_id}.yaml)")

    return data


def main() -> int:
    errors: list[str] = []
    entries: list[tuple[Path, dict]] = []

    if not PROJECTS_DIR.exists():
        print("projects/ directory does not exist", file=sys.stderr)
        return 1

    for path in sorted(PROJECTS_DIR.glob("*.yaml")):
        data = validate_project(path, errors)
        if data:
            entries.append((path, data))

    if not entries:
        errors.append("registry contains no project entries")

    for field in ("id", "slug", "repository"):
        seen: dict[str, Path] = {}
        for path, data in entries:
            value = data.get(field)
            if not isinstance(value, str):
                continue
            if value in seen:
                errors.append(
                    f"duplicate {field} {value!r}: "
                    f"{seen[value].relative_to(ROOT)} and {path.relative_to(ROOT)}"
                )
            else:
                seen[value] = path

    if errors:
        print("Registry validation failed:\n", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Registry valid: {len(entries)} project(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
