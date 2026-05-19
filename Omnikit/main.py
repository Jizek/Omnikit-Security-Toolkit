import os
import sys

srum = open("surum.txt")
surum = srum.read().strip()

# Platform-agnostic Python command
python_cmd = sys.executable
os.system(f"{python_cmd} omnikittoolsv{surum}.py")