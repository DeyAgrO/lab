import os
import importlib

def grade_course(course_name):
    """
    Runs all the scripts in the corresponding 'grade' directory and reports the results.
    """
    grade_dir = os.path.join('my_scripts', f'{course_name}_grade')
    if os.path.isdir(grade_dir):
        for filename in os.listdir(grade_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = f'my_scripts.{course_name}_grade.{os.path.splitext(filename)[0]}'
                module = importlib.import_module(module_name)
                if hasattr(module, 'grade'):
                    try:
                        module.grade()
                        print(f"\033[33m'{filename}' graded Finished.\033[0m")
                    except Exception as e:
                        print(f"\033[31m'{filename}' failed to grade: {e}\033[0m")
                else:
                    print(f"\033[33mNo 'grade()' function found in '{filename}'\033[0m")
    else:
        print(f"Directory '{grade_dir}' not found.")

def main():
    # Grade the courses
    grade_course("course101")
    grade_course("course102")
    grade_course("course103")

if __name__ == "__main__":
    main()