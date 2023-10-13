#packet_analyser.py

from ipChecker import ip_Checker
from alerts_manager import AlertManager

class PacketAnalyzer:
    def __init__(self, packet, level, time, IP, Port):
        self.packet = packet
        self.level = level
        self.time = time
        self.IP = IP
        self.Port = Port

    def analyze_packet(self):
        # Check for each error 
        if self.ip_check(self.IP) == False:
            self.create_alert("Unknown IP")
        if self.port_scan_check() == True:
            self.create_alert("Port Scan")
        if self.login_attempts() == True:
            self.create_alert("Failed Login Attempts")

    def ip_check(self,IP):
        ip_check = ip_Checker()
        return ip_check.ip_in_list(IP)

    def port_scan_check(self):

        #call port scan check and have it return a boolean indicating if there is an error

        return False 

    def login_attempts(self):
        
        #call login attempts and have it return a boolean indicating if there is an error

        return False  
    
    def create_alert(self,description):
        # Call the AlertsManager class to create an alert
        alerts_manager = AlertManager()
        alerts_manager.create_alert(self.level,self.time,self.IP,self.Port,description)