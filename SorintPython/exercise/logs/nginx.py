import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command {command}: {e.stderr}")

def install_nginx():
    run_command("sudo yum install -y epel-release")
    run_command("sudo yum install -y nginx")

def configure_nginx_logging():
    config_lines = [
        "error_log /var/log/nginx/error.log;"
    ]
    config_file = "/etc/nginx/nginx.conf"
    with open(config_file, "a") as file:
        file.write("\n".join(config_lines) + "\n")

def misconfigure_nginx():
    # Adding an invalid configuration directive
    error_line = "invalid_directive;"
    config_file = "/etc/nginx/nginx.conf"
    with open(config_file, "a") as file:
        file.write(f"\n{error_line}\n")

def start_nginx():
    run_command("sudo systemctl daemon-reload")
    run_command("sudo systemctl restart nginx")

if __name__ == "__main__":
    install_nginx()
    configure_nginx_logging()
    misconfigure_nginx()
    start_nginx()