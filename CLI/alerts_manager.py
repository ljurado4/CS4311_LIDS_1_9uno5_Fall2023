from Alerts import Alerts


class AlertManager:

    sharedAlerts = []

    def __init__(self):
        self.alerts = []

    def create_alert(self, level, time, IP, Port, description):
        alert = Alerts(level, time, IP, Port, description)
        self.alerts.append(alert)
        self.sharedAlerts.append(alert)

    def get_alerts(self):
        return self.alerts