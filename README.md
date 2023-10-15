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

2. Navigate to the project directory.


3. **Set Up a Virtual Environment**:
   - Install `virtualenv`:
pip3 install virtualenv

   - Create a new environment:
virtualenv env

4. **Install Flask and Required Packages**:
   - Install Flask:
pip3 install flask

   - Install Flask-CORS:
pip3 install flask-cors

   - Install other required packages for the project:
pip3 install -r requirements.txt

   - Install the Flask-SQLAlchemy package:

pip3 install Flask-SQLAlchemy
pip3 install Flask-Migrate

5. **Install Pyshark**:
   - Install Pyshark:
pip3 install pyshark

6. **Activate the virtual environment**:
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
2. Start the Flask server by running `app.py`. (FYI macOS will require you to still run python3)

python3 app.py
=======

Once the server is running, access the Web UI by navigating to `http://127.0.0.1:5000` in your web browser.

#### Database Setup and Migration with Flask

**Installation:**
1. Install Flask-Migrate and Flask-SQLAlchemy: These tools help manage and migrate the database schema.
pip3 install Flask-Migrate Flask-SQLAlchemy

**Configuration:**
Ensure you've set up your app's configuration to use the desired database. For instance, for SQLite in the `app.py` file:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lids.db'

**Usage:**
1. Initialize the Migration Environment:
If you're setting up migrations for the first time, you need to initialize the migration environment. This will create a migrations folder which will contain versions of schema changes.
flask db init

2. Generate a Migration Script:
After making changes to your model (i.e., the structure of your database tables), you can auto-generate a migration script using the following command:
flask db migrate -m "Your message about the migration"

3. Apply Migrations to the Database:
To update your database schema according to the generated script, run:
flask db upgrade


Install the Flask-SQLAlchemy package:

pip3 install Flask-SQLAlchemy
pip3 install Flask-Migrate