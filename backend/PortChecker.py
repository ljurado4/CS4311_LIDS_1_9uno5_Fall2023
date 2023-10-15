#PortChecker.py

class portDetection:
    def __init__(self):
        self.connection_count = {}

    def update_connection_count(self, ip, port, threshold):
        key = f"{ip}:{port}"
        if key in self.connection_count:
            self.connection_count[key] += 1
            if self.connection_count[key] > threshold:
                return True
        else:
            self.connection_count[key] = 1
        return False
