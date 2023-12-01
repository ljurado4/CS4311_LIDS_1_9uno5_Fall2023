#! /usr/bin/env bash
# File: install.sh
#
# Description: This script sets up the virtual environment, installs the necessary dependencies, and prepares the system for running this code.
#
# @ Author: Raul Tinajero
# @ Modifier:

# Set up virtual environment
pip3 install virtualenv==20.24.5
virtualenv env

# Install Flask and required packages
pip3 install flask = 3.0.0
pip3 install flask-cors==4.0.0

# Install Pyshark
pip3 install pyshark==0.6

# Install SocketIO
pip3 install python-socketio

# Install tcdump using administrator credentials
sudo apt-get install tcpdump

# Activate virtual environment according to O.S.
case "$OSTYPE" in
  linux* | darwin*)
    # For Linux and macOS
    source env/bin/activate;;
  cygwin* | mingw* | msys* | Windows_NT)
    # For Windows (Cygwin, MinGW, etc.)
    .\\env\\Scripts\\activate.bat;;
  *)
  echo "Unknown O.S.: $OSTYPE"
  echo "Activate the virtual environment manually."
  ;;
esac