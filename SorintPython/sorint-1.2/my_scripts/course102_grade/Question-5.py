import os
import subprocess

def check_known_hosts():
    known_hosts_path = os.path.expanduser('~/.ssh/known_hosts')
    try:
        with open(known_hosts_path, 'r') as file:
            lines = file.readlines()
        return len(lines) > 1
    except FileNotFoundError:
        return False

def check_ssh_keys():
    ssh_dir = os.path.expanduser('~/.ssh/')
    private_key = os.path.join(ssh_dir, 'sorintKey')
    public_key = os.path.join(ssh_dir, 'sorintKey.pub')
    return os.path.isfile(private_key) and os.path.isfile(public_key)

def check_ssh_copy_id_used():
    history_file = os.path.expanduser('~/.bash_history')
    try:
        with open(history_file, 'r') as file:
            history_lines = file.readlines()
        return any('ssh-copy-id' in line for line in history_lines)
    except FileNotFoundError:
        return False

def grade():
    known_hosts_ok = check_known_hosts()
    ssh_keys_ok = check_ssh_keys()
    ssh_copy_id_ok = check_ssh_copy_id_used()

    if known_hosts_ok and ssh_keys_ok and ssh_copy_id_ok:
        print("\033[92mYou have completed the SSH steps correctly.\033[0m")
    else:
        if not known_hosts_ok:
            print("\033[91mYou don't have more than one entry in known_hosts.\033[0m")
        if not ssh_keys_ok:
            print("\033[91mYou don't have the sorintKey and sorintKey.pub files.\033[0m")
        if not ssh_copy_id_ok:
            print("\033[91mYou didn't use the ssh-copy-id command.\033[0m")

if __name__ == "__main__":
    grade()
