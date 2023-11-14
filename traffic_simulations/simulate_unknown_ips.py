# File: simulate_unkown_ips.py
#
# Description: 
# This script is intended to simulate network traffic from random IP addresses to a specified destination, typically for the purpose of testing network intrusion detection systems or similar security mechanisms. It generates packets with random source IPs and sends them to a defined destination IP and port. Additionally, it captures live network trafficusing PyShark and allows for the inspection of these packets.
#
# @ Author:
# @ Modified:



from scapy.all import IP, TCP, send, RandIP
import pyshark


def simulate_unknown_ips():
    # change dest to valid agents ip 
    ip_layer = IP(src=RandIP(), dst="192.168.1.136")
    tcp_layer = TCP(dport=80)
    packet = ip_layer/tcp_layer
    send(packet)

def print_packet(packet):
    print(packet)

if __name__ == "__main__":
    # First, set up a live capture. You might need to change the interface.
    capture = pyshark.LiveCapture(interface='\\Device\\NPF_{84CA8BDA-2551-4E90-9BC8-6212F55D9F65}')

    # Send the simulated packet.
    for i in range(100):
        simulate_unknown_ips()

    # Use the packet callback to print captured packets.
    capture.apply_on_packets(print_packet, timeout=30)  # wait for 30 seconds, for example

    
