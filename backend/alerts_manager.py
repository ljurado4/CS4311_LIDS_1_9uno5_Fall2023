# alerts_manager.py
import logging
from backend import Alerts

class AlertManager:
    sharedAlerts = []
    identifierList = []

    def __init__(self):
        self.alerts = []

    def setup_logging(self):
        # Set up logging to a file
        logging.basicConfig(filename='alerts.log', level=logging.INFO)

    def create_alert(self, pcap_data, time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description):
        alert = Alerts.Alerts(time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description)
        alert.PCAPData = pcap_data  # Set the PCAPData property
        self.alerts.append(alert)
        self.sharedAlerts.append(alert)
        
        # Log the alert
        logging.info(f"Alert created: {description} at {time}")
    
    def ident_list(self, packet, identifier):
        self.identifierList.append({identifier: [packet]})

    def get_alerts(self):
        return self.alerts
