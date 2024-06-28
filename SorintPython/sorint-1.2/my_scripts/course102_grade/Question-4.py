import os

def check_command_usage(commands):
    history_file = os.path.expanduser('~/.bash_history')
    used_commands = {cmd: False for cmd in commands}

    try:
        with open(history_file, 'r') as file:
            history_lines = file.readlines()

        for line in history_lines:
            for cmd in commands:
                if cmd in line:
                    used_commands[cmd] = True

        all_used = True
        for cmd, used in used_commands.items():
            if used:
                print(f"\033[92mGood Work on using the {cmd} command.\033[0m")
            else:
                print(f"You didn't use the {cmd} command.")
                all_used = False

        if all_used:
            print("\033[92mAll necessary commands to control processes are used. Thank you for paying attention.\033[0m")
    except FileNotFoundError:
        print(f"History file {history_file} not found.")

def grade():
    commands_to_check = ['kill', 'ps', 'grep']
    check_command_usage(commands_to_check)

if __name__ == "__main__":
    grade()
