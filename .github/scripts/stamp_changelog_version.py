#!/usr/bin/env python3
"""Stamp the top "## Unreleased" CHANGELOG.md entry with a real semver tag and date.

Looks for a heading of the form:
    ## Unreleased — Title of the change
    ## Unreleased (major) — Title of the change

and rewrites it in place to:
    ## vX.Y.Z — YYYY-MM-DD — Title of the change

using the next available tag: MAJOR bumps (resetting MINOR/PATCH to 0) when the
"(major)" marker is present, otherwise MINOR bumps (resetting PATCH to 0). PATCH is
always 0 — reserved, unused for now. If no tag exists yet, the first entry (whether
or not it's marked major) becomes v1.0.0, the baseline.

Writes NEW_VERSION=vX.Y.Z to $GITHUB_ENV when a version was stamped, so the calling
workflow step knows whether to commit and tag. Writes nothing (a no-op) when no
"## Unreleased" heading is found, e.g. a commit that touches CHANGELOG.md for some
other reason (typo fix, reformatting).
"""

import os
import re
import subprocess
import sys
from datetime import datetime, timezone

CHANGELOG_PATH = "CHANGELOG.md"

HEADING_RE = re.compile(
    r"^## Unreleased(?P<major> \(major\))?\s*—\s*(?P<title>.+)$",
    re.MULTILINE,
)


def latest_tag() -> str | None:
    result = subprocess.run(
        ["git", "tag", "-l", "v*.*.*", "--sort=-v:refname"],
        capture_output=True,
        text=True,
        check=True,
    )
    tags = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return tags[0] if tags else None


def next_version(is_major: bool) -> str:
    tag = latest_tag()
    if tag is None:
        # Baseline: the very first tag is v1.0.0, whether or not that first
        # entry happens to be marked (major) — there's nothing to bump from.
        return "v1.0.0"

    major, minor, _patch = (int(part) for part in tag.lstrip("v").split("."))
    if is_major:
        major += 1
        minor = 0
    else:
        minor += 1
    return f"v{major}.{minor}.0"


def main() -> None:
    with open(CHANGELOG_PATH, encoding="utf-8") as f:
        content = f.read()

    match = HEADING_RE.search(content)
    if not match:
        print("No '## Unreleased' entry found — nothing to stamp.")
        return

    is_major = match.group("major") is not None
    title = match.group("title").strip()
    version = next_version(is_major)
    today = datetime.now(timezone.utc).date().isoformat()

    new_heading = f"## {version} — {today} — {title}"
    new_content = content[: match.start()] + new_heading + content[match.end() :]

    with open(CHANGELOG_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Stamped {version} ({today}) for: {title}")

    github_env = os.environ.get("GITHUB_ENV")
    if github_env:
        with open(github_env, "a", encoding="utf-8") as f:
            f.write(f"NEW_VERSION={version}\n")


if __name__ == "__main__":
    sys.exit(main())
