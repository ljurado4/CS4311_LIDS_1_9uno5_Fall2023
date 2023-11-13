from . import ipChecker, alerts_manager, loginCheck, PortChecker
from datetime import datetime

class PacketAnalyzer:
    def __init__(self):
        self.packetAnalyzer = None
        self.iC = ipChecker.ip_Checker()
        self.getAlerts = alerts_manager.AlertManager()
        self.portCheck = PortChecker.portDetection()
        self.loginChecker = loginCheck.LoginCheck()

    def analyze_packet(self, packet, time, identifier, sourceIP, sourcePort,destIP,destPort,protocol):
        # Check for each error 
        if self.login_attempts(packet,protocol,destPort) == True:
            self.create_alert(packet, time, identifier, 3, sourceIP, sourcePort,destIP,destPort,"Failed Login Error","Multiple failed logins detected")
        res = self.port_scan_check(sourceIP, destPort, time)
        if res == "threshold2":
            self.create_alert(packet, time, identifier, 3, sourceIP, sourcePort,destIP,destPort,"Port Scan Error","Port Scan surpassing threshold2")
        elif res == "threshold1":
            self.create_alert(packet, time, identifier, 2, sourceIP, sourcePort,destIP,destPort,"Port Scan Error","Port Scan surpassing threshold1")
        elif self.ip_check(sourceIP) == False:
            self.create_alert(packet, time, identifier, 1, sourceIP, sourcePort,destIP,destPort,"Unknown IP Error","Source IP detected that is not appart of approved IP list")

    def ip_check(self, IP):
        return self.iC.ip_in_List(IP)

    def port_scan_check(self, IP, destPort, time):
        threshold1 = -1
        threshold2 = 0
        timeAllowed = 700
        timeOF = datetime.strptime(time,"%Y-%m-%d %H:%M:%S.%f")
        return self.portCheck.port_Checking(IP, destPort, timeOF, timeAllowed, threshold1, threshold2)

    def login_attempts(self, packet,protocol,time,destPort):
        timeAllowed = 700
        timeOF = datetime.strptime(time,"%Y-%m-%d %H:%M:%S.%f")
        return self.loginChecker.failedPssWrd(protocol,timeOF,timeAllowed,destPort)

    def create_alert(self, packet, time, identifier, level, sourceIP, sourcePort,destIP,destPort,typeAlert,description):
        # Capture PCAP data as a string from the packet
        pcap_data = str(packet)
        # Call the AlertsManager class to create an alert
        self.getAlerts.create_alert(pcap_data,time, identifier, level, sourceIP, sourcePort,destIP,destPort,typeAlert,description)
        self.getAlerts.ident_list(pcap_data, identifier)
        alerts = self.getAlerts.get_alerts()
