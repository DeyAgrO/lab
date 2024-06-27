#!/usr/bin/env python3

import sys
from my_scripts.start import run_scripts
from my_scripts.grade import grade_course

def main():
    if len(sys.argv) < 3:
        print("Usage: sorint <start|grade> <argument>")
        return

    command = sys.argv[1]
    argument = sys.argv[2]

    if command == "start":
        run_scripts(argument)
    elif command == "grade":
        grade_course(argument)
    else:
        print("Invalid command. Please use 'start', 'grade', or 'finish'.")

if __name__ == "__main__":
    main()