import os
import pwd
import grp

def check_directory_ownership(directory, expected_owner, expected_group):
    try:
        stat_info = os.stat(directory)
        owner = pwd.getpwuid(stat_info.st_uid).pw_name
        group = grp.getgrgid(stat_info.st_gid).gr_name

        if owner == expected_owner and group == expected_group:
            print(f"\033[92mThe directory '{directory}' exists and belongs to user '{owner}' and group '{group}'.\033[0m")
            return True
        elif owner != expected_owner:
            print(f"\033[91mError: The directory '{directory}' does not belong to user '{expected_owner}'.\033[0m")
            return False
        else:
            print(f"\033[91mError: The directory '{directory}' does not belong to group '{expected_group}'.\033[0m")
            return False
    except FileNotFoundError:
        print(f"\033[91mError: The directory '{directory}' does not exist.\033[0m")
        return False

def check_symlink_exists(source, target):
    try:
        if os.path.islink(source) and os.readlink(source) == target:
            print(f"\033[92mThe symbolic link '{source}' -> '{target}' exists.\033[0m")
            return True
        else:
            print(f"\033[91mError: The symbolic link '{source}' -> '{target}' does not exist.\033[0m")
            return False
    except FileNotFoundError:
        print(f"\033[91mError: The directory '{source}' does not exist.\033[0m")
        return False

def grade():
    if check_directory_ownership("/partage", "tester1", "sorint"):
        check_symlink_exists("/partage", "/tmp/shared")

if __name__ == "__main__":
    grade()