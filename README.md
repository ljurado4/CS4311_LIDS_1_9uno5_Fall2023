# CS4311_LIDS_Team1_9uno5_Fall2023

## LIDS (Local Intrusion Detection System)

### Description
LIDS is a Local Intrusion Detection System designed to monitor network activity and alert administrators of any suspicious actions. Built with Python and Flask, the system features a CLI and a Web UI for easy configuration and monitoring.

### Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
   - [CLI](#cli)
   - [Web UI](#web-ui)

### Installation

#### Prerequisites
- Ensure `install.sh` has execution permissions:
```
chmod +x install.sh
```

#### Automated Installation
The installation script (`install.sh`) is provided in the root of this project to simplify installation. This script sets up the virtual environment, installs the necessary dependencies, and prepares the system for running this code.

1. Clone the repository to your local machine:
```
git clone https://github.com/ljurado4/CS4311_LIDS_19uno5_Fall2023.git
```
2. Navigate to the project directory:
```
cd CS4311_LIDS_19uno5_Fall2023
```
3. Run `install.sh`:
```
./install.sh
```

#### Manual Steps Required
- In case the script fails to install Wireshark or set permissions for `dumpcap`, please run the following commands:
```
sudo apt-get install -y wireshark
sudo chmod +s /usr/bin/dumpcap
```

#### Activate the Virtual Environment Manually
If `install.sh` is unable to recognize the OS of your machine, activate the virtual environment manually:
- On Windows (using CMD):
```
.\env\Scripts\activate.bat
```
- On macOS or Linux:
```
source env/bin/activate
```

### Usage

#### CLI
To interact with LIDS via CLI, navigate to the CLI folder and run:
```
python3 main_cli.py --config_file=your_config.xml
```


#### Web UI
Once the environment is active:
1. Navigate to the project folder.
2. Start the Flask server:
```
python app.py
```
3. Access the Web UI by navigating to `http://127.0.0.1:5000` in your web browser.