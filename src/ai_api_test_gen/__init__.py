"""AI API Test Generator — turn a Swagger/OpenAPI spec into a pytest suite."""

from ai_api_test_gen.parser import SwaggerParser
from ai_api_test_gen.ai_generator import AITestGenerator
from ai_api_test_gen.executor import TestExecutor

__version__ = "0.1.0"

__all__ = ["SwaggerParser", "AITestGenerator", "TestExecutor", "__version__"]
