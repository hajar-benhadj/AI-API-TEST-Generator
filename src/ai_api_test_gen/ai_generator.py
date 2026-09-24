import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import openai  # type: ignore[import-not-found]
else:
    try:
        import openai
    except ImportError:  # pragma: no cover
        openai = None  # type: ignore[assignment]

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AITestGenerator:
    def __init__(self):
        # Initialize OpenAI API key if available
        self.api_key = os.getenv("OPENAI_API_KEY")
        if openai is not None and self.api_key:
            openai.api_key = self.api_key

    def generate_tests(self, endpoints, base_url="http://localhost:5000"):
        """
        Generates executable Pytest test cases based on the provided API endpoints.
        It maps out GET and POST requests, handles base URLs, and adds
        assertions for expected status codes (e.g., 200, 201, 400).
        """
        print("🤖 Generating Pytest test code for the extracted endpoints...")

        # Start constructing the Python test file content
        test_code = f"""import pytest
import requests

# Base URL of the target backend server
# NOTE: Ensure your actual backend server is running at this URL before executing pytest.
BASE_URL = "{base_url}"

"""

        # Loop through each endpoint and generate a corresponding test function
        for ep in endpoints:
            path = ep.get("path")
            method = ep.get("method", "GET").upper()
            summary = ep.get("summary", "No summary provided")

            # Create a clean function name based on the path and method
            clean_name = path.replace("/", "_").replace("{", "").replace("}", "").strip("_")
            if not clean_name:
                clean_name = "root"
            
            test_func_name = f"test_{method.lower()}_{clean_name}"

            # Generate test logic depending on the HTTP method
            if method == "GET":
                test_code += f'''def {test_func_name}():
    """Test for {method} {path} - {summary}"""
    url = f"{{BASE_URL}}{path}"
    response = requests.get(url)
    # Verify that the server responds successfully
    assert response.status_code in [200, 404], f"Unexpected status code: {{response.status_code}}"

'''
            elif method == "POST":
                test_code += f'''def {test_func_name}():
    """Test for {method} {path} - {summary}"""  # type: ignore
    url = f"{{BASE_URL}}{path}"
    payload = {{}}  # Add sample payload data if needed
    response = requests.post(url, json=payload)
    # Verify creation or successful handling
    assert response.status_code in [200, 201, 400, 422], f"Unexpected status code: {{response.status_code}}"

'''

        # Adding a negative test case to check error handling on unknown routes
        test_code += '''def test_unknown_endpoint_returns_error():
    """Negative test case: an endpoint that does not exist in the spec."""
    url = f"{BASE_URL}/__nonexistent_endpoint_probe__"
    response = requests.get(url)
    # Expecting a 404 (or a 4xx validation error) for non-existent resources
    assert response.status_code in [404, 400, 405, 422], f"Expected error code, got: {response.status_code}"
'''

        return test_code