# CS4311_LIDS_Team1_9uno5_Fall2023

CS4311 Software Engineering: Design and Implementation Team 1 9UNO 5

LIDS (Local Intrusion Detection System)

### Description

LIDS is a Local Intrusion Detection System designed to monitor network activity and alert administrators of any suspicious actions. Built with Python and Flask, the system features a CLI and a Web UI for easy configuration and monitoring.

### Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [CLI](#cli)
   - [Web UI](#web-ui)
   - [Database Setup and Migration with Flask](#database-setup-and-migration-with-flask)
3. [Troubleshooting](#troubleshooting)
4. [Contributing](#contributing)

---

### Installation

1. Clone the repository to your local machine.
git clone https://github.com/ljurado4/CS4311_LIDS_19uno5_Fall2023.git



3. **Prerequisites**:
   - Ensure you have Python installed 3.10.12 installed
     ```
     python --version  # Check your current Python version
 
     ```

3. Navigate to the project directory.

4. **Set Up a Virtual Environment**:
   - Install `virtualenv`:
pip3 install virtualenv==20.24.5

   - Create a new environment:
virtualenv env

5. **Install Flask and Required Packages**:
   - Install Flask:
pip3 install Flask==3.0.0

   - Install Flask-CORS:
pip3 install flask-cors==4.0.0

6. **Install Pyshark**:
   - Install Pyshark:
pip3 install pyshark==0.6

7. **Install python-socketio**:
   - Install SocketIO:
pip3 install pip3 install python-socketio

7. **Install Pyshark**:
   - Install Pyshark:
pip3 install pyshark==0.6

8. **Install tcpdump**:
   - Install tcpdump:
sudo apt-get install tcpdump


7. **Activate the virtual environment**:
   - On Windows using CMD:
.\env\Scripts\activate.bat

   - On Mac or Linux:
source env/bin/activate

---

### Usage

#### CLI

To interact with LIDS via CLI, navigate to the CLI folder and run the following command:
python3 main_cli.py --config_file=your_config.xml

#### Web UI

Once the environment is active:
1. Navigate to the project folder.
2. Start the Flask server by running `python app.py`. (FYI macOS will require you to still run python3)


Once the server is running, access the Web UI by navigating to `http://127.0.0.1:5000` in your web browser.
