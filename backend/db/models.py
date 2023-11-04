##################################################################
# File: models.py
#
# Version: [5.0]
#
# Description: 
# This module defines the data models for the application, specifically
# the Alert model. The Alert model captures the essential fields needed
# to represent an alert, such as its severity level, timestamp, associated
# IP, port, and a description of the alert. It leverages the SQLAlchemy ORM
# for interaction with the application's database.
#
# Modification History:
# [11/02/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Define the Alert class with SQLAlchemy, including the appropriate fields and types.
# - [Task 2]: Ensure the 'time' field is set to the current UTC time by default when an alert is created.
# - [Task 3]: Add validation constraints to the model fields where appropriate (e.g., length validators for strings).
# - [Task 4]: Write documentation strings for the model, describing the purpose of each field.
# - [Task 5]: Implement any necessary methods within the Alert model for typical operations (e.g., serializing for API responses).
# - [Task 6]: Set up database migration scripts for the Alert model to manage schema changes.
# - [Task 7]: Create unit tests to verify the Alert model's interaction with the database (CRUD operations).
# - [Task 8]: Review and optimize index usage for the model's fields to improve query performance.
#
##################################################################


from datetime import datetime
from . import db

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(10))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    IP = db.Column(db.String(15))
    Port = db.Column(db.Integer)
    description = db.Column(db.Text)
