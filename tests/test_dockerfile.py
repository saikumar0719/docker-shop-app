"""Tests for the Dockerfile, Jenkinsfile and scripts (text checks)."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
SECRET_PATTERNS = [r"AKIA[0-9A-Z]{16}", r"BEGIN PRIVATE KEY", r"password\s*="]


def test_dockerfile_basics():
    text = (ROOT / "Dockerfile").read_text(encoding="utf-8")
    first_real_line = next(
        line for line in text.splitlines() if line.strip() and not line.strip().startswith("#")
    )
    assert first_real_line.startswith("FROM python"), "Dockerfile must start with FROM python"
    assert "COPY" in text, "Dockerfile must COPY the app"
    assert "CMD" in text, "Dockerfile must have a CMD to run the app"
    assert "python:3.11" in text


def test_image_tag_matches_everywhere():
    tag = "shop-app:1.0.0"
    for rel in ("Jenkinsfile", "scripts/build_image.sh", "scripts/run_app.sh"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert tag in text, f"{rel} must use the image tag {tag}"


def test_jenkinsfile_has_build_docker_image_stage_after_test():
    text = (ROOT / "Jenkinsfile").read_text(encoding="utf-8")
    assert "stage('Test')" in text
    assert "stage('Build Docker image')" in text
    assert text.index("stage('Test')") < text.index("stage('Build Docker image')"), (
        "Build Docker image must come after Test, so a failed test stops the build"
    )


def test_no_secrets_in_repo_text_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in {".py", ".md", ".sh", ".yml", ".txt"}:
            if ".git" in path.parts:
                continue
            if path.name == "test_dockerfile.py":
                # Skip this file itself: it holds the pattern list used
                # for the scan, so scanning it would always match.
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in SECRET_PATTERNS:
                assert not re.search(pattern, text), f"secret pattern in {path}"
