# File: __init__.py
#
# Description: Sets up the necessary tools for working with databases in a Flask web application
#
# @ Author: Lizbeth Jurado
# @ Modifier: 

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
