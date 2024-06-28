#!/bin/bash

# Function to check the exam directories
grade() {
    local user="$USER"
    local txt_dir="/home/$user/exam/txt"
    local mp4_dir="/home/$user/exam/mp4"
    local mp3_dir="/home/$user/exam/mp3"

    if [ -d "$txt_dir" ]; then
        echo -e "\e[92mThe directory '$txt_dir' exists.\e[0m"
    else
        echo -e "\e[91mThe directory '$txt_dir' does not exist.\e[0m"
    fi

    if [ -d "$mp4_dir" ]; then
        echo -e "\e[92mThe directory '$mp4_dir' exists.\e[0m"
    else
        echo -e "\e[91mThe directory '$mp4_dir' does not exist.\e[0m"
    fi

    if [ -d "$mp3_dir" ]; then
        echo -e "\e[92mThe directory '$mp3_dir' exists.\e[0m"
    else
        echo -e "\e[91mThe directory '$mp3_dir' does not exist.\e[0m"
    fi

    if [ -d "$txt_dir" ] && [ -d "$mp4_dir" ] && [ -d "$mp3_dir" ]; then
        return 0
    else
        return 1
    fi
}

# Call the check_exam_directories function
grade