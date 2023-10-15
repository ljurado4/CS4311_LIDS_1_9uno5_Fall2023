#packet_analyzer.py

from . import ipChecker,alerts_manager,loginCheck,PortChecker


class PacketAnalyzer:
     
    def __init__(self):
        self.packetAnalyzer = None
        self.iC = ipChecker.ip_Checker()
        self.getAlerts = alerts_manager.AlertManager()
        self.portCheck = PortChecker.portDetection()


    def analyze_packet(self,lvl,time,IP,port):
        # Check for each error 
        if self.ip_check(IP) == False:
            self.create_alert(lvl,time,IP,port,"Unknown IP")
            # print("here")
        if self.port_scan_check(IP,port) == True:
            self.create_alert(lvl,time,IP,port,"Port Scan")
            # print("here")
        if self.login_attempts(self) == True:
            self.create_alert(lvl,time,IP,port,"Failed Login Attempts")
            # print("here")

    def ip_check(self,IP):

        return self.iC.ip_in_List(IP)


    def port_scan_check(self,IP,port):

        return self.portCheck.update_connection_count(IP,port,1)

    def login_attempts(self,packet):
        return False
    
    def create_alert(self,lvl,time,IP,port,description):
        # Call the AlertsManager class to create an alert
        self.getAlerts.create_alert(lvl,time,IP,port,description)
        alerts = self.getAlerts.get_alerts()
        #for alert in alerts:
         #   print(alert)
