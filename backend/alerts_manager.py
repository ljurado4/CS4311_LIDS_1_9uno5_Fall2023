# File: alerts_manager.py
#
# Description: This class is designed to manage and create alerts within a system and has some logging functionality.
# 
# @ Author: Alejandro Hernandez
# @ Modifier: Alejandro Hernandez

import logging
from backend import Alerts

class AlertManager:
    sharedAlerts = []
    identifierList = []

    def __init__(self):
        self.alerts = []
# @ Author: Alejandro Hernandez

    def setup_logging(self):
        # Set up logging to a file
        logging.basicConfig(filename='alerts.log', level=logging.INFO)

    #Creates the alerts with given alert data
    def create_alert(self, pcap_data, time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description):

        alert = Alerts.Alerts(time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description)
        alert.PCAPData = pcap_data  # Set the PCAPData property
        self.alerts.append(alert)
        self.sharedAlerts.append(alert)
        
        # Log the alert
        logging.info(f"Alert created: {description} at {time}")
    
# @ Author: Alejandro Hernandez
# Append alerts to identifier list
    def ident_list(self, packet, identifier):
        self.identifierList.append({identifier: [packet]})

# @ Author: Alejandro Hernandez
# Gets all generated alerts
    def get_alerts(self):
        return self.alerts
