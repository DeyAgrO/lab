#!/bin/bash


generate_random_file() {
    local min_size=$((1 * 1024 * 1024))  # 1 MB
    local max_size=$((24 * 1024 * 1024)) # 24 MB
    local file_size=$((RANDOM % (max_size - min_size + 1) + min_size))
    local file_path="/home/$(whoami)/manage/random_file_$1.txt"
    head -c $file_size < /dev/urandom > "$file_path"
}


case "$1" in
  "start")
    case "$2" in
      "files101")

        echo "Starting Linux 101 course"

        # Create a Directory manage ----101-START-----
        echo "Creating Home a Manage Directory"
        mkdir /home/$(whoami)/manage

        # Creating Files a Directory manage ----102-START-----
        echo "Creating Random Files"
        for i in {1..15}; do
            generate_random_file "$i"
        done
        ;;
      "python101")
        echo "Starting Python 101 course"
        # Add the course-specific logic for starting the Python 101 course
        echo "Running Python 101 course startup tasks..."
        ;;
      *)
        echo "Usage: lab start <course_name>"
        exit 1
        ;;
    esac
    ;;
