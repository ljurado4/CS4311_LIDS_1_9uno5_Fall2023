# File: alerts_manager.py
#
# Description: This class is designed to manage and create alerts within a system 
# and has some logging functionality. Now modified to facilitate headless alerts 
# output to the CLI.
# 
# @ Author: Alejandro Hernandez
# @ Modifier: Alejandro Hernandez
# @ Modifier: Lizbeth Jurado 

import logging
from backend import Alerts

class AlertManager:
    sharedAlerts = []
    identifierList = []

    def __init__(self):
        self.alerts = []
        self.setup_logging()

    # @ Modified: Lizbeth Jurado 
    def setup_logging(self):
        # Set up logging to a file with an enhanced format for better readability
        logging.basicConfig(
            filename='alerts.log',
            level=logging.INFO,
            format='%(asctime)s:%(levelname)s:%(message)s'
        )

    # @ Modified: Lizbeth Jurado 
    def create_alert(self, pcap_data, time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description):
        # Create an alert instance with the provided details
        alert = Alerts.Alerts(time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description)
        alert.PCAPData = pcap_data  # Set the PCAPData property
        self.alerts.append(alert)
        self.sharedAlerts.append(alert)
        
        # Log the alert
        logging.info(f"Alert created: {description} at {time}")

        # Handle alert for CLI (headless alert)
        self.handle_cli_alert(alert)

    # @ Added: Lizbeth Jurado 
    def handle_cli_alert(self, alert):
        # Output alert details to console for CLI
        print(f"Headless Alert Generated:\nTime: {alert.time}\nIdentifier: {alert.identifier}\nLevel: {alert.level}\nSource IP: {alert.sourceIP}\nSource Port: {alert.sourcePort}\nDestination IP: {alert.destIP}\nDestination Port: {alert.destPort}\nType: {alert.typeAlert}\nDescription: {alert.description}\n")

    # @ Author: Alejandro Hernandez
    def ident_list(self, packet, identifier):
        # Keep a list of identifiers for each packet
        self.identifierList.append({identifier: [packet]})

    # @ Author: Alejandro Hernandez
    def get_alerts(self):
        # Retrieve the list of generated alerts
        return self.alerts
