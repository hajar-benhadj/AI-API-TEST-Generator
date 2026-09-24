"""Command-line interface for AI API Test Generator."""

import argparse
import os
import sys

from ai_api_test_gen.ai_generator import AITestGenerator
from ai_api_test_gen.executor import TestExecutor
from ai_api_test_gen.parser import SwaggerParser


def build_arg_parser():
    parser = argparse.ArgumentParser(
        prog="ai-api-test-gen",
        description="Parse a Swagger/OpenAPI spec and generate a pytest test suite for it.",
    )
    parser.add_argument(
        "spec",
        nargs="?",
        default="samples/sample_swagger.json",
        help="Path to a Swagger/OpenAPI JSON or YAML file (default: samples/sample_swagger.json)",
    )
    parser.add_argument(
        "-o", "--output-dir",
        default="generated_tests",
        help="Directory where the generated test file is written (default: generated_tests)",
    )
    parser.add_argument(
        "-b", "--base-url",
        default="http://localhost:5000",
        help="Base URL the generated tests will call (default: http://localhost:5000)",
    )
    parser.add_argument(
        "--run",
        action="store_true",
        help="Run the generated suite with pytest right after generating it",
    )
    return parser


def main(argv=None):
    """Generate a pytest suite from a spec. Returns a process exit code."""
    args = build_arg_parser().parse_args(argv)

    print("🏁 Starting the automated API testing and generation system...")

    parser = SwaggerParser(args.spec)
    endpoints = parser.parse_endpoints()
    if not endpoints:
        print("❌ No endpoints found in the Swagger file.")
        return 1

    print(f"✅ Successfully extracted {len(endpoints)} endpoints from the Swagger file.")

    generator = AITestGenerator()
    test_code = generator.generate_tests(endpoints, base_url=args.base_url)
    if not test_code:
        print("❌ Failed to generate test code.")
        return 1

    os.makedirs(args.output_dir, exist_ok=True)
    output_file = os.path.join(args.output_dir, "test_generated_api.py")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(test_code)
    print(f"✅ Test file successfully created at: {output_file}")

    if args.run:
        executor = TestExecutor(output_file)
        return 0 if executor.run_tests() else 1

    print("ℹ️ Note: Ensure your actual backend server is running before executing pytest.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
