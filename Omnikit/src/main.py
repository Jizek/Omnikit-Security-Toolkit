#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Omnikit Security Toolkit - Main Launcher
"""

import os
import sys

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read version
version_file = os.path.join(script_dir, "..", "surum.txt")
with open(version_file, 'r') as f:
    surum = f.read().strip()

# Path to the main program
main_program = os.path.join(script_dir, f"omnikittoolsv{surum}.py")

# Platform-agnostic Python command
python_cmd = sys.executable

# Run the main program
os.system(f'"{python_cmd}" "{main_program}"')