import pyshark
from datetime import datetime

"""
NOTE: Used Python 3.11 because interpreter could 
not resolve the pyshark import

NOTE: For pyshark utilization
With Python311 and Python311\Scripts in PATH, use 'pip install pyshark'

"""
class PackTime:
    packet_list = []

    def __init__(self):
        self.pack_time = None

    def display_pack_times(self):
        print(self.packet_list)

    def add_packets(self,capture_limit):

        capture = pyshark.LiveCapture()
        max_cap = capture_limit
        packets_captured = 0

        for in_packet in capture.sniff_continuously():
            time = datetime.now()
            time = time.strftime("%Y-%m-%d %H:%M:%S.%f")
            if 'IP' in in_packet:
                src = in_packet.ip.src
                dst = in_packet.ip.dst

                if 'TCP' in in_packet:
                    protocol = 'TCP'
                    packet_length = int(in_packet.length)
                    flags = in_packet.tcp.flags

                    if 'SYN' in flags:
                        description = 'TCP Handshake SYN'
                    else:
                        description = 'Other TCP Packet'
                elif 'UDP' in in_packet:
                    protocol = 'UDP'
                    packet_length = int(in_packet.length)
                    description = 'UDP Packet'
                elif 'ICMP' in in_packet:
                    protocol = 'ICMP'
                    packet_length = int(in_packet.length)
                    description = 'ICMP Packet'
                else:
                    protocol = 'Other'
                    packet_length = int(in_packet.length)
                    description = "Unknown/Other Protocol"
                tempPackTimeDict = {
                    "Time": time,
                    "Source": src,
                    "Destination": dst,
                    "Protocol": protocol,
                    "Length": packet_length,
                    "Description": description
                }
            #PackTime.add_pack_time(tempPackTimeDict)
            self.packet_list.append(tempPackTimeDict)
            packets_captured += 1

            if packets_captured >= max_cap:
                return self.packet_list
                




