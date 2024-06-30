#!/bin/bash

# Update the package manager
sudo dnf update -y

# Upgrade the system
sudo dnf upgrade -y

# Install the packages
sudo dnf install vim-enhanced firewalld net-tools qemu-guest-agent openssh-server git curl wget python3 pip -y

# install needed python Models
pip install psutil
pip install termcolor

# Disable SELinux
sudo sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config

echo "Packages installed successfully!"
echo "SELinux has been disabled."

# Reboot the system
echo "Powering Off the system in 20 seconds..."
sleep 20
sudo poweroff
