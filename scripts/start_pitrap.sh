#!/bin/bash

echo "Starting PiTrap..."

python3 collectors/network_sniffer.py &
python3 dashboard/app.py &