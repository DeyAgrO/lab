#!/bin/bash

# Update the package manager
sudo dnf update -y

# Upgrade the system
sudo dnf upgrade -y

# Install the packages
sudo dnf install vim-enhanced firewalld net-tools qemu-guest-agent openssh-server git curl wget python3 python3-pip nano openssh-client -y

# install needed python Models
pip install psutil
pip install termcolor

# Remove SSH host keys
sudo rm -rf /etc/ssh/ssh_host_*

# Disable SELinux
sudo sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config

echo "Packages installed successfully!"
echo "SELinux has been disabled."
echo "Keys Has been removed."

# Reboot the system
echo "Power Off the system in 20 seconds..."
sleep 20
sudo poweroff
