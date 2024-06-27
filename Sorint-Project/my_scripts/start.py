import os
import importlib

def run_scripts(course_name):
    """
    Runs all the scripts in the corresponding 'start' directory.
    """
    start_dir = os.path.join('my_scripts', f'{course_name}_start')
    if os.path.isdir(start_dir):
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