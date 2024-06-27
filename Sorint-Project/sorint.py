#!/usr/bin/env python3

import sys
from my_scripts.start import run_start
from my_scripts.grade import run_grade

def main():
    if len(sys.argv) < 3:
        print("Usage: sorint <start|grade|finish> <argument>")
        return

    command = sys.argv[1]
    argument = sys.argv[2]

    if command == "start":
        run_start(argument)
    elif command == "grade":
        run_grade(argument)
    else:
        print("Invalid command. Please use 'start', 'grade', or 'finish'.")

if __name__ == "__main__":
    main()