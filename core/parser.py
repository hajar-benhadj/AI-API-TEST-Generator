import json
import os

class SwaggerParser:
    def __init__(self, swagger_path):
        self.swagger_path = swagger_path

    def parse_endpoints(self):
        """
        Reads the Swagger/OpenAPI JSON file and extracts all available 
        paths, HTTP methods, and summaries to be used for test generation.
        """
        if not os.path.exists(self.swagger_path):
            print(f"❌ Swagger file not found at path: {self.swagger_path}")
            return []

        try:
            with open(self.swagger_path, 'r', encoding='utf-8') as f:
                swagger_data = json.load(f)

            endpoints = []
            paths = swagger_data.get("paths", {})
            
            # Iterate through paths and methods to map endpoints
            for path, methods in paths.items():
                for method, details in methods.items():
                    endpoints.append({
                        "path": path,
                        "method": method.upper(),
                        "summary": details.get("summary", "")
                    })
            
            return endpoints

        except Exception as e:
            print(f"❌ An error occurred while parsing the Swagger file: {e}")
            return []