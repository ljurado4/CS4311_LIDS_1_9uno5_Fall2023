##################################################################
# File: packet_analyzer.py
#
# Version: [5.0]
#
# Description: 
# This module defines the PacketAnalyzer class which is responsible
# for analyzing network packets. It leverages other modules such as
# ipChecker, alerts_manager, loginCheck, and PortChecker to detect
# anomalies such as failed login attempts, port scans, and unauthorized
# IP addresses.
#
# Modification History:
# [11/02/23] - [5.0] - [Lizbeth Jurado] - [File Description and Organization Set Up]
#
# Tasks:
# - [Task 1]: Instantiate necessary classes for IP checking, alert management,
#             port scanning, and login attempts detection.
# - [Task 2]: Develop the analyze_packet method to orchestrate the detection
#             mechanisms and respond to different packet anomalies.
# - [Task 3]: Implement a method for IP address validation against a whitelist.
# - [Task 4]: Implement a method for detecting port scans and classifying them
#             based on predefined thresholds.
# - [Task 5]: Implement a method for detecting failed login attempts across
#             different protocols such as SSH, FTP, and RDP.
# - [Task 6]: Create a method to generate alerts based on the detected anomalies
#             and pass them to the AlertManager.
# - [Task 7]: Handle packet data extraction and encapsulation to include in alerts.
# - [Task 8]: Document each method and their interaction within the system for
#             clarity and maintainability.
# - [Task 9]: Ensure that time comparison logic is accurate and accounts for
#             network delays and timezone differences.
# - [Task 10]: Implement comprehensive error handling and validation to ensure
#              robustness against malformed packets and unexpected input.
# - [Task 11]: Optimize performance for real-time packet analysis in high traffic
#              environments.
# - [Task 12]: Write unit tests for each component of the packet analysis to
#              ensure reliability.
# - [Task 13]: Create an integration test to simulate real network traffic and
#              validate the overall system behavior.
#
##################################################################
from . import ipChecker, alerts_manager, loginCheck, PortChecker
from datetime import datetime

class PacketAnalyzer:
    def __init__(self):
        self.packetAnalyzer = None
        self.iC = ipChecker.ip_Checker()
        self.getAlerts = alerts_manager.AlertManager()
        self.portCheck = PortChecker.PortDetection()

    def analyze_packet(self, packet, time, identifier, sourceIP, sourcePort,destIP,destPort):
        # Check for each error 
        if self.login_attempts(packet) == True:
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

    def login_attempts(self, packet):
         if 'SSH' or 'FTP' or 'RDP' in packet:
            return True

    def create_alert(self, packet, time, identifier, level, sourceIP, sourcePort,destIP,destPort,typeAlert,description):
        # Capture PCAP data as a string from the packet
        pcap_data = str(packet)
        # Call the AlertsManager class to create an alert
        self.getAlerts.create_alert(pcap_data,time, identifier, level, sourceIP, sourcePort,destIP,destPort,typeAlert,description)
        self.getAlerts.ident_list(pcap_data, identifier)
        alerts = self.getAlerts.get_alerts()
