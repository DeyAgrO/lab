import os
import importlib
import sys

def run_scripts(course_name):
    """
    Runs all the scripts in the corresponding 'start' directory.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    start_dir = os.path.join(base_dir, f'{course_name}_start')

    if os.path.isdir(start_dir):
        sys.path.append(base_dir)
        for filename in os.listdir(start_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = f'my_scripts.{course_name}_start.{os.path.splitext(filename)[0]}'
                module = importlib.import_module(module_name)
                if hasattr(module, 'main'):
                    module.main()
                else:
                    print(f"No 'main()' function found in {filename}")
    else:
        print(f"Directory '{start_dir}' not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: start.py <course_name>")
        sys.exit(1)

    course_name = sys.argv[1]
    run_scripts(course_name)

if __name__ == "__main__":
    main()
