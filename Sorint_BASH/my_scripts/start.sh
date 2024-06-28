#!/bin/bash

# Function to run scripts in the 'start' directory
run_scripts() {
    local course_name="$1"
    local start_dir="my_scripts/${course_name}_start"
    
    if [ -d "$start_dir" ]; then
        for file in "$start_dir"/*.sh; do
            if [ -f "$file" ]; then
                echo "Running script: $file"
                "$file"
            fi
        done
    else
        echo "Directory '$start_dir' not found."
    fi
}

# Check if the correct number of arguments are provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <course_name>"
    exit 1
fi

# Get the course name from the command line argument
course_name="$1"

# Call the run_scripts function
run_scripts "$course_name"
