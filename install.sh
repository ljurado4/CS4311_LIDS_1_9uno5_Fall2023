#!/usr/bin/env bash
# File: install.sh
#
# Description: Sets up the virtual environment, installs dependencies, prepares the system for running LIDS.
#
# Author: Raul Tinajero
# Modifier: Lizbeth Jurado

# Function to check if a command exists
command_exists() {
    type "$1" &> /dev/null ;
}

echo "Starting installation..."

# Check and install Python3 and Pip3
if command_exists python3 && command_exists pip3 ; then
    echo "Python3 and Pip3 already installed."
else
    echo "Installing Python3 and Pip3..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi

# Install Python3 venv
echo "Installing python3-venv..."
sudo apt-get install -y python3-venv

# Check if virtualenv is installed, if not, install it
if command_exists virtualenv ; then
    echo "Virtualenv already installed."
else
    echo "Installing virtualenv..."
    pip3 install virtualenv --user
fi

echo "Setting up virtual environment..."
python3 -m venv env

# Activate virtual environment and install dependencies
source env/bin/activate

# Upgrade pip in the virtual environment
echo "Upgrading pip..."
pip install --upgrade pip

# Install Flask and required packages
echo "Installing Python dependencies..."
pip install flask==3.0.0
pip install flask-cors==4.0.0
pip install flask_socketio
pip install pyshark==0.6
pip install python-socketio

echo "Installation completed."

# Kill any Python process using port 5000
echo "Ensuring port 5000 is free for LIDS..."
lsof -i :5000 | grep Python | awk '{print $2}' | xargs -r kill -9

echo "System ready for LIDS."
