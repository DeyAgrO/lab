import os
import random

def generate_random_file(filename):
    min_size = 1 * 1024 * 1024  # 1 MB
    max_size = 24 * 1024 * 1024 # 24 MB
    file_size = random.randint(min_size, max_size)
    file_path = os.path.join(os.path.expanduser("~"), "manage", f"random_file_{filename}.txt")
    with open(file_path, "wb") as f:
        f.write(os.urandom(file_size))
    return file_path

def main(args):
    if len(args) < 2 or args[1] != "start":
        print("Usage: python script.py start <course_name>")
        return 1

    course_name = args[2] if len(args) > 2 else ""
    if course_name == "files101":
        print("Starting Linux 101 course")

        # Create a Directory manage ----101-START-----
        print("Creating Home a Manage Directory")
        manage_dir = os.path.join(os.path.expanduser("~"), "manage")
        os.makedirs(manage_dir, exist_ok=True)

        # Creating Files a Directory manage ----102-START-----
        print("Creating Random Files")
        for i in range(1, 16):
            generate_random_file(str(i))
    elif course_name == "python101":
        print("Starting Python 101 course")
        # Add the course-specific logic for starting the Python 101 course
        print("Running Python 101 course startup tasks...")
    else:
        print("Usage: python script.py start <course_name>")
        return 1

    return 0

if __name__ == "__main__":
    import sys
    exit_code = main(sys.argv)
    sys.exit(exit_code)
