##################################################################
# File: alerts.py
#
# Version: [5.0]
#
# Description: 
# This module defines the Alerts class which represents an alert
# generated in response to network traffic events. It includes
# detailed information such as time, identifier, level, source and
# destination IPs and ports, type of alert, and a description.
#
# Modification History:
# [11/02/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Implement the __init__ constructor with all parameters
#             that define an alert.
# - [Task 2]: Create a __str__ method to provide a formatted string
#             representation of the Alert instance for easy logging
#             and debugging.
# - [Task 3]: Implement serialization methods to convert alert objects
#             to and from a format that can be stored or transmitted.
# - [Task 4]: Add validation to the input data to ensure that the Alert
#             objects are created with consistent and valid data.
# - [Task 5]: Document the class and methods, explaining the role of each
#             attribute and how the class should be utilized in the system.
# - [Task 6]: Create unit tests to validate the functionality of the Alerts class.
# - [Task 7]: Consider integrating the Alerts class with a notification system
#             to alert system administrators when a new alert is generated.
# - [Task 8]: Optimize the class to handle a large number of instances efficiently,
#             especially if used in a high-traffic network environment.
#
##################################################################


class Alerts:
    def __init__(self, time, identifier, level, sourceIP, sourcePort,destIP,destPort,typeAlert,description):
        self.time = time
        self.identifier = identifier
        self.level = level
        self.sourceIP = sourceIP
        self.sourcePort = sourcePort
        self.destIP = destIP
        self.destPort = destPort
        self.typeAlert = typeAlert
        self.description = description
    
    def __str__(self):
        return f"Time: {self.time}, identifier: {self.identifier}, Level: {self.level}, SourceIP: {self.sourceIP}, SourcePort: {self.sourcePort}, DestinationIP: {self.destIP}, DestinationPort: {self.destPort}, Type of Alert: {self.typeAlert}, Description: {self.description}"