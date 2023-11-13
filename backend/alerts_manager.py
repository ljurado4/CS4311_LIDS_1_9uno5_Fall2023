# alerts_manager.py

from backend import Alerts

class AlertManager:
    sharedAlerts = []
    identifierList = []

    def __init__(self):
        self.alerts = []

    #Author Alejandro Hernandez
    
    def create_alert(self, pcap_data, time, identifier, level, sourceIP, sourcePort,destIP,destPort,typeAlert,description):
        alert = Alerts.Alerts(time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description)
        alert.PCAPData = pcap_data  # Set the PCAPData property
        self.alerts.append(alert)
        self.sharedAlerts.append(alert)
    
    #Author Alejandro Hernandez
    
    def ident_list(self, packet, identifier):
        self.identifierList.append({identifier: [packet]})

    #Author Alejandro Hernandez
    
    def get_alerts(self):
        return self.alerts
