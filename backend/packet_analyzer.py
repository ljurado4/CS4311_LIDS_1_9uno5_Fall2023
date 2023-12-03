# File: packet_analyzer.py
#
# Description: Adds functionality to analyze network packets and manage alerts, now including packet storage capabilities.
#
# @ Author: Alejandro Hernandez
# @ Modifier: Lizbeth Jurado

from . import ipChecker, alerts_manager, loginCheck, PortChecker
from datetime import datetime
import pyshark
import json

class PacketAnalyzer:
    def __init__(self):
        self.loginCheck = loginCheck.LoginCheck()
        self.iC = ipChecker.ip_Checker()
        self.getAlerts = alerts_manager.AlertManager()
        self.portCheck = PortChecker.portDetection()

    # @ Modified for Packet Storage: Lizbeth Jurado
    def analyze_packet(self, packet, time, identifier, sourceIP, sourcePort, destIP, destPort, protocol, handshake, packetList):
        if self.login_attempts(packet, protocol, destPort, time) == True:
            self.create_alert(packet, time, identifier, 3, sourceIP, sourcePort, destIP, destPort, "Failed Login Error", "Multiple failed logins detected")
            self.store_packet_data(packet, identifier)

        if not self.ip_check(sourceIP):
            res = self.port_scan_check(sourceIP, destPort, time, handshake, packetList)
            if res == "threshold1":
                self.create_alert(packet, time, identifier, 2, sourceIP, sourcePort, destIP, destPort, "Port Scan Error", "Port Scan surpassing threshold1")
                self.store_packet_data(packet, identifier)
        elif not self.ip_check(sourceIP):
            self.create_alert(packet, time, identifier, 1, sourceIP, sourcePort, destIP, destPort, "Unknown IP Error", "Source IP detected that is not part of approved IP list")
            self.store_packet_data(packet, identifier)

    # @ Author: Alejandro Hernandez
    def ip_check(self, IP):
        return self.iC.ip_in_List(IP)

    # @ Author: Alejandro Hernandez
    def port_scan_check(self, IP, destPort, time, handshake, packetList):
        threshold1 = 300
        timeAllowed = 700
        timeOF = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
        if handshake:
            return self.portCheck.port_Checking(IP, destPort, timeOF, timeAllowed, threshold1, packetList)
    
    # @ Author: Alejandro Hernandez
    def login_attempts(self, packet, protocol, destPort, time):
        threshold = 700
        timeOF = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
        return self.loginCheck.failedPssWrd(packet, protocol, timeOF, destPort, threshold)

    # @ Author: Alejandro Hernandez
    def create_alert(self, packet, time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description):
        pcap_data = str(packet)
        self.getAlerts.create_alert(pcap_data, time, identifier, level, sourceIP, sourcePort, destIP, destPort, typeAlert, description)
        self.getAlerts.ident_list(pcap_data, identifier)

    # @ Modifier for Packet Storage: Lizbeth Jurado
    def store_packet_data(self, packet_data, identifier):
        # Serialize packet data and save it to a JSON file
        try:
            with open(f'packet_data_{identifier}.json', 'w') as outfile:
                json.dump(packet_data, outfile, indent=4)
        except Exception as e:
            print(f"An error occurred while storing the packet data: {e}")

    # @ Author: Lizbeth Jurado
    def read_pcap(self, pcap_file_path):
        try:
            cap = pyshark.FileCapture(pcap_file_path, only_summaries=True)
            packets_data = []

            for packet in cap:
                packet_dict = {
                    'number': packet.no,
                    'time': packet.time,
                    'source': packet.source,
                    'destination': packet.destination,
                    'protocol': packet.protocol,
                    'length': packet.length,
                    'info': packet.info
                }
                packets_data.append(packet_dict)

            cap.close()
            return packets_data
        except Exception as e:
            print(f"An error occurred while reading the pcap file: {e}")
            return []

    # @ Author: Lizbeth Jurado
    def format_for_frontend(self, packet_data):
        return json.dumps(packet_data, indent=4)
