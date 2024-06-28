#!/bin/bash

# Function to grade a course
grade_course() {
    local course_name="$1"
    local grade_dir="my_scripts/${course_name}_grade"

    if [ -d "$grade_dir" ]; then
        for file in "$grade_dir"/*.sh; do
            if [ -f "$file" ] && [ "$(basename "$file")" != "__init__.py" ]; then
                script_name="${file%.*}"
                script_name="${script_name#*/}"
                if [ "$(type -t grade)" = "function" ]; then
                    set +e
                    grade
                    if [ $? -eq 0 ]; then
                        echo -e "\e[33m'$(basename "$file")' graded Finished.\e[0m"
                    else
                        echo -e "\e[31m'$(basename "$file")' failed to grade: $?\e[0m"
                    fi
                    set -e
                else
                    echo -e "\e[33mNo 'grade()' function found in '$(basename "$file")'\e[0m"
                fi
            fi
        done
    else
        echo "Directory '$grade_dir' not found."
    fi
}
