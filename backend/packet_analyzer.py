#packet_analyzer.py

from . import ipChecker,alerts_manager,loginCheck,PortChecker


class PacketAnalyzer:
     
    def __init__(self):
        self.packetAnalyzer = None
        self.iC = ipChecker.ip_Checker()
        self.getAlerts = alerts_manager.AlertManager()
        self.portCheck = PortChecker.portDetection()


    def analyze_packet(self,packet,identifier,time,IP,port):
        # Check for each error 
        if self.login_attempts(self) == True:
            self.create_alert(packet,identifier,3,time,IP,port,"Failed Login Attempts")
            # print("here")
        res = self.port_scan_check(IP,port)
        if res == "threshold2":
            self.create_alert(packet,identifier,3,time,IP,port,"Port Scan")
        elif res == "threshold1":
            self.create_alert(packet,identifier,2,time,IP,port,"Port Scan")
        elif self.ip_check(IP) == False:
            self.create_alert(packet,identifier,1,time,IP,port,"Unknown IP")
            # print("here")

    def ip_check(self,IP):

        return self.iC.ip_in_List(IP)


    def port_scan_check(self,IP,port):

        return self.portCheck.update_connection_count(IP,port,1,2)

    def login_attempts(self,packet):
        return False
    
    def create_alert(self,packet,identifier,lvl,time,IP,port,description):
        # Call the AlertsManager class to create an alert
        self.getAlerts.create_alert(lvl,time,IP,port,description,identifier)
        self.getAlerts.ident_list(packet,identifier)
        alerts = self.getAlerts.get_alerts()
        #for alert in alerts:
         #   print(alert)
