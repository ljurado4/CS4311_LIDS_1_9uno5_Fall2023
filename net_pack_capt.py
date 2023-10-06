import pyshark
from datetime import datetime

class PackTime:
    packet_list = []

    def __init__(self, target_ip, threshold):
        self.target_ip = target_ip
        self.threshold = threshold
        self.scanned_ports = {}

    def display_pack_times(self):
        for packet in self.packet_list:
            print(f"Time: {packet['Time']}")
            print(f"Source: {packet['Source']}")
            print(f"Destination: {packet['Destination']}")
            print(f"Protocol: {packet['Protocol']}")
            print(f"Length: {packet['Length']}")
            print(f"Description: {packet['Description']}")
            print("-" * 50)  # Add a separator for readability

    def process_packet(self, pkt):
        time = datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S.%f")

        if 'IP' in pkt:
            src = pkt.ip.src
            dst = pkt.ip.dst

            if 'TCP' in pkt:
                protocol = 'TCP'
                packet_length = int(pkt.length)
                flags = pkt.tcp.flags

                if 'SYN' in flags:
                    description = 'TCP Handshake SYN'
                    self.port_scan_callback(pkt)
                else:
                    description = 'Other TCP Packet'
            elif 'UDP' in pkt:
                protocol = 'UDP'
                packet_length = int(pkt.length)
                description = 'UDP Packet'
            elif 'ICMP' in pkt:
                protocol = 'ICMP'
                packet_length = int(pkt.length)
                description = 'ICMP Packet'
                self.ping_sweep_callback(pkt)
            else:
                protocol = 'Other'
                packet_length = int(pkt.length)
                description = "Unknown/Other Protocol"

            tempPackTimeDict = {
                "Time": time,
                "Source": src,
                "Destination": dst,
                "Protocol": protocol,
                "Length": packet_length,
                "Description": description
            }

            self.packet_list.append(tempPackTimeDict)

    def add_packets(self, capture_limit):
        capture = pyshark.LiveCapture()
        max_cap = capture_limit
        packets_captured = 0

        traffic_capture = pyshark.LiveCapture(interface="eth0")

        for in_packet in capture.sniff_continuously():
            self.process_packet(in_packet)
            packets_captured += 1

            if packets_captured >= max_cap:
                return self.packet_list

    def port_scan_callback(self, pkt):
        if "IP" in pkt and "TCP" in pkt:
            src_ip = pkt.ip.src
            dst_ip = pkt.ip.dst
            dst_port = int(pkt.tcp.dstport)

            if dst_ip == self.target_ip:
                if src_ip not in self.scanned_ports:
                    self.scanned_ports[src_ip] = [dst_port]
                else:
                    if dst_port - 1 not in self.scanned_ports[src_ip]:
                        self.scanned_ports[src_ip].append(dst_port)
                    else:
                        print(f"Port scan detected from {src_ip} to port {dst_port - 1}!")

    def ping_sweep_callback(self, pkt):
        if "ICMP" in pkt:
            print(f"Potential ping sweep detected from {pkt['IP'].src} to {pkt['IP'].dst}.")

# Usage
target_ip = "192.168.1.100"
threshold = 1000
# ho ho ho
capture_limit = 100

pack_time_obj = PackTime(target_ip, threshold)
packet_list = pack_time_obj.add_packets(capture_limit)
pack_time_obj.display_pack_times()
