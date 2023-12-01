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

# Check if virtualenv is installed, if not, install it
if command_exists virtualenv ; then
    echo "Virtualenv already installed."
else
    echo "Installing virtualenv..."
    pip3 install virtualenv==20.24.5 --user
fi

# Modifier: Lizbeth Jurado
# Set up virtual environment
echo "Setting up virtual environment..."
virtualenv env

# Activate virtual environment and install dependencies
case "$OSTYPE" in
  linux* | darwin*)
    # For Linux and macOS
    source env/bin/activate
    ;;
  cygwin* | mingw* | msys* | Windows_NT)
    # For Windows (Cygwin, MinGW, etc.)
    .\\env\\Scripts\\activate.bat
    ;;
  *)
    echo "Unknown O.S.: $OSTYPE"
    echo "Activate the virtual environment manually."
    exit 1
    ;;
esac

# Upgrade pip in the virtual environment
echo "Upgrading pip..."
pip install --upgrade pip

# Install Flask and required packages
echo "Installing dependencies..."
pip install flask==3.0.0
pip install flask-cors==4.0.0
pip install pyshark==0.6
pip install python-socketio

# Install tcpdump for Linux and macOS
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    if command_exists tcpdump ; then
        echo "Tcpdump already installed."
    else
        echo "Installing tcpdump, might require sudo access..."
        sudo apt-get install tcpdump
    fi
fi

echo "Installation completed."

# Author: Lizbeth Jurado
# Kill any Python process using port 5000
echo "Ensuring port 5000 is free for LIDS..."
lsof -i :5000 | grep Python | awk '{print $2}' | xargs kill -9

echo "System ready for LIDS."
