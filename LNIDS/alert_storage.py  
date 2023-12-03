# File: alerts_manager.py
#
# Description: 
# 
# @Author : Lizbeth Jurado 

import sys
import os
from datetime import datetime
import json

# Change the sys.path to import the Alerts class from the parent 'backend' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from backend.Alerts import Alerts

class AlertsStorage:
    def __init__(self, storage_directory):
        self.storage_directory = storage_directory
        if not os.path.exists(self.storage_directory):
            os.makedirs(self.storage_directory)

    def store_alert(self, alert):
        if not isinstance(alert, Alerts):
            raise ValueError("Expected an instance of Alerts")
        
        alert_dict = alert.__dict__  # Convert the alert object to a dictionary for JSON serialization
        filename = f"alert_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.storage_directory, filename)
        
        with open(filepath, 'w') as file:
            json.dump(alert_dict, file, indent=4)
        
        print(f"Alert stored: {filepath}")
