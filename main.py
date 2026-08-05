import os
from core.parser import SwaggerParser
from core.ai_generator import AITestGenerator
from core.executor import TestExecutor

def main():
    print("🏁 Starting the automated API testing and generation system...")
    
    # 1. Define the path to the Swagger sample JSON file
    swagger_file = "samples/sample_swagger.json"
    
    # 2. Parse the Swagger file to extract actual endpoints and methods
    parser = SwaggerParser(swagger_file)
    endpoints = parser.parse_endpoints()
    
    if not endpoints:
        print("❌ No endpoints found in the Swagger file.")
        return
        
    print(f"✅ Successfully extracted {len(endpoints)} endpoints from the Swagger file.")

    # 3. Generate Pytest test cases using AI / template generation
    generator = AITestGenerator()
    test_code = generator.generate_tests(endpoints)
    
    if not test_code:
        print("❌ Failed to generate test code.")
        return

    # 4. Save the generated test code into the 'generated_tests' folder
    os.makedirs("generated_tests", exist_ok=True)
    output_file = "generated_tests/test_generated_api.py"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(test_code)
        
    print(f"✅ Test file successfully created at: {output_file}")
    
    # NOTE FOR USERS: 
    # To run these tests successfully using pytest, make sure your actual 
    # backend server is running locally (e.g., at http://localhost:5000), 
    # otherwise you will get a connection refused error.
    print("ℹ️ Note: Ensure your actual backend server is running before executing pytest.")

if __name__ == "__main__":
    main()