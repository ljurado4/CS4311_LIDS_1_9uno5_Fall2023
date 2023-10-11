
class Alerts:
    def __init__(self, level, time, IP, description, Port = 0):
        self.level = level
        self.time = time
        self.IP = IP
        self.port = Port
        self.description = description

    def to_dict(self,alert):
        alertDict = {
            "Level":alert.level,
            "Time":alert.time,
            "": alert.IP,
            "": alert.port,
            "": alert.description,
        }
        return alertDict
    