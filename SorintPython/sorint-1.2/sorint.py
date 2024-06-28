#!/usr/bin/env python3

import sys
import os
import subprocess

# Determine the script directory
script_dir = os.path.dirname(os.path.realpath(__file__))
scripts_path = os.path.join(script_dir, '..', 'share', 'sorint', 'my_scripts')
sys.path.append(scripts_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: sorint <command> <course>")
        sys.exit(1)

    command = sys.argv[1]
    course = sys.argv[2]

    if command == "start":
        subprocess.run(["python3", os.path.join(scripts_path, "start.py"), course])
    elif command == "grade":
        subprocess.run(["python3", os.path.join(scripts_path, "grade.py"), course])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
