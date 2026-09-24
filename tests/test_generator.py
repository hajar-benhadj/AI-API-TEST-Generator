import re

from ai_api_test_gen.ai_generator import AITestGenerator

ENDPOINTS = [
    {"path": "/users", "method": "GET", "summary": "Get all users"},
    {"path": "/users", "method": "POST", "summary": "Create a user"},
    {"path": "/products/{id}", "method": "GET", "summary": "Get one product"},
]


def test_generated_code_is_valid_python():
    code = AITestGenerator().generate_tests(ENDPOINTS)

    # Raises SyntaxError if the generated suite is not valid Python
    compile(code, "test_generated_api.py", "exec")


def test_one_test_function_per_endpoint():
    code = AITestGenerator().generate_tests(ENDPOINTS)

    assert "def test_get_users():" in code
    assert "def test_post_users():" in code
    assert "def test_get_products_id():" in code


def test_base_url_is_injected():
    code = AITestGenerator().generate_tests(ENDPOINTS, base_url="https://api.example.com")

    assert 'BASE_URL = "https://api.example.com"' in code


def test_default_base_url_is_local():
    code = AITestGenerator().generate_tests(ENDPOINTS)

    assert 'BASE_URL = "http://localhost:5000"' in code


def test_includes_negative_case_and_uses_requests():
    code = AITestGenerator().generate_tests(ENDPOINTS)

    assert "import requests" in code
    assert re.search(r"def test_unknown_endpoint_returns_error\(\):", code)
    assert "requests.get" in code and "requests.post" in code


def test_empty_endpoint_list_still_returns_valid_module():
    code = AITestGenerator().generate_tests([])

    compile(code, "test_generated_api.py", "exec")
    assert "test_unknown_endpoint_returns_error" in code
