"""Tests for docker-compose.yml (YAML if available, else text checks)."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_compose_file():
    path = ROOT / "docker-compose.yml"
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
    except ImportError:
        # No PyYAML here — plain text checks are enough for this file.
        assert "shop-app:" in text
        assert "build:" in text
        assert "Dockerfile" in text
        return
    data = yaml.safe_load(text)
    service = data["services"]["shop-app"]
    assert service["build"]["context"] == "."
    assert service["build"]["dockerfile"] == "Dockerfile"
