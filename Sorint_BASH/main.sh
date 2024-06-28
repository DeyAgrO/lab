#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <start|grade> <argument>"
    exit 1
fi

# Get the command and argument from the command line
command="$1"
argument="$2"

# Execute the appropriate function based on the command
case "$command" in
    "start")
        ./my_scripts/start.sh "$argument"
        ;;
    "grade")
        ./my_scripts/grade.sh "$argument"
        ;;
    *)
        echo "Invalid command. Please use 'start', 'grade', or 'finish'."
        exit 1
        ;;
esac
