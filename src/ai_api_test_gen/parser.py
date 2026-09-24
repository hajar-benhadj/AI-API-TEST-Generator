import json
import os

# HTTP methods that can appear under a path in an OpenAPI document. Keys such
# as "parameters" or "servers" also live there and must not become endpoints.
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}


class SwaggerParser:
    def __init__(self, swagger_path):
        self.swagger_path = swagger_path

    def _load_spec(self):
        """Load the spec as a dict, supporting both JSON and YAML files."""
        with open(self.swagger_path, "r", encoding="utf-8") as f:
            content = f.read()

        if self.swagger_path.lower().endswith((".yaml", ".yml")):
            import yaml

            return yaml.safe_load(content)

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            # Some specs use a .json extension but contain YAML; fall back.
            import yaml

            return yaml.safe_load(content)

    def parse_endpoints(self):
        """
        Reads a Swagger/OpenAPI file (JSON or YAML) and extracts all available
        paths, HTTP methods, and summaries to be used for test generation.
        """
        if not os.path.exists(self.swagger_path):
            print(f"❌ Swagger file not found at path: {self.swagger_path}")
            return []

        try:
            swagger_data = self._load_spec()
            if not isinstance(swagger_data, dict):
                raise ValueError("spec root must be a mapping")

            endpoints = []
            paths = swagger_data.get("paths", {})

            # Iterate through paths and methods to map endpoints
            for path, methods in paths.items():
                if not isinstance(methods, dict):
                    continue
                for method, details in methods.items():
                    if method.lower() not in HTTP_METHODS:
                        continue
                    endpoints.append({
                        "path": path,
                        "method": method.upper(),
                        "summary": details.get("summary", "") if isinstance(details, dict) else "",
                    })

            return endpoints

        except Exception as e:
            print(f"❌ An error occurred while parsing the Swagger file: {e}")
            return []
