#alerts.py

class Alerts:
    def __init__(self, level, time, IP, Port, description):
        self.level = level
        self.time = time
        self.IP = IP
        self.Port = Port
        self.description = description