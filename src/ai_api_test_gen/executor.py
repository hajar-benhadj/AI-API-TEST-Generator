import subprocess
import os

class TestExecutor:
    def __init__(self, test_file_path):
        self.test_file_path = test_file_path

    def run_tests(self):
        """
        Executes the generated pytest test file automatically 
        and reports whether the API endpoints pass or fail.
        Requires a live running server to successfully pass requests.
        """
        if not os.path.exists(self.test_file_path):
            print(f"❌ Test file does not exist: {self.test_file_path}")
            return False

        print(f"🚀 Running tests from file: {self.test_file_path} ...")
        # Run pytest with verbose mode
        result = subprocess.run(["pytest", self.test_file_path, "-v"])
        
        return result.returncode == 0