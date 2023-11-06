##################################################################
# File: db_utils.py
#
# Version: [5.0]
#
# Description: 
# This module serves as a utility script for database operations
# specific to the Alert model within the application. It provides
# functions to add new alerts to the database, retrieve all alerts,
# and get a specific alert by its ID. The functions abstract and
# encapsulate direct interactions with the database via SQLAlchemy
# ORM, offering a simplified interface for performing CRUD operations
# on Alert entities.
#
# Modification History:
# [11/02/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Implement the 'add_alert' function to add a new alert to the database.
# - [Task 2]: Implement the 'get_all_alerts' function to retrieve all alerts from the database.
# - [Task 3]: Implement the 'get_alert_by_id' function to fetch a single alert by its unique identifier.
# - [Task 4]: Ensure proper error handling and transaction management within database operations.
# - [Task 5]: Write unit tests for each utility function to validate functionality and data integrity.
# - [Task 6]: Document each function with appropriate docstrings detailing parameters, return values, and any exceptions raised.
# - [Task 7]: Optimize queries to ensure efficient data retrieval, especially for the 'get_all_alerts' function.
#
##################################################################


from . import db
from .models import Alert

def add_alert(level, IP, Port, description):
    alert = Alert(level=level, IP=IP, Port=Port, description=description)
    db.session.add(alert)
    db.session.commit()

def get_all_alerts():
    return Alert.query.all()

def get_alert_by_id(alert_id):
    return Alert.query.get(alert_id)
