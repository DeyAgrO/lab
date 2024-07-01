import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError:
        pass

def install_mysql():
    run_command("sudo yum install -y mysql-server")

def configure_mysql_logging():
    config_lines = [
        "[mysqld]",
        "log-error=/var/log/mysql/mysqld.log"
    ]
    config_file = "/etc/my.cnf"
    with open(config_file, "a") as file:
        file.write("\n".join(config_lines) + "\n")

def misconfigure_mysql():
    error_line = "invalid_option"
    config_file = "/etc/my.cnf"
    with open(config_file, "a") as file:
        file.write(f"\n{error_line}\n")

def create_log_directory():
    run_command("sudo mkdir -p /var/log/mysql")
    run_command("sudo chown mysql:mysql /var/log/mysql")
    run_command("sudo chmod 755 /var/log/mysql")

def start_mysql():
    run_command("sudo systemctl daemon-reload")
    run_command("sudo systemctl restart mysqld")

if __name__ == "__main__":
    install_mysql()
    create_log_directory()
    configure_mysql_logging()
    misconfigure_mysql()
    start_mysql()