# File: models.py
#
# Description: This class is designed to manage and create alerts within a system and has some logging functionality.
#
# @ Modifier: Lizbeth Jurado
# @ Modifier: Sandra Barbra
# @ Modifier:Tomas Sandoval

from datetime import datetime
from . import db

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(10))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    IP = db.Column(db.String(15))
    Port = db.Column(db.Integer)
    description = db.Column(db.Text)
