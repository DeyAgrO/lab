import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError:
        pass

def install_httpd():
    run_command("sudo yum install -y httpd")

def misconfigure_httpd():
    error_line = "ErrorDirective InvalidDirective"
    config_file = "/etc/httpd/conf/httpd.conf"
    with open(config_file, "a") as file:
        file.write(f"\n{error_line}\n")

def start_httpd():
    run_command("sudo systemctl start httpd")

if __name__ == "__main__":
    install_httpd()
    misconfigure_httpd()
    start_httpd()
