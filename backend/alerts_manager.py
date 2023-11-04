##################################################################
# File: alerts_manager.py
#
# Version: [5.0]
#
# Description: # This module is responsible for managing alert objects within the application.
# It provides functionality to create alerts, manage a shared list of alerts,
# and keep a list of identifiers related to alert events. It interacts with
# the Alerts module to instantiate and populate alert objects based on
# network traffic data.
#
# Modification History:
# [11/02/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Implement the `create_alert` method that takes traffic data and
#             initializes alert objects, adding them to the alerts lists.
# - [Task 2]: Develop the `ident_list` method to maintain a mapping of identifiers
#             to packets, aiding in the correlation of alerts.
# - [Task 3]: Add a method to retrieve all current alerts.
# - [Task 4]: Ensure thread safety when accessing and modifying sharedAlerts list.
# - [Task 5]: Write unit tests for each method in AlertManager.
# - [Task 6]: Optimize the storage and retrieval mechanism of alerts to handle
#             high throughput and avoid memory issues.
# - [Task 7]: Document the usage and functionality of each method within AlertManager.
# - [Task 8]: Integrate AlertManager with the rest of the backend components,
#             ensuring alerts are processed and managed correctly in the application's workflow.
#
##################################################################


from backend import Alerts

class AlertManager:
    sharedAlerts = []
    identifierList = []

    def __init__(self):
        self.alerts = []

    def create_alert(self, pcap_data, time, identifier, level, sourceIP, sourcePort,destIP,destPort,typeAlert,description):
        alert = Alerts.Alerts(time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description)
        alert.PCAPData = pcap_data  # Set the PCAPData property
        self.alerts.append(alert)
        self.sharedAlerts.append(alert)
    
    def ident_list(self, packet, identifier):
        self.identifierList.append({identifier: [packet]})

    def get_alerts(self):
        return self.alerts
