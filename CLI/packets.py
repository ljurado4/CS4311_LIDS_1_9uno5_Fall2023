import pyshark
from datetime import datetime
import threading as th
from threading import Semaphore
import ipChecker
import Alerts

"""
NOTE: Used Python 3.11 because interpreter could 
not resolve the pyshark import

NOTE: For pyshark utilization
With Python311 and Python311\Scripts in PATH, use 'pip install pyshark'

"""
class PackTime:
    packet_list = []
    alert_list = []
    ################
    #Delete when alert logic is ready, only exists to 
    #limit packets for testing
    packets_captured = 0
    #################
    cap_sem = Semaphore(1)
    process_sem = Semaphore(0)

    def __init__(self):
        self.pack_time = None
    """
    create_packet will take in a packet and format the packet to be 
    enqueued to the global list of packets
    """
    def create_packet(self,in_packet):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        if 'IP' in in_packet:
            src = in_packet.ip.src
            dst = in_packet.ip.dst
            if 'TCP' in in_packet:
                protocol = 'TCP'
                flags = in_packet.tcp.flags
                src_port = in_packet.tcp.srcport
                dst_port = in_packet.tcp.dstport
                if 'SYN' in flags:
                    description = 'TCP Handshake SYN'
                else:
                    description = 'Other TCP Packet'
            elif 'UDP' in in_packet:
                src_port = in_packet.tcp.srcport
                dst_port = in_packet.tcp.dstport
                protocol = 'UDP'
                description = 'UDP Packet'
            elif 'ICMP' in in_packet:
                protocol = 'ICMP'
                description = 'ICMP Packet'
            else:
                protocol = 'Other'
                description = "Unknown/Other Protocol"
            packet_length = int(in_packet.length)
            temp_packet_dict = {
                "Time": time,
                "Source": src,
                "Destination": dst,
                "Protocol": protocol,
                "Length": packet_length,
                "Description": description
            }
            self.add_alert(severity= "Medium",time= time,IP = src,Port=dst_port,description = description)
            self.packet_list.append(temp_packet_dict)
        
    """
    packet_handler will dequeue a packet from the list and will use the alert logic
    to analyze the packet and determine if it is an alert
    """
    def packet_handler(self):
        while True:
            self.process_sem.acquire()
            self.cap_sem.acquire()
            if not self.packet_list:
                self.cap_sem.release()
                break
            packet = self.packet_list.pop(0)
            # Add alert detecting logic here
            #Something along the lines of
            #if alertDetector(in_packet):
            #pull packet and move elsewhere
            
            #Check the packet to see if the packet
            not_in_whitelist = ipChecker.ip_Checker.ip_in_List(packet["Source"],packet["Destination"])
            #checks if in_whitelist, then performs something
            if not_in_whitelist:
                #TODO: Do something with the alert
                break
            self.cap_sem.release()
            print("Packet: ", packet)

    """
    Creates alert object and appends to alert_list List
    """
    def add_alert(self,severity, time, IP, Port, description):
        alert_to_add = Alerts(severity, time, IP, Port, description)
        self.alert_list.append(alert_to_add)
    """
    Used as driver code of the class, starts
    sniffing the network using previous classes
    on differing threads
    """
    def run_sniffer(self):
        packet_handler_thread = th.Thread(target=self.packet_handler)

        packet_handler_thread.start()

        for in_packet in self.capture.sniff_continuously():
            self.cap_sem.acquire()
            self.create_packet(in_packet)
            self.process_sem.release()
            #################
            self.packets_captured += 1
            if self.packets_captured >= 5:
                break
            #################
            self.cap_sem.release()


