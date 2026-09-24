"""Make the src/ package importable when running pytest from a source checkout."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
