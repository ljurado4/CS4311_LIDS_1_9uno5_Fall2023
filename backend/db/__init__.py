##################################################################
# File: __init__.py
#
# Version: [5.0]
#
# Description: 
# This file serves as the initialization script for a Python package,
# commonly found at the root of a project directory. In this specific
# instance, the script is configured to initialize database components
# for a web application using Flask. It sets up SQLAlchemy for ORM-based
# database interactions and Flask-Migrate for handling database migrations.
#
# Modification History:
# [11/02/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Import the necessary modules for database operations (SQLAlchemy and Migrate).
# - [Task 2]: Create an instance of the SQLAlchemy class to handle ORM operations.
# - [Task 3]: Create an instance of the Migrate class to handle database migrations.
# - [Task 4]: Ensure these instances are accessible for the application package to facilitate
#             database operations throughout the application.
# - [Task 5]: Integrate these instances with the Flask application object as required in
#             other modules or when initializing the application.
# - [Task 6]: Document the process of how to perform database migrations within the application.
# - [Task 7]: Ensure the compatibility of database components with the rest of the application
#             architecture.
#
##################################################################

# Initialize our database and migration capabilities
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
