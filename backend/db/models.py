#models.py
#database tables

from datetime import datetime
from . import db

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(10))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    IP = db.Column(db.String(15))
    Port = db.Column(db.Integer)
    description = db.Column(db.Text)
