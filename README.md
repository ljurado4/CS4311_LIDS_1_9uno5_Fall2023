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
4. [Troubleshooting](#troubleshooting)
5. [Contributing](#contributing)

---

### Installation

1. Clone the repository to your local machine.
    ```
    git clone https://github.com/ljurado4/CS4311_LIDS_19uno5_Fall2023.git
    ```
2. Navigate to the project directory.
    ```
    cd CS4311_LIDS_19uno5_Fall2023
    ```
3. Set Up a Virtual Environment
    ```
    * Install virtualenv
      pip3 install virtualenv
    * Create a new enviroment
      virtualenv env
    * Activate the virtual enviroment
      *On Windows using CMD
        .\env\Scripts\activate.bat
      * On Mac or Linux
        source env/bin/activate



    ```
3. Install Flask and Required Packages.
    ```
    pip install -r requirements.txt
    * Install Flask
      pip3 install flask

    ```
---

### Usage

#### CLI

To interact with LIDS via CLI, navigate to the CLI folder and run the following command:

```bash
python3 main_cli.py --config_file=your_config.xml
```

#### Web UI

Start the Flask server by navigating to the `DB` folder and running:

```bash
python3 server.py
```

Once the server is running, access the Web UI by navigating to `http://127.0.0.1:5000` in your web browser.


### Troubleshooting

For more help, please open an issue in the GitHub repository.

---

### Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request.

