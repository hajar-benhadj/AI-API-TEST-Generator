from ai_api_test_gen import __version__
from ai_api_test_gen.cli import main

SAMPLE_SPEC = """{
  "openapi": "3.0.0",
  "info": {"title": "Demo", "version": "1.0.0"},
  "paths": {
    "/users": {
      "get": {"summary": "Get all users"},
      "post": {"summary": "Create a user"}
    }
  }
}
"""


def test_cli_generates_test_file(tmp_path):
    spec = tmp_path / "spec.json"
    spec.write_text(SAMPLE_SPEC, encoding="utf-8")
    out_dir = tmp_path / "out"

    exit_code = main([str(spec), "-o", str(out_dir), "-b", "https://api.test"])

    assert exit_code == 0
    generated = (out_dir / "test_generated_api.py").read_text(encoding="utf-8")
    assert 'BASE_URL = "https://api.test"' in generated
    assert "def test_get_users():" in generated
    assert "def test_post_users():" in generated


def test_cli_fails_cleanly_when_spec_has_no_endpoints(tmp_path):
    spec = tmp_path / "empty.json"
    spec.write_text('{"openapi": "3.0.0", "paths": {}}', encoding="utf-8")

    assert main([str(spec), "-o", str(tmp_path / "out")]) == 1


def test_cli_fails_cleanly_when_spec_is_missing(tmp_path):
    assert main([str(tmp_path / "ghost.json"), "-o", str(tmp_path / "out")]) == 1


def test_package_exports_version():
    assert isinstance(__version__, str)
