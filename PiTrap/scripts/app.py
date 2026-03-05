#!/bin/bash

echo "Installing PiTrap dependencies..."

sudo apt update
sudo apt install python3 python3-pip git tcpdump -y

pip3 install -r requirements.txt

echo "Installation completed."