#!/bin/bash

# Update the package manager
sudo dnf update -y

# Upgrade the system
sudo dnf upgrade -y

# Install the packages
sudo dnf install vim-enhanced firewalld net-tools qemu-guest-agent openssh-server git curl wget -y

# Disable SELinux
sudo sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config

echo "Packages installed successfully!"
echo "SELinux has been disabled."

# Reboot the system
echo "Rebooting the system in 20 seconds..."
sleep 20
sudo reboot