import os
import sys

# Simply used to add the root directory to the current system path for testing.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


pytest_plugins = [
    "tests.fixtures",
]
