#alerts.py

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