
class Alerts:
    def __init__(self, level, time, IP, description, Port = 0):
        self.level = level
        self.time = time
        self.IP = IP
        self.port = Port
        self.description = description
    
    #Used to turn the Alert object into a dictionary
    def to_dict(self,alert):
        alertDict = {
            "Level":alert.level,
            "Time":alert.time,
            "Source": alert.IP,
            "Port": alert.port,
            "Description": alert.description,
        }
        return alertDict
    