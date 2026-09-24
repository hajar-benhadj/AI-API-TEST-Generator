import json

import pytest

from ai_api_test_gen.parser import SwaggerParser

SPEC = {
    "openapi": "3.0.0",
    "info": {"title": "Demo", "version": "1.0.0"},
    "paths": {
        "/users": {
            "get": {"summary": "Get all users"},
            "post": {"summary": "Create a user"},
            "parameters": [{"name": "x", "in": "query", "schema": {"type": "string"}}],
        },
        "/products": {"get": {"summary": "Get products"}},
    },
}


@pytest.fixture
def spec_json(tmp_path):
    path = tmp_path / "spec.json"
    path.write_text(json.dumps(SPEC), encoding="utf-8")
    return str(path)


def test_extracts_endpoints_with_uppercase_methods(spec_json):
    endpoints = SwaggerParser(spec_json).parse_endpoints()

    assert {e["method"] for e in endpoints} == {"GET", "POST"}
    assert len(endpoints) == 3
    users_get = next(e for e in endpoints if e["path"] == "/users" and e["method"] == "GET")
    assert users_get["summary"] == "Get all users"


def test_ignores_non_http_keys_under_a_path(spec_json):
    endpoints = SwaggerParser(spec_json).parse_endpoints()

    # "parameters" is shared metadata for /users, not an endpoint of its own
    assert not any(e["method"] == "PARAMETERS" for e in endpoints)


def test_missing_file_returns_empty_list(tmp_path):
    endpoints = SwaggerParser(str(tmp_path / "nope.json")).parse_endpoints()

    assert endpoints == []


def test_malformed_file_returns_empty_list(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("{definitely not json", encoding="utf-8")

    assert SwaggerParser(str(path)).parse_endpoints() == []


def test_yaml_spec_is_supported(tmp_path):
    path = tmp_path / "spec.yaml"
    path.write_text(
        """
openapi: 3.0.0
info:
  title: Demo
  version: 1.0.0
paths:
  /orders:
    get:
      summary: Get orders
    delete:
      summary: Delete an order
""",
        encoding="utf-8",
    )
    endpoints = SwaggerParser(str(path)).parse_endpoints()

    assert {e["method"] for e in endpoints} == {"GET", "DELETE"}
